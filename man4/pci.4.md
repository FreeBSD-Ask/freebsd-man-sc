# pci.4

`pci` — 通用 PCI/PCIe 总线驱动

## 名称

`pci`

## 概要

`要将 PCI 总线驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device pci

`要编译进对单根 I/O 虚拟化（SR-IOV）的支持：`

> options PCI_IOV

`要编译进对原生 PCI-express 热插拔的支持：`

> options PCI_HP

## 描述

`pci` 驱动为内核中的 PCI 和 PCIe 设备提供支持，并向用户态提供对 PCI 设备的有限访问。

`pci` 驱动提供了一个 `/dev/pci` 字符设备，用户态程序可使用它读写 PCI 配置寄存器。程序还可使用此设备获取所有 PCI 设备的列表，或匹配各种模式的所有 PCI 设备的列表。

由于 `pci` 驱动提供对 PCI 配置寄存器的写接口，系统管理员在授予对 `pci` 设备的访问权限时应格外谨慎。若使用不当，此驱动可能允许用户态应用程序导致机器崩溃或造成数据丢失。具体而言，驱动仅当文件描述符以写方式打开时，才允许对已打开的 `/dev/pci` 进行会修改系统状态的操作。例如，`PCIOCREAD` 和 `PCIOCBARMMAP` 操作要求描述符可写，因为读取配置寄存器或 BAR 读取访问可能会产生特定于功能的副作用。

`pci` 驱动实现了内核中的 PCI 总线。它枚举 PCI 总线上的所有设备，并让 PCI 客户端驱动有机会附加到这些设备。当 BIOS 未分配资源时，它为子设备分配资源。它在必要时处理中断路由。当 PCI 客户端驱动在运行时动态加载时，它会重新探测未附加的 PCI 子设备。`pci` 驱动还支持 PCI-PCI 桥、各种平台特定的 Host-PCI 桥，以及对 PCI VGA 适配器的基本支持。

## IOCTLS

`pci` 驱动支持以下 ioctl(2) 调用。它们定义于头文件

`#include <sys/pciio.h>`

**pc_sel** PCI 域、总线、插槽和功能号。

**pd_name** PCI 设备驱动名称。

**pd_unit** PCI 设备驱动单元号。

**pc_vendor** PCI 厂商 ID。

**pc_device** PCI 设备 ID。

**pc_class** PCI 设备类。

**flags** 标志描述内核应匹配哪些字段。设备必须匹配所有指定字段才能被返回。匹配标志在 `pci_getconf_flags` 结构中枚举。希望这些标志值足够直观，无需详述。

**pc_sel** PCI 域、总线、插槽和功能号。

**pc_hdr** PCI 头类型。

**pc_subvendor** PCI 子厂商 ID。

**pc_subdevice** PCI 子设备 ID。

**pc_vendor** PCI 厂商 ID。

**pc_device** PCI 设备 ID。

**pc_class** PCI 设备类。

**pc_subclass** PCI 设备子类。

**pc_progif** PCI 设备编程接口。

**pc_revid** PCI 修订 ID。

**pd_name** 驱动名称。

**pd_unit** 驱动单元号。

**pd_numa_domain** 设备 NUMA 域。

**pc_reported_len** 包含它的 `pci_conf` 结构的有效部分长度。此值应始终等同于 `pc_spare` 成员的偏移量。

**pc_secbus** 二级 PCI 总线号。（仅对桥设备有效）

**pc_subbus** 下级 PCI 总线号。（仅对桥设备有效）

**pc_spare** 保留供将来使用。

**PCI_GETCONF_LAST_DEVICE** 表示在 `matches` 缓冲区中返回的设备之后，PCI 设备列表中没有更多匹配指定条件的设备。

**PCI_GETCONF_LIST_CHANGED** 此状态告知用户：自上次调用 `PCIOCGETCONF` ioctl 以来，PCI 设备列表已发生变化，用户必须将 `offset` 和 `generation` 重置为零，从列表开头重新开始。

**PCI_GETCONF_MORE_DEVS** 表示用户缓冲区不够大，无法容纳设备列表中剩余所有匹配其条件的设备。

**PCI_GETCONF_ERROR** 表示在处理用户请求时发生一般性错误。如果 `pat_buf_len` 不等于 `num_patterns` 乘以 Fn sizeof struct pci_match_conf，`errno` 将被设为 Er EINVAL。

**pat_buf_len** 由用户提供的模式填充的缓冲区长度（以字节为单位）。

**num_patterns** 用户提供的模式数量。

**patterns** 指向由用户提供的模式填充的缓冲区的指针。`patterns` 是指向 `num_patterns` 个 `pci_match_conf` 结构的指针。`pci_match_conf` 结构由以下元素组成：

**match_buf_len** 用户为保存 `PCIOCGETCONF` 查询结果而分配的 `matches` 缓冲区长度。

**num_matches** 内核返回的匹配数量。

**matches** 包含内核返回的匹配设备的缓冲区。此缓冲区中的项类型为 `pci_conf`，由以下项组成：

**offset** offset 由用户传入，告知内核应从设备列表的何处开始遍历。内核传出的值指向返回的最后一条记录之后的那条记录。用户可在后续调用 `PCIOCGETCONF` ioctl 时传入内核返回的值。如果用户不打算使用 offset，则必须将其设为零。

**generation** PCI 配置 generation。此值仅在 offset 已设置时才需要设置。内核会将其内部设备列表的当前 generation 号与用户传入的 generation 进行比较，以确定自用户上次调用 `PCIOCGETCONF` ioctl 以来设备列表是否已变化。如果设备列表已变化，将传回 `PCI_GETCONF_LIST_CHANGED` 状态。

**status** status 告知用户其设备列表请求的处理结果。可能的状态值有：

**pi_sel** 一个 `pcisel` 结构，指定用户希望查询的域、总线、插槽和功能号。如果找不到指定的总线，errno 将被设为 ENODEV，ioctl 返回 -1。

**pi_reg** 用户希望访问的 PCI 配置寄存器。

**pi_width** 用户希望读取的数据宽度（以字节为单位）。此值可为 1、2 或 4。不支持 3 字节读取和大于 4 字节的读取。如果传入了无效宽度，errno 将被设为 EINVAL。

**pi_data** 内核返回的数据。

**`void *pbm_map_base`** 向调用者报告已建立的映射基址。如果指定了 `PCIIO_BAR_MMAP_FIXED` 标志，则在调用之前必须用映射的期望地址填充此字段。

**`size_t pbm_map_length`** 报告 BAR 的映射长度（以字节为单位）。其 `size_t` 值始终为机器页大小的倍数。

**`uint64_t pbm_bar_length`** 报告设备暴露的 BAR 长度。

**`int pbm_bar_off`** 报告从映射基址到 BAR 中第一个寄存器起始处的偏移量。

**`struct pcisel pbm_sel`** 在调用之前填充。描述要操作的设备。

**`int pbm_reg`** 要 mmap 的 BAR 索引。

**`int pbm_flags`** 增强操作的标志。见下文。

**`int pbm_memattr`** 映射的缓存属性。典型值为：控制寄存器 BAR 使用 `VM_MEMATTR_UNCACHEABLE`，帧缓冲区使用 `VM_MEMATTR_WRITE_COMBINING`。常规的类似内存的 BAR 应使用 `VM_MEMATTR_DEFAULT` 属性映射。

**PCIIO_BAR_MMAP_FIXED** 结果映射应建立在 `pbm_map_base` 成员指定的地址处，否则失败。

**PCIIO_BAR_MMAP_EXCL** 必须与 `PCIIO_BAR_MMAP_FIXED` 一起使用。如果指定基址包含已建立的映射，操作将失败，而不是隐式取消这些映射。

**PCIIO_BAR_MMAP_RW** 请求的映射允许读取和写入。不带此标志时建立只读映射。注意，设备寄存器即使在读取时也常常具有副作用。

**PCIIO_BAR_MMAP_ACTIVATE** （未实现）如果 BAR 未被激活，则在映射过程中将其激活。目前尝试 mmap 未激活的 BAR 会返回错误。

**`struct pcisel pbi_sel`** 描述要操作的设备。

**`int pbi_op`** 要执行的操作。当前支持的值为 `PCIBARIO_READ` 和 `PCIBARIO_WRITE`。

**`uint32_t pbi_bar`** 要操作的 BAR 索引。

**`uint32_t pbi_offset`** BAR 内的操作偏移量。

**`uint32_t pbi_width`** I/O 操作的大小（以字节为单位）。支持 1 字节、2 字节、4 字节和 8 字节操作。

**`uint32_t pbi_value`** 对于读取，值在此字段中返回。对于写入，调用者在此字段中指定要写入的值。注意，此操作会映射并取消映射相应资源，因此对内存 BAR 而言代价相对较高。可改用 `PCIOCBARMMAP` ioctl(2) 为此类 BAR 创建持久的用户空间映射。

**PCIOCGETCONF** 此 ioctl(2) 接收一个 `pci_conf_io` 结构。它允许用户获取系统中所有 PCI 设备的信息，或匹配用户所提供模式的 PCI 设备的信息。此调用可能将 `errno` 设为 copyin(9) 或 copyout(9) 中指定的任何值。`pci_conf_io` 结构由多个字段组成：

**PCIOCREAD** 此 ioctl(2) 读取由传入的 `pci_io` 结构指定的 PCI 配置寄存器。`pci_io` 结构由以下字段组成：

**PCIOCWRITE** 此 ioctl(2) 允许用户写入由传入的 `pci_io` 结构指定的 PCI 配置寄存器。`pci_io` 结构如上所述。上述对读取寄存器数据宽度的限制同样适用于写入 PCI 配置寄存器。

**PCIOCATTACHED** 此 ioctl(2) 允许用户查询是否已有驱动附加到传入的 `pci_io` 结构指定的 PCI 设备。`pci_io` 结构如上所述，但不使用 `pi_reg` 和 `pi_width` 字段。设备的状态保存在 `pi_data` 字段中。值为 0 表示无驱动附加，值大于 0 表示有驱动附加。

**PCIOCBARMMAP** 此 ioctl(2) 命令允许用户空间进程将内存映射的 PCI BAR mmap(2) 到其地址空间中。输入参数和结果通过 `pci_bar_mmap` 结构传递，该结构具有以下字段：当前定义的标志有：

**PCIOCBARIO** 此 ioctl(2) 命令允许用户对 BAR 进行读写。I/O 请求参数通过 `struct pci_bar_ioreq` 结构传递，该结构具有以下字段：

## 加载器可调参数

可在引导内核之前在 [loader(8)](../man8/loader.8.md) 提示符处设置可调参数，或将其存储在 loader.conf(5) 中。这些可调参数的当前值可在运行时通过同名 [sysctl(8)](../man8/sysctl.8.md) 节点查看。除非另有说明，这些可调参数均为布尔值，可通过将其设为非零值来启用。

**3** 关闭所有没有设备驱动的 PCI 设备的电源。

**2** 关闭大多数没有设备驱动的设备电源。显示、内存和基础外设类的 PCI 设备不会被关闭电源。

**1** 与设为 2 类似，但存储控制器也不会被关闭电源。

**0** 所有设备保持全供电。

**<D>** PCI 设备的域（或段），以十进制表示。

**<B>** PCI 设备的总线地址，以十进制表示。

**<S>** PCI 设备的插槽，以十进制表示。

**<P>** 要覆盖的 PCI 插槽中断引脚。为 `A`、`B`、`C` 或 `D` 之一。

**`hw.pci.clear_bars`** （默认为 0）忽略任何固件分配的内存和 I/O 端口资源。这强制 PCI 总线驱动从头分配内存和 I/O 端口资源的资源范围。

**`hw.pci.clear_buses`** （默认为 0）忽略 PCI-PCI 桥中任何固件分配的总线号寄存器。这强制 PCI 总线驱动和 PCI-PCI 桥驱动为 PCI-PCI 桥之后的二级总线分配总线号。

**`hw.pci.clear_pcib`** （默认为 0）忽略 PCI-PCI 桥中任何固件分配的内存和 I/O 端口资源窗口。这强制 PCI-PCI 桥驱动从头为资源窗口分配内存和 I/O 端口资源。默认情况下，PCI-PCI 桥驱动将分配包含固件分配给桥后设备资源的窗口。此外，PCI-PCI 桥驱动会在可能时从现有窗口区域中进行子分配以满足资源请求。因此，必须同时启用 `hw.pci.clear_bars` 和 `hw.pci.clear_pcib` 才能完全忽略固件提供的资源分配。

**`hw.pci.default_vgapci_unit`** （默认为 -1）默认情况下，系统遇到的首个 PCI VGA 适配器被视作引导显示设备。可通过指定关联的 `vgapci``X` 设备的单元号来设置此可调参数以选择特定的 VGA 适配器。

**`hw.pci.do_power_nodriver`** （默认为 0）当未找到合适的设备驱动时，将设备置于低功耗状态（D3）。可设为以下值之一：PCI 设备必须支持电源管理才能被关闭电源。将设备置于低功耗状态未必能降低功耗。

**`hw.pci.do_power_resume`** （默认为 1）在恢复系统或单个设备时，将 PCI 设备置于完全供电状态。不建议将其设为零，因为系统在挂起后不会尝试为未供电的 PCI 设备加电。

**`hw.pci.do_power_suspend`** （默认为 1）在挂起系统或单个设备时，将 PCI 设备置于低功耗状态。通常使用 D3 状态作为低功耗状态，但固件可能在系统挂起期间覆盖所期望的电源状态。

**`hw.pci.enable_ari`** （默认为 1）启用对 PCI-express 替代 RID 解释（Alternative RID Interpretation）的支持。这通常与 SR-IOV 一起使用。

**`hw.pci.enable_io_modes`** （默认为 1）如果 PCI 设备的命令寄存器中具有固件分配的内存或 I/O 端口资源，则在该设备中启用内存或 I/O 端口解码。某些系统的固件（BIOS）即使在已为设备分配资源时，也不会为某些设备启用内存或 I/O 端口解码。此可调参数在总线探测期间为此类资源启用解码。

**`hw.pci.enable_msi`** （默认为 1）启用对消息信号中断（MSI）的支持。可通过将此可调参数设为 0 来禁用 MSI 中断。

**`hw.pci.enable_msix`** （默认为 1）启用对扩展消息信号中断（MSI-X）的支持。可通过将此可调参数设为 0 来禁用 MSI-X 中断。

**`hw.pci.enable_pcie_ei`** （默认为 0）启用对 PCI-express 机电联锁的支持。

**`hw.pci.enable_pcie_hp`** （默认为 1）启用对原生 PCI-express 热插拔的支持。

**`hw.pci.honor_msi_blacklist`** （默认为 1）当设置此可调参数时，对于已知 MSI 和 MSI-X 实现有缺陷的某些芯片组，MSI 和 MSI-X 中断将被禁用。可将其设为零以在芯片组匹配为误报时允许使用 MSI 和 MSI-X 中断。

**`hw.pci.iov_max_config`** （默认为 1MB）通过 SR-IOV 创建虚拟功能（Virtual Function）时所允许的配置参数的最大内存量。此可调参数也可在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 更改。

**`hw.pci.realloc_bars`** （默认为 0）在初始设备扫描期间，对任何固件分配的范围与其他活动资源冲突的内存或 I/O 端口资源，尝试分配新的资源范围。

**`hw.pci.usb_early_takeover`** （默认在 amd64 和 i386 上为 1）在初始设备扫描期间禁用 USB 设备的旧式设备仿真。在使用未包含 USB 控制器驱动的自定义内核时，可将此可调参数设为零以通过旧式仿真使用 USB 设备。

**`hw.pci<D>.<B>.<S>.INT<P>.irq`** 这些可调参数可用于覆盖传统 PCI INTx 中断的中断路由。与列表中的其他可调参数不同，它们没有对应的 sysctl 节点。可调参数名称包含 PCI 设备的地址以及要覆盖的所需 INTx IRQ 引脚：可调参数的值是用于可调参数名称所标识的 INTx 中断引脚的原始 IRQ 值。IRQ 值到平台中断源的映射取决于机器。

## 设备绑定

你可以使用 [device.hints(5)](../man5/device.hints.5.md) 在指定位置绑定设备单元。

### 基于 BSF 的绑定

设备可绑定到总线/插槽/功能（BSF）地址。这是 pciconf(8) 报告的形式。形如 `hints.<name>.<unit>.at="pci<B>:<S>:<F>"` 或 `hints.<name>.<unit>.at="pci<D>:<B>:<S>:<F>"` 的条目将强制驱动 `name` 对任何匹配该规范的 PCI 设备以单元 `unit` 进行探测和附加，其中：

**<D>** PCI 设备的域（或段），以十进制表示。如未指定，默认为 0。

**<B>** PCI 设备的总线地址，以十进制表示。

**<S>** PCI 设备的插槽，以十进制表示。

**<F>** PCI 设备的功能号，以十进制表示。

用于匹配的代码要求字符串精确匹配。不要在 hints 文件中指定尖括号（< >）。将多个设备绑定到相同的 `name` 和 `unit` 会产生未定义的结果。

### 示例

给定 **/boot/device.hints** 中的以下行：

```sh
hint.nvme.3.at="pci6:0:0"
hint.igb.8.at="pci14:0:0"
```

如果在 PCI 总线 14 插槽 0 功能 0 处存在支持 igb(4) 的设备，则会为其分配 igb8 进行探测和附加。同样，如果在 PCI 总线 6 插槽 0 功能 0 处存在 [nvme(4)](nvme.4.md) 设备，则会为其分配 nvme3 进行探测和附加。如果其他类型的卡位于上述任一位置，该卡的名称和单元号将为默认名称，不受这些 hints 影响。如果其他 igb 或 nvme 卡位于其他位置，则会按顺序为其分配单元号，跳过具有 'at' hints 的单元号。

### 基于位置的绑定

虽然 BSF 绑定易于定位设备的放置位置，但该总线号并非不变。系统内设备的任何数量变化都可能使此值在每次引导时发生变化。UEFI 标准定义了一种仅基于地址不变部分的设备路径：根复合体（域）、插槽号和功能号。这些路径难以手工构造，请参见 [devctl(8)](../man8/devctl.8.md) 的‘`getpath`’命令配合‘`UEFI`’定位器。上例也可表示为

```sh
hint.nvme.3.at="PciRoot(0x2)/Pci(0x1,0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)/Pci(0x0,0x0)"
hint.nvme.8.at="PciRoot(0x1)/Pci(0x2,0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)"
```

这种表示法的优点在于你可以指定设备将位于的确切位置。对于具有相同配置的多个系统的部署，这有助于管理设备。但是，即使是主板上的细微变化也可能导致路径大幅改变。考虑到很少有其他工具会报告 UEFI 设备路径，因此考虑 UEFI 设备路径也不太自然。

## 文件

**`/dev/pci`** `pci` 驱动的字符设备。

## 参见

[device.hints(5)](../man5/device.hints.5.md), pciconf(8)

## 历史

`pci` 驱动（非内核的 PCI 支持代码）首次出现于 FreeBSD 2.2，由 Stefan Esser 和 Garrett Wollman 编写。设备列表和匹配支持由 Kenneth Merry 重新实现，首次出现于 FreeBSD 3.0。

## 作者

Kenneth Merry <ken@FreeBSD.org>

## 缺陷

用户无法在不至少调用一次 `PCIOCGETCONF` 的情况下指定设备列表中的准确偏移量，因为否则他们无法知道当前的 generation 号。不过，这可能不是一个严重问题，因为用户可以通过指定一个或多个模式供内核匹配来轻松缩小搜索范围。
