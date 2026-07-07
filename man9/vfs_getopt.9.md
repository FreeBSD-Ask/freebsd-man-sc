# vfs_getopt(9)

`vfs_getopt` — 操作挂载选项及其值

## 名称

`vfs_getopt`, `vfs_getopts`, `vfs_flagopt`, `vfs_scanopt`, `vfs_copyopt`, `vfs_filteropt`, `vfs_setopt`, `vfs_setopt_part`, `vfs_setopts`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`int vfs_getopt(struct vfsoptlist *opts, const char *name, void **buf, int *len)`

`char * vfs_getopts(struct vfsoptlist *opts, const char *name, int *error)`

`int vfs_flagopt(struct vfsoptlist *opts, const char *name, uint64_t *flags, uint64_t flag)`

`int vfs_scanopt(struct vfsoptlist *opts, const char *name, const char *fmt, ...)`

`int vfs_copyopt(struct vfsoptlist *opts, const char *name, void *dest, int len)`

`int vfs_filteropt(struct vfsoptlist *opts, const char **legal)`

`int vfs_setopt(struct vfsoptlist *opts, const char *name, void *value, int len)`

`int vfs_setopt_part(struct vfsoptlist *opts, const char *name, void *value, int len)`

`int vfs_setopts(struct vfsoptlist *opts, const char *name, const char *value)`

## 描述

`vfs_getopt()` 函数将 `buf` 设置为指向命名挂载选项的值，如果 `len` 不为 `NULL`，则将 `len` 设置为该值的长度。`buf` 参数将指向实际值，无需释放（可能也不应修改）。

`vfs_getopts()` 函数在指定选项为字符串（即以 `NUL` 结尾）时返回该选项的值。

`vfs_flagopt()` 函数确定选项是否存在。如果选项存在且 `flags` 不为 `NULL`，则将 `flag` 添加到 `flags` 中已设置的标志中。如果选项不存在且 `flags` 不为 `NULL`，则从 `flags` 中已设置的标志中移除 `flag`。典型用法示例：

```c
if (vfs_flagopt(mp->mnt_optnew, "wormlike", NULL, 0))
	vfs_flagopt(mp->mnt_optnew, "appendok", &(mp->flags), F_APPENDOK);
```

`vfs_scanopt()` 函数使用给定的格式对选项的值执行 vsscanf(3)，结果存入指定的可变参数。该值必须是字符串（即以 `NUL` 结尾）。

`vfs_copyopt()` 函数创建选项值的副本。`len` 参数必须与选项值的长度完全匹配（即较大的缓冲区仍会导致 `vfs_copyout()` 失败并返回 `EINVAL`）。

`vfs_filteropt()` 函数确保未指定任何未知选项。如果选项的名称与合法名称列表中的某个名称匹配，则该选项有效。选项可以带有 `no` 前缀，仍被视为有效。

`vfs_setopt()` 和 `vfs_setopt_part()` 函数将新数据复制到选项的值中。在 `vfs_setopt()` 中，`len` 参数必须与选项值的长度完全匹配（即较大的缓冲区仍会导致 `vfs_copyout()` 失败并返回 `EINVAL`）。

`vfs_setopts()` 函数将新字符串复制到选项的值中。该字符串（包括 `NUL` 字节）的长度不得超过选项的长度。

## 返回值

`vfs_getopt()` 函数找到选项时返回 0；否则返回 `ENOENT`。

`vfs_getopts()` 函数在找到指定选项且以 `NUL` 结尾时返回该选项。如果找到选项但未以 `NUL` 结尾，则将 `error` 设为 `EINVAL` 并返回 `NULL`。如果未找到选项，则将 `error` 设为 0 并返回 `NULL`。

`vfs_flagopt()` 函数找到选项时返回 1，未找到时返回 0。

`vfs_scanopt()` 函数在未找到选项或选项未以 `NUL` 结尾时返回 0；否则返回 vsscanf(3) 的返回值。如果 vsscanf(3) 返回 0，则原样返回；因此返回值 0 并不总是意味着选项不存在或不是有效的字符串。

`vfs_copyopt()` 和 `vfs_setopt()` 函数在复制成功时返回 0，找到选项但长度不匹配时返回 `EINVAL`，未找到选项时返回 `ENOENT`。

`vfs_filteropt()` 函数在所有选项都合法时返回 0；否则返回 `EINVAL`。

`vfs_setopts()` 函数在复制成功时返回 0，找到选项但字符串太长时返回 `EINVAL`，未找到选项时返回 `ENOENT`。

## 作者

本手册页由 Chad David <davidc@FreeBSD.org> 和 Ruslan Ermilov <ru@FreeBSD.org> 编写。
