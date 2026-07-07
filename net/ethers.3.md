# ethers(3)

`ethers` — 以太网地址转换与查找例程

## 名称

`ethers`, `ether_line`, `ether_aton`, `ether_aton_r`, `ether_ntoa`, `ether_ntoa_r`, `ether_ntohost`, `ether_hostton`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <net/ethernet.h>`

```c
int
ether_line(const char *l, struct ether_addr *e, char *hostname);

struct ether_addr *
ether_aton(const char *a);

struct ether_addr *
ether_aton_r(const char *a, struct ether_addr *e);

char *
ether_ntoa(const struct ether_addr *n);

char *
ether_ntoa_r(const struct ether_addr *n, char *buf);

int
ether_ntohost(char *hostname, const struct ether_addr *e);

int
ether_hostton(const char *hostname, struct ether_addr *e);
```

## 描述

这些函数使用 `ether_addr` 结构操作以太网地址，该结构定义于头文件

`#include <net/ethernet.h>`

```c
/*
 * 以太网（MAC）地址的字节数。
 */
#define ETHER_ADDR_LEN		6
/*
 * 48 位以太网地址的结构。
 */
struct  ether_addr {
        u_char octet[ETHER_ADDR_LEN];
};
```

`ether_line` 函数扫描 `l`（一个 [ethers(5)](../man5/ethers.5.md) 格式的 ASCII 字符串），将 `e` 设置为字符串中指定的以太网地址，将 `h` 设置为主机名。此函数用于将 **/etc/ethers** 中的行解析为其组成部分。

`ether_aton` 和 `ether_aton_r` 函数将以太网地址的 ASCII 表示转换为 `ether_addr` 结构。相应地，`ether_ntoa` 和 `ether_ntoa_r` 函数将以 `ether_addr` 结构指定的以太网地址转换为 ASCII 字符串。

`ether_ntohost` 和 `ether_hostton` 函数按照 **/etc/ethers** 数据库中的指定，将以太网地址映射到对应的主机名。`ether_ntohost` 函数从以太网地址转换为主机名，`ether_hostton` 从主机名转换为以太网地址。

## 返回值

`ether_line` 函数成功时返回零，如果无法解析所提供行 `l` 的任何部分，则返回非零值。它在所提供的 `ether_addr` 结构 `e` 中返回提取的以太网地址，在所提供的字符串 `h` 中返回主机名。

成功时，`ether_ntoa` 和 `ether_ntoa_r` 函数返回指向包含以太网地址 ASCII 表示的字符串的指针。如果无法转换所提供的 `ether_addr` 结构，则返回 `NULL` 指针。`ether_ntoa` 将结果存储在静态缓冲区中；`ether_ntoa_r` 将结果存储在用户传递的缓冲区中。

类似地，`ether_aton` 和 `ether_aton_r` 成功时返回指向 `ether_addr` 结构的指针，失败时返回 `NULL` 指针。`ether_aton` 将结果存储在静态缓冲区中；`ether_aton_r` 将结果存储在用户传递的缓冲区中。

`ether_ntohost` 和 `ether_hostton` 函数成功时返回零，如果无法在 **/etc/ethers** 数据库中找到匹配项，则返回非零值。

## 注释

用户必须确保传递给 `ether_line`、`ether_ntohost` 和 `ether_hostton` 函数的主机名字符串足够大，以容纳返回的主机名。

## NIS 交互

如果 **/etc/ethers** 包含一行仅有单个 +，`ether_ntohost` 和 `ether_hostton` 函数除查询 **/etc/ethers** 文件中的数据外，还会尝试查询 NIS 的 `ethers.byname` 和 `ethers.byaddr` 映射。

## 参见

[ethers(5)](../man5/ethers.5.md), [yp(8)](../man8/yp.8.md)

## 历史

此 `ether_hostton` 库函数的特定实现为 FreeBSD 2.1 编写并首次出现。线程安全的函数变体首次出现于 FreeBSD 7.0。

## 缺陷

`ether_aton` 和 `ether_ntoa` 函数返回的值存储在静态内存区中，下次调用时可能被覆盖。

`ether_ntoa_r` 接受字符缓冲区指针，但不接受缓冲区长度。调用者必须确保缓冲区中有足够的空间，以避免缓冲区溢出。
