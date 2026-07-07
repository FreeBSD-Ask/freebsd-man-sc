# timer_delete(2)

`timer_delete` — 删除每进程定时器（REALTIME）

## 名称

`timer_delete`

## 库

Lb librt

## 概要

`#include <time.h>`

```c
int
timer_delete(timer_t timerid);
```

## 描述

`timer_delete()` 系统调用删除先前由 [timer_create(2)](timer_create.2.md) 系统调用创建的指定定时器 `timerid`。如果在调用 `timer_delete()` 时定时器已武装，其行为等同于在移除前自动解除武装。已删除定时器的待处理信号会被清除。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`timer_delete()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `timerid` 指定的定时器 ID 不是有效的定时器 ID。

## 参见

[timer_create(2)](timer_create.2.md)

## 标准

`timer_delete()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 每进程定时器的支持首次出现于 FreeBSD 7.0。
