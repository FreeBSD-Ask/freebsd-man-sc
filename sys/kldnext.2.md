# kldnext(2)

`kldnext` — 返回下一个 kld 文件的 fileid

## 名称

`kldnext`

## 库

Lb libc

## 概要

`#include <sys/linker.h>`

```c
int
kldnext(int fileid);
```

## 描述

`kldnext()` 系统调用返回下一个 kld 文件（即 `fileid` 之后的那个）的 fileid，如果 `fileid` 是最后加载的文件则返回 0。要获取第一个 kld 文件的 fileid，向 `kldnext()` 传入 `fileid` 值 0。

## 返回值

`kldnext()` 系统调用成功时返回下一个 kld 文件的 fileid 或 0。否则，`kldnext()` 返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`kldnext()` 设置的唯一错误是 `ENOENT`，当 `fileid` 引用一个不存在（未加载）的 kld 文件时设置。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldload(2)](kldload.2.md), [kldstat(2)](kldstat.2.md), [kldsym(2)](kldsym.2.md), [kldunload(2)](kldunload.2.md), [modfind(2)](modfind.2.md), [modfnext(2)](modnext.2.md), [modnext(2)](modnext.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md), [kldstat(8)](../man8/kldstat.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。
