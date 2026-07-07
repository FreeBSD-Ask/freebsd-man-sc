# dcons(4)

`dcons` — dumb 控制台设备驱动

## 名称

`dcons`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> options GDB
> device firewire
> device dcons

`或者，若要在引导时以模块方式加载此驱动，请在内核配置文件中加入以下行：`

> options GDB

`并在 loader.conf(5) 中：`

> dcons_load="YES"

## 描述

`dcons` 设备是一个简单的控制台设备，它只是分别从分配的缓冲区读取和写入以进行输入和输出。它本身没有用处，预期该缓冲区通过类似 [firewire(4)](firewire.4.md) 的总线或 kvm(3) 进行访问以实现交互。

缓冲区由 4 个通道组成。有 2 个端口，一个用于控制台 TTY，另一个是 GDB 端口，然后每个端口都有一个输入通道和一个输出通道。

## 文件

**`/dev/dcons`**
**`/etc/ttys`**

## 实例

如果要在 `dcons` 上运行 getty(8)，请在 ttys(5) 中插入以下行，并使用 [kill(1)](../man1/kill.1.md) 向 [init(8)](../man8/init.8.md) 发送 `HUP` 信号。

```sh
dcons	"/usr/libexec/getty std.115200"	vt100	on  secure
```

一旦 [fwohci(4)](fwohci.4.md) 设备初始化为允许物理访问，即可使用 dconschat(8) 应用程序从另一台主机通过 [firewire(4)](firewire.4.md) 总线访问该缓冲区。详情见 dconschat(8)。

如果要将 `dcons` 用作 gdb(1)（`ports/devel/gdb`）端口，请在 loader.conf(5) 中加入以下行：

```sh
dcons_gdb="1"
```

## 参见

[dcons_crom(4)](dcons_crom.4.md), [ddb(4)](ddb.4.md), [firewire(4)](firewire.4.md), [fwohci(4)](fwohci.4.md), [gdb(4)](gdb.4.md), ttys(5), conscontrol(8), dconschat(8), fwcontrol(8)

## 作者

Hidetoshi Shimokawa <simokawa@FreeBSD.org>

## 缺陷

此驱动为 Ud
