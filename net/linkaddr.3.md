# linkaddr(3)

`link_addr` — 链路层访问的地址规范例程

## 名称

`link_addr`, `link_ntoa`, `link_ntoa_r`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <net/if_dl.h>`

```c
int
link_addr(const char *addr, struct sockaddr_dl *sdl);

char *
link_ntoa(const struct sockaddr_dl *sdl);

int
link_ntoa_r(const struct sockaddr_dl *sdl, char *obuf, size_t *buflen);
```

## 描述

`link_addr` 例程解析表示链路层地址的字符串 `addr`，并将结果地址存储到 `sdl` 所指向的结构中。链路层地址由可选的接口名、一个冒号（所有情况下都必须有）和地址组成；地址可以是十六进制数字串，也可以是由字符 '.'、':' 或 '-' 分隔的十六进制八位组序列。

`link_ntoa` 例程接受一个链路层地址，返回表示其中部分信息的 ASCII 字符串，包括链路层地址本身以及接口名或编号（如果存在）。返回的字符串存储在静态缓冲区中。此功能为实验性，仍可能变更。

`link_ntoa_r` 例程的行为类似于 `link_ntoa`，但字符串被放入提供的缓冲区而非静态缓冲区。调用者应将 `buflen` 初始化为 `obuf` 中可用的字节数。返回时，`buflen` 被设置为输出缓冲区所需的实际字节数（包括 NUL 终止符）。如果 `obuf` 为 NULL，则按上述方式设置 `buflen`，但不写入任何内容。这可用于在第二次调用 `link_ntoa_r` 之前确定缓冲区所需的长度。

对于 `link_addr`，字符串 `addr` 可包含形式为 "name unit-number" 的可选网络接口标识符，适合作为 [ifconfig(8)](../man8/ifconfig.8.md) 的第一个参数，其后总是跟一个冒号和一个由以句点分隔的十六进制数字组构成的接口地址。每组表示地址的一个字节；地址字节从低位字节到高位字节从左到右填充。

因此 `le0:8.0.9.13.d.30` 表示要在第一个 Lance 以太网接口上传输的以太网地址。

## 返回值

`link_ntoa` 函数始终返回以 null 终止的字符串。

`link_ntoa_r` 函数成功时返回 0；如果提供的缓冲区不够大，则返回 -1。在后一种情况下，缓冲区的内容不确定，但如果缓冲区至少有一个字节大小，则始终会写入结尾的 NUL。

`link_addr` 函数成功时返回 0。如果地址看起来不是有效的链路层地址，则返回 -1，并设置 `errno` 以指示错误。

## 参见

[getnameinfo(3)](getnameinfo.3.md)

## 历史

`link_addr` 和 `link_ntoa` 函数出现于 4.3BSD。`link_ntoa_r` 函数出现于 FreeBSD 15.0。

## 缺陷

`link_ntoa` 的返回值存储在静态内存区中。

如果链路套接字地址 `sdl` 的 `sdl_len` 字段为 0，`link_ntoa` 不会在接口地址字节前插入冒号。如果将此转换后的地址在未插入初始冒号的情况下传递给 `link_addr`，后者将无法正确解析。
