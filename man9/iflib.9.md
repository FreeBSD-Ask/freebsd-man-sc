# iflib.9

`iflib` — 网络接口驱动程序框架

## 名称

`iflib`

## 描述

`iflib` 是一个为 FreeBSD 编写网络接口驱动程序的框架。它旨在消除现代网络接口设备通常需要的大量样板代码，让驱动程序作者能够专注于其硬件所需的特定代码。

`iflib` 有三个逻辑组件，每个组件都在其各自的手册页中描述。它们是：

**[iflibdi(9)](iflibdi.9.md)** 设备无关函数，用于将 `iflib` 集成到 FreeBSD 网络栈的其余部分。

**[iflibdd(9)](iflibdd.9.md)** 设备相关函数，用于编写新的基于 `iflib` 的驱动程序。

**[iflibtxrx(9)](iflibtxrx.9.md)** 设备相关的发送和接收函数，用于编写新的基于 `iflib` 的驱动程序。

## 参见

[iflib(4)](../man4/iflib.4.md), [iflibdd(9)](iflibdd.9.md), [iflibdi(9)](iflibdi.9.md), [iflibtxrx(9)](iflibtxrx.9.md), [ifnet(9)](ifnet.9.md)

## 作者

Benno Rice <benno@FreeBSD.org>
