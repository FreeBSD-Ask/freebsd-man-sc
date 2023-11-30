  CAMCONTROL(8)  

CAMCONTROL(8)

FreeBSD System Manager's Manual

CAMCONTROL(8)

[名称](#__u540D___u79F0_)
=======================

`camcontrol` —

CAM 控制程序

[概要](#__u6982___u8981_)
=======================

`camcontrol` ⟨command⟩ \[device id\] \[generic args\] \[command args\] `camcontrol` `devlist` \[`-b`\] \[`-v`\] `camcontrol` `periphlist` \[device id\] \[`-n` dev\_name\] \[`-u` unit\_number\] `camcontrol` `tur` \[device id\] \[generic args\] `camcontrol` `inquiry` \[device id\] \[generic args\] \[`-D`\] \[`-S`\] \[`-R`\] `camcontrol` `identify` \[device id\] \[generic args\] \[`-v`\] `camcontrol` `reportluns` \[device id\] \[generic args\] \[`-c`\] \[`-l`\] \[`-r` reporttype\] `camcontrol` `readcap` \[device id\] \[generic args\] \[`-b`\] \[`-h`\] \[`-H`\] \[`-l`\] \[`-N`\] \[`-q`\] \[`-s`\] `camcontrol` `start` \[device id\] \[generic args\] `camcontrol` `stop` \[device id\] \[generic args\] `camcontrol` `load` \[device id\] \[generic args\] `camcontrol` `eject` \[device id\] \[generic args\] `camcontrol` `reprobe` \[device id\] `camcontrol` `rescan` ⟨all | device id | bus\[:target:lun\]⟩ `camcontrol` `reset` ⟨all | device id | bus\[:target:lun\]⟩ `camcontrol` `defects` \[device id\] \[generic args\] ⟨`-f` format⟩ \[`-P`\] \[`-G`\] \[`-q`\] \[`-s`\] \[`-S` offset\] \[`-X`\] `camcontrol` `modepage` \[device id\] \[generic args\] \[`-6`\] ⟨`-m` page\[,subpage\] | `-l`⟩ \[`-P` pgctl\] \[`-D`\] \[`-L`\] \[`-b` | `-e`\] \[`-d`\] `camcontrol` `cmd` \[device id\] \[generic args\] ⟨`-a` cmd \[args\]⟩ ⟨`-c` cmd \[args\]⟩ \[`-d`\] \[`-f`\] \[`-i` len fmt\] \[`-o` len fmt \[args\]\] \[`-r` fmt\] `camcontrol` `smpcmd` \[device id\] \[generic args\] ⟨`-r` len fmt \[args\]⟩ ⟨`-R` len fmt \[args\]⟩ `camcontrol` `smprg` \[device id\] \[generic args\] \[`-l`\] `camcontrol` `smppc` \[device id\] \[generic args\] ⟨`-p` phy⟩ \[`-l`\] \[`-o` operation\] \[`-d` name\] \[`-m` rate\] \[`-M` rate\] \[`-T` pp\_timeout\] \[`-a` enable|disable\] \[`-A` enable|disable\] \[`-s` enable|disable\] \[`-S` enable|disable\] `camcontrol` `smpphylist` \[device id\] \[generic args\] \[`-l`\] \[`-q`\] `camcontrol` `smpmaninfo` \[device id\] \[generic args\] \[`-l`\] `camcontrol` `debug` \[`-I`\] \[`-P`\] \[`-T`\] \[`-S`\] \[`-X`\] \[`-c`\] \[`-p`\] ⟨all | off | device id | bus\[:target\[:lun\]\]⟩ `camcontrol` `tags` \[device id\] \[generic args\] \[`-N` tags\] \[`-q`\] \[`-v`\] `camcontrol` `negotiate` \[device id\] \[generic args\] \[`-c`\] \[`-D` enable|disable\] \[`-M` mode\] \[`-O` offset\] \[`-q`\] \[`-R` syncrate\] \[`-T` enable|disable\] \[`-U`\] \[`-W` bus\_width\] \[`-v`\] `camcontrol` `format` \[device id\] \[generic args\] \[`-q`\] \[`-r`\] \[`-w`\] \[`-y`\] `camcontrol` `sanitize` \[device id\] \[generic args\] ⟨`-a` overwrite | block | crypto | exitfailure⟩ \[`-c` passes\] \[`-I`\] \[`-P` pattern\] \[`-q`\] \[`-U`\] \[`-r`\] \[`-w`\] \[`-y`\] `camcontrol` `idle` \[device id\] \[generic args\] \[`-t` time\] `camcontrol` `standby` \[device id\] \[generic args\] \[`-t` time\] `camcontrol` `sleep` \[device id\] \[generic args\] `camcontrol` `powermode` \[device id\] \[generic args\] `camcontrol` `apm` \[device id\] \[generic args\] \[`-l` level\] `camcontrol` `aam` \[device id\] \[generic args\] \[`-l` level\] `camcontrol` `fwdownload` \[device id\] \[generic args\] ⟨`-f` fw\_image⟩ \[`-q`\] \[`-s`\] \[`-y`\] `camcontrol` `security` \[device id\] \[generic args\] \[`-d` pwd\] \[`-e` pwd\] \[`-f`\] \[`-h` pwd\] \[`-k` pwd\] \[`-l` high|maximum\] \[`-q`\] \[`-s` pwd\] \[`-T` timeout\] \[`-U` user|master\] \[`-y`\] `camcontrol` `hpa` \[device id\] \[generic args\] \[`-f`\] \[`-l`\] \[`-P`\] \[`-p` pwd\] \[`-q`\] \[`-s` max\_sectors\] \[`-U` pwd\] \[`-y`\] `camcontrol` `ama` \[device id\] \[generic args\] \[`-f`\] \[`-q`\] \[`-s` max\_sectors\] `camcontrol` `persist` \[device id\] \[generic args\] ⟨`-i` action | `-o` action⟩ \[`-a`\] \[`-I` trans\_id\] \[`-k` key\] \[`-K` sa\_key\] \[`-p`\] \[`-R` rel\_tgt\_port\] \[`-s` scope\] \[`-S`\] \[`-T` res\_type\] \[`-U`\] `camcontrol` `attrib` \[device id\] \[generic args\] ⟨`-r` action | `-w` attrib⟩ \[`-a` attr\_num\] \[`-c`\] \[`-e` elem\_addr\] \[`-F` form1,form2\] \[`-p` part\] \[`-s` start\_addr\] \[`-T` elem\_type\] \[`-V` lv\_num\] `camcontrol` `opcodes` \[device id\] \[generic args\] \[`-o` opcode\] \[`-s` service\_action\] \[`-N`\] \[`-T`\] `camcontrol` `zone` ⟨`-c` cmd⟩ \[`-a`\] \[`-l` lba\] \[`-o` rep\_opts\] \[`-P` print\_opts\] `camcontrol` `epc` ⟨`-c` cmd⟩ \[`-d`\] \[`-D`\] \[`-e`\] \[`-H`\] \[`-p` power\_cond\] \[`-P`\] \[`-r` restore\_src\] \[`-s`\] \[`-S` power\_src\] \[`-T` timer\] `camcontrol` `timestamp` \[device id\] \[generic args\] ⟨`-r` \[`-f` format | `-m` | `-U`\] | `-s` ⟨`-f` format `-T` time | `-U`⟩⟩ `camcontrol` `devtype` \[device id\] `camcontrol` `help`

[描述](#__u63CF___u8FF0_)
=======================

`camcontrol` 实用程序旨在为用户提供一种访问和控制 FreeBSD CAM 子系统的方法。

如果使用不当， `camcontrol` 实用程序可能会导致数据丢失和/或系统崩溃。 即使是专家用户，在使用此命令时也应谨慎行事。 新手用户应远离此实用程序。

`camcontrol` 实用程序具有许多主要功能，其中许多功能支持可选的设备标识符。 设备标识符可以采用以下三种形式之一：

deviceUNIT

指定设备名称和单元编号组合，如 "da5" 或 "cd3"。

bus:target

指定总线编号和目标 ID。 总线编号可以从 “camcontrol devlist” 的输出中确定。 lun 默认为 0。

bus:target:lun

指定设备的总线、目标和 lun。（例如 1:2:0）

设备标识符（如果已指定） _must_ 紧跟在函数名之后，并且在任何通用或特定于函数的参数之前。 请注意，下面描述的 `-n` 和 `-u` 参数将覆盖预先指定的任何设备名称或单元编号。 但是， `-n` 和 `-u` 参数 _not_ 覆盖指定的 bus:target 或 bus:target:lun 。

大多数 `camcontrol` 主要函数都支持这些通用参数：

[`-C`](#C) count

SCSI 命令重试计数。 为了使其工作，必须打开错误恢复 (`-E`) 。

[`-E`](#E)

指示内核对给定命令执行通用 SCSI 错误恢复。 这是为了遵守重试计数 (`-C`) 所必需的。除了重试命令之外，代码中的一般错误恢复通常会尝试启动未旋转的驱动器。 它可能会采取一些其他行动，具体取决于从命令返回的感知代码。

[`-n`](#n) dev\_name

指定要操作的设备类型，例如 "da"、 "cd"。

[`-Q`](#Q) task\_attr

SCSI 命令的 SCSI 任务属性（如果它是 SCSI 命令）。 这可能是有序的、简单的、头部的或 aca。 在大多数情况下，这不是必需的。 默认设置是简单的，适用于所有 SCSI 设备。 任务属性也可以用数字指定。

[`-t`](#t) timeout

SCSI 命令超时（以秒为单位）。 这会覆盖任何给定命令的默认超时。

[`-u`](#u) unit\_number

指定设备单元号，例如 "1"、 "5"。

[`-v`](#v)

详细一点，打印出失败的 SCSI 命令的感知信息。

主要命令功能：

[`devlist`](#devlist)

列出连接到 CAM 子系统的所有物理设备（逻辑单元）。 这还包括附加到每个设备的外围驱动程序列表。 使用 `-v` 参数，还会打印 SCSI 总线号、适配器名称和单元号。 另一方面，使用 `-b` 参数时，将仅打印总线适配器和单元信息，而将省略设备信息。

[`periphlist`](#periphlist)

列出连接到给定物理设备（逻辑单元）的所有外围驱动程序。

[`tur`](#tur)

将 SCSI 测试单元就绪 (0x00) 命令发送到给定设备。 `camcontrol` 实用程序将报告设备是否准备就绪。

[`inquiry`](#inquiry)

向设备发送 SCSI 查询命令 (0x12)。 默认情况下， `camcontrol` 会打印出标准查询数据、设备序列号和传输速率信息。 用户可以指定只打印某些类型的查询数据：

[`-D`](#D)

获取标准查询数据。

[`-S`](#S)

打印出序列号。 如果此标志是唯一指定的标志，则 `camcontrol` 不会在驱动器返回的值之前打印出 "Serial Number" 。 这是为了帮助编写脚本。

[`-R`](#R)

打印传输率信息。

[`identify`](#identify)

向设备发送 ATA 识别命令 (0xec)。

[`reportluns`](#reportluns)

将 SCSI REPORT LUNS (0xA0) 命令发送到给定设备。 默认情况下， `camcontrol` 将打印出目标设备支持的逻辑单元 (LUN) 列表。 有几个选项可以修改输出：

[`-c`](#c)

只需打印出 LUN 的计数，而不是实际的 LUN 编号。

[`-l`](#l)

只需打印 LUN，不要打印计数。

[`-r`](#r) reporttype

指定要从目标请求的报告类型：

default

返回默认报告。 这是 `camcontrol` 默认值。 如果支持 REPORT LUNS 命令，大多数目标将支持此报告。

wellknown

仅返回众所周知的 LUN。

all

返回所有可用的 LUN。

`camcontrol`-
将尝试以合理的格式打印出 LUN 编号。 它可以理解外围、平面、LUN 和扩展 LUN 格式。

[`readcap`](#readcap)

将 SCSI READ CAPACITY 命令发送到给定设备并显示结果。 如果设备大于 2TB，将发送 SCSI READ CAPACITY (16) 服务操作以获取设备的完整大小。 默认情况下， `camcontrol` 将打印出设备的最后一个逻辑块，以及设备的块大小（以字节为单位）。 要修改输出格式，请使用以下选项：

[`-b`](#b)

只需打印块大小，而不是最后一个块或设备大小。 这不能与 `-N` 或 `-s` 一起使用。

[`-h`](#h)

以人类可读（base 2, 1K == 1024）格式打印出设备大小。 这意味着 `-N` 并且不能与 `-q` 或 `-b` 一起使用。

[`-H`](#H)

以人类可读（base 10, 1K == 1000）格式打印出设备大小。

[`-l`](#l_2)

跳过发送 SCSI READ CAPACITY (10) 命令。 仅发送 SCSI READ CAPACITY (16) 服务操作并报告其结果。 当两者不匹配时，需要一个怪癖来解决歧义。

[`-N`](#N)

打印出设备中的块数，而不是最后一个逻辑块。

[`-q`](#q)

安静，仅打印数字（如果未指定 `-b` 或 `-s` ，则以逗号分隔）。

[`-s`](#s)

仅打印最后一个逻辑块或设备的大小，并省略块大小。

请注意，此命令仅显示信息，不会更新内核数据结构。 使用 `camcontrol` 子命令来执行此操作。

[`start`](#start)

将 SCSI 启动/停止单元 (0x1B) 命令发送到设置了启动位的给定设备。

[`stop`](#stop)

将 SCSI 启动/停止单元 (0x1B) 命令发送到指定设备，并清除启动位。

[`load`](#load)

将 SCSI 启动/停止单元 (0x1B) 命令发送到设置了启动位和加载/弹出位的给定设备。

[`eject`](#eject)

将 SCSI 启动/停止单元 (0x1B) 命令发送到给定设备，清除启动位并设置加载/弹出位。

[`rescan`](#rescan)

告诉内核扫描系统中的所有总线（使用 all 参数）、给定总线 (XPT\_SCAN\_BUS)、bus:target:lun 或设备 (XPT\_SCAN\_LUN) 以查找新设备或已消失的设备。 用户可以指定扫描所有总线、单个总线或 lun。 不支持扫描目标上的所有 lun。

如果设备由外设名称和单元编号指定，例如 da4，则仅当该设备当前存在于 CAM EDT（现有设备表）中时才可以重新扫描。 如果设备不再存在（请参阅 `camcontrol` devlist ），您必须使用 bus:target:lun 形式重新扫描它。

[`reprobe`](#reprobe)

告诉内核刷新设备信息并通知上层， GEOM(4) 。 这包括发送 SCSI READ CAPACITY 命令和更新对系统其余部分可见的磁盘大小。

[`reset`](#reset)

告诉内核通过为该总线发出 SCSI 总线重置来重置系统中的所有总线（使用 all 参数）、给定总线 (XPT\_RESET\_BUS)，或者重置给定的 bus:target:lun 或设备 (XPT\_RESET\_DEV)，通常通过在连接到该设备后发出 BUS DEVICE RESET 消息。 请注意，这可能会对系统产生破坏性影响。

[`defects`](#defects)

向给定设备发送 SCSI READ DEFECT DATA (10) 命令 (0x37) 或 SCSI READ DEFECT DATA (12) 命令 (0xB7)，并打印出以下任意组合：缺陷总数、主要缺陷列表 (PLIST) ) 和增长缺陷列表 (GLIST)。

[`-f`](#f) format

指定缺陷列表的请求格式。 格式参数是必需的。 大多数驱动器都支持物理扇区格式。 一些驱动器支持逻辑块格式。 许多驱动器，如果它们不支持请求的格式，则以替代格式返回数据，以及指示请求的数据格式不受支持的感知信息。 `camcontrol` 实用程序尝试检测这一点，并打印出驱动器返回的任何格式。 如果驱动器使用非标准检测代码报告它不支持请求的格式，则 `camcontrol` 可能会将错误视为未能完成请求。

格式选项是：

block

将列表打印为逻辑块。 这仅限于 32 位块大小，并且不受许多现代驱动器的支持。

longblock

将列表打印为逻辑块。 此选项使用 64 位块大小。

bfi

从索引格式打印出以字节为单位的列表。

extbfi

从索引格式中以扩展字节打印出列表。 扩展格式允许打印范围的块。

phys

以物理扇区格式打印出列表。 大多数驱动器都支持这种格式。

extphys

以扩展的物理扇区格式打印出列表。 扩展格式允许打印范围的块。

[`-G`](#G)

打印出增长的缺陷列表。 这是自磁盘出厂以来已重新映射的坏块列表。

[`-P`](#P)

打印出主要缺陷列表。 这是工厂中存在的缺陷列表。

[`-q`](#q_2)

使用 `-s` 打印状态信息时，仅打印缺陷数。

[`-s`](#s_2)

只打印缺陷数量，而不是缺陷列表。

[`-S`](#S_2) offset

在缺陷列表中指定起始偏移量。 这意味着使用 SCSI 命令，因为该命令的 10 字节版本不支持地址描述符索引字段。 并非所有驱动器都支持 12 字节命令，并且某些支持 12 字节命令的驱动器不支持地址描述符索引字段。

[`-X`](#X)

以十六进制（基数 16）形式而不是基数 10 形式打印缺陷。

如果既没有指定 `-P` 也没有指定 `-G` , `camcontrol` 将打印出驱动器返回的 READ DEFECT DATA 标头中给出的缺陷数。 如果既未请求主要缺陷列表也未请求增长缺陷列表，则某些驱动器将报告 0 缺陷。

[`modepage`](#modepage)

允许用户显示和选择性地编辑 SCSI 模式页面。 模式页面格式位于 /usr/share/misc/scsi\_modes 。 这可以通过在 `SCSI_MODES` 环境变量中指定不同的文件来覆盖。 `modepage` 命令有几个参数：

[`-6`](#6)

使用 6 字节 MODE 命令而不是默认的 10 字节。 旧设备可能不支持 10 字节 MODE 命令，而新设备可能无法使用 6 字节命令报告所有模式页面。 如果未指定，则 `camcontrol` 从 10 字节命令开始，并在出错时回退到 6 字节。

[`-d`](#d)

禁用模式感知的块描述符。

[`-D`](#D_2)

显示/编辑块描述符而不是模式页面。

[`-L`](#L)

使用长 LBA 块描述符。 允许大于 2^^32 的 LBA 数量。

[`-b`](#b_2)

以二进制格式显示模式页面数据。

[`-e`](#e)

该标志允许用户在模式页面中编辑值。 用户可以使用 `EDITOR` 环境变量指向的文本编辑器编辑模式页面值，或者通过标准输入提供模式页面值，使用与 `camcontrol` 用于显示模式页面值的相同格式。 如果 `camcontrol` 检测到标准输入是终端，则将调用编辑器。

[`-l`](#l_3)

列出所有可用的模式页面。 如果指定不止一次，还会列出子页面。

[`-m`](#m) page\[,subpage\]

这指定了用户想要查看和/或编辑的模式页面和可选子页面的编号。 除非指定了 `-l` ，否则此参数是强制性的。

[`-P`](#P_2) pgctl

这允许用户指定页面控制字段。可能的值为：

0

当前值

1

可变值

2

默认值

3

保存的值

[`cmd`](#cmd)

允许用户将任意 ATA 或 SCSI CDB 发送到任何设备。 `cmd` 函数需要 `-c` 参数来指定 SCSI CDB 或 `-a` 参数来指定 ATA 命令块寄存器值。 其他参数是可选的，具体取决于命令类型。 命令和数据规范语法记录在 cam\_cdbparse(3) 中。 注意：如果指定的 CDB 导致数据传入或传出相关 SCSI 设备，则必须指定 `-i` 或 `-o` 。

[`-a`](#a) cmd \[args\]

这指定了 12 个 ATA 命令块寄存器的内容 (command, features, lba\_low, lba\_mid, lba\_high, device, lba\_low\_exp, lba\_mid\_exp. lba\_high\_exp, features\_exp, sector\_count, sector\_count\_exp)。

[`-c`](#c_2) cmd \[args\]

这指定了 SCSI CDB。 SCSI CDB 可以是 6、10、12 或 16 字节。

[`-d`](#d_2)

指定用于 ATA 命令的 DMA 协议。

[`-f`](#f_2)

指定用于 ATA 命令的 FPDMA (NCQ) 协议。

[`-i`](#i) len fmt

这指定了要读取的数据量，以及它应该如何显示。 如果格式为 ‘-’ ，将从设备读取 len 个字节的数据并写入标准输出。

[`-o`](#o) len fmt \[args\]

这指定要写入设备的数据量以及要写入的数据。 如果格式为 ‘-’ ，将从标准输入读取 len 个字节的数据并将其写入设备。

[`-r`](#r_2) fmt

这指定应显示 11 个结果 ATA 命令块寄存器 (status, error, lba\_low, lba\_mid, lba\_high, device, lba\_low\_exp, lba\_mid\_exp, lba\_high\_exp, sector\_count, sector\_count\_exp)以及如何显示。 如果格式为 ‘-’ ，则 11 个结果寄存器将以十六进制形式写入标准输出。

[`smpcmd`](#smpcmd)

允许用户向设备发送任意串行管理协议 (SMP) 命令。 `smpcmd` 函数需要 `-r` 参数来指定要发送的 SMP 请求，以及 `-R` 参数来指定 SMP 响应的格式。 SMP 请求和响应参数的语法记录在 cam\_cdbparse(3) 中。

请注意，支持 SMP 直通的 SAS 适配器（至少是当前已知的适配器）在请求中不接受来自用户的 CRC 字节，也不在响应中将 CRC 字节传回给用户。 因此，用户不应在请求的长度中包含 CRC 字节，也不应期望在响应中返回 CRC 字节。

[`-r`](#r_3) len fmt \[args\]

这指定了 SMP 请求的大小（不包括 CRC 字节）和 SMP 请求格式。 如果格式为 ‘-’ ，将从标准输入读取 len 个字节的数据并作为 SMP 请求写入。

[`-R`](#R_2) len fmt \[args\]

这指定了为 SMP 响应分配的缓冲区大小和 SMP 响应格式。 如果格式为 ‘-’ ，将为响应分配 len 个字节的数据，并将响应写入标准输出。

[`smprg`](#smprg)

允许用户向设备发送串行管理协议 (SMP) 报告常规命令。 `camcontrol` 将显示 Report General 命令返回的数据。 如果 SMP 目标支持长响应格式，则会自动请求并显示附加数据。

[`-l`](#l_4)

仅请求长响应格式。 并非所有 SMP 目标都支持长响应格式。 此选项导致 `camcontrol` 跳过发送未设置长位的初始报告常规请求，而仅发出设置了长位的报告常规请求。

[`smppc`](#smppc)

允许用户向设备发出串行管理协议 (SMP) PHY 控制命令。 应谨慎使用此功能，因为它可能导致设备无法访问，并且还可能导致数据损坏。 `-p` 参数是指定要操作的 PHY 所必需的。

[`-p`](#p) phy

指定要操作的 PHY。 该参数是必需的。

[`-l`](#l_5)

请求长请求/响应格式。 并非所有 SMP 目标都支持长响应格式。 对于 PHY Control 命令，目前仅影响请求长度是否设置为 0 以外的值。

[`-o`](#o_2) operation

指定 PHY 控制操作。 只能指定一个 `-o` 操作。 可以用数字（十进制、十六进制或八进制）指定操作，也可以指定以下操作名称之一：

nop

无操作。 没有必要指定这个参数。

linkreset

向 phy 发送 LINK RESET 命令。

hardreset

向 phy 发送 HARD RESET 命令。

disable

向 phy 发送 DISABLE 命令。 请注意，LINK RESET 或 HARD RESET 命令应重新启用 phy。

clearerrlog

发送清除错误日志命令。 这将清除指定 phy 的错误日志计数器。

clearaffiliation

发送 CLEAR AFFILIATION 命令。 这将清除与请求清除操作的 SMP 启动器具有相同 SAS 地址的 STP 启动器端口的从属关系。

sataportsel

将 TRANSMIT SATA PORT SELECTION SIGNAL 命令发送到 phy。 这将导致 SATA 端口选择器将给定的 phy 用作其活动 phy，并使其他 phy 处于非活动状态。

clearitnl

向 PHY 发送 CLEAR STP I\_T NEXUS LOSS 命令。

setdevname

向 PHY 发送 SET ATTACHED DEVICE NAME 命令。 这需要 `-d` 参数来指定设备名称。

[`-d`](#d_3) name

指定附加的设备名称。 `-o` setdevname phy 操作需要此选项。 该名称是一个 64 位数字，可以指定为十进制、十六进制或八进制格式。

[`-m`](#m_2) rate

设置 phy 的最小物理链路速率。 这是一个数字参数。 目前已知的链接速率为：

0x0

不要改变当前值。

0x8

1.5 Gbps

0x9

3 Gbps

0xa

6 Gbps

可以为较新的物理链路速率指定其他值。

[`-M`](#M) rate

设置 phy 的最大物理链路速率。 这是一个数字参数。 有关已知的链接速率参数，请参阅 `-m` 参数说明。

[`-T`](#T) pp\_timeout

设置部分路径超时值，以微秒为单位。 有关此字段的更多信息，请参阅 ANSI SAS 协议层 (SPL) 规范。

[`-a`](#a_2) enable|disable

启用或禁用 SATA 休眠 phy 电源条件。

[`-A`](#A) enable|disable

启用或禁用 SATA 部分电源条件。

[`-s`](#s_3) enable|disable

启用或禁用 SAS 休眠物理电源条件。

[`-S`](#S_3) enable|disable

启用或禁用 SAS 部分物理电源条件。

[`smpphylist`](#smpphylist)

列出连接到 SAS 扩展器的 phy、连接到 phy 的终端设备的地址，以及该设备和连接到该设备的外围设备的查询数据。 如果可用，将显示查询数据和外围设备。

[`-l`](#l_6)

打开用于此命令的底层 SMP 命令的长响应格式。

[`-q`](#q_3)

仅打印连接到 CAM EDT（现有设备表）中设备的 phy。

[`smpmaninfo`](#smpmaninfo)

向设备发送 SMP 报告制造商信息命令并显示响应。

[`-l`](#l_7)

打开用于此命令的底层 SMP 命令的长响应格式。

[`debug`](#debug)

在内核中开启CAM调试printfs。 这需要内核配置文件中的选项CAMDEBUG。 警告：当前启用调试 printfs 会导致内核 printfs 数量过多。 一旦启动调试 printfs，您可能很难关闭它们，因为内核将忙于打印消息并且无法快速服务其他请求。 `debug` 函数接受许多参数：

[`-I`](#I)

启用 CAM\_DEBUG\_INFO printfs。

[`-P`](#P_3)

启用 CAM\_DEBUG\_PERIPH printfs。

[`-T`](#T_2)

启用 CAM\_DEBUG\_TRACE printfs。

[`-S`](#S_4)

启用 CAM\_DEBUG\_SUBTRACE printfs。

[`-X`](#X_2)

启用 CAM\_DEBUG\_XPT printfs。

[`-c`](#c_3)

启用 CAM\_DEBUG\_CDB printfs。 这将导致内核打印出发送到指定设备的 SCSI CDB。

[`-p`](#p_2)

启用 CAM\_DEBUG\_PROBE printfs。

all

为所有设备启用调试。

off

关闭所有设备的调试

bus\[:target\[:lun\]\]

打开给定总线、目标或 lun 的调试。 如果未指定 lun 或目标和 lun，则使用通配符。 （即，只需指定总线即可为该总线上的所有设备打开调试 printfs。）

[`tags`](#tags)

显示或设置我们尝试排队到特定设备的 "tagged openings" 或同时交易的数量。 默认情况下， `tags` 命令，没有特定于命令的参数（即只有通用参数）打印出可以排队到有问题的设备的 "soft" 最大事务数。 有关更多详细信息，请使用下面描述的 `-v` 参数。

[`-N`](#N_2) tags

设置给定设备的标签数量。 这必须在内核 quirk 表中设置的最小和最大数字之间。 大多数支持标记队列的设备的默认值是最少 2 个，最多 255 个。 可以使用 `-v` 开关确定给定设备的最小值和最大值。 此 `camcontrol` 子命令的 `-v` 开关的含义如下所述。

[`-q`](#q_4)

保持安静，不要报告标签数量。 这通常在设置标签数量时使用。

[`-v`](#v_2)

详细标志具有 _tags_ 参数的特殊功能。 它使 `camcontrol` 打印出 XPT\_GDEV\_TYPE CCB 的标记队列相关字段：

dev\_openings

这是排队到给定设备的事务的容量。

dev\_active

这是当前排队到设备的事务数。

devq\_openings

这是事务的内核队列空间。 此计数通常反映 dev\_openings，除非在错误恢复操作期间，当设备队列被冻结（不允许设备接收命令）、dev\_openings 的数量减少或正在发生事务重放时。

devq\_queued

这是在内核队列中等待设备容量的事务数。 除非正在进行错误恢复，否则此数字通常为零。

held

持有的计数是外围驱动程序持有的 CCB 的数量，这些 CCB 要么刚刚完成，要么即将释放到传输层以供设备服务。 持有的 CCB 在给定设备上保留容量。

mintags

这是可以一次排队到设备的当前 "hard" 最小事务数。 上面的 dev\_openings 值不能低于这个数字。 mintags 的默认值为 2，尽管对于各种设备，它可能设置得更高或更低。

maxtags

这是一次可以排队到设备的 "hard" 最大事务数。 dev\_openings 值不能超过这个数字。 maxtags 的默认值是 255，尽管它可以为各种设备设置更高或更低。

[`negotiate`](#negotiate)

显示或协商各种通信参数。 某些控制器可能不支持设置或更改其中一些值。 例如，Adaptec 174x 控制器不支持更改设备的同步速率或偏移。 如果控制器指示它不支持设置参数，则 `camcontrol` 实用程序将不会尝试设置参数。 要了解控制器支持的内容，请使用 `-v` 标志。 `negotiate` 命令的 `-v` 标志的含义如下所述。 此外，一些控制器驱动程序不支持设置协商参数，即使底层控制器支持协商更改。 一些控制器，例如 Advansys 范围的控制器，支持为设备启用和禁用同步协商，但不支持设置同步协商速率。

[`-a`](#a_3)

尝试通过向设备发送测试单元就绪命令使协商设置立即生效。

[`-c`](#c_4)

显示或设置当前协商设置。 这是默认设置。

[`-D`](#D_3) enable|disable

启用或禁用断开连接。

[`-M`](#M_2) mode

设置 ATA 模式。

[`-O`](#O) offset

设置命令延迟偏移。

[`-q`](#q_5)

保持安静，不要打印任何东西。 当您想要设置参数但不想要任何状态信息时，这通常很有用。

[`-R`](#R_3) syncrate

更改设备的同步速率。 同步速率是以 MHz 为单位指定的浮点值。 因此，例如， ‘20.000’ 是合法值， ‘20’ 也是如此。

[`-T`](#T_3) enable|disable

启用或禁用设备的标记队列。

[`-U`](#U)

显示或设置用户协商设置。 默认是显示或设置当前的协商设置。

[`-v`](#v_3)

详细开关对于 `negotiate` 子命令具有特殊含义。 它使 `camcontrol` 打印出发送到控制器驱动程序的路径查询 (XPT\_PATH\_INQ) CCB 的内容。

[`-W`](#W) bus\_width

指定与设备协商的总线宽度。 总线宽度以位为单位。 要指定的唯一有用值是 8、16 和 32 位。 控制器必须支持相关总线宽度才能使设置生效。

一般情况下，同步速率和偏移设置在向设备发送命令之前不会对设备生效。 上面的 `-a` 开关会自动向设备发送测试单元就绪，以便协商参数生效。

[`format`](#format)

向指定设备发出 SCSI FORMAT UNIT 命令。

_WARNING! WARNING! WARNING!_

低级格式化磁盘会破坏磁盘上的所有数据。 发出此命令时要格外小心。 许多用户对实际上并不需要低级格式化的磁盘进行低级格式化。 需要对磁盘进行低级格式化的情况相对较少。 低级格式化磁盘的一个原因是在更改其物理扇区大小后初始化磁盘。 对磁盘进行低级格式化的另一个原因是，如果您在响应读取和写入请求时从磁盘收到 "medium format corrupted" 错误，则需要恢复磁盘。

一些磁盘需要比其他磁盘更长的时间来格式化。用户应指定足够长的超时时间以允许格式完成。 默认格式化超时为 3 小时，对于大多数磁盘来说应该足够长。 有些硬盘会在很短的时间内（大约 5 分钟或更短）完成格式化操作。 这通常是因为驱动器并不真正支持 FORMAT UNIT 命令——它只是接受命令，等待几分钟然后返回它。

‘format’ 子命令采用几个参数来修改其默认行为。 `-q` 和 `-y` 参数对脚本很有用。

[`-q`](#q_6)

保持安静，不要打印任何状态消息。 但是，此选项不会禁用问题。 要禁用问题，请使用下面的 `-y` 参数。

[`-r`](#r_4)

以 “report only” 模式运行。 这将报告已在驱动器上运行的格式的状态。

[`-w`](#w)

发出非立即格式化命令。 默认情况下， `camcontrol` 发出带有立即位设置的 FORMAT UNIT 命令。 这告诉设备在格式化实际完成之前立即返回格式化命令。 然后， `camcontrol` 每秒从设备收集 SCSI 感知信息，以确定它在格式化过程中的进度。 如果指定了 `-w` 参数， `camcontrol` 将发出非立即格式化命令，并且无法打印任何信息让用户知道磁盘已格式化的百分比。

[`-y`](#y)

不要问任何问题。 默认情况下， `camcontrol` 会询问用户他/她是否真的要格式化相关磁盘，以及默认格式化命令超时是否可以接受。 如果在命令行上指定了超时，则不会询问用户超时。

[`sanitize`](#sanitize)

向指定设备发出 SANITIZE 命令。

_WARNING! WARNING! WARNING!_

磁盘上的所有数据都将被破坏或无法访问。 无法恢复数据。 发出此命令时要格外小心。

‘sanitize’ 子命令采用几个参数来修改其默认行为。 `-q` 和 `-y` 参数对脚本很有用。

[`-a`](#a_4) operation

指定要执行的清理操作。

overwrite

通过将用户提供的数据模式一次或多次写入设备来执行覆盖操作。 模式由 `-P` 参数给出。 次数由 `-c` 参数给出。

block

执行块擦除操作。 所有设备的块都设置为供应商定义的值，通常为零。

crypto

执行加密擦除操作。 更改加密密钥以防止数据被解密。

exitfailure

退出先前失败的清理操作。 失败的清理操作只有在无限制完成模式下运行时才能退出，如 `-U` 参数提供的那样。

[`-c`](#c_5) passes

执行 ‘overwrite’ 操作时的通过次数。 有效值介于 1 和 31 之间。 默认值为 1。

[`-I`](#I_2)

执行 ‘overwrite’ 操作时，模式在连续通过之间反转。

[`-P`](#P_4) pattern

包含执行 ‘overwrite’ 操作时要使用的模式的文件的路径。 根据需要重复该模式以填充每个块。

[`-q`](#q_7)

保持安静，不要打印任何状态消息。 但是，此选项不会禁用问题。 要禁用问题，请使用下面的 `-y` 参数。

[`-U`](#U_2)

在不受限制的完成模式下执行清理。 如果操作失败，稍后可以使用 ‘exitfailure’ 操作退出。

[`-r`](#r_5)

以 “report only” 模式运行。 这将报告已在驱动器上运行的清理程序的状态。

[`-w`](#w_2)

发出非立即清理命令。 默认情况下， `camcontrol` 发出带有立即位设置的 SANITIZE 命令。 这告诉设备在清理实际完成之前立即返回清理命令。 然后， `camcontrol` 每秒从设备收集 SCSI 感知信息，以确定它在清理过程中的进度。 如果指定了 `-w` 参数，则 `camcontrol` 将发出非立即清理命令，并且无法打印任何信息以让用户知道已清理磁盘的百分比。

[`-y`](#y_2)

不要问任何问题。 默认情况下， `camcontrol` 会询问用户他/她是否真的想要清理相关磁盘，以及默认清理命令超时是否可以接受。 如果在命令行上指定了超时，则不会询问用户超时。

[`idle`](#idle)

将 ATA 设备置于 IDLE 状态。 可选参数 (`-t`) 以秒为单位指定自动待机计时器值。 值 0 禁用计时器。

[`standby`](#standby)

将 ATA 设备置于 STANDBY 状态。 可选参数 (`-t`) 以秒为单位指定自动待机计时器值。 值 0 禁用计时器。

[`sleep`](#sleep)

将 ATA 设备置于 SLEEP 状态。 请注意，使设备脱离此状态的唯一方法可能是重置。

[`powermode`](#powermode)

报告 ATA 设备电源模式。

[`apm`](#apm)

可选参数 (`-l`) 指定、启用和设置高级电源管理级别，其中 1 - 最小功率，127 - 待机时最大性能，128 - 无待机时最小功率，254 - 最大性能。 如果未指定 - APM 被禁用。

[`aam`](#aam)

它指定可选参数 (`-l`) ，启用和设置自动声学管理级别，其中 1 - 最小噪音，254 - 最大性能。 如果未指定 - AAM 将被禁用。

[`security`](#security)

使用 ATA 识别命令 (0xec) 更新或报告安全设置。 默认情况下， `camcontrol` 将打印出设备的安全支持和相关设置。 `security` 命令有几个参数：

[`-d`](#d_4) pwd

根据设备配置的安全级别，使用给定密码为所选用户禁用设备安全性。

[`-e`](#e_2) pwd

使用所选用户的给定密码擦除设备。

_WARNING! WARNING! WARNING!_

发出安全擦除将 _ERASE_ 设备上的所有用户数据，并且可能需要几个小时才能完成。

当对 SSD 驱动器使用此命令时，其所有单元将被标记为空，将其恢复为出厂默认写入性能。 对于 SSD，此操作通常只需几秒钟。

[`-f`](#f_3)

冻结指定设备的安全配置。

命令完成后，任何其他更新设备锁定模式的命令都将被命令中止。 关机或硬件复位禁用冻结模式。

[`-h`](#h_2) pwd

增强了使用所选用户的给定密码擦除设备。

_WARNING! WARNING! WARNING!_

发出增强的安全擦除将 _ERASE_ 设备上的所有用户数据，并且可能需要几个小时才能完成。

增强型擦除将预定数据模式写入所有用户数据区域，所有先前写入的用户数据将被覆盖，包括由于重新分配而不再使用的扇区。

[`-k`](#k) pwd

根据设备配置的安全级别，使用给定密码为所选用户解锁设备。

[`-l`](#l_8) high|maximum

指定发出 `-s` pwd 命令时要设置的安全级别。 安全级别决定了使用主密码解锁设备时的设备行为。 当安全级别设置为高时，设备需要解锁命令和主密码才能解锁。 当安全级别设置为最高时，设备需要使用主密码进行安全擦除才能解锁。

此选项必须与安全操作命令之一结合使用。

默认为 _high_

[`-q`](#q_8)

保持安静，不要打印任何状态消息。 但是，此选项不会禁用问题。 要禁用问题，请使用下面的 `-y` 参数。

[`-s`](#s_4) pwd

使用所选用户的给定密码为设备设置密码（启用安全性）。 此选项可以与其他选项结合使用，例如 `-e` _pwd_

除了用户密码之外，还可以设置主密码。 主密码的目的是允许管理员建立一个对用户保密的密码，如果用户密码丢失，该密码可用于解锁设备。

_Note:_ 设置主密码不会启用设备安全性。

如果设置了主密码并且驱动器支持主修订代码功能，则主密码修订代码将递减。

[`-T`](#T_4) timeout

覆盖用于 `-e` 和 `-h` 的默认超时，以秒为单位指定，如果您的系统在正确处理长超时时遇到问题，这很有用。

通常超时是根据存储在驱动器上的信息（如果存在）计算得出的，否则默认为 2 小时。

[`-U`](#U_3) user|master

指定为运行操作命令设置/使用哪个用户，有效值为 user 或 master，如果未设置则默认为 master。

此选项必须与安全操作命令之一结合使用。

默认为 _master_

[`-y`](#y_3)

对危险选项（例如 `-e` ）确认是，而不提示确认。

如果为任何操作命令指定的密码与为指定用户配置的密码不匹配，则该命令将失败。

所有情况下的密码都限制为 32 个字符，更长的密码将失效。

[`hpa`](#hpa)

更新或报告宿主保护区的详细信息。 默认情况下， `camcontrol` 将打印出设备的 HPA 支持和相关设置。 `hpa` 命令有几个可选参数：

[`-f`](#f_4)

冻结指定设备的 HPA 配置。

命令完成后，任何其他更新 HPA 配置的命令都将被中止。 关机或硬件复位禁用冻结模式。

[`-l`](#l_9)

锁定设备的 HPA 配置，直到成功调用解锁或发生下一次上电复位。

[`-P`](#P_5)

使 HPA 最大扇区在上电复位或硬件复位期间保持不变。 这必须与 `-s` max\_sectors 结合使用

[`-p`](#p_3) pwd

设置解锁呼叫所需的 HPA 配置密码。

[`-q`](#q_9)

保持安静，不要打印任何状态消息。 此选项不会禁用问题。 要禁用问题，请使用下面的 `-y` 参数。

[`-s`](#s_5) max\_sectors

配置设备的最大用户可访问扇区。 这将更改设备报告的扇区数。

_WARNING! WARNING! WARNING!_

使用此选项更改设备的最大扇区将使设备上超出指定值的数据无法访问。

在没有上电复位或设备硬件复位的情况下，只能进行一次成功的 `-s` max\_sectors 调用。

[`-U`](#U_4) pwd

使用给定密码解锁指定设备的 HPA 配置。 如果指定的密码与通过 `-p` pwd 配置的密码不匹配，该命令将失败。

解锁呼叫失败 5 次后，由于密码不匹配，设备将拒绝其他解锁呼叫，直到上电重置后。

[`-y`](#y_4)

在不提示确认的情况下对危险选项（例如 `-e` ）确认是

所有 HPA 命令的密码限制为 32 个字符，更长的密码将失效。

[`ama`](#ama)

更新或报告可访问的最大地址配置。 默认情况下， `camcontrol` 将打印出设备的可访问最大地址配置支持和相关设置。 `ama` 命令采用几个可选参数：

[`-f`](#f_5)

冻结指定设备的可访问最大地址配置。

命令完成后，任何其他更新配置的命令都将被命令中止。 关闭电源会禁用冻结模式。

[`-q`](#q_10)

保持安静，不要打印任何状态消息。

[`-s`](#s_6) max\_sectors

配置设备的最大用户可访问扇区。 这将更改设备报告的扇区数。

_WARNING! WARNING! WARNING!_

使用此选项更改设备的最大扇区将使设备上超出指定值的数据不确定。

只有一次成功 `-s` max\_sectors 调用才能在没有设备上电复位的情况下进行。

[`fwdownload`](#fwdownload)

使用提供的映像文件为指定的 SCSI 或 ATA 设备编程固件。

如果设备是 SCSI 设备并且它为 WRITE BUFFER 命令提供了建议的超时（请参阅 `camcontrol` 子命令），则该超时将用于固件下载。 可以使用 `-t` 选项在命令行上覆盖驱动器推荐的超时值。

当前支持的 SCSI/SAS 驱动器供应商列表：

HGST

使用 4TB SAS 驱动器进行测试，型号为 HUS724040ALS640。

HITACHI

HP

IBM

使用 LTO-5 (ULTRIUM-HH5) 和 LTO-6 (ULTRIUM-HH6) 磁带机进行了测试。 硬盘驱动器有一个单独的表条目，因为硬盘驱动器的更新方法与磁带驱动器的方法不同。

PLEXTOR

QUALSTAR

QUANTUM

SAMSUNG

使用 SM1625 SSD 测试。

SEAGATE

使用 Constellation ES (ST32000444SS)、ES.2 (ST33000651SS) 和 ES.3 (ST1000NM0023) 驱动器进行测试。

SmrtStor

使用 400GB Optimus SSD (TXA2D20400GA6001) 进行测试。

_WARNING! WARNING! WARNING!_

几乎没有进行测试以确保来自每个供应商的不同设备型号可以正确使用 fwdownload 命令。 支持列表中出现的供应商名称仅表示该供应商的至少一种设备类型的固件已使用 fwdownload 命令成功编程。 使用此命令时应格外小心，因为不能保证它不会破坏所列供应商的设备。 在执行固件更新之前，请确保您最近备份了设备上的数据。

请注意，未知的 SCSI 协议设备将不会被编程，因为固件下载成功的可能性很小。

`camcontrol` 当前将尝试将固件下载到任何 ATA 或 SATA 设备，因为标准的 ATA DOWNLOAD MICROCODE 命令可能会起作用。 连接到标准 ATA 和 SATA 控制器的设备以及连接到具有 SCSI 到 ATA 转换功能的 SAS 控制器的设备支持将固件下载到 ATA 和 SATA 设备。 在后一种情况下， `camcontrol` 使用 SCSI ATA PASS-THROUGH 命令将 ATA DOWNLOAD MICROCODE 命令发送到驱动器。 一些 SCSI 到 ATA 的转换实现在将 SCSI WRITE BUFFER 命令转换为 ATA DOWNLOAD MICROCODE 命令时不能完全工作，但支持 ATA passthrough 足以进行固件下载。

[`-f`](#f_6) fw\_image

要下载到指定设备的固件映像文件的路径。

[`-q`](#q_11)

不打印信息性消息，只打印错误。 此选项应与 `-y` 选项一起使用以抑制所有输出。

[`-s`](#s_7)

在模拟模式下运行。 运行设备检查并显示确认对话框，但不会下载固件。

[`-v`](#v_4)

在发生故障时显示 SCSI 或 ATA 错误。

在模拟模式下，打印出将用于固件下载命令的 SCSI CDB 或 ATA 寄存器值。

[`-y`](#y_5)

不要要求确认。

[`persist`](#persist)

持续预订支持。 持久保留是一种保留特定 SCSI LUN 以供一个或多个 SCSI 启动器使用的方法。 如果指定了 `-i` 选项， `camcontrol` 将使用请求的服务操作发出 SCSI PERSISTENT RESERVE IN 命令。 如果指定了 `-o` 选项， `camcontrol` 将使用请求的服务操作发出 SCSI PERSISTENT RESERVE OUT 命令。 这两个选项之一是必需的。

永久保留很复杂，完全解释它们超出了本手册的范围。 请访问 http://www.t10.org 并下载最新的 SPC 规范以获取有关持久保留的完整说明。

[`-i`](#i_2) mode

为 PERSISTENT RESERVE IN 命令指定服务操作。 支持的服务操作：

read\_keys

报告当前的持久保留生成 (PRgeneration) 和任何已注册的密钥。

read\_reservation

报告持久保留（如果有）。

report\_capabilities

报告 LUN 的持久保留功能。

read\_full\_status

报告 LUN 上永久保留的完整状态。

[`-o`](#o_3) mode

为 PERSISTENT RESERVE OUT 命令指定服务操作。 对于作为其他服务操作名称组成部分的注册服务操作，必须指定整个名称。 否则，必须指定足够的服务操作名称以将其与其他可能的服务操作区分开来。 支持的服务操作：

register

向 LUN 注册保留密钥或取消注册保留密钥。 要注册密钥，请将请求的密钥指定为服务操作保留密钥。 要取消注册密钥，请将先前注册的密钥指定为保留密钥。 要更改密钥，请将旧密钥指定为保留密钥，将新密钥指定为服务操作保留密钥。

register\_ignore

这类似于 register 子命令，只是忽略了 Reservation Key。 服务操作保留密钥将覆盖之前为发起者注册的任何密钥。

reserve

创建预订。 在保留 LUN 之前，必须向 LUN 注册密钥，并且必须将其指定为 Reservation Key。 还必须指定预订类型。 范围默认为 LUN 范围 (LU\_SCOPE)，但可以更改。

release

释放预订。 必须指定保留密钥。

clear

释放保留并从设备中删除所有密钥。 必须指定保留密钥。

preempt

删除属于另一个发起者的预留。 必须指定保留密钥。 根据正在执行的操作，可以指定服务操作保留密钥。

preempt\_abort

删除属于另一个启动器的保留并中止来自该启动器的所有未完成的命令。 必须指定保留密钥。 根据正在执行的操作，可以指定服务操作保留密钥。

register\_move

向 LUN 注册另一个启动器，并在 LUN 上为该启动器建立预留。 必须指定预留密钥和服务操作预留密钥。

replace\_lost

替换丢失的预订信息。

[`-a`](#a_5)

设置所有目标端口 (ALL\_TG\_PT) 位。 这要求将密钥注册应用于所有目标端口，而不仅仅是接收命令的特定目标端口。 这仅适用于 register 和 register\_ignore 操作。

[`-I`](#I_3) tid

指定传输 ID。 这仅适用于 Persistent Reserve Out 的 Register 和 Register 以及 Move 服务操作。 可以使用多个 `-I` 参数指定多个传输 ID。 通过注册服务操作，指定一个或多个传输 ID 会隐式启用 `-S` 选项，该选项会打开 SPEC\_I\_PT 位。 传输 ID 通常具有格式协议 ID。

SAS

SAS 传输 ID 由 “sas” 和后跟 64 位 SAS 地址组成。

`sas,0x1234567812345678`

FC

光纤通道传输 ID 由 “fcp,” 和后跟 64 位光纤通道全球名称组成。例如：

`fcp,0x1234567812345678`

SPI

并行 SCSI 地址由 “spi” 、后跟 SCSI 目标 ID 和相对目标端口标识符组成。

`spi,4,1`

1394

IEEE 1394（火线）传输 ID 由 “sbp” 和后跟 64 位 EUI-64 IEEE 1394 节点唯一标识符组成。 例如：

`sbp,0x1234567812345678`

RDMA

SCSI over RDMA 传输 ID 由 “srp” 和后跟 128 位 RDMA 发起程序端口标识符组成。 端口标识符必须是 32 或 34（如果包括前导 0x）十六进制数字。 仅支持十六进制（以 16 为基数）数字。例如：

`srp,0x12345678123456781234567812345678`

iSCSI

iSCSI 传输 ID 由 iSCSI 名称和可选的分隔符和 iSCSI 会话 ID 组成。 例如，如果仅指定 iSCSI 名称：

`iqn.2012-06.com.example:target0`

如果指定了 iSCSI 分隔符和启动器会话 ID：

`iqn.2012-06.com.example:target0,i,0x123`

PCIe

SCSI over PCIe 传输 ID 由 “sop” 和后跟 PCIe 路由 ID 组成。 路由 ID 由总线、设备和功能组成，或者以另一种形式，由总线和功能组成。 总线必须在 0 到 255 的范围内，设备必须在 0 到 31 的范围内。 如果使用标准形式，函数必须在 0 到 7 的范围内，如果使用替代形式，函数必须在 0 到 255 的范围内。 例如，如果为标准 Routing ID 表单指定了总线、设备和功能：

`sop,4,5,1`

如果使用备用路由 ID 表单：

`sop,4,1`

[`-k`](#k_2) key

指定保留密钥。 这可以是十进制、八进制或十六进制格式。 如果没有另外指定，默认情况下该值为零。 该值必须介于 0 和 2^64 - 1 之间，包括 0 和 2^64 - 1。

[`-K`](#K) key

指定服务操作保留密钥。 这可以是十进制、八进制或十六进制格式。 如果没有另外指定，默认情况下该值为零。 该值必须介于 0 和 2^64 - 1 之间，包括 0 和 2^64 - 1。

[`-p`](#p_4)

启用通过断电激活持久性位。 这仅用于 register 和 register\_ignore 操作。 这要求保留在断电事件中持续存在。

[`-s`](#s_8) scope

指定保留的范围。 范围可以按名称或编号指定。 register、register\_ignore 和 clear 的范围被忽略。 如果所需范围不能按名称提供，您可以指定数字。

lun

LUN 范围 (0x00)。这包括整个 LUN。

extent

范围范围 (0x01)。

element

元素范围 (0x02)。

[`-R`](#R_4) rtp

指定相对目标端口。 这仅适用于 Persistent Reserve Out 命令的注册和移动服务操作。

[`-S`](#S_5)

启用 SPEC\_I\_PT 位。 这仅适用于 Persistent Reserve Out 的注册服务操作。 如果设置了此选项，您还必须使用 `-I` 指定至少一个传输 ID。 如果您指定传输 ID，则会自动设置此选项。 为注册以外的任何服务操作指定此选项是错误的。

[`-T`](#T_5) type

指定预订类型。 预订类型可以按名称或编号指定。 如果所需的预订类型无法按名称提供，您可以指定编号。 支持的预订类型名称：

read\_shared

读取共享模式。

wr\_ex

写独占模式。 也可以指定为 “write\_exclusive” 。

rd\_ex

阅读独占模式。 也可以指定为 “read\_exclusive” 。

ex\_ac

独占访问模式。 也可以指定为 “exclusive\_access” 。

wr\_ex\_ro

仅写入独占注册人模式。 也可以指定为 “write\_exclusive\_reg\_only” 。

ex\_ac\_ro

独占访问仅限注册者模式。 也可以指定为 “exclusive\_access\_reg\_only” 。

wr\_ex\_ar

写入独占所有注册者模式。 也可以指定为 “write\_exclusive\_all\_regs” 。

ex\_ac\_ar

独占访问所有注册者模式。 也可以指定为 “exclusive\_access\_all\_regs” 。

[`-U`](#U_5)

指定目标应取消注册发送注册和移动请求的发起者。 默认情况下，目标不会取消注册发送注册和移动请求的发起者。 此选项仅适用于 Persistent Reserve Out 命令的注册和移动服务操作。

[`attrib`](#attrib)

发出 SCSI READ 或 WRITE ATTRIBUTE 命令。 这些命令用于读取和写入中等辅助存储器 (MAM) 中的属性。 中型辅助存储器最常见的地方是小型闪存芯片，包括磁带盒。 例如， LTO 磁带具有 MAM。 必须指定 `-r` 选项或 `-w` 选项。

[`-r`](#r_6) action

指定 READ ATTRIBUTE 服务操作。

attr\_values

发出属性值服务操作。 读取和解码可用属性及其值。

attr\_list

发出属性列表服务操作。 列出可读取和写入的属性。

lv\_list

发出 LOGICAL VOLUME LIST 服务操作。 列出 MAM 中可用的逻辑卷。

part\_list

发出 PARTITION LIST 服务操作。列出 MAM 中的可用分区。

supp\_attr

发出支持的属性服务操作。 列出支持读取或写入的属性。 这些属性当前可能存在也可能不存在于 MAM 中。

[`-w`](#w_3) attr

指定要写入 MAM 的属性。 此选项尚未实施。

[`-a`](#a_6) num

指定要显示的属性编号。 此选项仅适用于 `-r` 的 attr\_values、attr\_list 和 supp\_attr 参数。

[`-c`](#c_6)

显示缓存的属性。 如果设备支持此标志，则它允许显示驱动器中加载的最后一块媒体的属性。

[`-e`](#e_3) num

指定元素地址。 这用于指定读取属性时要访问的介质转换器中的哪个元素编号。 元素编号可以用于拾取器、入口、插槽或驱动器。

[`-F`](#F) form1,form2

将属性值 (attr\_val) 的输出格式指定为以逗号分隔的选项列表。 默认输出当前设置为 field\_all,nonascii\_trim,text\_raw。 一旦将此代码移植到 FreeBSD 10，任何文本字段都将使用 iconv(3) 从其代码集转换为用户的本机代码集。

文本选项是互斥的；如果你指定多个，你会得到不可预知的结果。 nonascii 选项也是互斥的。 大多数字段选项可以逻辑或在一起。

text\_esc

打印带有非 ASCII 字符转义的文本字段。

text\_raw

本机打印文本字段，无需代码集转换。

nonascii\_esc

如果在应该是 ASCII 的字段中出现任何非 ASCII 字符，请转义非 ASCII 字符。

nonascii\_trim

如果在应该是 ASCII 的字段中出现任何非 ASCII 字符，请忽略非 ASCII 字符。

nonascii\_raw

如果在应该是 ASCII 的字段中出现任何非 ASCII 字符，请按原样打印它们。

field\_all

打印所有前缀字段：描述、属性编号、属性大小和属性的只读状态。 如果指定了 field\_all，则指定任何其他字段选项将不起作用。

field\_none

不打印任何前缀字段，只打印属性值。 如果指定了 field\_none，则指定任何其他字段选项将导致打印这些字段。

field\_desc

打印出属性描述。

field\_num

打印出属性号。

field\_size

打印出属性大小。

field\_rw

打印出属性的只读状态。

[`-p`](#p_5) part

指定分区。 当媒体有多个分区时，指定不同的分区号可以查看每个单独分区的值。

[`-s`](#s_9) start\_num

指定起始属性编号。 这要求目标设备返回从给定编号开始的属性信息。

[`-T`](#T_6) elem\_type

指定元素类型。 对于介质更换器设备，这允许指定元素地址 ( `-e` )中引用的元素的类型。 有效类型为： “all”, “picker”, “slot”, “portal” 和 “drive” 。

[`-V`](#V) vol\_num

指定要操作的逻辑卷的编号。 如果媒体有多个逻辑卷，这将允许在给定的逻辑卷上显示或写入属性。

[`opcodes`](#opcodes)

发出 SCSI MAINTENANCE IN 命令的 REPORT SUPPORTED OPCODES 服务操作。 如果没有参数，此命令将返回设备支持的所有 SCSI 命令的列表，包括支持服务操作的命令的服务操作。 它还将包括每个命令的 SCSI CDB （命令数据块）长度，以及每个命令的描述（如果已知）。

[`-o`](#o_4) opcode

请求有关特定操作码的信息，而不是支持的命令列表。 如果支持，目标将返回一个类似 CDB 的结构，指示操作码、服务操作（如果有）和该 CDB 中支持的位掩码。

[`-s`](#s_10) service\_action

对于支持服务操作的命令，指定要查询的服务操作。

[`-N`](#N_3)

如果为给定的操作码指定了服务操作，并且设备不支持给定的服务操作，则设备不应返回 SCSI 错误，而是在返回的参数数据中指示不支持该命令。 默认情况下，如果为操作码指定了服务操作，并且相关操作码不支持服务操作，则设备将返回错误。

[`-T`](#T_7)

包括超时值。 此选项适用于默认显示，其中包括设备支持的所有命令，以及 `-o` 和 `-s` 选项，它们请求有关特定命令和服务操作的信息。 这要求设备报告给定命令的标称和建议超时值。 超时值以秒为单位。 超时描述符还包括一个特定于命令的

[`zone`](#zone)

管理 SCSI 和 ATA 分区块设备。 这允许管理符合 SCSI 分区块命令 (ZBC) 和 ATA 分区 ATA 命令集 (ZAC) 规范的设备。 使用这些命令集的设备通常是使用叠瓦式磁记录 (SMR) 的硬盘驱动器。共有三种类型的 SMR 驱动器：

Drive Managed

驱动器托管驱动器的外观和行为就像标准随机访问块设备，但在其底层，驱动器使用 SMR 区域读取和写入其大部分容量。 顺序写入将产生更好的性能，但不需要顺序写入。

Host Aware

Host Aware 驱动器通过 SCSI 或 ATA 命令公开底层区域布局，并允许主机管理区域条件。 但是，主机不需要管理驱动器上的区域。 顺序写入将在顺序写入首选区域中产生更好的性能，但主机可以在这些区域中随机写入。

Host Managed

主机托管驱动器通过 SCSI 或 ATA 命令公开底层区域布局。 主机需要根据区域布局描述的规则访问区域。 任何违反规则的命令都将返回错误。

SMR 驱动器分为三个一般类别的区域（通常每个区域在 256MB 范围内）：

Conventional

这些也称为非写指针区域。 这些区域可以随机写入而不会造成意外的性能损失。

Sequential Preferred

这些区域应该从区域的写指针开始顺序写入。 它们可能是随机写入的。 不符合区域布局的写入可能比预期的要慢得多。

Sequential Required

这些区域必须按顺序写入。 如果它们没有按顺序写入，从写指针开始，命令将失败。

[`-c`](#c_7) cmd

指定区域子命令：

rz

发出报告区域命令。 默认情况下返回所有区域。 使用 `-o` 指定报告选项，使用 `-P` 指定打印选项。 使用 `-l` 指定起始 LBA。 请注意， “reportzones” 也被接受为命令参数。

open

显式打开起始 LBA 指定的区域。

close

关闭启动 LBA 指定的区域。

finish

完成起始 LBA 指定的区域。

rwp

重置由起始 LBA 指定的区域的写指针。

[`-a`](#a_7)

对于 Open、Close、Finish 和 Reset Write Pointer 操作，将操作应用于驱动器上的所有区域。

[`-l`](#l_10) lba

指定起始 LBA。 对于 Report Zones 命令，这告诉驱动器从给定 LBA 开始的区域开始报告。 对于其他命令，这允许用户识别其起始 LBA 请求的区域。 LBA 可以用十进制、十六进制或八进制表示法指定。

[`-o`](#o_5) rep\_opt

对于 Report Zones 命令，指定要报告的区域子集。

all

报告所有区域。这是默认设置。

emtpy

仅报告空白区域。

imp\_open

报告隐式打开的区域。 这意味着主机已向该区域发送了一个写操作，但并未明确打开该区域。

exp\_open

报告明确开放的区域。

closed

报告已被主机关闭的区域。

full

报告已满的区域。

ro

报告处于只读状态的区域。 请注意， “readonly” 也被接受为参数。

offline

报告处于脱机状态的区域。

reset

报告设备建议重置写指针的区域。

nonseq

报告设置了非顺序资源活动标志的区域。 这些是顺序写入首选的区域，但已被非顺序写入。

nonwp

报告非写指针区域，也称为常规区域。

[`-P`](#P_6) print\_opt

指定报告区域的打印选项：

normal

正常报告区域输出。 这是默认设置。 打印摘要和列标题，字段由空格分隔，并且字段本身可能包含空格。

summary

只需打印摘要：区域数、最大 LBA（驱动器上最后一个逻辑块的 LBA）以及 “same” 字段的值。 “same” 字段描述驱动器上的区域是否全部相同、全部不同，或者除了最后一个区域之外它们是否相同等。

script

以脚本友好的格式打印区域。 省略摘要和列标题，字段以逗号分隔，字段不包含空格。 这些字段包含通常使用空格的下划线。

[`epc`](#epc)

发出 ATA 扩展电源条件 (EPC) 功能集命令。 这仅适用于 ATA 协议驱动器，不适用于 SCSI 它将在 SCSI 到 ATA 转换层 (SAT) 后面的 SATA 驱动器上工作。 阅读 t13.org 上提供的扩展电源条件功能集的 ATA 命令集 - 4 (ACS-4) 描述可能会有所帮助，以了解此特定 `camcontrol` 命令的详细信息。

[`-c`](#c_8) cmd

指定 epc 子命令

restore

恢复驱动器电源条件设置。

[`-r`](#r_7) src

指定恢复电源设置的来源， “default” 或 “saved” 。 该参数是必需的。

[`-s`](#s_11)

保存设置。 这只有在从默认值恢复时指定才有意义。

goto

转到指定的电源条件。

[`-p`](#p_6) cond

指定电源条件： Idle\_a, Idle\_b, Idle\_c, Standby\_y, Standby\_z。 该参数是必需的。

[`-D`](#D_4)

指定延迟进入电源条件。 如果驱动器支持这一点，则可以在命令完成后进入电源状态。

[`-H`](#H_2)

保持电源状态。 如果驱动器支持此选项，它将保持电源状况并拒绝通常会导致其退出该电源状况的所有命令。

timer

设置电源条件的计时器值并启用或禁用该条件。 请参阅下面描述的 “list” 显示，以了解驱动器支持的每个空闲和待机模式的当前计时器设置。

[`-e`](#e_4)

启用电源条件。 `-e` 或 `-d` 之一是必需的。

[`-d`](#d_5)

禁用电源条件。 `-d` 或 `-e` 之一是必需的。

[`-T`](#T_8) timer

以秒为单位指定计时器。 用户可以将计时器指定为浮点数，支持的最大分辨率为十分之一秒。 驱动器可能支持也可能不支持亚秒级计时器值。

[`-p`](#p_7) cond

指定电源条件： Idle\_a, Idle\_b, Idle\_c, Standby\_y, Standby\_z。 该参数是必需的。

[`-s`](#s_12)

保存定时器和电源条件启用/禁用状态。 默认情况下，如果未指定此选项，则仅影响此电源条件的当前值。

state

启用或禁用特定的电源条件。

[`-e`](#e_5)

启用电源条件。 `-e` 或 `-d` 之一是必需的。

[`-d`](#d_6)

禁用电源条件。 `-d` 或 `-e` 之一是必需的。

[`-p`](#p_8) cond

指定电源条件： Idle\_a, Idle\_b, Idle\_c, Standby\_y, Standby\_z。 该参数是必需的。

[`-s`](#s_13)

保存电源条件启用/禁用状态。 默认情况下，如果未指定此选项，则仅影响此电源条件的当前值。

enable

启用扩展功率条件 (EPC) 功能集。

disable

禁用扩展电源条件 (EPC) 功能集。

source

指定 EPC 电源。

[`-S`](#S_6) src

指定电源， “battery” 或 “nonbattery” 。

status

获取与扩展电源条件 (EPC) 功能集相关的几个参数的当前状态，包括是否支持和启用 APM 和 EPC、是否支持低功耗待机、是否支持设置 EPC 电源、是否启用低功耗待机支持和当前的电源状况。

[`-P`](#P_7)

只报告当前的电源状况。 如果收到 ATA CHECK POWER MODE 命令以外的命令，某些驱动器将退出其当前的电源状态。 如果指定了这个标志， `camcontrol` 将只向驱动器发出 ATA CHECK POWER MODE 命令。

list

显示 ATA 电源状况日志（日志地址 0x08）。 这显示了驱动器支持的空闲和待机电源条件列表，以及每个条件的一些参数，包括是否启用以及计时器值是多少。

[`timestamp`](#timestamp)

发出 REPORT TIMESTAMP 或 SET TIMESTAMP SCSI 命令。 必须指定 `-r` 选项或 `-s` 选项。

[`-r`](#r_8)

报告设备的时间戳。 如果未指定更多参数，则将使用日期和时间的国家表示形式报告时间戳，然后是时区。

[`-f`](#f_7) format

指定 strftime 格式字符串，如 strftime(3) 中所述，用于格式化报告的时间戳。

[`-m`](#m_3)

将时间戳报告为自纪元以来的毫秒数。

[`-U`](#U_6)

使用日期和时间的国家表示形式报告时间戳，但覆盖系统时区并改用 UTC。

[`-s`](#s_14)

设置设备的时间戳。 必须指定 `-f` 和 `-T` 选项或 `-U` 选项。

[`-f`](#f_8) format

指定 strptime 格式字符串，如 strptime(3) 中所述。 还必须使用 `-T` 选项指定时间。

[`-T`](#T_9) time

以使用 `-f` 选项指定的格式提供时间。

[`-U`](#U_7)

将时间戳设置为主机系统的 UTC 时间。

[`devtype`](#devtype)

打印指定设备的设备类型。

ata

直接连接到 ATA 控制器的 ATA 设备

satl

通过 SCSI-ATA 转换层 (SATL) 连接到 SAS 控制器后面的 SATA 设备

scsi

SCSI 设备

nvme

直接连接的 NVMe 设备

mmcsd

通过 mmcsd 总线连接的 MMC 或 SD 设备

none

未报告设备类型

unknown

设备类型未知

illegal

发生编程错误

[`help`](#help)

打印出详细的使用信息。

[环境](#__u73AF___u5883_)
=======================

`SCSI_MODES` 量允许用户指定备用模式页面格式文件。

`EDITOR` 变量确定在编辑模式页面时启动哪个文本编辑器 `camcontrol` 。

[文件](#__u6587___u4EF6_)
=======================

/usr/share/misc/scsi\_modes

是 SCSI 模式格式数据库。

/dev/xpt0

是传输层设备。

/dev/pass\*

是 CAM 应用程序直通设备。

[实例](#__u5B9E___u4F8B_)
=======================

`camcontrol eject -n cd -u 1 -v`

从 cd1 中弹出 CD，如果命令失败，则打印 SCSI 感知信息。

`camcontrol tur da0`

向 da0 发送 SCSI 测试单元就绪命令。 `camcontrol` 实用程序将报告磁盘是否准备就绪，但如果由于未指定 `-v` 开关而导致命令失败，则不会显示感知信息。

camcontrol tur da1 -E -C 4 -t 50 -Q head -v 

向 da1 发送测试单元就绪命令。 启用内核错误恢复。 指定重试计数为 4，超时为 50 秒。 如果命令失败，启用感知打印（使用 `-v` 标志）。 由于打开了错误恢复，如果磁盘当前没有旋转，它将旋转起来。 该命令的 SCSI 任务属性将设置为队列头。 `camcontrol` 实用程序将报告磁盘是否准备好。

camcontrol cmd -n cd -u 1 -v -c "3C 00 00 00 00 00 00 00 0e 00" \\ -i 0xe "s1 i3 i1 i1 i1 i1 i1 i1 i1 i1 i1 i1" 

向 cd1 发出 READ BUFFER 命令 (0x3C)。 显示 cd1 的缓冲区大小，并显示 cd1 上缓存的前 10 个字节。 如果命令失败，则显示 SCSI 感知信息。

camcontrol cmd -n cd -u 1 -v -c "3B 00 00 00 00 00 00 00 0e 00" \\ -o 14 "00 00 00 00 1 2 3 4 5 6 v v v v" 7 8 9 8 

向 cd1 发出 WRITE BUFFER (0x3B) 命令。 写出 10 字节的数据，不包括（保留的）4 字节标头。 如果命令失败，打印出感知信息。 使用此命令要非常小心，使用不当可能会导致数据损坏。

camcontrol modepage da3 -m 1 -e -P 3 

编辑 da3 的模式页面 1（读写错误恢复页面），并将设置保存在驱动器上。 模式页面 1 包含磁盘驱动器的自动读取和写入重新分配设置等。

`camcontrol rescan all`

重新扫描系统中的所有 SCSI 总线以查找已添加、删除或更改的设备。

`camcontrol rescan 0`

重新扫描 SCSI 总线 0 以查找已添加、删除或更改的设备。

`camcontrol rescan 0:1:0`

重新扫描 SCSI 总线 0、目标 1、lun 0 以查看是否已添加、删除或更改。

`camcontrol tags da5 -N 24`

将 da5 的并发事务数设置为 24。

camcontrol negotiate -n da -u 4 -T disable 

禁用 da4 的标记队列。

camcontrol negotiate -n da -u 3 -R 20.000 -O 15 -a 

与 da3 协商 20MHz 的同步速率和 15 的偏移量。然后发送Test Unit Ready 命令使设置生效。

camcontrol smpcmd ses0 -v -r 4 "40 0 00 0" -R 1020 "s9 i1" 

将 SMP REPORT GENERAL 命令发送到 ses0，并显示它包含的 PHY 数量。 如果命令失败，则显示 SMP 错误。

camcontrol security ada0 

报告 ada0 的安全支持和设置

camcontrol security ada0 -U user -s MyPass 

使用密码 MyPass 在设备 ada0 上启用安全性

camcontrol security ada0 -U user -e MyPass 

已使用用户密码 MyPass 启用安全性的安全擦除 ada0

_WARNING! WARNING! WARNING!_

这将 _ERASE_ 设备中的所有数据，因此请在使用前备份您的数据！

此命令可用于 SSD 驱动器以将其恢复到出厂默认写入性能。

camcontrol hpa ada0 

报告 ada0 的 HPA 支持和设置（也通过 identify 报告）。

camcontrol hpa ada0 -s 10240 

在 ada0 上启用 HPA，将报告的最大扇区数设置为 10240。

_WARNING! WARNING! WARNING!_

这将 _PREVENT ACCESS_ 超出此限制的设备上的所有数据，直到通过将 HPA 设置为设备的本机最大扇区来禁用 HPA，这只能在开机或硬件重置后完成！

_DO NOT_ 不要在具有活动文件系统的设备上使用它！

camcontrol persist da0 -v -i read\_keys 

这将读取使用 da0 注册的任何持久保留键，并显示发送 PERSISTENT RESERVE IN SCSI 命令时遇到的任何错误。

camcontrol persist da0 -v -o register -a -K 0x12345678 

这将向 da0 注册持久保留密钥 0x12345678，将该注册应用于 da0 上的所有端口，并显示发送 PERSISTENT RESERVE OUT 命令时发生的任何错误。

camcontrol persist da0 -v -o reserve -s lun -k 0x12345678 -T ex\_ac 

这将保留 da0 供发出命令的发起者独占使用。 预留的范围是整个 LUN。 将显示发送 PERSISTENT RESERVE OUT 命令的任何错误。

camcontrol persist da0 -v -i read\_full 

这将显示 da0 上所有预订的完整状态，并在有任何错误时打印出状态。

camcontrol persist da0 -v -o release -k 0x12345678 -T ex\_ac 

这将释放 da0 上 ex\_ac（独占访问）类型的预留。 此注册的保留密钥是 0x12345678。 将显示发生的任何错误。

camcontrol persist da0 -v -o register -K 0x12345678 -S \\ -I sas,0x1234567812345678 -I sas,0x8765432187654321 

这会将密钥 0x12345678 注册到 da0，指定它适用于 SAS 地址为 0x1234567812345678 和 0x8765432187654321 的 SAS 启动器。

camcontrol persist da0 -v -o register\_move -k 0x87654321 \\ -K 0x12345678 -U -p -R 2 -I fcp,0x1234567812345678 

这会将注册从当前启动器（其注册密钥为 0x87654321）移动到光纤通道全球节点名称为 0x1234567812345678 的光纤通道启动器。 将为具有光纤通道全球节点名称 0x1234567812345678 的启动器注册一个新的注册密钥 0x12345678，并且将从目标中注销当前启动器。 保留将移动到目标设备上的相对目标端口 2。 注册将在断电期间持续存在。

camcontrol attrib sa0 -v -i attr\_values -p 1 

这将从磁带驱动器 sa0 中磁带上的分区 1 读取和解码属性值，并将显示导致的任何 SCSI 错误。

camcontrol zone da0 -v -c rz -P summary 

这将从磁盘 da0 请求 SMR 区域列表，并打印出区域参数的摘要，并显示导致的任何 SCSI 或 ATA 错误。

camcontrol zone da0 -v -c rz -o reset 

这将请求应从磁盘 da0 重置其写指针的 SMR 区域列表，并显示导致的任何 SCSI 或 ATA 错误。

camcontrol zone da0 -v -c rwp -l 0x2c80000 

这将为从 LBA 0x2c80000 开始的区域向磁盘 da0 发出 Reset Write Pointer 命令，并显示由此产生的任何 SCSI 或 ATA 错误。

camcontrol epc ada0 -c timer -T 60.1 -p Idle\_a -e -s 

将驱动器 ada0 上的 Idle\_a 电源条件的计时器设置为 60.1 秒，启用该特定电源条件，并保存计时器值和电源条件的启用状态。

camcontrol epc da4 -c goto -p Standby\_z -H 

告诉驱动器 da4-
进入 Standby\_z 电源状态（这是驱动器的最低电源状态）并保持在该状态，直到它被另一个 `goto` 命令显式释放。

camcontrol epc da2 -c status -P 

仅报告驱动器 da2 的电源状态。 某些驱动器会根据 status 子命令发送的命令启动，而 `-P` 选项会导致 `camcontrol` 仅发送 ATA CHECK POWER MODE 命令，这不应触发驱动器电源状态的更改。

camcontrol epc ada0 -c list 

显示驱动器 ada0 的 ATA 电源状况日志（日志地址 0x08）。

camcontrol timestamp sa0 -s -f "%a, %d %b %Y %T %z" \\ -T "Wed, 26 Oct 2016 21:43:57 -0600" 

使用 strptime(3) 格式字符串后跟使用此格式字符串创建的时间字符串设置驱动器 sa0 的时间戳。

[参见](#__u53C2___u89C1_)
=======================

cam(3), cam\_cdbparse(3), cam(4), pass(4), xpt(4)

[历史](#__u5386___u53F2_)
=======================

`camcontrol` 实用程序首先出现在 FreeBSD 3.0 中。

模式页面编辑代码和任意 SCSI 命令代码基于旧 scsi(8) 实用程序和 scsi(3) 库中的代码，由 Julian Elischer 和 Peter Dufault 编写。 scsi(8) 程序最早出现在 386BSD-0.1.2.4 中，最早出现在 FreeBSD 的 FreeBSD 2.0.5 中。

[作者](#__u4F5C___u8005_)
=======================

Kenneth Merry <[ken@FreeBSD.org](mailto:ken@FreeBSD.org)\>

[缺陷](#__u7F3A___u9677_)
=======================

解析通用命令行参数的代码不知道某些子命令采用多个参数。 因此，例如，如果您尝试过这样的事情：

camcontrol cmd -n da -u 1 -c "00 00 00 00 00 v" 0x00 -v 

来自测试单元就绪命令的感知信息不会被打印出来，因为 `camcontrol` 中的第一个 getopt(3) 调用在看到上面的 `-c` (0x00) 的第二个参数时会退出。 修复此行为需要一些粗略的代码，或更改 getopt(3) 接口。 避免此问题的最佳方法是始终确保在任何特定于命令的参数之前指定通用 `camcontrol` 参数。

August 6, 2019

FreeBSD 13.1-RELEASE