# dev_refthread(9)

`dev_refthread` — 安全访问设备方法

## 名称

`dev_refthread`, `devvn_refthread`, `dev_relthread`

## 概要

```c
#include <sys/param.h>
#include <sys/conf.h>

struct cdevsw *
dev_refthread(struct cdev *dev, int *ref)

struct cdevsw *
devvn_refthread(struct vnode *vp, struct cdev **devp, int *ref)

void
dev_relthread(struct cdev *dev, int ref)
```

## 描述

`dev_refthread`（或 `devvn_refthread`）和 `dev_relthread` 例程提供了一种安全的方式来访问可能被 `destroy_dev` 并发销毁的 [devfs(4)](../man4/devfs.4.md) 设备（例如可移动介质）。

如果成功，`dev_refthread` 和 `devvn_refthread` 会获取关联 `struct cdev` 的一个"线程引用"，并返回指向该 cdev 的 `struct cdevsw` 方法表的非 NULL 指针。在该引用持续期间，cdev 关联的私有数据和方法表对象有效。cdev 的销毁会睡眠等待线程引用被释放。

引用不能阻止介质移除。当设备处于待销毁状态时，个别驱动程序如何处理来自持有 `dev_refthread` 引用的调用者的方法调用，这是各个驱动程序的实现细节。对于磁盘设备，一种常见行为是返回 `ENXIO` 状态，但此 KPI 并不要求这样做。

`devvn_refthread` 是 `dev_refthread` 的变体，它在执行与 `dev_refthread` 相同的操作之前，自动从 `VCHR` [vnode(9)](vnode.9.md) 中提取 `struct cdev` 指针。此外，`struct cdev` 的指针通过 `*devp` 返回给调用者。`devvn_refthread` 正确处理 vnode 可能的并行回收。

`dev_relthread` 用于释放对 `struct cdev` 的引用。**必须**仅在关联的 `dev_refthread` 或 `devvn_refthread` 调用返回非 NULL 的 `struct cdevsw *` 时才调用 `dev_relthread`。

## 上下文

`struct cdev` 对象有两个引用计数：`si_refcount` 和 `si_threadcount`。`dev_refthread`、`devvn_refthread` 和 `dev_relthread` 函数操作 `si_threadcount`。`si_threadcount` 引用保证 `struct cdev` 对象的存活性。另一个 `si_refcount` 引用仅提供较弱的保证，即支撑 `struct cdev` 的内存尚未被释放。

## 返回值

如果 `dev_refthread` 或 `devvn_refthread` 不成功，它们返回 `NULL`。如果这些例程不成功，它们不会增加 `struct cdev` 的 `si_threadcount`，也不会以任何方式初始化 `*ref` 参数所指向的值。

## 参见

[devfs(4)](../man4/devfs.4.md), [destroy_dev(9)](destroy_dev.9.md)

## 注意事项

除非匹配的 refthread 例程成功，否则不要调用 `dev_relthread`！
