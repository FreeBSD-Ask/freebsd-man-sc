# kldstat(2)

`kldstat` — 获取 kld 文件状态

## 名称

`kldstat`

## 库

Lb libc

## 概要

`#include <sys/linker.h>`

```c
int
kldstat(int fileid, struct kld_file_stat *stat);
```

## 描述

`kldstat()` 系统调用将 `fileid` 所引用文件的信息写入 `stat`。

```c
struct kld_file_stat {
	int         version;    /* 设置为 sizeof(struct kld_file_stat) */
	char        name[MAXPATHLEN];
	int         refs;
	int         id;
	caddr_t     address;
	size_t      size;
	char        pathname[MAXPATHLEN];
};
```

**version** 该字段由调用 `kldstat()` 的代码（而非 `kldstat()` 本身）设置为上述结构的大小。

**name** `fileid` 所引用文件的名称。

**refs** `fileid` 所引用文件的引用数。

**id** `fileid` 中指定的文件 ID。

**address** kld 文件的加载地址。

**size** 该文件分配的内存量（以字节为单位）。

**pathname** `fileid` 所引用文件的完整名称，包括路径。

## 返回值

`kldstat()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除非发生以下情况，否则 `fileid` 所引用文件的信息将被填入 `stat` 所指向的结构：

**[`ENOENT`]** 未找到该文件（可能未加载）。

**[`EINVAL`]** `stat` 的 `version` 字段中指定的版本不是正确的版本。如果你已正确填写了 `version` 字段，但出现此错误，则需要重新构建 world、内核或你的应用程序。

**[`EFAULT`]** 在 [copyout(9)](../man9/copyout.9.md) 函数中将字段复制到 `stat` 时出现问题。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldload(2)](kldload.2.md), [kldnext(2)](kldnext.2.md), [kldsym(2)](kldsym.2.md), [kldunload(2)](kldunload.2.md), [modfind(2)](modfind.2.md), [modfnext(2)](modfnext.2.md), [modnext(2)](modnext.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md), [kldstat(8)](../man8/kldstat.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。

## 缺陷

如果自模块加载后文件系统挂载情况已更改，或者此函数在 chroot 环境中被调用，则 pathname 可能不准确。
