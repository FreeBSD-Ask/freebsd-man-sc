# timespec_getres(3)

`timespec_getres` — 获取时钟分辨率

## 名称

`timespec_getres`

## 库

Lb libc

## 概要

```c
#include <time.h>

int
timespec_getres(struct timespec *ts, int base);
```

## 描述

如果 `ts` 非空且 `base` 引用一个受支持的时间基准（参见 [timespec_get(3)](timespec_get.3.md)），`timespec_getres` 函数将填充 `ts` 所指向的结构，以反映该时间基准的分辨率。

## 返回值

`timespec_getres` 函数成功时返回 `base` 的值，否则返回零。

## 参见

clock_getres(2), [timespec_get(3)](timespec_get.3.md)

## 标准

`timespec_getres` 函数遵循 ISO/IEC 9899:2023 ("ISO C23")。

## 历史

此接口首次出现于 FreeBSD 14。

## 作者

`timespec_getres` 函数及本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
