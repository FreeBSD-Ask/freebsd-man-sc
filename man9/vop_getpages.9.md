# VOP_GETPAGES(9)

`VOP_GETPAGES` — 从文件读取或写入 VM 页面

## 名称

`VOP_GETPAGES`, `VOP_PUTPAGES`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <vm/vm.h>

int
VOP_GETPAGES(struct vnode *vp, vm_page_t *ma, int count, int *rbehind,
    int *rahead)

int
VOP_PUTPAGES(struct vnode *vp, vm_page_t *ma, int bytecount, int flags,
    int *rtvals)
```

## 描述

`VOP_GETPAGES` 方法被调用以读取由普通文件支持的虚拟内存页面。如果其他相邻页面由同一文件的相邻区域支持，则请求 `VOP_GETPAGES` 也读取这些页面，尽管并不要求它必须这样做。`VOP_PUTPAGES` 方法执行相反的操作；也就是说，它写出相邻的脏虚拟内存页面。

在入口时，持有 vnode 锁，但不持有页面队列和 VM 对象锁。这两种方法在成功和错误返回时都处于相同状态。

参数为：

**`vp`** 要访问的文件。

**`ma`** 指向表示要读取或写入的文件连续区域的页面数组第一个元素的指针。

**`count`** `ma` 数组的长度。

**`bytecount`** 应从数组页面中写入的字节数。

**`flags`** 影响函数操作的标志位字段。如果设置了 `VM_PAGER_PUT_SYNC`，写入应是同步的；在写入完成之前不得将控制返回给调用者。如果设置了 `VM_PAGER_PUT_INVAL`，页面在写入后将被失效。如果设置了 `VM_PAGER_PUT_NOREUSE`，执行的 I/O 应设置 IO_NOREUSE 标志，以向文件系统指示页面应在需要时标记为快速重用。这可以通过调用 vm_page_deactivate_noreuse(9) 来实现，该函数将此类页面放到非活动队列的头部。如果设置了 `VM_PAGER_CLUSTER_OK`，写入可以被延迟，以便相关的写入可以合并以提高效率，例如使用缓冲区缓存的群集机制。

**`rtvals`** VM 系统结果代码数组，指示 `VOP_PUTPAGES` 写入的每个页面的状态。

**`rbehind`** 可选的指向整数的指针，指定如果可能要回读的页面数。如果文件系统支持该功能，将回报实际读取的页面数，否则返回零。

**`rahead`** 可选的指向整数的指针，指定如果可能要预读的页面数。如果文件系统支持该功能，将回报实际读取的页面数，否则返回零。

`VOP_PUTPAGES` 方法的状态以逐页方式在数组 `rtvals[]` 中返回。可能的状态值如下：

**`VM_PAGER_OK`** 页面成功写入。实现必须调用 vm_page_undirty(9) 将页面标记为干净。

**`VM_PAGER_PEND`** 页面被调度为异步写入。当写入完成时，完成回调应调用 vm_object_pip_wakeup(9) 和 vm_page_sunbusy(9) 以清除忙标志并唤醒等待此页面的其他线程，此外还要调用 vm_page_undirty(9)。

**`VM_PAGER_BAD`** 页面完全超出支持文件的末尾。如果 vnode 的文件系统正确实现，这种情况不应可能出现。

**`VM_PAGER_ERROR`** 由于底层存储介质或协议上的错误，页面无法写入。

**`VM_PAGER_FAIL`** 处理方式与 `VM_PAGER_ERROR` 相同。

**`VM_PAGER_AGAIN`** 此请求未处理该页面。

`VOP_GETPAGES` 方法必须填充并验证所有请求的页面才能返回成功。预期它会通过调用 [vm_page_free(9)](vm_page_free.9.md) 释放 `ma` 中未成功处理的任何页面。成功时，`VOP_GETPAGES` 必须适当设置有效位。进入 `VOP_GETPAGES` 时，`ma` 中的所有页面都以独占方式忙碌。成功返回时，页面也必须全部以独占方式忙碌，但在处理过程中页面可以被解除忙碌。文件系统负责激活换出的页面，但这不一定需要在 `VOP_GETPAGES` 中完成，具体取决于特定文件系统的架构。

## 返回值

如果 `VOP_GETPAGES` 成功读取 `ma` 中的所有页面，则返回 `VM_PAGER_OK`；否则返回 `VM_PAGER_ERROR`。按照约定，`VOP_PUTPAGES` 的返回值为 `rtvals[0]`。

## 参见

vm_object_pip_wakeup(9), [vm_page_free(9)](vm_page_free.9.md), vm_page_sunbusy(9), vm_page_undirty(9), vm_page_xunbusy(9), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写，后来由 Garrett Wollman 大幅重写。
