# if_indextoname(3)

`if_nametoindex` — 提供接口名与索引之间的映射

## 名称

`if_nametoindex`, `if_indextoname`, `if_nameindex`, `if_freenameindex`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <net/if.h>`

```c
unsigned int
if_nametoindex(const char *ifname);

char *
if_indextoname(unsigned int ifindex, char *ifname);

struct if_nameindex *
if_nameindex(void);

void
if_freenameindex(struct if_nameindex *ptr);
```

## 描述

`if_nametoindex` 函数将 `ifname` 中指定的接口名映射到其对应的索引。如果指定的接口不存在，返回 0。

`if_indextoname` 函数将 `ifindex` 中指定的接口索引映射到其对应的名称，该名称被复制到 `ifname` 所指向的缓冲区中，此缓冲区必须至少为 `IFNAMSIZ` 字节。该指针也是函数的返回值。如果没有与指定索引对应的接口，返回 `NULL`。

`if_nameindex` 函数返回一个 `if_nameindex` 结构数组，每个接口对应一个结构，定义于包含文件

`#include <net/if.h>`

`if_nameindex` 结构至少包含以下条目：

```c
    unsigned int   if_index;  /* 1, 2, ... */
    char          *if_name;   /* 以 null 结尾的名称："le0", ... */
```

结构数组的末尾由一个 `if_index` 为 0 且 `if_name` 为 `NULL` 的结构指示。出错时返回 `NULL` 指针。

`if_freenameindex` 函数释放由 `if_nameindex` 分配的动态内存。

## 返回值

成功完成时，`if_nametoindex` 返回接口的索引号。如果未找到接口，返回 0 并将 `errno` 设置为 `ENXIO`。如果通过 [getifaddrs(3)](getifaddrs.3.md) 检索接口列表时发生错误，也返回 0。

成功完成时，`if_indextoname` 返回 `ifname`。如果未找到接口，返回 `NULL` 指针并将 `errno` 设置为 `ENXIO`。如果通过 [getifaddrs(3)](getifaddrs.3.md) 检索接口列表时发生错误，也返回 `NULL` 指针。

`if_nameindex` 在通过 [getifaddrs(3)](getifaddrs.3.md) 检索接口列表时发生错误，或无法分配足够内存时，返回 `NULL` 指针。

## 参见

[getifaddrs(3)](getifaddrs.3.md), networking(4)

## 标准

`if_nametoindex`、`if_indextoname`、`if_nameindex` 和 `if_freenameindex` 函数遵循 RFC 2553。

## 历史

该实现首次出现于 BSDi BSD/OS。
