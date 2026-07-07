# clock(3)

`clock` — 确定所使用的处理器时间

## 名称

`clock`

## 库

libc

## 概要

`#include <time.h>`

```c
clock_t
clock(void);
```

## 描述

`clock` 函数确定自调用进程启动以来所使用的处理器时间量，以 `CLOCKS_PER_SEC` 分之一秒为单位计量。

## 返回值

`clock` 函数返回所使用的时间量，除非发生错误，此时返回值为 -1。

## 参见

[getrusage(2)](../sys/getrusage.2.md), [clocks(7)](../man7/clocks.7.md)

## 标准

`clock` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。然而，-susv2 要求将 `CLOCKS_PER_SEC` 定义为一百万。FreeBSD 不符合此要求；更改该值会引入二进制不兼容性，而且一百万在现代处理器上仍然不够。
