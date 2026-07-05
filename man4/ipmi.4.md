# ipmi.4

`ipmi` — OpenIPMI 兼容的 IPMI 接口驱动

## 名称

`ipmi`

## 概要

`device ipmi`

要在 **/boot/device.hints** 中手动指定 I/O 附加方式：`hint.ipmi.0.at="isa" hint.ipmi.0.port="0xCA2" hint.ipmi.0.spacing="8" hint.ipmi.0.mode="KCS"`

要在 **/boot/device.hints** 中手动指定内存附加方式：`hint.ipmi.0.at="isa" hint.ipmi.0.maddr="0xf0000000" hint.ipmi.0.spacing="8" hint.ipmi.0.mode="SMIC"`

spacing 的含义：

8 位对齐

16 位对齐

32 位对齐

**8**

**16**

**32**

如果未指定 port 和 spacing，将使用接口类型默认值。仅指定 port 用于 I/O 访问或 maddr 用于内存访问。

## 描述

IPMI（Intelligent Platform Management Interface，智能平台管理接口）是一项用于监测系统硬件的标准，允许通用代码检测和监测系统中的传感器。IPMI 标准提供看门狗支持、FRU 数据库和其他支持扩展。目前正被许多单板和嵌入式系统制造商采用。

FreeBSD 中的 `ipmi` 驱动大量借鉴自标准和 Linux 驱动；但是，并非标准中描述的所有功能都受支持。

`ipmi` 驱动实现了 [shutdown(8)](../man8/shutdown.8.md) 的电源循环选项，用于实现系统的电源循环。主板上的 BMC 必须支持机箱设备以及 IPMI 标准第 28.3 节中描述的机箱控制命令的可选电源循环子命令。系统关闭的时长至少为一秒，但如果已设置电源循环间隔，则可能更长（见第 28.9 节）。

## IOCTLS

通过 `ipmi` 驱动发送和接收消息需要使用 ioctl(2)。由于发送到和接收自设备的数据复杂性，使用 ioctl。以下 ioctl(2) 命令码定义于

`#include <sys/ipmi.h>`

ioctl(2) 的第三个参数应为指向所示类型的指针。

当前支持以下 ioctl：

**[EAGAIN]** 处理队列中没有消息。

**[EFAULT]** 提供的地址无效。

**[EMSGSIZE]** 地址无法放入消息缓冲区并将保留在缓冲区中。

**[EFAULT]** 提供的地址无效。

**[ENOMEM]** 无法为命令分配缓冲区，内存不足。

**`IPMICTL_RECEIVE_MSG`** (`struct ipmi_recv`) 接收消息。可能的错误值：

**`IPMICTL_RECEIVE_MSG_TRUNC`** (`struct ipmi_recv`) 类似于 `IPMICTL_RECEIVE_MSG`，但如果消息无法放入缓冲区，将截断内容而非将数据保留在缓冲区中。

**`IPMICTL_SEND_COMMAND`** (`struct ipmi_req`) 向接口发送消息。可能的错误值：

**`IPMICTL_SET_MY_ADDRESS_CMD`** (`unsigned int`) 设置源消息的从地址。

**`IPMICTL_GET_MY_ADDRESS_CMD`** (`unsigned int`) 获取源消息的从地址。

**`IPMICTL_SET_MY_LUN_CMD`** (`unsigned int`) 设置源消息的从 LUN。

**`IPMICTL_GET_MY_LUN_CMD`** (`unsigned int`) 获取源消息的从 LUN。

### 未实现的 ioctl

**[EFAULT]** 提供的地址无效。

**[EBUSY]** 网络功能/命令已被占用。

**[ENOMEM]** 无法分配内存。

**[EFAULT]** 提供的地址无效。

**[ENOENT]** 未找到网络功能/命令。

**`IPMICTL_REGISTER_FOR_CMD`** (`struct ipmi_cmdspec`) 注册以接收特定命令。可能的错误值：

**`IPMICTL_UNREGISTER_FOR_CMD`** (`struct ipmi_cmdspec`) 注销以接收特定命令。可能的错误值：

### 仅存根的 ioctl

**[EFAULT]** 提供的地址无效。

**`IPMICTL_SET_GETS_EVENTS_CMD`** (`int`) 设置此接口是否接收事件。可能的错误值：

## 参见

ioctl(2), [watchdog(4)](watchdog.4.md), [reboot(8)](../man8/reboot.8.md), [shutdown(8)](../man8/shutdown.8.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`ipmi` 驱动首次出现于 FreeBSD 6.2。

## 作者

`ipmi` 驱动由 Doug Ambrisko <ambrisko@FreeBSD.org> 编写。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 编写。

## 缺陷

并非 MontaVista 驱动的所有功能都受支持。

目前未实现 IPMB 和 BT 模式。
