# abort(3)

`abort` — 引发异常程序终止

## 名称

`abort`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void
abort(void);
```

## 描述

`abort` 函数引发异常程序终止，除非信号 `SIGABRT` 正被捕获且信号处理程序不返回。

所有打开的流都会被刷新并关闭。

## 实现说明

`abort` 函数是线程安全的。是否为异步取消安全则未知。

## 返回值

`abort` 函数永不返回。

## 参见

[abort2(2)](../sys/abort2.2.md), [sigaction(2)](../sys/sigaction.2.md), [exit(3)](exit.3.md)

## 标准

`abort` 函数遵循 IEEE Std 1003.1-1990 ("POSIX.1")。`abort` 函数还遵循 ISO/IEC 9899:1999 ("ISO C99")，并具有上述实现特定的细节。
