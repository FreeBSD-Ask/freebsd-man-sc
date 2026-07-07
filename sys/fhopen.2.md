# fhopen.2

`fhopen` — 通过文件句柄访问文件

## 名称

`fhopen`, `fhstat`, `fhstatfs`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`#include <sys/stat.h>`

```c
int
fhopen(const fhandle_t *fhp, int flags)

int
fhstat(const fhandle_t *fhp, struct stat *sb)

int
fhstatfs(const fhandle_t *fhp, struct statfs *buf)
```

## 描述

这些系统调用提供了在给定文件句柄 `fhp` 的情况下访问文件的方法。由于此方法绕过了目录访问限制，这些调用仅限超级用户使用。

`fhopen()` 系统调用按 `flags` 参数指定的方式打开 `fhp` 所引用的文件进行读取和/或写入，并将文件描述符返回给调用进程。`flags` 参数通过将 [open(2)](open.2.md) 系统调用所用的标志进行*按位或*运算来指定。除 `O_CREAT` 外，所有上述标志均有效。如果文件句柄引用命名属性或命名属性目录，则必须指定 `O_NAMEDATTR` 标志。

`fhstat()` 和 `fhstatfs()` 系统调用提供 fstat(2) 和 fstatfs(2) 调用的功能，区别在于它们返回 `fhp` 所引用文件的信息，而非打开文件的信息。

## 返回值

成功完成时，`fhopen()` 返回所打开文件的文件描述符；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

`fhstat()` 和 `fhstatfs()` 函数在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除分别由 [open(2)](open.2.md)、fstat(2) 和 fstatfs(2) 返回的错误外，`fhopen()`、`fhstat()` 和 `fhstatfs()` 还将返回：

**[`EINVAL`]** 调用 `fhopen()` 时设置了 `O_CREAT`。

**[`ENOATTR`]** 虽然指定了 `O_NAMEDATTR` 标志，但文件句柄并未引用命名属性或命名属性目录。

**[`ENOATTR`]** 文件句柄引用了命名属性或命名属性目录，但未指定 `O_NAMEDATTR` 标志。

**[`ESTALE`]** 文件句柄 `fhp` 已不再有效。

## 参见

fstat(2), fstatfs(2), [getfh(2)](getfh.2.md), [open(2)](open.2.md), [named_attribute(7)](../man7/named_attribute.7.md)

## 历史

`fhopen()`、`fhstat()` 和 `fhstatfs()` 系统调用首次出现于 NetBSD 1.5，由 Alfred Perlstein 适配到 FreeBSD 4.0。

## 作者

本手册页由 William Studenmund 为 NetBSD 编写。
