# ftw.3

`ftw` — 遍历（行走）文件树

## 名称

`ftw`, `nftw`

## 概要

`#include <ftw.h>`

```c
int
ftw(const char *path, int (*fn)(const char *, const struct stat *, int),
    int maxfds);

int
nftw(const char *path,
    int (*fn)(const char *, const struct stat *, int, struct FTW *),
    int maxfds, int flags);
```

## 描述

`ftw()` 和 `nftw()` 函数遍历（行走）以 `path` 为根的目录层次结构。对于层次结构中的每个对象，这些函数调用 `fn` 所指向的函数。`ftw()` 函数向该函数传递一个指向以 `NUL` 结尾的字符串的指针（该字符串包含对象名称）、一个指向与该对象对应的 `stat` 结构的指针，以及一个整数标志。`nftw()` 函数传递上述参数外加一个指向 `FTW` 结构的指针，该结构由

`#include <ftw.h>`

定义（如下所示）：

```c
struct FTW {
    int base;	/* 路径名中基名的偏移量 */
    int level;	/* 相对于起始点的目录深度 */
};
```

传递给 `fn` 的标志的可能值为：

**`FTW_F`** 普通文件。

**`FTW_D`** 正在按前序访问的目录。

**`FTW_DNR`** 无法读取的目录。不会进入该目录。

**`FTW_DP`** 正在按后序访问的目录（仅 `nftw()`）。

**`FTW_NS`** 无法获取 [stat(2)](../sys/stat.2.md) 信息的文件。`stat` 结构的内容未定义。

**`FTW_SL`** 符号链接。

**`FTW_SLN`** 指向不存在目标的符号链接（仅 `nftw()`）。

`ftw()` 函数按前序遍历树。也就是说，它在处理目录内容之前先处理目录本身。

`maxfds` 参数指定遍历树时保持打开的最大文件描述符数量。在本实现中无效。

`nftw()` 函数有一个额外的 `flags` 参数，其可能值如下：

**`FTW_PHYS`** 物理遍历，不跟随符号链接。

**`FTW_MOUNT`** 遍历不会跨越挂载点。

**`FTW_DEPTH`** 按后序处理目录。在目录本身之前先访问目录的内容。默认情况下，`nftw()` 按前序遍历树。

**`FTW_CHDIR`** 在读取目录之前更改到该目录。默认情况下，`nftw()` 会更改其起始目录。在 `nftw()` 返回之前，当前工作目录将恢复为其原始值。

## 返回值

如果树遍历成功，`ftw()` 和 `nftw()` 函数返回 0。如果 `fn` 所指向的函数返回非零值，`ftw()` 和 `nftw()` 将停止处理树并返回 `fn` 的返回值。如果检测到错误，两个函数都返回 -1。

## 实例

以下示例展示了 `nftw` 的用法。它从程序唯一参数所指向的目录开始遍历文件树，并显示完整路径和文件类型的简要指示。

```c
#include <ftw.h>
#include <stdio.h>
#include <sysexits.h>
int
nftw_callback(const char *path, const struct stat *sb, int typeflag, struct FTW *ftw)
{
	char type;
	switch(typeflag) {
	case FTW_F:
		type = 'F';
		break;
	case FTW_D:
		type = 'D';
		break;
	case FTW_DNR:
		type = '-';
		break;
	case FTW_DP:
		type = 'd';
		break;
	case FTW_NS:
		type = 'X';
		break;
	case FTW_SL:
		type = 'S';
		break;
	case FTW_SLN:
		type = 's';
		break;
	default:
		type = '?';
		break;
	}
	printf("[%c] %s\n", type, path);
	return (0);
}
int
main(int argc, char **argv)
{
	if (argc != 2) {
		printf("Usage %s <directory>\n", argv[0]);
		return (EX_USAGE);
	} else
		return (nftw(argv[1], nftw_callback, /* 未使用 */ 1, 0));
}
```

## 错误

`ftw()` 和 `nftw()` 函数可能失败并设置 `errno`，错误类型与库函数 [close(2)](../sys/close.2.md)、[open(2)](../sys/open.2.md)、[stat(2)](../sys/stat.2.md)、malloc(3)、opendir(3) 和 readdir(3) 所指定的相同。如果设置了 `FTW_CHDIR` 标志，`nftw()` 函数可能失败并设置 `errno`，错误类型与 [chdir(2)](../sys/chdir.2.md) 所指定的相同。此外，任一函数都可能失败并按如下方式设置 `errno`：

**[EINVAL]** `maxfds` 参数小于 1。

## 参见

[chdir(2)](../sys/chdir.2.md), [close(2)](../sys/close.2.md), [open(2)](../sys/open.2.md), [stat(2)](../sys/stat.2.md), [fts(3)](fts.3.md), malloc(3), opendir(3), readdir(3)

## 标准

`ftw()` 和 `nftw()` 函数符合 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

这些函数首次出现在 AT&T System V Release 3 UNIX 中。它们首次出现在 FreeBSD 5.3 中。

## 缺陷

`maxfds` 参数目前被忽略。
