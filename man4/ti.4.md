# ti.4

`ti` — Alteon Networks Tigon I 和 Tigon II 千兆以太网驱动程序

## 名称

`ti`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ti
> options TI_SF_BUF_JUMBO
> options TI_JUMBO_HDRSPLIT

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_ti_load="YES"
```

## 描述

`ti` 驱动为基于 Alteon Networks Tigon 千兆以太网控制器芯片的 PCI 千兆以太网适配器提供支持。Tigon 包含嵌入式 R4000 CPU、千兆 MAC、双 DMA 通道和 PCI 接口单元。Tigon II 包含两个 R4000 CPU 和其他改进。两种芯片都可用于 32 位或 64 位 PCI 插槽。与芯片的通信通过 PCI 共享内存和总线主控 DMA 实现。Tigon I 和 II 支持硬件多播地址过滤、VLAN 标记提取和插入以及高达 9000 字节的巨型以太网帧。注意，Tigon I 芯片组已不再积极生产：所有新适配器都应配备 Tigon II 芯片组。

虽然 Tigon 芯片组支持 10、100 和 1000Mbps 速度，但 10 和 100Mbps 速度支持仅在具有适当收发器的板上可用。大多数适配器仅设计为在 1000Mbps 下工作，但驱动应支持那些在较低速度下工作的 NIC。

通过接口 MTU 设置提供对巨型帧的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 选择大于 1500 字节的 MTU 可配置适配器接收和传输巨型帧。使用巨型帧可以大大提高某些任务（如文件传输和数据流）的性能。

Tigon 2 板的头部拆分支持（此选项对 Tigon 1 无效）可通过 `TI_JUMBO_HDRSPLIT` 选项启用。参见 zero_copy(9) 以获取有关零拷贝接收和头部拆分的更多讨论。

`ti` 驱动使用 UMA 支持的巨型接收缓冲区，但可配置为使用 sendfile(2) 缓冲区分配器。要启用 sendfile(2) 缓冲区分配器，请使用 `TI_SF_BUF_JUMBO` 选项。

还可使用 [vlan(4)](vlan.4.md) 机制支持 VLAN。详见 [vlan(4)](vlan.4.md) 手册页。

`ti` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择。用户可以通过在 **`/etc/rc.conf`** 文件中添加媒体选项来手动覆盖自动选择的模式。

**10baseT/UTP** 设置 10Mbps 操作。`mediaopt` 选项也可用于选择 `full-duplex` 或 `half-duplex` 模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。`mediaopt` 选项也可用于选择 `full-duplex` 或 `half-duplex` 模式。

**1000baseSX** 设置 1000Mbps（千兆以太网）操作。此速度下仅支持 `full-duplex` 模式。

`ti` 驱动支持以下媒体选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ti` 驱动支持基于 Alteon Tigon I 和 II 芯片的千兆以太网适配器。`ti` 驱动已使用以下适配器测试：

- 3Com 3c985-SX 千兆以太网适配器（Tigon 1）
- 3Com 3c985B-SX 千兆以太网适配器（Tigon 2）
- Alteon AceNIC V 千兆以太网适配器（1000baseSX）
- Alteon AceNIC V 千兆以太网适配器（1000baseT）
- Digital EtherWORKS 1000SX PCI 千兆适配器
- Netgear GA620 千兆以太网适配器（1000baseSX）
- Netgear GA620T 千兆以太网适配器（1000baseT）

以下适配器也应该受支持，但尚未经过测试：

- Asante GigaNIX1000T 千兆以太网适配器
- Asante PCI 1000BASE-SX 千兆以太网适配器
- Farallon PN9000SX 千兆以太网适配器
- NEC 千兆以太网
- Silicon Graphics PCI 千兆以太网适配器

## 加载器可调参数

可在引导内核之前在 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，或存储在 loader.conf(5) 中。

**`hw.ti.%d.dac`** 如果此可调参数设为 0，将禁用 DAC（双地址周期）。默认值为 1，表示驱动将使用完整 64 位 DMA 寻址。

## SYSCTL 变量

以下变量作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数都可用。更改以下任何可调参数时，必须先关闭再启动接口才能使更改生效。下面提到的一微秒时钟滴答是标称时间，实际硬件可能无法提供此级别的粒度。例如，在 Tigon 2（修订版 6）卡上，发布版本 12.0 的时钟粒度为 5 微秒。

**`dev.ti.%d.rx_coal_ticks`** 此值，接收合并滴答，控制必须经过多少个时钟滴答（每个 1 微秒）才能让 NIC DMA 接收返回生产者指针到主机并生成中断。此参数与 rx_max_coal_bds（接收最大合并 BD）可调参数配合使用。当任一阈值被超过时，NIC 将接收返回生产者指针返回给主机。值为 0 表示忽略此参数，仅在达到接收最大合并 BD 值时才返回接收 BD。默认值为 170。

**`dev.ti.%d.rx_max_coal_bds`** 此值，接收最大合并 BD，控制 NIC 更新接收返回环生产者索引之前将合并的接收缓冲区描述符数量。如果此值设为 0，将禁用接收缓冲区描述符合并。默认值为 64。

**`dev.ti.%d.ti_tx_coal_ticks`** 此值，发送合并滴答，控制必须经过多少个时钟滴答（每个 1 微秒）才能让 NIC DMA 发送消费者指针到主机并生成中断。此参数与 tx_max_coal_bds（发送最大合并 BD）可调参数配合使用。当任一阈值被超过时，NIC 将发送消费者指针返回给主机。值为 0 表示忽略此参数，仅在达到发送最大合并 BD 值时才返回发送 BD。默认值为 2000。

**`dev.ti.%d.tx_max_coal_bds`** 此值，发送最大合并 BD，控制 NIC 更新发送消费者索引之前将合并的发送缓冲区描述符数量。如果此值设为 0，将禁用发送缓冲区描述符合并。默认值为 32。

**`dev.ti.%d.tx_buf_ratio`** 此值控制 NIC 中剩余内存中应专用于发送缓冲区与接收缓冲区的比率。低 7 位用于以 1/64 增量表示比率。例如，将此值设为 16 会将发送缓冲区设为剩余缓冲区空间的 1/4。在任何情况下，发送或接收缓冲区都不会减少到 68 KB 以下。对于 1 MB NIC，数据缓冲区的近似总空间为 800 KB。对于 512 KB NIC，该数字为 300 KB。默认值为 21。

**`dev.ti.%d.stat_ticks`** 此值，统计滴答，控制必须经过多少个时钟滴答（每个 1 微秒）才能让 NIC DMA 统计块到主机并生成 STATS_UPDATED 事件。如果设为零，则统计信息从不 DMA 到主机。建议将此值设为足够高的频率，以免误导读取统计信息刷新的人。每秒几次就足够了。默认值为 2000000（2 秒）。

## IOCTL

除了大多数网络驱动实现的标准 socket(2) ioctl(2) 调用外，`ti` 驱动还包括一个字符设备接口，可用于附加诊断、配置和调试。使用此字符设备接口和特别修补的 gdb(1) 版本（`ports/devel/gdb`），用户可以调试在 Tigon 板上运行的固件。

这些 ioctl 及其参数定义于

`#include <sys/tiio.h>`

头文件。

**`TIIOCGETSTATS`** 返回从卡 DMA 到内核内存的卡统计信息，大约每 2 秒一次。（该时间间隔可通过 `TIIOCSETPARAMS` ioctl 更改。）参数为 `struct ti_stats`。

**`TIIOCGETPARAMS`** 获取各种影响中断合并方式的性能相关固件参数。参数为 `struct ti_params`。

**`TIIOCSETPARAMS`** 设置各种影响中断合并方式的性能相关固件参数。参数为 `struct ti_params`。

**`TIIOCSETTRACE`** 告诉 NIC 跟踪请求的信息类型。参数为 `ti_trace_type`。

**`TIIOCGETTRACE`** 从卡转储跟踪缓冲区。参数为 `struct ti_trace_buf`。

**`ALT_ATTACH`** 此 ioctl 用于与 Alteon 的 Solaris 驱动兼容。他们显然只有一个用于调试的字符接口，因此必须告诉它要调试哪个 Tigon 实例。此 ioctl 在 FreeBSD 上是空操作。

**`ALT_READ_TG_MEM`** 从 Tigon 板读取请求的内存区域。参数为 `struct tg_mem`。

**`ALT_WRITE_TG_MEM`** 写入 Tigon 板上请求的内存区域。参数为 `struct tg_mem`。

**`ALT_READ_TG_REG`** 从 Tigon 板读取请求的寄存器。参数为 `struct tg_reg`。

**`ALT_WRITE_TG_REG`** 写入 Tigon 板上请求的寄存器。参数为 `struct tg_reg`。

## 文件

**`/dev/ti[0-255]`** Tigon 驱动字符接口。

## 诊断

- ti%d: couldn't map memory 发生了致命的初始化错误。
- ti%d: couldn't map interrupt 发生了致命的初始化错误。
- ti%d: no memory for softc struct! 驱动在初始化期间未能为每设备实例信息分配内存。
- ti%d: failed to enable memory mapping! 驱动未能初始化 PCI 共享内存映射。如果卡不在总线主控插槽中，可能会发生这种情况。
- ti%d: no memory for jumbo buffers! 驱动在初始化期间未能为巨型帧分配内存。
- ti%d: bios thinks we're in a 64 bit slot, but we aren't BIOS 将 NIC 编程为好像它安装在 64 位 PCI 插槽中，但实际上 NIC 在 32 位插槽中。这是由于某些 BIOS 中的错误而发生的。这可以在 Tigon II 上解决，但在 Tigon I 上初始化将失败。
- ti%d: board self-diagnostics failed! 系统启动后 CPU 状态寄存器中的 ROMFAIL 位被设置，表明板载 NIC 诊断失败。
- ti%d: unknown hwrev 驱动检测到具有不受支持的硬件修订版的板。`ti` 驱动支持修订版 4（Tigon 1）和修订版 6（Tigon 2）芯片，并且仅有这些设备的固件。
- ti%d: watchdog timeout 设备已停止响应网络，或网络连接（电缆）有问题。

## 参见

sendfile(2), [altq(4)](altq.4.md), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md), zero_copy(9)

## 历史

`ti` 设备驱动首次出现于 FreeBSD 3.0。

## 作者

`ti` 驱动由 Bill Paul <wpaul@bsdi.com> 编写。头部拆分固件修改、字符 ioctl(2) 接口和调试支持由 Kenneth Merry <ken@FreeBSD.org> 编写。初始零拷贝支持由 Andrew Gallatin <gallatin@FreeBSD.org> 编写。
