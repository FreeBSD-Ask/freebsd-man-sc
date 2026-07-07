# proto(4)

`proto` — 通用原型设计与诊断驱动程序

## 名称

`proto`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device proto

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
proto_load="YES"
```

若要让驱动程序附加到设备而非其常规驱动程序，将其列入赋给以下加载器变量的设备列表中：

> hw.proto.attach="desc[,desc]"

## 描述

当 PCI 或 ISA 设备没有其他驱动程序存在时，`proto` 设备驱动程序会附加到这些设备，并为该设备关联的所有资源创建设备专用文件。该驱动程序本身不了解所附加设备的任何信息。程序可以打开这些设备专用文件并执行寄存器级别的读写。因此，`proto` 设备驱动程序不过是用户空间程序与硬件设备之间的通道或网关。

这种设计在硬件诊断和原型设计场景中非常有用。在这两种场景下，在用户空间开发和运行逻辑都更为便利。特别是硬件诊断需要相对友好的用户界面和完善的报告机制。这些在内核代码中都不容易实现。

### I/O 端口资源

为 I/O 端口资源创建的设备专用文件允许对其执行 lseek(2)、read(2)、write(2) 和 ioctl(2) 操作。read(2) 和 write(2) 系统调用分别用于在该端口上执行输入和输出。单次可读取或写入的数据量为 1、2 或 4 字节。虽然在某些架构上 `proto` 驱动程序并不阻止一次读取或写入 8 字节，但不应假设这确实能产生正确结果。lseek(2) 系统调用用于选择端口号，相对于设备专用文件所代表的 I/O 端口区域。例如，若设备专用文件对应于 0x3f8 至 0x3ff（含）的 I/O 端口区域，则当 lseek 的 whence 取值为 SEEK_SET 时给定偏移 4，下一次读或写操作将指向端口 0x3fc。ioctl(2) 系统调用可用于 `PROTO_IOC_REGION` 请求。此 ioctl 请求返回该设备专用文件所覆盖资源的范围。范围以下列结构返回：

```sh
struct proto_ioc_region {
        unsigned long   address;
        unsigned long   size;
};
```

### 内存映射 I/O 资源

为内存映射 I/O 资源创建的设备专用文件，其行为与为 I/O 端口资源创建的设备专用文件相同。此外，内存映射 I/O 资源的设备专用文件允许通过 mmap(2) 将内存映射到进程的地址空间。对 mmap(2) 返回的内存地址的读写会直接到达硬件。这样可以避免使用 read(2) 和 write(2)，显著降低访问开销。底层设备施加的对齐和访问宽度限制仍然适用。同时，确保编译器不会优化掉内存访问，也不会将多次访问合并为更大的访问。

### DMA 伪资源

为执行 DMA 创建了一个名为 `busdma` 的设备专用文件。它仅支持 ioctl(2)，且仅支持 `PROTO_IOC_BUSDMA` 请求。此设备专用文件不支持 read(2) 和 write(2)。`PROTO_IOC_BUSDMA` 请求的参数同时用于输入和输出，定义如下：

```sh
struct proto_ioc_busdma {
        unsigned int    request;
        unsigned long   key;
        union {
                struct {
                        unsigned long   align;
                        unsigned long   bndry;
                        unsigned long   maxaddr;
                        unsigned long   maxsz;
                        unsigned long   maxsegsz;
                        unsigned int    nsegs;
                        unsigned int    datarate;
                        unsigned int    flags;
                } tag;
                struct {
                        unsigned long   tag;
                        unsigned int    flags;
                        unsigned long   virt_addr;
                        unsigned long   virt_size;
                        unsigned int    phys_nsegs;
                        unsigned long   phys_addr;
                        unsigned long   bus_addr;
                        unsigned int    bus_nsegs;
                } md;
                struct {
                        unsigned int    op;
                        unsigned long   base;
                        unsigned long   size;
                } sync;
        } u;
        unsigned long   result;
};
```

`request` 字段用于指定要执行的 DMA 操作。`key` 字段用于指定操作所应用的对象。对象要么是标签，要么是内存描述符（md）。已定义的 DMA 操作如下：

**PROTO_IOC_BUSDMA_TAG_CREATE** 创建一个根标签。输出时将 DMA 标签的键值设置到 `result` 字段。该标签按照 `tag` 子结构所给的约束创建。这些约束大致对应于可传递给 bus_dma_tag_create(9) 函数的约束。

**PROTO_IOC_BUSDMA_TAG_DERIVE** 创建一个派生标签。`key` 字段用于标识要从中派生新标签的父标签。派生标签的键值通过 `result` 字段返回。派生标签将父标签的约束与 `tag` 子结构所给的约束合并。返回时合并后的约束会被写回 `tag` 子结构。

**PROTO_IOC_BUSDMA_TAG_DESTROY** 销毁此前创建的根标签或派生标签。`key` 字段指定要销毁的标签。标签只有在不再被引用时才能被销毁。这意味着以该标签为父的派生标签和由该标签创建的内存描述符必须先被销毁。

**PROTO_IOC_BUSDMA_MEM_ALLOC** 分配满足 `md` 子结构的 `tag` 字段所给标签约束的内存。该内存的内存描述符键值通过 `result` 字段返回。返回时 `md` 子结构会填入分配的详细信息。分配内存的内核虚拟地址和大小通过 `virt_addr` 和 `virt_size` 字段返回。连续物理内存段的数目和首段地址通过 `phys_nsegs` 和 `phys_addr` 字段返回。分配的内存会自动加载并映射到总线空间。总线段的数目和首段地址通过 `bus_nsegs` 和 `bus_addr` 字段返回。此操作的行为严重依赖于 bus_dmamem_alloc(9) 的实现方式，这意味着目前内存总是以单一连续的物理内存区域分配。实践中这也倾向于在总线空间中给出单一连续区域。这一点日后可能变化。

**PROTO_IOC_BUSDMA_MEM_FREE** 释放此前分配的内存并销毁内存描述符。`proto` 驱动程序无法跟踪内存是否已映射到进程的地址空间，因此在释放前由应用程序负责解除映射。即使在内存已释放后，`proto` 驱动程序也无法防止硬件对该内存进行读写。当内存被重用于其他用途时，若在释放前 DMA 尚未完全停止，内存可能被破坏，或使硬件行为不可预测。

**PROTO_IOC_BUSDMA_MD_CREATE** 创建一个空的内存描述符，标签由 `md` 子结构的 `tag` 字段指定。内存描述符的键值通过 `result` 字段返回。

**PROTO_IOC_BUSDMA_MD_DESTROY** 销毁由 `key` 字段指定的此前创建的内存描述符。若内存描述符仍处于加载状态，会先卸载。

**PROTO_IOC_BUSDMA_MD_LOAD** 在由 `key` 字段指定的内存描述符中加载一段连续内存区域。其大小和进程虚拟地址空间中的地址由 `virt_size` 和 `virt_addr` 字段指定。返回时，`md` 子结构包含操作结果。物理段的数目和首段地址通过 `phys_nsegs` 和 `phys_addr` 字段返回。总线空间段的数目和总线空间中首段地址通过 `bus_nsegs` 和 `bus_addr` 字段返回。

**PROTO_IOC_BUSDMA_MD_UNLOAD** 卸载由 `key` 字段指定的内存描述符。

**PROTO_IOC_BUSDMA_SYNC** 保证所有硬件组件对由 `key` 字段指定的内存描述符所跟踪的内存拥有一致视图。可通过指定要使其一致的相对偏移和大小来定向内存的某个子区。偏移和大小由 `sync` 子结构的 `base` 和 `size` 字段给出。`op` 字段保存要执行的同步操作。这类似于 bus_dmamap_sync(9) 函数。

### PCI 配置空间

可通过 `pcicfg` 设备专用文件访问 PCI 配置空间。该设备专用文件支持 lseek(2)、read(2) 和 write(2)。用法与 I/O 端口资源相同。

## 文件

对应于 PCI 设备的所有设备专用文件位于 **`/dev/proto/pci<d>:<b>:<s>:<f>`** 下，其中 `pci<d>:<b>:<s>:<f>` 表示该 PCI 设备在 PCI 层次结构中的位置。一个 PCI 位置包含：

**<d>** PCI 域号
**<b>** PCI 总线号
**<s>** PCI 插槽或设备号
**<f>** PCI 功能号

每个 PCI 设备都有一个名为 `pcicfg` 的设备专用文件。此设备专用文件提供对 PCI 配置空间的访问。同时还会创建一个名为 `busdma` 的设备专用文件，提供执行 DMA 所需的接口。对每个有效的基地址寄存器（BAR），都会创建一个包含 BAR 偏移和资源类型的设备专用文件。资源类型可以是 `io` 或 `mem`，分别表示 I/O 端口或内存映射 I/O 空间。

ISA 设备没有位置标识。它们以第一个 I/O 端口地址或第一个内存映射 I/O 地址来标识。因此，对应于 ISA 设备的所有设备专用文件位于 **`/dev/proto/isa:<addr>`** 下，其中 `addr` 是十六进制表示的地址。对每个 I/O 端口或内存映射 I/O 地址，都会创建一个包含内核所用资源标识和资源类型的设备专用文件。资源类型可以是 `io` 或 `mem`，分别表示 I/O 端口或内存映射 I/O 空间。当设备被分配了 DMA 通道时，还会创建名为 `busdma` 的设备专用文件，提供执行 DMA 所需的接口。

如果 ISA 设备既不是即插即用设备，也不在 ACPI 设备树中，则必须提供适当的 hints，以便内核为其预留资源。

## 实例

位于域 0、总线 1、插槽 2 中且具有单一内存映射 I/O 区域的单功能 PCI 设备将拥有以下设备专用文件：

**`/dev/proto/pci0:1:2:0/10.mem`**
**`/dev/proto/pci0:1:2:0/pcicfg`**

一个传统的软盘控制器将拥有以下设备文件：

**`/dev/proto/isa:0x3f0/00.io`**
**`/dev/proto/isa:0x3f0/01.io`**
**`/dev/proto/isa:0x3f0/busdma`**

## 参见

ioctl(2), lseek(2), mmap(2), read(2), write(2), bus_dma_tag_create(9), bus_dmamap_sync(9), bus_dmamem_alloc(9)

## 作者

`proto` 设备驱动程序及本手册页由 Marcel Moolenaar <marcel@xcllnt.net> 编写。

## 安全注意事项

由于程序可以直接访问硬件，`proto` 驱动程序本质上是不安全的。不建议在生产机器上使用此驱动程序。

## 缺失功能

`proto` 驱动程序未完全支持需要多个物理内存段或多个总线空间段的内存描述符。至少需要在 DMA 伪资源上提供一个操作，让应用程序能够获取所有段。

`proto` 驱动程序尚不支持中断。由于中断无法由驱动程序自身处理，必须将其转换为信号并投递给已注册中断的程序。在信号处理期间保持中断屏蔽的令人满意的机制仍在研究中。

除总线主控设备外，其他设备的 DMA 支持尚未实现。程序与 DMA 控制器交互方式的细节仍需进一步细化。
