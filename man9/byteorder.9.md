# byteorder(9)

`bswap16` — 字节序操作

## 名称

`bswap16`, `bswap32`, `bswap64`, `be16toh`, `be32toh`, `be64toh`, `htobe16`, `htobe32`, `htobe64`, `htole16`, `htole32`, `htole64`, `le16toh`, `le32toh`, `le64toh`, `be16enc`, `be16dec`, `be32enc`, `be32dec`, `be64enc`, `be64dec`, `le16enc`, `le16dec`, `le32enc`, `le32dec`, `le64enc`, `le64dec`

## 概要

```c
#include <sys/endian.h>

uint16_t
bswap16(uint16_t int16)

uint32_t
bswap32(uint32_t int32)

uint64_t
bswap64(uint64_t int64)

uint16_t
be16toh(uint16_t big16)

uint32_t
be32toh(uint32_t big32)

uint64_t
be64toh(uint64_t big64)

uint16_t
htobe16(uint16_t host16)

uint32_t
htobe32(uint32_t host32)

uint64_t
htobe64(uint64_t host64)

uint16_t
htole16(uint16_t host16)

uint32_t
htole32(uint32_t host32)

uint64_t
htole64(uint64_t host64)

uint16_t
le16toh(uint16_t little16)

uint32_t
le32toh(uint32_t little32)

uint64_t
le64toh(uint64_t little64)

uint16_t
be16dec(const void *)

uint32_t
be32dec(const void *)

uint64_t
be64dec(const void *)

uint16_t
le16dec(const void *)

uint32_t
le32dec(const void *)

uint64_t
le64dec(const void *)

void
be16enc(void *, uint16_t)

void
be32enc(void *, uint32_t)

void
be64enc(void *, uint64_t)

void
le16enc(void *, uint16_t)

void
le32enc(void *, uint32_t)

void
le64enc(void *, uint64_t)
```

## 描述

`bswap16`、`bswap32` 和 `bswap64` 函数返回字节序交换后的整数。在大端序系统上，数字被转换为小端序字节序。在小端序系统上，数字被转换为大端序字节序。

`be16toh`、`be32toh` 和 `be64toh` 函数返回已转换为本机字节序的大端序整数。在大端序系统上，返回值与参数相同。

`le16toh`、`le32toh` 和 `le64toh` 函数返回已转换为本机字节序的小端序整数。在小端序系统上，返回值与参数相同。

`htobe16`、`htobe32` 和 `htobe64` 函数返回已转换为大端序字节序的本机字节序整数。在大端序系统上，返回值与参数相同。

`htole16`、`htole32` 和 `htole64` 函数返回已转换为小端序字节序的本机字节序整数。在小端序系统上，返回值与参数相同。

`be16enc`、`be16dec`、`be32enc`、`be32dec`、`be64enc`、`be64dec`、`le16enc`、`le16dec`、`le32enc`、`le32dec`、`le64enc` 和 `le64dec` 函数以大端序或小端序格式，在任意对齐方式的字节串中编码和解码整数。

## 参见

[byteorder(3)](../man3/byteorder.3.md)

## 历史

`hto*` 和 `*toh` 函数首次出现于 FreeBSD 5.0，最初由 NetBSD 项目开发。

编码/解码函数首次出现于 FreeBSD 5.1。
