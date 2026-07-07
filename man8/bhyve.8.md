# bhyve(8)

`bhyve` — 在虚拟机中运行客户机操作系统

## 名称

`bhyve`

## 概要

`bhyve [-aCDeHhMPSuWwxY] [-c [cpus=]numcpus[,sockets=n][,cores=n][,threads=n]] [-f name,[string|file]=data] [-G [w][bind_address:]port] [-k config_file] [-K layout] [-l lpcdev[,conf]] [-m memsize[K|k|M|m|G|g|T|t]] [-o var=value] [-p vcpuN[-vcpuM]:hostcpuN[-hostcpuM]] [-r file] [-s slot,emulation[,conf]] [-U uuid] vmname`

`bhyve -l help`

`bhyve -s help`

## 描述

`bhyve` 是一个虚拟机监控器，用于在虚拟机中运行客户机操作系统。它可以在具有合适硬件支持的 amd64 和 arm64 平台上运行客户机。

虚拟 CPU 数量、客户机内存大小以及 I/O 连接等参数都可以通过命令行参数指定。

`bhyve` 通常与能够加载客户机操作系统的启动 ROM 配合使用。在 arm64 平台上，目前这是必需的。如果不使用启动 ROM，则在运行 `bhyve` 之前，必须使用 [bhyveload(8)](bhyveload.8.md) 或类似的引导加载器加载客户机操作系统。在 amd64 上，`edk2-bhyve` 包提供了可用于引导客户机的 UEFI 固件；在 arm64 上，`u-boot-bhyve-arm64` 包提供了可用于引导客户机的 U-Boot 镜像。

`bhyve` 会一直运行，直到客户机操作系统重启（未启用 `monitor` 模式时）、停机，或检测到未处理的虚拟机监控器退出。

通常 `bhyve` 必须由超级用户运行，但属于 `vmm` 组的用户也可以创建和运行虚拟机。参见 [vmm(4)](../man4/vmm.4.md)。由非特权用户运行时，`bhyve` 必须能够访问所需的所有资源，如磁盘镜像或网络设备。非特权用户无法使用 PCI 直通。

## 选项

- `pcislot`
- `pcislot` `:` `function`
- `bus` `:` `pcislot` `:` `function`

**`-a`** 将客户机的本地 APIC 配置为 xAPIC 模式。此选项仅适用于 amd64 平台。xAPIC 模式是默认设置，因此此选项是冗余的，将在未来版本中废弃。

**`-C`** 将客户机内存包含在核心文件中。

**`-c`** [[`cpus=` ]`numcpus` ][`,sockets=``n` ][`,cores=``n` ][`,threads=``n` ]] 客户机虚拟 CPU 数量和/或 CPU 拓扑。`numcpus`、`sockets`、`cores` 和 `threads` 的默认值均为 1。如果未指定 `numcpus`，则根据其他参数计算得出。拓扑必须一致，即 `numcpus` 必须等于 `sockets`、`cores` 和 `threads` 的乘积。如果某个设置被多次指定，以最后一次为准。虚拟 CPU 的最大数量默认为系统中活动物理 CPU 的数量，可通过 `hw.vmm.maxcpu` [sysctl(8)](sysctl.8.md) 变量获取。该限制可通过 `hw.vmm.maxcpu` loader 可调参数调整。

**`-D`** 客户机发起关机时销毁虚拟机。

**`-e`** 当客户机访问未被模拟的 I/O 端口时，强制 `bhyve` 退出。此选项用于调试目的，仅适用于 amd64 平台。

**`-f`** `name``,`[`string`|`file`]`=``data`] 向 fw_cfg 接口添加一个名为 `name` 的 fw_cfg 文件。如果指定了 `string`，则 fw_cfg 文件以该字符串作为数据。如果指定了 `file`，则 bhyve 读取该文件并将文件内容作为 fw_cfg 数据添加。

**`-G`** [`w` ][`bind_address` `:` ]] `port` 启动一个调试服务器，使用 GDB 协议将客户机状态导出给调试器。IPv4 TCP 套接字将绑定到指定的 `bind_address` 和 `port`，监听调试器连接。同一时间只能有一个调试器连接到调试服务器。如果选项以 `w` 开头，`bhyve` 将在第一条指令处暂停执行，等待调试器连接。

**`-H`** 当检测到 HLT 指令时让出虚拟 CPU 线程。如果未指定此选项，虚拟 CPU 将占用主机 CPU 的 100%。此选项仅适用于 amd64 平台。

**`-h`** 打印帮助信息并退出。

**`-k`** `config_file` 从简单的键值对配置文件中设置配置变量。配置文件的每一行应包含一个配置变量名、一个等号（“=”）和一个值。变量名、等号和值之间不允许有空格。空行和以 “#” 开头的行将被忽略。详见 bhyve_config(5)。

**`-K`** `layout` 指定键盘布局。可指定的值设置了 **/usr/share/bhyve/kbdlayout** 中的文件名。此设置仅在 UEFI 模式下加载 VNC 时生效。当使用支持 QEMU 扩展按键事件消息的 VNC 客户端（如 TigerVNC）时，不需要此选项。当使用不支持 QEMU 扩展按键事件消息的 VNC 客户端（如 TightVNC）时，除非另行指定，否则布局默认为美式键盘。

**`-l`** `help` 打印支持的 LPC 设备列表。

**`-l`** `lpcdev`[`,``conf`] 允许配置 LPC PCI-ISA 桥后面的设备。支持的设备仅有 TTY 类设备 `com1 , com2 , com3` 和 `com4`、TPM 模块 `tpm`、启动 ROM 设备 `bootrom`、`fwcfg` 类型以及调试/测试设备 `pc-testdev`。`conf` 参数的可能值在 `-s` 标志说明中列出。此选项仅适用于 amd64 平台。在 arm64 上，控制台和启动 ROM 设备使用更通用的 `-o` 选项配置。

**`-m`** `memsize`[] `K | k | M | m | G | g | T | t` ] 设置客户机物理内存大小。此大小必须与传递给 [bhyveload(8)](bhyveload.8.md) 的大小相同。size 参数可后跟 `K , M , G` 或 `T` 之一（大小写均可），分别表示千字节、兆字节、吉字节或太字节的倍数。如果未指定后缀，则假定为兆字节。默认值为 256M。

**`-M`** 以 `monitor` 模式运行虚拟机。在此模式下，客户机重启不会导致 bhyve 进程退出，bhyve 会重启虚拟机。一旦 bhyve 进程退出或被杀死，虚拟机将自动销毁。

**`-n`** `id``,``size``,``cpus`[`,``domain_policy`] 配置客户机 NUMA 域。此选项仅适用于 amd64 平台。`-n` 选项允许将客户机物理地址空间划分为多个域。每个域的布局编码在客户机操作系统可见的 ACPI 表中。`-n` 选项还允许为支撑给定 NUMA 域的主机内存指定 [domainset(9)](../man9/domainset.9.md) 内存分配策略。一个客户机最多可有 8 个 NUMA 域。此功能要求客户机使用启动 ROM，特别是不能用于通过 [bhyveload(8)](bhyveload.8.md) 初始化的客户机。每个域由数字 *id* 标识。域内存 *size* 使用与 `-m` 标志相同的格式指定。所有 *size* 参数的总和覆盖 `-m` 标志指定的虚拟机总内存大小。但如果至少有一个域内存 size 参数缺失，虚拟机总内存大小将平均分配到所有模拟域。*cpuset* 参数指定属于该域的 CPU 集合。*domain_policy* 参数可选，用于为模拟域配置 [domainset(9)](../man9/domainset.9.md) 主机 NUMA 内存分配策略。有效的 NUMA 内存分配策略及其格式列表参见 cpuset(1) 中的 `-n` 标志。

**`-o`** `var``=``value` 将配置变量 `var` 设置为 `value`。配置选项参见 bhyve_config(5)。

**`-P`** 当检测到 PAUSE 指令时，强制客户机虚拟 CPU 退出。此选项仅适用于 amd64 平台。

**`-p`** `vcpuN`[-`vcpuM` ]`:``hostcpuN`[-`hostcpuM`]] 将客户机从 *vcpuN* 到 *vcpuM* 的虚拟 CPU 绑定到主机从 *hostcpuN* 到 *hostcpuM* 的 CPU 上。主机 CPU 和客户机虚拟 CPU 从 0 开始编号。*vcpuM* 和 *hostcpuM* 参数可省略。

**`-r`** `file` 从快照恢复客户机。客户机内存内容从 `file` 恢复，客户机设备及 vCPU 状态从 “`file`.kern” 文件恢复。注意，当前快照文件格式要求新虚拟机中的设备配置必须与创建快照的虚拟机匹配，即需指定相同的 `-s` 和 `-l` 选项。vCPU 数量和内存配置从快照中读取。

**`-S`** 锁定客户机内存。

**`-s`** `help` 打印支持的 PCI 设备列表。

**`-s`** `slot``,``emulation`[`,``conf`] 配置虚拟 PCI 插槽和功能。`bhyve` 提供 PCI 总线模拟以及可连接到总线插槽的虚拟设备。共有 32 个可用插槽，每个插槽最多可提供 8 个功能。`slot` 可按以下格式之一指定：`pcislot` 值为 0 到 31。可选的 `function` 值为 0 到 7。可选的 `bus` 值为 0 到 255。如果未指定，`function` 默认为 0。如果未指定，`bus` 默认为 0。`emulation` 参数的可用选项参见 “PCI 模拟” 章节。

**`-U`** `uuid` 在客户机的系统管理 BIOS 系统信息结构中设置通用唯一标识符（UUID）。默认情况下，UUID 由主机名和 `vmname` 生成。

**`-u`** RTC 使用 UTC 时间。

**`-W`** 强制 virtio PCI 设备模拟使用 MSI 中断而非 MSI-X 中断。

**`-w`** 忽略对未实现的特定模型寄存器（MSR）的访问。此选项用于调试目的。

**`-x`** 将客户机的本地 APIC 配置为 x2APIC 模式。此选项仅适用于 amd64 平台。

**`-Y`** 禁用 MPtable 生成。此选项仅适用于 amd64 平台。

**`vmname`** 客户机的字母数字名称。应与 [bhyveload(8)](bhyveload.8.md) 创建的名称相同。

## PCI 模拟

`bhyve` 为各种 PCI 设备提供模拟。它们由 `-s` `slot,emulation,conf` 配置中的 `emulation` 参数指定，可以是以下之一：

**`hostbridge`** 简单的主机桥。通常配置在插槽 0，大多数客户机操作系统都需要它。

**`amd_hostbridge`** 使用 AMD 的 PCI 厂商 ID，模拟与 `hostbridge` 相同。

**`passthru`** PCI 直通设备。

**`virtio-net`** Virtio 网络接口。

**`virtio-blk`** Virtio 块存储接口。

**`virtio-scsi`** Virtio SCSI 接口。

**`virtio-9p`** Virtio 9p（VirtFS）接口。

**`virtio-rnd`** Virtio 随机数生成器接口。

**`virtio-console`** Virtio 控制台接口，以简单字符设备的形式向客户机暴露多个端口，用于客户机和主机用户空间之间的简单 I/O。

**`virtio-input`** Virtio 输入接口。

**`ahci`** 连接任意设备的 AHCI 控制器。

**`ahci-cd`** 连接 ATAPI CD/DVD 的 AHCI 控制器。

**`ahci-hd`** 连接 SATA 硬盘的 AHCI 控制器。

**`e1000`** Intel e82545 网络接口。

**`uart`** PCI 16550 串口设备。

**`lpc`** 带有 COM1、COM2、COM3 和 COM4 16550 串口、启动 ROM 以及可选 TPM 模块、fw_cfg 类型和调试/测试设备的 LPC PCI-ISA 桥。LPC 桥模拟只能在总线 0 上配置。

**`fbuf`** 连接到 VNC 服务器的原始帧缓冲设备。

**`xhci`** 可扩展主机控制器接口（xHCI）USB 控制器。

**`nvme`** NVM Express（NVMe）控制器。

**`hda`** 高保真音频控制器。

可选参数 `conf` 描述设备模拟的后端。如果未指定 `conf`，则设备模拟没有后端，可视为未连接。

### 网络设备后端

- `tap` `N` [`,mac=` `xx:xx:xx:xx:xx:xx`] [`,mtu=` `N`]
- `vmnet` `N` [`,mac=` `xx:xx:xx:xx:xx:xx`] [`,mtu=` `N`]
- `ngd` `N`
- `netgraph,path=` `ADDRESS` `,peerhook=` `HOOK` [`,socket=` `NAME`] [`,hook=` `HOOK`] [`,mac=` `xx:xx:xx:xx:xx:xx`] [`,mtu=` `N`]
- `slirp` [`,open`] [`,hostfwd=` `proto`: `hostaddr`: `hostport -` `guestaddr`: `guestport`] [`,mac=` `xx:xx:xx:xx:xx:xx`] [`,mtu=` `N`]

如果未指定 `mac`，MAC 地址由固定的 OUI 派生，其余字节由插槽号、功能号和设备名的 MD5 哈希生成。如果指定，必须是单播 MAC 地址。

MAC 地址是 [ethers(5)](../man5/ethers.5.md) 格式的 ASCII 字符串。

`ngd` 设备可用于通过 [ng_device(4)](../man4/ng_device.4.md) 节点将客户机连接到 [netgraph(4)](../man4/netgraph.4.md)。这可用于在 [VNET(9)](../man9/vnet.9.md) jail 中运行 bhyve，并通过 devfs(8) 暴露 ng_device，使其能够访问无法直接到达的主机 netgraph。

对于 `virtio-net` 设备，可指定 `mtu` 参数以告知客户机允许的最大 MTU（以字节为单位）。

对于 `netgraph` 后端，必须指定 `path` 和 `peerhook` 参数以设置目标节点和对应的钩子。可选参数 `socket` 和 `hook` 可用于设置 [ng_socket(4)](../man4/ng_socket.4.md) 节点名和源钩子。`ADDRESS`、`HOOK` 和 `NAME` 必须符合 [netgraph(4)](../man4/netgraph.4.md) 寻址规则。

`slirp` 后端可用于为客户机提供 NAT 网络。此后端性能有限，但不需要在主机系统上进行任何网络配置，且可由非特权用户使用。它依赖于 `net/libslirp` Port。如果设置了 `open` 关键字，客户机将能够发起出站网络连接，`bhyve` 会透明处理必要的地址转换。`hostfwd` 选项接受一个 5 元组，描述如何将来自主机的连接转发到客户机。可指定多条规则，以分号分隔。注意，分号必须转义或加引号，以防止 shell 解释。后端将向客户机提供 DHCP 和 DNS 服务。

### 块存储设备后端

- `/filename` [`,` `block-device-options`]
- `/dev/xxx` [`,` `block-device-options`]

`block-device-options` 如下：

**`nocache`** 以 `O_DIRECT` 打开文件。

**`direct`** 以 `O_SYNC` 打开文件。

**`ro`** 强制以只读方式打开文件。

**`sectorsize=`** `logical`[`/``physical` ]] 指定模拟磁盘的逻辑和物理扇区大小。物理扇区大小是可选的，未显式指定时等于逻辑扇区大小。

**`nodelete`** 禁用通过 `DIOCGDELETE` 请求模拟客户机 trim 请求。

**`bootindex=`** `index` 将设备添加到 `index` 指定的启动顺序中。使用 fw_cfg 文件指定启动顺序。客户机固件可能忽略或不支持此 fw_cfg 文件。在这种情况下，此功能无法按预期工作。

### SCSI 设备后端

- [`target`=[ID : ]`path`]]] [`,` `scsi-device-options` ]] [`,` `backend-specific-options` ]]

可指定多个 `target` 参数，每个配置不同的 `path` 作为独立的 SCSI 目标。如果未为某个 `target` 显式配置 `target` `ID`，该 `target` 将被分配为此时已使用的最高 `target` `ID` 之后的下一个顺序 `ID`，如果是第一个配置的目标则为 0。所有 `target` `ID` 在每个实例中必须唯一。`path` 参数的含义特定于每个后端：

CAM 目标层（CTL）设备节点的路径。如果未配置任何目标，默认将配置一个由 **/dev/cam/ctl** 支撑的单一目标。

| **后端** | **路径** | **描述** |
| --- | --- | --- |
| ctl | **/dev/cam/ctl**[`pp`.`vp` ]] |  |

`scsi-device-options` 如下：

**`backend=`** `backend` 要使用的 virtio-scsi 后端。后端名称不区分大小写。目前仅有一个后端 “ctl”，这也是默认后端。

**`bootindex=`** `index` 将设备添加到 `index` 指定的启动顺序中。使用 fw_cfg 文件指定启动顺序。客户机固件可能忽略或不支持此 fw_cfg 文件。在这种情况下，此功能无法按预期工作。

**`ctl_ringsz=`** `ringsz` 控制队列使用的环形缓冲区大小。

**`evt_ringsz=`** `ringsz` 事件队列使用的环形缓冲区大小。

**`req_ringsz=`** `ringsz` 每个 I/O 请求队列使用的环形缓冲区大小。

**`num_queues=`** `num` 要使用的 I/O 请求队列数。

**`seg_max=`** `num` 单个命令中允许的最大段数。

**`thr_per_q=`** `num` 每个 I/O 请求队列的并行请求处理线程数。

**CTL** 后端的 `backend-specific-options` 如下：

**`iid=`** `IID` 向 **CTL** 发送请求时使用的发起方 ID。默认值为 0。

### 9P 设备后端

- `sharename` `=` `/path/to/share` [`,` `9p-device-options`]

`9p-device-options` 如下：

**`ro`** 以只读模式暴露共享。

### TTY 设备后端

**`stdio`** 将串口连接到 `bhyve` 进程的标准输入和输出。

**`/dev/xxx`** 使用主机 TTY 设备进行串口 I/O。

**`tcp=ip:port`** 使用 TCP 服务器进行串口 I/O。配置此选项将启动一个等待连接的 TCP 服务器。同一时间仅允许一个连接。当现有连接处于活动状态时，TCP 服务器将立即关闭新连接。请注意，此功能允许非特权用户访问客户机控制台，因此需确保适当地限制访问。

### TPM 设备后端

- `type`,`path`[`,``tpm-device-options`]

模拟 TPM 设备。`type` 支持的选项：

**`passthru`** 使用物理 TPM 设备。参数 `path` 需指向有效的 TPM 设备路径，即 **/dev/tpm0**。

**`swtpm`** 连接到正在运行的 `swtpm` 实例。参数 `path` 需指向 `swtpm` 进程正在监听的 UNIX 域套接字。

`tpm-device-options` 如下：

**`version=`** `version` 根据 TCG 规范的 TPM 设备版本。默认为 `2.0`，这也是目前唯一支持的版本。

### 启动 ROM 设备后端

- `romfile`[`,``varfile`]

将 `romfile` 映射到为客户机启动固件保留的地址空间。

如果提供了 `varfile`，该文件也将映射到启动固件客户机地址空间，客户机所做的任何修改都将保存到该文件。

fw_cfg 类型：

**`fwcfg`** fw_cfg 接口用于向客户机固件传递 CPU 数量或 ACPI 表等信息。支持的值为 `bhyve` 和 `qemu`。出于向后兼容性考虑，`bhyve` 是默认选项。使用 `bhyve` 时，使用 bhyve 的 fwctl 接口。它目前仅向客户机固件报告 CPU 数量。`qemu` 选项使用 QEMU 的 fw_cfg 接口。此接口被广泛使用，允许向客户机传递用户定义的信息。它用于向客户机传递 CPU 数量、ACPI 表、启动顺序等许多内容。某些操作系统（如 Fedora CoreOS）也可通过 QEMU 的 fw_cfg 接口进行配置。

### 直通设备后端

- `ppt` `N` [, `passthru-device-options` ]]
- `bus` `/` `slot` `/` `function` [, `passthru-device-options`]
- `pci` `bus` : `slot` :`function` [, `passthru-device-options`]

连接到主机上名为 ppt `N` 或由 `slot`、`bus` 和 `function` 编号描述的选择器处的 PCI 设备。

`passthru-device-options` 如下：

**`rom=`** `romfile` 将 `romfile` 作为选项 ROM 添加到 PCI 设备。ROM 将由固件加载，应能初始化设备。

**`bootindex=`** `index` 将设备添加到 `index` 指定的启动顺序中。使用 fw_cfg 文件指定启动顺序。客户机固件可能忽略或不支持此 fw_cfg 文件。在这种情况下，此功能无法按预期工作。

配置直通设备时，必须使用 `-S` 选项锁定客户机内存。

主机设备必须如 [vmm(4)](../man4/vmm.4.md) 中所述，在启动时使用 `pptdevs` loader 变量进行预留。

### Virtio 控制台设备后端

- `port1=``/path/to/port1.sock`[`,port``N` `=``/path/to/port2.sock` `...`]

每个设备最多可创建 16 个端口。每个端口都有名称，对应由 `bhyve` 创建的 Unix 域套接字。`bhyve` 同一时间每个端口最多接受一个连接。

限制：

- 由于 `bhyve` 缺少析构函数，`bhyve` 退出后文件系统上的套接字必须手动清理。
- 目前无法使用 “console port” 功能，也不支持控制台端口调整大小。
- 紧急写入已宣告，但目前为空操作。

### Virtio 输入设备后端

- `/dev/input/eventX`

通过 VirtIO 输入接口将 **/dev/input/eventX** 的输入事件发送给客户机。

### 帧缓冲设备后端

- [`rfb=` `address`] [`,w=` `width`] [`,h=` `height`] [`,vga=` `vgaconf`] [`,wait`] [`,password=` `password`]

配置选项定义如下：

- [`IPv4` `:`] `port`
- `[` `IPv6%zone` `]` `:` `port`
- `unix:` `my/unix.sock`

**`rfb=`** `address`（或 `tcp=``address`）VNC 应监听的 UNIX 域套接字或 IP 地址和端口。有三种可能的格式：默认为监听 localhost IPv4 地址和默认 VNC 端口 5900。IPv6 地址必须用方括号括起，可包含可选的区域标识符。

**`w=`** `width` 和 `h=``height` 分别为显示分辨率宽度和高度。如果未指定，将使用默认分辨率 1024x768 像素。支持的最小分辨率为 640x480 像素，最大为 3840x2160 像素。

**`vga=`** `vgaconf` 此选项的可能值为 `io`（默认）、`on` 和 `off`。PCI 显卡具有双重特性：它们既是带 BAR 寻址的标准 PCI 设备，也可能隐式解码传统 VGA I/O 空间（Ad 0x3c0-3df）和内存空间（64 KiB，Ad 0xA0000）。对于会发起导致 I/O 端口查询的 BIOS 调用，且禁用 I/O 解码时无法启动的客户机，应使用默认的 `io` 选项。`on` 选项应与 UEFI 中的 CSM BIOS 功能配合使用，以引导需要传统 VGA I/O 和内存区域可用的传统 BIOS 客户机。对于假设如果检测到 I/O 端口就存在 VGA 适配器的 UEFI 客户机，应使用 `off` 选项。此类客户机的一个例子是 UEFI 模式下的 OpenBSD。有关特定客户机的配置说明，请参阅 `bhyve` FreeBSD wiki 页面（https://wiki.freebsd.org/bhyve）。

**`wait`** 指示 `bhyve` 仅在 VNC 连接建立后才启动，简化需要立即键盘输入的操作系统安装过程。安装后可移除此选项。

**`password=`** `password` 此类认证已知在加密方面较弱，不适用于不受信任的网络。许多实现会希望使用更强的安全措施，例如通过 IPsec 或 SSH 提供的加密通道运行会话。

### xHCI USB 设备后端

- `tablet`

一种 USB 平板设备，在使用 VNC 时提供精确的光标同步。

### NVMe 设备后端

- `devpath` [`,maxq=` `#`] [`,qsz=` `#`] [`,ioslots=` `#`] [`,sectsz=` `#`] [`,ser=` `#`] [`,eui64=` `#`] [`,dsm=` `opt`]

配置选项定义如下：

**`devpath`** 接受的设备路径为：`/dev/blockdev` 或 `/path/to/image` 或 `ram=``size_in_MiB`。

**`maxq`** 最大队列数。

**`qsz`** 每个队列的最大元素数。

**`ioslots`** 最大并发 I/O 请求数。

**`sectsz`** 扇区大小（默认为 blockif 扇区大小）。

**`ser`** 序列号，最多 20 个字符。

**`eui64`** IEEE 扩展唯一标识符（8 字节值）。

**`dsm`** 数据集管理支持。支持的值为：`auto , enable` 和 `disable`。

### AHCI 设备后端

- [[`hd: | cd:` ]`path`]] [`,nmrr=` `nmrr`] [`,ser=` `#`] [`,rev=` `#`] [`,model=` `#`]

配置选项定义如下：

**`nmrr`** 标称介质旋转速率，即 RPM。值为 1 表示该设备是固态硬盘，即非旋转设备。默认值为 0。

**`ser`** 序列号，最多 20 个字符。

**`rev`** 修订号，最多 8 个字符。

**`model`** 型号，最多 40 个字符。

### HD Audio 设备后端

- [`play=` `playback`] [`,rec=` `recording`]

配置选项定义如下：

**`play`** 播放设备，通常为 **/dev/dsp0**。

**`rec`** 录音设备，通常为 **/dev/dsp0**。

## 配置变量

`bhyve` 使用内部的配置变量树来描述全局和每设备的设置。`bhyve` 启动时，按命令行给出的顺序解析命令行选项（包括配置文件）。每个命令行选项设置一个或多个配置变量。例如，`-s` 选项为 PCI 设备创建新的树节点，并在该节点下设置一个或多个变量，包括设备模型和设备模型特定的变量。在此解析阶段，变量可被多次设置，最终值覆盖之前的值。

所有命令行选项处理完毕后，配置值将被冻结。`bhyve` 随后使用配置值初始化设备模型和全局设置。

有关配置变量的更多细节，参见 bhyve_config(5)。

## 配置文件创建

`-k` 标志允许提供一个配置文件路径，其中包含所有设置，否则需要向 `bhyve` 提供一长串程序参数。

有一种非常简单的方法，可将复杂的程序参数集合转换为 bhyve_config(5) 格式的等效配置文件。

使用 `-o` `config.dump=1` 让 `bhyve` 将表示已用标志和参数的配置文件输出到 stdout。可将输出重定向到文件以保存生成的设置。

使用该配置文件启动 `bhyve` 之前，请务必从生成的配置文件中删除 `config.dump` 行。

## 调试服务器

当前调试服务器对调试器的支持有限。

### 寄存器

每个虚拟 CPU 作为线程暴露给调试器。

可查询每个虚拟 CPU 的通用寄存器，但浮点和系统寄存器等其他寄存器无法查询。

### 内存

调试器可读取和写入内存（包括内存映射 I/O 区域）。内存操作使用虚拟地址，通过当前虚拟 CPU 的活动地址转换解析为物理地址。

### 控制

调试器可随时中断运行中的客户机（例如在调试器中按 Ctrl-C）。

单步执行仅在支持 MTRAP VM 退出的 Intel CPU 上支持。

断点在支持单步执行的 Intel CPU 上支持。注意，在客户机启用中断的情况下从断点继续执行，可能无法按预期工作，因为在断点单步执行期间定时器中断会触发。

## 信号处理

`bhyve` 处理以下信号：

**SIGTERM** 为虚拟机触发 ACPI 关机

## 退出状态

退出状态指示虚拟机的终止方式：

**0** 重启
**1** 关机
**2** 停机
**3** 三重错误（仅 amd64）
**4** 因错误退出
**5** 挂起

## 实例

如果不使用启动 ROM，则在运行 [bhyve(4)](../man4/bhyve.4.md) 之前，必须使用 [bhyveload(8)](bhyveload.8.md) 或类似的引导加载器加载客户机操作系统。否则不需要引导加载器。

运行一台具有 1 GiB 内存、两个虚拟 CPU、由 **/my/image** 文件系统镜像支撑的 virtio 块设备，以及用于控制台的串口的虚拟机：

```sh
bhyve -c 2 -s 0,hostbridge -s 1,lpc -s 2,virtio-blk,/my/image \
  -l com1,stdio -H -P -m 1G vm1
```

在 arm64 上执行相同操作：

```sh
bhyve -c 2 -s 0,hostbridge -s 1,virtio-blk,/my/image -o console=stdio \
  -o bootrom=/usr/local/share/u-boot/u-boot-bhyve-arm64/u-boot.bin -m 1G vm1
```

运行一台 24 GiB 单 CPU 虚拟机，具有三个网络端口，其中一个指定了 MAC 地址：

```sh
bhyve -s 0,hostbridge -s 1,lpc -s 2:0,virtio-net,tap0 \
  -s 2:1,virtio-net,tap1 \
  -s 2:2,virtio-net,tap2,mac=00:be:fa:76:45:00 \
  -s 3,virtio-blk,/my/image -l com1,stdio \
  -H -P -m 24G bigvm
```

运行一台 8 GiB 四 CPU 虚拟机，具有 8 个 AHCI SATA 硬盘、一个 AHCI ATAPI CD-ROM、一个 virtio 网络端口、一个 AMD 主机桥，控制台端口连接到 [nmdm(4)](../man4/nmdm.4.md) null-modem 设备。

```sh
bhyve -c 4 \
  -s 0,amd_hostbridge -s 1,lpc \
  -s 1:0,ahci,hd:/images/disk.1,hd:/images/disk.2,\
hd:/images/disk.3,hd:/images/disk.4,\
hd:/images/disk.5,hd:/images/disk.6,\
hd:/images/disk.7,hd:/images/disk.8,\
cd:/images/install.iso \
  -s 3,virtio-net,tap0 \
  -l com1,/dev/nmdm0A \
  -H -P -m 8G
```

运行一台 UEFI 虚拟机，显示分辨率为 800x600 像素，可通过 VNC 在 0.0.0.0:5900 访问，或通过 TCP 上的串口控制台在 127.0.0.1:1234 访问（在无保护情况下暴露串口控制台是不安全的）。

```sh
bhyve -c 2 -m 4G -w -H \
  -s 0,hostbridge \
  -s 3,ahci-cd,/path/to/uefi-OS-install.iso \
  -s 4,ahci-hd,disk.img \
  -s 5,virtio-net,tap0 \
  -s 29,fbuf,tcp=0.0.0.0:5900,w=800,h=600,wait \
  -s 30,xhci,tablet \
  -s 31,lpc -l com1,tcp=127.0.0.1:1234 \
  -l bootrom,/usr/local/share/uefi-firmware/BHYVE_UEFI.fd \
   uefivm
```

运行一台 UEFI 虚拟机，VNC 显示绑定到所有 IPv6 地址的 5900 端口，串口 I/O 端口绑定到回环地址的 TCP 1234 端口（在无保护情况下暴露串口控制台是不安全的）。

```sh
bhyve -c 2 -m 4G -w -H \
  -s 0,hostbridge \
  -s 4,ahci-hd,disk.img \
  -s 5,virtio-net,tap0 \
  -s 29,fbuf,tcp=[::]:5900,w=800,h=600 \
  -s 30,xhci,tablet \
  -s 31,lpc -l com1,tcp=[::1]:1234 \
  -l bootrom,/usr/local/share/uefi-firmware/BHYVE_UEFI.fd \
   uefivm
```

运行一台带 VARS 文件的 UEFI 虚拟机以保存 EFI 变量。注意，`bhyve` 会将客户机的修改写入给定的 VARS 文件。务必从 **/usr** 中的模板 VARS 文件为每个客户机创建一个副本。

```sh
bhyve -c 2 -m 4g -w -H \
  -s 0,hostbridge \
  -s 31,lpc -l com1,stdio \
  -l bootrom,/usr/local/share/uefi-firmware/BHYVE_UEFI_CODE.fd,BHYVE_UEFI_VARS.fd
   uefivm
```

为虚拟机创建配置文件 `configfile`，使用 `-o` `config.dump=1`：

```sh
/usr/sbin/bhyve -c 2 -m 256 -H -P \
  -s 0:0,hostbridge -s 1:0,virtio-net,tap0 \
  -s 2:0,ahci-hd,./vm0.img \
  -s 31,lpc -l com1,stdio \
  -o config.dump=1 vm0 > configfile
```

然后使用你喜欢的编辑器从新生成的 `configfile` 中删除 “config.dump=1” 行。

要使用此配置文件启动 `bhyve`，使用 `-k` 标志：

```sh
/usr/sbin/bhyve -k configfile vm0
```

运行一台具有四个 CPU 和两个模拟 NUMA 域的 UEFI 虚拟机：

```sh
bhyve -c 4 -w -H \
  -s 0,hostbridge \
  -s 4,ahci-hd,disk.img \
  -s 31,lpc -l com1,stdio \
  -l bootrom,/usr/local/share/uefi-firmware/BHYVE_UEFI.fd \
  -n id=0,size=4G,cpus=0-1 \
  -n id=1,size=4G,cpus=2-3 \
   numavm
```

假设主机具有两个 NUMA 域，使用 `prefer` [domainset(9)](../man9/domainset.9.md) 策略运行一台具有四个 CPU 的 UEFI 虚拟机，仅从第一个主机 NUMA 域分配客户机内存。

```sh
bhyve -c 2 -w -H \
  -s 0,hostbridge \
  -s 4,ahci-hd,disk.img \
  -s 31,lpc -l com1,stdio \
  -l bootrom,/usr/local/share/uefi-firmware/BHYVE_UEFI.fd \
  -n id=0,size=4G,cpus=0-1,domain_policy=prefer:0 \
   numavm
```

运行一台将单个 vCPU 绑定到主机 CPU 12 的虚拟机：

```sh
bhyve -c 1 -s 0,hostbridge -s 1,lpc -s 2,virtio-blk,/my/image \
  -l com1,stdio -H -P -m 1G -p 0:12 vm1
```

运行一台将 4 个 vCPU 绑定到主机 CPU 12-15 的虚拟机：

```sh
bhyve -c 4 -s 0,hostbridge -s 1,lpc -s 2,virtio-blk,/my/image \
  -l com1,stdio -H -P -m 1G -p 0-3:12-15 vm1
```

## 参见

[bhyve(4)](../man4/bhyve.4.md), [netgraph(4)](../man4/netgraph.4.md), [ng_socket(4)](../man4/ng_socket.4.md), [nmdm(4)](../man4/nmdm.4.md), [vmm(4)](../man4/vmm.4.md), bhyve_config(5), [ethers(5)](../man5/ethers.5.md), [bhyvectl(8)](bhyvectl.8.md), [bhyveload(8)](bhyveload.8.md), [domainset(9)](../man9/domainset.9.md)

> Intel, *64 and IA-32 Architectures Software Developer’s Manual*, Volume 3.

## 历史

`bhyve` 首次出现在 FreeBSD 10.0 中。

## 作者

Neel Natu <neel@freebsd.org> Peter Grehan <grehan@freebsd.org>
