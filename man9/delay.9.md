# DELAY(9)

`DELAY` — 忙等待一段时间间隔

## 名称

`DELAY`

## 概要

```c
#include <sys/types.h>
#include <sys/systm.h>
```

```c
void
DELAY(int delay)
```

## 描述

延迟 `delay` 微秒（1/1000000 秒）。

## 参见

pause(9)

## 作者

本手册页由 Alfred Perlstein 编写。
