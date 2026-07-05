# arch.7

`arch` — 架构专属细节

## 名称

`arch`

## 描述

FreeBSD 支持的 CPU 架构与平台之间的差异。

### 简介

本文档是 FreeBSD 各架构移植版本关键 ABI 细节的快速参考。如需完整细节，请查阅处理器专属的 ABI 补充文档。

除非另有说明，尺寸均以字节为单位。本文档中的架构细节适用于 FreeBSD 13.0 及以后版本，另有说明的除外。

FreeBSD 使用平坦地址空间。`unsigned long`、`ptraddr_t` 和 `size_t` 类型的变量具有相同的表示。

为了最大化与未来指针完整性机制的兼容性，将指针作为整数进行操作时应通过 `uintptr_t` 或 `intptr_t` 进行，而不使用其他类型，因为 C 标准仅保证这两种整数类型可以将指针转换为该类型再转换回原类型。在 CHERI 系统上，`uintptr_t` 和 `intptr_t` 定义为 `__uintcap_t` 和 `__intcap_t`，表示可通过整数运算操作的能力（capability）。如果指针稍后将被转换回可解引用的指针，则不应将其转换为 `long`、`ptrdiff_t` 或 `size_t`，因为在所有架构上它们仍然是裸整数类型。

某些架构（例如 `powerpc64` 的 AIM 变体）中，内核使用独立的地址空间。其他架构中，内核与用户态进程共享单一地址空间。内核位于最高地址处。

在每个架构上，主用户态线程的栈从靠近最高用户地址处开始，向下生长。

FreeBSD 的架构支持因版本而异。下表展示当前支持的 CPU 架构，以及首次支持该架构的 FreeBSD 版本。

| **架构** | **首次发布版本** |
| --- | --- |
| aarch64 | 11.0 |
| aarch64c | 16.0（计划中） |
| amd64 | 5.1 |
| armv7 | 12.0 |
| powerpc64 | 9.0 |
| powerpc64le | 13.0 |
| riscv64 | 12.0 |
| riscv64c | 16.0（计划中） |

已停止支持的架构见下表。

| **架构** | **首次发布版本** | **最终发布版本** |
| --- | --- | --- |
| alpha | 3.2 | 6.4 |
| arm | 6.0 | 12.4 |
| armeb | 8.0 | 11.4 |
| armv6 | 10.0 | 14.x |
| ia64 | 5.0 | 10.4 |
| i386 | 1.0 | 14.x |
| mips | 8.0 | 13.5 |
| mipsel | 9.0 | 13.5 |
| mipselhf | 12.0 | 13.5 |
| mipshf | 12.0 | 13.5 |
| mipsn32 | 9.0 | 13.5 |
| mips64 | 9.0 | 13.5 |
| mips64el | 9.0 | 13.5 |
| mips64elhf | 12.0 | 13.5 |
| mips64hf | 12.0 | 13.5 |
| pc98 | 2.2 | 11.4 |
| powerpc | 6.0 | 14.x |
| powerpcspe | 12.0 | 14.x |
| riscv64sf | 12.0 | 13.5 |
| sparc64 | 5.0 | 12.4 |

### 类型尺寸

所有 FreeBSD 架构均使用某种 ELF（参见 [elf(5)](../man5/elf.5.md)）**应用二进制接口**（ABI）变体用于机器处理器。支持的 ABI 可分为三大类：

**`ILP32`** `int`、`intptr_t`、`long` 和 `void *` 类型的机器表示均为 4 字节。

**`LP64`** `int` 类型的机器表示使用 4 字节，而 `intptr_t`、`long` 和 `void *` 使用 8 字节。

**`L64PC128`** `int` 类型的机器表示使用 4 字节。`long` 类型的机器表示使用 8 字节。`intptr_t` 和 `void *` 为 16 字节能力。

某些机器支持多种 FreeBSD ABI。通常这些是 64 位机器，其“原生”`LP64` 执行环境伴随“传统”`ILP32` 环境，后者是 64 位演化的历史 32 位前身。例如：

| **LP64** | **对应的 ILP32** |
| --- | --- |
| `amd64` | `i386` |
| `powerpc64` | `powerpc` |
| `aarch64` | `armv7` |

如果 CPU 实现了 `AArch32` 执行状态，`aarch64` 将支持执行 `armv7` 二进制文件。FreeBSD 不再支持针对 `armv6` 及更早版本的目标二进制文件。

具备 128 位能力的架构同时支持“原生”`L64PC128` 执行环境和 `LP64` 环境：

| **L64PC128** | **对应的 LP64** |
| --- | --- |
| `aarch64c` | `aarch64` |
| `riscv64c` | `riscv64` |

在所有支持的架构上：

| **类型** | **尺寸** |
| --- | --- |
| short | 2 |
| int | 4 |
| long long | 8 |
| float | 4 |
| double | 8 |

整数以二进制补码表示。整数和指针类型的对齐是自然对齐，即变量地址必须与类型尺寸取模为零。唯一例外是 `i386` 仅要求 64 位整数 4 字节对齐。

依赖机器的类型尺寸：

| **架构** | **long** | **void \*** | **long double** | **time_t** |
| --- | --- | --- | --- | --- |
| aarch64 | 8 | 8 | 16 | 8 |
| aarch64c | 8 | 16 | 16 | 8 |
| amd64 | 8 | 8 | 16 | 8 |
| armv7 | 4 | 4 | 8 | 8 |
| i386 | 4 | 4 | 12 | 4 |
| powerpc | 4 | 4 | 8 | 8 |
| powerpc64 | 8 | 8 | 8 | 8 |
| powerpc64le | 8 | 8 | 16 | 8 |
| riscv64 | 8 | 8 | 16 | 8 |
| riscv64c | 8 | 16 | 16 | 8 |

除 i386 外，所有受支持架构的 **time_t** 均为 8 字节。

### 字节序与 char 符号性

| **架构** | **字节序** | **char 符号性** | **wchar_t 符号性** |
| --- | --- | --- | --- |
| aarch64 | 小端 | 无符号 | 无符号 |
| aarch64c | 小端 | 无符号 | 无符号 |
| amd64 | 小端 | 有符号 | 有符号 |
| armv7 | 小端 | 无符号 | 无符号 |
| i386 | 小端 | 有符号 | 有符号 |
| powerpc | 大端 | 无符号 | 有符号 |
| powerpc64 | 大端 | 无符号 | 有符号 |
| powerpc64le | 小端 | 无符号 | 有符号 |
| riscv64 | 小端 | 有符号 | 有符号 |
| riscv64c | 小端 | 有符号 | 有符号 |

### 页面尺寸

| **架构** | **页面尺寸** |
| --- | --- |
| aarch64 | 4K, 64K, 2M, 1G |
| aarch64c | 4K, 64K, 2M, 1G |
| amd64 | 4K, 2M, 1G |
| armv7 | 4K, 1M |
| i386 | 4K, 2M (PAE), 4M |
| powerpc | 4K |
| powerpc64 | 4K |
| powerpc64le | 4K |
| riscv64 | 4K, 2M, 1G |
| riscv64c | 4K, 2M, 1G |

### 用户地址空间布局

| **架构** | **最大地址** | **地址空间大小** |
| --- | --- | --- |
| aarch64 | 0x0001000000000000 | 256TiB |
| aarch64c | 0x0001000000000000 | 256TiB |
| amd64 (LA48) | 0x0000800000000000 | 128TiB |
| amd64 (LA57) | 0x0100000000000000 | 64PiB |
| armv7 | 0xbfc00000 | 3GiB |
| i386 | 0xffc00000 | 4GiB |
| powerpc | 0xfffff000 | 4GiB |
| powerpc64 | 0x000fffffc0000000 | 4PiB |
| powerpc64le | 0x000fffffc0000000 | 4PiB |
| riscv64 (Sv39) | 0x0000004000000000 | 256GiB |
| riscv64c (Sv39) | 0x0000004000000000 | 256GiB |
| riscv64 (Sv48) | 0x0000800000000000 | 128TiB |
| riscv64c (Sv48) | 0x0000800000000000 | 128TiB |

进程地址空间的布局可通过 `KERN_PROC_VM_LAYOUT` sysctl(3) MIB 查询。

历史上，amd64 CPU 限制为 48 位虚拟地址空间。较新的 CPU 支持 5 级页表，将地址的有效位扩展到 57 位（LA57 模式）。地址空间布局由 CPU 对 LA57 的支持决定。将 **vm.pmap.la57** 可调参数设为 0 会强制系统进入 4 级分页模式，即使硬件支持 5 级分页。在此模式下，所有进程获得 48 位地址空间。**vm.pmap.prefer_la48_uva** 可调参数决定在 LA57 系统上运行的进程默认是否限制为 48 位地址空间。某些应用程序利用指针值中未使用的高位存储信息，因此隐式假定运行在 LA48 模式下。为避免破坏兼容性，所有进程默认运行在 LA48 模式。可使用 elfctl(1) 工具为特定可执行文件请求 LA48 或 LA57 模式。类似地，可使用 proccontrol(1) 在执行进程时配置地址空间布局。

RISC-V 规范允许 3 级（Sv39）、4 级（Sv48）和 5 级（Sv57）页表。硬件仅要求实现 Sv39；支持 Sv48 的实现也必须支持 Sv39，支持 Sv57 的实现也必须支持 Sv48。可使用 **vm.pmap.mode** 可调参数选择布局。FreeBSD 目前支持 Sv39 和 Sv48，默认使用 Sv39。

### 浮点

| **架构** | **float, double** | **long double** |
| --- | --- | --- |
| aarch64 | 硬件 | 软件，四精度 |
| aarch64c | 硬件 | 软件，四精度 |
| amd64 | 硬件 | 硬件，80 位 |
| armv7 | 硬件 | 硬件，双精度 |
| i386 | 硬件 | 硬件，80 位 |
| powerpc | 硬件 | 硬件，双精度 |
| powerpc64 | 硬件 | 硬件，双精度 |
| powerpc64le | 硬件 | 软件，四精度 |
| riscv64 | 硬件 | 硬件，四精度 |
| riscv64c | 硬件 | 硬件，四精度 |

### 默认工具链

FreeBSD 在所有支持的 CPU 架构上使用 [clang(1)](../man1/clang.1.md) 作为默认编译器，使用 LLVM 的 [ld.lld(1)](../man1/ld.lld.1.md) 作为默认链接器，以及 LLVM 二进制工具如 objcopy(1) 和 [readelf(1)](../man1/readelf.1.md)。

### MACHINE_ARCH、MACHINE_CPUARCH 与 MACHINE 的对比

在 Makefile 中测试通用架构时应优先使用 `MACHINE_CPUARCH`。当涉及特定架构类型且存在多种选择或可能存在多种选择时，应优先使用 `MACHINE_ARCH`。在引用内核、依赖特定内核类型的接口或类似启动序列等内容时，使用 `MACHINE`。

| `MACHINE` | `MACHINE_CPUARCH` | `MACHINE_ARCH` |
| --- | --- | --- |
| arm64 | aarch64 | aarch64, aarch64c |
| amd64 | amd64 | amd64 |
| arm | arm | armv7 |
| i386 | i386 | i386 |
| powerpc | powerpc | powerpc, powerpc64, powerpc64le |
| riscv | riscv | riscv64, riscv64c |

### 预定义宏

编译器提供若干预定义宏。其中一些提供架构专属细节，下文加以说明。其他宏，包括语言标准要求的宏，此处不列出。

完整的预定义宏集合可通过以下命令获取：

```sh
cc -x c -dM -E /dev/null
```

常见类型尺寸和字节序宏：

| **宏** | **含义** |
| --- | --- |
| `__SIZEOF_LONG__` | long 的字节尺寸 |
| `__SIZEOF_POINTER__` | intptr_t 和指针的字节尺寸 |
| `__SIZEOF_SIZE_T__` | size_t 的字节尺寸 |
| `__LP64__` | 64 位（8 字节）long 和指针，32 位（4 字节）int |
| `__ILP32__` | 32 位（4 字节）int、long 和指针 |
| `__CHERI__` | 128 位（16 字节）能力指针，64 位（8 字节）long |
| `BYTE_ORDER` | `BIG_ENDIAN` 或 `LITTLE_ENDIAN` |

由于历史上系统要么是 `__ILP32__` 要么是 `__LP64__`，程序员通常只测试其中一个并在 else 分支中假定另一个。随着 CHERI 架构的出现，情况已不再如此。应改用 `__SIZEOF_*__` 宏。应避免新使用 `__ILP32__` 和 `__LP64__`。CHERI 目标的编译器不定义 `__LP64__`，因为其指针是 128 位能力。

架构专属宏：

| **架构** | **预定义宏** |
| --- | --- |
| aarch64 | `__aarch64__` |
| aarch64c | `__aarch64__`, `__CHERI__` |
| amd64 | `__amd64__`, `__x86_64__` |
| armv7 | `__arm__`, `__ARM_ARCH >= 7` |
| i386 | `__i386__` |
| powerpc | `__powerpc__` |
| powerpc64 | `__powerpc__`, `__powerpc64__` |
| powerpc64le | `__powerpc__`, `__powerpc64__` |
| riscv64 | `__riscv`, `__riscv_xlen == 64` |
| riscv64c | `__riscv`, `__riscv_xlen == 64`, `__CHERI__` |

编译器可能定义架构专属宏的其他变体。在 FreeBSD 中优先使用上述宏。

### 重要的 make(1) 变量

大多数可外部设置的变量在 [build(7)](build.7.md) 手册页中定义。这些变量未在其他地方记录，但在构建系统中被广泛使用。

**`MACHINE`** 表示硬件平台。与原生平台的 [uname(1)](../man1/uname.1.md) `-m` 输出相同。它同时定义用户态/内核接口，以及引导加载器/内核接口。仅应在这些上下文中使用。每个 CPU 架构可能支持多个硬件平台，这些平台的 `MACHINE` 各不相同。它用于汇集 [config(8)](../man8/config.8.md) 的所有文件以构建内核。它通常与 `MACHINE_ARCH` 相同，正如一种 CPU 架构可由多种硬件平台实现一样，一种硬件平台也可能支持多个 CPU 架构家族成员，但二进制文件不同。例如，i386 的 `MACHINE` 支持 IBM-AT 硬件平台，而 pc98 的 `MACHINE` 支持日本 NEC 公司的 PC-9801 和 PC-9821 硬件平台。这两种硬件平台都仅支持 i386 的 `MACHINE_ARCH`，它们共享通用 ABI，仅在涉及底层硬件平台差异（总线架构、设备枚举和引导接口）的某些内核/用户态接口上有所不同。一般而言，`MACHINE` 仅应在 src/sys 和 src/stand 中使用，或在系统映像制作器或安装程序中使用。

**`MACHINE_ARCH`** 表示 CPU 处理器架构。与原生平台的 [uname(1)](../man1/uname.1.md) `-p` 输出相同。它定义所支持的 CPU 指令家族。它还可能编码多字节整数字节序（端序）的变体。它还可能编码整数或指针尺寸的变体。它还可能编码 ISA 修订版本。它还可能编码硬浮点与软浮点 ABI 及用法。它还可能在其他因素不能唯一定义 ABI 时编码变体 ABI。它与 `MACHINE` 一起定义系统使用的 ABI。通常，纯 CPU 名称指定 CPU 最常见（或至少首个）变体。这就是 powerpc 和 powerpc64 暗示“大端”，而 armv7 和 aarch64 暗示小端的原因。如果将来要支持所谓的 x32 ABI（在 amd64 架构上使用 32 位指针），很可能编码为 amd64-x32。遗憾的是，amd64 指定 x86 平台的 64 位演化（符合“首条规则”），而几乎所有其他人都使用 x86_64。FreeBSD 移植如此之早，早于 Intel 加入市场后的处理器名称标准化。当时每个操作系统选择自己的约定。向后兼容性意味着不容易更改为共识名称。

**`MACHINE_CPUARCH`** 表示给定 `MACHINE_ARCH` 的源代码位置。它通常是共享相同实现的所有 MACHINE_ARCH 的公共前缀，尽管 'riscv' 打破了这一规则。虽然 amd64 和 i386 关系密切，但它们的 MACHINE_CPUARCH 不是 x86。FreeBSD 源代码库以名为 amd64 和 i386 的子目录支持 amd64 和 i386（尽管在幕后有一些符合此框架的共享）。

**`CPUTYPE`** 设置要构建的 `MACHINE_ARCH` 风格。用于针对二进制文件运行的特定 CPU/核心优化构建。通常这不会改变 ABI，尽管在特定情况下优化与改变 ABI 之间界限微妙。

**`TARGET`** 用于在顶层 Makefile 中为交叉构建设置 `MACHINE`。在该范围之外未使用。它不会传递到构建的其余部分。顶层之外的 Makefile 完全不应使用它（尽管有些由于历史原因拥有自己的私有副本）。

**`TARGET_ARCH`** 用于在顶层 Makefile 中为交叉构建设置 `MACHINE_ARCH`。与 `TARGET` 一样，在该范围之外未使用。

## 参见

elfctl(1), proccontrol(1), sysctl(3), [src.conf(5)](../man5/src.conf.5.md), [build(7)](build.7.md), [simd(7)](simd.7.md)

## 历史

`arch` 手册页首次出现于 FreeBSD 11.1。
