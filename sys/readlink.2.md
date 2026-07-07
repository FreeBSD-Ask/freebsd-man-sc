# readlink(2)

`readlink` — 读取符号链接的值

## 名称

`readlink`, `readlinkat`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
ssize_t
readlink(const char *restrict path, char *restrict buf,
    size_t bufsiz);

ssize_t
readlinkat(int fd, const char *restrict path, char *restrict buf,
    size_t bufsize);
```

## 描述

`readlink()` 系统调用将符号链接 `path` 的内容放入缓冲区 `buf` 中，该缓冲区大小为 `bufsiz`。`readlink()` 系统调用不会在 `buf` 末尾追加 `NUL` 字符。

`readlinkat()` 系统调用等效于 `readlink()`，但当 `path` 指定相对路径时有所不同。此时，读取其内容的符号链接相对于与文件描述符 `fd` 关联的目录，而不是当前工作目录。如果向 `readlinkat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为与调用 `readlink()` 相同。

## 返回值

调用成功时返回放入缓冲区的字符数，出错时返回 -1，并将错误代码存入全局变量 `errno`。

## 错误

`readlink()` 系统调用在以下情况下会失败：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`EACCES`]** 对路径前缀的某个组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EINVAL`]** 指定的文件不是符号链接。

**[`EIO`]** 从文件系统读取时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EFAULT`]** `buf` 参数超出了进程分配的地址空间。

除 `readlink()` 返回的错误外，`readlinkat()` 还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD`，也不是用于搜索的有效文件描述符。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD`，也不是与目录关联的文件描述符。

## 参见

[fhreadlink(2)](fhreadlink.2.md), lstat(2), [stat(2)](stat.2.md), [symlink(2)](symlink.2.md), symlink(7)

## 标准

`readlinkat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`readlink()` 系统调用首次出现于 4.2BSD。`readlinkat()` 系统调用首次出现于 FreeBSD 8.0。
