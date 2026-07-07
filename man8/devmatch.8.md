# devmatch(8)

`devmatch` — 打印未附加设备的信息

## 名称

`devmatch`

## 概要

`devmatch [-a | --all] [-d | --dump] [[-h | --hints] file] [[-p | --nomatch] event] [-q | --quiet] [-u | --unbound] [-v | --verbose]`

## 描述

不带任何参数时，`devmatch` 工具会打印它为系统中所有未附加且已启用的设备找到的所有内核模块。

**`-a`**, **`--all`** 包含所有设备，而不仅仅是未附加的设备。

**`-d`**, **`--dump`** 生成 `linker.hints` 文件的可读转储。

**`-h`**, **`--hints`** `file` 使用指定的 `file`，而不是从当前模块加载路径推测出的 `linker.hints`。

**`-p`**, **`--nomatch`** `event` 解析并使用来自 devd(8) 的标准 NOMATCH 事件进行匹配，而不是搜索设备树。

**`-q`**, **`--quiet`** 抑制某些错误消息，仅返回非零退出码。这有助于在没有提示可用时避免引导期间出现无尽的警告列表。

**`-u`**, **`--unbound`** 尝试生成一份列表，列出那些具有 PNP 信息但其驱动程序表中找不到该 PNP 信息的驱动程序。

**`-v`**, **`--verbose`** 生成更详细的输出。

## 参见

[rc.conf(5)](../man5/rc.conf.5.md), [devinfo(8)](devinfo.8.md), [MODULE_PNP_INFO(9)](../man9/module_pnp_info.9.md)

## 历史

`devmatch` 首次出现于 FreeBSD 12.0。

## 作者

Warner Losh <imp@FreeBSD.org>

## 缺陷

内核中包含提示（hints），但我们在为未匹配设备建议模块的列表中将其排除。在建议驱动程序时我们将其排除，但在查找未绑定设备或生成 `linker.hints` 的完整转储时又将其包含在内。这可能令人困惑。

某些模块是 **/boot/kernel** 中的硬链接，会被报告两次。

PNP 字符串的属性会针对该总线上每个 PNP 条目评估一次，而不是只评估一次。

在 FreeBSD 中，PNP 这个术语的含义被重载了。它通常指总线提供的关于设备的标识数据。虽然这包括旧的 ISA PNP 标识符，但也包括 USB、PCI 等中的逻辑等价物。

目前许多驱动程序缺乏正确的 PNP 表修饰，需要更新。
