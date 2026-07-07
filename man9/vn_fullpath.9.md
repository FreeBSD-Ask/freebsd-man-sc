# vn_fullpath(9)

`vn_fullpath` — 在给定进程上下文的情况下，将 vnode 引用转换为完整路径名

## 名称

`vn_fullpath`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
vn_fullpath(struct vnode *vp, char **retbuf, char **freebuf)

int
vn_fullpath_jail(struct vnode *vp, char **retbuf, char **freebuf)

int
vn_fullpath_global(struct vnode *vp, char **retbuf, char **freebuf)

int
vn_fullpath_hardlink(struct vnode *vp, struct vnode *dvp,
    const char *hrdl_name, size_t hrdl_name_length,
    char **retbuf, char **freebuf, size_t *buflen)
```

## 描述

`vn_fullpath`、`vn_fullpath_jail`、`vn_fullpath_global` 和 `vn_fullpath_hardlink` 函数尽"最大努力"为传入的 vnode 生成字符串路径名。它们的区别在于返回路径相对于哪个目录，`vn_fullpath_hardlink` 除外——在此方面它的行为与 `vn_fullpath` 相同，将在最后描述。

`vn_fullpath` 函数返回相对于传入线程指针关联进程的根目录的路径。该根目录是系统的或线程进程所在 jail 的根目录，或通过 [chroot(2)](../man2/chroot.2.md) 调用建立的此类目录的某个子目录。`vn_fullpath_jail` 函数返回相对于传入线程进程当前 jail 根目录的路径，忽略该 jail 内可能进行的 [chroot(2)](../man2/chroot.2.md) 调用。`vn_fullpath_global` 函数返回从系统根目录开始的完整路径，忽略所有 jail 根目录和 [chroot(2)](../man2/chroot.2.md) 调用。

内核打算与传入用户线程通信的路径应仅通过 `vn_fullpath` 获取。通过 `vn_fullpath_jail` 或 `vn_fullpath_global` 获取的路径仅用于特定的内核检查或审计目的。

所有这些函数都通过检查 VFS 名称缓存实现，并尝试从进程根目录到对象重建路径。由于几个原因，此过程必然不可靠：路径中的中间条目可能不在缓存中；文件可能有多个名称（硬链接），并非所有文件系统都使用名称缓存（特别是大多数合成文件系统不使用）；单个名称可能用于多个文件（在文件系统覆盖其他文件系统的情况下）；文件可能没有名称（如果已删除但仍打开或被引用）。然而，对于用户来说，生成的字符串可能仍然比 vnode 指针值或设备号和索引节点号更有用。使用此函数结果的代码应预期（并正确处理）失败。

这些函数接受以下参数：

**`vp`** 要搜索的 vnode。调用者无需锁定。

**`retbuf`** 指向 `char *` 的指针，成功时可能被设置为指向包含结果路径名的新分配缓冲区。

**`freebuf`** 指向 `char *` 的指针，成功时可能被设置为指向一个缓冲区，当调用者使用完 `retbuf` 时应释放它。

典型的消费者会声明两个字符指针：`fullpath` 和 `freepath`；他们会将 `freepath` 设置为 `NULL`，将 `fullpath` 设置为在 `vn_fullpath` 调用失败时使用的名称。使用完 `fullpath` 的值后，调用者会检查 `freepath` 是否非 `NULL`，如果是，则以 `M_TEMP` 池类型调用 [free(9)](free.9.md)。

`vn_fullpath_hardlink` 函数是一个便捷包装器，它自动将通过 `hrdl_name` 和 `hrdl_name_length` 参数传递的硬链接名称附加到对 vnode 父目录调用 `vn_fullpath` 的结果中。它要求将先前使用 `WANTPARENT` 标志调用 [namei(9)](namei.9.md) 的结果传入 `vp` 和 `dvp` 参数。参数 `buflen` 必须指向包含所需缓冲区大小的有效存储，如果超过 `MAXPATHLEN` 则会缩减为 `MAXPATHLEN`。

## 返回值

如果 vnode 成功转换为路径名，返回 0；否则返回错误号。

## 参见

[free(9)](free.9.md)

## 作者

本手册页最初由 Robert Watson <rwatson@FreeBSD.org> 编写以描述 `vn_fullpath` 函数。其他相关函数的描述由 Olivier Certner <olce@FreeBSD.org> 添加。
