# ioat(4)

`I/OAT` — Intel I/O 加速技术

## 名称

`I/OAT`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device ioat

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ioat_load="YES"
```

在 loader.conf(5) 中：

`hw.ioat.force_legacy_interrupts=0`

在 loader.conf(5) 和 sysctl.conf(5) 中：

`hw.ioat.enable_ioat_test=0 hw.ioat.debug_level=0`（仅关键错误；最大为 3）

`typedef void (*bus_dmaengine_callback_t)(void *arg, int error)`

`bus_dmaengine_t ioat_get_dmaengine(uint32_t channel_index)`

`void ioat_put_dmaengine(bus_dmaengine_t dmaengine)`

`int ioat_get_hwversion(bus_dmaengine_t dmaengine)`

`size_t ioat_get_max_io_size(bus_dmaengine_t dmaengine)`

`int ioat_set_interrupt_coalesce(bus_dmaengine_t dmaengine, uint16_t delay)`

`uint16_t ioat_get_max_coalesce_period(bus_dmaengine_t dmaengine)`

`void ioat_acquire(bus_dmaengine_t dmaengine)`

`int ioat_acquire_reserve(bus_dmaengine_t dmaengine, uint32_t n, int mflags)`

`void ioat_release(bus_dmaengine_t dmaengine)`

`struct bus_dmadesc * ioat_copy(bus_dmaengine_t dmaengine, bus_addr_t dst, bus_addr_t src, bus_size_t len, bus_dmaengine_callback_t callback_fn, void *callback_arg, uint32_t flags)`

`struct bus_dmadesc * ioat_copy_8k_aligned(bus_dmaengine_t dmaengine, bus_addr_t dst1, bus_addr_t dst2, bus_addr_t src1, bus_addr_t src2, bus_dmaengine_callback_t callback_fn, void *callback_arg, uint32_t flags)`

`struct bus_dmadesc * ioat_copy_crc(bus_dmaengine_t dmaengine, bus_addr_t dst, bus_addr_t src, bus_size_t len, uint32_t *initialseed, bus_addr_t crcptr, bus_dmaengine_callback_t callback_fn, void *callback_arg, uint32_t flags)`

`struct bus_dmadesc * ioat_crc(bus_dmaengine_t dmaengine, bus_addr_t src, bus_size_t len, uint32_t *initialseed, bus_addr_t crcptr, bus_dmaengine_callback_t callback_fn, void *callback_arg, uint32_t flags)`

`struct bus_dmadesc * ioat_blockfill(bus_dmaengine_t dmaengine, bus_addr_t dst, uint64_t fillpattern, bus_size_t len, bus_dmaengine_callback_t callback_fn, void *callback_arg, uint32_t flags)`

`struct bus_dmadesc * ioat_null(bus_dmaengine_t dmaengine, bus_dmaengine_callback_t callback_fn, void *callback_arg, uint32_t flags)`

## 描述

`I/OAT` 驱动为某些 Intel 服务器平台上的多种 DMA 引擎提供内核 API。

每个 CPU 封装有多个 DMA 通道（通常为 4 或 8 个）。每个通道可独立使用。在单个通道上的操作按顺序进行。

块填充操作可用于将 64 位模式写入内存。

复制操作可用于将内存复制工作卸载到 DMA 引擎。

空操作什么都不做，但可用于测试中断和回调机制。

所有操作可选择使用 `DMA_INT_EN` 标志在完成时触发中断。例如，用户可向同一通道提交多个操作，并仅为最后一个操作启用中断和回调。

硬件可在给定通道上延迟并合并中断，持续时间可配置（以微秒为单位）。这可能有助于减少每个描述符的处理和中断开销，特别是对于由许多小操作组成的工作流。软件可通过 `ioat_set_interrupt_coalesce` API 按通道控制此行为。`ioat_get_max_coalesce_period` API 可用于确定硬件支持的最大合并周期（以微秒为单位）。当前平台支持高达 16.383 毫秒的合并周期。最佳配置因工作流和所需操作延迟而异。

所有操作都可在非阻塞上下文中使用 `DMA_NO_WAIT` 标志安全使用。（当然，分配可能失败，使用 `DMA_NO_WAIT` 请求的操作可能返回 NULL。）

依赖于先前操作结果的操作应使用 `DMA_FENCE`。例如，当两个相关的 DMA 操作排队时可能出现这种情况。首先 DMA 复制到一个位置（A），紧接着从 A 复制到 B。在这种情况下，某些类别的 I/OAT 硬件可能在第一个操作写入 A 之前就为第二个操作预取 A。为避免在依赖操作序列中读取到陈旧值，请使用 `DMA_FENCE`。

所有操作以及 `ioat_get_dmaengine` 在特殊情况下都可能返回 NULL。例如，`I/OAT` 驱动正在被卸载、管理员引发了硬件复位，或使用错误导致需要恢复的硬件错误状态。

在 `bus_dmaengine_callback_t` 上下文中尝试提交新的 DMA 操作是无效的。

CRC 操作有三种不同模式。默认模式为累加。通过跨多个描述符累加，用户可对多块内存收集 CRC，并仅写入一次结果。

`DMA_CRC_STORE` 标志使操作发出 CRC32C 结果。如果设置了 `DMA_CRC_INLINE`，结果将内联写入到目标数据之后（或在 `ioat_crc` 模式下为源数据之后）。如果未设置 `DMA_CRC_INLINE`，结果将写入到提供的 `crcptr`。

类似地，`DMA_CRC_TEST` 标志使操作将 CRC32C 结果与现有校验和进行比较。如果设置了 `DMA_CRC_INLINE`，结果将与源数据末尾的内联四字节进行比较。如果未设置，结果将与 `crcptr` 所指向的值进行比较。

`ioat_copy_crc` 在复制数据时计算 CRC32C。`ioat_crc` 仅计算某些数据的 CRC32C。如果任一例程的 `initialseed` 参数非 NULL，则 CRC32C 引擎将使用其指向的值进行初始化。

## 用法

典型用户将使用 `ioat_get_dmaengine` 查找给定通道的 DMA 引擎对象。当用户想要卸载复制时，他们将首先 `ioat_acquire` 该 `bus_dmaengine_t` 对象以获得对该通道上排队操作的独占访问。可选地，用户可改用 `ioat_acquire_reserve` 预留空间。如果 `ioat_acquire_reserve` 成功，则保证内部环形缓冲区中有空间容纳 `N` 个新操作。

然后，他们将使用 `ioat_blockfill`、`ioat_copy`、`ioat_copy_8k_aligned`、`ioat_copy_crc`、`ioat_crc` 或 `ioat_null` 提交一个或多个操作。在排队一个或多个独立 DMA 操作后，他们将 `ioat_release` 该 `bus_dmaengine_t` 以放弃对该通道的独占访问。当操作完成时，他们为 `callback_fn` 参数提供的例程将连同提供的 `callback_arg` 一起被调用。当用户完成使用 `bus_dmaengine_t` 后，应调用 `ioat_put_dmaengine`。

用户**不得**在 `ioat_acquire` 和 `ioat_release` 之间阻塞。用户**不应**长时间持有 `bus_dmaengine_t` 引用，以启用故障恢复和内核模块卸载。

有关用法示例，请参见 `src/sys/dev/ioat/ioat_test.c`。

## 文件

**`/dev/ioat_test`** ioatcontrol(8) 的测试设备

## 参见

ioatcontrol(8)

## 历史

`I/OAT` 驱动首次出现于 FreeBSD 11.0。

## 作者

`I/OAT` 驱动由 Jim Harris <jimharris@FreeBSD.org>、Carl Delsey <carl.r.delsey@intel.com> 和 Conrad Meyer <cem@FreeBSD.org> 开发。本手册页由 Conrad Meyer <cem@FreeBSD.org> 编写。

## 注意事项

复制操作以总线地址作为参数，而非虚拟地址。

单个复制操作的缓冲区必须物理连续。

不支持超过最大传输大小（1MB，但可能因硬件而异）的复制。未来版本可能通过将传输拆分为较小尺寸来支持此功能。

## 缺陷

`I/OAT` 驱动目前仅支持块填充、复制和空操作。该驱动尚不支持某些 I/OAT 设备支持的高级 DMA 模式，例如 XOR。
