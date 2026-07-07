# raise(3)

`raise` — 向当前线程发送信号

## 名称

`raise` — 向当前线程发送信号

## 库

Lb libc

## 概要

```c
#include <signal.h>

int
raise(int sig);
```

## 描述

`raise` 函数向当前线程发送信号 `sig`。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`raise` 函数可能失败并为库函数 [getpid(2)](../sys/getpid.2.md) 和 [kill(2)](../sys/kill.2.md) 指定的任何错误设置 `errno`。

## 参见

[kill(2)](../sys/kill.2.md)

## 标准

`raise` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。
