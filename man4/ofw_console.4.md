# ofw_console(4)

`ofw_console` — Open Firmware 控制台

## 名称

`ofw_console`

## 概要

`cpu AIM options OFWCONS_POLL_HZ=N`

`options KDB options DDB options ALT_BREAK_TO_DEBUGGER`

## 描述

`ofw_console` 驱动提供简单的文本控制台，使用 Open Firmware 服务进行输入和输出。它将使用通过 `input-device` 和 `output-device` 变量设置的 Open Firmware 控制台设备。

此驱动已弃用，仅在实际控制台硬件无法由 FreeBSD 驱动时作为后备控制台机制提供。

如果 `ofw_console` 控制台工作速度太慢，可以通过包含 `options OFWCONS_POLL_HZ=N` 来改善其响应速度。省略时，`OFWCONS_POLL_HZ` 默认为 4。例如，在 Sun Ultra 2 上，值为 20 或更高效果最佳。另一方面，过高的值可能导致 `ofw_console` 不必要地消耗 CPU。

## 文件

**`/dev/console`**
**`/dev/keyboard`** 当控制台输入设备为键盘时的终端输入设备
**`/dev/screen`** 当控制台输出设备为屏幕时的终端输出设备
**`/dev/tty[a-z]`** 当控制台输入和输出设备均为 tty[a-z] 时的终端设备

## 参见

[akbd(4)](akbd.4.md), [powermac_nvram(4)](powermac_nvram.4.md), [vt(4)](vt.4.md)

## 历史

`ofw_console` 驱动首次出现于 FreeBSD 5.0。

## 作者

`ofw_console` 驱动由 Benno Rice <benno@FreeBSD.org> 编写。

## 注意事项

由于 Open Firmware 会在 `ofw_console` 之前处理 BREAK（或 Stop-A）序列，使用 `ofw_console` 时进入 [ddb(4)](ddb.4.md) 的首选方法是在启用 ddb 的内核中包含 `options ALT_BREAK_TO_DEBUGGER`，并输入替代 BREAK 序列（RETURN TILDE CTRL-b）。

## 缺陷

`ofw_console` 驱动也不会附加到它实际通信的硬件资源。
