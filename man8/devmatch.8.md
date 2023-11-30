  DEVMATCH(8)  

DEVMATCH(8)

FreeBSD System Manager's Manual

DEVMATCH(8)

[名称](#__u540D___u79F0_)
=======================

`devmatch` —

打印有关未连接设备的信息

[概要](#__u6982___u8981_)
=======================

`devmatch` \[`-adhpuv`\] \[`--all`\] \[`--dump`\] \[`--hints` file\] \[`--nomatch` event\] \[`--unbound`\] \[`--verbose`\]

[描述](#__u63CF___u8FF0_)
=======================

`devmatch` 实用程序不带任何参数，打印它为系统中所有未连接的、启用的设备找到的所有内核模块。

[`-a`](#a) `--all`

包括所有设备，而不仅仅是未连接的设备。

[`-d`](#d) `--dump`

生成 linker.hints 文件的人类可读转储。

[`-h`](#h) `--hints` file

使用命名 file 而不是从当前模块加载路径猜测的 linker.hints 。

[`-p`](#p) `--nomatch` event

解析并使用来自 devd(8) 的标准 NOMATCH 事件进行匹配，而不是搜索设备树。

[`-u`](#u) `--unbound`

尝试生成具有 PNP 信息的驱动程序列表，其驱动程序表与该 PNP 信息无法找到。

[`-v`](#v) `--verbose`

产生更详细的输出。

[参见](#__u53C2___u89C1_)
=======================

devinfo(8), MODULE\_PNP\_INFO(9)

[历史](#__u5386___u53F2_)
=======================

`devmatch` 最早出现在 FreeBSD 12.0 中。

[作者](#__u4F5C___u8005_)
=======================

Warner Losh <[imp@FreeBSD.org](mailto:imp@FreeBSD.org)\>

[缺陷](#__u7F3A___u9677_)
=======================

内核中有提示，但我们将其从模块列表中排除，以便为不匹配的设备提供建议。 我们在建议驱动程序时将其排除在外，但在查找未绑定的设备或生成完整的 linker.hints 时将其包括在内。 这可能会令人困惑。

有些模块是 /boot/kernel 中的硬链接，会被报告两次。

PNP 字符串的属性在该总线上的每个 PNP 条目被评估一次，而不是一次。

在 FreeBSD 中，术语 PNP 被重载了。 通常，这意味着总线提供的有关设备的识别数据。 虽然这包括旧的 ISA PNP 标识符，但它还包括 USB、PCI 等中的逻辑等价物。

许多驱动程序目前缺乏适当的 PNP 表装饰，需要更新。

October 12, 2020

FreeBSD 13.1-RELEASE