# tcgetwinsize(3)

`tcgetwinsize` — 获取和设置终端窗口大小

## 名称

`tcgetwinsize`, `tcsetwinsize`

## 库

Lb libc

## 概要

`#include <termios.h>`

```c
struct winsize {
        unsigned short  ws_row;         /* 行数，以字符为单位 */
        unsigned short  ws_col;         /* 列数，以字符为单位 */
        unsigned short  ws_xpixel;      /* 水平尺寸，以像素为单位 */
        unsigned short  ws_ypixel;      /* 垂直尺寸，以像素为单位 */
};
```

```c
int
tcgetwinsize(int fd, struct winsize *w);

int
tcsetwinsize(int fd, const struct winsize *w);
```

## 描述

`tcgetwinsize` 函数获取 `fd` 作为打开文件描述符所对应终端的终端窗口大小，并将其存储到 `w` 所指向的 `winsize` 结构中。

`tcsetwinsize` 函数从 `w` 所引用的 `winsize` 结构设置 `fd` 作为打开文件描述符所对应终端的终端窗口大小。更改立即生效。如果终端的终端窗口大小被成功更改为与 `tcsetwinsize` 调用之前不同的值，则 `SIGWINCH` 信号将发送到终端前台进程组中所有以该终端为控制终端的成员。

上述 `struct winsize` 的声明可能不是字面意义的。它仅用于列出可访问的成员。因此，在调用 `tcsetwinsize` 之前，必须通过调用 `tcgetwinsize` 来初始化 `winsize` 结构的成员。`winsize` 结构中的信息由内核存储，以提供一致的接口，但内核不使用它。

## 返回值

若成功完成，`tcgetwinsize` 和 `tcsetwinsize` 返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。如果 `tcsetwinsize` 失败，终端窗口大小保持不变。

## 错误

以下是可能的失败条件：

**[`EBADF`]** 传递给 `tcgetwinsize` 或 `tcsetwinsize` 的 `fd` 参数不是有效的文件描述符。

**[`ENOTTY`]** 传递给 `tcgetwinsize` 或 `tcsetwinsize` 的 `fd` 参数未关联字符特殊设备。

**[`EINVAL`]** 传递给 `tcsetwinsize` 的 `w` 参数无效。

**[`EFAULT`]** 传递给 `tcgetwinsize` 或 `tcsetwinsize` 的 `w` 参数指向进程分配地址空间之外。

## 参见

stty(1), [ioctl(2)](../sys/ioctl.2.md), [sigaction(2)](../sys/sigaction.2.md), [termios(4)](../man4/termios.4.md), [tty(4)](../man4/tty.4.md)

## 标准

`tcgetwinsize` 和 `tcsetwinsize` 函数预期遵循 IEEE Std 1003.1 ("POSIX.1") 基本规范第 8 版。`struct winsize` 的 `ws_xpixel` 和 `ws_ypixel` 成员是 FreeBSD 扩展。
