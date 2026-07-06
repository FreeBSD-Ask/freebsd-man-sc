# bus_dma.9

`bus_dma` — 总线与机器无关的 DMA 映射接口

## 名称

`bus_dma`, `bus_dma_tag_create`, `bus_dma_tag_destroy`, `bus_dma_template_init`, `bus_dma_template_tag`, `bus_dma_template_clone`, `bus_dma_template_fill`, `BUS_DMA_TEMPLATE_FILL`, `bus_dmamap_create`, `bus_dmamap_destroy`, `bus_dmamap_load`, `bus_dmamap_load_bio`, `bus_dmamap_load_ccb`, `bus_dmamap_load_crp`, `bus_dmamap_load_crp_buffer`, `bus_dmamap_load_mbuf`, `bus_dmamap_load_mbuf_sg`, `bus_dmamap_load_uio`, `bus_dmamap_unload`, `bus_dmamap_sync`, `bus_dmamem_alloc`, `bus_dmamem_free`

## 概要

```c
#include <machine/bus.h>

int
bus_dma_tag_create(bus_dma_tag_t parent, bus_size_t alignment,
    bus_addr_t boundary, bus_addr_t lowaddr, bus_addr_t highaddr,
    bus_dma_filter_t *filtfunc, void *filtfuncarg, bus_size_t maxsize,
    int nsegments, bus_size_t maxsegsz, int flags,
    bus_dma_lock_t *lockfunc, void *lockfuncarg, bus_dma_tag_t *dmat)

int
bus_dma_tag_destroy(bus_dma_tag_t dmat)

void
bus_dma_template_init(bus_dma_template_t *template, bus_dma_tag_t parent)

int
bus_dma_template_tag(bus_dma_template_t *template, bus_dma_tag_t *dmat)

void
bus_dma_template_clone(bus_dma_template_t *template, bus_dma_tag_t dmat)

void
bus_dma_template_fill(bus_dma_template_t *template,
    bus_dma_param_t params[], u_int count)

BUS_DMA_TEMPLATE_FILL(bus_dma_template_t *template, bus_dma_param_t param, ...)

int
bus_dmamap_create(bus_dma_tag_t dmat, int flags, bus_dmamap_t *mapp)

int
bus_dmamap_destroy(bus_dma_tag_t dmat, bus_dmamap_t map)

int
bus_dmamap_load(bus_dma_tag_t dmat, bus_dmamap_t map, void *buf,
    bus_size_t buflen, bus_dmamap_callback_t *callback,
    void *callback_arg, int flags)

int
bus_dmamap_load_bio(bus_dma_tag_t dmat, bus_dmamap_t map,
    struct bio *bio, bus_dmamap_callback_t *callback,
    void *callback_arg, int flags)

int
bus_dmamap_load_ccb(bus_dma_tag_t dmat, bus_dmamap_t map,
    union ccb *ccb, bus_dmamap_callback_t *callback,
    void *callback_arg, int flags)

int
bus_dmamap_load_crp(bus_dma_tag_t dmat, bus_dmamap_t map,
    struct crypto *crp, bus_dmamap_callback_t *callback,
    void *callback_arg, int flags)

int
bus_dmamap_load_crp_buffer(bus_dma_tag_t dmat, bus_dmamap_t map,
    struct crypto_buffer *cb, bus_dmamap_callback_t *callback,
    void *callback_arg, int flags)

int
bus_dmamap_load_mbuf(bus_dma_tag_t dmat, bus_dmamap_t map,
    struct mbuf *mbuf, bus_dmamap_callback2_t *callback,
    void *callback_arg, int flags)

int
bus_dmamap_load_mbuf_sg(bus_dma_tag_t dmat, bus_dmamap_t map,
    struct mbuf *mbuf, bus_dma_segment_t *segs, int *nsegs, int flags)

int
bus_dmamap_load_uio(bus_dma_tag_t dmat, bus_dmamap_t map,
    struct uio *uio, bus_dmamap_callback2_t *callback,
    void *callback_arg, int flags)

void
bus_dmamap_unload(bus_dma_tag_t dmat, bus_dmamap_t map)

void
bus_dmamap_sync(bus_dma_tag_t dmat, bus_dmamap_t map, op)

int
bus_dmamem_alloc(bus_dma_tag_t dmat, void **vaddr, int flags,
    bus_dmamap_t *mapp)

void
bus_dmamem_free(bus_dma_tag_t dmat, void *vaddr, bus_dmamap_t map)
```

## 描述

直接内存访问（DMA）是一种不涉及 CPU 的数据传输方法，因此提供更高的性能。DMA 事务可以在设备到内存、设备到设备或内存到内存之间进行。

`bus_dma` API 是总线、设备和机器无关（MI）的 DMA 机制接口。它通过抽象机器相关的问题（如设置 DMA 映射、处理缓存问题、总线特定功能和限制），为客户提供灵活性和简洁性。

## 概览

标签结构（`bus_dma_tag_t`）用于描述一组相关 DMA 事务的属性。一种理解方式是标签描述了 DMA 引擎的限制。例如，如果设备中的 DMA 引擎限制为 32 位地址，则在为该设备创建标签时通过参数指定此限制。类似地，可以将标签标记为要求缓冲区地址对齐到特定边界。

某些设备可能需要多个标签来描述具有不同属性的 DMA 事务。例如，设备可能要求其描述符环 16 字节对齐，而允许 I/O 缓冲区任意对齐。在这种情况下，驱动程序必须为描述符环创建一个标签，为 I/O 缓冲区创建单独的标签。如果设备除了不同事务组之间不同的限制外，还有所有 DMA 事务共有的限制，驱动程序可以首先创建一个描述这些共有限制的"父"标签。然后每组标签可以从这个"父"标签继承这些限制，而不必在创建每组标签时显式列出。

映射结构（`bus_dmamap_t`）表示内存区域的 DMA 映射。在具有 I/O MMU 的系统上，映射结构跟踪请求使用的任何 I/O MMU 条目。对于需要弹跳页的 DMA 请求，映射跟踪使用的弹跳页。

要准备一个或多个 DMA 事务，必须通过调用 `bus_dmamap_load` 系列函数之一将映射绑定到内存区域。这些函数配置映射，可能包括在 I/O MMU 中编程条目和/或分配弹跳页。这些函数的输出（直接或通过调用回调例程间接）是消费者可以传递给 DMA 引擎以访问内存区域的散布/聚集地址范围列表。当不再需要映射时，必须通过 `bus_dmamap_unload` 卸载映射。

在每次 DMA 事务前后，必须使用 `bus_dmamap_sync` 确保 DMA 引擎和 CPU 使用正确的数据。如果映射使用弹跳页，同步操作在弹跳页和绑定到映射的内存区域之间复制数据。同步操作还处理架构特定的细节，如 CPU 缓存刷新和 CPU 内存操作排序。

## 静态与动态

`bus_dma` 处理两种类型的 DMA 事务：静态和动态。静态事务用于长期存在的内存区域，该区域为许多事务重复使用，如描述符环。动态事务用于与瞬态缓冲区的传输，如保存网络数据包或磁盘块的 I/O 缓冲区。每种事务类型使用 `bus_dma` API 的不同子集。

### 静态事务

静态事务使用由 `bus_dmamem_alloc` 分配的内存区域。每个静态内存区域通过调用 `bus_dmamem_alloc` 分配。此函数需要一个有效的标签来描述到此区域的 DMA 事务的属性，如对齐或地址限制。如果多个区域共享相同的限制，可以共享单个标签。

`bus_dmamem_alloc` 分配内存区域和映射对象。然后必须将关联的标签、内存区域和映射对象传递给 `bus_dmamap_load` 以将映射绑定到分配的区域并获取散布/聚集列表。

预期 `bus_dmamem_alloc` 将尝试分配需要较少昂贵同步操作的内存（例如，实现不应分配需要弹跳页的区域），但仍应使用同步操作。例如，驱动程序应在中断处理程序中使用 `bus_dmamap_sync` 读取设备在中断前写入的描述符环条目。

当消费者完成使用内存区域时，应通过 `bus_dmamap_unload` 卸载映射，然后通过 `bus_dmamem_free` 释放内存区域和映射对象。

### 动态事务

动态事务映射由系统其他部分提供的内存区域。必须通过 `bus_dma_tag_create` 创建标签来描述到这些内存区域的 DMA 事务，并且必须通过 `bus_dmamap_create` 分配映射对象池以跟踪任何进行中的事务的映射。

当消费者希望为内存区域调度事务时，消费者必须首先从其映射对象池中获取未使用的映射对象。必须通过 `bus_dmamap_load` 系列函数之一将内存区域绑定到映射对象。在调度事务之前，消费者应使用一个或多个"PRE"标志通过 `bus_dmamap_sync` 同步内存区域。事务完成后，消费者应使用一个或多个"POST"标志通过 `bus_dmamap_sync` 同步内存区域。然后可以通过 `bus_dmamap_unload` 卸载映射，并将映射对象返回到未使用映射对象池。

当消费者不再调度 DMA 事务时，应通过 `bus_dmamap_destroy` 释放映射对象，通过 `bus_dma_tag_destroy` 释放标签。

## 结构和类型

```c
	alignment	1
	boundary	0
	lowaddr		BUS_SPACE_MAXADDR
	highaddr	BUS_SPACE_MAXADDR
	maxsize		BUS_SPACE_MAXSIZE
	nsegments	BUS_SPACE_UNRESTRICTED
	maxsegsize	BUS_SPACE_MAXSIZE
	flags		0
	lockfunc	NULL
	lockfuncarg	NULL
```

```c
int client_filter(void *filtarg, bus_addr_t testaddr)
```

```c
	bus_addr_t	ds_addr;
	bus_size_t	ds_len;
```

```c
void client_callback(void *callback_arg, bus_dma_segment_t *segs,
    int nseg, int error)
```

```c
void client_callback2(void *callback_arg, bus_dma_segment_t *segs,
    int nseg, bus_size_t mapsize, int error)
```

**`BUS_DMASYNC_PREREAD`** 在设备更新主机内存之前执行所需的任何同步。

**`BUS_DMASYNC_PREWRITE`** 在 CPU 更新主机内存之后、设备访问主机内存之前执行所需的任何同步。

**`BUS_DMASYNC_POSTREAD`** 在设备更新主机内存之后、CPU 访问主机内存之前执行所需的任何同步。

**`BUS_DMASYNC_POSTWRITE`** 在设备访问主机内存之后执行所需的任何同步。

```c
void lockfunc(void *lockfuncarg, bus_dma_lock_op_t op)
```

**`BUS_DMA_LOCK`** 获取和/或锁定客户端锁定原语。

**`BUS_DMA_UNLOCK`** 释放和/或解锁客户端锁定原语。

**`bus_dma_tag_t`** 机器相关（MD）不透明类型，描述一组 DMA 事务的特征。DMA 标签组织成层次结构，每个子标签继承其父标签的限制。这允许 DMA 事务路径上的所有设备为这些事务的约束做出贡献。

**`bus_dma_template_t`** 模板是一种从一组默认值创建 `bus_dma_tag_t` 的结构。通过 `bus_dma_template_init` 初始化后，驱动程序可以覆盖单个字段以适应其需求。以下字段以指示的默认值开始：每个字段的描述在 `bus_dma_tag_create` 中记录。注意，DMA 标签的 `filtfunc` 和 `filtfuncarg` 属性在模板中不受支持。

**`bus_dma_filter_t`** 客户端指定的地址过滤器，格式如下：可以在标签创建期间指定地址过滤器，以适应其 DMA 地址限制无法由单个窗口指定的设备。`filtarg` 参数由客户端在标签创建期间指定，传递给回调的所有调用。`testaddr` 参数包含 DMA 映射的潜在起始地址。过滤器函数对从 `testaddr` 到 `trunc_page(testaddr) + PAGE_SIZE - 1`（含）的地址集进行操作。如果此范围内的任何映射可以被设备容纳，过滤器函数应返回零，否则返回非零。*注意：不再支持使用过滤器，将导致错误。*

**`bus_dma_segment_t`** 机器相关类型，描述单个 DMA 段。它包含以下字段：`ds_addr` 字段包含 DMA 段的设备可见地址，`ds_len` 包含 DMA 段的长度。虽然映射调用返回的 DMA 段将遵守成功 DMA 操作所需的所有限制，但在向设备呈现段信息时，几乎总是需要一些转换（例如从主机字节顺序到设备字节顺序的转换）。

**`bus_dmamap_t`** 机器相关不透明类型，描述单个映射。每个要加载的内存分配使用一个映射。映射一旦卸载就可以重用。多个映射可以与一个 DMA 标签关联。虽然映射的值在某些平台上的某些条件下可能评估为 `NULL`，但永远不应假设它在所有情况下都是 `NULL`。

**`bus_dmamap_callback_t`** 客户端指定的回调，用于接收通过 `bus_dmamap_load`、`bus_dmamap_load_bio`、`bus_dmamap_load_ccb`、`bus_dmamap_load_crp` 或 `bus_dmamap_load_crp_buffer` 加载 `bus_dmamap_t` 产生的映射信息。回调格式如下：`callback_arg` 是传递给 dmamap 加载函数的回调参数。`segs` 和 `nseg` 参数描述表示映射的 `bus_dma_segment_t` 结构数组。此数组仅在回调函数范围内有效。映射的成功或失败由 `error` 参数指示。有关回调使用的更多信息，请参见各个 dmamap 加载函数的描述。

**`bus_dmamap_callback2_t`** 客户端指定的回调，用于接收通过 `bus_dmamap_load_uio` 或 `bus_dmamap_load_mbuf` 加载 `bus_dmamap_t` 产生的映射信息。Callback2 的格式如下：Callback2 的行为与 `bus_dmamap_callback_t` 相同，只是通过 `mapsize` 提供映射数据的长度。

**`bus_dmasync_op_t`** 内存同步操作说明符。总线 DMA 要求内存与其设备可见映射显式同步，以保证内存一致性。`bus_dmasync_op_t` 允许将要执行或已执行的 DMA 操作类型传达给系统，以便采取正确的一致性措施。操作表示为可以组合在一起的位域标志，但组合 PRE 标志或 POST 标志才有意义，不能两者组合。有关如何使用这些操作的更多详细信息，请参见下面的 `bus_dmamap_sync` 描述。下面指定的所有操作从主机内存角度执行，其中读取意味着数据从设备到主机内存，写入意味着数据从主机内存到设备。或者，可以从驱动程序操作的角度考虑操作，其中读取网络数据包或存储扇区对应于 `bus_dma` 中的读取操作。

**`bus_dma_lock_t`** 客户端指定的锁/互斥操作方法。当 busdma 需要代表客户端操作锁时，将从 busdma 内部调用此方法。在其当前形式中，该函数将在用 `BUS_DMA_LOCK` 延迟的 DMA 加载操作的回调之前立即调用，在之后用 `BUS_DMA_UNLOCK` 立即调用。如果加载操作不需要延迟，则不会调用它，因为加载映射的函数应持有适当的锁。此方法的格式如下：`lockfuncarg` 参数由客户端在标签创建期间指定，传递给回调的所有调用。`op` 参数指定要执行的锁操作。为方便起见，提供了两个 `lockfunc` 实现。`busdma_lock_mutex` 对通过 `lockfuncarg` 提供的睡眠互斥锁执行标准互斥操作。`dflt_lock` 如果被调用将产生系统 panic。当 `lockfunc` 作为 `NULL` 传递给 `bus_dma_tag_create` 时，它被替换到标签中，对于不应与延迟加载操作一起使用的标签很有用。

**`bus_dma_lock_op_t`** 由客户端指定的 `lockfunc` 执行的操作。

## 函数

**`BUS_DMA_ALLOCNOW`** 预分配足够资源以处理此标签上的至少一次映射加载操作。如果没有足够资源可用，返回 `ENOMEM`。这不应用于仅描述将通过 `bus_dmamem_alloc` 分配的缓冲区的标签。此外，由于与其他标签的资源共享，此标志不保证资源将专门为此标签分配或保留。应仅将其视为次要优化。

**`BUS_DMA_COHERENT`** 指示 DMA 引擎和 CPU 是缓存一致的。缓存内存可用于支持 `bus_dmamem_alloc` 创建的分配。对于 `bus_dma_tag_create`，`BUS_DMA_COHERENT` 标志目前在 arm64 上实现。

**`parent`** 从中继承限制的父标签。在其他参数中传递的限制只能进一步收紧从父标签继承的限制。设备驱动程序创建的所有标签必须从 `bus_get_dma_tag` 返回的标签继承，以遵守父桥、CPU 内存和设备之间的限制。

**`alignment`** 使用此标签创建的任何映射的对齐约束（以字节为单位）。对齐必须是 2 的幂。可以从任何地址开始 DMA 的硬件应指定 *1* 表示字节对齐。要求 DMA 传输从 4K 倍数开始的硬件应指定 *4096*。

**`boundary`** 目标 DMA 内存区域的边界约束（以字节为单位）。边界指示不能由单个 `bus_dma_segment_t` 跨越的地址集，所有地址都是 boundary 参数的倍数。boundary 必须是 2 的幂且不得小于最大段大小。`0` 表示没有边界限制。

**`lowaddr`, `highaddr`** 设备 *不能* 直接访问的总线地址空间窗口的边界。窗口包含所有大于 `lowaddr` 且小于或等于 `highaddr` 的地址。例如，不能在 4GB 以上进行 DMA 的设备应指定 `highaddr` 为 `BUS_SPACE_MAXADDR`，`lowaddr` 为 `BUS_SPACE_MAXADDR_32BIT`。类似地，只能对 16MB 以下地址执行 DMA 的设备应指定 `highaddr` 为 `BUS_SPACE_MAXADDR`，`lowaddr` 为 `BUS_SPACE_MAXADDR_24BIT`。某些实现要求设备可见地址空间的某个区域（与可用主机内存重叠）在窗口之外。此"安全内存"区域用于弹跳否则会与排除窗口冲突的请求。

**`filtfunc`** 原先是可选的过滤器函数；必须为 `NULL`。

**`filtfuncarg`** 必须为 `NULL`。

**`maxsize`** 与此标签关联的给定 DMA 映射中所有段长度之和的最大大小（以字节为单位）。

**`nsegments`** DMA 映射区域中允许的不连续点（散布/聚集段）数。

**`maxsegsz`** 与 `dmat` 关联的任何 DMA 映射区域中段的最大大小（以字节为单位）。

**`flags`** 如下：

**`lockfunc`** 可选锁操作函数（可以为 `NULL`），当 busdma 需要代表客户端操作锁时调用。如果指定为 `NULL`，使用 `dflt_lock`。

**`lockfuncarg`** 传递给 `lockfunc` 指定的函数的可选参数。

**`dmat`** 指向 `bus_dma_tag_t` 的指针，结果 DMA 标签将存储在此。

```c
	BD_PARENT()	void *
	BD_ALIGNMENT()	uintmax_t
	BD_BOUNDARY()	uintmax_t
	BD_LOWADDR()	vm_paddr_t
	BD_HIGHADDR()	vm_paddr_t
	BD_MAXSIZE()	uintmax_t
	BD_NSEGMENTS()	uintmax_t
	BD_MAXSEGSIZE()	uintmax_t
	BD_FLAGS()	uintmax_t
	BD_LOCKFUNC()	void *
	BD_LOCKFUNCARG() void *
```

**`BUS_DMA_COHERENT`** 尝试映射使用此映射加载的内存，使缓存同步操作尽可能便宜。当使用此映射加载的内存将由 CPU 和 DMA 引擎频繁访问时（如控制数据，而非接收和发送缓冲区等可流式传输数据），通常在映射上设置此标志。使用此标志不删除使用 `bus_dmamap_sync` 的要求，但可能降低执行这些操作的成本。

**`dmat`** DMA 标签。

**`flags`** 如下：

**`mapp`** 指向 `bus_dmamap_t` 的指针，结果 DMA 映射将存储在此。

**`dmat`** 用于分配 `map` 的 DMA 标签。

**`map`** 要销毁的 DMA 映射。

**`BUS_DMA_NOWAIT`** 在映射资源不足的情况下不应延迟加载，而应立即返回适当的错误。

**`BUS_DMA_NOCACHE`** 与虚拟页面之间生成的事务不可缓存。

**`dmat`** 用于分配 `map` 的 DMA 标签。

**`map`** 没有当前活动映射的 DMA 映射。

**`buf`** 指向连续（在 KVA 中）缓冲区的内核虚拟地址指针，将映射到设备可见地址空间。

**`buflen`** 缓冲区大小。

**`callback`**, **`callback_arg`** 回调函数及其参数。一旦 DMA 操作有足够的映射资源可用，就调用此函数。如果资源暂时不可用，此函数将延迟到稍后调用，但加载操作仍将立即返回给调用者。因此，调用者不应假设回调将在加载返回之前调用，代码应适当结构化以处理此情况。有关控制此行为的特定标志和错误代码，请参见下文。

**`flags`** 如下：

**0** 回调已被调用并完成。映射的状态已传递给回调。

**`EINPROGRESS`** 由于缺乏资源，映射已被延迟。资源可用时将调用回调。回调按 FIFO 顺序服务。注意，同一标签的后续加载操作如果不需要额外资源仍将成功。这可能导致请求的乱序处理。如果调用者要求保留请求顺序，则调用者需要阻止后续请求，直到待处理请求的回调被调用。

**`ENOMEM`** 加载请求由于资源不足而失败，且调用者特别使用了 `BUS_DMA_NOWAIT` 标志。

**`EINVAL`** 加载请求无效。回调已被调用并提供了相同的错误。此错误值可能表示 `dmat`、`map`、`buf` 或 `callback` 无效，或 `buflen` 大于用于创建 dma 标签 `dmat` 的 `maxsize` 参数。

**0** 映射成功，`dm_segs` 回调参数包含描述映射的 `bus_dma_segment_t` 元素数组。此数组仅在回调函数范围内有效。

**`EFBIG`** 即使请求的分配大小小于 maxsize，也无法在标签中提供的段约束内实现映射。

**`CAM_DATA_VADDR`** 数据是单个 KVA 缓冲区。

**`CAM_DATA_PADDR`** 数据是单个总线地址范围。

**`CAM_DATA_SG`** 数据是 KVA 缓冲区的散布/聚集列表。

**`CAM_DATA_SG_PADDR`** 数据是总线地址范围的散布/聚集列表。

**`CAM_DATA_BIO`** 数据包含在附加到 CCB 的 `struct bio` 中。

- XPT_ATA_IO
- XPT_CONT_TARGET_IO
- XPT_SCSI_IO

**`dmat`** 用于分配 `map` 的 DMA 标签。

**`map`** 要卸载的 DMA 映射。

**`dmat`** 用于分配 `map` 的 DMA 标签。

**`map`** 要同步的 DMA 映射。

**`op`** 要执行的同步操作类型。有关 `op` 可接受值的描述，请参见 `bus_dmasync_op_t` 的定义。

**`BUS_DMA_WAITOK`** 例程可以安全地等待（睡眠）资源。

**`BUS_DMA_NOWAIT`** 例程不允许等待资源。如果资源不可用，返回 `ENOMEM`。

**`BUS_DMA_COHERENT`** 尝试以一致方式映射此内存。有关此标志的描述，请参见上面的 `bus_dmamap_create`。对于 `bus_dmamem_alloc`，`BUS_DMA_COHERENT` 标志目前在 arm 和 arm64 上实现。

**`BUS_DMA_ZERO`** 使分配的内存设置为全零。

**`BUS_DMA_NOCACHE`** 分配的内存不会在处理器缓存中缓存。所有内存访问都出现在总线上并执行而不重新排序。对于 `bus_dmamem_alloc`，`BUS_DMA_NOCACHE` 标志目前在 amd64 和 i386 上实现，结果是为分配的虚拟地址范围设置强不可缓存 PAT。

**`dmat`** 描述 DMA 映射约束的 DMA 标签。

**`vaddr`** 指向指针的指针，将保存分配区域的返回 KVA 映射。

**`flags`** 标志定义如下：

**`mapp`** 指向 `bus_dmamap_t` 的指针，结果 DMA 映射将存储在此。

**`dmat`** DMA 标签。

**`vaddr`** 内存的内核虚拟地址。

**`map`** 要失效的 DMA 映射。

`bus_dma_tag_create(parent, alignment, boundary, lowaddr, highaddr, *filtfunc, *filtfuncarg, maxsize, nsegments, maxsegsz, flags, lockfunc, lockfuncarg, *dmat)` 分配 DMA 标签，并根据提供的参数初始化它：如果没有足够内存用于标签创建或分配映射资源，返回 `ENOMEM`。如果 `filtfunc` 或 `filtarg` 参数不为 `NULL`，返回 `EINVAL`。

`bus_dma_tag_destroy(dmat)` 释放由 `bus_dma_tag_create` 创建的 DMA 标签 `dmat`。如果任何 DMA 映射仍与 `dmat` 关联，返回 `EBUSY`，成功返回 `0`。

`bus_dma_template_init(*template, parent)` 初始化 `bus_dma_template_t` 结构。如果 `parent` 参数非 NULL，此父标签与模板关联，并将编译到稍后创建的 dma 标签中。父标签的值不会复制到模板中。在 `bus_dma_tag_template` 中创建标签期间，父标签中比所提供模板中更具限制性的任何参数将覆盖新标签中的内容。

`bus_dma_template_tag(*template, *dmat)` 将模板解包为标签，并通过 `dmat` 返回标签。所有返回值与 `bus_dma_tag_create` 相同。模板不会被此函数修改，可以在返回后重用和/或释放。

`bus_dma_template_clone(*template, dmat)` 将现有标签的字段复制到模板。模板不需要先初始化。其所有字段将被标签中包含的值覆盖。与 `bus_dma_template_tag` 配对使用时，此函数对于创建标签的副本很有用。

`bus_dma_template_fill(*template, params[], count)` 用 `params` 数组中的键控值填充模板的选定字段。这不打算直接调用，请使用 `BUS_DMA_TEMPLATE_FILL`。

`BUS_DMA_TEMPLATE_FILL(*template, param, ...)` 用可变数量的键值参数填充模板的选定字段。下面列出的宏接受指定类型的参数，并将其封装为可直接用作参数参数的键值结构。可以一次提供多个参数。

`bus_dmamap_create(dmat, flags, *mapp)` 分配并初始化 DMA 映射。参数如下：如果没有足够内存用于创建映射或分配映射资源，返回 `ENOMEM`。

`bus_dmamap_destroy(dmat, map)` 释放与给定 DMA 映射关联的所有资源。参数如下：如果 `map` 仍有活动映射，返回 `EBUSY`。

`bus_dmamap_load(dmat, map, buf, buflen, *callback, callback_arg, flags)` 在设备可见地址空间中创建 `buf` 的 `buflen` 字节的映射，与 DMA 映射 `map` 关联。此调用始终立即返回，不会因任何原因阻塞。参数如下：给调用者的返回值如下：调用回调时，会呈现指示映射处置的错误值。Error 可能是以下之一：

`bus_dmamap_load_bio(dmat, map, bio, callback, callback_arg, flags)` 这是 `bus_dmamap_load` 的变体，映射 `bio` 指向的缓冲区以进行 DMA 传输。`bio` 可以指向映射或未映射的缓冲区。

`bus_dmamap_load_ccb(dmat, map, ccb, callback, callback_arg, flags)` 这是 `bus_dmamap_load` 的变体，映射 `ccb` 指向的数据以进行 DMA 传输。`ccb` 的数据可以是以下任何类型：`bus_dmamap_load_ccb` 支持以下 CCB XPT 功能代码：

`bus_dmamap_load_crp(dmat, map, crp, callback, callback_arg, flags)` 这是 `bus_dmamap_load` 的变体，映射 `crp` 指向的输入缓冲区以进行 DMA 传输。隐含 `BUS_DMA_NOWAIT` 标志，因此不会发生回调延迟。

`bus_dmamap_load_crp_buffer(dmat, map, cb, callback, callback_arg, flags)` 这是 `bus_dmamap_load` 的变体，映射 `cb` 指向的加密数据缓冲区以进行 DMA 传输。隐含 `BUS_DMA_NOWAIT` 标志，因此不会发生回调延迟。

`bus_dmamap_load_mbuf(dmat, map, mbuf, callback2, callback_arg, flags)` 这是 `bus_dmamap_load` 的变体，映射 mbuf 链以进行 DMA 传输。`bus_size_t` 参数也传递给回调例程，包含 mbuf 链的数据包头长度。隐含 `BUS_DMA_NOWAIT` 标志，因此不会发生回调延迟。假设 mbuf 链在内核虚拟地址空间中。除了 `bus_dmamap_load` 列出的错误值外，如果 mbuf 链的大小超过 DMA 标签的最大限制，返回 `EINVAL`。

`bus_dmamap_load_mbuf_sg(dmat, map, mbuf, segs, nsegs, flags)` 这与 `bus_dmamap_load_mbuf` 类似，不同之处在于它立即返回而不调用回调函数。它是为提高效率而提供的。散布/聚集段数组 `segs` 由调用者提供并由函数直接填充。`nsegs` 参数返回填充的段数。返回与 `bus_dmamap_load_mbuf` 相同的错误。

`bus_dmamap_load_uio(dmat, map, uio, callback2, callback_arg, flags)` 这是 `bus_dmamap_load` 的变体，映射 `uio` 指向的缓冲区以进行 DMA 传输。`bus_size_t` 参数也传递给回调例程，包含 `uio` 的大小，即 `uio->uio_resid`。隐含 `BUS_DMA_NOWAIT` 标志，因此不会发生回调延迟。返回与 `bus_dmamap_load` 相同的错误。如果 `uio->uio_segflg` 为 `UIO_USERSPACE`，则假设缓冲区 `uio` 在 `uio->uio_td->td_proc` 的地址空间中。用户空间内存必须在尝试映射加载操作之前在内存中并锁定。可以使用 [vslock(9)](vslock.9.md) 锁定页面。

`bus_dmamap_unload(dmat, map)` 卸载 DMA 映射。参数如下：`bus_dmamap_unload` 不会执行 DMA 缓冲区的任何隐式同步。这必须在卸载映射之前通过调用 `bus_dmamap_sync` 显式完成。

`bus_dmamap_sync(dmat, map, op)` 执行设备可见映射与该映射引用的 CPU 可见内存的同步。参数如下：`bus_dmamap_sync` 函数是用于确保 CPU 和设备对共享内存的直接内存访问（DMA）一致的方法。例如，CPU 可用于设置要提供给设备的缓冲区内容。为确保数据通过设备的内存映射可见，必须在 CPU 更新缓冲区之后、设备访问启动之前加载缓冲区并执行 `BUS_DMASYNC_PREWRITE` 的 DMA 同步操作。如果 CPU 稍后再次修改此缓冲区，必须在额外设备访问之前执行另一次 `BUS_DMASYNC_PREWRITE` 同步操作。相反，假设设备更新要由 CPU 读取的内存。在这种情况下，必须加载缓冲区，并在设备访问启动之前执行 `BUS_DMASYNC_PREREAD` 的 DMA 同步操作。CPU 只有在 DMA 操作完成并执行 `BUS_DMASYNC_POSTREAD` 同步操作后才能看到此内存更新的结果。如果读取和写入操作之前和之后没有适当的同步操作，行为是未定义的。

`bus_dmamem_alloc(dmat, **vaddr, flags, *mapp)` 分配在 `vaddr` 返回的地址处映射到 KVA 的内存，并永久加载到通过 `mapp` 返回的新创建的 `bus_dmamap_t` 中。参数如下：要分配的内存大小是 `dmat` 调用 `bus_dma_tag_create` 时指定的 `maxsize`。`bus_dmamem_alloc` 的当前实现将所有请求分配为单个段。需要初始加载操作以获取分配内存的总线地址，在释放内存之前需要卸载操作，如下面的 `bus_dmamem_free` 所述。映射由此函数自动处理，不应显式分配或销毁。虽然返回映射引用的内存的每次访问不需要显式加载，但 `bus_dmamap_sync` 部分中描述的同步要求仍然适用，应用于在没有一致总线的架构上实现可移植性。如果没有足够内存完成操作，返回 `ENOMEM`。

`bus_dmamem_free(dmat, *vaddr, map)` 释放先前由 `bus_dmamem_alloc` 分配的内存。任何映射都将失效。参数如下：

## 返回值

如果无效参数传递给上述任何函数，行为是未定义的。如果无法为给定事务分配足够资源，返回 `ENOMEM`。所有非 `void` 类型的例程成功时返回 0，失败时返回错误代码，如上所述。

如果提供有效参数，所有 `void` 例程都将成功。

## 锁定

`bus_dma` 使用两种锁定协议。第一种是私有全局锁，用于在使用弹跳缓冲池的架构上同步对弹跳缓冲池的访问。此锁严格是叶锁，仅在 `bus_dma` 内部使用，不暴露给 API 的客户端。

第二种协议涉及保护存储在标签中的各种资源。由于几乎所有 `bus_dma` 操作都是通过创建标签的驱动程序的请求完成的，保护标签资源最有效的方法是通过驱动程序使用的锁。在 `bus_dma` 自行行动而不由驱动程序调用的情况下，标签中指定的锁原语会自动获取和释放。例如，当 `bus_dmamap_load` 回调函数从延迟上下文而非驱动程序上下文调用时。这意味着某些 `bus_dma` 函数必须始终在持有标签中指定的相同锁的情况下调用。这些函数包括：

- `bus_dmamap_load`
- `bus_dmamap_load_bio`
- `bus_dmamap_load_ccb`
- `bus_dmamap_load_mbuf`
- `bus_dmamap_load_mbuf_sg`
- `bus_dmamap_load_uio`
- `bus_dmamap_unload`
- `bus_dmamap_sync`

此规则有一个例外。在驱动程序启动期间不持有任何锁调用其中一些函数是常见做法。只要在此操作期间保证不同线程不会并发使用标签，不持有这些函数的锁是安全的。

某些 `bus_dma` 操作不应在持有驱动程序锁时调用，因为它们已受内部锁保护，或由于内存或资源分配可能睡眠。以下函数不得在持有任何不可睡眠锁时调用：

- `bus_dma_tag_create`
- `bus_dmamap_create`
- `bus_dmamem_alloc`

所有其他函数没有锁定协议，因此可以在持有或不持有任何系统或驱动程序锁的情况下调用。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md), [rman(9)](rman.9.md), [vslock(9)](vslock.9.md)

> Jason R. Thorpe, "A Machine-Independent DMA Framework for NetBSD", *Proceedings of the Summer 1998 USENIX Technical Conference*, June 1998.

## 历史

`bus_dma` 接口首次出现于 NetBSD 1.3。

`bus_dma` API 从 NetBSD 采纳，用于 CAM SCSI 子系统。对原始 API 的修改旨在删除每个 `bus_dmamap_t` 中存储的 `bus_dma_segment_t` 数组的需要，同时允许调用者在稀缺资源上排队。

## 作者

`bus_dma` 接口由 NASA Ames 研究中心数值航空航天模拟设施的 Jason R. Thorpe 设计和实现。Chris Demetriou、Charles Hannum、Ross Harvey、Matthew Jacob、Jonathan Stone 和 Matt Thomas 为 `bus_dma` 设计提供了额外意见。

FreeBSD 中的 `bus_dma` 接口得益于 Justin T. Gibbs、Peter Wemm、Doug Rabson、Matthew N. Dodd、Sam Leffler、Maxime Henrion、Jake Burkholder、Takahashi Yoshihiro、Scott Long 等许多人的贡献。

本手册页由 Hiten M. Pandya 和 Justin T. Gibbs 编写。
