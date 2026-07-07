# modfind(2)

`modfind` — 返回内核模块的 modid

## 名称

`modfind`

## 库

Lb libc

## 概要

`#include <sys/param.h>`
`#include <sys/module.h>`

```c
int
modfind(const char *modname);
```

## 描述

`modfind()` 系统调用返回 `modname` 所引用的内核模块的 modid。

## 返回值

`modfind()` 系统调用返回 `modname` 所引用的内核模块的 modid。出错时，`modfind()` 返回 -1，并设置 `errno` 以指示错误。

## 错误

如果 `modfind()` 失败，`errno` 设置为以下值：

**[`EFAULT`]** 此操作所需的数据无法从内核空间读取。

**[`ENOENT`]** 指定的文件未加载到内核中。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldload(2)](kldload.2.md), [kldnext(2)](kldnext.2.md), [kldstat(2)](kldstat.2.md), [kldsym(2)](kldsym.2.md), [kldunload(2)](kldunload.2.md), [modfnext(2)](modnext.2.md), [modnext(2)](modnext.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md), [kldstat(8)](../man8/kldstat.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。
