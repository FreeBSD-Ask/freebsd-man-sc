# tap.4

`tap` — 以太网隧道软件网络接口

## 名称

`tap`, `vmnet`

## 概要

`device tuntap`

## 描述

`vmnet` 接口是一种软件回环机制，可以粗略地描述为 [pty(4)](pty.4.md) 的网络接口对应物，也就是说，`vmnet` 之于网络接口就像 [pty(4)](pty.4.md) 驱动之于终端。

`vmnet` 驱动像 [pty(4)](pty.4.md) 驱动一样提供两个接口：一个类似它所模拟的常规设施（在 `vmnet` 的情况下是以太网网络接口，对于 [pty(4)](pty.4.md) 是终端）的接口，以及一个字符特殊设备“控制”接口。客户端程序通过 `vmnet` “控制”接口收发以太网帧。[tun(4)](tun.4.md) 接口在网络层提供类似功能：客户端通过 [tun(4)](tun.4.md) “控制”接口收发（默认情况下）IP 数据包。

网络接口命名为“`tap0`”、“`tap1`”等，每个已打开的控制设备对应一个。这些以太网网络接口会持续存在，直到卸载 `if_tuntap.ko` 模块，或通过“ifconfig destroy”移除（见下文）。

`vmnet` 设备通过接口克隆创建。可使用“ifconfig tap**N** create”命令完成。这是创建 `vmnet` 设备的首选方法。同样可用此方法移除接口，使用“ifconfig tap**N** destroy”命令。

如果 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.tap.devfs_cloning` 不为零，`vmnet` 接口允许在特殊控制设备 **`/dev/tap`** 上进行打开操作。打开此设备时，`vmnet` 将返回最低未使用 `vmnet` 设备的句柄（使用 devname(3) 确定具体是哪一个）。

**禁用旧版 devfs 克隆功能可能破坏使用 `vmnet` 的现有应用程序，如 VMware 和 [ssh(1)](../man1/ssh.1.md)。因此，在另行通知之前，它默认启用。**

控制设备（成功打开后）持续存在，直到卸载 `if_tuntap.ko` 或接口被销毁。

每个接口支持常用的以太网网络接口 ioctl(2)，因此可像其他以太网接口一样与 [ifconfig(8)](../man8/ifconfig.8.md) 一起使用。当系统选择在网络接口上传输以太网帧时，可从控制设备读取该帧（在那里它显示为“输入”）；向控制设备写入以太网帧会在网络接口上生成一个输入帧，就像（不存在的）硬件刚接收到它一样。

以太网隧道设备（通常是 **`/dev/tap`**N）是独占打开的（如果已经打开则无法再打开），并且仅限超级用户使用，除非 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.tap.user_open` 不为零。如果 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.tap.up_on_open` 不为零，则打开控制设备时隧道设备会被标记为“up”。如果接口未“ready”，Fn read 调用将返回错误（Er EHOSTDOWN）。一旦接口就绪，Fn read 将返回可用的以太网帧；如果没有，则要么阻塞直到有帧可用，要么返回 Er EWOULDBLOCK，取决于是否启用了非阻塞 I/O。如果帧长度超过传递给 Fn read 的缓冲区允许长度，额外数据将被静默丢弃。

write(2) 调用将以太网帧传入以在伪接口上“接收”。每次 Fn write 调用恰好提供一帧；帧长度取自提供给 Fn write 的数据量。写入不会阻塞；如果由于暂时原因（如无可用缓冲区空间）无法接受帧，则静默丢弃；如果原因非暂时性（如帧过大），则返回错误。支持以下 ioctl(2) 调用（定义于

`#include <net/if_tap.h>`

**`TAPSIFINFO`** 设置网络接口信息（线路速率和 MTU）。类型必须与 `TAPGIFINFO` 返回的相同或设为 `IFT_ETHER`，否则 ioctl(2) 调用将失败。参数应为指向 `struct tapinfo` 的指针。

**`TAPGIFINFO`** 检索网络接口信息（线路速率、MTU 和类型）。参数应为指向 `struct tapinfo` 的指针。

**`TAPSDEBUG`** 参数应为指向 `int` 的指针；将内部调试变量设为该值。此变量控制什么（如果有）在此未文档化；参见源代码。

**`TAPGDEBUG`** 参数应为指向 `int` 的指针；将内部调试变量的值存入其中。

**`TAPGIFNAME`** 检索网络接口名。参数应为指向 `struct ifreq` 的指针。接口名将在 `ifr_name` 字段中返回。

**`TAPSTRANSIENT`** 参数应为指向 `int` 的指针；在 `vmnet` 设备上设置瞬态标志。瞬态 `vmnet` 在最后一次关闭时将被销毁。

**`TAPGTRANSIENT`** 参数应为指向 `int` 的指针；将瞬态标志的当前状态（启用或禁用）存入其中。

**`FIONBIO`** 根据参数 `int` 的值是否为零，开启或关闭读取的非阻塞 I/O（写入始终为非阻塞）。

**`FIOASYNC`** 根据参数 `int` 的值是否为零，开启或关闭读取的异步 I/O（即当有数据可读时生成 `SIGIO`）。

**`FIONREAD`** 如果有排队的帧可读，将第一帧的大小存入参数 `int`；否则存入零。

**`TIOCSPGRP`** 将启用异步 I/O 时接收 `SIGIO` 信号的进程组设为参数 `int` 的值。

**`TIOCGPGRP`** 将 `SIGIO` 信号的进程组值检索到参数 `int` 中。

**`SIOCGIFADDR`** 检索“远端”的媒体访问控制（`MAC`）地址。此命令由 VMware 移植使用，预期在与控制设备关联的描述符上执行（通常是 **`/dev/vmnet`**N 或 **`/dev/tap`**N）。作为参数传递的 `buffer` 应有足够空间存储 `MAC` 地址。在打开时，“本地”和“远端” `MAC` 地址相同，因此此命令可用于检索“本地” `MAC` 地址。

**`SIOCSIFADDR`** 设置“远端”的媒体访问控制（`MAC`）地址。此命令由 VMware 移植使用，预期在与控制设备关联的描述符上执行（通常是 **`/dev/vmnet`**N）。

控制设备还支持 select(2) 用于读取；为写入选择是没有意义的，并且总是成功，因为写入始终是非阻塞的。

在数据设备的最后一次关闭时，接口会被关闭（如同使用“ifconfig tap**N** down”）并删除所有已配置的地址，除非该设备是 *VMnet* 设备或设置了 `IFF_LINK0` 标志。所有排队的帧都被丢弃。如果数据设备未打开时接口处于 up 状态，输出帧将被丢弃而不是堆积。

`vmnet` 设备也可与 VMware 移植一起使用，作为旧版 *VMnet* 设备驱动的替代。当控制设备关闭时，*VMnet* 设备不会通过 [ifconfig(8)](../man8/ifconfig.8.md) 自行关闭。其他方面都相同。

除上述 ioctl(2) 调用外，VMware 移植还有一个额外的调用。

**`VMIO_SIOCSIFFLAGS`** VMware `SIOCSIFFLAGS`。

## 参见

[inet(4)](inet.4.md), [intro(4)](intro.4.md), [tun(4)](tun.4.md)
