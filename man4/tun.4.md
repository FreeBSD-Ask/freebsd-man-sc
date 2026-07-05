# tun.4

`tun` — 隧道软件网络接口

## 名称

`tun`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device tuntap

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_tuntap_load="YES"
```

## 描述

`tun` 接口是一种软件回环机制，可以粗略地描述为 [pty(4)](pty.4.md) 的网络接口对应物，也就是说，`tun` 之于网络接口就像 [pty(4)](pty.4.md) 驱动之于终端。

`tun` 驱动像 [pty(4)](pty.4.md) 驱动一样提供两个接口：一个类似它所模拟的常规设施（在 `tun` 的情况下是网络接口，对于 [pty(4)](pty.4.md) 是终端）的接口，以及一个字符特殊设备“控制”接口。客户端程序通过 `tun` “控制”接口收发（默认情况下）IP 数据包。[tap(4)](tap.4.md) 接口在以太网层提供类似功能：客户端通过 [tap(4)](tap.4.md) “控制”接口收发以太网帧。

网络接口命名为“`tun0`”、“`tun1`”等，每个已打开的控制设备对应一个。这些网络接口会持续存在，直到卸载 `if_tuntap.ko` 模块，或通过 [ifconfig(8)](../man8/ifconfig.8.md) 命令移除。

`tun` 设备通过接口克隆创建。可使用“ifconfig tun**N** create”命令完成。这是创建 `tun` 设备的首选方法。同样可用此方法移除接口，使用“ifconfig tun**N** destroy”命令。

如果 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.tun.devfs_cloning` 不为零，`tun` 接口允许在特殊控制设备 **`/dev/tun`** 上进行打开操作。打开此设备时，`tun` 将返回最低未使用 `tun` 设备的句柄（使用 devname(3) 确定具体是哪一个）。

**禁用旧版 devfs 克隆功能可能破坏使用 `tun` 的现有应用程序，如 ppp(8) 和 [ssh(1)](../man1/ssh.1.md)。因此，在另行通知之前，它默认启用。**

控制设备（成功打开后）持续存在，直到卸载 `if_tuntap.ko`，与网络接口持续存在的方式相同（见上文）。

每个接口支持常用的网络接口 ioctl(2)，如 `SIOCAIFADDR`，因此可像其他接口一样与 [ifconfig(8)](../man8/ifconfig.8.md) 一起使用。在引导时，它们是 `POINTOPOINT` 接口，但可以更改；参见下文对控制设备的描述。当系统选择在网络接口上传输数据包时，可从控制设备读取该数据包（在那里它显示为“输入”）；向控制设备写入数据包会在网络接口上生成一个输入数据包，就像（不存在的）硬件刚接收到它一样。

隧道设备（**`/dev/tun`**N）是独占打开的（如果已经打开则无法再打开）。如果接口未“ready”（即控制设备已打开且接口地址已设置），read(2) 调用将返回错误（Er EHOSTDOWN）。

一旦接口就绪，read(2) 将返回可用的数据包；如果没有，则要么阻塞直到有数据包可用，要么返回 Er EWOULDBLOCK，取决于是否启用了非阻塞 I/O。如果数据包长度超过传递给 read(2) 的缓冲区允许长度，额外数据将被静默丢弃。

如果已设置 `TUNSLMODE` ioctl，从控制设备读取的数据包将附加网络接口输出例程 Fn tunoutput 所呈现的目标地址作为前缀。目标地址为 `struct sockaddr` 格式。前缀地址的实际长度在成员 `sa_len` 中。如果已设置 `TUNSIFHEAD` ioctl，数据包将附加四字节的地址族（网络字节序）作为前缀。`TUNSLMODE` 和 `TUNSIFHEAD` 互斥。无论哪种情况，数据包数据紧随其后。

write(2) 调用将数据包传入以在伪接口上“接收”。如果已设置 `TUNSIFHEAD` ioctl，必须附加地址族前缀，否则假定数据包类型为 `AF_INET`。每次 write(2) 调用恰好提供一个数据包；数据包长度取自提供给 write(2) 的数据量（减去任何提供的地址族）。写入不会阻塞；如果由于暂时原因（如无可用缓冲区空间）无法接受数据包，则静默丢弃；如果原因非暂时性（如数据包过大），则返回错误。

支持以下 ioctl(2) 调用（定义于

`#include <net/if_tun.h>`

`#include <net/if_tun.h>`

**`TUNSDEBUG`** 参数应为指向 `int` 的指针；将内部调试变量设为该值。此变量控制什么（如果有）在此未文档化；参见源代码。

**`TUNGDEBUG`** 参数应为指向 `int` 的指针；将内部调试变量的值存入其中。

**`TUNSIFINFO`** 参数应为指向 `struct tuninfo` 的指针，允许设置隧道设备的 MTU 和波特率。类型必须与 `TUNGIFINFO` 返回的相同或设为 `IFT_PPP`，否则 ioctl(2) 调用将失败。`struct tuninfo` 声明于。此 ioctl 的使用仅限超级用户。

**`TUNGIFINFO`** 参数应为指向 `struct tuninfo` 的指针，当前 MTU、类型和波特率将存入其中。

**`TUNSIFMODE`** 参数应为指向 `int` 的指针；其值必须为 `IFF_POINTOPOINT` 或 `IFF_BROADCAST`，如需多播支持则应将 `IFF_MULTICAST` OR 到该值中。相应“`tun`N”接口的类型设为所提供的类型。如果值超出上述范围，返回 Er EINVAL 错误。接口此时必须处于 down 状态；如果处于 up 状态，返回 Er EBUSY 错误。

**`TUNSLMODE`** 参数应为指向 `int` 的指针；非零值关闭“multi-af”模式并开启“链路层”模式，使从隧道设备读取的数据包附加网络目标地址前缀（见上文）。

**`TUNSIFPID`** 将隧道设备的拥有 pid 设为当前进程的 pid。

**`TUNSIFHEAD`** 参数应为指向 `int` 的指针；非零值关闭“链路层”模式，启用“multi-af”模式，每个数据包前附加四字节地址族。

**`TUNGIFHEAD`** 参数应为指向 `int` 的指针；如果设备处于“multi-af”模式，ioctl 将值设为 1，否则设为 0。

**`TUNSTRANSIENT`** 参数应为指向 `int` 的指针；在 `tun` 设备上设置瞬态标志。瞬态 `tun` 在最后一次关闭时将被销毁。

**`TUNGTRANSIENT`** 参数应为指向 `int` 的指针；将瞬态标志的当前状态（启用或禁用）存入其中。

**`FIONBIO`** 根据参数 `int` 的值是否为零，开启或关闭读取的非阻塞 I/O（写入始终为非阻塞）。

**`FIOASYNC`** 根据参数 `int` 的值是否为零，开启或关闭读取的异步 I/O（即当有数据可读时生成 `SIGIO`）。

**`FIONREAD`** 如果有排队等待读取的数据包，将第一个的大小存入参数 `int`；否则存入零。

**`TIOCSPGRP`** 将启用异步 I/O 时接收 `SIGIO` 信号的进程组设为参数 `int` 值。

**`TIOCGPGRP`** 将 `SIGIO` 信号的进程组值检索到参数 `int` 值中。

控制设备还支持 select(2) 用于读取；为写入选择是没有意义的，并且总是成功，因为写入始终是非阻塞的。

在数据设备的最后一次关闭时，默认情况下接口会被关闭（如同使用 `ifconfig` `tunN` `down`）。所有排队的数据包都被丢弃。如果数据设备未打开时接口处于 up 状态，输出数据包将被丢弃而不是堆积。

## 参见

ioctl(2), read(2), select(2), write(2), devname(3), [inet(4)](inet.4.md), [intro(4)](intro.4.md), [pty(4)](pty.4.md), [tap(4)](tap.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 作者

本 man 页面最初取自 NetBSD。
