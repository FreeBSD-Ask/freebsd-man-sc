# modnext(2)

`modnext` — 返回下一个内核模块的 modid

## 名称

`modnext`

## 库

Lb libc

## 概要

`#include <sys/param.h>`
`#include <sys/module.h>`

```c
int
modnext(int modid);

int
modfnext(int modid);
```

## 描述

`modnext()` 系统调用返回下一个内核模块（即 `modid` 之后的那个）的 modid，如果 `modid` 是列表中的最后一个模块则返回 0。

如果 `modid` 值为 0，则 `modnext()` 返回第一个模块的 modid。`modfnext()` 系统调用必须始终传入有效的 modid。

## 返回值

`modnext()` 系统调用返回下一个模块的 modid（参见[描述](#描述)）或 0。如果发生错误，设置 `errno` 以指示错误。

## 错误

`modnext()` 设置的唯一错误是 `ENOENT`，当 `modid` 引用一个不存在（未加载）的内核模块时设置。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldload(2)](kldload.2.md), [kldnext(2)](kldnext.2.md), [kldstat(2)](kldstat.2.md), [kldsym(2)](kldsym.2.md), [kldunload(2)](kldunload.2.md), [modfind(2)](modfind.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md), [kldstat(8)](../man8/kldstat.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。
