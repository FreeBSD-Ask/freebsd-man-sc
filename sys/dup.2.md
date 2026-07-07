# dup(2)

`dup` — 复制现有文件描述符

## 名称

`dup`, `dup2`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
dup(int oldd);

int
dup2(int oldd, int newd);
```

## 描述

`dup()` 系统调用复制现有的对象描述符，并将其值返回给调用进程（`newd` = `dup(oldd)`）。参数 `oldd` 是每进程描述符表中的一个小非负整数索引。该调用返回的新描述符是当前进程未使用的编号最小的描述符。

描述符所引用的对象不以任何方式区分 `oldd` 和 `newd`。因此，如果 `newd` 和 `oldd` 是对同一打开文件的重复引用，[read(2)](read.2.md)、[write(2)](write.2.md) 和 [lseek(2)](lseek.2.md) 调用都移动同一个指向文件的指针，且追加模式、非阻塞 I/O 和异步 I/O 选项在这些引用之间共享。如果需要独立的指向文件的指针，必须通过额外的 [open(2)](open.2.md) 系统调用获取对该文件的不同对象引用。新文件描述符上的 close-on-exec 和 close-on-fork 标志未设置。新文件描述符上的 resolve-beneath 标志设置为与旧文件描述符相同的状态。

在 `dup2()` 中，新描述符 `newd` 的值是指定的。如果该描述符已在使用中且 `oldd` 不等于 `newd`，则该描述符会先被释放，如同使用了 [close(2)](close.2.md) 系统调用。如果 `oldd` 不是有效的描述符，则 `newd` 不会被关闭。如果 `oldd` == `newd` 且 `oldd` 是有效的描述符，则 `dup2()` 成功返回，且不执行任何操作。

## 返回值

这些调用成功时返回新的文件描述符；否则返回值 -1，并设置外部变量 `errno` 以指示错误原因。

## 错误

`dup()` 系统调用在以下情况下会失败：

**[`EBADF`]** `oldd` 参数不是有效的活动描述符。

**[`EMFILE`]** 活动描述符过多。

`dup2()` 系统调用在以下情况下会失败：

**[`EBADF`]** `oldd` 参数不是有效的活动描述符，或 `newd` 参数为负或超过最大允许的描述符编号。

## 参见

[accept(2)](accept.2.md), [close(2)](close.2.md), [fcntl(2)](fcntl.2.md), [getdtablesize(2)](getdtablesize.2.md), [open(2)](open.2.md), [pipe(2)](pipe.2.md), [socket(2)](socket.2.md), [socketpair(2)](socketpair.2.md), [dup3(3)](../gen/dup3.3.md)

## 标准

`dup()` 和 `dup2()` 系统调用预期遵循 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`dup()` 函数出现于 Version 3 AT&T UNIX。`dup2()` 函数出现于 Version 7 AT&T UNIX。
