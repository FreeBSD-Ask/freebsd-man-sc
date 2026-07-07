# getrlimitusage(2)

`getrlimitusage` — 查询当前进程受限资源的使用量

## 名称

`getrlimitusage`

## 库

Lb libc

## 概要

```c
#include <sys/resource.h>

int
getrlimitusage(unsigned which, int flags, rlim_t *res);
```

## 描述

`getrlimitusage()` 系统调用允许进程查询由 [setrlimit(2)](setrlimit.2.md) 调用限制的资源的当前消耗量。

`which` 参数指定资源，与 [getrlimit(2)](getrlimit.2.md) 和 [setrlimit(2)](setrlimit.2.md) 调用相同，强制执行的资源类型列表参见它们的手册页。

`flags` 参数通过以下方式修改调用行为：

**`GETRLIMITUSAGE_EUID`** 查询由进程有效 UID 标识的用户的资源使用量，而非真实 UID（后者为记账的默认值）。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getrlimitusage()` 系统调用在以下情况下将失败：

**[EFAULT]** 为 `res` 指定的地址无效。

**[EINVAL]** `getrlimitusage()` 的 `which` 参数指定的资源未知。

**[ENXIO]** `getrlimitusage()` 的 `which` 参数指定的资源不被记账，仅在特定情况下强制执行。此类资源的示例有 `RLIMIT_FSIZE` 和 `RLIMIT_CORE`。

## 参见

[procstat(1)](../man1/procstat.1.md), [getrlimit(2)](getrlimit.2.md), [setrlimit(2)](setrlimit.2.md)

## 历史

`getrlimitusage()` 系统调用首次出现于 FreeBSD 14.2。