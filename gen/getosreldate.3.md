# getosreldate(3)

`getosreldate` — 获取 `__FreeBSD_version` 的值

## 名称

`getosreldate`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
getosreldate(void);
```

## 描述

`getosreldate` 函数返回一个整数，表示当前运行的 FreeBSD 内核的版本。各值的定义可在 *The Porter's Handbook* 中找到：

<https://www.FreeBSD.org/doc/en/books/porters-handbook/>

## 返回值

若成功完成，`getosreldate` 返回所请求的值；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 环境变量

**`OSVERSION`** 如果设置了环境变量 `OSVERSION`，它将覆盖 `getosreldate` 的返回值。

## 实例

示例可在 **/usr/share/examples/FreeBSD_version** 中找到。

## 错误

`getosreldate` 函数可能失败并为库函数 [sysctl(3)](sysctl.3.md) 指定的任何错误设置 `errno`。

## 参见

> *The Porter's Handbook*.

## 历史

`getosreldate` 函数出现于 FreeBSD 2.0。
