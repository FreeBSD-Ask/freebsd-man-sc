# dnv(9)

`dnvlist_get` — 获取带有默认值的名称/值对的 API

## 名称

`dnvlist_get`, `dnvlist_take`

## 库

libnv

## 概要

```c
#include <sys/dnv.h>

bool
dnvlist_get_bool(const nvlist_t *nvl, const char *name, bool defval);

uint64_t
dnvlist_get_number(const nvlist_t *nvl, const char *name, uint64_t defval);

char *
dnvlist_get_string(const nvlist_t *nvl, const char *name, const char *defval);

nvlist_t *
dnvlist_get_nvlist(const nvlist_t *nvl, const char *name, nvlist_t *defval);

int
dnvlist_get_descriptor(const nvlist_t *nvl, const char *name, int defval);

void *
dnvlist_get_binary(const nvlist_t *nvl, const char *name, size_t *sizep,
    void *defval, size_t defsize);

bool
dnvlist_take_bool(const nvlist_t *nvl, const char *name, bool defval);

uint64_t
dnvlist_take_number(const nvlist_t *nvl, const char *name, uint64_t defval);

char *
dnvlist_take_string(const nvlist_t *nvl, const char *name, const char *defval);

nvlist_t *
dnvlist_take_nvlist(const nvlist_t *nvl, const char *name, nvlist_t *defval);

int
dnvlist_take_descriptor(const nvlist_t *nvl, const char *name, int defval);

void *
dnvlist_take_binary(const nvlist_t *nvl, const char *name, size_t *sizep,
    void *defval, size_t defsize);
```

## 描述

`libnv` 库允许轻松管理名称/值对，并可以通过套接字发送和接收它们。更多信息参见 [nv(9)](nv.9.md)。

`dnvlist_get` 函数返回与 `name` 关联的值。若名为 `name` 的元素不存在，函数返回 `defval` 中提供的值。返回的字符串、nvlist、描述符、二进制数据或数组不得被用户修改，因为它们仍属于该 nvlist。若 nvlist 处于错误状态，尝试使用这些函数中的任何一个都会导致程序中止。

`dnvlist_take` 函数返回与 `name` 关联的值，并从 `nvl` 中移除关联的元素。若名为 `name` 的元素不存在，返回 `defval` 中提供的值。当值为字符串、二进制或数组值时，调用者负责使用 [free(3)](../man3/free.3.md) 释放返回的内存。当值为 nvlist 时，调用者负责使用 `nvlist_destroy` 销毁返回的 nvlist。当值为描述符时，调用者负责使用 [close(2)](../man2/close.2.md) 关闭返回的描述符。

## 参见

[close(2)](../man2/close.2.md), [free(3)](../man3/free.3.md), [nv(9)](nv.9.md)

## 历史

`dnv` API 出现于 FreeBSD 11.0。

## 作者

`dnv` API 由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD Foundation 赞助下实现。本手册页由 Adam Starak <starak.adam@gmail.com> 编写。
