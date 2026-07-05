# efirt.9

`efirt` — 内核访问 UEFI 运行时服务

## 名称

`efirt`, `efi_rt_ok`, `efi_get_table`, `efi_get_time`, `efi_get_time_capabilities`, `efi_reset_system`, `efi_set_time`, `efi_var_get`, `efi_var_nextname`, `efi_var_set`

## 概要

```c
options EFIRT
#include <sys/efi.h>
```

```c
int
efi_rt_ok(void)

int
efi_get_table(struct uuid *uuid, void **ptr)

int
efi_get_time(struct efi_tm *tm)

int
efi_get_time_capabilities(struct efi_tmcap *tmcap)

int
efi_reset_system(enum efi_reset type)

int
efi_set_time(struct efi_tm *tm)

int
efi_var_get(uint16_t *name, struct uuid *vendor, uint32_t *attrib,
    size_t *datasize, void *data)

int
efi_var_nextname(size_t *namesize, uint16_t *name, struct uuid *vendor)

int
efi_var_set(uint16_t *name, struct uuid *vendor, uint32_t attrib,
    size_t datasize, void *data)
```

## 描述

如果 UEFI 运行时服务不可用，以下所有调用都将返回 `ENXIO`。`efi_var_set` 当前仅在 amd64 和 arm64 上可用。

`efi_rt_ok` 在 UEFI 运行时服务存在且可用时返回 0，否则返回 `ENXIO`。

`efi_get_table` 函数按 uuid 从 UEFI 系统表获取一个表。找到表时返回 0 并以地址填充 *ptr。如果配置表或系统表未设置则返回 `ENXIO`。如果找不到所请求的表则返回 `ENOENT`。

`efi_get_time` 函数在可用时从 RTC 获取当前时间。成功时返回 0 并填充 `struct efi_tm`。如果 `struct efi_tm` 为 `NULL` 则返回 `EINVAL`，如果由于硬件错误无法获取时间则返回 `EIO`。

`efi_get_time_capabilities` 函数从 RTC 获取能力。成功时返回 0 并填充 `struct efi_tmcap`。如果 `struct efi_tm` 为 `NULL` 则返回 `EINVAL`，如果由于硬件错误无法获取时间则返回 `EIO`。

`efi_reset_system` 函数请求系统重置。`type` 参数可以是以下 `enum efi_reset` 值之一：

**`EFI_RESET_COLD`** 对系统执行冷重置并重启。

**`EFI_RESET_WARM`** 对系统执行热重置并重启。

**`EFI_RESET_SHUTDOWN`** 关闭系统电源。

`efi_set_time` 函数将 RTC 上的时间设置为传入的 `struct efi_tm` 所描述的时间。成功时返回 0，如果时间字段超出范围则返回 `EINVAL`，如果由于硬件错误无法设置时间则返回 `EIO`。

`efi_var_get` 函数获取由 `vendor` 和 `name` 标识的变量。成功时返回 0 并填充 `attrib`、`datasize` 和 `data`。否则返回以下错误之一：

**`ENOENT`** 未找到该变量。

**`EOVERFLOW`** `datasize` 不足以容纳变量数据。`namesize` 会被更新以反映完成请求所需的大小。

**`EINVAL`** `name`、`vendor` 或 `datasize` 中有一个为 NULL。或者 `datasize` 足以容纳响应但 `data` 为 NULL。

**`EIO`** 由于硬件错误无法获取该变量。

**`EDOOFUS`** 由于认证失败无法获取该变量。

`efi_var_nextname` 函数用于枚举变量。在初次调用 `efi_var_nextname` 时，`name` 应为空字符串。后续调用应传入上次返回的 `name` 和 `vendor`，直到返回 `ENOENT`。成功时返回 0 并以下一个变量的数据填充 `namesize`、`name` 和 `vendor`。否则返回以下错误之一：

**`ENOENT`** 未找到下一个变量。

**`EOVERFLOW`** `datasize` 不足以容纳变量数据。`namesize` 会被更新以反映完成请求所需的大小。

**`EINVAL`** `name`、`vendor` 或 `datasize` 中有一个为 NULL。

**`EIO`** 由于硬件错误无法获取该变量。

`efi_var_set` 函数设置由 `name` 和 `vendor` 描述的变量。变量成功设置时返回 0。否则返回以下错误之一：

**`EINVAL`** `attrib` 是无效的属性组合，或 `datasize` 超过允许的最大大小，或 `name` 是空的 Unicode 字符串。

**`EAGAIN`** 没有足够的存储空间来容纳变量及其数据。

**`EIO`** 由于硬件错误无法保存该变量。

**`EROFS`** 所讨论的变量是只读的或不可删除。

**`EDOOFUS`** 由于认证失败无法设置该变量。

**`ENOENT`** 试图更新或删除的变量未找到。

## 参见

[efidev(4)](../man4/efidev.4.md)

## 作者

本手册页由 Kyle Evans <kevans@FreeBSD.org> 编写。
