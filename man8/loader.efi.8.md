# loader.efi(8)

`loader.efi` — UEFI 内核加载器

## 名称

`loader.efi`

## 描述

在 UEFI 系统上，`loader.efi` 负责加载内核。

在使用 bsdinstall(8) 安装的系统上，当 `loader.efi` 按照uefi(8)中所述安装为默认 EFI 引导程序，或使用 efibootmgr(8) 配置为 EFI 引导项时，会直接从 EFI 系统分区（ESP）调用 `loader.efi`。

在从 FreeBSD 10 或更早版本升级的系统上，ESP 可能太小而无法容纳 `loader.efi`。在这种情况下，可以将 boot1.efi(8) 保留为固件引导程序。它会链式加载当前的 **`/boot/loader.efi`**，该文件会在 `installworld` 过程中更新。boot1.efi(8) 在新安装中已弃用。

### 控制台注意事项

UEFI 固件提供一个通用控制台。在 `loader.efi` 中，通过将 `console` 变量设置为“efi”来选择它。`loader.efi` 会检查 UEFI 环境变量 `8be4df61-93ca-11d2-aa0d-00e098032b8c-ConOut` 以推测“efi”控制台指向的位置。`loader.efi` 会将其提示和菜单输出到 ConOut 指定的所有位置。然而，当存在多个控制台时，FreeBSD 内核有一个限制：内核会输出到所有已配置的控制台，但只有主控制台会接收来自rc(8)系统的日志消息以及诸如 geli(8) 密码之类的提示。如果 `loader.efi` 首先发现视频设备，则 `loader.efi` 会通知内核将视频控制台作为主控制台。同样，如果 `ConOut` 列表中第一个是串口设备，则串口将成为主控制台。

如果没有 `ConOut` 变量，则同时尝试串口和视频。`loader.efi` 对视频使用“efi”控制台（可能工作也可能不工作），对 `COM1` 上的串口使用默认波特率的“comconsole”。内核将使用双控制台，如果检测到 UEFI 图形设备则以视频控制台为主，否则以串口控制台为主。

在 x86 平台上，如果你希望在 UEFI 固件不支持时将加载器的输出重定向到串口，或重定向到非 UEFI 固件输出所指向的串口，请将 `console` 设置为“comconsole”。默认端口为 `COM1`，I/O 地址为 0x3f8。可使用 `comconsole_port` 将其设置为不同的端口地址。可使用 `comconsole_speed` 设置串口的波特率（默认为 9600）。如果将 `console` 设置为“efi,comconsole”，则会在 EFI 控制台和串口上同时获得输出。如果这导致字符重复，请将 `console` 设置为“efi”，因为你的 UEFI 固件已经在重定向到串口。

如果你的 UEFI 固件重定向了串口，可能需要告知内核使用哪个地址。EFI 使用 ACPI 的 UID 来标识串口，但 `loader.efi` 没有 ACPI 解析器，因此无法将其转换为 I/O 端口。FreeBSD 内核在解码 ACPI 资源之前就初始化其控制台。FreeBSD 内核会查看 `hw.uart.console` 变量来设置其串口控制台。其格式在uart(4)中描述。将其设置为“io:0x3f8,br:115200”并使用正确的端口地址。PCI 或内存映射端口超出了本手册页的范围。

在 IBM PC 兼容系统上，串口分配如下：

| **Windows 名称** | **I/O 端口地址** | **典型 FreeBSD 设备** |
| --- | --- | --- |
| COM1 | 0x3f8 | `/dev/uart0` |
| COM2 | 0x2f8 | `/dev/uart1` |
| COM3 | 0x3e8 | `/dev/uart2` |
| COM4 | 0x2e8 | `/dev/uart3` |

不过 `COM3` 和 `COM4` 可能有所不同。

### 主控制台

主控制台通过引导标志设置。这些命令行参数为内核设置相应的标志。可以通过将 loader 环境变量设置为“yes”或“no”来控制这些标志。引导标志可在引导命令的命令行上设置。在内核内部，RB_ 标志用于控制行为，有时以架构特定的方式使用，包含它们是为了帮助发现本文档未涵盖的任何行为。

| **引导标志** | **Loader 变量** | **内核 RB_ 标志** |
| --- | --- | --- |
| `-a` | `boot_askme` | `RB_ASKNAME` |
| `-c` | `boot_cdrom` | `RB_CDROM` |
| `-d` | `boot_ddb` | `RB_KDB` |
| `-r` | `boot_dfltroot` | `RB_DFLTROOT` |
| `-D` | `boot_multiple` | `RB_MULTIPLE` |
| `-m` | `boot_mute` | `RB_MUTE` |
| `-g` | `boot_gdb` | `RB_GDB` |
| `-h` | `boot_serial` | `RB_SERIAL` |
| `-p` | `boot_pause` | `RB_PAUSE` |
| `-P` | `boot_probe` | `RB_PROBE` |
| `-s` | `boot_single` | `RB_SINGLE` |
| `-v` | `boot_verbose` | `RB_VERBOSE` |

以下标志决定主控制台：

| **标志** | **内核标志** | **内核控制台** | **主控制台** |
| --- | --- | --- | --- |
| 无 | 0 | 视频 | 视频 |
| `-h` | RB_SERIAL | 串口 | 串口 |
| `-D` | RB_MULTIPLE | 串口，视频 | 视频 |
| `-Dh` | RB_SERIAL \| RB_MULTIPLE | 串口，视频 | 串口 |

`loader.efi` 不实现探测 `-P` 功能（即在连接键盘时使用视频控制台，否则使用串口控制台）。

### 额外环境变量

`loader.efi` 可以在启动早期从 EFI 分区上的文件中设置变量。默认情况下，该文件为 **`/efi/freebsd/loader.env`**。可以通过设置 FreeBSD EFI 变量 `LoaderEnv` 来更改，例如：

```sh
echo -n /efi/freebsd/alt.env | efivar -w -t 7 \
    -n cfee69ad-a0de-47a9-93a8-f63106f8ae99-LoaderEnv
```

执行该命令后，将使用 **`/efi/freebsd/alt.env`** 而不是 **`/efi/freebsd/loader.env`**。有关设置 EFI 变量的更多信息，请参见 efivar(8)。

可以将 EFI 变量 `NextLoaderEnv` 设置为第二个启动文件的路径名。该变量在取值后立即删除，因此设置它只会影响下一次引导尝试。对于任一变量，缺失的文件都会被静默忽略。

启动文件中只能设置简单变量。可以用来指定根文件系统：

```sh
rootdev=disk0s1a
```

启动文件包含一系列由空格、制表符或换行符分隔的赋值语句。引号不会被特殊处理。如果未给出 `=value`，则使用值 `1`。无效语法等会被静默忽略。

### 暂存余量

内核必须解析固件内存映射表，以了解可以使用哪些内存。它还需要为内核页表分配内存。由于它必须分配内存才能做到这一点，而又不能覆盖重要的结构（例如跳板页表），`loader.efi` 确保在它加载的所有内容（内核、模块和元数据）之后有额外的可用内存，称为“slop”，供内核引导内存分配器使用。

默认情况下，amd64 保留 8MB。`staging_slop` 命令允许调整 slop 大小。它接受单个参数，即以字节为单位的 slop 大小。

### amd64 Nocopy

`loader.efi` 会将内核加载到 4GB 以下 2MB 对齐的内存中。它无法加载到固定地址，因为 UEFI 固件可能在运行时为其自身使用保留任意内存。在 FreeBSD 13.1 之前，内核保留了在恰好 2MB 处加载的旧 BIOS 引导协议。此类内核在启动前必须从其加载位置复制到 2MB。`copy_staging` 命令用于为旧内核启用此复制。它接受单个参数，可以是以下之一：

**`disable`** 强制禁用将暂存区复制到 2MB 地址。

**`enable`** 强制启用将暂存区复制到 2MB 地址。

**`auto`** 根据内核从非 2MB 物理基址引导的能力来选择行为。内核通过导出符号 `kernphys` 来报告此能力。

Arm64 加载器从一开始就在“nocopy”模式下运行，因此该平台上没有 `copy_staging` 命令。Riscv、32 位 arm 和 arm64 一直在任何 2MB 对齐的位置加载，因此不提供 `copy_staging`。

> **注意。**
> i386 和 amd64 上的 BIOS 加载器将暂存区起始地址放在物理地址 2MB 处，然后为低 1GB 启用具有相同映射的分页。`loader.efi` 的初始移植遵循了相同的方案来将控制权移交给内核，因为这样可以避免修改 loader/内核交接协议和内核页表引导。这种方法与 UEFI 规范不兼容，并且在实际中在许多主板上引起问题，因为 UEFI 固件可以自由地为其自身需求使用任何内存。像 `loader.efi` 这样的应用程序只能使用通过引导接口显式分配的内存。原始方式还可能破坏 UEFI 运行时接口数据。最终，`loader.efi` 和内核都得到了改进以避免此问题。

### amd64 故障

由于在 64 位长模式下执行，amd64 版本的 `loader.efi` 容易因程序员错误和内存损坏而发生 CPU 故障。为了便于调试此类故障，amd64 `loader.efi` 可以提供故障发生时 CPU 状态的详细报告。

`grab_faults` 命令直接在 IDT 中安装故障处理程序，避免使用 UEFI 调试接口 `EFI_DEBUG_SUPPORT_PROTOCOL.RegisterExceptionCallback()`。该接口保留给 UEFI 环境中的高级调试器使用。`ungrab_faults` 命令尝试卸载故障处理程序，将 TSS 和 IDT CPU 表恢复到安装前的状态。`fault` 命令通过执行 `ud2` 处理器指令，在 `loader.efi` 环境中产生一个故障用于测试目的。

### amd64 机器上的 i386 固件

某些设备具有支持 64 位（长模式）的 CPU，但配备了 32 位（保护模式）UEFI 实现。为这类设备提供了 **`/boot/loader_ia32.efi`**。它会在执行内核之前切换到长模式。请注意，由于固件期望其运行时 EFI 函数在 32 位保护模式下执行，因此 EFI 运行时服务对内核不可用。这意味着像 efibootmgr(8) 这样的程序将无法工作。

## 文件

**`/boot/loader.efi`** 系统中 UEFI 内核加载器的位置。

### EFI 系统分区

`loader.efi` 安装在 ESP（EFI 系统分区）上的以下位置之一：

**`efi/boot/bootXXX.efi`** 任何 EFI 加载器的默认位置（有关替换 `XXX` 的值，请参见uefi(8)）。

**`efi/freebsd/loader.efi`** 专门为 FreeBSD EFI 加载器保留的位置。

ESP 挂载点的默认位置记录在hier(7)中。

## 实例

### 在 ESP 上更新 loader.efi

以下示例展示如何在 ESP 上安装新的 `loader.efi`。由于安装、设置和情况的多样性，确切的位置比较复杂。在本节中，全小写的路径是 Unix 路径。全大写的路径是相对于 ESP 挂载点的路径，但在你的系统上可能显示为小写，因为 ESP 的 FAT 文件系统不区分大小写。

找到 ESP，它有自己“efi”的分区类型：

```sh
# gpart show nda0
=>        40  7501476448  nda0  GPT  (3.5T)
          40      614400     1  efi  (300M)
      614440  7500862048     2  freebsd-zfs  (3.5T)
```

此系统上的 ESP 名称为 `nda0p1`。默认情况下，它将挂载到 **`/boot/efi`**。检查：

```sh
# mount | grep nda0p1
/dev/nda0p1 on /boot/efi (msdosfs, local)
```

如果未挂载，则需要挂载它：

```sh
# mount -t msdosfs /dev/nda0p1 /boot/efi
```

efibootmgr(8) 报告我们引导来源。

```sh
# efibootmgr -v
Boot to FW : false
BootCurrent: 0001
Timeout    : 2 seconds
BootOrder  : 0000, 0001, 0003, 0004, 0005, 0006, 0001, 0008, 000A, 000B, 000C, 000E, 0007
...
+Boot0001* FreeBSD ZPOOL HD(1,GPT,b5d0f86b-265d-1e1b-18aa-0ed55e1e73bd,0x28,0x96000)/File(\eEFI\eFREEBSDeLOADER.EFI)
                            nda0p1:/EFI/FREEBSD/LOADER.EFI /boot/efi//EFI/FREEBSD/LOADER.EFI
...
```

根据 BIOS 的不同，通常有多个选项。我们用于引导的条目在行首以“+”标记，如上所示。因此，在这种情况下，此固件使用 ESP 上的 **`/EFI/FREEBSD/LOADER.EFI`**。通常它是 UEFI“默认”加载器，因架构而异。

| **架构** | **默认路径** |
| --- | --- |
| amd64 | `/EFI/BOOT/BOOTX64.EFI` |
| arm | `/EFI/BOOT/BOOTARM.EFI` |
| arm64 | `/EFI/BOOT/BOOTAA64.EFI` |
| i386 | `/EFI/BOOT/BOOTIA32.EFI` |
| riscv | `/EFI/BOOT/BOOTRISCV64.EFI` |

但是，必须小心：某些多重引导环境依赖于特殊的 `bootXXX.efi` 才能工作。在更新 `bootXXX.efi` 文件之前，请确保它是 FreeBSD 引导加载器：

```sh
# strings /boot/efi/EFI/BOOT/BOOTX64.EFI | grep FreeBSD | grep EFI
FreeBSD/amd64 EFI loader, Revision 3.0
```

如果之前没有默认加载器，bsdinstall(8) 会将 `loader.efi` 复制为默认名称。在更新之前，请检查它们是否是相同的副本（使用上表替换 X64）：

```sh
# cmp /boot/efi/EFI/FREEBSD/LOADER.EFI /boot/efi/EFI/BOOT/BOOTX64.EFI
```

复制加载器：

```sh
# cp /boot/loader.efi /boot/efi/EFI/FREEBSD/LOADER.EFI
```

将示例中的全大写部分替换为正确的路径。

如果 ESP 路径是 **`/FREEBSD/LOADER.EFI`**，并且在 cmp 步骤中 LOADER.EFI 和 BOOTX64.EFI 相同，则将加载器复制到默认位置：

```sh
# cp /boot/loader.efi /boot/efi/EFI/BOOT/BOOTX64.EFI
```

最后，如果你挂载了 ESP，可能希望卸载它。

```sh
# umount /boot/efi
```

## 参见

[loader(8)](loader.8.md), [uefi(8)](uefi.8.md)

## 缺陷

非 x86 串口控制台的处理更加混乱，文档也更少。

有时当未设置串口速度时，使用 9600。其他时候结果通常是 115200，因为速度保持默认值不变。

U-Boot 实现了 UEFI 标准的子集。某些版本不支持获取 loader 变量，因此 `efibootmgr` 可能无法工作。此外，`efibootmgr` 在 armv7 或 riscv 上不受支持。在这些情况下，用户必须了解引导的是什么才能正确更新它（在大多数情况下，它将是 FreeBSD 路径和 UEFI 默认值，因此如果有加载器，只需将 loader.efi 复制到那里即可）。通常在这些嵌入式情况下，只有一个 `.efi` 文件（`loader.efi` 或 `loader.efi` 的副本）。此文件的路径通常是上面的默认可移动路径。

在 UEFI 上管理多重操作系统引导差异很大，因此在更新 UEFI 默认加载器时需要格外小心。
