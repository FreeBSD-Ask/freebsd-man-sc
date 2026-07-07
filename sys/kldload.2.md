# kldload(2)

`kldload` — 将 KLD 文件加载到内核中

## 名称

`kldload`

## 库

Lb libc

## 概要

`#include <sys/linker.h>`

```c
int
kldload(const char *file);
```

## 描述

`kldload()` 系统调用使用内核链接器（参见 [kld(4)](../man4/kld.4.md)）将由 `file` 指定的 kld 文件加载到内核中。`file` 可以指定为完整路径或相对路径，否则将按加载器可调参数和 sysctl 变量 `kern.module_path` 定义的模块路径进行搜索。`file` 的 .ko 扩展名不是必需的。

## 返回值

`kldload()` 系统调用返回加载到内核中的 kld 文件的 fileid。如果发生错误，`kldload()` 将返回 -1 并设置 `errno` 以指示错误。

## 错误

除非发生以下情况，否则指定的文件将被加载：

**[`EPERM`]** 你没有读取该文件或将其与内核链接的权限。你必须以 root 用户身份才能使用 `kld` 系统调用。

**[`EFAULT`]** 向内核空间添加 kld 信息时遇到错误地址。

**[`ENOMEM`]** 没有足够的内存将文件加载到内核中。

**[`ENOENT`]** 未找到该文件。

**[`ENOEXEC`]** 无法识别 `file` 的文件格式。

**[`EEXIST`]** 所提供的 `file` 已经被加载。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldnext(2)](kldnext.2.md), [kldstat(2)](kldstat.2.md), [kldsym(2)](kldsym.2.md), [kldunload(2)](kldunload.2.md), [modfind(2)](modfind.2.md), [modfnext(2)](modfnext.2.md), [modnext(2)](modnext.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md), [kldload(8)](../man8/kldload.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。
