# snp.4

`snp` — tty 窥探接口

## 名称

`snp`

## 概要

`#include <sys/snoop.h>`

`Ft int Fn ioctl fd SNPSTTY &dev Ft int Fn ioctl fd SNPGTTY &dev Ft int Fn ioctl fd FIONREAD &result`

## 描述

`/dev/snp` 是一个窥探设备，允许用户附加到任何 tty 并观察其上的活动。内核必须以 `device snp` 编译，或加载 `snp` 模块，这些设备才可用。

要将给定的 `snp` 设备与要观察的 tty 关联起来，请打开 `snp` 设备和一个 tty 设备，然后在 `snp` 设备上发起 `SNPSTTY` ioctl。传递给 ioctl(2) 的参数是一个 `int` 类型变量的地址，该变量持有 tty 设备的文件描述符。要将 `snp` 设备从 tty 分离，使用指向值为 -1 的指针。

`SNPGTTY` ioctl 返回关于附加到所打开 `snp` 设备的当前 tty 的信息。

`FIONREAD` ioctl 返回一个等于读缓冲区中字符数的正值。已定义的特殊值有：

**`SNP_TTYCLOSE`** 未附加 tty。

**`SNP_DETACH`** `snp` 设备已被用户分离，或 tty 设备已关闭并分离。

## 参见

[pty(4)](pty.4.md), [kldload(8)](../man8/kldload.8.md), watch(8)

## 历史

`snp` 设备首次出现于 FreeBSD 2.1。在 FreeBSD 8.0 中，`snp` 驱动被重写以与替换后的 TTY 子系统协同工作。

## 作者

当前实现的作者是 Ed Schouten <ed@FreeBSD.org>。早期版本的 `snp` 基于 Ugen J.S. Antsilevich <ugen@NetVision.net.il> 编写的代码。
