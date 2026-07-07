# rtld_get_var(3)

`rtld_get_var` — 在映像激活后查询或更改运行时链接器参数

## 名称

`rtld_get_var`, `rtld_set_var`

## 库

Lb libc

## 概要

`#include <sys/errno.h>`

`#include <link.h>`

```c
const char *
rtld_get_var(const char *name);

int
rtld_set_var(const char *name, const char *value);
```

## 描述

动态链接器 rtld(1) 可以通过在映像激活前为进程设置某些环境变量来进行配置。有时需要在事后查询当前生效的设置或对其进行更改。

由于进程环境变量由较高级别的库维护，运行时链接器在映像激活后无法访问它们。所述函数使得操作 rtld 设置成为可能。

`rtld_get_var` 函数返回指定参数的当前值。

`rtld_set_var` 函数在可能的情况下将参数的值更改为新的 `value` 值。两个函数的 `name` 参数均为参数名，与对应的环境变量（参见 rtld(1)）相同，但不带 `LD_`（或 `LD_32_` 或任何其他 ABI 特定的）前缀。

可使用 `rtld_set_var` 函数修改的变量列表为：

**`LD_BIND_NOT`**

**`LD_BIND_NOW`**

**`LD_DEBUG`**

**`LD_DUMP_REL_PRE`**

**`LD_DUMP_REL_POST`**

**`LD_DYNAMIC_WEAK`**

**`LD_LIBMAP_DISABLE`**

**`LD_LIBRARY_PATH`**

**`LD_LIBRARY_PATH_FDS`**

**`LD_LIBRARY_PATH_RPATH`**

**`LD_LOADFLTR`**

## 返回值

`rtld_get_var` 返回指定参数的当前值，如果名称无效则返回 `NULL`。

`rtld_set_var` 成功时返回 0，或返回一个指示阻止该操作的错误条件的整数。

## 错误

`rtld_set_var` 可能返回的错误：

**[`EPERM`]** 请求的更改无法在运行时进行，要么因为运行时链接器只能在初始化时接受此参数，要么因为当前进程正在以提升的权限执行。

**[`ENOENT`]** 提供的参数 `name` 未知。

## 参见

[rtld(1)](../man1/rtld.1.md)

## 历史

`rtld_get_var` 函数首次出现于 FreeBSD 14.3。
