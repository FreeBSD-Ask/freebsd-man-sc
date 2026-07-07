# closefrom(2)

`closefrom` — 删除打开的文件描述符

## 名称

`closefrom`, `close_range`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
void
closefrom(int lowfd);

int
close_range(u_int lowfd, u_int highfd, int flags);
```

## 描述

`closefrom()` 系统调用从每进程对象引用表中删除所有大于或等于 `lowfd` 的打开文件描述符。关闭文件描述符时遇到的任何错误都会被忽略。

`close_range()` 系统调用删除 `lowfd` 和 `highfd` 之间（含）的所有打开文件描述符，范围会限制在已打开文件描述符的范围内。关闭文件描述符时遇到的任何错误都会被忽略。支持的 `flags`：

**`CLOSE_RANGE_CLOEXEC`** 对范围内的描述符设置 close-on-exec 标志，而非关闭它们。

**`CLOSE_RANGE_CLOFORK`** 对范围内的描述符设置 close-on-fork 标志，而非关闭它们。

## 返回值

成功完成时，`close_range()` 返回值 0。否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`close_range()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `highfd` 参数小于 `lowfd` 参数。

**[`EINVAL`]** 设置了无效的标志。

## 参见

[close(2)](close.2.md)

## 历史

`closefrom()` 函数首次出现于 FreeBSD 8.0。

`close_range()` 函数首次出现于 FreeBSD 12.2。

`CLOSE_RANGE_CLOFORK` 标志出现于 FreeBSD 15.0。
