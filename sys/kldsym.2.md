# kldsym(2)

`kldsym` — 在 KLD 中按符号名查找地址

## 名称

`kldsym`

## 库

Lb libc

## 概要

`#include <sys/linker.h>`

```c
int
kldsym(int fileid, int cmd, void *data);
```

## 描述

`kldsym()` 系统调用返回由 `fileid` 指定的模块中、由 `data` 指定的符号的地址。如果 `fileid` 为 0，则搜索所有已加载的模块。目前，唯一实现的 `cmd` 是 `KLDSYM_LOOKUP`。

`data` 参数采用以下结构：

```c
struct kld_sym_lookup {
    int         version;        /* sizeof(struct kld_sym_lookup) */
    char        *symname;       /* 要查找的符号名 */
    u_long      symvalue;
    size_t      symsize;
};
```

`version` 成员由调用 `kldsym()` 的代码设置为 `sizeof(struct kld_sym_lookup)`。接下来的两个成员 `version` 和 `symname` 由用户指定。最后两个成员 `symvalue` 和 `symsize` 由 `kldsym()` 填入，分别包含与 `symname` 关联的地址以及它所指向的数据的大小。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`kldsym()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `data->version` 或 `cmd` 中的值无效。

**[`ENOENT`]** `fileid` 参数无效，或找不到指定的符号。

## 参见

[kldfind(2)](kldfind.2.md), [kldfirstmod(2)](kldfirstmod.2.md), [kldload(2)](kldload.2.md), [kldnext(2)](kldnext.2.md), [kldunload(2)](kldunload.2.md), [modfind(2)](modfind.2.md), [modnext(2)](modnext.2.md), [modstat(2)](modstat.2.md), [kld(4)](../man4/kld.4.md)

## 历史

`kldsym()` 系统调用首次出现于 FreeBSD 3.0。