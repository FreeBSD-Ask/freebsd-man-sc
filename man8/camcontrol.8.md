# camcontrol(8)

`camcontrol` — CAM 控制程序

## 名称

`camcontrol`

## 概要

`camcontrol <command> [device id] [generic args] [command args]`

`camcontrol devlist [-b] [-v]`

`camcontrol periphlist [device id] [-n dev_name] [-u unit_number]`

`camcontrol tur [device id] [generic args]`

`camcontrol sense [device id] [generic args] [-D] [-x]`

`camcontrol inquiry [device id] [generic args] [-D] [-S] [-R]`

`camcontrol identify [device id] [generic args] [-v]`

`camcontrol reportluns [device id] [generic args] [-c] [-l] [-r reporttype]`

`camcontrol readcap [device id] [generic args] [-b] [-h] [-H] [-l] [-N] [-q] [-s]`

`camcontrol start [device id] [generic args]`

`camcontrol stop [device id] [generic args]`

`camcontrol load [device id] [generic args]`

`camcontrol eject [device id] [generic args]`

`camcontrol reprobe [device id]`

`camcontrol rescan <all | device id | bus[:target:lun]>`

`camcontrol reset <all | device id | bus[:target:lun]>`

`camcontrol defects [device id] [generic args] <-f format> [-P] [-G] [-q] [-s] [-S offset] [-X]`

`camcontrol modepage [device id] [generic args] [-6] <-m page[,subpage] | -l> [-P pgctl] [-D] [-L] [-b | -e] [-d]`

`camcontrol cmd [device id] [generic args] <-a cmd [args]> <-c cmd [args]> [-d] [-f] [-i len fmt] [-o len fmt [args]] [-r fmt]`

`camcontrol smpcmd [device id] [generic args] <-r len fmt [args]> <-R len fmt [args]>`

`camcontrol smprg [device id] [generic args] [-l]`

`camcontrol smppc [device id] [generic args] <-p phy> [-l] [-o operation] [-d name] [-m rate] [-M rate] [-T pp_timeout] [-a enable|disable] [-A enable|disable] [-s enable|disable] [-S enable|disable]`

`camcontrol smpphylist [device id] [generic args] [-l] [-q]`

`camcontrol smpmaninfo [device id] [generic args] [-l]`

`camcontrol debug [-I] [-P] [-T] [-S] [-X] [-c] [-p] <all | off | device id | bus[:target[:lun]]>`

`camcontrol tags [device id] [generic args] [-N tags] [-q] [-v]`

`camcontrol negotiate [device id] [generic args] [-c] [-D enable|disable] [-M mode] [-O offset] [-q] [-R syncrate] [-T enable|disable] [-U] [-W bus_width] [-v]`

`camcontrol format [device id] [generic args] [-q] [-r] [-w] [-y]`

`camcontrol sanitize [device id] [generic args] <-a overwrite | block | crypto | exitfailure> [-c passes] [-I] [-P pattern] [-q] [-U] [-r] [-w] [-y]`

`camcontrol idle [device id] [generic args] [-t time]`

`camcontrol standby [device id] [generic args] [-t time]`

`camcontrol sleep [device id] [generic args]`

`camcontrol powermode [device id] [generic args]`

`camcontrol apm [device id] [generic args] [-l level]`

`camcontrol aam [device id] [generic args] [-l level]`

`camcontrol fwdownload [device id] [generic args] <-f fw_image> [-q] [-s] [-y]`

`camcontrol security [device id] [generic args] [-d pwd] [-e pwd] [-f] [-h pwd] [-k pwd] [-l high|maximum] [-q] [-s pwd] [-T timeout] [-U user|master] [-y]`

`camcontrol hpa [device id] [generic args] [-f] [-l] [-P] [-p pwd] [-q] [-s max_sectors] [-U pwd] [-y]`

`camcontrol ama [device id] [generic args] [-f] [-q] [-s max_sectors]`

`camcontrol persist [device id] [generic args] <-i action | -o action> [-a] [-I trans_id] [-k key] [-K sa_key] [-p] [-R rel_tgt_port] [-s scope] [-S] [-T res_type] [-U]`

`camcontrol attrib [device id] [generic args] <-r action | -w attrib> [-a attr_num] [-c] [-e elem_addr] [-F form1,form2] [-p part] [-s start_addr] [-T elem_type] [-V lv_num]`

`camcontrol opcodes [device id] [generic args] [-o opcode] [-s service_action] [-N] [-T]`

`camcontrol zone <-c cmd> [-a] [-l lba] [-o rep_opts] [-P print_opts]`

`camcontrol epc <-c cmd> [-d] [-D] [-e] [-H] [-p power_cond] [-P] [-r restore_src] [-s] [-S power_src] [-T timer]`

`camcontrol timestamp [device id] [generic args] <-r [-f format | -m | -U] | -s <-f format -T time | -U>>`

`camcontrol devtype [device id]`

`camcontrol depop [device id] [generic args] <-l | -d | -r> [-e elem] [-c capacity]`

`camcontrol help`

## 描述

`camcontrol` 工具允许用户访问和控制 cam(4) 中所述的 FreeBSD CAM 子系统。

`camcontrol` 工具如果使用不当，可能导致数据丢失和/或系统崩溃。即使专家用户也应谨慎使用此命令。新手用户应远离此工具。

`camcontrol` 工具具有许多主要功能，其中许多支持可选的设备标识符。设备标识符可采用以下三种形式之一：

**deviceUNIT** 指定设备名和单元号组合，如 "da5" 或 "cd3"。

**bus:target** 指定总线号和目标 ID。总线号可从 “camcontrol devlist” 的输出中确定。LUN 默认为 0。

**bus:target:lun** 指定设备的总线、目标和 LUN。（例如 1:2:0）

如果指定了设备标识符，它 *必须* 紧跟在功能名之后、任何通用或特定功能参数之前。注意，下文所述的 `-n` 和 `-u` 参数将覆盖事先指定的任何设备名或单元号。但 `-n` 和 `-u` 参数 *不会* 覆盖指定的 bus:target 或 bus:target:lun。

大多数 `camcontrol` 主要功能支持以下通用参数：

**`-C`** `count` SCSI 命令重试次数。要使此功能生效，必须启用错误恢复（`-E`）。

**`-E`** 指示内核对给定命令执行通用 SCSI 错误恢复。这是重试次数（`-C`）生效所必需的。除重试命令外，代码中的通用错误恢复通常还会尝试启动未旋转的驱动器。根据命令返回的 sense 代码，它可能采取其他操作。

**`-n`** `dev_name` 指定要操作的设备类型，如 "da"、"cd"。

**`-Q`** `task_attr` SCSI 命令的 SCSI 任务属性（如果是 SCSI 命令）。可以是 ordered、simple、head 或 aca。大多数情况下不需要此参数。默认为 simple，适用于所有 SCSI 设备。任务属性也可以用数字指定。

**`-t`** `timeout` SCSI 命令超时（秒）。这会覆盖任何给定命令的默认超时。

**`-u`** `unit_number` 指定设备单元号，如 "1"、"5"。

**`-v`** 详细模式，打印失败 SCSI 命令的 sense 信息。

主要命令功能：

**`devlist`** 列出连接到 CAM 子系统的所有物理设备（逻辑单元）。还包括连接到每个设备的外围驱动程序列表。使用 `-v` 参数时，还会打印 SCSI 总线号、适配器名和单元号。使用 `-b` 参数时，仅打印总线适配器和单元信息，省略设备信息。

**`periphlist`** 列出连接到给定物理设备（逻辑单元）的所有外围驱动程序。

**`tur`** 向给定设备发送 SCSI TEST UNIT READY (0x00) 命令。`camcontrol` 工具将报告设备是否就绪。

**`sense`** 向设备发送 SCSI REQUEST SENSE 命令 (0x03)。解码后的 sense（或十六进制转储）将打印到 stdout。

**`inquiry`** 向设备发送 SCSI INQUIRY 命令 (0x12)。默认情况下，`camcontrol` 将打印标准查询数据、设备序列号和传输速率信息。用户可以指定仅打印某些类型的查询数据：

**`-D`** 获取标准查询数据。

**`-S`** 打印序列号。如果仅指定此标志，`camcontrol` 不会在驱动器返回的值之前打印 "Serial Number"。这有助于脚本编写。

**`-R`** 打印传输速率信息。

**`identify`** 向设备发送 ATA IDENTIFY 命令 (0xec)。

**`reportluns`** 向给定设备发送 SCSI REPORT LUNS (0xA0) 命令。默认情况下，`camcontrol` 将打印目标设备支持的逻辑单元（LUN）列表。有 couple of options to modify the output: `camcontrol` 会尝试以合理的格式打印 LUN 号。它能识别 peripheral、flat、LUN 和扩展 LUN 格式。

**`-c`** 仅打印 LUN 数量，而非实际 LUN 号。

**`-l`** 仅打印 LUN，不打印数量。

**`-r`** `reporttype` 指定从目标请求的报告类型：

- `default`：返回默认报告。这是 `camcontrol` 的默认值。大多数目标如果支持 REPORT LUNS 命令，就支持此报告。
- `wellknown`：仅返回已知的 LUN。
- `all`：返回所有可用的 LUN。

**`readcap`** 向给定设备发送 SCSI READ CAPACITY 命令并显示结果。如果设备大于 2TB，将发送 SCSI READ CAPACITY (16) 服务操作以获取设备的完整大小。默认情况下，`camcontrol` 将打印设备的最后一个逻辑块和设备的块大小（字节）。要修改输出格式，请使用以下选项：

**`-b`** 仅打印块大小，不打印最后一块或设备大小。不能与 `-N` 或 `-s` 一起使用。

**`-h`** 以人类可读（以 2 为底，1K == 1024）格式打印设备大小。此选项隐含 `-N`，不能与 `-q` 或 `-b` 一起使用。

**`-H`** 以人类可读（以 10 为底，1K == 1000）格式打印设备大小。

**`-l`** 跳过发送 SCSI READ CAPACITY (10) 命令。仅发送 SCSI READ CAPACITY (16) 服务操作并报告其结果。当两者不匹配时，需要 quirk 来解决歧义。

**`-N`** 打印设备中的块数，而非最后一个逻辑块。

**`-q`** 静默模式，仅打印数字（若未指定 `-b` 或 `-s`，则以逗号分隔）。

**`-s`** 仅打印最后一个逻辑块或设备大小，省略块大小。

注意，此命令仅显示信息，不会更新内核数据结构。请使用 `camcontrol` reprobe 子命令来完成更新。

**`start`** 向给定设备发送 SCSI START STOP UNIT (0x1B) 命令，start 位置位。

**`stop`** 向给定设备发送 SCSI START STOP UNIT (0x1B) 命令，start 位清零。

**`load`** 向给定设备发送 SCSI START STOP UNIT (0x1B) 命令，start 位置位且 load/eject 位置位。

**`eject`** 向给定设备发送 SCSI START STOP UNIT (0x1B) 命令，start 位清零且 load/eject 位置位。

**`rescan`** 告诉内核扫描系统中的所有总线（使用 `all` 参数）、给定总线（XPT_SCAN_BUS）、bus:target:lun 或设备（XPT_SCAN_LUN），以查找新设备或已消失的设备。用户可以指定扫描所有总线、单条总线或一个 LUN。不支持扫描一个目标上的所有 LUN。如果通过外围设备名和单元号指定设备（例如 da4），则仅当该设备当前存在于 CAM EDT（现有设备表）中时才能重新扫描。如果设备已不存在（参见 `camcontrol` devlist），必须使用 bus:target:lun 形式重新扫描。

**`reprobe`** 告诉内核刷新设备信息并通知上层 GEOM(4)。这包括发送 SCSI READ CAPACITY 命令并更新系统其余部分可见的磁盘大小。

**`reset`** 告诉内核重置系统中的所有总线（使用 `all` 参数）、通过为该总线发出 SCSI 总线重置来重置给定总线（XPT_RESET_BUS），或重置给定的 bus:target:lun 或设备（XPT_RESET_DEV），通常是在连接到该设备后发出 BUS DEVICE RESET 消息。注意，这可能对系统产生破坏性影响。

**`defects`** 向给定设备发送 SCSI READ DEFECT DATA (10) 命令 (0x37) 或 SCSI READ DEFECT DATA (12) 命令 (0xB7)，并打印以下任意组合：缺陷总数、主缺陷列表（PLIST）和增长缺陷列表（GLIST）。如果未指定 `-P` 或 `-G`，`camcontrol` 将打印驱动器返回的 READ DEFECT DATA 头中给出的缺陷数量。如果未请求主缺陷列表或增长缺陷列表，某些驱动器会报告 0 个缺陷。

**`-f`** `format` 指定请求的缺陷列表格式。format 参数是必需的。大多数驱动器支持物理扇区格式。一些驱动器支持逻辑块格式。许多驱动器如果不支持请求的格式，会以替代格式返回数据，并附带表明不支持请求数据格式的 sense 信息。`camcontrol` 工具会尝试检测这一点，并打印驱动器返回的任何格式。如果驱动器使用非标准 sense 代码报告其不支持请求的格式，`camcontrol` 可能会将错误视为完成请求失败。格式选项有：

- `block`：以逻辑块形式打印列表。仅限于 32 位块大小，许多现代驱动器不支持。
- `longblock`：以逻辑块形式打印列表。此选项使用 64 位块大小。
- `bfi`：以 bytes from index 格式打印列表。
- `extbfi`：以扩展 bytes from index 格式打印列表。扩展格式允许打印块范围。
- `phys`：以物理扇区格式打印列表。大多数驱动器支持此格式。
- `extphys`：以扩展物理扇区格式打印列表。扩展格式允许打印块范围。

**`-G`** 打印增长缺陷列表。这是磁盘出厂后已重新映射的坏块列表。

**`-P`** 打印主缺陷列表。这是出厂时存在的缺陷列表。

**`-q`** 使用 `-s` 打印状态信息时，仅打印缺陷数量。

**`-s`** 仅打印缺陷数量，不打印缺陷列表。

**`-S`** `offset` 指定缺陷列表的起始偏移量。这隐含使用 SCSI READ DEFECT DATA (12) 命令，因为 10 字节版本的命令不支持地址描述符索引字段。并非所有驱动器都支持 12 字节命令，且一些支持 12 字节命令的驱动器不支持地址描述符索引字段。

**`-X`** 以十六进制（base 16）形式而非十进制形式打印缺陷。

**`modepage`** 允许用户显示和可选地编辑 SCSI 模式页。模式页格式位于 **/usr/share/misc/scsi_modes**。可以通过在 `SCSI_MODES` 环境变量中指定不同的文件来覆盖此设置。`modepage` 命令接受多个参数：

**`-6`** 使用 6 字节 MODE 命令而非默认的 10 字节。旧设备可能不支持 10 字节 MODE 命令，而新设备可能无法用 6 字节命令报告所有模式页。如果未指定，`camcontrol` 从 10 字节命令开始，出错时回退到 6 字节。

**`-d`** 为 mode sense 禁用块描述符。

**`-D`** 显示/编辑块描述符而非模式页。

**`-L`** 使用长 LBA 块描述符。允许 LBA 数量超过 2^^32。

**`-b`** 以二进制格式显示模式页数据。

**`-e`** 此标志允许用户编辑模式页中的值。用户可以使用其 `EDITOR` 环境变量指向的文本编辑器编辑模式页值，或通过标准输入提供模式页值，使用与 `camcontrol` 显示模式页值相同的格式。如果 `camcontrol` 检测到标准输入是终端，将调用编辑器。

**`-l`** 列出所有可用的模式页。如果指定多次，还列出子页。

**`-m`** `page[,subpage]` 指定用户想要查看和/或编辑的模式页号及可选子页。除非指定了 `-l`，否则此参数是必需的。

**`-P`** `pgctl` 允许用户指定页控制字段。可能值为：

- **0** 当前值
- **1** 可更改值
- **2** 默认值
- **3** 保存的值

**`cmd`** 允许用户向任何设备发送任意 ATA 或 SCSI CDB。`cmd` 功能需要 `-c` 参数指定 SCSI CDB 或 `-a` 参数指定 ATA 命令块寄存器值。其他参数可选，取决于命令类型。命令和数据规范语法在 cam_cdbparse(3) 中有文档说明。注意：如果指定的 CDB 导致数据传入或传出 SCSI 设备，你必须指定 `-i` 或 `-o`。

**`-a`** `cmd` [args] 指定 12 个 ATA 命令块寄存器的内容（command、features、lba_low、lba_mid、lba_high、device、lba_low_exp、lba_mid_exp、lba_high_exp、features_exp、sector_count、sector_count_exp）。

**`-c`** `cmd` [args] 指定 SCSI CDB。SCSI CDB 可为 6、10、12 或 16 字节。

**`-d`** 指定 ATA 命令使用的 DMA 协议。

**`-f`** 指定 ATA 命令使用的 FPDMA (NCQ) 协议。

**`-i`** `len` `fmt` 指定要读取的数据量及其显示方式。如果格式为 ‘-’，将从设备读取 `len` 字节数据并写入标准输出。

**`-o`** `len` `fmt` [args] 指定要写入设备的数据量及要写入的数据。如果格式为 ‘-’，将从标准输入读取 `len` 字节数据并写入设备。

**`-r`** `fmt` 指定应显示 11 个结果 ATA 命令块寄存器（status、error、lba_low、lba_mid、lba_high、device、lba_low_exp、lba_mid_exp、lba_high_exp、sector_count、sector_count_exp）及其显示方式。如果格式为 ‘-’，11 个结果寄存器将以十六进制写入标准输出。

**`smpcmd`** 允许用户向设备发送任意串行管理协议（SMP）命令。`smpcmd` 功能需要 `-r` 参数指定要发送的 SMP 请求，以及 `-R` 参数指定 SMP 响应的格式。SMP 请求和响应参数的语法在 cam_cdbparse(3) 中有文档说明。注意，支持 SMP passthrough 的 SAS 适配器（至少目前已知的适配器）不接受用户请求中的 CRC 字节，也不在响应中将 CRC 字节传回给用户。因此，用户不应在请求长度中包含 CRC 字节，也不应期望响应中返回 CRC 字节。

**`-r`** `len` `fmt` [args] 指定 SMP 请求的大小（不含 CRC 字节）及 SMP 请求格式。如果格式为 ‘-’，将从标准输入读取 `len` 字节数据并作为 SMP 请求写入。

**`-R`** `len` `fmt` [args] 指定为 SMP 响应分配的缓冲区大小及 SMP 响应格式。如果格式为 ‘-’，将为响应分配 `len` 字节数据，响应将写入标准输出。

**`smprg`** 允许用户向设备发送串行管理协议（SMP）REPORT GENERAL 命令。`camcontrol` 将显示 REPORT GENERAL 命令返回的数据。如果 SMP 目标支持长响应格式，将自动请求并显示附加数据。

**`-l`** 仅请求长响应格式。并非所有 SMP 目标都支持长响应格式。此选项使 `camcontrol` 跳过发送未设置 long 位的初始 report general 请求，仅发送设置了 long 位的 report general 请求。

**`smppc`** 允许用户向设备发出串行管理协议（SMP）PHY CONTROL 命令。此功能应谨慎使用，因为它可能使设备无法访问，还可能导致数据损坏。`-p` 参数是必需的，用于指定要操作的 PHY。

**`-p`** `phy` 指定要操作的 PHY。此参数是必需的。

**`-l`** 请求长请求/响应格式。并非所有 SMP 目标都支持长响应格式。对于 PHY CONTROL 命令，这目前仅影响请求长度是否设置为非 0 值。

**`-o`** `operation` 指定 PHY 控制操作。只能指定一个 `-o` 操作。操作可以用数字（十进制、十六进制或八进制）指定，或指定以下操作名称之一：

- `nop`：无操作。指定此参数不是必需的。
- `linkreset`：向 phy 发送 LINK RESET 命令。
- `hardreset`：向 phy 发送 HARD RESET 命令。
- `disable`：向 phy 发送 DISABLE 命令。注意，LINK RESET 或 HARD RESET 命令应重新启用 phy。
- `clearerrlog`：发送 CLEAR ERROR LOG 命令。这会清除指定 phy 的错误日志计数器。
- `clearaffiliation`：发送 CLEAR AFFILIATION 命令。这会从具有与请求清除操作的 SMP 发起方相同 SAS 地址的 STP 发起方端口清除关联。
- `sataportsel`：向 phy 发送 TRANSMIT SATA PORT SELECTION SIGNAL 命令。这会使 SATA 端口选择器使用给定的 phy 作为其活动 phy，并使另一个 phy 不活动。
- `clearitnl`：向 PHY 发送 CLEAR STP I_T NEXUS LOSS 命令。
- `setdevname`：向 PHY 发送 SET ATTACHED DEVICE NAME 命令。这需要 `-d` 参数指定设备名。

**`-d`** `name` 指定附加设备名。此选项与 `-o` `setdevname` phy 操作一起使用。名称为 64 位数字，可用十进制、十六进制或八进制格式指定。

**`-m`** `rate` 设置 phy 的最小物理链路速率。这是数字参数。目前已知链路速率为：

- **0x0** 不更改当前值
- **0x8** 1.5 Gbps
- **0x9** 3 Gbps
- **0xa** 6 Gbps

可为更新的物理链路速率指定其他值。

**`-M`** `rate` 设置 phy 的最大物理链路速率。这是数字参数。已知链路速率参数参见 `-m` 参数说明。

**`-T`** `pp_timeout` 设置部分通路超时值（微秒）。有关此字段的更多信息，请参见 ANSI SAS Protocol Layer (SPL) 规范。

**`-a`** `enable|disable` 启用或禁用 SATA slumber phy 电源状态。

**`-A`** `enable|disable` 启用或禁用 SATA partial 电源状态。

**`-s`** `enable|disable` 启用或禁用 SAS slumber phy 电源状态。

**`-S`** `enable|disable` 启用或禁用 SAS partial phy 电源状态。

**`smpphylist`** 列出连接到 SAS expander 的 phys、连接到 phy 的终端设备地址，以及该设备的查询数据和连接到该设备的外围设备。查询数据和外围设备在可用时显示。

**`-l`** 为此命令使用的底层 SMP 命令启用长响应格式。

**`-q`** 仅打印连接到 CAM EDT（现有设备表）中设备的 phys。

**`smpmaninfo`** 向设备发送 SMP REPORT MANUFACTURER INFORMATION 命令并显示响应。

**`-l`** 为此命令使用的底层 SMP 命令启用长响应格式。

**`debug`** 在内核中启用 CAM 调试 printf。这需要内核配置文件中有 options CAMDEBUG。警告：启用调试 printf 目前会导致极大量的内核 printf。一旦开始，你可能难以关闭调试 printf，因为内核将忙于打印消息而无法快速响应其他请求。`debug` 功能接受多个参数：

**`-I`** 启用 CAM_DEBUG_INFO printf。

**`-P`** 启用 CAM_DEBUG_PERIPH printf。

**`-T`** 启用 CAM_DEBUG_TRACE printf。

**`-S`** 启用 CAM_DEBUG_SUBTRACE printf。

**`-X`** 启用 CAM_DEBUG_XPT printf。

**`-c`** 启用 CAM_DEBUG_CDB printf。这会使内核打印出向指定设备发送的 SCSI CDB。

**`-p`** 启用 CAM_DEBUG_PROBE printf。

- `all`：为所有设备启用调试。
- `off`：关闭所有设备的调试。
- `bus[:target[:lun]]`：为给定总线、目标或 LUN 启用调试。如果未指定 LUN 或目标和 LUN，则使用通配符。（即仅指定总线会为该总线上的所有设备启用调试 printf。）

**`tags`** 显示或设置我们尝试排队到特定设备的 "tagged openings" 或并发事务数。默认情况下，`tags` 命令不带命令特定参数（即仅通用参数）时打印可排队到该设备的 "soft" 最大事务数。要获取更详细的信息，请使用下文描述的 `-v` 参数。

**`-N`** `tags` 设置给定设备的标签数。此值必须介于内核 quirk 表中设置的最小值和最大值之间。大多数支持标记队列的设备的默认最小值为 2，最大值为 255。给定设备的最小值和最大值可通过 `-v` 开关确定。`-v` 开关对此 `camcontrol` 子命令的含义如下所述。

**`-q`** 静默模式，不报告标签数。通常在设置标签数时使用。

**`-v`** 详细标志对 *tags* 参数有特殊功能。它使 `camcontrol` 打印 XPT_GDEV_TYPE CCB 的标记队列相关字段：

- `dev_openings`：排队到给定设备的事务容量。
- `dev_active`：当前排队到设备的事务数。
- `allocated`：为设备分配的 CCB 数。
- `held`：held 计数是外围驱动程序持有的 CCB 数，这些 CCB 要么刚刚完成，要么即将释放给传输层由设备服务。held CCB 在给定设备上保留容量。
- `mintags`：这是可一次排队到设备的当前 "硬" 最小事务数。上面的 `dev_openings` 值不能低于此数。`mintags` 的默认值为 2，但对不同设备可能设置更高或更低。
- `maxtags`：这是可一次排队到设备的 "硬" 最大事务数。`dev_openings` 值不能超过此数。`maxtags` 的默认值为 255，但对不同设备可能设置更高或更低。

**`negotiate`** 显示或协商各种通信参数。某些控制器可能不支持设置或更改其中某些值。例如，Adaptec 174x 控制器不支持更改设备的同步速率或偏移。如果控制器指示不支持设置某参数，`camcontrol` 工具不会尝试设置该参数。要了解控制器支持什么，请使用 `-v` 标志。`-v` 标志对 `negotiate` 命令的含义如下所述。此外，一些控制器驱动程序不支持设置协商参数，即使底层控制器支持协商更改。一些控制器（如 Advansys 宽带控制器）支持为设备启用和禁用同步协商，但不支持设置同步协商速率。

**`-a`** 通过向设备发送 TEST UNIT READY 命令尝试使协商设置立即生效。

**`-c`** 显示或设置当前协商设置。这是默认值。

**`-D`** `enable|disable` 启用或禁用断开连接。

**`-M`** `mode` 设置 ATA 模式。

**`-O`** `offset` 设置命令延迟偏移。

**`-q`** 静默模式，不打印任何内容。通常在你想要设置参数但不需要任何状态信息时使用。

**`-R`** `syncrate` 更改设备的同步速率。同步速率是以 MHz 为单位指定的浮点值。例如，‘20.000’ 是合法值，‘20’ 也是。

**`-T`** `enable|disable` 为设备启用或禁用标记队列。

**`-U`** 显示或设置用户协商设置。默认为显示或设置当前协商设置。

**`-v`** 详细开关对 `negotiate` 子命令有特殊含义。它使 `camcontrol` 打印发送给控制器驱动的 Path Inquiry (XPT_PATH_INQ) CCB 的内容。

**`-W`** `bus_width` 指定与设备协商的总线宽度。总线宽度以位为单位指定。仅有用的值为 8、16 和 32 位。控制器必须支持相关总线宽度，设置才能生效。

通常，同步速率和偏移设置在向设备发送命令后才会对设备生效。上面的 `-a` 开关会自动向设备发送 TEST UNIT READY，使协商参数生效。

**`format`** 向指定设备发出 SCSI FORMAT UNIT 命令。*警告！警告！警告！* 低级格式化磁盘会破坏磁盘上的所有数据。使用此命令时务必极其谨慎。许多用户对并不需要低级格式化的磁盘进行低级格式化。需要低级格式化磁盘的场景相对较少。低级格式化磁盘的一个原因是在更改物理扇区大小后初始化磁盘。另一个原因是在读写请求中从磁盘收到 "medium format corrupted" 错误时尝试恢复磁盘。某些磁盘格式化时间比其他磁盘长。用户应指定足够长的超时以允许格式化完成。默认格式化超时为 3 小时，对大多数磁盘应足够。某些硬盘会在极短时间内完成格式化操作（约 5 分钟或更少）。这通常是因为驱动器并不真正支持 FORMAT UNIT 命令——它只是接受命令，等待几分钟然后返回。‘format’ 子命令接受多个修改其默认行为的参数。`-q` 和 `-y` 参数对脚本有用。

**`-q`** 静默模式，不打印任何状态消息。但此选项不会禁用问题。要禁用问题，请使用下文的 `-y` 参数。

**`-r`** 以 “仅报告” 模式运行。这会报告驱动器上已在运行的格式化状态。

**`-w`** 发出非立即格式化命令。默认情况下，`camcontrol` 发出设置了 immediate 位的 FORMAT UNIT 命令。这告诉设备在格式化实际完成前立即返回格式化命令。然后，`camcontrol` 每秒从设备收集 SCSI sense 信息以确定格式化过程的进度。如果指定了 `-w` 参数，`camcontrol` 将发出非立即格式化命令，无法打印任何信息让用户知道磁盘已格式化的百分比。

**`-y`** 不询问任何问题。默认情况下，`camcontrol` 会询问用户是否真的要格式化相关磁盘，以及默认格式化命令超时是否可接受。如果在命令行上指定了超时，则不会询问用户超时问题。

**`sanitize`** 向指定设备发出 SANITIZE 命令。*警告！警告！警告！* 磁盘上的所有数据将被销毁或变为不可访问。数据恢复是不可能的。使用此命令时务必极其谨慎。‘sanitize’ 子命令接受多个修改其默认行为的参数。`-q` 和 `-y` 参数对脚本有用。

**`-a`** `operation` 指定要执行的 sanitize 操作：

- `overwrite`：通过向设备写入用户提供的数据模式一次或多次来执行覆盖操作。模式由 `-P` 参数给出。次数由 `-c` 参数给出。
- `block`：执行块擦除操作。设备的所有块被设置为供应商定义的值，通常为零。
- `crypto`：执行加密擦除操作。加密密钥被更改以防止数据解密。
- `exitfailure`：退出先前失败的 sanitize 操作。失败的 sanitize 操作只有在以 unrestricted completion 模式运行时才能退出，该模式由 `-U` 参数提供。

**`-c`** `passes` 执行 ‘overwrite’ 操作时的次数。有效值为 1 到 31。默认为 1。

**`-I`** 执行 ‘overwrite’ 操作时，模式在连续 pass 之间反转。

**`-P`** `pattern` 执行 ‘overwrite’ 操作时使用的模式文件路径。模式按需重复以填充每个块。

**`-q`** 静默模式，不打印任何状态消息。但此选项不会禁用问题。要禁用问题，请使用下文的 `-y` 参数。

**`-U`** 以 unrestricted completion 模式执行 sanitize。如果操作失败，稍后可用 ‘exitfailure’ 操作退出。

**`-r`** 以 “仅报告” 模式运行。这会报告驱动器上已在运行的 sanitize 状态。

**`-w`** 发出非立即 sanitize 命令。默认情况下，`camcontrol` 发出设置了 immediate 位的 SANITIZE 命令。这告诉设备在 sanitize 实际完成前立即返回 sanitize 命令。然后，`camcontrol` 每秒从设备收集 SCSI sense 信息以确定 sanitize 过程的进度。如果指定了 `-w` 参数，`camcontrol` 将发出非立即 sanitize 命令，无法打印任何信息让用户知道磁盘已 sanitize 的百分比。

**`-y`** 不询问任何问题。默认情况下，`camcontrol` 会询问用户是否真的要 sanitize 相关磁盘，以及默认 sanitize 命令超时是否可接受。如果在命令行上指定了超时，则不会询问用户超时问题。

**`idle`** 将 ATA 设备置于 IDLE 状态。可选参数（`-t`）以秒为单位指定自动 standby 定时器值。值 0 禁用定时器。

**`standby`** 将 ATA 设备置于 STANDBY 状态。可选参数（`-t`）以秒为单位指定自动 standby 定时器值。值 0 禁用定时器。

**`sleep`** 将 ATA 设备置于 SLEEP 状态。注意，使设备退出此状态的唯一方法可能是重置。

**`powermode`** 报告 ATA 设备电源模式。

**`apm`** 若指定可选参数（`-l`），则启用并设置高级电源管理级别，其中 1——最低功耗，127——带 standby 的最大性能，128——不带 standby 的最低功耗，254——最大性能。如果未指定——禁用 APM。

**`aam`** 若指定可选参数（`-l`），则启用并设置自动声学管理级别，其中 1——最低噪声，254——最大性能。如果未指定——禁用 AAM。

**`security`** 使用 ATA IDENTIFY 命令 (0xec) 更新或报告安全设置。默认情况下，`camcontrol` 将打印设备的安全支持和相关设置。`security` 命令接受多个参数：如果为任何操作命令指定的密码与指定用户配置的密码不匹配，命令将失败。所有情况下密码限制为 32 个字符，更长的密码将失败。

**`-d`** `pwd` 根据设备配置的安全级别，使用给定密码为选定用户禁用设备安全。

**`-e`** `pwd` 使用给定密码为选定用户擦除设备。*警告！警告！警告！* 发出安全擦除将 *擦除所有* 用户数据，可能需要数小时才能完成。对 SSD 驱动器使用此命令时，其所有单元将被标记为空，恢复到出厂默认写入性能。对于 SSD，此操作通常只需几秒。

**`-f`** 冻结指定设备的安全配置。命令完成后，任何其他更新设备锁定模式的命令将被中止。冻结模式通过断电或硬件重置禁用。

**`-h`** `pwd` 使用给定密码为选定用户增强擦除设备。*警告！警告！警告！* 发出增强安全擦除将 *擦除所有* 用户数据，可能需要数小时才能完成。增强擦除向所有用户数据区域写入预定的数据模式，所有先前写入的用户数据将被覆盖，包括由于重新分配而不再使用的扇区。

**`-k`** `pwd` 根据设备配置的安全级别，使用给定密码为选定用户解锁设备。

**`-l`** `high|maximum` 指定发出 `-s` `pwd` 命令时设置的安全级别。安全级别决定使用主密码解锁设备时的设备行为。当安全级别设置为 high 时，设备需要 unlock 命令和主密码来解锁。当安全级别设置为 maximum 时，设备需要使用主密码进行安全擦除来解锁。此选项必须与某个安全操作命令一起使用。默认为 *high*

**`-q`** 静默模式，不打印任何状态消息。但此选项不会禁用问题。要禁用问题，请使用下文的 `-y` 参数。

**`-s`** `pwd` 使用给定密码为选定用户对设备设置密码（启用安全）。此选项可与其他选项组合使用，如 `-e` *pwd*。除用户密码外，还可设置主密码。主密码的目的是允许管理员建立一个对用户保密的密码，用于在用户密码丢失时解锁设备。*注意：* 设置主密码不会启用设备安全。如果设置了主密码且驱动器支持 Master Revision Code 功能，Master Password Revision Code 将递减。

**`-T`** `timeout` 覆盖默认超时（秒），用于 `-e` 和 `-h`。如果你的系统在正确处理长超时方面有问题，这很有用。通常超时根据驱动器上存储的信息（如果存在）计算，否则默认为 2 小时。

**`-U`** `user|master` 指定为当前操作命令设置/使用的用户，有效值为 user 或 master，未设置时默认为 master。此选项必须与某个安全操作命令一起使用。默认为 *master*

**`-y`** 对危险选项（如 `-e`）确认 yes 而不提示确认。

**`hpa`** 更新或报告主机保护区域（Host Protected Area）详情。默认情况下，`camcontrol` 将打印设备的 HPA 支持和相关设置。`hpa` 命令接受多个可选参数：所有 HPA 命令的密码限制为 32 个字符，更长的密码将失败。

**`-f`** 冻结指定设备的 HPA 配置。命令完成后，任何其他更新 HPA 配置的命令将被中止。冻结模式通过断电或硬件重置禁用。

**`-l`** 锁定设备的 HPA 配置，直到成功调用 unlock 或下一次上电重置。

**`-P`** 使 HPA max sectors 在上电重置或硬件重置后持久存在。必须与 `-s` `max_sectors` 一起使用。

**`-p`** `pwd` 设置 unlock 调用所需的 HPA 配置密码。

**`-q`** 静默模式，不打印任何状态消息。此选项不会禁用问题。要禁用问题，请使用下文的 `-y` 参数。

**`-s`** `max_sectors` 配置设备的最大用户可访问扇区。这将更改设备报告的扇区数。*警告！警告！警告！* 使用此选项更改设备的 max sectors 将使设备上超出指定值的数据变为不可访问。在没有上电重置或硬件重置设备的情况下，只能进行一次成功的 `-s` `max_sectors` 调用。

**`-U`** `pwd` 使用给定密码解锁指定设备的 HPA 配置。如果指定的密码与通过 `-p` `pwd` 配置的密码不匹配，命令将失败。由于密码不匹配导致 5 次失败的 unlock 调用后，设备将拒绝额外的 unlock 调用，直到上电重置后。

**`-y`** 对危险选项（如 `-e`）确认 yes 而不提示确认。

**`ama`** 更新或报告可访问最大地址配置（Accessible Max Address Configuration）。默认情况下，`camcontrol` 将打印设备的可访问最大地址配置支持和相关设置。`ama` 命令接受多个可选参数：

**`-f`** 冻结指定设备的可访问最大地址配置。命令完成后，任何其他更新配置的命令将被中止。冻结模式通过断电禁用。

**`-q`** 静默模式，不打印任何状态消息。

**`-s`** `max_sectors` 配置设备的最大用户可访问扇区。这将更改设备报告的扇区数。*警告！警告！警告！* 使用此选项更改设备的 max sectors 将使设备上超出指定值的数据变为不确定。在没有上电重置设备的情况下，只能进行一次成功的 `-s` `max_sectors` 调用。

**`fwdownload`** 使用提供的镜像文件为指定的 SCSI 或 ATA 设备编程固件。如果设备是 SCSI 设备且为 WRITE BUFFER 命令提供推荐超时（参见 `camcontrol` opcodes 子命令），该超时将用于固件下载。驱动器推荐的超时值可在命令行上用 `-t` 选项覆盖。SCSI/SAS 驱动器当前支持的供应商列表：*警告！警告！警告！* 为确保每个供应商的不同设备型号能正确与 fwdownload 命令配合工作，所做测试很少。出现在支持列表中的供应商名仅表示该供应商至少有一种设备类型的固件已成功通过 fwdownload 命令编程。使用此命令时应格外谨慎，因为无法保证它不会损坏所列供应商的设备。在执行固件更新前，请确保已对设备上的数据进行最近备份。注意，未知的 SCSI 协议设备不会被编程，因为固件下载成功的可能性很小。`camcontrol` 目前会尝试向任何 ATA 或 SATA 设备下载固件，因为标准的 ATA DOWNLOAD MICROCODE 命令可能有效。连接到标准 ATA 和 SATA 控制器的设备，以及连接到具有 SCSI 到 ATA 转换能力的 SAS 控制器的设备，支持向 ATA 和 SATA 设备下载固件。在后一种情况下，`camcontrol` 使用 SCSI ATA PASS-THROUGH 命令向驱动器发送 ATA DOWNLOAD MICROCODE 命令。一些 SCSI 到 ATA 转换实现在将 SCSI WRITE BUFFER 命令转换为 ATA DOWNLOAD MICROCODE 命令时不能完全工作，但足够支持 ATA passthrough 来进行固件下载。

当前支持的 SCSI/SAS 驱动器供应商列表：

- **HGST**：已使用 4TB SAS 驱动器（型号 HUS724040ALS640）测试。
- **HITACHI**
- **HP**
- **IBM**：已使用 LTO-5 (ULTRIUM-HH5) 和 LTO-6 (ULTRIUM-HH6) 磁带驱动器测试。硬盘有单独的表条目，因为硬盘的更新方法与磁带驱动器不同。
- **PLEXTOR**
- **QUALSTAR**
- **QUANTUM**
- **SAMSUNG**：已使用 SM1625 SSD 测试。
- **SEAGATE**：已使用 Constellation ES (ST32000444SS)、ES.2 (ST33000651SS) 和 ES.3 (ST1000NM0023) 驱动器测试。
- **SmrtStor**：已使用 400GB Optimus SSD (TXA2D20400GA6001) 测试。
- **TOSHIBA**：已使用 22TB MG10SFA22TE SAS 驱动器测试。

**`-f`** `fw_image` 要下载到指定设备的固件镜像文件路径。

**`-q`** 不打印信息性消息，仅打印错误。此选项应与 `-y` 选项一起使用以抑制所有输出。

**`-s`** 以模拟模式运行。运行设备检查并显示确认对话框，但不会发生固件下载。

**`-v`** 在失败时显示 SCSI 或 ATA 错误。在模拟模式下，打印将用于固件下载命令的 SCSI CDB 或 ATA 寄存器值。

**`-y`** 不要求确认。

**`persist`** 持久预留支持。持久预留是一种为一个或多个 SCSI 发起方预留特定 SCSI LUN 的方法。如果指定了 `-i` 选项，`camcontrol` 将使用请求的服务操作发出 SCSI PERSISTENT RESERVE IN 命令。如果指定了 `-o` 选项，`camcontrol` 将使用请求的服务操作发出 SCSI PERSISTENT RESERVE OUT 命令。这两个选项之一是必需的。持久预留很复杂，完整解释超出了本手册的范围。请访问 https://www.t10.org 下载最新的 SPC 规范以获取持久预留的完整解释。

**`-i`** `mode` 指定 PERSISTENT RESERVE IN 命令的服务操作。支持的服务操作：

- `read_keys`：报告当前持久预留生成（PRgeneration）和任何已注册的密钥。
- `read_reservation`：报告持久预留（如果有）。
- `report_capabilities`：报告 LUN 的持久预留能力。
- `read_full_status`：报告 LUN 上持久预留的完整状态。

**`-o`** `mode` 指定 PERSISTENT RESERVE OUT 命令的服务操作。对于像 register 这样作为其他服务操作名称组成部分的服务操作，必须指定完整名称。否则，必须指定足够多的服务操作名称以将其与其他可能的服务操作区分开。支持的服务操作：

- `register`：向 LUN 注册预留密钥或取消注册预留密钥。要注册密钥，将请求的密钥指定为 Service Action Reservation Key。要取消注册密钥，将先前注册的密钥指定为 Reservation Key。要更改密钥，将旧密钥指定为 Reservation Key，新密钥指定为 Service Action Reservation Key。
- `register_ignore`：类似于 register 子命令，但忽略 Reservation Key。Service Action Reservation Key 将覆盖为发起方注册的任何先前密钥。
- `reserve`：创建预留。在预留 LUN 之前必须向 LUN 注册密钥，并将其指定为 Reservation Key。还必须指定预留类型。范围默认为 LUN 范围（LU_SCOPE），但可以更改。
- `release`：释放预留。必须指定 Reservation Key。
- `clear`：释放预留并从设备中删除所有密钥。必须指定 Reservation Key。
- `preempt`：删除属于另一个发起方的预留。必须指定 Reservation Key。根据执行的操作，可能需要指定 Service Action Reservation Key。
- `preempt_abort`：删除属于另一个发起方的预留并中止该发起方的所有未完成命令。必须指定 Reservation Key。根据执行的操作，可能需要指定 Service Action Reservation Key。
- `register_move`：向 LUN 注册另一个发起方，并为该发起方在 LUN 上建立预留。必须指定 Reservation Key 和 Service Action Reservation Key。
- `replace_lost`：替换丢失的预留信息。

**`-a`** 设置 All Target Ports (ALL_TG_PT) 位。这请求将密钥注册应用于所有目标端口，而不仅仅是接收命令的特定目标端口。这仅适用于 register 和 register_ignore 操作。

**`-I`** `tid` 指定 Transport ID。这仅适用于 Persistent Reserve Out 的 Register 和 Register and Move 服务操作。可以通过多个 `-I` 参数指定多个 Transport ID。使用 Register 服务操作时，指定一个或多个 Transport ID 会隐式启用 `-S` 选项，该选项打开 SPEC_I_PT 位。Transport ID 通常具有 protocol,id 格式。

Transport ID 示例：

```sh
sas,0x1234567812345678
```

```sh
fcp,0x1234567812345678
```

```sh
spi,4,1
```

```sh
sbp,0x1234567812345678
```

```sh
srp,0x12345678123456781234567812345678
```

```sh
iqn.2012-06.com.example:target0
```

```sh
iqn.2012-06.com.example:target0,i,0x123
```

```sh
sop,4,5,1
```

```sh
sop,4,1
```

- **SAS**：SAS Transport ID 由 “sas,” 加 64 位 SAS 地址组成。例如：
- **FC**：Fibre Channel Transport ID 由 “fcp,” 加 64 位 Fibre Channel World Wide Name 组成。例如：
- **SPI**：Parallel SCSI 地址由 “spi,” 加 SCSI 目标 ID 和相对目标端口标识符组成。例如：
- **1394**：IEEE 1394 (Firewire) Transport ID 由 “sbp,” 加 64 位 EUI-64 IEEE 1394 节点唯一标识符组成。例如：
- **RDMA**：SCSI over RDMA Transport ID 由 “srp,” 加 128 位 RDMA 发起方端口标识符组成。端口标识符必须恰好为 32 或 34（如果包含前导 0x）个十六进制数字。仅支持十六进制（base 16）数字。例如：
- **iSCSI**：iSCSI Transport ID 由 iSCSI 名称和可选的分隔符及 iSCSI 会话 ID 组成。例如，如果仅指定 iSCSI 名称：如果指定了 iSCSI 分隔符和发起方会话 ID：
- **PCIe**：SCSI over PCIe Transport ID 由 “sop,” 加 PCIe Routing ID 组成。Routing ID 由总线、设备和功能组成，或以替代形式由总线和功能组成。总线必须在 0 到 255 范围内（含），设备必须在 0 到 31 范围内（含）。如果使用标准形式，功能必须在 0 到 7 范围内（含），如果使用替代形式，功能必须在 0 到 255 范围内（含）。例如，如果为标准 Routing ID 形式指定了总线、设备和功能：如果使用替代 Routing ID 形式：

**`-k`** `key` 指定 Reservation Key。这可以是十进制、八进制或十六进制格式。如果未另行指定，默认值为零。值必须在 0 到 2^64 - 1 之间（含）。

**`-K`** `key` 指定 Service Action Reservation Key。这可以是十进制、八进制或十六进制格式。如果未另行指定，默认值为零。值必须在 0 到 2^64 - 1 之间（含）。

**`-p`** 启用 Activate Persist Through Power Loss 位。这仅用于 register 和 register_ignore 操作。这请求预留在断电事件后持久存在。

**`-s`** `scope` 指定预留的范围。范围可以按名称或数字指定。范围对于 register、register_ignore 和 clear 被忽略。如果所需范围无法通过名称获得，可以指定数字。

- `lun`：LUN 范围 (0x00)。这涵盖整个 LUN。
- `extent`：Extent 范围 (0x01)。
- `element`：Element 范围 (0x02)。

**`-R`** `rtp` 指定 Relative Target Port。这仅适用于 Persistent Reserve Out 命令的 Register and Move 服务操作。

**`-S`** 启用 SPEC_I_PT 位。这仅适用于 Persistent Reserve Out 的 Register 服务操作。如果设置此选项，你还必须使用 `-I` 指定至少一个 Transport ID。如果指定 Transport ID，此选项会自动设置。为 Register 以外的任何服务操作指定此选项是错误的。

**`-T`** `type` 指定预留类型。预留类型可以按名称或数字指定。如果所需预留类型无法通过名称获得，可以指定数字。支持的预留类型名称：

- `read_shared`：Read Shared 模式。
- `wr_ex`：Write Exclusive 模式。也可指定为 “write_exclusive”。
- `rd_ex`：Read Exclusive 模式。也可指定为 “read_exclusive”。
- `ex_ac`：Exclusive Access 模式。也可指定为 “exclusive_access”。
- `wr_ex_ro`：Write Exclusive Registrants Only 模式。也可指定为 “write_exclusive_reg_only”。
- `ex_ac_ro`：Exclusive Access Registrants Only 模式。也可指定为 “exclusive_access_reg_only”。
- `wr_ex_ar`：Write Exclusive All Registrants 模式。也可指定为 “write_exclusive_all_regs”。
- `ex_ac_ar`：Exclusive Access All Registrants 模式。也可指定为 “exclusive_access_all_regs”。

**`-U`** 指定目标应取消注册发送 Register and Move 请求的发起方。默认情况下，目标不会取消注册发送 Register and Move 请求的发起方。此选项仅适用于 Persistent Reserve Out 命令的 Register and Move 服务操作。

**`attrib`** 发出 SCSI READ 或 WRITE ATTRIBUTE 命令。这些命令用于在介质辅助内存（Medium Auxiliary Memory，MAM）中读取和写入属性。介质辅助内存最常见于磁带盒中包含的小型闪存芯片。例如，LTO 磁带具有 MAM。必须指定 `-r` 或 `-w` 选项之一。

**`-r`** `action` 指定 READ ATTRIBUTE 服务操作：

- `attr_values`：发出 ATTRIBUTE VALUES 服务操作。读取并解码可用属性及其值。
- `attr_list`：发出 ATTRIBUTE LIST 服务操作。列出可读写的属性。
- `lv_list`：发出 LOGICAL VOLUME LIST 服务操作。列出 MAM 中可用的逻辑卷。
- `part_list`：发出 PARTITION LIST 服务操作。列出 MAM 中可用的分区。
- `supp_attr`：发出 SUPPORTED ATTRIBUTES 服务操作。列出支持读写的属性。这些属性可能存在于 MAM 中，也可能不存在。
- `text_esc`：以转义的非 ASCII 字符打印文本字段。
- `text_raw`：以本机方式打印文本字段，不进行代码集转换。
- `nonascii_esc`：如果本应为 ASCII 的字段中出现任何非 ASCII 字符，则转义非 ASCII 字符。
- `nonascii_trim`：如果本应为 ASCII 的字段中出现任何非 ASCII 字符，则省略非 ASCII 字符。
- `nonascii_raw`：如果本应为 ASCII 的字段中出现任何非 ASCII 字符，则按原样打印。
- `field_all`：打印所有前缀字段：description、attribute number、attribute size 和 attribute 的 readonly 状态。如果指定了 field_all，指定任何其他字段选项将无效。
- `field_none`：不打印任何前缀字段，仅打印属性值。如果指定了 field_none，指定任何其他字段选项将导致这些字段被打印。
- `field_desc`：打印属性描述。
- `field_num`：打印属性号。
- `field_size`：打印属性大小。
- `field_rw`：打印属性的 readonly 状态。

**`-w`** `attr` 指定要写入 MAM 的属性。此选项尚未实现。

**`-a`** `num` 指定要显示的属性号。此选项仅适用于 `-r` 的 attr_values、attr_list 和 supp_attr 参数。

**`-c`** 显示缓存的属性。如果设备支持此标志，它允许显示驱动器中最后装入的介质的属性。

**`-e`** `num` 指定元素地址。用于指定读取属性时要访问的介质更换器中的元素号。元素号可以是 picker、portal、slot 或 drive。

**`-F`** `form1,form2` 以逗号分隔的选项列表形式指定属性值（attr_val）显示的输出格式。默认输出当前设置为 field_all,nonascii_trim,text_raw。一旦此代码移植到 FreeBSD 10，任何文本字段都将使用 iconv(3) 从其代码集转换为用户的本机代码集。text 选项互斥；如果指定多个，将得到不可预测的结果。nonascii 选项也互斥。大多数 field 选项可以逻辑 OR 组合。

**`-p`** `part` 指定分区。当介质有多个分区时，指定不同的分区号可以查看每个单独分区的值。

**`-s`** `start_num` 指定起始属性号。这请求目标设备从给定号开始返回属性信息。

**`-T`** `elem_type` 指定元素类型。对于介质更换器设备，这允许指定元素地址（`-e`）中引用的元素类型。有效类型为：“all”、“picker”、“slot”、“portal” 和 “drive”。

**`-V`** `vol_num` 指定要操作的逻辑卷号。如果介质有多个逻辑卷，这允许在给定逻辑卷上显示或写入属性。

**`opcodes`** 发出 SCSI MAINTENANCE IN 命令的 REPORT SUPPORTED OPCODES 服务操作。不带参数时，此命令返回设备支持的所有 SCSI 命令列表，包括支持服务操作的命令的服务操作。它还将包括每个命令的 SCSI CDB（Command Data Block）长度，以及每个命令的描述（如果已知）。

**`-o`** `opcode` 请求特定 opcode 的信息，而非支持的命令列表。如果支持，目标将返回类似 CDB 的结构，指示 opcode、服务操作（如果有）以及该 CDB 中支持的位掩码。

**`-s`** `service_action` 对于支持服务操作的命令，指定要查询的服务操作。

**`-N`** 如果为给定 opcode 指定了服务操作，而设备不支持该服务操作，设备不应返回 SCSI 错误，而应在返回的参数数据中指示不支持该命令。默认情况下，如果为 opcode 指定了服务操作而该 opcode 不支持服务操作，设备将返回错误。

**`-T`** 包含超时值。此选项适用于默认显示（包括设备支持的所有命令）以及 `-o` 和 `-s` 选项（请求特定命令和服务操作的信息）。这请求设备报告给定命令的 Nominal 和 Recommended 超时值。超时值以秒为单位。超时描述符还包括特定于命令的

**`zone`** 管理 SCSI 和 ATA 分区块设备。这允许管理符合 SCSI Zoned Block Commands (ZBC) 和 ATA Zoned ATA Command Set (ZAC) 规范的设备。使用这些命令集的设备通常是使用叠瓦式磁记录（Shingled Magnetic Recording，SMR）的硬盘。SMR 驱动器有三种类型：SMR 驱动器被划分为区域（通常每个 256MB 左右），分为三大类：

- **Drive Managed**（驱动器管理）：托管驱动器的外观和行为就像标准的随机访问块设备，但在底层，驱动器使用 SMR 区域读取和写入其大部分容量。顺序写入将产生更好的性能，但不要求顺序写入。
- **Host Aware**（主机感知）：主机感知驱动器通过 SCSI 或 ATA 命令公开底层区域布局，并允许主机管理区域状态。但不要求主机管理驱动器上的区域。在 Sequential Write Preferred 区域中，顺序写入将产生更好的性能，但主机可以在这些区域中随机写入。
- **Host Managed**（主机托管）：主机托管驱动器通过 SCSI 或 ATA 命令公开底层区域布局。主机必须按照区域布局描述的规则访问区域。任何违反规则的命令都将返回错误。

SMR 驱动器分为三类区域：

- **Conventional**（常规）：也称为 Non Write Pointer 区域。这些区域可以随机写入，不会有意外的性能损失。
- **Sequential Preferred**（顺序优先）：这些区域应从区域的写指针开始顺序写入。它们可以随机写入。不符合区域布局的写入可能比预期慢得多。
- **Sequential Required**（顺序必需）：这些区域必须顺序写入。如果不从写指针开始顺序写入，命令将失败。

**`-c`** `cmd` 指定 zone 子命令：

- `rz`：发出 REPORT ZONES 命令。默认返回所有区域。使用 `-o` 指定报告选项，使用 `-P` 指定打印选项。使用 `-l` 指定起始 LBA。注意，也接受 “reportzones” 作为命令参数。
- `open`：显式打开由起始 LBA 指定的区域。
- `close`：关闭由起始 LBA 指定的区域。
- `finish`：完成由起始 LBA 指定的区域。
- `rwp`：重置由起始 LBA 指定的区域的写指针。

**`-a`** 对于 Open、Close、Finish 和 Reset Write Pointer 操作，将操作应用于驱动器上的所有区域。

**`-l`** `lba` 指定起始 LBA。对于 REPORT ZONES 命令，这告诉驱动器从给定 LBA 开始的区域开始报告。对于其他命令，这允许用户通过起始 LBA 标识请求的区域。LBA 可以用十进制、十六进制或八进制表示法指定。

**`-o`** `rep_opt` 对于 REPORT ZONES 命令，指定要报告的区域子集：

- `all`：报告所有区域。这是默认值。
- `empty`：仅报告空区域。
- `imp_open`：报告隐式打开的区域。这意味着主机在未显式打开区域的情况下向该区域发送了写入。
- `exp_open`：报告显式打开的区域。
- `closed`：报告主机已关闭的区域。
- `full`：报告已满的区域。
- `ro`：报告处于只读状态的区域。注意，也接受 “readonly” 作为参数。
- `offline`：报告处于离线状态的区域。
- `reset`：报告设备建议重置写指针的区域。
- `nonseq`：报告设置了 Non Sequential Resources Active 标志的区域。这些区域是 Sequential Write Preferred，但已被非顺序写入。
- `nonwp`：报告 Non Write Pointer 区域，也称为 Conventional 区域。

**`-P`** `print_opt` 指定 REPORT ZONES 的打印选项：

- `normal`：正常 Report Zones 输出。这是默认值。打印摘要和列标题，字段以空格分隔，字段本身可以包含空格。
- `summary`：仅打印摘要：区域数、最大 LBA（驱动器上最后一个逻辑块的 LBA）和 “same” 字段的值。“same” 字段描述驱动器上的区域是全部相同、全部不同，还是除最后一个区域外都相同等。
- `script`：以脚本友好格式打印区域。省略摘要和列标题，字段以逗号分隔，字段不包含空格。字段在通常使用空格的地方包含下划线。

**`epc`** 发出 ATA 扩展电源条件（Extended Power Conditions，EPC）功能集命令。这仅适用于 ATA 协议驱动器，不适用于 SCSI 协议驱动器。它适用于 SCSI 到 ATA 转换层（SAT）后面的 SATA 驱动器。阅读 t13.org 上提供的 ATA Command Set - 4 (ACS-4) 中有关扩展电源条件功能集的描述可能有助于理解此特定 `camcontrol` 子命令的细节。

**`-c`** `cmd` 指定 epc 子命令：

- `restore`：恢复驱动器电源条件设置。
- `goto`：转到指定的电源条件。
- `timer`：为电源条件设置定时器值并启用或禁用该条件。参见下文描述的 “list” 显示以查看驱动器支持的每个 Idle 和 Standby 模式的当前定时器设置。
- `state`：启用或禁用特定电源条件。
- `enable`：启用扩展电源条件（EPC）功能集。
- `disable`：禁用扩展电源条件（EPC）功能集。
- `source`：指定 EPC 电源来源。
- `status`：获取与扩展电源条件（EPC）功能集相关的多个参数的当前状态，包括是否支持和启用 APM 和 EPC、是否支持 Low Power Standby、是否支持设置 EPC 电源来源、是否支持 Low Power Standby 以及当前电源条件。
- `list`：显示 ATA Power Conditions 日志（Log Address 0x08）。这显示驱动器支持的 Idle 和 Standby 电源条件列表，以及每个条件的多个参数，包括是否启用及定时器值。

**`-r`** `src` 指定恢复电源设置的来源，“default” 或 “saved”。此参数是必需的。

**`-s`** 保存设置。仅在从默认值恢复时指定才有意义。

**`-p`** `cond` 指定电源条件：Idle_a、Idle_b、Idle_c、Standby_y、Standby_z。此参数是必需的。

**`-D`** 指定延迟进入电源条件。如果驱动器支持，可在命令完成后进入电源条件。

**`-H`** 保持电源条件。如果驱动器支持此选项，它将保持电源条件并拒绝所有通常会使其退出该电源条件的命令。

**`-e`** 启用电源条件。`-e` 或 `-d` 之一是必需的。

**`-d`** 禁用电源条件。`-d` 或 `-e` 之一是必需的。

**`-T`** `timer` 以秒为单位指定定时器。用户可以指定浮点数作为定时器，最大支持分辨率为十分之一秒。驱动器可能支持也可能不支持亚秒级定时器值。

**`-p`** `cond` 指定电源条件：Idle_a、Idle_b、Idle_c、Standby_y、Standby_z。此参数是必需的。

**`-s`** 保存定时器和电源条件启用/禁用状态。默认情况下，如果未指定此选项，仅影响此电源条件的当前值。

**`-e`** 启用电源条件。`-e` 或 `-d` 之一是必需的。

**`-d`** 禁用电源条件。`-d` 或 `-e` 之一是必需的。

**`-p`** `cond` 指定电源条件：Idle_a、Idle_b、Idle_c、Standby_y、Standby_z。此参数是必需的。

**`-s`** 保存电源条件启用/禁用状态。默认情况下，如果未指定此选项，仅影响此电源条件的当前值。

**`-S`** `src` 指定电源来源，“battery” 或 “nonbattery”。

**`-P`** 仅报告当前电源条件。某些驱动器在收到 ATA CHECK POWER MODE 命令以外的命令时会退出当前电源条件。如果指定此标志，`camcontrol` 将仅向驱动器发出 ATA CHECK POWER MODE 命令。

**`timestamp`** 发出 REPORT TIMESTAMP 或 SET TIMESTAMP SCSI 命令。必须指定 `-r` 或 `-s` 选项之一。

**`-f`** `format` 指定 strftime 格式字符串（如 strftime(3) 所述），用于格式化报告的时间戳。

**`-m`** 以自纪元以来的毫秒数报告时间戳。

**`-U`** 使用日期和时间的国家表示形式报告时间戳，但覆盖系统时区并使用 UTC。

**`-r`** 报告设备的时间戳。如果未指定更多参数，时间戳将使用日期和时间的国家表示形式报告，后跟时区。

**`-f`** `format` 指定 strptime 格式字符串（如 strptime(3) 所述）。还必须使用 `-T` 选项指定时间。

**`-T`** `time` 以 `-f` 选项指定的格式提供时间。

**`-U`** 将设备时间戳设置为主机系统的 UTC 时间。

**`-s`** 设置设备的时间戳。必须指定 `-f` 和 `-T` 选项或 `-U` 选项。

**`devtype`** 打印指定设备的设备类型。

- `ata`：直接连接到 ATA 控制器的 ATA 设备
- `satl`：通过 SCSI-ATA 转换层（SATL）连接到 SAS 控制器后面的 SATA 设备
- `scsi`：SCSI 设备
- `nvme`：直接连接的 NVMe 设备
- `mmcsd`：通过 mmcsd 总线连接的 MMC 或 SD 设备
- `none`：未报告设备类型
- `unknown`：设备类型未知
- `illegal`：发生编程错误

**`depop`** 支持设备缺陷元素（通常为硬盘的磁头）去populate（depop）或设置容量点（通常用于闪存驱动器）所需的命令。发出 GET PHYSICAL ELEMENT STATUS、REMOVE ELEMENT AND TRUNCATE 或 RESTORE ELEMENT AND REBUILD 命令来管理驱动器的存储元素。元素移除或恢复可能需要长达一天才能完成。必须指定 `-d`、`-l` 或 `-r` 选项之一。这些选项互斥。仅支持 SCSI 驱动器。更改存储驱动器的存储元素可能导致该存储驱动器上的所有数据丢失。驱动器在 `-d` 或 `-r` 命令后可能需要重新初始化。在这些命令完成之前，驱动器上的数据不可访问。一旦这些命令之一开始，驱动器在操作成功完成之前处于格式损坏状态。在格式损坏期间，无法对驱动器进行读或写 I/O。如果驱动器电源循环，它将保持格式损坏状态，必须重新启动操作。TEST UNIT READY 或 “camcontrol tur” 可以监视进行中的 depop 操作。

**`-c`** `capacity` 指定驱动器的所需容量点。仅对 `-d` 标志有效。

**`-d`** 将物理元素从服务中移除或设置 `-e` 或 `-c` 标志指定的容量点。驱动器的容量可能因此操作而减少。

**`-e`** `element` 指定要从服务中移除的物理元素。仅对 `-d` 标志有效。

**`-l`** 报告驱动器物理元素的当前状态。

**`-r`** 将所有合格的物理元素恢复到服务中。

**`help`** 打印详细的用法信息。

## 环境变量

`SCSI_MODES` 变量允许用户指定替代的模式页格式文件。

`EDITOR` 变量决定 `camcontrol` 在编辑模式页时启动哪个文本编辑器。

## 文件

**/usr/share/misc/scsi_modes** 是 SCSI 模式格式数据库。

**/dev/xpt0** 是传输层设备。

**/dev/pass\*** 是 CAM 应用程序 passthrough 设备。

## 实例

从 cd1 弹出 CD，并在命令失败时打印 SCSI sense 信息：

```sh
camcontrol eject -n cd -u 1 -v
```

向 da0 发送 SCSI TEST UNIT READY 命令。`camcontrol` 工具将报告磁盘是否就绪，但由于未指定 `-v` 开关，如果命令失败，不会显示 sense 信息：

```sh
camcontrol tur da0
```

向 da1 发送 TEST UNIT READY 命令。启用内核错误恢复。指定重试次数为 4，超时为 50 秒。如果命令失败，启用 sense 打印（使用 `-v` 标志）。由于启用了错误恢复，如果磁盘当前未旋转，将启动磁盘。命令的 SCSI 任务属性将设置为 Head of Queue。`camcontrol` 工具将报告磁盘是否就绪：

```sh
camcontrol tur da1 -E -C 4 -t 50 -Q head -v
```

向 cd1 发出 READ BUFFER 命令 (0x3C)。显示 cd1 的缓冲区大小，并显示 cd1 缓存中的前 10 个字节。如果命令失败，显示 SCSI sense 信息：

```sh
camcontrol cmd -n cd -u 1 -v -c "3C 00 00 00 00 00 00 00 0e 00" e
	-i 0xe "s1 i3 i1 i1 i1 i1 i1 i1 i1 i1 i1 i1"
```

向 cd1 发出 WRITE BUFFER (0x3B) 命令。写入 10 字节数据，不包括（保留的）4 字节头。如果命令失败，打印 sense 信息。使用此命令要非常小心，不当使用可能导致数据损坏：

```sh
camcontrol cmd -n cd -u 1 -v -c "3B 00 00 00 00 00 00 00 0e 00" e
	-o 14 "00 00 00 00 1 2 3 4 5 6 v v v v" 7 8 9 8
```

为 da3 编辑模式页 1（读写错误恢复页）并保存设置到驱动器。模式页 1 包含磁盘驱动器的自动读写重新分配设置等内容：

```sh
camcontrol modepage da3 -m 1 -e -P 3
```

重新扫描系统中的所有 SCSI 总线，查找已添加、移除或更改的设备：

```sh
camcontrol rescan all
```

重新扫描 SCSI 总线 0，查找已添加、移除或更改的设备：

```sh
camcontrol rescan 0
```

重新扫描 SCSI 总线 0、目标 1、LUN 0，查看是否已添加、移除或更改：

```sh
camcontrol rescan 0:1:0
```

将 da5 的并发事务数设置为 24：

```sh
camcontrol tags da5 -N 24
```

为 da4 禁用标记队列：

```sh
camcontrol negotiate -n da -u 4 -T disable
```

与 da3 协商 20MHz 的同步速率和 15 的偏移。然后发送 TEST UNIT READY 命令使设置生效：

```sh
camcontrol negotiate -n da -u 3 -R 20.000 -O 15 -a
```

向 ses0 发送 SMP REPORT GENERAL 命令，并显示它包含的 PHY 数量，如果命令失败则显示 SMP 错误：

```sh
camcontrol smpcmd ses0 -v -r 4 40 0 00 0 -R 1020 s9 i1
```

报告 ada0 的安全支持和设置：

```sh
camcontrol security ada0
```

使用密码 MyPass 在设备 ada0 上启用安全：

```sh
camcontrol security ada0 -U user -s MyPass
```

使用用户密码 MyPass 安全擦除已启用安全的 ada0。

*警告！警告！警告！*

以下命令将 *擦除所有* 设备数据，使用前请备份你的数据！

这将使固态硬盘（SSD）恢复到出厂默认写入性能：

```sh
camcontrol security ada0 -U user -e MyPass
```

报告 ada0 的 HPA 支持和设置（也可通过 identify 报告）：

```sh
camcontrol hpa ada0
```

在 ada0 上启用 HPA，将最大报告扇区数设置为 10240。

*警告！警告！警告！*

以下命令将 *阻止访问* 设备上超出此限制的所有数据，直到通过将 HPA 设置为设备的原始最大扇区来禁用 HPA，这只能在上电或硬件重置后完成！

*不要* 在具有活动文件系统的设备上使用此命令：

```sh
camcontrol hpa ada0 -s 10240
```

这将读取向 da0 注册的任何持久预留密钥，并显示发送 PERSISTENT RESERVE IN SCSI 命令时遇到的任何错误：

```sh
camcontrol persist da0 -v -i read_keys
```

向 da0 注册持久预留密钥 0x12345678，将该注册应用于 da0 上的所有端口，并显示发送 PERSISTENT RESERVE OUT 命令时发生的任何错误：

```sh
camcontrol persist da0 -v -o register -a -K 0x12345678
```

为发出命令的发起方独占使用预留 da0。预留范围是整个 LUN。发送 PERSISTENT RESERVE OUT 命令时的任何错误都将显示：

```sh
camcontrol persist da0 -v -o reserve -s lun -k 0x12345678 -T ex_ac
```

显示 da0 上所有预留的完整状态，如果有任何错误则打印状态：

```sh
camcontrol persist da0 -v -i read_full
```

这将释放 da0 上 ex_ac（Exclusive Access）类型的预留。此注册的 Reservation Key 为 0x12345678。发生的任何错误都将显示：

```sh
camcontrol persist da0 -v -o release -k 0x12345678 -T ex_ac
```

向 da0 注册密钥 0x12345678，指定它适用于 SAS 地址为 0x1234567812345678 和 0x8765432187654321 的 SAS 发起方：

```sh
camcontrol persist da0 -v -o register -K 0x12345678 -S e
	-I sas,0x1234567812345678 -I sas,0x8765432187654321
```

将注册从当前发起方（其 Registration Key 为 0x87654321）移动到具有 Fibre Channel World Wide Node Name 0x1234567812345678 的 Fibre Channel 发起方。将为具有 Fibre Channel World Wide Node Name 0x1234567812345678 的发起方注册新的注册密钥 0x12345678，当前发起方将从目标取消注册。预留将移动到目标设备上的 relative target port 2。注册将在断电后持久存在：

```sh
camcontrol persist da0 -v -o register_move -k 0x87654321 e
	-K 0x12345678 -U -p -R 2 -I fcp,0x1234567812345678
```

从磁带驱动器 sa0 中磁带的分区 1 读取并解码属性值，并显示导致的任何 SCSI 错误：

```sh
camcontrol attrib sa0 -v -i attr_values -p 1
```

从磁盘 da0 请求 SMR 区域列表，打印区域参数摘要，并显示导致的任何 SCSI 或 ATA 错误：

```sh
camcontrol zone da0 -v -c rz -P summary
```

从磁盘 da0 请求应重置写指针的 SMR 区域列表，并显示导致的任何 SCSI 或 ATA 错误：

```sh
camcontrol zone da0 -v -c rz -o reset
```

向磁盘 da0 上从 LBA 0x2c80000 开始的区域发出 Reset Write Pointer 命令，并显示导致的任何 SCSI 或 ATA 错误：

```sh
camcontrol zone da0 -v -c rwp -l 0x2c80000
```

将驱动器 ada0 上 Idle_a 电源条件的定时器设置为 60.1 秒，启用该特定电源条件，并保存定时器值和电源条件的启用状态：

```sh
camcontrol epc ada0 -c timer -T 60.1 -p Idle_a -e -s
```

告诉驱动器 da4 转到 Standby_z 电源状态（驱动器的最低电源状态）并保持在该状态，直到通过另一个 `goto` 命令显式释放：

```sh
camcontrol epc da4 -c goto -p Standby_z -H
```

仅报告驱动器 da2 的电源状态。某些驱动器会响应 `status` 子命令发送的命令而上电，`-P` 选项使 `camcontrol` 仅发送 ATA CHECK POWER MODE 命令，这不应触发驱动器电源状态的更改：

```sh
camcontrol epc da2 -c status -P
```

显示驱动器 ada0 的 ATA Power Conditions 日志（Log Address 0x08）：

```sh
camcontrol epc ada0 -c list
```

使用 strptime(3) 格式字符串后跟使用此格式字符串创建的时间字符串来设置驱动器 sa0 的时间戳：

```sh
camcontrol timestamp sa0 -s -f "%a, %d %b %Y %T %z" e
	-T "Wed, 26 Oct 2016 21:43:57 -0600"
```

## 参见

cam(3), cam_cdbparse(3), cam(4), [pass(4)](../man4/pass.4.md), [xpt(4)](../man4/xpt.4.md), [diskinfo(8)](diskinfo.8.md), trim(8), zonectl(8)

## 历史

`camcontrol` 工具首次出现于 FreeBSD 3.0。

模式页编辑代码和任意 SCSI 命令代码基于旧 scsi(8) 工具和 scsi(3) 库中的代码，由 Julian Elischer 和 Peter Dufault 编写。scsi(8) 程序首次出现于 386BSD，并首次出现于 FreeBSD 2.0.5。

## 作者

Kenneth Merry <ken@FreeBSD.org>

## 缺陷

解析通用命令行参数的代码不知道某些子命令接受多个参数。因此，如果你尝试类似这样的操作：

```sh
camcontrol cmd -n da -u 1 -c "00 00 00 00 00 v" 0x00 -v
```

TEST UNIT READY 命令的 sense 信息不会被打印出来，因为 `camcontrol` 中的第一个 getopt(3) 调用在看到上面 `-c` 的第二个参数 (0x00) 时就会退出。修复此行为需要一些粗暴的代码，或对 getopt(3) 接口进行更改。解决此问题的最佳方法是始终确保在任何命令特定参数之前指定通用 `camcontrol` 参数。
