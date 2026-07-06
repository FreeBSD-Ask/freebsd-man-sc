# bus_space.9

`bus_space` — 总线空间操作函数

## 名称

`bus_space`, `bus_space_barrier`, `bus_space_copy_region_1`, `bus_space_copy_region_2`, `bus_space_copy_region_4`, `bus_space_copy_region_8`, `bus_space_copy_region_stream_1`, `bus_space_copy_region_stream_2`, `bus_space_copy_region_stream_4`, `bus_space_copy_region_stream_8`, `bus_space_free`, `bus_space_map`, `bus_space_peek_1`, `bus_space_peek_2`, `bus_space_peek_4`, `bus_space_peek_8`, `bus_space_poke_1`, `bus_space_poke_2`, `bus_space_poke_4`, `bus_space_poke_8`, `bus_space_read_1`, `bus_space_read_2`, `bus_space_read_4`, `bus_space_read_8`, `bus_space_read_multi_1`, `bus_space_read_multi_2`, `bus_space_read_multi_4`, `bus_space_read_multi_8`, `bus_space_read_multi_stream_1`, `bus_space_read_multi_stream_2`, `bus_space_read_multi_stream_4`, `bus_space_read_multi_stream_8`, `bus_space_read_region_1`, `bus_space_read_region_2`, `bus_space_read_region_4`, `bus_space_read_region_8`, `bus_space_read_region_stream_1`, `bus_space_read_region_stream_2`, `bus_space_read_region_stream_4`, `bus_space_read_region_stream_8`, `bus_space_read_stream_1`, `bus_space_read_stream_2`, `bus_space_read_stream_4`, `bus_space_read_stream_8`, `bus_space_set_multi_1`, `bus_space_set_multi_2`, `bus_space_set_multi_4`, `bus_space_set_multi_8`, `bus_space_set_multi_stream_1`, `bus_space_set_multi_stream_2`, `bus_space_set_multi_stream_4`, `bus_space_set_multi_stream_8`, `bus_space_set_region_1`, `bus_space_set_region_2`, `bus_space_set_region_4`, `bus_space_set_region_8`, `bus_space_set_region_stream_1`, `bus_space_set_region_stream_2`, `bus_space_set_region_stream_4`, `bus_space_set_region_stream_8`, `bus_space_subregion`, `bus_space_unmap`, `bus_space_write_1`, `bus_space_write_2`, `bus_space_write_4`, `bus_space_write_8`, `bus_space_write_multi_1`, `bus_space_write_multi_2`, `bus_space_write_multi_4`, `bus_space_write_multi_8`, `bus_space_write_multi_stream_1`, `bus_space_write_multi_stream_2`, `bus_space_write_multi_stream_4`, `bus_space_write_multi_stream_8`, `bus_space_write_region_1`, `bus_space_write_region_2`, `bus_space_write_region_4`, `bus_space_write_region_8`, `bus_space_write_region_stream_1`, `bus_space_write_region_stream_2`, `bus_space_write_region_stream_4`, `bus_space_write_region_stream_8`, `bus_space_write_stream_1`, `bus_space_write_stream_2`, `bus_space_write_stream_4`, `bus_space_write_stream_8`

## 概要

```c
#include <machine/bus.h>
```

```c
int
bus_space_map(bus_space_tag_t space, bus_addr_t address,
    bus_size_t size, int flags, bus_space_handle_t *handlep)

void
bus_space_unmap(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t size)

int
bus_space_subregion(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, bus_size_t size, bus_space_handle_t *nhandlep)

int
bus_space_alloc(bus_space_tag_t space, bus_addr_t reg_start,
    bus_addr_t reg_end, bus_size_t size, bus_size_t alignment,
    bus_size_t boundary, int flags, bus_addr_t *addrp,
    bus_space_handle_t *handlep)

void
bus_space_free(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t size)
```

```c
int
bus_space_peek_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)

int
bus_space_peek_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)

int
bus_space_peek_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)

int
bus_space_peek_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)

int
bus_space_poke_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)

int
bus_space_poke_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)

int
bus_space_poke_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)

int
bus_space_poke_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap)
```

```c
uint8_t
bus_space_read_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

uint16_t
bus_space_read_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

uint32_t
bus_space_read_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

uint64_t
bus_space_read_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

uint8_t
bus_space_read_stream_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

uint16_t
bus_space_read_stream_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

uint32_t
bus_space_read_stream_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

uint64_t
bus_space_read_stream_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset)

void
bus_space_write_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t value)

void
bus_space_write_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t value)

void
bus_space_write_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t value)

void
bus_space_write_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t value)

void
bus_space_write_stream_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t value)

void
bus_space_write_stream_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t value)

void
bus_space_write_stream_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t value)

void
bus_space_write_stream_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t value)
```

```c
void
bus_space_barrier(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, bus_size_t length, int flags)
```

```c
void
bus_space_read_region_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap, bus_size_t count)

void
bus_space_read_region_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t *datap, bus_size_t count)

void
bus_space_read_region_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t *datap, bus_size_t count)

void
bus_space_read_region_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t *datap, bus_size_t count)

void
bus_space_read_region_stream_1(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint8_t *datap,
    bus_size_t count)

void
bus_space_read_region_stream_2(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint16_t *datap,
    bus_size_t count)

void
bus_space_read_region_stream_4(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint32_t *datap,
    bus_size_t count)

void
bus_space_read_region_stream_8(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint64_t *datap,
    bus_size_t count)

void
bus_space_write_region_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap, bus_size_t count)

void
bus_space_write_region_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t *datap, bus_size_t count)

void
bus_space_write_region_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t *datap, bus_size_t count)

void
bus_space_write_region_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t *datap, bus_size_t count)

void
bus_space_write_region_stream_1(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint8_t *datap,
    bus_size_t count)

void
bus_space_write_region_stream_2(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint16_t *datap,
    bus_size_t count)

void
bus_space_write_region_stream_4(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint32_t *datap,
    bus_size_t count)

void
bus_space_write_region_stream_8(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint64_t *datap,
    bus_size_t count)
```

```c
void
bus_space_copy_region_1(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)

void
bus_space_copy_region_2(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)

void
bus_space_copy_region_4(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)

void
bus_space_copy_region_8(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)

void
bus_space_copy_region_stream_1(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)

void
bus_space_copy_region_stream_2(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)

void
bus_space_copy_region_stream_4(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)

void
bus_space_copy_region_stream_8(bus_space_tag_t space,
    bus_space_handle_t srchandle, bus_size_t srcoffset,
    bus_space_handle_t dsthandle, bus_size_t dstoffset,
    bus_size_t count)
```

```c
void
bus_space_set_region_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t value, bus_size_t count)

void
bus_space_set_region_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t value, bus_size_t count)

void
bus_space_set_region_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t value, bus_size_t count)

void
bus_space_set_region_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t value, bus_size_t count)

void
bus_space_set_region_stream_1(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint8_t value,
    bus_size_t count)

void
bus_space_set_region_stream_2(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint16_t value,
    bus_size_t count)

void
bus_space_set_region_stream_4(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint32_t value,
    bus_size_t count)

void
bus_space_set_region_stream_8(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint64_t value,
    bus_size_t count)
```

```c
void
bus_space_read_multi_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap, bus_size_t count)

void
bus_space_read_multi_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t *datap, bus_size_t count)

void
bus_space_read_multi_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t *datap, bus_size_t count)

void
bus_space_read_multi_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t *datap, bus_size_t count)

void
bus_space_read_multi_stream_1(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint8_t *datap,
    bus_size_t count)

void
bus_space_read_multi_stream_2(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint16_t *datap,
    bus_size_t count)

void
bus_space_read_multi_stream_4(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint32_t *datap,
    bus_size_t count)

void
bus_space_read_multi_stream_8(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint64_t *datap,
    bus_size_t count)

void
bus_space_write_multi_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t *datap, bus_size_t count)

void
bus_space_write_multi_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t *datap, bus_size_t count)

void
bus_space_write_multi_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t *datap, bus_size_t count)

void
bus_space_write_multi_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t *datap, bus_size_t count)

void
bus_space_write_multi_stream_1(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint8_t *datap,
    bus_size_t count)

void
bus_space_write_multi_stream_2(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint16_t *datap,
    bus_size_t count)

void
bus_space_write_multi_stream_4(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint32_t *datap,
    bus_size_t count)

void
bus_space_write_multi_stream_8(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint64_t *datap,
    bus_size_t count)
```

```c
void
bus_space_set_multi_1(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint8_t value, bus_size_t count)

void
bus_space_set_multi_2(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint16_t value, bus_size_t count)

void
bus_space_set_multi_4(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint32_t value, bus_size_t count)

void
bus_space_set_multi_8(bus_space_tag_t space, bus_space_handle_t handle,
    bus_size_t offset, uint64_t value, bus_size_t count)

void
bus_space_set_multi_stream_1(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint8_t value,
    bus_size_t count)

void
bus_space_set_multi_stream_2(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint16_t value,
    bus_size_t count)

void
bus_space_set_multi_stream_4(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint32_t value,
    bus_size_t count)

void
bus_space_set_multi_stream_8(bus_space_tag_t space,
    bus_space_handle_t handle, bus_size_t offset, uint64_t value,
    bus_size_t count)
```

## 描述

`bus_space` 函数族为设备驱动程序提供了机器无关的总线内存和寄存器区域访问能力。本文档中描述的所有函数和类型都可以通过包含以下头文件来使用：

```c
#include <machine/bus.h>
```

许多常见设备可用于多种架构，但由于架构约束，每种架构上的访问方式各不相同。例如，在某个系统的 I/O 空间中映射的设备，在另一个系统上可能映射在内存空间中。在第三个系统上，架构限制可能会改变寄存器的访问方式（例如创建非线性的寄存器空间）。在某些情况下，单个驱动程序可能需要在单个系统或架构中以多种方式访问同一类型的设备。`bus_space` 函数族的目标是允许单个驱动程序源文件在不同系统架构上操作一组设备，并允许单个驱动程序目标文件在单个架构上的多种总线类型上操作一组设备。

并非所有总线都需要实现本文档中描述的全部函数，但如果总线在逻辑上支持某些操作，则鼓励实现这些函数。未实现的函数应尽可能在编译时引发错误。

本文档中描述的所有接口定义均以函数原型形式展示，并按其必须为函数的要求进行讨论。鼓励实现这些接口的原型化（类型检查）版本，但如有需要，也可将其实现为宏。机器相关的类型、变量和函数应在以下头文件中明确标注：

```c
#include <machine/bus.h>
```

以避免与机器无关的类型和函数混淆，并尽可能使用能清楚表明机器依赖性的名称。

## 概念和准则

总线空间由总线空间标签描述，标签只能由机器相关代码创建。一台给定的机器可能具有多种不同类型的总线空间（例如内存空间和 I/O 空间），因此可能提供多个不同的总线空间标签。机器上的单个总线或设备可能使用多个总线空间标签。例如，ISA 设备会被赋予一个 ISA 内存空间标签和一个 ISA I/O 空间标签。由于存在多种不同的主机总线接口芯片组，架构可能具有多个表示同一类型空间的标签。

总线空间中的范围由总线地址和总线大小描述。总线地址描述总线空间中范围的起始位置。总线大小描述范围的字节大小。非字节可寻址的总线可能要求使用具有适当对齐地址和正确取整大小的总线空间范围。

通过使用总线空间句柄可以方便地访问总线空间的区域，句柄通常通过映射总线空间的特定范围来创建。句柄也可通过分配并映射总线空间范围来创建，其实际位置由实现在调用者指定的边界内选择。

所有总线空间访问函数都需要一个总线空间标签参数、至少一个句柄参数和至少一个偏移量参数（总线大小）。总线空间标签指定空间，每个句柄指定空间中的一个区域，每个偏移量指定要访问的实际位置在区域内的偏移量。偏移量以字节为单位给出，但总线可能施加对齐约束。用于相对于给定句柄访问数据的偏移量必须确保所有被访问的数据都位于该句柄所描述的映射区域内。试图访问该区域之外的数据是错误的。

由于某些架构的内存系统使用缓冲来提高内存和设备访问性能，提供了一种可在总线空间读和写流中创建“屏障”的机制。屏障有三种类型：读、写和读/写。在读屏障之前启动的所有到该区域的读操作必须在该读屏障之后的任何读操作启动之前完成。（写屏障也有类似的要求。）读/写屏障强制屏障之前启动的所有读和写操作在屏障之后的任何读或写操作启动之前完成。编写正确的驱动程序应包含所有适当的屏障，并仅假设屏障操作所施加的读/写顺序。

试图使用 `bus_space` 函数编写可移植驱动程序的人应尽量减少对系统能力的假设。特别是，应预期系统要求被访问的总线空间地址自然对齐（即句柄的基地址加上偏移量是访问大小的倍数），并且系统对指针进行对齐检查（即指向被读写对象的指针必须指向正确对齐的数据）。

下文对 `bus_space` 函数的描述均假设它们以正确的参数调用。如果以无效参数或超出范围的参数调用（例如试图在创建给定句柄所映射区域之外访问数据），将导致未定义行为。在这种情况下，可能导致系统有意（通过 panic）或无意（通过引发致命陷阱或其他方式）停止，也可能导致不会立即致命的不正确操作。返回 `void` 或返回从总线空间读取数据的函数（即不明显返回错误代码的函数）不会失败。它们只有在给定无效参数时才可能失败，此时其行为未定义。接受字节计数的函数在指定的 `count` 为零时结果未定义。

## 类型

以下头文件中定义了若干类型，以便驱动程序使用 `bus_space` 函数：

```c
#include <machine/bus.h>
```

### `bus_addr_t`

`bus_addr_t` 类型用于描述总线地址。它必须是能够容纳架构可用的最大总线地址的无符号整型。该类型主要用于映射和取消映射总线空间。

### `bus_size_t`

`bus_size_t` 类型用于描述总线空间中范围的大小。它必须是能够容纳架构可用的最大总线地址范围大小的无符号整型。几乎所有 `bus_space` 函数都使用该类型，在映射区域时描述大小，在执行空间访问操作时描述区域内的偏移量。

### `bus_space_tag_t`

`bus_space_tag_t` 类型用于描述机器上的特定总线空间。其内容由机器相关，机器无关代码应将其视为不透明类型。所有 `bus_space` 函数都使用该类型来命名其操作所在的空间。

### `bus_space_handle_t`

`bus_space_handle_t` 类型用于描述总线空间范围的映射。其内容由机器相关，机器无关代码应将其视为不透明类型。该类型在执行总线空间访问操作时使用。

## 映射和取消映射总线空间

本节特定于这些函数的 NetBSD 版本，可能适用于也可能不适用于 FreeBSD 版本。

总线空间在使用前必须进行映射，不再需要时应取消映射。`bus_space_map` 和 `bus_space_unmap` 函数提供了这些功能。

某些驱动程序需要能够将已映射总线空间的子区域传递给另一个驱动程序或驱动程序内的模块。`bus_space_subregion` 函数允许创建此类子区域。

### `bus_space_map(space, address, size, flags, handlep)`

`bus_space_map` 函数映射由 `space`、`address` 和 `size` 参数命名的总线空间区域。成功时返回零，并将 `handlep` 所指向的总线空间句柄填充为可用于访问映射区域的句柄。失败时返回非零值，并将 `handlep` 所指向的总线空间句柄置于未定义状态。

`flags` 参数控制空间的映射方式。支持的标志包括：

**`BUS_SPACE_MAP_CACHEABLE`** 尝试映射空间以便系统可以缓存和/或预取访问。如果未指定此标志，实现应映射空间使其不被缓存或预取。为了向后兼容，在所有实现中此标志的值必须为 1。

**`BUS_SPACE_MAP_LINEAR`** 尝试映射空间以便其内容可通过常规内存访问方法（如指针解引用和结构体访问）线性访问。当软件希望直接访问内存设备（如帧缓冲区）时此功能很有用。如果指定了此标志但线性映射不可行，`bus_space_map` 调用应失败。如果未指定此标志，系统可以以最方便的任何方式映射空间。

**`BUS_SPACE_MAP_NONPOSTED`** 尝试使用非 posted 设备内存映射空间。这是为了支持使用 posted 设备内存映射不被支持或存在缺陷的总线和设备。此标志目前仅在 arm64 上可用。

并非所有标志组合都有意义或被所有空间支持。例如，`BUS_SPACE_MAP_CACHEABLE` 在许多系统的 I/O 端口空间上可能无意义，在某些系统上 `BUS_SPACE_MAP_LINEAR` 而无 `BUS_SPACE_MAP_CACHEABLE` 可能永远无法工作。当系统硬件或固件提供了关于空间应如何映射的提示（如 PCI 内存映射寄存器的“可预取”位）时，为获得最大兼容性应遵循这些提示。在某些系统上，请求无法满足的映射（例如系统只能提供可缓存映射时请求不可缓存映射）将导致请求失败。

某些实现可能会跟踪部分或所有总线空间的使用情况，并拒绝允许重复分配。对于没有插槽特定空间寻址概念的总线空间（如 ISA），以及与这些空间共存的空间（如与 ISA 内存和 I/O 空间共存的 PCI 内存和 I/O 空间），鼓励这样做。

映射区域可能包含总线上没有设备的区域。如果访问这些区域的空间，结果取决于总线。

### `bus_space_unmap(space, handle, size)`

`bus_space_unmap` 函数取消映射由 `bus_space_map` 映射的总线空间区域。取消映射区域时，指定的 `size` 应与映射该区域时给予 `bus_space_map` 的大小相同。

在对句柄调用 `bus_space_unmap` 之后，该句柄不再有效。（如果对句柄进行了复制，复制也不再有效。）

此函数不会失败。如果它失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，`bus_space_unmap` 不会返回。

### `bus_space_subregion(space, handle, offset, size, nhandlep)`

`bus_space_subregion` 函数是一个便利函数，用于为已映射总线空间区域的某个子区域创建新句柄。新句柄描述的子区域从 `handle` 所描述区域内的字节偏移量 `offset` 处开始，大小由 `size` 给出，且必须完全包含在原始区域内。

成功时，`bus_space_subregion` 返回零，并将 `nhandlep` 所指向的总线空间句柄填充。失败时返回非零值，并将 `nhandlep` 所指向的总线空间句柄置于未定义状态。无论哪种情况，`handle` 所描述的句柄仍然有效且未被修改。

使用完由 `bus_space_subregion` 创建的句柄后，应将其丢弃。在任何情况下都不应对该句柄使用 `bus_space_unmap`。这样做可能干扰对该空间正在进行的任何资源管理，并将导致未定义行为。当对句柄调用 `bus_space_unmap` 或 `bus_space_free` 时，该句柄的所有子区域都会变为无效。

## 分配和释放总线空间

本节特定于这些函数的 NetBSD 版本，可能适用于也可能不适用于 FreeBSD 版本。

某些设备要求或允许操作系统为设备使用分配总线空间。当设备不再需要该空间时，操作系统应将其释放以供其他设备使用。`bus_space_alloc` 和 `bus_space_free` 函数提供了这些功能。

### `bus_space_alloc(space, reg_start, reg_end, size, alignment, boundary, flags, addrp, handlep)`

`bus_space_alloc` 函数分配并映射一个大小由 `size` 给出的总线空间区域，并满足给定的约束。成功时返回零，将 `addrp` 所指向的总线地址填充为所分配区域的总线空间地址，并将 `handlep` 所指向的总线空间句柄填充为可用于访问该区域的句柄。失败时返回非零值，并将 `addrp` 所指向的总线地址和 `handlep` 所指向的总线空间句柄置于未定义状态。

分配的约束由 `reg_start`、`reg_end`、`alignment` 和 `boundary` 参数给出。所分配区域将从 `reg_start` 处或之后开始，并在 `reg_end` 处或之前结束。`alignment` 约束必须是 2 的幂，所分配区域将从该 2 的幂的偶数倍地址开始。`boundary` 约束（如果非零）确保分配区域使得“区域内首地址”/`boundary` 与“区域内末地址”/`boundary` 具有相同的值。如果无法满足约束，`bus_space_alloc` 将失败。指定一组永远无法满足的约束是错误的（例如 `size` 大于 `boundary`）。

`flags` 参数与 `bus_space_map` 中同名参数相同，应使用相同的标志值，含义也相同。

由 `bus_space_alloc` 创建的句柄应仅用 `bus_space_free` 释放。试图对它们使用 `bus_space_unmap` 会导致未定义行为。`bus_space_subregion` 函数可用于由 `bus_space_alloc` 创建的句柄。

### `bus_space_free(space, handle, size)`

`bus_space_free` 函数取消映射并释放由 `bus_space_alloc` 分配和映射的总线空间区域。取消映射区域时，指定的 `size` 应与分配该区域时给予 `bus_space_alloc` 的大小相同。

在对句柄调用 `bus_space_free` 之后，该句柄不再有效。（如果对句柄进行了复制，复制也不再有效。）

此函数不会失败。如果它失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，`bus_space_free` 不会返回。

## 读取和写入单个数据项

访问总线空间最简单的方式是读取或写入单个数据项。`bus_space_read_N` 和 `bus_space_write_N` 函数族提供了在支持这些访问大小的总线上读写 1、2、4 和 8 字节数据项的能力。

### `bus_space_read_1(space, handle, offset)`

### `bus_space_read_2(space, handle, offset)`

### `bus_space_read_4(space, handle, offset)`

### `bus_space_read_8(space, handle, offset)`

`bus_space_read_N` 函数族从 `space` 指定的总线空间中由 `handle` 指定的区域内、由 `offset` 指定的偏移量处读取 1、2、4 或 8 字节的数据项。被读取的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被读取数据项大小的倍数。在某些系统上，不遵守此要求可能导致读取到错误数据，在其他系统上可能导致系统崩溃。

`bus_space_read_N` 函数执行的读操作可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

### `bus_space_write_1(space, handle, offset, value)`

### `bus_space_write_2(space, handle, offset, value)`

### `bus_space_write_4(space, handle, offset, value)`

### `bus_space_write_8(space, handle, offset, value)`

`bus_space_write_N` 函数族向 `space` 指定的总线空间中由 `handle` 指定的区域内、由 `offset` 指定的偏移量处写入 1、2、4 或 8 字节的数据项。被写入的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被写入数据项大小的倍数。在某些系统上，不遵守此要求可能导致写入错误数据，在其他系统上可能导致系统崩溃。

`bus_space_write_N` 函数执行的写操作可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

## 探测可能无响应硬件的总线空间

`bus_space_read_N` 和 `bus_space_write_N` 函数族的一个问题是，当没有物理硬件或设备响应读或写周期时，它们无法防止可能发生的异常。在这种情况下，系统通常会由于内核态总线错误而 panic。`bus_space_peek_N` 和 `bus_space_poke_N` 函数族提供了一种优雅地处理这些异常的机制，而不会导致系统崩溃的风险。

与 `bus_space_read_N` 和 `bus_space_write_N` 一样，peek 和 poke 函数提供了在支持这些访问大小的总线上读写 1、2、4 和 8 字节数据项的能力。`bus_space_read_N` 和 `bus_space_write_N` 函数描述中指定的所有约束同样适用于 `bus_space_peek_N` 和 `bus_space_poke_N`。

此外，不需要显式调用 `bus_space_barrier` 函数，因为实现会确保在 peek 或 poke 操作开始之前所有待处理操作完成。实现还会确保 peek 或 poke 操作在返回之前完成。

返回值指示 peek 或 poke 操作的结果。返回值为零表示硬件设备在总线空间中指定偏移量处响应了操作。非零返回值表示内核在尝试 peek 或 poke 操作时拦截到了硬件异常（如总线错误）。请注意，某些总线在不存在的硬件被访问时无法产生异常。在这种情况下，这些函数将始终返回零，且 `bus_space_peek_N` 读取的数据值将是未指定的。

最后，需要注意的是，目前 `bus_space_peek_N` 和 `bus_space_poke_N` 函数不可重入，因此不应从中断服务例程中使用。此限制可能在将来的某个时候被移除。

### `bus_space_peek_1(space, handle, offset, datap)`

### `bus_space_peek_2(space, handle, offset, datap)`

### `bus_space_peek_4(space, handle, offset, datap)`

### `bus_space_peek_8(space, handle, offset, datap)`

`bus_space_peek_N` 函数族谨慎地从 `space` 指定的总线空间中由 `handle` 指定的区域内、由 `offset` 指定的偏移量处读取 1、2、4 或 8 字节的数据项。读取的数据项存储在 `datap` 所指向的位置。允许 `datap` 为 NULL，此时数据项在读取后将被丢弃。

### `bus_space_poke_1(space, handle, offset, value)`

### `bus_space_poke_2(space, handle, offset, value)`

### `bus_space_poke_4(space, handle, offset, value)`

### `bus_space_poke_8(space, handle, offset, value)`

`bus_space_poke_N` 函数族谨慎地将 `value` 指定的 1、2、4 或 8 字节数据项写入 `space` 指定的总线空间中由 `handle` 指定的区域内、由 `offset` 指定的偏移量处。

## 屏障

为了允许高性能缓冲实现避免每次操作都进行总线活动，驱动程序应在必要时显式指定读写顺序。`bus_space_barrier` 函数提供了这种能力。

### `bus_space_barrier(space, handle, offset, length, flags)`

`bus_space_barrier` 函数为 `space` 指定空间中由 `handle` 命名的区域的指定子区域（由 `offset` 和 `length` 参数描述）强制总线空间读写操作的顺序。

`flags` 参数控制要排序的操作类型。支持的标志有：

**`BUS_SPACE_BARRIER_READ`** 同步读操作。

**`BUS_SPACE_BARRIER_WRITE`** 同步写操作。

这些标志可以组合（按位或）以同时强制读和写操作的顺序。

在屏障操作之前对区域执行的所有指定类型操作，保证在屏障之后执行的任何指定类型操作之前完成。

示例：考虑一个假设的设备，它有两个单字节端口，一个只写输入端口（偏移量 0 处）和一个只读输出端口（偏移量 1 处）。设备的操作如下：数据字节被写入输入端口，并由设备放入一个栈中，通过读取输出端口读取栈顶。正确地向设备写入两个数据字节然后读回这两个字节的序列如下：

```c
/*
 * t 和 h 是映射设备空间的标签和句柄。
 */
bus_space_write_1(t, h, 0, data0);
bus_space_barrier(t, h, 0, 1, BUS_SPACE_BARRIER_WRITE);  /* 1 */
bus_space_write_1(t, h, 0, data1);
bus_space_barrier(t, h, 0, 2,
    BUS_SPACE_BARRIER_READ|BUS_SPACE_BARRIER_WRITE);     /* 2 */
ndata1 = bus_space_read_1(t, h, 1);
bus_space_barrier(t, h, 1, 1, BUS_SPACE_BARRIER_READ);   /* 3 */
ndata0 = bus_space_read_1(t, h, 1);
/* data0 == ndata0, data1 == ndata1 */
```

第一个屏障确保第一次写操作在第二次写操作发出之前完成，这样对输入端口的两次写操作按顺序执行，而不会被合并为一次写操作。这确保了数据字节正确且按顺序写入设备。

第二个屏障确保对输出端口的写操作在对输入端口的任何读操作发出之前完成，从而确保在读取数据之前所有写操作都已完成。这确保了从设备读取的第一个字节确实是最后写入的字节。

第三个屏障确保第一次读操作在第二次读操作发出之前完成，确保数据正确且按顺序读取。

上例中的屏障指定覆盖了最少数量的总线空间位置。使屏障操作覆盖设备的整个总线空间范围（即指定偏移量为零和整个区域的大小）是正确的，并且通常更容易。

## 区域操作

某些设备使用在总线空间中映射为区域的缓冲区。驱动程序常常需要在这些缓冲区与内存之间复制内容，例如复制到可传递给系统高层的 mbuf 中，或从要输出到网络的 mbuf 中复制。为了使驱动程序能尽可能高效地执行此操作，提供了 `bus_space_read_region_N` 和 `bus_space_write_region_N` 函数族。

驱动程序偶尔需要将总线空间的一个区域复制到另一个区域，或将一个区域中的所有位置设置为单个值。`bus_space_copy_region_N` 函数族和 `bus_space_set_region_N` 函数族允许驱动程序执行这些操作。

### `bus_space_read_region_1(space, handle, offset, datap, count)`

### `bus_space_read_region_2(space, handle, offset, datap, count)`

### `bus_space_read_region_4(space, handle, offset, datap, count)`

### `bus_space_read_region_8(space, handle, offset, datap, count)`

`bus_space_read_region_N` 函数族从 `space` 指定的总线空间中由 `handle` 指定的区域内、从字节偏移量 `offset` 处开始读取 `count` 个 1、2、4 或 8 字节的数据项，并将它们写入 `datap` 指定的数组。每个后续数据项从前一个数据项之后 1、2、4 或 8 字节的偏移量处读取（取决于使用的函数）。所有被读取的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被读取数据项大小的倍数，且数据数组指针应正确对齐。在某些系统上，不遵守这些要求可能导致读取到错误数据，在其他系统上可能导致系统崩溃。

`bus_space_read_region_N` 函数执行的读操作可能以任何顺序执行。它们也可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。无法在 `bus_space_read_region_N` 函数执行的单个总线空间位置读取之间插入屏障。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

### `bus_space_write_region_1(space, handle, offset, datap, count)`

### `bus_space_write_region_2(space, handle, offset, datap, count)`

### `bus_space_write_region_4(space, handle, offset, datap, count)`

### `bus_space_write_region_8(space, handle, offset, datap, count)`

`bus_space_write_region_N` 函数族从 `datap` 指定的数组读取 `count` 个 1、2、4 或 8 字节的数据项，并将它们写入 `space` 指定的总线空间中由 `handle` 指定的区域内、从字节偏移量 `offset` 处开始的位置。每个后续数据项写入前一个数据项之后 1、2、4 或 8 字节的偏移量处（取决于使用的函数）。所有被写入的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被写入数据项大小的倍数，且数据数组指针应正确对齐。在某些系统上，不遵守这些要求可能导致写入错误数据，在其他系统上可能导致系统崩溃。

`bus_space_write_region_N` 函数执行的写操作可能以任何顺序执行。它们也可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。无法在 `bus_space_write_region_N` 函数执行的单个总线空间位置写入之间插入屏障。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

### `bus_space_copy_region_1(space, srchandle, srcoffset, dsthandle, dstoffset, count)`

### `bus_space_copy_region_2(space, srchandle, srcoffset, dsthandle, dstoffset, count)`

### `bus_space_copy_region_4(space, srchandle, srcoffset, dsthandle, dstoffset, count)`

### `bus_space_copy_region_8(space, srchandle, srcoffset, dsthandle, dstoffset, count)`

`bus_space_copy_region_N` 函数族在同一总线空间中，从 `space` 指定的总线空间中由 `srchandle` 指定的区域内、从字节偏移量 `srcoffset` 处开始的区域，复制 `count` 个 1、2、4 或 8 字节的数据项到由 `dsthandle` 指定的区域内、从字节偏移量 `dstoffset` 处开始的区域。每个被读取或写入的后续数据项相对于前一个数据项偏移 1、2、4 或 8 字节（取决于使用的函数）。所有被读取和写入的位置必须位于各自句柄指定的总线空间区域内。

为了可移植性，每个句柄指定区域的起始地址加上其各自的偏移量应为被复制数据项大小的倍数。在某些系统上，不遵守此要求可能导致复制错误数据，在其他系统上可能导致系统崩溃。

`bus_space_copy_region_N` 函数执行的读和写操作可能以任何顺序执行。它们也可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。无法在 `bus_space_copy_region_N` 函数执行的单个总线空间位置的读或写之间插入屏障。

`bus_space_copy_region_N` 函数能正确处理单个总线空间区域内不同子区域之间的重叠复制。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

### `bus_space_set_region_1(space, handle, offset, value, count)`

### `bus_space_set_region_2(space, handle, offset, value, count)`

### `bus_space_set_region_4(space, handle, offset, value, count)`

### `bus_space_set_region_8(space, handle, offset, value, count)`

`bus_space_set_region_N` 函数族将给定的 `value` 写入 `space` 指定的总线空间中由 `handle` 指定的区域内、从字节偏移量 `offset` 处开始的 `count` 个 1、2、4 或 8 字节数据项。每个后续数据项相对于前一个数据项偏移 1、2、4 或 8 字节（取决于使用的函数）。所有被写入的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被写入数据项大小的倍数。在某些系统上，不遵守此要求可能导致写入错误数据，在其他系统上可能导致系统崩溃。

`bus_space_set_region_N` 函数执行的写操作可能以任何顺序执行。它们也可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。无法在 `bus_space_set_region_N` 函数执行的单个总线空间位置写入之间插入屏障。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

## 多次读写单个位置

某些设备在总线空间中实现了需要多次读取或写入以通信数据的单个位置，例如某些以太网设备的数据包缓冲区 FIFO。为了使驱动程序能尽可能高效地操作这些类型的设备，提供了 `bus_space_read_multi_N`、`bus_space_set_multi_N` 和 `bus_space_write_multi_N` 函数族。

### `bus_space_read_multi_1(space, handle, offset, datap, count)`

### `bus_space_read_multi_2(space, handle, offset, datap, count)`

### `bus_space_read_multi_4(space, handle, offset, datap, count)`

### `bus_space_read_multi_8(space, handle, offset, datap, count)`

`bus_space_read_multi_N` 函数族从 `space` 指定的总线空间中由 `handle` 指定的区域内、字节偏移量 `offset` 处读取 `count` 个 1、2、4 或 8 字节的数据项，并将它们写入 `datap` 指定的数组。每个后续数据项从总线空间中的同一位置读取。被读取的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被读取数据项大小的倍数，且数据数组指针应正确对齐。在某些系统上，不遵守这些要求可能导致读取到错误数据，在其他系统上可能导致系统崩溃。

`bus_space_read_multi_N` 函数执行的读操作可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。由于 `bus_space_read_multi_N` 函数多次读取同一总线空间位置，它们在该总线空间位置的每次连续读取之间放置一个隐式读屏障。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

### `bus_space_write_multi_1(space, handle, offset, datap, count)`

### `bus_space_write_multi_2(space, handle, offset, datap, count)`

### `bus_space_write_multi_4(space, handle, offset, datap, count)`

### `bus_space_write_multi_8(space, handle, offset, datap, count)`

`bus_space_write_multi_N` 函数族从 `datap` 指定的数组读取 `count` 个 1、2、4 或 8 字节的数据项，并将它们写入 `space` 指定的总线空间中由 `handle` 指定的区域内、字节偏移量 `offset` 处。每个后续数据项写入总线空间中的同一位置。被写入的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被写入数据项大小的倍数，且数据数组指针应正确对齐。在某些系统上，不遵守这些要求可能导致写入错误数据，在其他系统上可能导致系统崩溃。

`bus_space_write_multi_N` 函数执行的写操作可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。由于 `bus_space_write_multi_N` 函数多次写入同一总线空间位置，它们在该总线空间位置的每次连续写入之间放置一个隐式写屏障。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

### `bus_space_set_multi_1(space, handle, offset, value, count)`

### `bus_space_set_multi_2(space, handle, offset, value, count)`

### `bus_space_set_multi_4(space, handle, offset, value, count)`

### `bus_space_set_multi_8(space, handle, offset, value, count)`

`bus_space_set_multi_N` 将 `value` 写入 `space` 指定的总线空间中由 `handle` 指定的区域内、字节偏移量 `offset` 处，共写入 `count` 次。被写入的位置必须位于 `handle` 指定的总线空间区域内。

为了可移植性，`handle` 指定区域的起始地址加上偏移量应为被写入数据项大小的倍数，且数据数组指针应正确对齐。在某些系统上，不遵守这些要求可能导致写入错误数据，在其他系统上可能导致系统崩溃。

`bus_space_set_multi_N` 函数执行的写操作可能相对于其他待处理的读和写操作乱序执行，除非通过使用 `bus_space_barrier` 函数强制顺序。由于 `bus_space_set_multi_N` 函数多次写入同一总线空间位置，它们在该总线空间位置的每次连续写入之间放置一个隐式写屏障。

这些函数不会失败。如果它们失败（例如由于参数错误），则表明存在应导致 panic 的软件错误。在这种情况下，它们不会返回。

## 流函数

大多数 `bus_space` 函数隐含主机字节序和总线字节序，并为调用者处理任何转换。但在某些情况下，硬件可能映射了一个 FIFO 或其他内存区域，调用者可能希望对其进行多字、未转换的访问。对这些类型内存区域的访问应使用 `bus_space_*_stream_N` 函数。

- `bus_space_read_stream_1`
- `bus_space_read_stream_2`
- `bus_space_read_stream_4`
- `bus_space_read_stream_8`
- `bus_space_read_multi_stream_1`
- `bus_space_read_multi_stream_2`
- `bus_space_read_multi_stream_4`
- `bus_space_read_multi_stream_8`
- `bus_space_read_region_stream_1`
- `bus_space_read_region_stream_2`
- `bus_space_read_region_stream_4`
- `bus_space_read_region_stream_8`
- `bus_space_write_stream_1`
- `bus_space_write_stream_2`
- `bus_space_write_stream_4`
- `bus_space_write_stream_8`
- `bus_space_write_multi_stream_1`
- `bus_space_write_multi_stream_2`
- `bus_space_write_multi_stream_4`
- `bus_space_write_multi_stream_8`
- `bus_space_write_region_stream_1`
- `bus_space_write_region_stream_2`
- `bus_space_write_region_stream_4`
- `bus_space_write_region_stream_8`
- `bus_space_copy_region_stream_1`
- `bus_space_copy_region_stream_2`
- `bus_space_copy_region_stream_4`
- `bus_space_copy_region_stream_8`
- `bus_space_set_multi_stream_1`
- `bus_space_set_multi_stream_2`
- `bus_space_set_multi_stream_4`
- `bus_space_set_multi_stream_8`
- `bus_space_set_region_stream_1`
- `bus_space_set_region_stream_2`
- `bus_space_set_region_stream_4`
- `bus_space_set_region_stream_8`

这些函数的定义与非流式对应函数相同，区别在于它们不提供字节序转换。

## 兼容性

当前 NetBSD 版本的 `bus_space` 接口规范与最初广泛使用并被 FreeBSD 采用的原始规范略有不同。为保持一致性和增强功能，部分函数名称和参数已发生变更。

## 参见

[bus_dma(9)](bus_dma.9.md)

## 历史

`bus_space` 函数最初以不同形式（内存空间和 I/O 空间通过不同的函数集访问）在 NetBSD 1.2 中引入。在 NetBSD 1.3 开发周期早期，这些函数被合并为可在通用“空间”上工作，许多驱动程序被转换以使用它们。本文档在 NetBSD 1.3 开发周期后期编写，规范被更新以修复一些一致性问题并添加一些缺失的功能。

随后，该手册页被适配为 FreeBSD 为 CAM SCSI 驱动程序导入的接口版本及其后续演进。FreeBSD 的 `bus_space` 版本在 FreeBSD 3.0 中导入。

## 作者

`bus_space` 接口由 NetBSD 开发者社区设计和实现。主要贡献者和实现者包括 Chris Demetriou、Jason Thorpe 和 Charles Hannum，但 NetBSD 开发者社区的其余成员和用户社区在开发中发挥了重要作用。

Justin Gibbs 将这些接口移植到 FreeBSD。

Chris Demetriou 编写了本手册页。

Warner Losh 为 FreeBSD 实现进行了修改。

## 缺陷

本手册可能未完整准确地记录该接口，接口的许多部分尚未明确规范。
