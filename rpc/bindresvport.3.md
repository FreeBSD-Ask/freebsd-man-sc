# bindresvport(3)

`bindresvport` — 将套接字绑定到特权 IP 端口

## 名称

`bindresvport`, `bindresvport_sa`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <rpc/rpc.h>`

```c
int
bindresvport(int sd, struct sockaddr_in *sin);

int
bindresvport_sa(int sd, struct sockaddr *sa);
```

## 描述

`bindresvport` 和 `bindresvport_sa` 函数用于将套接字描述符绑定到特权 IP 端口，即端口号在 0 到 1023 范围内的端口。

如果 `sin` 是指向 `struct sockaddr_in` 的指针，则应定义该结构中的相应字段。注意，`sin->sin_family` 必须初始化为由 `sd` 传递的套接字的地址族。如果 `sin->sin_port` 为 ‘0’，则会选择一个匿名端口（范围 600 到 1023），若 bind(2) 成功，`sin->sin_port` 将被更新为所分配的端口。

如果 `sin` 是 `NULL` 指针，则会分配一个匿名端口（如上所述）。但在这种情况下，`bindresvport` 无法返回所分配的端口。

只有 root 用户才能绑定到特权端口；对其他任何用户此调用都会失败。

`bindresvport` 的函数原型偏向于 `AF_INET` 套接字。`bindresvport_sa` 函数的行为完全相同，但具有更中性的函数原型。注意，这两个函数的行为完全相同，且都支持 `AF_INET6` 套接字和 `AF_INET` 套接字。

## 返回值

成功时返回 0，失败时返回 -1，并设置 `errno` 指示错误。

## 错误

**`[EPFNOSUPPORT]`** 如果提供了第二个参数，且参数之间的地址族不匹配。

`bindresvport` 函数也可能失败，并为 bind(2)、getsockopt(2) 或 setsockopt(2) 调用所指定的任何错误设置 `errno`。

## 参见

bind(2), getsockopt(2), setsockopt(2), [ip(4)](../man4/ip.4.md)
