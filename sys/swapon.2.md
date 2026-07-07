# swapon(2)

`swapon` — 控制用于交错分页/交换的设备

## 名称

`swapon`, `swapoff`

## 库

Lb libc

## 概要

`#include <vm/vm_param.h>`

`#include <vm/swap_pager.h>`

`#include <unistd.h>`

```c
int
swapon(const char *special);

int
swapoff(const char *special, u_int flags);
```

## 描述

`swapon()` 系统调用使块设备 `special` 可供系统分配用于分页和交换。系统已知潜在可用设备的名称，并在系统配置时定义。`special` 上交换区的大小在该设备首次启用交换时计算。

`swapoff()` 系统调用在给定设备上禁用分页和交换。所有关联的交换元数据均被释放，该设备可用于其他用途。

`special` 参数指向用于交换的设备或文件的名称。`flags` 参数接受以下标志：

**`SWAPOFF_FORCE`** 覆盖一项非常保守的检查，该检查在空闲内存总量与剩余交换设备空间可能不足以维持系统继续运行时阻止 swapoff。

## 返回值

如果发生错误，返回值为 -1，并设置 `errno` 以指示错误。

## 错误

`swapon()` 和 `swapoff()` 都可能因以下原因失败：

**[`ENOTDIR`]** 路径前缀的某个组成部分不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组成部分超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的设备不存在。

**[`EACCES`]** 对路径前缀的某个组成部分拒绝搜索权限。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 调用者不是超级用户。

**[`EFAULT`]** `special` 参数指向进程分配地址空间之外的位置。

此外，`swapon()` 还可能因以下原因失败：

**[`ENOTBLK`]** `special` 参数不是块设备。

**[`EBUSY`]** 由 `special` 指定的设备已经启用交换。

**[`ENXIO`]** `special` 的主设备号超出范围（这表示关联硬件没有对应的设备驱动程序）。

**[`EIO`]** 打开交换设备时发生 I/O 错误。

**[`EINTEGRITY`]** 在读取文件系统以打开交换设备时检测到损坏的数据。

最后，`swapoff()` 还可能因以下原因失败：

**[`EINVAL`]** 系统当前未向 `special` 进行交换。

**[`ENOMEM`]** 没有足够的虚拟内存可安全地禁用对给定设备的分页和交换。

## 参见

[config(8)](../man8/config.8.md), swapon(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`swapon()` 系统调用出现于 4.0BSD。`swapoff()` 系统调用出现于 FreeBSD 5.1。
