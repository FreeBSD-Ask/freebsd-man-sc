# resettodr.9

`resettodr` — 根据系统时间设置电池后备时钟

## 名称

`resettodr`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/systm.h>
```

```c
void
resettodr(void)
```

## 描述

`resettodr` 函数根据系统 `time` 变量的内容设置系统的电池后备时钟。

## 参见

[inittodr(9)](inittodr.9.md), [time(9)](time.9.md)

## 缺陷

在许多系统上，`resettodr` 必须将 `time` 转换为以年、月、日、小时、分钟和秒表示的时间。许多实现可以共享代码，但实际上并没有。
