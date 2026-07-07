# memguard(9)

`MemGuard` — 用于调试目的的内存分配器

## 名称

`MemGuard`

## 概要

```c
options DEBUG_MEMGUARD
```

## 描述

`MemGuard` 是一个简单且小型的替代内存分配器，旨在帮助检测释放后篡改场景。这类问题越来越常见，并且在多线程内核中由于竞态条件更为普遍而更可能发生。

`MemGuard` 可接管单一 malloc 类型的 `malloc`、`realloc` 和 `free`。或者，`MemGuard` 可接管单一 uma(9) zone 的 `uma_zalloc`、`uma_zalloc_arg` 和 `uma_free`。`MemGuard` 还可以保护所有大于 `PAGE_SIZE` 的分配，并可保护所有分配的随机一部分。还有一个旋钮可防止小于指定大小的分配被保护，以限制内存浪费。

## 实例

要将 `MemGuard` 用于某种内存类型，可在 **/boot/loader.conf** 中添加一项：

```sh
vm.memguard.desc=<memory_type>
```

或在运行时设置 `vm.memguard.desc` [sysctl(8)](../man8/sysctl.8.md) 变量：

```sh
sysctl vm.memguard.desc=<memory_type>
```

其中 `memory_type` 可为要监视的内存类型的简短描述，或 uma(9) zone 的名称。只有在设置 `vm.memguard.desc` 之后从该 `memory_type` 进行的分配才可能被保护。如果在运行时修改 `vm.memguard.desc`，则只有在设置 [sysctl(8)](../man8/sysctl.8.md) 之后，新 `memory_type` 的分配才可能被保护。现有的受保护分配仍将由 free(9) 或 uma_zfree(9) 正确释放，具体取决于接管的是哪种分配。

要确定 [malloc(9)](malloc.9.md) 类型的简短描述，可以从 [vmstat(8)](../man8/vmstat.8.md) `-m` 输出的第一列中获取，或在内核源码中查找。它是 MALLOC_DEFINE(9) 宏的第二个参数。要确定 uma(9) zone 的名称，可以从 [vmstat(8)](../man8/vmstat.8.md) `-z` 输出的第一列中获取，或在内核源码中查找。它是 uma_zcreate(9) 函数的第一个参数。

`vm.memguard.divisor` 引导时可调参数用于缩放 `MemGuard` 允许使用的系统物理内存量。默认为 10，因此最多可使用 `vm_cnt.v_page_count`/10 页。`MemGuard` 将保留 `vm_kmem_max` / `vm.memguard.divisor` 字节的虚拟地址空间，受两倍物理内存大小限制。物理限制报告为 `vm.memguard.phys_limit`，为 `MemGuard` 保留的虚拟空间报告为 `vm.memguard.mapsize`。

对于小于 `vm.memguard.minsize` 字节的任何分配，`MemGuard` 不会执行页面提升。默认为 0，意味着所有分配都可能被保护。`MemGuard` 可以随机保护足够大的分配，平均频率为每 100000 / `vm.memguard.frequency` 次分配一次。默认为 0，意味着不随机保护任何分配。

如果 `vm.memguard.options` 的第 1 位被设置，`MemGuard` 可选择在每个分配周围添加未映射的保护页以检测溢出和下溢。此选项默认启用。如果 `vm.memguard.options` 的第 2 位被设置，`MemGuard` 将保护所有 `PAGE_SIZE` 或更大的分配。此选项默认关闭。默认情况下，`MemGuard` 不保护以 `UMA_ZONE_NOFREE` 标志初始化的 uma(9) zone，因为可能对其产生误报。但可通过设置 `vm.memguard.options` 可调参数的第 3 位来关闭此安全措施。

## 参见

[sysctl(8)](../man8/sysctl.8.md), [vmstat(8)](../man8/vmstat.8.md), [contigmalloc(9)](contigmalloc.9.md), [malloc(9)](malloc.9.md), [redzone(9)](redzone.9.md), uma(9)

## 历史

`MemGuard` 首次出现于 FreeBSD 6.0。

## 作者

`MemGuard` 最初由 Bosko Milekic <bmilekic@FreeBSD.org> 编写。本手册页最初由 Christian Brueffer <brueffer@FreeBSD.org> 编写。Matthew Fleming <mdf@FreeBSD.org> 和 Gleb Smirnoff <glebius@FreeBSD.org> 对实现和文档均做了补充。
