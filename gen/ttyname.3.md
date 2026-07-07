# ttyname(3)

`ttyname` — 从文件描述符获取关联终端（tty）的名称

## 名称

`ttyname`, `ttyname_r`, `isatty`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
char *
ttyname(int fd);

int
ttyname_r(int fd, char *buf, size_t len);

int
isatty(int fd);
```

## 描述

这些函数对终端类型设备的文件描述符进行操作。

`isatty` 函数确定文件描述符 `fd` 是否引用有效的终端类型设备。

`ttyname` 函数获取 `isatty` 为真的文件描述符的相关设备名称。

`ttyname` 函数返回存储在静态缓冲区中的名称，该缓冲区在后续调用时会被覆盖。`ttyname_r` 函数接受缓冲区和长度作为参数以避免此问题。

## 返回值

如果 `fd` 引用终端类型设备，`isatty` 函数返回 1；否则返回 0，并可能设置 `errno` 以指示错误。如果找到设备且 `isatty` 为真，`ttyname` 函数返回以 null 结尾的名称；否则返回 `NULL` 指针。`ttyname_r` 函数成功时返回 0。否则返回一个错误号。

## 错误

这些函数可能在以下情况失败：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`ENOTTY`]** 与 `fd` 关联的文件不是终端。

此外，`ttyname_r` 可能在以下情况失败：

**[`ERANGE`]** `bufsize` 参数小于要返回的字符串长度。

## 参见

fdevname(3), [ptsname(3)](../stdlib/ptsname.3.md), tcgetattr(3), [tty(4)](../man4/tty.4.md)

## 历史

`isatty` 和 `ttyname` 函数出现于 Version 7 AT&T UNIX。`ttyname_r` 函数出现于 FreeBSD 6.0。
