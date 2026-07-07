# rtime(3)

`rtime` — 获取远程时间

## 名称

`rtime`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/time.h>`

`#include <netinet/in.h>`

```c
int
rtime(struct sockaddr_in *addrp, struct timeval *timep,
    struct timeval *timeout);
```

## 描述

`rtime` 函数向 `addrp` 所指向地址上的 Internet 时间服务器发出查询，并将远程时间返回到 `timep` 所指向的 `timeval` 结构中。通常，查询时间服务器时使用 UDP 协议。`timeout` 参数指定例程在等待回复时放弃前应等待的时长。但是，如果将 `timeout` 指定为 `NULL`，例程将改用 TCP 并阻塞，直到从时间服务器收到回复。

## 返回值

成功时返回 0；失败时返回 -1，并设置 `errno` 指示错误。
