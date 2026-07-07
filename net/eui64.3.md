# eui64(3)

`eui64` — IEEE EUI-64 转换与查找例程

## 名称

`eui64`, `eui64_aton`, `eui64_ntoa`, `eui64_ntohost`, `eui64_hostton`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/eui64.h>`

```c
int
eui64_aton(const char *a, struct eui64 *e);

int
eui64_ntoa(const struct eui64 *id, char *a, size_t len);

int
eui64_ntohost(char *hostname, size_t len, const struct eui64 *id);

int
eui64_hostton(const char *hostname, struct eui64 *id);
```

## 描述

这些函数使用 `eui64` 结构操作 IEEE EUI-64，该结构定义于头文件

`#include <sys/eui64.h>`

```c
/*
 * EUI-64 的字节数。
 */
#define EUI64_LEN		8
/*
 * IEEE EUI-64 的结构。
 */
struct  eui64 {
        u_char octet[EUI64_LEN];
};
```

`eui64_aton` 函数将 EUI-64 的 ASCII 表示转换为 `eui64` 结构。相应地，`eui64_ntoa` 将以 `eui64` 结构指定的 EUI-64 转换为 ASCII 字符串。

`eui64_ntohost` 和 `eui64_hostton` 函数按照 **/etc/eui64** 数据库中的指定，将 EUI-64 映射到对应的主机名。`eui64_ntohost` 函数从 EUI-64 转换为主机名，`eui64_hostton` 从主机名转换为 EUI-64。

## 返回值

成功时，`eui64_ntoa` 返回指向包含 EUI-64 ASCII 表示的字符串的指针。如果无法转换所提供的 `eui64` 结构，则返回 `NULL` 指针。类似地，`eui64_aton` 成功时返回指向 `eui64` 结构的指针，失败时返回 `NULL` 指针。

`eui64_ntohost` 和 `eui64_hostton` 函数成功时返回零，如果无法在 **/etc/eui64** 数据库中找到匹配项，则返回非零值。

## 注释

用户必须确保传递给 `eui64_ntohost` 和 `eui64_hostton` 函数的主机名字符串足够大，以容纳返回的主机名。

## NIS 交互

如果 **/etc/eui64** 包含一行仅有单个 `+`，`eui64_ntohost` 和 `eui64_hostton` 函数除查询 **/etc/eui64** 文件中的数据外，还会尝试查询 NIS 的 `eui64.byname` 和 `eui64.byid` 映射。

## 参见

[firewire(4)](../man4/firewire.4.md), [eui64(5)](../man5/eui64.5.md), [yp(8)](../man8/yp.8.md)

## 历史

这些函数首次出现于 FreeBSD 5.3。它们派生自 [ethers(3)](ethers.3.md) 函数族。
