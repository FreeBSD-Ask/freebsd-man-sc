# tcsetattr(3)

`cfgetispeed` — 操作 termios 结构

## 名称

`cfgetispeed`, `cfsetispeed`, `cfgetospeed`, `cfsetospeed`, `cfsetspeed`, `cfmakeraw`, `cfmakesane`, `tcgetattr`, `tcsetattr`

## 库

Lb libc

## 概要

```c
#include <termios.h>

speed_t
cfgetispeed(const struct termios *t);

int
cfsetispeed(struct termios *t, speed_t speed);

speed_t
cfgetospeed(const struct termios *t);

int
cfsetospeed(struct termios *t, speed_t speed);

int
cfsetspeed(struct termios *t, speed_t speed);

void
cfmakeraw(struct termios *t);

void
cfmakesane(struct termios *t);

int
tcgetattr(int fd, struct termios *t);

int
tcsetattr(int fd, int action, const struct termios *t);
```

## 描述

`cfmakeraw()`、`cfmakesane()`、`tcgetattr()` 和 `tcsetattr()` 函数用于获取和设置 termios 结构。

`cfgetispeed()`、`cfsetispeed()`、`cfgetospeed()`、`cfsetospeed()` 和 `cfsetspeed()` 函数用于获取和设置 termios 结构中的波特率值。这些函数对终端的影响（如下所述）在调用 `tcsetattr()` 函数之前不会生效，也不是所有错误都能被检测到。在 termios 结构中设置并传递给 `tcsetattr()` 的某些波特率值具有特殊含义。这些将在手册页中描述 `tcsetattr()` 函数的部分中讨论。

## 获取和设置波特率

输入和输出波特率存在于 termios 结构中。无符号整数 `speed_t` 在 `termios.h` 头文件中通过 typedef 定义。该整数的值直接对应于所表示的波特率，但是，以下符号值已被定义。

```c
#define B0      0
#define B50     50
#define B75     75
#define B110    110
#define B134    134
#define B150    150
#define B200    200
#define B300    300
#define B600    600
#define B1200   1200
#define B1800   1800
#define B2400   2400
#define B4800   4800
#define B9600   9600
#define B19200  19200
#define B38400  38400
#ifndef _POSIX_SOURCE
#define EXTA    19200
#define EXTB    38400
#endif  /*_POSIX_SOURCE */
```

`cfgetispeed()` 函数返回 `t` 所引用的 termios 结构中的输入波特率。

`cfsetispeed()` 函数将 `t` 所引用的 termios 结构中的输入波特率设置为 `speed`。

`cfgetospeed()` 函数返回 `t` 所引用的 termios 结构中的输出波特率。

`cfsetospeed()` 函数将 `t` 所引用的 termios 结构中的输出波特率设置为 `speed`。

`cfsetspeed()` 函数将 `t` 所引用的 termios 结构中的输入和输出波特率均设置为 `speed`。

成功完成后，`cfsetispeed()`、`cfsetospeed()` 和 `cfsetspeed()` 函数返回 0。否则，返回 -1，并设置全局变量 `errno` 以指示错误。

## 获取和设置 TERMIOS 状态

本节描述用于控制通用终端接口的函数。除非针对特定命令另有说明，否则这些函数不允许后台进程使用。尝试执行这些操作的进程组将被发送 SIGTTOU 信号。如果调用进程正在阻塞或忽略 SIGTTOU 信号，则允许该进程执行操作，且不发送 SIGTTOU 信号。

在所有函数中，虽然 `fd` 是一个打开的文件描述符，但函数影响的是底层终端文件，而不仅仅是与特定文件描述符关联的打开文件描述。

`cfmakeraw()` 函数将 termios 结构中存储的标志设置为禁用所有输入和输出处理的状态，提供一条“原始 I/O 路径”，而 `cfmakesane()` 函数将它们设置为类似于新创建终端设备的状态。需要注意的是，没有函数可以逆转此效果。这是因为有多种处理选项可以重新启用，正确的方法是应用程序使用 `tcgetattr()` 函数快照当前终端状态，使用 `cfmakeraw()` 或 `cfmakesane()` 以及随后的 `tcsetattr()` 设置原始或合理模式，然后使用保存的状态通过另一个 `tcsetattr()` 恢复到之前的终端状态。

`tcgetattr()` 函数将 `fd` 所引用的终端的参数复制到 `t` 所引用的 termios 结构中。该函数允许从后台进程调用，但是，终端属性可能随后被前台进程更改。

`tcsetattr()` 函数从 `t` 所引用的 termios 结构设置与终端关联的参数。`action` 参数是以下值之一，如 `termios.h` 头文件中所指定：

**`TCSANOW`** 更改立即发生。

**`TCSADRAIN`** 更改在所有写入 `fd` 的输出已传输到终端后发生。当更改影响输出的参数时应使用此 `action` 值。

**`TCSAFLUSH`** 更改在所有写入 `fd` 的输出已传输到终端后发生。此外，任何已接收但未读取的输入都将被丢弃。

`action` 可以通过按位或 `TCSASOFT` 来修改，这将导致 `c_cflag`、`c_ispeed` 和 `c_ospeed` 字段的值被忽略。

0 波特率用于终止连接。如果将 0 指定为 `tcsetattr()` 函数的输出速度，调制解调器控制将不再在终端上生效，从而断开终端连接。

如果将 0 指定为 `tcsetattr()` 函数的输入速度，输入波特率将被设置为与输出波特率相同的值。

如果 `tcsetattr()` 无法进行任何所请求的更改，它返回 -1 并设置 errno。否则，它尽可能进行所有所请求的更改。如果指定的输入和输出波特率不同，且该组合不受支持，则两个波特率都不会被更改。

成功完成后，`tcgetattr()` 和 `tcsetattr()` 函数返回 0。否则，它们返回 -1，并设置全局变量 `errno` 以指示错误，如下所示：

**`[EBADF]`** `tcgetattr()` 或 `tcsetattr()` 的 `fd` 参数不是有效的文件描述符。

**`[EINTR]`** `tcsetattr()` 函数被信号中断。

**`[EINVAL]`** `tcsetattr()` 函数的 `action` 参数无效，或尝试将 termios 结构中表示的属性更改为不支持的值。

**`[ENOTTY]`** `tcgetattr()` 或 `tcsetattr()` 的 `fd` 参数所关联的文件不是终端。

## 参见

[tcsendbreak(3)](tcsendbreak.3.md), [termios(4)](../man4/termios.4.md)

## 标准

`cfgetispeed()`、`cfsetispeed()`、`cfgetospeed()`、`cfsetospeed()`、`tcgetattr()` 和 `tcsetattr()` 函数预期符合 IEEE Std 1003.1-1988 ("POSIX.1") 规范。`cfmakeraw()`、`cfmakesane()` 和 `cfsetspeed()` 函数以及 `tcsetattr()` 函数的 `TCSASOFT` 选项是 IEEE Std 1003.1-1988 ("POSIX.1") 规范的扩展。
