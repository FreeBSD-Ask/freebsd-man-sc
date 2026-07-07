# tcsendbreak(3)

`tcsendbreak` — 线路控制函数

## 名称

`tcsendbreak`, `tcdrain`, `tcflush`, `tcflow`

## 库

Lb libc

## 概要

```c
#include <termios.h>

int
tcdrain(int fd);

int
tcflow(int fd, int action);

int
tcflush(int fd, int action);

int
tcsendbreak(int fd, int len);
```

## 描述

`tcdrain()` 函数等待，直到写入到由 `fd` 所引用终端的所有输出都已发送到该终端为止。

`tcflow()` 函数根据 `action` 的值，暂停向 `fd` 所引用终端的数据发送或从该终端的数据接收。 `action` 的值必须是以下之一：

**`TCOOFF`** 暂停输出。

**`TCOON`** 恢复已暂停的输出。

**`TCIOFF`** 发送一个 STOP 字符，旨在使终端停止向系统发送数据。（参见 [termios(4)](../man4/termios.4.md) 中 `Input Modes` 章节对 IXOFF 的描述。）

**`TCION`** 发送一个 START 字符，旨在使终端开始向系统发送数据。（参见 [termios(4)](../man4/termios.4.md) 中 `Input Modes` 章节对 IXOFF 的描述。）

`tcflush()` 函数根据 `action` 的值，丢弃写入到由 `fd` 所引用终端但尚未发送到该终端的任何数据，或从该终端接收到但尚未读取的任何数据。 `action` 的值必须是以下之一：

**`TCIFLUSH`** 刷新已接收但未读取的数据。

**`TCOFLUSH`** 刷新已写入但未发送的数据。

**`TCIOFLUSH`** 同时刷新已接收但未读取的数据和已写入但未发送的数据。

`tcsendbreak()` 函数向 `fd` 所引用的终端发送持续十分之四秒的零值位流。在本实现中忽略 `len` 参数。

## 返回值

若成功完成，所有这些函数都返回零。

## 错误

如果发生任何错误，返回 -1，并设置全局变量 `errno` 以指示错误，如下所示：

**`[EBADF]`** `fd` 参数不是一个有效的文件描述符。

**`[EINVAL]`** `action` 参数不是一个有效的值。

**`[ENOTTY]`** 与 `fd` 关联的文件不是一个终端。

**`[EINTR]`** 一个信号中断了 `tcdrain()` 函数。

**`[EWOULDBLOCK]`** 在 `tcdrain()` 函数写入所有缓冲输出之前，所配置的超时时间已到。

## 参见

[tcsetattr(3)](tcsetattr.3.md), [termios(4)](../man4/termios.4.md), [tty(4)](../man4/tty.4.md), comcontrol(8)

## 标准

`tcsendbreak()`、`tcflush()` 和 `tcflow()` 函数预计符合 IEEE Std 1003.1-1988 ("POSIX.1") 规范。

当使用 comcontrol(8) 将排空等待值设置为零，或使用 [ioctl(2)](../sys/ioctl.2.md) 的 `TIOCSDRAINWAIT`，或使用 [sysctl(8)](../man8/sysctl.8.md) 的 `kern.tty_drainwait` 时， `tcdrain()` 函数预计符合 IEEE Std 1003.1-1988 ("POSIX.1")。非零的排空等待值可能导致 `tcdrain()` 在未写入所有输出的情况下返回 `EWOULDBLOCK`。 `kern.tty_drainwait` 的默认值为 300 秒。
