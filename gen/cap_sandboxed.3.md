# cap_sandboxed(3)

`cap_sandboxed` — 检查是否处于 capability 模式沙箱中

## 名称

`cap_sandboxed`

## 库

Lb libc

## 概要

`#include <sys/capsicum.h>`

`#include <stdbool.h>`

```c
bool
cap_sandboxed(void);
```

## 描述

`cap_sandboxed` 在进程处于 capability 模式沙箱中时返回 `true`，否则返回 `false`。此函数是 cap_getmode(2) 系统调用的更便捷替代方案，因为它总是会成功，因此无需进行错误检查。如果内核未编译入 capability 模式支持，`cap_sandboxed` 将始终返回 `false`。

## 返回值

`cap_sandboxed` 函数总是会成功，返回 `true` 或 `false`。

## 参见

[cap_enter(2)](../sys/cap_enter.2.md), [capsicum(4)](../man4/capsicum.4.md)

## 历史

`cap_sandboxed` 函数首次出现于 FreeBSD 9.2。

## 作者

此函数由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下实现，手册页也由其编写。
