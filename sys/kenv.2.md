# kenv(2)

`kenv` — 内核环境

## 名称

`kenv`

## 库

Lb libc

## 概要

`#include <kenv.h>`

```c
int
kenv(int action, const char *name, char *value, int len);
```

## 描述

`kenv()` 系统调用用于操作内核环境变量。它支持获取、设置和取消设置环境变量等众所周知的用户态操作，以及转储内核环境中的所有条目的能力。

`action` 参数可以是以下之一：

**`KENV_GET`** 获取具有给定 `name` 的变量的 `value`。`value` 缓冲区的大小由 `len` 给出，应至少为 `KENV_MVALLEN` + 1 字节，以避免截断并确保以 NUL 结尾。

**`KENV_SET`** 设置或添加变量。`name` 和 `value` 分别限制为 `KENV_MNAMELEN` 和 `KENV_MVALLEN` 个字符（不包括 NUL 终止符）。`len` 参数指示 `value` 的长度，必须包含 NUL 终止符。此选项仅对超级用户可用。

**`KENV_UNSET`** 取消设置具有给定 `name` 的变量。`value` 和 `len` 参数被忽略。此选项仅对超级用户可用。

**`KENV_DUMP`** 将尽可能多的动态内核环境转储到 `value` 中，其大小由 `len` 给出。如果 `value` 为 `NULL`，`kenv()` 将返回复制出整个环境所需的字节数。`name` 被忽略。

**`KENV_DUMP_LOADER`** 转储由 [loader(8)](../man8/loader.8.md) 提供的静态环境，语义与 `KENV_DUMP` 相同。最初存在于此环境中的重复和格式错误的变量会被内核丢弃，不会出现在输出中。

**`KENV_DUMP_STATIC`** 转储由 config(5) 定义的静态环境。语义与 `KENV_DUMP_LOADER` 相同。

## 返回值

`kenv()` 系统调用在 `KENV_SET` 和 `KENV_UNSET` 成功时返回 0，在 `KENV_DUMP` 和 `KENV_GET` 的情况下返回复制到 `value` 中的字节数。如果发生错误，返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`kenv()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `action` 参数不是有效选项，或对于 `KENV_SET`，`value` 的长度小于 1。

**[`ENOENT`]** 对于 `KENV_GET` 或 `KENV_UNSET`，找不到 `name` 对应的值。

**[`ENOENT`]** 对于 `KENV_DUMP_LOADER` 或 `KENV_DUMP_STATIC`，请求的环境不可用。内核默认配置为销毁这些环境。

**[`EPERM`]** 非超级用户尝试设置或取消设置内核环境变量。

**[`EPERM`]** 非超级用户尝试从内核环境获取变量或转储内核环境，且 `security.bsd.unprivileged_kenv_read` sysctl 设置为 0。

**[`EFAULT`]** 在尝试将用户参数复制进来或将值复制出去时遇到错误地址。

**[`ENAMETOOLONG`]** `name` 或 `value` 分别长于 `KENV_MNAMELEN` 或 `KENV_MVALLEN` 个字符，或对于 `KENV_SET`，`len` 未包含 NUL 终止符。

## 参见

[kenv(1)](../man1/kenv.1.md)

## 作者

本手册页由 Chad David <davidc@FreeBSD.org> 编写。

`kenv()` 系统调用由 Maxime Henrion <mux@FreeBSD.org> 编写。
