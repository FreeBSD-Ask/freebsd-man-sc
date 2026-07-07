# scandir(3)

`scandir` — 扫描目录

## 名称

`scandir`, `fdscandir`, `scandirat`, `scandir_b`, `fdscandir_b`, `fdscandirat_b`, `alphasort`, `versionsort`

## 库

Lb libc

## 概要

`#include <dirent.h>`

```c
int
scandir(const char *dirname, struct dirent ***namelist,
    int (*select)(const struct dirent *),
    int (*compar)(const struct dirent **, const struct dirent **));

int
fdscandir(int dirfd, struct dirent ***namelist,
    int (*select)(const struct dirent *),
    int (*compar)(const struct dirent **, const struct dirent **));

int
scandirat(int dirfd, const char *dirname, struct dirent ***namelist,
    int (*select)(const struct dirent *),
    int (*compar)(const struct dirent **, const struct dirent **));

int
scandir_b(const char *dirname, struct dirent ***namelist,
    int (^select)(const struct dirent *),
    int (^compar)(const struct dirent **, const struct dirent **));

int
fdscandir_b(int dirfd, struct dirent ***namelist,
    int (^select)(const struct dirent *),
    int (^compar)(const struct dirent **, const struct dirent **));

int
scandirat_b(int dirfd, const char *dirname, struct dirent ***namelist,
    int (^select)(const struct dirent *),
    int (^compar)(const struct dirent **, const struct dirent **));

int
alphasort(const struct dirent **d1, const struct dirent **d2);

int
versionsort(const struct dirent **d1, const struct dirent **d2);
```

## 描述

`scandir` 函数读取目录 `dirname` 并使用 malloc(3) 构建一个指向目录项的指针数组。它返回数组中的条目数。指向目录项数组的指针存储在 `namelist` 所引用的位置（即使没有选中任何条目）。

`select` 参数是指向用户提供的子例程的指针，`scandir` 调用该子例程来选择要包含在数组中的条目。select 例程接收一个指向目录项的指针，如果该目录项要包含在数组中，则应返回非零值。如果 `select` 为 null，则将包含所有目录项。

`compar` 参数是指向用户提供的子例程的指针，该子例程传递给 [qsort(3)](../stdlib/qsort.3.md) 用于对完成的数组进行排序。如果此指针为 null，则不对数组排序。

`alphasort` 函数是一个例程，可用于 `compar` 参数，使用 [strcoll(3)](../string/strcoll.3.md) 按字母顺序对数组排序。

`versionsort` 函数是一个例程，可用于 `compar` 参数，使用 [strverscmp(3)](../string/strverscmp.3.md) 对数组进行自然排序。

为数组分配的内存可以使用 free(3) 释放，方法是先释放数组中的每个指针，然后释放数组本身。

`fdscandir` 函数类似于 `scandir`，但接受引用目录的文件描述符而非路径。无论结果如何，文件描述符在返回时都保持打开状态。

`scandirat` 函数类似于 `scandir`，但接受一个额外的 `dirfd` 参数。如果提供的 `dirname` 是绝对路径，则该函数的行为与 `scandir` 相同，`dirfd` 参数不被使用。如果 `dirname` 是相对路径，`dirfd` 必须是引用目录的有效文件描述符，此时 `dirname` 查找相对于 `dirfd` 引用的目录执行。如果 `dirfd` 具有特殊值 `AT_FDCWD`，则当前进程目录用作相对查找的基准。有关更多详细信息，参见 openat(2)。

`scandir_b`、`fdscandir_b` 和 `scandirat_b` 函数的行为分别与 `scandir`、`fdscandir` 和 `scandirat` 相同，但接受块而非函数指针作为参数，并调用 `qsort_b` 而非 `qsort`。

## 诊断

`scandir`、`fdscandir`、`scandirat`、`scandir_b`、`fdscandir_b` 和 `scandirat_b` 函数返回成功时找到的目录条目数。如果无法打开目录进行读取、读取目录时发生错误，或 malloc(3) 无法分配足够的内存来容纳所有目录条目，则返回 -1 并将 `errno` 设置为适当的值。

## 错误

`scandir`、`scandirat`、`scandir_b` 和 `scandirat_b` 函数可能失败并为 opendir(3)、malloc(3)、readdir(3) 和 closedir(3) 函数指定的任何错误设置 `errno`。

`fdscandir` 和 `fdscandir_b` 函数可能失败并为 fdopendir(3)、malloc(3)、readdir(3) 和 closedir(3) 函数指定的任何错误设置 `errno`。

## 参见

openat(2), [directory(3)](directory.3.md), malloc(3), [qsort(3)](../stdlib/qsort.3.md), [strcoll(3)](../string/strcoll.3.md), [strverscmp(3)](../string/strverscmp.3.md), [dir(5)](../man5/dir.5.md)

## 标准

`alphasort` 和 `scandir` 函数预计遵循 IEEE Std 1003.1-2008 ("POSIX.1") 标准。`scandirat` 和 `versionsort` 函数是 GNU 扩展，不遵循任何标准。`fdscandir`、`scandir_b`、`fdscandir_b` 和 `scandirat_b` 函数是 FreeBSD 扩展。

## 历史

`scandir` 和 `alphasort` 函数出现于 4.2BSD。`scandir_b` 函数添加于 FreeBSD 11.0。`scandirat` 和 `versionsort` 函数添加于 FreeBSD 13.2。`fdscandir`、`fdscandir_b` 和 `scandirat_b` 函数添加于 FreeBSD 15.0。
