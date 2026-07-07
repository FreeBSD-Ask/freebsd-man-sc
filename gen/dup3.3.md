# dup3(3)

`dup3` — 复制一个现有文件描述符

## 名称

`dup3`

## 库

libc

## 概要

`#include <fcntl.h>`

`#include <unistd.h>`

```c
int
dup3(int oldd, int newd, int flags);
```

## 描述

`dup3` 函数复制一个现有对象描述符，同时允许指定新描述符的值。

新文件描述符上的 close-on-exec 标志由 `flags` 中的 `O_CLOEXEC` 位决定。

新文件描述符上的 close-on-fork 标志由 `flags` 中的 `O_CLOFORK` 位决定。

新文件描述符上的 resolve-beneath 标志会被保留。

如果 `oldd` != `newd` 且 `flags` == 0，其行为等同于 `dup2(oldd, newd)` 。

如果 `oldd` == `newd` ，则 `dup3` 失败，这与 dup2(2) 不同。

## 返回值

如果发生错误，返回 -1。外部变量 `errno` 指示错误原因。

## 错误

`dup3` 函数在以下情况下会失败：

**`[EBADF]`** `oldd` 参数不是一个有效的活动描述符，或 `newd` 参数为负或超过最大允许的描述符编号。

**`[EINVAL]`** `oldd` 参数等于 `newd` 参数。

**`[EINVAL]`** `flags` 参数中设置了 `O_CLOEXEC` 或 `O_CLOFORK` 以外的位。

## 参见

[accept(2)](../sys/accept.2.md), [close(2)](../sys/close.2.md), dup2(2), [fcntl(2)](../sys/fcntl.2.md), [getdtablesize(2)](../sys/getdtablesize.2.md), [open(2)](../sys/open.2.md), [pipe(2)](../sys/pipe.2.md), [socket(2)](../sys/socket.2.md), [socketpair(2)](../sys/socketpair.2.md)

## 标准

`dup3` 函数不遵循任何标准。

## 历史

`dup3` 函数出现于 FreeBSD 10.0。`O_CLOFORK` 标志出现于 FreeBSD 15.0。
