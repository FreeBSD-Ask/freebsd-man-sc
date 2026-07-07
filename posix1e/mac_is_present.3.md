# mac_is_present(3)

`mac_is_present` — 报告运行中的系统是否支持 MAC

## 名称

`mac_is_present`

## 库

libc

## 概要

`#include <sys/mac.h>`

```c
int
mac_is_present(const char *policyname);
```

## 描述

`mac_is_present` 函数确定当前运行的内核是否针对给定策略支持 MAC。若 `policyname` 非 `NULL`，则检查指定策略（如 "`biba`"、"`mls`"、"`te`"）是否存在；否则检查是否存在任何 MAC 策略。

## 返回值

若系统支持给定的 MAC 策略，返回值 1。若不支持指定的 MAC 策略，返回值 0。若发生错误，返回值 -1。

## 错误

`[EINVAL]` `policyname` 的值无效。

`[ENOMEM]` 内存不足，无法分配内部存储。

## 参见

[mac(3)](mac.3.md), [mac_free(3)](mac_free.3.md), [mac_get(3)](mac_get.3.md), [mac_prepare(3)](mac_prepare.3.md), [mac_set(3)](mac_set.3.md), [mac_text(3)](mac_text.3.md), [mac(4)](../man4/mac.4.md), [mac(9)](../man9/mac.9.md)

## 历史

对强制访问控制（Mandatory Access Control）的支持作为 TrustedBSD 项目的一部分引入于 FreeBSD 5.0。
