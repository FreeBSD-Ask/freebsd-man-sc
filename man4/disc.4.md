# disc(4)

`disc` — 软件丢弃网络接口

## 名称

`disc`

## 概要

`device disc`

## 描述

`disc` 接口是一种软件丢弃机制，可用于性能分析和/或软件测试。与其他网络接口一样，丢弃接口必须为每个要使用的地址族分配网络地址。这些地址可通过 `SIOCSIFADDR` ioctl(2) 设置或更改。

每个 `disc` 接口在运行时使用接口克隆创建。最简单的方法是使用 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量。

## 参见

[inet(4)](inet.4.md), [intro(4)](intro.4.md)

## 历史

`disc` 设备似乎在 4.4BSD 时期从 [lo(4)](lo.4.md) 设备派生而来。本手册页改编自 [lo(4)](lo.4.md)，首次出现于 FreeBSD 5.0。
