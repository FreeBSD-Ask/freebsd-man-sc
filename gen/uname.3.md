# uname(3)

`uname` — 获取系统标识信息

## 名称

`uname`

## 库

Lb libc

## 概要

`#include <sys/utsname.h>`

```c
int
uname(struct utsname *name);
```

## 描述

`uname` 函数将标识当前系统的信息以 null 结尾的字符串形式存储到 `name` 所引用的结构中。

`utsname` 结构定义在头文件 `<sys/utsname.h>` 中，包含以下成员：

**sysname** 操作系统实现的名称。

**nodename** 此机器的网络名称。

**release** 操作系统的发行级别。

**version** 操作系统的版本级别。

**machine** 机器硬件平台。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 环境变量

**`UNAME_s`** 如果设置了环境变量 `UNAME_s`，它将覆盖 `sysname` 成员。

**`UNAME_r`** 如果设置了环境变量 `UNAME_r`，它将覆盖 `release` 成员。

**`UNAME_v`** 如果设置了环境变量 `UNAME_v`，它将覆盖 `version` 成员。

**`UNAME_m`** 如果设置了环境变量 `UNAME_m`，它将覆盖 `machine` 成员。

## 错误

`uname` 函数可能失败并为库函数 [sysctl(3)](sysctl.3.md) 指定的任何错误设置 `errno`。

## 参见

[uname(1)](../man1/uname.1.md), [sysctl(3)](sysctl.3.md)

## 标准

`uname` 函数遵循 IEEE Std 1003.1-1988 ("POSIX.1") 标准。

## 历史

`uname` 函数首次出现于 4.4BSD。
