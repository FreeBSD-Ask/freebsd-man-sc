# getentropy(3)

`getentropy` — 获取熵

## 名称

`getentropy`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
getentropy(void *buf, size_t buflen);
```

## 描述

`getentropy` 用高质量的随机数据填充缓冲区。

允许的最大 `buflen` 为 256 字节。

如果不产生错误，`getentropy` 始终提供所请求数量的随机数据字节。

与刚启动后从 **/dev/urandom** 读取类似，`getentropy` 可能会阻塞，直到系统收集到足够的熵来播种 CSPRNG。

## 实现说明

`getentropy` 函数使用 [getrandom(2)](../sys/getrandom.2.md) 实现。

## 返回值

若成功，`getentropy` 函数返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getentropy` 除非出现以下情况，否则将成功：

**[`EFAULT`]** `buf` 参数指向无效地址。

**[`EINVAL`]** 请求的字节数过多。

## 参见

[getrandom(2)](../sys/getrandom.2.md), [arc4random(3)](arc4random.3.md), [random(4)](../man4/random.4.md)

## 标准

`getentropy` 遵循 IEEE Std 1003.1-2024 ("POSIX.1")。

## 历史

`getentropy` 函数出现于 OpenBSD 5.6。FreeBSD libc 兼容垫片首次出现于 FreeBSD 12.0。
