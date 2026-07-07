# kldfirstmod(2)

`kldfirstmod` — 返回指定 kld 文件的第一个模块 ID

## 名称

`kldfirstmod`

## 库

Lb libc

## 概要

`#include <sys/linker.h>`

```c
int
kldfirstmod(int fileid);
```

## 描述

`kldfirstmod()` 系统调用返回与 `fileid` 引用的第一个模块相关的模块 ID。

## 返回值

`kldfirstmod()` 返回 `fileid` 引用的第一个模块的 ID，如果没有引用则返回 0。

## 错误

**[`ENOENT`]** `fileid` 引用的 kld 文件未找到。

## 参见

[kldfind(2)](kldfind.2.md), [kldload(2)](kldload.2.md), [kldnext(2)](kldnext.2.md), [kldstat(2)](kldstat.2.md), [kldsym(2)](kldsym.2.md), [kldunload(2)](kldunload.2.md), [modfind(2)](modfind.2.md), [modfnext(2)](modnext.2.md), [modnext(2)](modnext.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md), [kldstat(8)](../man8/kldstat.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。
