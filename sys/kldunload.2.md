# kldunload(2)

`kldunload` — 卸载 kld 文件

## 名称

`kldunload`, `kldunloadf`

## 库

Lb libc

## 概要

```c
#include <sys/linker.h>

int
kldunload(int fileid);

int
kldunloadf(int fileid, int flags);
```

## 描述

`kldunload()` 系统调用从内核中卸载先前通过 [kldload(2)](kldload.2.md) 链接的 kld 文件。

`kldunloadf()` 系统调用接受一个额外的 flags 参数，可以是 `LINKER_UNLOAD_NORMAL`（行为与 `kldunload()` 相同）或 `LINKER_UNLOAD_FORCE`（导致卸载时忽略模块静默失败）。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除非发生以下情况，否则 `fileid` 所引用的文件将被卸载：

**[`EPERM`]** 你没有从内核中卸载该文件的权限。

**[`ENOENT`]** 未找到该文件。

**[`EBUSY`]** 你尝试卸载由内核链接的文件。

**[`EINVAL`]** `kldunloadf()` 系统调用传入了无效的 flags。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldload(2)](kldload.2.md), [kldnext(2)](kldnext.2.md), [kldstat(2)](kldstat.2.md), [kldsym(2)](kldsym.2.md), [modfind(2)](modfind.2.md), modfnext(2), [modnext(2)](modnext.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md), [kldunload(8)](../man8/kldunload.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。
