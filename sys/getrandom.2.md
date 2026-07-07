# getrandom(2)

`getrandom` — 获取随机数据

## 名称

`getrandom`

## 库

Lb libc

## 概要

`#include <sys/random.h>`

```c
ssize_t
getrandom(void *buf, size_t buflen, unsigned int flags);
```

## 描述

`getrandom()` 用最多 `buflen` 字节的随机数据填充 `buf`。

`flags` 参数可以包含零个或多个以下标志：

**`GRND_NONBLOCK`** 如果 [random(4)](../man4/random.4.md) 设备尚未完成种子初始化，则返回 `EAGAIN` 而不是阻塞。默认情况下，`getrandom()` 将阻塞直到设备完成种子初始化。

**`GRND_RANDOM`** 此标志在 FreeBSD 上无效。**`/dev/random`** 和 **`/dev/urandom`** 是相同的。

**`GRND_INSECURE`** 此标志被视为 `GRND_NONBLOCK` 的别名。提供它仅是为了与 Linux 的 API 兼容。

如果 [random(4)](../man4/random.4.md) 设备已完成种子初始化，最多 256 字节的读取将始终返回所请求的字节数，且不会被信号中断。

## 返回值

成功完成时，返回实际读取的字节数。对于大于 256 字节的请求，返回的字节数可能少于请求的字节数。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getrandom()` 操作返回以下错误：

**[`EAGAIN`]** 设置了 `GRND_NONBLOCK`（或 `GRND_INSECURE`）标志，且 [random(4)](../man4/random.4.md) 设备尚未完成种子初始化。

**[`EFAULT`]** `buf` 参数指向无效地址。

**[`EINTR`]** 睡眠被信号中断。

**[`EINVAL`]** 指定了无效的 `flags`。

**[`EINVAL`]** 请求的 `buflen` 大于 `IOSIZE_MAX`。

## 参见

[arc4random(3)](../man3/arc4random.3.md), [getentropy(3)](../man3/getentropy.3.md), [random(4)](../man4/random.4.md)

## 标准

`getrandom()` 是非标准的。它存在于 Linux 中。

## 历史

`getrandom()` 系统调用首次出现于 FreeBSD 12.0。

## 注意事项

与 Linux 不同，FreeBSD 上的 `GRND_INSECURE` 标志在 [random(4)](../man4/random.4.md) 设备完成种子初始化之前不会产生任何输出。
