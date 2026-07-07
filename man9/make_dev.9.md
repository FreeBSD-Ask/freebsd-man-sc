# make_dev(9)

`make_dev` — 创建和销毁字符设备，包括 devfs 注册

## 名称

`make_dev`, `make_dev_cred`, `make_dev_credf`, `make_dev_p`, `make_dev_s`, `make_dev_alias`, `make_dev_alias_p`, `destroy_dev`, `destroy_dev_sched`, `destroy_dev_sched_cb`, `destroy_dev_drain`, `dev_depends`

## 概要

`#include <sys/param.h>`

`#include <sys/conf.h>`

`Ft void Fn make_dev_args_init struct make_dev_args *args Ft int Fn make_dev_s struct make_dev_args *args struct cdev **cdev const char *fmt ... Ft int Fn make_dev_alias_p int flags struct cdev **cdev struct cdev *pdev const char *fmt ... Ft void Fn destroy_dev struct cdev *dev Ft void Fn destroy_dev_sched struct cdev *dev Ft void Fn destroy_dev_sched_cb struct cdev *dev void (*cb)(void *) void *arg Ft void Fn destroy_dev_drain struct cdevsw *csw Ft void Fn dev_depends struct cdev *pdev struct cdev *cdev`

`LEGACY INTERFACES Ft struct cdev * Fn make_dev struct cdevsw *cdevsw int unit uid_t uid gid_t gid int perms const char *fmt ... Ft struct cdev * Fn make_dev_cred struct cdevsw *cdevsw int unit struct ucred *cr uid_t uid gid_t gid int perms const char *fmt ... Ft struct cdev * Fn make_dev_credf int flags struct cdevsw *cdevsw int unit struct ucred *cr uid_t uid gid_t gid int perms const char *fmt ... Ft int Fn make_dev_p int flags struct cdev **cdev struct cdevsw *devsw struct ucred *cr uid_t uid gid_t gid int mode const char *fmt ... Ft struct cdev * Fn make_dev_alias struct cdev *pdev const char *fmt ...`

## 描述

`make_dev_s` 函数为新设备创建一个 `cdev` 结构，并通过 `cdev` 参数返回。它还会通知 [devfs(4)](../man4/devfs.4.md) 新设备的存在，从而导致创建相应的节点。此外，还会发送 [devctl(4)](../man4/devctl.4.md) 通知。该函数接受 `struct make_dev_args args` 结构，该结构指定了设备创建的参数：

```c
struct make_dev_args {
	size_t		 mda_size;
	int		 mda_flags;
	struct cdevsw	*mda_devsw;
	struct ucred	*mda_cr;
	uid_t		 mda_uid;
	gid_t		 mda_gid;
	int		 mda_mode;
	int		 mda_unit;
	void		*mda_si_drv1;
	void		*mda_si_drv2;
};
```

在使用并填充所需值之前，必须通过 `make_dev_args_init` 函数初始化该结构，这确保未来的内核接口扩展不会影响驱动程序源代码或二进制接口。

创建的设备将由 `args.mda_uid` 拥有，组所有权为 `args.mda_gid`。名称是 `fmt` 及其后参数的展开，正如 [printf(9)](printf.9.md) 所打印的那样。该名称决定了它在 **/dev** 或其他 [devfs(4)](../man4/devfs.4.md) 挂载点下的路径，并且可以包含斜杠 `/` 字符以表示子目录。`args.mda_mode` 中指定的文件权限定义于

`#include <sys/stat.h>`

```c
#define S_IRWXU 0000700    /* 所有者的 RWX 掩码 */
#define S_IRUSR 0000400    /* 所有者可读 */
#define S_IWUSR 0000200    /* 所有者可写 */
#define S_IXUSR 0000100    /* 所有者可执行 */
#define S_IRWXG 0000070    /* 组的 RWX 掩码 */
#define S_IRGRP 0000040    /* 组可读 */
#define S_IWGRP 0000020    /* 组可写 */
#define S_IXGRP 0000010    /* 组可执行 */
#define S_IRWXO 0000007    /* 其他的 RWX 掩码 */
#define S_IROTH 0000004    /* 其他可读 */
#define S_IWOTH 0000002    /* 其他可写 */
#define S_IXOTH 0000001    /* 其他可执行 */
#define S_ISUID 0004000    /* 执行时设置用户 ID */
#define S_ISGID 0002000    /* 执行时设置组 ID */
#define S_ISVTX 0001000    /* 粘滞位 */
#ifndef _POSIX_SOURCE
#define S_ISTXT 0001000
#endif
```

`args.mda_cr` 参数指定将存储在已初始化 `struct cdev` 的 `si_cred` 成员中的凭证。

`args.mda_flags` 参数改变 `make_dev_s` 的操作。当前接受以下值：

**`MAKEDEV_REF`** 引用所创建的设备

**`MAKEDEV_NOWAIT`** 不睡眠，调用可能失败

**`MAKEDEV_WAITOK`** 允许函数睡眠以满足 malloc

**`MAKEDEV_ETERNAL`** 创建的设备永远不会被销毁

**`MAKEDEV_CHECKNAME`** 如果设备名称无效或已存在则返回错误

`make_dev_alias_p` 函数仅接受 `MAKEDEV_NOWAIT`、`MAKEDEV_WAITOK` 和 `MAKEDEV_CHECKNAME` 值。

如果未指定 `MAKEDEV_WAITOK`、`MAKEDEV_NOWAIT` 中的任何一个，则假定使用 `MAKEDEV_WAITOK` 标志。

[dev_clone(9)](dev_clone.9.md) 事件处理程序在响应查找而创建设备时应指定 `MAKEDEV_REF` 标志，以避免在 `devfs_lookup` 释放其对 `cdev` 的引用后创建的设备立即被销毁的竞态。

`MAKEDEV_ETERNAL` 标志允许内核在将系统调用转换为 cdevsw 方法调用时不获取某些锁。驱动程序作者有责任确保永远不会对返回的 cdev 调用 `destroy_dev`。为方便起见，对于可以编译进内核或作为可加载模块加载（和卸载）的代码，请使用 `MAKEDEV_ETERNAL_KLD` 标志。

如果未指定 `MAKEDEV_CHECKNAME` 标志且设备名称无效或已存在，将发生 panic。

`make_dev_p` 的使用形式：

```c
struct cdev *dev;
int res;
res = make_dev_p(flags, &dev, cdevsw, cred, uid, gid, perms, name);
```

等价于以下代码：

```c
struct cdev *dev;
struct make_dev_args args;
int res;
make_dev_args_init(&args);
args.mda_flags = flags;
args.mda_devsw = cdevsw;
args.mda_cr = cred;
args.mda_uid = uid;
args.mda_gid = gid;
args.mda_mode = perms;
res = make_dev_s(&args, &dev, name);
```

类似地，`make_dev_credf` 函数调用等价于：

```c
(void) make_dev_s(&args, &dev, name);
```

换句话说，`make_dev_credf` 不允许调用者获取返回值，并且在使用 `INVARIANTS` 选项编译的内核中，该函数断言设备创建成功。

`make_dev_cred` 函数等价于调用：

```c
make_dev_credf(0, cdevsw, unit, cr, uid, gid, perms, fmt, ...);
```

`make_dev` 函数调用与以下相同：

```c
make_dev_credf(0, cdevsw, unit, NULL, uid, gid, perms, fmt, ...);
```

`make_dev_alias_p` 函数接受 `make_dev` 返回的 `cdev`，并为该设备创建另一个（别名）名称。在调用 `make_dev` 之前调用 `make_dev_alias_p` 是错误的。

`make_dev_alias` 函数类似于 `make_dev_alias_p`，但它返回生成的别名 `*cdev`，并且不会返回错误。

`make_dev_s` 和 `make_dev_alias_p` 返回的 `cdev` 有两个字段，`si_drv1` 和 `si_drv2`，可用于存储状态。这两个字段都是 `void *` 类型，可以通过填充 `make_dev_s` 参数结构的 `args.mda_si_drv1` 和 `args.mda_si_drv2` 成员在分配 `cdev` 的同时进行初始化，或者在使用旧接口时在分配 `cdev` 之后填充。在后一种情况下，驱动程序应自行处理访问未初始化的 `si_drv1` 和 `si_drv2` 的竞态。这些字段旨在替代 `make_dev` 的 `unit` 参数，后者可以通过 `dev2unit` 获取。

`destroy_dev` 函数接受 `make_dev` 返回的 `cdev` 并销毁该设备的注册。会向 [devctl(4)](../man4/devctl.4.md) 发送有关销毁事件的通知。不要对通过 `make_dev_alias` 创建的设备调用 `destroy_dev`。

`dev_depends` 函数在两个设备之间建立父子关系。最终效果是，对父设备调用 `destroy_dev` 也会导致子设备（如果存在）被销毁。一个设备可以同时是父设备和子设备，因此可以构建完整的层次结构。

`destroy_dev_sched_cb` 函数在安全上下文中调度指定 `cdev` 的 `destroy_dev` 执行。在 `destroy_dev` 完成之后，如果提供的 `cb` 不为 `NULL`，则会以 `arg` 为参数调用回调 `cb`。`destroy_dev_sched` 函数与以下相同：

```c
destroy_dev_sched_cb(cdev, NULL, NULL);
```

`d_close` 驱动程序方法和 devfs_cdevpriv(9) `dtr` 方法都不能直接调用 `destroy_dev`。这样做会在 `destroy_dev` 等待所有线程离开驱动程序方法并完成执行任何每次打开的析构函数时导致死锁。此外，由于 `destroy_dev` 会睡眠，调用期间不能持有任何不可睡眠的锁。`destroy_dev_sched` 系列函数克服了这些问题。

设备驱动程序可以调用 `destroy_dev_drain` 函数来等待所有以 `csw` 作为 cdevsw 的设备被销毁。当驱动程序知道已对所有实例化的设备调用了 `destroy_dev_sched`，但需要将模块卸载推迟到所有设备的 `destroy_dev` 实际完成时，这很有用。

## 返回值

如果成功，`make_dev_s` 和 `make_dev_p` 将返回 0，否则返回错误。如果成功，`make_dev_credf` 将返回有效的 `cdev` 指针，否则返回 `NULL`。

## 错误

`make_dev_s`、`make_dev_p` 和 `make_dev_alias_p` 调用将失败，设备将不会被注册，如果：

**[ENOMEM]** 指定了 `MAKEDEV_NOWAIT` 标志且无法满足内存分配请求。

**[ENAMETOOLONG]** 指定了 `MAKEDEV_CHECKNAME` 标志且提供的设备名称长于 `SPECNAMELEN`。

**[EINVAL]** 指定了 `MAKEDEV_CHECKNAME` 标志且提供的设备名称为空、包含 "." 或 ".." 路径组件或以 `/` 结尾。

**[EINVAL]** 指定了 `MAKEDEV_CHECKNAME` 标志且提供的设备名称包含无效字符。

**[EEXIST]** 指定了 `MAKEDEV_CHECKNAME` 标志且提供的设备名称已存在。

## 参见

[devctl(4)](../man4/devctl.4.md), [devfs(4)](../man4/devfs.4.md), [dev_clone(9)](dev_clone.9.md)

## 历史

`make_dev` 和 `destroy_dev` 函数首次出现于 FreeBSD 4.0。函数 `make_dev_alias` 首次出现于 FreeBSD 4.1。函数 `dev_depends` 首次出现于 FreeBSD 5.0。函数 `make_dev_credf`、`destroy_dev_sched`、`destroy_dev_sched_cb` 首次出现于 FreeBSD 7.0。函数 `make_dev_p` 首次出现于 FreeBSD 8.2。函数 `make_dev_s` 首次出现于 FreeBSD 11.0。
