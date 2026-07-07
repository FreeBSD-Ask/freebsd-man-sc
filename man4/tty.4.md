# tty(4)

`tty` — 通用终端接口

## 名称

`tty`

## 概要

`#include <sys/ioctl.h>`

## 描述

本节描述系统中终端驱动程序的接口。

### 终端特殊文件

系统上的每个硬件终端端口在 **`/dev/`** 目录中都有多个与之关联的终端特殊设备文件（例如 **`/dev/tty03`** 和 **`/dev/cua03`**）。当用户通过这些硬件终端端口之一登录系统时，系统已经打开了关联的设备，并将线路准备为正常的交互使用（参见 getty(8)）。还有一种特殊情况，终端文件并不连接到硬件终端端口，而是连接到另一侧的另一个程序。这种特殊终端设备称为 *pty*，提供了必要的机制，使得用户通过网络登录时（例如使用 [telnet(1)](../man1/telnet.1.md)）能获得相同的系统接口。即使在这些情况下，终端文件如何打开和设置的细节也已由系统中的特殊软件处理。因此，用户通常无需担心这些线路如何打开或使用的细节。此外，这些线路通常用于从系统拨出（通过外呼调制解调器），但系统同样提供了隐藏访问这些终端特殊文件细节的程序（参见 tip(1)）。

当交互用户登录时，系统会将线路准备为以特定方式运行（称为 *线路规程*），其具体细节在命令层级的 stty(1) 和编程层级的 [termios(4)](termios.4.md) 中描述。用户可能需要更改与其特定登录终端相关的设置，对于常见情况应参考前述 man 页面。本 man 页面的其余部分涉及描述低层级使用和控制终端设备的细节，例如希望提供类似于系统所提供功能的程序可能需要的内容。

### 终端文件操作

以下所有操作都通过 ioctl(2) 系统调用发起。关于 *request* 和 *argp* 参数的描述，请参考该 man 页面。除这里定义的 ioctl *request* 外，当前生效的特定线路规程还会定义特定于它的其他 *request*（实际上 [termios(4)](termios.4.md) 将它们定义为函数调用，而非 ioctl *request*）。以下章节列出了可用的 ioctl request。列出了 request 的名称、用途描述以及带类型的 *argp* 参数（如果有）。例如，第一个条目为

> *TIOCSPGRP int *tpgrp*

并通过以下代码片段在与文件描述符零关联的终端上调用：

```sh
	int pgrp;
	pgrp = getpgrp();
	ioctl(0, TIOCSPGRP, &pgrp);
```

### 终端文件 request 描述

`#include <sys/file.h>`

`#include <sys/ioctl.h>`

**TIOCM_LE** 线路启用（Line Enable）。
**TIOCM_DTR** 数据终端就绪（Data Terminal Ready）。
**TIOCM_RTS** 请求发送（Request To Send）。
**TIOCM_ST** 辅助发送（Secondary Transmit）。
**TIOCM_SR** 辅助接收（Secondary Receive）。
**TIOCM_CTS** 清除发送（Clear To Send）。
**TIOCM_CAR** 载波检测（Carrier Detect）。
**TIOCM_CD** 载波检测（同义词）。
**TIOCM_RNG** 振铃指示（Ring Indication）。
**TIOCM_RI** 振铃指示（同义词）。
**TIOCM_DSR** 数据集就绪（Data Set Ready）。

**`TIOCSETD`** `int *ldisc` 此调用已弃用，但为兼容性而保留。在 FreeBSD 8.0 之前，它会切换到 `ldisc` 所指向的新线路规程。

**`TIOCGETD`** `int *ldisc` 在 `ldisc` 所指向的整数中返回当前线路规程。

**`TIOCSBRK`** `void` 将终端硬件设置为 BREAK 状态。

**`TIOCCBRK`** `void` 清除终端硬件的 BREAK 状态。

**`TIOCSDTR`** `void` 置位数据终端就绪（DTR）。

**`TIOCCDTR`** `void` 清除数据终端就绪（DTR）。

**`TIOCGPGRP`** `int *tpgrp` 在 `tpgrp` 所指向的整数中返回与终端关联的当前进程组。这是实现 [termios(4)](termios.4.md) Fn tcgetattr 调用的底层调用。

**`TIOCSPGRP`** `int *tpgrp` 将终端与 `tpgrp` 所指向的进程组（作为整数）关联。这是实现 [termios(4)](termios.4.md) Fn tcsetattr 调用的底层调用。

**`TIOCGETA`** `struct termios *term` 将与设备关联的 termios 状态的当前值放入 `term` 所指向的 termios 结构中。这是实现 [termios(4)](termios.4.md) Fn tcgetattr 调用的底层调用。

**`TIOCSETA`** `struct termios *term` 立即设置与设备关联的 termios 状态。这是实现 [termios(4)](termios.4.md) Fn tcsetattr 调用（带 `TCSANOW` 选项）的底层调用。

**`TIOCSETAW`** `struct termios *term` 首先等待任何输出完成，然后设置与设备关联的 termios 状态。这是实现 [termios(4)](termios.4.md) Fn tcsetattr 调用（带 `TCSADRAIN` 选项）的底层调用。

**`TIOCSETAF`** `struct termios *term` 首先等待任何输出完成，清除所有挂起的输入，然后设置与设备关联的 termios 状态。这是实现 [termios(4)](termios.4.md) Fn tcsetattr 调用（带 `TCSAFLUSH` 选项）的底层调用。

**`TIOCOUTQ`** `int *num` 将输出队列中的当前字符数放入 `num` 所指向的整数中。

**`TIOCSTI`** `char *cp` 模拟键入输入。假装终端接收到了 `cp` 所指向的字符。

**`TIOCNOTTY`** `void` 过去，当没有控制终端的进程（参见 [termios(4)](termios.4.md) 中的 *控制终端* 部分）首次打开终端设备时，它会将该终端作为其控制终端。对于某些程序来说这是一种隐患，因为它们根本不需要控制终端，而此调用提供了将控制终端与调用进程分离的机制。它*必须*通过打开文件 **`/dev/tty`** 并在该文件描述符上调用 `TIOCNOTTY` 来调用。当前系统不会在 Fn open 调用时为进程分配控制终端：有一个名为 `TIOCSCTTY` 的特定 ioctl 用于将终端设为控制终端。此外，程序可以 Fn fork 并调用 Fn setsid 系统调用，这会将进程置入其自己的会话中——效果是将其与控制终端分离。这是程序失去控制终端的新的、首选方法。但是，环境限制可能禁止进程 Fn fork 并调用 Fn setsid 系统调用以将其与控制终端分离。在这种情况下，必须使用 `TIOCNOTTY`。

**`TIOCSTOP`** `void` 停止终端上的输出（类似于在键盘上键入 ^S）。

**`TIOCSTART`** `void` 启动终端上的输出（类似于在键盘上键入 ^Q）。

**`TIOCSCTTY`** `void` 将终端设为该进程的控制终端（该进程当前必须没有控制终端）。

**`TIOCDRAIN`** `void` 等待直到所有输出排空，或直到排空等待超时到期。

**`TIOCGDRAINWAIT`** `int *timeout` 以秒为单位返回当前的排空等待超时。

**`TIOCSDRAINWAIT`** `int *timeout` 以秒为单位设置排空等待超时。值为零则禁用超时。默认的排空等待超时由可调的 [sysctl(8)](../man8/sysctl.8.md) OID `kern.tty_drainwait` 控制。

**`TIOCEXCL`** `void` 在终端上设置独占使用。不允许进一步打开，root 除外。当然，这意味着由 root（或 setuid）运行的程序不会遵守独占设置——这限制了此功能的实用性。

**`TIOCNXCL`** `void` 清除终端的独占使用。允许进一步打开。

**`TIOCFLUSH`** `int *what` 如果 `what` 所指向的 int 值包含 `FREAD` 位（如中定义），则清除输入队列中的所有字符。如果包含 `FWRITE` 位，则清除输出队列中的所有字符。如果该整数值为零，则行为如同同时设置了 `FREAD` 和 `FWRITE` 位（即清除两个队列）。

**`TIOCGWINSIZE`** `struct winsize *ws` 将与终端关联的窗口大小信息放入 `ws` 所指向的 `winsize` 结构中。窗口大小结构包含连接到终端的设备的行数和列数（以及像素数，如适用）。它由用户软件设置，是大多数面向全屏的程序确定屏幕大小的方式。`winsize` 结构由提供

**`TIOCSWINSZ`** `struct winsize *ws` 将与终端关联的窗口大小设置为 `ws` 所指向的 `winsize` 结构中的值（见上文）。

**`TIOCCONS`** `int *on` 如果 `on` 指向非零整数，则将内核控制台输出（内核 printf）重定向到此终端。如果 `on` 指向零整数，则将内核控制台输出重定向回正常控制台。这通常在工作站上用于将内核消息重定向到特定窗口。

**`TIOCMSET`** `int *state` `state` 所指向的整数包含与调制解调器状态对应的位。以下是已定义变量及其所代表调制解调器状态的列表：此调用将终端调制解调器状态设置为 `state` 所表示的状态。并非所有终端都支持此调用。

**`TIOCMGET`** `int *state` 在 `state` 所指向的整数中返回上述调制解调器线路的当前状态。

**`TIOCMBIS`** `int *state` `state` 所指向的整数中的位表示调制解调器状态（如上所述），但该状态会与当前状态进行 OR 操作。

**`TIOCMBIC`** `int *state` `state` 所指向的整数中的位表示调制解调器状态（如上所述），但 `state` 中开启的每一位在终端中都会被清除。

## 实现说明

通过所有终端设备的输入和输出字节总数可通过 `kern.tty_nin` 和 `kern.tty_nout` 只读 [sysctl(8)](../man8/sysctl.8.md) 变量获取。

## 参见

stty(1), ioctl(2), [ng_tty(4)](ng_tty.4.md), [pts(4)](pts.4.md), [pty(4)](pty.4.md), [termios(4)](termios.4.md), [uart(4)](uart.4.md), getty(8)

## 历史

控制台打字机设备 **`/dev/tty`** 和异步通信接口 **`/dev/tty[0-5]`** 首次出现于 Version 1 AT&T UNIX。

## 缺陷

在互联网出现之前，串口主要用于来自终端的入站连接（直接或通过调制解调器），如今串口主要用于到设备的出站连接，这一演变不幸地将相关文档分散在三个不同的 man 页面中：[termios(4)](termios.4.md)、[uart(4)](uart.4.md)、[tty(4)](tty.4.md)。
