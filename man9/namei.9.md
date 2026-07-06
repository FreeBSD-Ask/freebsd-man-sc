# namei.9.md

`namei` — 路径名转换与查找操作

## 名称

`namei`, `NDINIT`, `NDINIT_AT`, `NDFREE_PNBUF`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/fcntl.h>
```

```c
#include <sys/namei.h>
```

```c
int
namei(struct nameidata *ndp)

void
NDINIT(struct nameidata *ndp, enum nameiop op, u_int64_t flags,
    enum uio_seg segflg, const char *namep)

void
NDINIT_AT(struct nameidata *ndp, enum nameiop op, u_int64_t flags,
    enum uio_seg segflg, const char *namep, int dirfd)

void
NDFREE_PNBUF(struct nameidata *ndp)
```

## 描述

`NDFREE_PNBUF` 设施允许客户端执行路径名转换和查找操作。`NDFREE_PNBUF` 函数会递增相关 vnode 的引用计数。在使用完 vnode 后，必须使用 [vrele(9)](vrele.9.md) 或 vput(9) 递减引用计数，具体取决于是否指定了 `LOCKLEAF` 标志。

`NDINIT` 宏用于初始化 `NDFREE_PNBUF` 组件。它接受以下参数：

**`ndp`** 指向要初始化的 `struct nameidata` 的指针。

**`op`** `namei` 将执行的操作。以下操作有效：`LOOKUP`、`CREATE`、`DELETE` 和 `RENAME`。后三个只是为这些效果做设置；仅调用 `namei` 不会导致 `VOP_RENAME` 被调用。

**`flags`** 操作标志，在下一节中描述。这些标志中的多个可以同时生效。

**`segflg`** UIO 段指示器。指示对象名称是在用户空间（`UIO_USERSPACE`）还是在内核地址空间（`UIO_SYSSPACE`）。

**`namep`** 指向组件路径名缓冲区的指针（将被查找的文件或目录名）。

`NDINIT_AT` 宏类似于 `NDINIT`，但接受一个额外参数：

**`dirfd`** 引用目录的文件描述符，或特殊值 `AT_FDCWD`（表示调用线程的当前工作目录）。查找将相对于此目录执行。

`NDFREE_PNBUF` 宏用于释放路径名缓冲区。对于每次成功的 `namei` 调用，必须恰好调用一次。它接受以下参数：

**`ndp`** 指向在成功的 `namei` 调用中使用的 `struct nameidata` 的指针。

## NAMEI 操作标志

`namei` 函数接受以下一组影响其操作的"操作标志"：

**`NC_NOMAKEENTRY`** `NOCACHE` 的别名。

**`NC_KEEPPOSENTRY`** 在缓存中保留正向缓存条目。此标志通常与 `NOCACHE` 组合使用，以不缓存新条目但保留现有条目，或与 `MAKEENTRY` 组合使用。

**`NOCACHE`** 避免 `namei` 在名称缓存中创建此条目（如果尚未存在）。通常，`namei` 会将不在缓存中的条目添加到名称缓存中。

**`LOCKLEAF`** 返回时以 `LK_EXCLUSIVE` 锁定 vnode，除非同时设置了 `LOCKSHARED`。应使用 VOP_UNLOCK(9) 释放锁（或使用 vput(9)，它等同于调用 VOP_UNLOCK(9) 后跟 [vrele(9)](vrele.9.md)，合为一体）。

**`LOCKPARENT`** 此标志让 `namei` 函数返回处于锁定状态的父（目录）vnode `ni_dvp`，除非它与 `ni_vp` 相同，在这种情况下 `ni_dvp` 本身不被锁定（但可能因 `LOCKLEAF` 而被锁定）。如果实施了锁定，应使用 vput(9) 或 VOP_UNLOCK(9) 和 [vrele(9)](vrele.9.md) 释放。

**`WANTPARENT`** 此标志允许 `namei` 函数以未锁定状态返回父（目录）vnode。父 vnode 必须使用 [vrele(9)](vrele.9.md) 单独释放。

**`FAILIFEXISTS`** 如果目标存在，使 `NDFREE_PNBUF` 操作失败。它要求设置 `LOCKPARENT` 标志且不设置 `LOCKLEAF`。

**`FOLLOW`** 使用此标志，如果所提供路径的最后一部分是符号链接，`namei` 将跟随该符号链接（即它将返回链接所指向内容的 vnode，而不是链接本身的 vnode）。

**`EMPTYPATH`** 对于用 `NDINIT_AT` 初始化的 `NDFREE_PNBUF` 调用，允许 `namep` 路径为空。在这种情况下，`dirfd` 文件描述符可以引用任意类型的文件，不一定是目录，查找返回此文件的 vnode。

**`LOCKSHARED`** 返回时以 `LK_SHARED` 锁定 vnode（如果拥有该 vnode 的文件系统允许）。文件系统必须在挂载期间通过在 `mp->mnt_kern_flag` 中设置 `MNTK_LOOKUP_SHARED` 以及在分配 vnode 时调用 `VN_LOCK_ASHARE` 来显式允许此操作。如果指定了 `LOCKLEAF` 但不允许共享锁定，则 vnode 将以 `LK_EXCLUSIVE` 返回。应使用 VOP_UNLOCK(9) 释放锁（或使用 vput(9)，它等同于调用 VOP_UNLOCK(9) 后跟 [vrele(9)](vrele.9.md)，合为一体）。

**`NOFOLLOW`** 不跟随符号链接（伪标志）。实际代码不会查找此标志，而是查找 `FOLLOW`。`NOFOLLOW` 用于向源代码读者表明有意不跟随符号链接。

**`RBENEATH`** 要求 `NDFREE_PNBUF` 未跨越 `dirfd` 目录。此标志用于实现 openat(2) 的 `O_RESOLVE_BENEATH` 标志。

**`NAMEILOOKUP`** 组件嵌入在 `NDFREE_PNBUF` 查找结构中，可使用 `vfs_lookup_nameidata` 函数获取该结构。这在需要获取额外查找元数据的 [VOP_LOOKUP(9)](vop_lookup.9.md) 实现中非常有用。

## 参数描述符标志

这些标志用于多种目的。其中一些影响全局 `NDFREE_PNBUF` 操作，一些为特定路径元素的处理提供信息，例如由相关文件系统的 `VOP_LOOKUP` 实现使用。

**`RDONLY`** 指定查找应表现得如同最终节点位于只读挂载上。该标志通常由文件服务器（例如 NFS）用于处理只读导出。

**`ISRESTARTED`** `NDFREE_PNBUF` 已通过 `NDRESTART` 重新启动。这在 ABI 子系统使用的双根查找中内部使用，在本机根查找失败后。组件被重置为原始值，并使用不同的根重复一次查找。

**`IGNOREWHITEOUT`** 忽略 whiteout，例如在检查目录是否为空时。

**`ISWHITEOUT`** 查找结果是 whiteout。

**`DOWHITEOUT`** 处理 whiteout，这是 `VOP_LOOKUP` 文件系统方法的指令。

**`WILLBEDIR`** 查找是为创建将成为目录的新条目而执行的。它允许路径字符串中的尾部斜杠。

**`ISOPEN`** 调用者是打开文件的代码。如果挂载点指示扩展共享锁支持，这允许减弱返回 vnode 的锁模式。

**`NOCROSSMOUNT`** 查找期间不跨越挂载点。对于导致挂载根的 ".." 查找，返回挂载的根 vnode，而不是放置挂载的文件系统的被覆盖 vnode。对于跨越挂载的其他查找，不跳入被挂载的文件系统。这允许进入否则被挂载点遮蔽的文件层次结构。

**`NOMACCHECK`** 查找期间不执行 MAC 检查。

**`AUDITVNODE1`** 审计查找的 vnode 信息，使用第一个插槽存储审计信息。

**`AUDITVNODE2`** 与 `AUDITVNODE1` 相同，但使用第二个插槽。

**`NOCAPCHECK`** 不执行能力检查。如果调用进程处于能力模式，查找将被直接拒绝。

**`OPENREAD`** 查找是为了打开文件，且文件将以读方式打开。

**`OPENWRITE`** 查找是为了打开文件，且文件将以写方式打开。

**`WANTIOCTLCAPS`** 为调用者保留 ioctl 能力。参见 `NDFREE_PNBUF` 结果的描述。

**`OPENNAMED`** 打开命名属性（目录）。

**`NOEXECCHECK`** 不对起始目录执行允许执行的检查。它用于实现 openat(2) 查找所需的 POSIX 语义，即必须使用目录打开时的权限，而不是用于查找时的权限。

**`MAKEENTRY`** 查找到的条目将添加到名称缓存。

**`ISSYMLINK`** 当前组件是符号链接，需要根据 `FOLLOW` 或 `NOFOLLOW` 标志进行解释。

**`ISLASTCN`** 这是路径名的最后一个组件。它被特殊处理，许多标志会增强其处理。

**`ISDOTDOT`** 当前组件名是 ".."。通常意味着需要特殊处理 vnode 锁定以实例化目标 vnode。通用的 `vn_vget_ino_gen` 函数及其更特化的变体 `vn_vget_ino` 可能有帮助。

**`TRAILINGSLASH`** 路径以斜杠结尾。

**`CREATENAMED`** 创建命名属性目录。

## 分配的元素

`nameidata` 结构由以下字段组成：

**`ni_startdir`** 在正常情况下，这要么是当前目录，要么是根目录。如果传入的名称不以 `/` 开头且未经过任何具有绝对路径的符号链接，则为当前目录，否则为根目录。在这种情况下，它仅由 `vfs_lookup` 使用，在调用 `namei` 之后不应视为有效。

**`ni_dvp`** 指向执行查找的对象所在目录的 vnode 指针。如果设置了 `LOCKPARENT` 或 `WANTPARENT`，则在成功返回时可用。如果设置了 `LOCKPARENT`，则处于锁定状态。

**`ni_vp`** 指向结果对象的 vnode 指针，否则为 `NULL`。此 vnode 的 `v_usecount` 字段被递增。如果设置了 `LOCKLEAF`，则也处于锁定状态。

**`ni_cnd.cn_pnbuf`** 路径名缓冲区包含 `NDFREE_PNBUF` 操作将使用的文件或目录的位置。它由 uma(9) 区域分配接口管理。

## 结果

`struct namei` 成员 `ni_resflags` 返回以下标志，提供成功操作的某些细节：

**`NIRES_ABS`** 传入的路径是绝对路径。

**`NIRES_STRICTREL`** 受限查找结果。仅执行了相对查找以将路径解析为 vnode。

**`NIRES_EMPTYPATH`** 提供并使用了 `EMPTYPATH` 标志。特别是，传入的路径为空。

如果指定了 `WANTIOCTLCAPS` 标志，返回时 `struct namei` 的 `ni_file_capabilities` 成员包含用作查找起点（`dirfd`）的文件描述符的能力。

## 返回值

如果成功，`namei` 返回 0，否则返回错误。

## 文件

**src/sys/kern/vfs_lookup.c**

## 实例

假设 `path` 变量包含指向用户空间路径字符串的指针，以下示例查找由其命名的文件，并执行所需的错误和资源处理：

```c
	char *path;
	struct nameidata nd;
	int error;
	NDINIT(&nd, LOOKUP, FOLLOW | LOCKLEAF | AUDITVNODE1, UIO_USERSPACE,
	    path);
	if ((error = namei(&nd)) != 0)
		return (error);
	NDFREE_PNBUF(&nd);
	... use nd.ni_vp vnode
```

## 错误

`namei` 可能返回的错误：

**`ENOTDIR`** 当需要目录时，指定路径名的某个组件不是目录。

**`ENAMETOOLONG`** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**`ENOENT`** 指定路径名的某个组件不存在，或路径名为空字符串。

**`EACCES`** 试图以文件访问权限禁止的方式访问文件。

**`ELOOP`** 在转换路径名时遇到过多符号链接。

**`EISDIR`** 试图以写模式打开目录。

**`EINVAL`** 为 `DELETE` 或 `RENAME` 操作指定的路径名最后一个组件是 `.`。

**`EROFS`** 试图在只读文件系统上修改文件或目录。

## 参见

[uio(9)](uio.9.md), uma(9), [VFS(9)](vfs.9.md), [vnode(9)](vnode.9.md), vput(9), [vref(9)](vref.9.md), [vrele(9)](vrele.9.md)

## 作者

本手册页由 Eivind Eklund <eivind@FreeBSD.org> 编写，后由 Hiten M. Pandya <hmp@FreeBSD.org> 进行了大量修订。

## 缺陷

`LOCKPARENT` 标志并不总是导致父 vnode 被锁定。这在使用 `LOCKPARENT` 时会导致复杂性。为了在使用 `LOCKPARENT` 和 `LOCKLEAF` 的情况下解决此问题，需要诉诸递归锁定。
