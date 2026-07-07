# modstat(2)

`modstat` — 获取内核模块状态

## 名称

`modstat`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/module.h>`

```c
int
modstat(int modid, struct module_stat *stat);
```

## 描述

`modstat()` 系统调用将 `modid` 所引用内核模块的信息写入 `stat`。

```c
struct module_stat {
	int         version;        /* 设置为 sizeof(module_stat) */
	char        name[MAXMODNAME];
	int         refs;
	int         id;
	modspecific_t data;
};
typedef union modspecific {
	int         intval;
	u_int       uintval;
	long        longval;
	u_long      ulongval;
} modspecific_t;
```

**version** 该字段由调用 `modstat()` 的代码（而非 `modstat()` 本身）设置为上述结构的大小。

**name** `modid` 所引用模块的名称。

**refs** `modid` 所引用模块的引用数。

**id** `modid` 中指定的模块 ID。

**data** 模块特定数据。

## 返回值

`modstat()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除非发生以下情况，否则 `modid` 所引用模块的信息将被填入 `stat` 所指向的结构：

**[`ENOENT`]** 未找到该模块（可能未加载）。

**[`EINVAL`]** `stat` 的 `version` 字段中指定的版本不是正确的版本。如果你已正确填写了 `version` 字段，但出现此错误，则需要重新构建 world、内核或你的应用程序。

**[`EFAULT`]** 在 [copyout(9)](../man9/copy.9.md) 函数中将字段复制到 `stat` 时出现问题。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldload(2)](kldload.2.md), [kldnext(2)](kldnext.2.md), [kldstat(2)](kldstat.2.md), [kldsym(2)](kldsym.2.md), [kldunload(2)](kldunload.2.md), [modfind(2)](modfind.2.md), [modfnext(2)](modnext.2.md), [modnext(2)](modnext.2.md), [kld(4)](../man4/kld.4.md), [kldstat(8)](../man8/kldstat.8.md)

## 历史

`kld` 接口首次出现于 FreeBSD 3.0。
