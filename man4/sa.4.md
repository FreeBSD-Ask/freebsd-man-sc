# sa(4)

`sa` — SCSI 顺序访问设备驱动

## 名称

`sa`

## 概要

`device sa`

## 描述

`sa` 驱动为通过受支持的 SCSI 主机适配器连接到系统的所有顺序访问类 SCSI 设备提供支持。顺序访问类包括磁带和其他线性访问设备。

在配置 SCSI 顺序访问设备之前，还必须单独将 SCSI 主机适配器配置到系统中。

## 挂载会话

`sa` 驱动基于“*mount session*”（挂载会话）的概念，即从磁带挂载到卸载之间的时间段。在挂载会话期间设置的任何参数在该会话的剩余时间内保持有效，直到替换。可通过多种方式卸载磁带，从而结束会话。这些方式包括：

- 关闭“rewind device”（回卷设备），下文称为子模式 00。例如 **`/dev/sa0`**。
- 使用 MTOFFL ioctl(2) 命令，可通过 mt(1) 的‘`offline`’命令调用。

应注意，磁带设备是独占打开设备，但打开控制模式设备的情况除外。在后一种情况下，仅在需要时（例如设置参数）才寻求独占访问。

## 子模式

子模式在设备关闭时采取的操作不同：

**`/dev/sa*`** 关闭将回卷设备；如果磁带已写入，则在请求回卷之前将写入一个文件标记。设备被卸载。

**`/dev/nsa*`** 关闭将保持磁带挂载。如果磁带已写入，将写入一个文件标记。不进行其他磁头定位。任何后续的读或写将直接在上次读取或写入的文件标记之后进行。

**`/dev/esa*`** 关闭将回卷设备。如果磁带已写入，则在请求回卷之前将写入一个文件标记。回卷完成后将发出卸载命令。设备被卸载。

## 块模式

SCSI 磁带可运行在‘*variable*’（可变）或‘*fixed*’（固定）块大小模式下。大多数 QIC 类型设备以固定块大小模式运行，而大多数九轨磁带和许多新磁带格式允许可变块大小。两者区别如下：

**可变**块大小：对设备的每次写入都生成一条写入磁带的逻辑记录。无法从磁带读取或写入记录的 *part*（部分）（但可以请求更大的块并读取较小的记录）；也不能读取多个块。因此，单次写入的数据由单次读取来读取。所使用的块大小可以是设备、SCSI 适配器和系统支持的任何值（通常在 1 字节到 64 KB 之间，有时更大）。从磁带读取可变记录/块时，磁头逻辑上位于上次读取项之后、下一项之前。如果下一项是文件标记但从未读取，则下一个读取的进程将立即遇到文件标记并收到文件结束通知。

**固定**块大小：用户写入的数据作为一系列固定大小的块传递给磁带。它在内存中可能是连续的，但被视为一系列独立的块。不能写入数据量不是块大小精确倍数的数据。可以以不同的记录集读取和写入相同数据。换言之，一起写入的块可以分开读取，反之亦然。如果请求的块数多于文件中剩余的块数，驱动器将遇到文件标记。由于有部分数据要返回（除非文件标记之前没有记录），读取将成功并返回该数据。下次读取将立即返回值 0。（如上所述，如果文件标记从未读取，则在非回卷模式下它将保留给下一个进程读取。）

## 块大小

默认情况下，驱动不接受超过单次写入或读取请求可处理大小的、对磁带设备的读取或写入操作。因此，应用程序作者可以确信其设定的磁带写入块大小会被遵守。例如，如果用户尝试向磁带写入 256KB 的块，但控制器最多只能处理 128KB，则写入将失败。FreeBSD 10.0 之前的 FreeBSD 行为是将大型读取或写入拆分为更小的块再写入磁带。但此行为的问题在于，至少在可变块模式下，它对应用程序作者隐藏了实际的磁带块大小。

如果用户希望将大型读取和写入拆分为单独的部分，可以设置以下加载器可调参数。请注意，这些可调参数在 FreeBSD 11.0 中将移除。它们仅用于过渡目的。

**kern.cam.sa.allow_io_split** 此变量设置为 1 时，将配置所有 `sa` 设备在需要时将大型缓冲区拆分为较小的部分。

**kern.cam.sa.%d.allow_io_split** 此变量设置为 1 时，将配置给定的 `sa` 单元将大型缓冲区拆分为多个部分。如果存在全局设置，这将覆盖全局设置。

有多个 [sysctl(8)](../man8/sysctl.8.md) 变量可用于查看块处理参数：

**kern.cam.sa.%d.allow_io_split** 此变量允许用户查看但不能修改当前的 I/O 拆分设置。不允许用户修改此设置，以确保在磁带挂载期间应用程序的行为不会发生变化。

**kern.cam.sa.%d.maxio** 此变量显示由内核调优参数（MAXPHYS、DFLTPHYS）和连接到磁带驱动器的控制器能力组合所允许的最大 I/O 大小（以字节为单位）。应用程序可参考此值了解可能允许的最大 I/O 大小，但应记住实际最大值可能受到磁带驱动器通过 SCSI READ BLOCK LIMITS 命令的进一步限制。

**kern.cam.sa.%d.cpi_maxio** 此变量显示通过 CAM Path Inquiry CCB（XPT_PATH_INQ）报告的控制器支持的最大 I/O 大小（以字节为单位）。如果为 0，则表示控制器未报告最大 I/O 大小。

## 文件标记处理

写入时文件标记的处理是自动的。如果用户已写入磁带，并且自上次写入以来未进行读取，则在设备关闭时会向磁带写入文件标记。如果在写入后请求回卷，则驱动假定磁带上的最后一个文件已写入，并确保向磁带写入两个文件标记。例外情况是，似乎存在一个标准（我们遵循但不理解原因），某些类型的磁带实际上不向磁带写入两个文件标记，但在读取时，当读取最后一个文件时报告一个“phantom”（幻影）文件标记。这些设备包括 QIC 系列设备。（可能此设备集与固定块设备集相同。这一点尚未确定，目前驱动将它们视为独立的行为。）

## 参数

`sa` 驱动支持多个参数。用户可以使用“mt param -l”（使用 `MTIOCPARAMGET` ioctl）查询参数，并使用“mt param -s”（使用 `MTIOCPARAMSET` ioctl）设置参数。有关接口的更多细节，参见 mt(1) 和 [mtio(4)](mtio.4.md)。

支持的参数：

**0** 无保护。

**1** Reed-Solomon CRC，长度 4 字节。

**2** CRC32C，长度 4 字节。

**sili** 默认为 0。设置为 1 时，它在磁带读取时设置 Suppress Incorrect Length Indicator（SILI）位。当应用程序读取的块长度与所请求数据量不同时，磁带驱动器通常返回检测数据（包含残差）。SILI 位在大多数情况下抑制该通知。更多信息参见 SSC-5 规范（可从 t10.org 获取），特别是 READ(6) 命令一节。

**eot_warn** 默认为 0。默认情况下，`sa` 驱动通过返回写入 0 字节的写入操作并将 `errno` 设置为 0 来报告进入 Programmable Early Warning、Early Warning 和 End of Media 状态。如果 `eot_warn` 设置为 1，`sa` 驱动将在进入任何空间不足状态时将 `errno` 设置为 `ENOSPC`。

**protection.protection_supported** 这是只读参数，如果磁带驱动器支持保护信息则设置为 1。

**protection.prot_method** 如果支持保护，将其设置为磁带驱动器支持的所需保护方法。截至 SSC-5r03（可从 t10.org 获取），保护方法值为：

**protection.pi_length** 保护信息的长度，长度见上文。

**protection.lbp_w** 设置为 1 时，在写入时启用逻辑块保护。CRC 必须附加到写入磁带驱动器的块末尾。磁带驱动器在收到块时将验证 CRC。

**protection.lbp_r** 设置为 1 时，在读取时启用逻辑块保护。CRC 将附加到从磁带驱动器读取的块末尾。应用程序在收到块时应验证 CRC。

**protection.rdbp** 设置为 1 时，在 RECOVER BUFFERED DATA 命令上启用逻辑块保护。`sa` 驱动当前不使用 RECOVER BUFFERED DATA 命令。

## 超时

`sa` 驱动有一组 SCSI 命令（READ、WRITE、TEST UNIT READY 等）的默认超时，在大多数情况下对许多磁带驱动器都适用。

对于声称支持 SPC-4 标准（SCSI Primary Commands 4）或更高标准的新磁带驱动器，`sa` 驱动将尝试使用 REPORT SUPPORTED OPERATION CODES 命令从驱动器获取超时描述符。如果驱动器确实报告了超时描述符，`sa` 驱动将使用驱动器推荐的命令超时。

使用中的超时通过 `kern.cam.sa.%d.timeout.*` [sysctl(8)](../man8/sysctl.8.md) 变量以**千分之一秒**为单位报告。

要覆盖默认超时或驱动器推荐的超时，可以设置两组加载器可调值之一。如果你有支持 REPORT SUPPORTED OPERATION CODES 超时描述符的驱动器（参见 [camcontrol(8)](../man8/camcontrol.8.md) `opcodes` 子命令），通常最好使用这些值。全局 `kern.cam.sa.timeout.*` 值将覆盖所有 `sa` 驱动实例的超时。如果系统中有 5 个磁带驱动器，它们都将获得相同的超时。`kern.cam.sa.%d.timeout.*` 值（其中 %d 是数字 `sa` 实例号）将覆盖全局超时，以及默认超时或驱动器推荐的超时。

要在引导后设置超时，每个实例的超时值（例如 `kern.cam.sa.0.timeout.read`）可作为 sysctl 变量使用。

如果磁带驱动器在引导后到达，将使用适用于新到达驱动器的全局可调参数或每实例可调参数。

加载器可调参数：

**kern.cam.sa.timeout.erase**
**kern.cam.sa.timeout.locate**
**kern.cam.sa.timeout.mode_select**
**kern.cam.sa.timeout.mode_sense**
**kern.cam.sa.timeout.prevent**
**kern.cam.sa.timeout.read**
**kern.cam.sa.timeout.read_position**
**kern.cam.sa.timeout.read_block_limits**
**kern.cam.sa.timeout.report_density**
**kern.cam.sa.timeout.reserve**
**kern.cam.sa.timeout.rewind**
**kern.cam.sa.timeout.space**
**kern.cam.sa.timeout.tur**
**kern.cam.sa.timeout.write**
**kern.cam.sa.timeout.write_filemarks**

加载器可调值和 [sysctl(8)](../man8/sysctl.8.md) 值：

**kern.cam.sa.%d.timeout.erase**
**kern.cam.sa.%d.timeout.locate**
**kern.cam.sa.%d.timeout.mode_select**
**kern.cam.sa.%d.timeout.mode_sense**
**kern.cam.sa.%d.timeout.prevent**
**kern.cam.sa.%d.timeout.read**
**kern.cam.sa.%d.timeout.read_position**
**kern.cam.sa.%d.timeout.read_block_limits**
**kern.cam.sa.%d.timeout.report_density**
**kern.cam.sa.%d.timeout.reserve**
**kern.cam.sa.%d.timeout.rewind**
**kern.cam.sa.%d.timeout.space**
**kern.cam.sa.%d.timeout.tur**
**kern.cam.sa.%d.timeout.write**
**kern.cam.sa.%d.timeout.write_filemarks**

如上所述，超时以**千分之一秒**为单位设置和报告，因此在设置时务必注意这一点。

## IOCTL

`sa` 驱动支持 [mtio(4)](mtio.4.md) 的所有 ioctl。

## 文件

**`/dev/[n][e]sa[0-9]`** 通用形式：
**`/dev/sa0`** 关闭时回卷
**`/dev/nsa0`** 关闭时不回卷
**`/dev/esa0`** 关闭时弹出（如果支持）
**`/dev/sa0.ctl`** 控制模式设备（用于在另一程序访问设备时检查状态等）。

## 诊断

`sa` 驱动支持注入 End Of Media（EOM）通知以辅助应用程序开发和测试。EOM 通过返回写入 0 字节的读取或写入来向应用程序指示。此外，当注入 EOM 时，磁带位置状态将临时显示 Beyond of the Programmable Early Warning（BPEW）状态。要查看 BPEW 状态，请使用 `MTIOCEXTGET` ioctl，该 ioctl 由“mt status”命令使用。要注入 EOM 通知，请将

`kern.cam.sa.%d.inject_eom`

sysctl 变量设置为 1。驱动将发送一次 EOM 通知，设置一次 BPEW 状态的位置查询，然后驱动状态将重置为正常。

## 参见

mt(1), cam(4), [mtio(4)](mtio.4.md)

## 作者

`sa` 驱动由 Justin T. Gibbs 和 Kenneth Merry 为 CAM SCSI 子系统编写。许多想法来自 Julian Elischer 编写并从 Mach 2.5 移植的 `st` 设备驱动。

多年来的记录所有者是 Matthew Jacob。当前维护者是 Kenneth Merry

## 缺陷

此驱动缺少处理旧设备所需的许多 hack。许多旧的 SCSI-1 设备可能无法在此驱动下正常工作。

此外，在 FreeBSD 2.X 下写入的某些磁带（主要是 QIC 磁带）无法用此驱动自动正确读取：可能需要显式设置可变块模式或设置为最适合你设备的块大小，才能读取在 FreeBSD 2.X 下写入的磁带。

分区仅支持状态信息和定位。添加创建和编辑磁带分区的支持会更好。
