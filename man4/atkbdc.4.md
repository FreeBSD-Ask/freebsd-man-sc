# atkbdc.4

`atkbdc` — AT 键盘控制器接口

## 名称

`atkbdc`

## 概要

`options KBD_RESETDELAY=N options KBD_MAXWAIT=N options KBD_DELAY1=N options KBD_DELAY2=N options KBDIO_DEBUG=N device atkbdc`

在 **/boot/device.hints** 中：

```ini
hint.atkbdc.0.at="isa"
hint.atkbdc.0.port="0x060"
```

## 描述

键盘控制器 `atkbdc` 为 AT 键盘和 PS/2 鼠标风格指点设备提供 I/O 服务。此控制器是键盘驱动 `atkbd` 和 PS/2 指点设备驱动 `psm` 所必需的。

系统中只能配置一个 `psm` 设备。

## 驱动配置

### 内核配置选项

以下内核配置选项可用于控制 `psm` 驱动。可在内核配置文件中设置（参见 [config(8)](../man8/config.8.md)）。

***KBD_RESETDELAY=X**，KBD_MAXWAIT=Y* 键盘驱动 `atkbd` 和指点设备驱动 `psm` 可能在引导过程中要求 `psm` 驱动重置这些设备。这些设备响应重置命令有时需要较长时间。这些选项控制 `psm` 驱动在最终放弃前应等待的时长——驱动最多等待 `X` * `Y` 毫秒。如果驱动似乎无法检测到设备，可增大这些值。`X` 的默认值为 200 毫秒，`Y` 的默认值为 5。

***KBD_DELAY1=X**，KBD_DELAY2=Y* DELAY1 将初始按键重复延迟设为 `X`。默认值为 500 毫秒。DELAY2 将按键重复延迟设为 `Y`。默认值为 100 毫秒。

***KBDIO_DEBUG=N*** 将调试级别设为 `N`。默认值为零，即抑制所有调试输出。

## 参见

[atkbd(4)](atkbd.4.md), [psm(4)](psm.4.md), [config(8)](../man8/config.8.md)

## 历史

`psm` 驱动首次出现于 FreeBSD 3.1。它基于 FreeBSD 2.2 中的 kbdio 模块。

## 作者

kbdio 模块、`psm` 驱动和本手册页由 Kazutaka Yokota <yokota@FreeBSD.org> 编写。
