# uuid(3)

`uuid_compare` — 符合 DCE 1.1 的 UUID 函数

## 名称

`uuid_compare`, `uuid_create`, `uuid_create_nil`, `uuid_equal`, `uuid_from_string`, `uuid_hash`, `uuid_is_nil`, `uuid_to_string`

## 库

Lb libc

## 概要

`#include <uuid.h>`

```c
int32_t
uuid_compare(const uuid_t *uuid1, const uuid_t *uuid2,
    uint32_t *status);

void
uuid_create(uuid_t *uuid, uint32_t *status);

void
uuid_create_nil(uuid_t *uuid, uint32_t *status);

int32_t
uuid_equal(const uuid_t *uuid1, const uuid_t *uuid2,
    uint32_t *status);

void
uuid_from_string(const char *str, uuid_t *uuid, uint32_t *status);

uint16_t
uuid_hash(const uuid_t *uuid, uint32_t *status);

int32_t
uuid_is_nil(const uuid_t *uuid, uint32_t *status);

void
uuid_to_string(const uuid_t *uuid, char **str, uint32_t *status);

void
uuid_enc_le(void *buf, const uuid_t *uuid);

void
uuid_dec_le(const void *buf, uuid_t *);

void
uuid_enc_be(void *buf, const uuid_t *uuid);

void
uuid_dec_be(const void *buf, uuid_t *);
```

## 描述

这一系列符合 DCE 1.1 的 UUID 函数允许应用程序操作通用唯一标识符（UUID）。`uuid_create` 和 `uuid_create_nil` 函数用于创建 UUID。要在二进制表示和字符串表示之间转换，分别使用 `uuid_to_string` 或 `uuid_from_string`。

`uuid_to_string` 函数将 `*str` 设置为指向一个足够大的缓冲区以容纳该字符串。当不再需要时，应将此指针传递给 free(3) 以释放所分配的存储空间。

`uuid_enc_le` 和 `uuid_enc_be` 函数分别将 UUID 的二进制表示编码为小端序和大端序字节顺序的字节流。目标缓冲区必须由调用者预先分配，并且必须足够大以容纳 16 字节的二进制 UUID。这些例程不是 DCE RPC API 的一部分。提供它们是为了方便。

`uuid_dec_le` 和 `uuid_dec_be` 函数分别从小端序和大端序字节顺序的字节流解码 UUID。这些例程不是 DCE RPC API 的一部分。提供它们是为了方便。

`uuid_compare` 和 `uuid_equal` 函数比较两个 UUID 是否相等。如果指针 `a` 和 `b` 相等或都为 `NULL`，或者 `a` 和 `b` 指向的结构相等，则 UUID 相等。`uuid_compare` 在 UUID 相等时返回 0，`a` 小于 `b` 时返回 -1，`a` 大于 `b` 时返回 1。`uuid_equal` 在 UUID 相等时返回 1，不相等时返回 0。

`uuid_is_nil` 函数将 UUID 与 `NULL` 比较。如果 `u` 为 `NULL` 或 UUID 全为零，该函数返回 1，否则返回零。

`uuid_hash` 函数返回指定 UUID 的 16 位哈希值。

## 返回值

函数成功或失败的状态通过 `status` 参数返回。可能的值为：

**`uuid_s_ok`** 函数成功完成。

**`uuid_s_bad_version`** UUID 的版本未知。

**`uuid_s_invalid_string_uuid`** UUID 的字符串表示无效。

**`uuid_s_no_memory`** 函数无法分配内存来存储 UUID 表示。

`uuid_compare`、`uuid_equal`、`uuid_is_nil` 和 `uuid_hash` 始终将 `status` 设置为 `uuid_s_ok`。

## 参见

[uuidgen(1)](../man1/uuidgen.1.md), [uuidgen(2)](../sys/uuidgen.2.md)

## 标准

UUID 函数遵循 DCE 1.1 RPC 规范。

## 缺陷

本手册页有待改进。
