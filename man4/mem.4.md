# mem(4)

`mem` — 内存文件

## 名称

`mem`, `kmem`

## 概要

`device mem`

## 描述

特殊文件 **`/dev/mem`** 是计算机物理内存的接口。此文件中的字节偏移量被解释为物理内存地址。读写此文件等同于读写内存本身。仅允许 **`/dev/mem`** 范围内的偏移量。

内核虚拟内存通过 **`/dev/kmem`** 接口以与 **`/dev/mem`** 相同的方式访问。仅允许当前映射到内存的内核虚拟地址。

在 ISA 上，I/O 内存空间从物理地址 0x000a0000 开始，到 0x00100000 结束。当前进程的每进程数据大小为 `UPAGES` 长，并在虚拟地址 0xf0000000 处结束。

## IOCTL 接口

### 地址属性

`MEM_EXTRACT_PADDR` ioctl 可用于查找调用进程地址空间中给定虚拟地址的物理地址和 NUMA 域。该请求由以下结构描述：

```sh
struct mem_extract {
	uint64_t	me_vaddr;	/* 输入 */
	uint64_t	me_paddr;	/* 输出 */
	int		me_domain;	/* 输出 */
	int		me_state;	/* 输出 */
};
```

如果地址无效，ioctl 会返回错误。`MEM_EXTRACT_PADDR` 返回的信息在 ioctl 调用返回时可能已过时。具体而言，并发的系统调用、页面错误或系统页面回收活动可能已在 ioctl 调用返回之前取消映射虚拟页或替换了后端物理页。已锁定的页（例如由 mlock(2) 锁定的页）不会被系统回收。

`me_state` 字段提供有关虚拟页状态的信息：

**`ME_STATE_INVALID`** 虚拟地址无效。

**`ME_STATE_VALID`** 虚拟地址有效，但在 ioctl 调用时未映射。

**`ME_STATE_MAPPED`** 虚拟地址对应于物理页映射，`me_paddr` 和 `me_domain` 字段有效。

### 内存范围

一些架构允许将属性与物理内存范围相关联。这些属性可以通过对 **`/dev/mem`** 执行 ioctl 调用来操作。声明和数据类型可在以下头文件中找到：

`#include <sys/memrange.h>`

具体属性和可编程范围数因架构而异。支持的完整属性集为：

**`MDF_UNCACHEABLE`** 该区域不被缓存。

**`MDF_WRITECOMBINE`** 对该区域的写入可能被合并或乱序执行。

**`MDF_WRITETHROUGH`** 对该区域的写入同步提交。

**`MDF_WRITEBACK`** 对该区域的写入异步提交。

**`MDF_WRITEPROTECT`** 该区域不可写入。

内存范围由以下结构描述：

```sh
struct mem_range_desc {
	uint64_t	mr_base;	/* 物理基地址 */
	uint64_t	mr_len;		/* 区域物理长度 */
	int		mr_flags;	/* 区域属性 */
	char		mr_owner[8];
};
```

除了上面列出的区域属性外，`mr_flags` 字段中还可设置以下标志：

**MDF_FIXBASE** 该区域的基地址无法更改。

**MDF_FIXLEN** 该区域的长度无法更改。

**MDF_FIRMWARE** 该区域被认为是系统固件建立的。

**MDF_ACTIVE** 该区域当前处于活动状态。

**MDF_BOGUS** 我们认为该区域无效或有其他错误。

**MDF_FIXACTIVE** 该区域无法禁用。

**MDF_BUSY** 该区域当前由另一个进程拥有，无法更改。

操作使用以下结构执行：

```sh
struct mem_range_op {
	struct mem_range_desc	*mo_desc;
	int			mo_arg[2];
};
```

`MEMRANGE_GET` ioctl 用于检索当前内存范围属性。如果 `mo_arg[0]` 设置为 0，它将更新为内存范围描述符的总数。如果大于 0，`mo_desc` 处的数组将填充相应数量的描述符结构，或最大数量，取较小者。

`MEMRANGE_SET` ioctl 用于添加、更改和删除内存范围属性。具有 `MDF_FIXACTIVE` 标志的范围无法删除；具有 `MDF_BUSY` 标志的范围无法删除或更新。

`mo_arg[0]` 应设置为 `MEMRANGE_SET_UPDATE` 以更新现有范围或建立新范围，或设置为 `MEMRANGE_SET_REMOVE` 以删除范围。

### 实时内核转储

`MEM_KERNELDUMP` ioctl 将针对运行中的系统启动内核转储，其内容将写入进程拥有的文件描述符。生成的转储输出将采用 minidump 格式。该请求由以下结构描述：

```sh
struct mem_livedump_arg {
	int	fd;		/* 输入 */
	int	flags		/* 输入 */
	uint8_t	compression	/* 输入 */
};
```

`fd` 字段用于传递文件描述符。

`flags` 字段当前未使用，必须设置为零。

`compression` 字段可用于指定要应用于转储输出的所需压缩。支持的值定义于：

`#include <sys/kerneldump.h>`

即 `KERNELDUMP_COMP_NONE`、`KERNELDUMP_COMP_GZIP` 或 `KERNELDUMP_COMP_ZSTD`。

针对运行中系统进行的内核转储可能由于转储过程中并发的内存分配、释放或修改而导致内核数据结构不一致。因此，生成的核心转储不保证可用。负载较重的系统更可能产生不一致的结果。尽管如此，实时内核转储对于离线调试某些类型的内核错误（如死锁）或检查系统状态的特定部分仍然有用。

## 返回值

### MEM_EXTRACT_PADDR

`MEM_EXTRACT_PADDR` ioctl 始终返回零值。

### MEMRANGE_GET/MEMRANGE_SET

**[Er** EOPNOTSUPP] 此架构不支持内存范围操作。

**[Er** ENXIO] 没有可用的内存范围描述符（例如，固件未启用任何描述符）。

**[Er** EINVAL] 作为参数提供的内存范围无效，或以本架构不支持的方式与另一范围重叠。

**[Er** EBUSY] 由于范围繁忙，删除或更新范围的尝试失败。

**[Er** ENOSPC] 由于硬件资源短缺（例如，描述符槽位），创建新范围的尝试失败。

**[Er** ENOENT] 由于没有范围与提供的描述符基地址/长度匹配，删除范围的尝试失败。

**[Er** EPERM] 由于范围被永久启用，删除范围的尝试失败。

### MEM_KERNELDUMP

**[Er** EOPNOTSUPP] 此架构不支持内核 minidump。

**[Er** EPERM] 由于调用线程缺乏特权，启动内核转储的尝试失败。

**[Er** EBADF] 提供的文件描述符无效，或没有写权限。

**[Er** EBUSY] 由于已有转储进行中，启动内核转储的尝试失败。

**[Er** EINVAL] 在 `flags` 中指定了无效或不支持的值。

**[Er** EINVAL] 指定了无效或不支持的压缩类型。`PRIV_KMEM_READ` 特权。

## 文件

**`/dev/mem`**

**`/dev/kmem`**

## 参见

kvm(3), memcontrol(8)

## 历史

**`/dev/mem`** 文件出现于 Version 1 AT&T UNIX，**`/dev/kmem`** 出现于 Version 5 AT&T UNIX。内存范围属性的 ioctl 接口在 FreeBSD 3.2 中添加。

## 缺陷

繁忙范围属性尚未得到正确管理。

所有 kvm(3) 的用户都需要此设备才能运行。
