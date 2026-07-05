# polling.4

`polling` — 设备轮询支持

## 名称

`polling`

## 概要

`options DEVICE_POLLING`

## 描述

设备轮询 `(`（为简便起见）指一种让操作系统周期性地轮询设备的技术，而不是依赖设备在需要关注时生成中断。这看起来似乎低效且反直觉，但如果做得正确，`(` 让操作系统对何时以及如何处理设备具有更多控制权，在系统响应能力和性能方面有许多优势。

特别是，`(` 减少了服务中断时产生的上下文切换开销，并对 CPU 在各种任务（用户进程、软件中断、设备处理）之间的调度提供更多控制，从而最终降低系统中活锁的可能性。

### 操作原理

在正常的基于中断的模式下，设备在需要关注时随时生成中断。这反过来导致上下文切换和执行中断处理程序，由后者执行设备所需的任何处理。除非设备驱动程序在编程时考虑了实时性（FreeBSD 驱动通常不是这种情况），否则中断处理程序的持续时间潜在无界。此外，在重流量负载下，系统可能持续处理中断而无法完成其他工作，无论是在内核中还是在用户态中。

设备轮询通过在适当的时间（即时钟中断时和空闲循环内）轮询设备来禁用中断。这样，上下文切换开销被消除。此外，操作系统可以准确控制花费多少工作来处理设备事件，从而通过为其他任务预留一定量的 CPU 来防止活锁。

启用 `(` 还会更改软件网络中断的调度方式，因此绝不会因为包未处理完而出现活锁风险。

### 启用轮询

目前仅网络接口驱动支持 `(` 功能。它可借助 [ifconfig(8)](../man8/ifconfig.8.md) 命令打开和关闭。

历史上的 `kern.polling.enable`（为所有接口启用轮询）可用以下代码替代：

```sh
for i in `ifconfig -l` ;
  do ifconfig $i polling; # 使用 -polling 禁用
done
```

### MIB 变量

`(` 的操作由以下 [sysctl(8)](../man8/sysctl.8.md) MIB 变量控制：

**`kern.polling.user_frac`** 当启用 `(` 时，在有工作要做的情况下，最多此百分比的 CPU 周期被保留给用户态任务，剩余部分可用于 `(` 处理。默认为 50。
**`kern.polling.burst`** 每个定时器滴答中从每个网络接口抓取的最大包数。此数字由内核根据编程的 `user_frac , burst_max`、CPU 速度和系统负载动态调整。
**`kern.polling.each_burst`** 上面的 burst 被分成由此数量的包组成的较小块，在所有为 `(` 注册的接口之间循环轮流。这可防止单个接口的大 burst 使 IP 中断队列（`net.inet.ip.intr_queue_maxlen`）饱和。默认为 5。
**`kern.polling.burst_max`** `kern.polling.burst` 的上限。注意，当启用 `(` 时，每个接口每秒最多可接收（`HZ` * `burst_max`）个包，除非空闲循环中有可用的空闲 CPU 周期用于 `(`。应调整此数字以匹配预期负载（在 GigE 网卡上可能相当高）。默认为 150，适用于 100Mbit 网络和 HZ=1000。
**`kern.polling.idle_poll`** 控制是否在空闲循环中启用 `(`。没有理由禁用此功能（除了节能或调度程序处理空闲优先级内核线程中的 bug）。
**`kern.polling.reg_frac`** 控制多久（每 `reg_frac` / `HZ` 秒）检查一次设备状态寄存器以查找错误情况等。增大此值可减少总线负载，但也会延迟错误检测。默认为 20。
**`kern.polling.handlers`** 多少个活动设备已注册 `(`。
**`kern.polling.short_ticks`**
**`kern.polling.lost_polls`**
**`kern.polling.pending_polls`**
**`kern.polling.residual_burst`**
**`kern.polling.phase`**
**`kern.polling.suspect`**
**`kern.polling.stalled`** 调试变量。

## 支持的设备

设备轮询需要对设备驱动程序进行显式修改。截至本文撰写时，支持 [bge(4)](bge.4.md)、[dc(4)](dc.4.md)、[em(4)](em.4.md)、[fwe(4)](fwe.4.md)、[fwip(4)](fwip.4.md)、[fxp(4)](fxp.4.md)、igb(4)、[nfe(4)](nfe.4.md)、[nge(4)](nge.4.md)、[re(4)](re.4.md)、[rl(4)](rl.4.md)、[sis(4)](sis.4.md)、[ste(4)](ste.4.md)、[stge(4)](stge.4.md)、[vge(4)](vge.4.md)、[vr(4)](vr.4.md) 和 [xl(4)](xl.4.md) 设备，其他设备正在开发中。修改相当简单，包括提取中断服务例程的内部部分并编写一个回调函数 Fn *_poll，调用该函数来探测设备的事件并处理它们。（更多详情请参见上述设备的条件编译部分。）

由于在最坏情况下设备仅在当时钟中断时被轮询，为了减少处理包的延迟，不建议将时钟频率降低到 1000 Hz 以下。

## 历史

设备轮询首次出现于 FreeBSD 4.6 和 FreeBSD 5.0。

## 作者

设备轮询由 Luigi Rizzo <luigi@iet.unipi.it> 编写。
