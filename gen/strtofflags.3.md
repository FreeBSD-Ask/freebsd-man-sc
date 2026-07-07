# strtofflags(3)

`fflagstostr`, `strtofflags` — 在文件标志位与其字符串名称之间转换

## 名称

`fflagstostr`, `strtofflags`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
char *
fflagstostr(u_long flags);

int
strtofflags(char **stringp, u_long *setp, u_long *clrp);
```

## 描述

`fflagstostr` 函数返回一个由逗号分隔的字符串，表示由 `flags` 所代表的文件标志。如果未设置任何标志，则返回长度为零的字符串。

如果无法为返回值分配内存，`fflagstostr` 返回 `NULL`。

`fflagstostr` 返回的值通过 `malloc` 获得，程序使用完毕后应使用 `free` 将其归还给系统。

`strtofflags` 函数接收一个文件标志字符串（如 chflags(1) 所述），对其进行解析，并返回"设置"标志和"清除"标志，这些标志可作为参数传递给 [chflags(2)](../sys/chflags.2.md)。成功时 `strtofflags` 返回 0，否则返回非零值，且 `stringp` 将指向出错的 token。

## 错误

`fflagstostr` 函数可能失败并设置 errno，错误类型与库函数 malloc(3) 中指定的相同。

## 参见

chflags(1), [chflags(2)](../sys/chflags.2.md), malloc(3)

## 历史

`fflagstostr` 和 `strtofflags` 函数首次出现于 FreeBSD 4.0。
