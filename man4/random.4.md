# random.4

`random` — 熵设备

## 名称

`random`

## 概要

`options RANDOM_LOADABLE options RANDOM_ENABLE_ETHER options RANDOM_ENABLE_TPM options RANDOM_ENABLE_UMA`

## 描述

`random` 设备读取时返回源源不断的随机字节。

生成器初始处于*未播种*状态，在首次播种完成之前会阻塞读取。

为在引导时提供对随机设备的即时访问，FreeBSD 会自动将一些熵数据保存到 **`/boot/entropy`**，由 [loader(8)](../man8/loader.8.md) 提供给内核。额外的熵会定期保存到 **`/var/db/entropy`**。在具备可写存储介质的设备上，这些保存的熵足以解除随机设备的阻塞。

不具备可写存储介质的嵌入式应用必须自行制定在引导时为随机设备重新播种的方案，或者接受设备保持未播种状态并无限期阻塞读取的事实。详见 SECURITY CONSIDERATIONS 一节。

除 read(2) 之外，抽象内核熵设备的直接输出还可以通过 getrandom(2)、getentropy(3) 或 [sysctl(8)](../man8/sysctl.8.md) 伪变量 `kern.arandom` 读取。

要查看软件 `random` 设备的当前设置，可使用以下命令：

```sh
sysctl kern.random
```

结果类似于：

```sh
kern.random.block_seeded_status: 0
kern.random.fortuna.minpoolsize: 64
kern.random.harvest.mask_symbolic: ENABLEDSOURCE,[DISABLEDSOURCE],...,CACHED
kern.random.harvest.mask_bin: 00000010000000111011111
kern.random.harvest.mask: 66015
kern.random.use_chacha20_cipher: 0
kern.random.random_sources: 'Intel Secure Key RNG'
kern.random.initial_seeding.bypass_before_seeding: 1
kern.random.initial_seeding.read_random_bypassed_before_seeding: 0
kern.random.initial_seeding.arc4random_bypassed_before_seeding: 0
kern.random.initial_seeding.disable_bypass_warnings: 0
```

除 `kern.random.block_seeded_status`、`kern.random.fortuna.minpoolsize` 和 `kern.random.harvest.mask` 之外，所有设置通过 [sysctl(8)](../man8/sysctl.8.md) 都是只读的。

`kern.random.fortuna.minpoolsize` sysctl 用于设置播种阈值。数值越小播种越快，但安全性越低。实践中 64 到 256 之间的取值均可接受。

`kern.random.harvest.mask` 位掩码用于选择可用的熵源。值 0（零）表示对应的源不被视为熵源。若希望使用该源，将对应位设置为 1（一）即可。`kern.random.harvest.mask_bin` 和 `kern.random.harvest.mask_symbolic` sysctl 可用于以人类可读形式确认设置。后者中被禁用的条目以方括号列出。关于熵采集的更多信息，参见 [random_harvest(9)](../man9/random_harvest.9.md)。

`kern.random.nist_healthtest_enabled` 可调参数可用于启用 NIST 特别出版物 800-90B 第 4 节中描述的熵源健康测试。启用后，所有熵源都将接受该文档中描述的重复计数测试和自适应比例测试。如果某项测试失败，该源会禁用，即来自该源的后续所有熵样本都会丢弃。该实现会执行启动测试，期间熵样本均丢弃。

## 文件

**`/dev/random`**

**`/dev/urandom`**

## 诊断

以下可调参数与 `random` 设备的初始播种相关：

**`kern.random.initial_seeding.bypass_before_seeding`** 默认值为 1（开启）。设置后，系统在初始播种之前会绕过 `random` 设备。*开启此项是不安全的*，但许多缺乏早期熵源、或无法在引导早期足够早地加载 **`/boot/entropy`** 供 `random` 消费者使用的系统因此获得了可用性。取消设置（0）时，若 `random` 设备尚未完成初始播种，系统将阻塞 read_random(9) 和 arc4random(9) 请求，直至播种完成。

**`kern.random.initial_seeding.disable_bypass_warnings`** 默认值为 0（关闭）。设置为非零值时，禁用 `random` 设备绕过时在 dmesg 中输出的警告。

以下只读 [sysctl(8)](../man8/sysctl.8.md) 变量允许以编程方式诊断引导过程中是否发生了 `random` 设备绕过。若设置为非零值，表示特定功能单元绕过了强 `random` 设备输出，且要么不产生输出（(read_random)），要么以最少的非加密强度熵为自身播种（(arc4random)）。

- `kern.random.initial_seeding.read_random_bypassed_before_seeding`
- `kern.random.initial_seeding.arc4random_bypassed_before_seeding`

## 参见

getrandom(2), arc4random(3), getentropy(3), random(3), [sysctl(8)](../man8/sysctl.8.md), [random(9)](../man9/random.9.md)

> Ferguson, Schneier, Kohno, *Cryptography Engineering*, Wiley, ISBN 978-0-470-47424-2.

## 历史

`random` 设备最早出现在 FreeBSD 2.2 中。FreeBSD 5.0 中实现改为 *Yarrow 算法*。FreeBSD 11.0 中引入 Fortuna 算法作为默认算法。FreeBSD 12.0 中 Yarrow 被完全移除。

## 作者

当前的 `random` 代码由 Mark V Murray 编写，并得到许多人的重要贡献。

*Fortuna* 算法由 Niels Ferguson、Bruce Schneier 和 Tadayoshi Kohno 设计。

## 注意事项

启用 `options RANDOM_LOADABLE` 时，在加载"算法模块"之前不会创建 **`/dev/random`** 设备。默认构建的唯一模块是 *random_fortuna*。可加载的 random 模块比编译进内核的等价模块效率更低。这是因为某些函数必须对加载和卸载事件加锁，并且必须是间接调用以允许移除。

启用 `options RANDOM_ENABLE_UMA` 时，**`/dev/random`** 设备将从 zone 分配器获取熵。这是一个速率极高的源，对性能影响显著。因此默认禁用。

启用 `options RANDOM_ENABLE_ETHER` 时，`random` 设备将从经过网络栈的 `mbuf` 结构中获取熵。此源代价极高且熵质量较差，因此默认禁用。

## 安全注意事项

随机数生成器的初始播种是一个需要非常仔细对待的自举问题。当具备可写存储介质时，*Fortuna* 论文描述了一种可快速为设备重新播种的稳健系统。

在某些嵌入式场景中，在系统完全运行之前可能难以找到足够的随机性为随机数生成器播种。在这些情况下，系统架构师有责任确保阻塞是可接受的，或者确保随机设备已被播种。（此建议不适用于典型的消费者系统。）

为模拟嵌入式系统，开发者可将 `kern.random.block_seeded_status` 可调参数设置为 1，以验证引导过程不依赖于 `random` 设备的早期可用性。
