# nlist(3)

`nlist` — 从可执行文件中检索符号表名称列表

## 名称

`nlist`

## 库

Lb libc

## 概要

`#include <nlist.h>`

```c
int
nlist(const char *filename, struct nlist *nl);
```

## 描述

`nlist` 函数从 ELF 对象（例如可执行文件或共享库）中类型为 `SHT_DYNSYM` 或 `SHT_SYMTAB` 的 [elf(5)](../man5/elf.5.md) 节中检索名称列表条目。提供此函数是为了与遗留应用程序兼容。不鼓励使用它。

参数 `nl` 被设置为引用列表的开头。列表会清除二进制和无效数据；如果名称列表中的条目有效，则将该条目的 `n_type` 和 `n_value` 复制到 `nl` 所引用的列表中。不复制其他数据。列表中的最后一个条目始终为 `NULL`。

## 返回值

若成功则返回无效条目的数量；否则，如果文件 `filename` 不存在或不可执行，返回值为 -1。

## 参见

[elf(5)](../man5/elf.5.md), [stab(5)](../man5/stab.5.md)

## 历史

`nlist` 函数出现于 Version 6 AT&T UNIX。
