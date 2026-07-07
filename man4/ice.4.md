# ice(4)

`ice` — Intel Ethernet 800 系列 1GbE 至 200GbE 驱动

## 名称

`ice`

## 概要

`device iflib device ice`

`在 loader.conf(5) 中： if_ice_load hw.ice.enable_health_events hw.ice.irdma hw.ice.irdma_max_msix hw.ice.debug.enable_tx_fc_filter hw.ice.debug.enable_tx_lldp_filter hw.ice.debug.ice_tx_balance_en`

`在 sysctl.conf(5) 或 loader.conf(5) 中： dev.ice.#.current_speed dev.ice.#.fw_version dev.ice.#.ddp_version dev.ice.#.pba_number dev.ice.#.hw.mac.*`

## 描述

`ice` 驱动为 Intel Ethernet 800 系列中的任何 PCI Express 适配器或 LOM（LAN On Motherboard）提供支持。

本手册涵盖以下主题：

- Sx Features
- Sx Dynamic Device Personalization
- Sx Jumbo Frames
- Sx Remote Direct Memory Access
- Sx RDMA Monitoring
- Sx Data Center Bridging
- Sx L3 QoS Mode
- Sx Firmware Link Layer Discovery Protocol Agent
- Sx Link-Level Flow Control
- Sx Forward Error Correction
- Sx Speed and Duplex Configuration
- Sx Disabling physical link when the interface is brought down
- Sx Firmware Logging
- Sx Debug Dump
- Sx Debugging PHY Statistics
- Sx Transmit Balancing
- Sx Thermal Monitoring
- Sx Network Memory Buffer Allocation
- Sx Additional Utilities
- Sx Optics and auto-negotiation
- Sx PCI-Express Slot Bandwidth
- Sx HARDWARE
- Sx LOADER TUNABLES
- Sx SYSCTL VARIABLES
- Sx INTERRUPT STORMS
- Sx IOVCTL OPTIONS
- Sx SUPPORT
- Sx SEE ALSO
- Sx HISTORY

### 特性

通过接口 MTU 设置提供 Jumbo 帧支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 可将适配器配置为接收和发送 Jumbo 帧。Jumbo 帧的最大 MTU 大小为 9706。更多信息请参见 Sx Jumbo Frames 部分。

此驱动版本支持 VLAN。有关启用 VLAN 的信息，请参见 [vlan(4)](vlan.4.md)。有关配置 VLAN 的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md) 的"VLAN Parameters"部分。

卸载也通过接口控制，例如，可以设置和取消设置 IPv4 和 IPv6 的校验和，TSO4 和/或 TSO6，最后是 LRO。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

此驱动对应的虚拟功能（VF）驱动为 [iavf(4)](iavf.4.md)。

此驱动对应的 RDMA 驱动为 [irdma(4)](irdma.4.md)。

### 动态设备个性化

DDP 包在设备初始化期间加载。驱动查找 **ice_ddp** 模块并检查其是否包含有效的 DDP 包文件。

如果驱动无法加载 DDP 包，设备将进入安全模式。安全模式禁用高级和性能功能，仅支持基本流量和最少功能，如更新 NVM 或下载新驱动或 DDP 包。安全模式仅适用于受影响的物理功能，不影响任何其他 PF。有关 DDP 和安全模式的更多详细信息，请参见"Intel Ethernet Adapters and Devices User Guide"。

如果遇到 DDP 包文件问题，可能需要下载更新的驱动或 **ice_ddp** 模块。更多信息请参见日志消息。

如果任何 PF 驱动已加载，则无法更新 DDP 包。要覆盖包，请卸载所有 PF，然后使用新包重新加载驱动。

每个驱动只能使用一个 DDP 包，即使多个已安装的设备使用该驱动。

每个设备只有第一个加载的 PF 可以为该设备下载包。

### Jumbo 帧

Jumbo 帧支持通过将最大传输单元（MTU）更改为大于默认值 1500 的值来启用。

使用 [ifconfig(8)](../man8/ifconfig.8.md) 增加 MTU 大小。

Jumbo 帧的最大 MTU 设置为 9706。这对应于 9728 字节的最大 jumbo 帧大小。

此驱动将尝试使用多个页大小缓冲区来接收每个 jumbo 数据包。这有助于避免分配接收数据包时的缓冲区不足问题。

使用 jumbo 帧时，丢包可能对吞吐量产生更大影响。如果在启用 jumbo 帧后观察到性能下降，启用流控制可能会缓解此问题。

### 远程直接内存访问

远程直接内存访问（RDMA）允许网络设备直接将数据传输到和从另一个系统上的应用程序内存，在某些网络环境中提高吞吐量并降低延迟。

ice 驱动同时支持 iWARP（Internet Wide Area RDMA Protocol）和 RoCEv2（RDMA over Converged Ethernet）协议。主要区别在于 iWARP 通过 TCP 执行 RDMA，而 RoCEv2 使用 UDP。

基于 Intel Ethernet 800 系列的设备在多端口模式下超过 4 个端口时不支持 RDMA。

有关 RDMA 的详细安装和配置信息，请参见 [irdma(4)](irdma.4.md)。

### RDMA 监控

出于调试/测试目的，可使用 sysctl 在端口上设置镜像接口。该接口可以接收镜像的 RDMA 流量，供 [tcpdump(1)](../man1/tcpdump.1.md) 等数据包分析工具使用。此镜像可能会影响性能。

要使用 RDMA 监控，可能需要保留更多 MSI-X 中断。在 `ice` 驱动加载之前，配置以下由 [iflib(4)](iflib.4.md) 提供的可调参数：

```sh
dev.ice.<interface #>.iflib.use_extra_msix_vectors=4
```

可能需要调整额外的 MSI-X 中断向量数量。

要创建/删除接口：

```sh
sysctl dev.ice.<interface #>.create_interface=1
sysctl dev.ice.<interface #>.delete_interface=1
```

镜像接口同时接收 LAN 和 RDMA 流量。可在 tcpdump 中配置附加过滤器。

为区分镜像接口和主接口，网络接口命名约定为：

```sh
<驱动名><端口号><修饰符><修饰符编号>
```

例如，"`ice0m0`"是"`ice0`"上的第一个镜像接口。

### 数据中心桥接

数据中心桥接（DCB）是硬件中的配置服务质量实现。它使用 VLAN 优先级标签（802.1p）来过滤流量。这意味着有 8 个不同的优先级可用于过滤流量。它还启用了优先级流控制（802.1Qbb），可以限制或消除网络压力期间丢弃的数据包数量。带宽可分配给每个优先级，在硬件级别强制执行（802.1Qaz）。

DCB 通常使用 DCBX 协议（802.1Qaz，LLDP 802.1AB 的特化）在网络中配置。`ice` 驱动支持以下互斥的 DCBX 支持变体：

- 基于固件的 LLDP 代理
- 基于软件的 LLDP 代理

在基于固件的模式下，固件拦截所有 LLDP 流量并为用户透明地处理 DCBX 协商。在此模式下，适配器以"willing"DCBX 模式运行，从链路伙伴（通常是交换机）接收 DCB 设置。本地用户只能查询协商的 DCB 配置。有关在交换机上配置 DCBX 参数的信息，请咨询交换机制造商的文档。

在基于软件的模式下，LLDP 流量被转发到网络栈和用户空间，由软件代理处理。在此模式下，适配器可以以"nonwilling"DCBX 模式运行，DCB 配置可在本地查询和设置。此模式要求禁用基于固件的 LLDP 代理。

基于固件的模式和基于软件的模式由"fw_lldp_agent"sysctl 控制。更多信息请参见固件链路层发现协议代理部分。

链路级流控制和优先级流控制互斥。ice 驱动在任何流量类（TC）上启用优先级流控制时将禁用链路流控制。启用链路流控制时将禁用优先级流控制。

要在基于软件的 DCBX 模式下启用/禁用优先级流控制：

```sh
sysctl dev.ice.<interface #>.pfc=1 (或 0 禁用)
```

增强传输选择（ETS）允许将带宽分配给某些 TC，以帮助确保流量可靠性。要查看分配的 ETS 配置，使用以下命令：

```sh
sysctl dev.ice.<interface #>.ets_min_rate
```

要设置每个 TC 的最小 ETS 带宽，用逗号分隔值。所有值总和必须为 100。例如，要将所有 TC 的最小带宽设置为 10%，TC 7 设置为 30%，使用以下命令：

```sh
sysctl dev.ice.<interface #>.ets_min_rate=10,10,10,10,10,10,10,30
```

要设置端口的用户优先级（UP）到 TC 映射，用逗号分隔值。例如，要将 UP 0 和 1 映射到 TC 0，UP 2 和 3 映射到 TC 1，UP 4 和 5 映射到 TC 2，UP 6 和 7 映射到 TC 3，使用以下命令：

```sh
sysctl dev.ice.<interface #>.up2tc_map=0,0,1,1,2,2,3,3
```

### L3 QoS 模式

`ice` 驱动支持在 PF 驱动中设置基于 DSCP 的第 3 层服务质量（L3 QoS）。驱动默认以 L2 QoS 模式初始化；L3 QoS 默认禁用。使用以下 sysctl 启用或禁用 L3 QoS：

```sh
sysctl dev.ice.<interface #>.pfc_mode=1 (或 0 禁用)
```

如果禁用 L3 QoS 模式，将返回 L2 QoS 模式。

要将 DSCP 值映射到流量类，用逗号分隔值。例如，将 DSCP 0-3 和 DSCP 8 分别映射到 DCB TC 0-3 和 4：

```sh
sysctl dev.ice.<interface #>.dscp2tc_map.0-7=0,1,2,3,0,0,0,0
sysctl dev.ice.<interface #>.dscp2tc_map.8-15=4,0,0,0,0,0,0,0
```

要将 DSCP 映射更改回默认流量类，将所有值设回 0。

要查看当前配置的映射，使用以下命令：

```sh
sysctl dev.ice.<interface #>.dscp2tc_map
```

启用 FW-LLDP 时 L3 QoS 模式不可用。

如果 L3 QoS 模式处于活动状态，则无法启用 FW-LLDP。

切换到 L3 QoS 模式前请禁用 FW-LLDP。

有关禁用 FW-LLDP 的更多信息，请参见本 README 中的 Sx Firmware Link Layer Discovery Protocol Agent 部分。

### 固件链路层发现协议代理

使用 sysctl 更改 FW-LLDP 设置。FW-LLDP 设置按端口配置，在重启后保持不变。

要启用 FW-LLDP 代理：

```sh
sysctl dev.ice.<interface #>.fw_lldp_agent=1
```

要禁用 FW-LLDP 代理：

```sh
sysctl dev.ice.<interface #>.fw_lldp_agent=0
```

要检查当前 LLDP 设置：

```sh
sysctl dev.ice.<interface #>.fw_lldp_agent
```

UEFI HII LLDP Agent 属性必须启用才能使此设置生效。如果"LLDP AGENT"属性设置为禁用，则无法从驱动启用 FW-LLDP 代理。

### 链路级流控制

以太网流控制（IEEE 802.3x 或 LFC）可通过 [sysctl(8)](../man8/sysctl.8.md) 配置，为 `ice` 启用接收和发送暂停帧。启用发送时，当接收数据包缓冲区超过预定义阈值时会生成暂停帧。启用接收时，收到暂停帧时发送单元将暂停固件中指定的时间延迟。

流控制默认禁用。

使用 sysctl 在不重新加载驱动的情况下更改单个接口的流控制设置：

```sh
sysctl dev.ice.<interface #>.fc
```

可用的流控制值：

```sh
0 = 禁用流控制
1 = 启用 Rx 暂停
2 = 启用 Tx 暂停
3 = 启用 Rx 和 Tx 暂停
```

通过检查 [ifconfig(8)](../man8/ifconfig.8.md) 中的接口条目并在"media"状态中查找标志"txpause"和/或"rxpause"来验证链路上是否协商了链路流控制。

`ice` 驱动要求端口和链路伙伴双方都启用流控制。如果一方禁用了流控制，端口在流量大时可能会出现挂起。

有关优先级流控制的更多信息，请参见 Sx Data Center Bridging 部分。

VF 驱动无法访问流控制。必须从主机端管理。

### 前向纠错

前向纠错（FEC）可提高链路稳定性但会增加延迟。许多高质量光模块、直连电缆和背板通道无需 FEC 即可提供稳定链路。

要使设备从此功能中受益，链路伙伴必须启用 FEC。

如果启用了 `allow_no_fec_modules_in_auto` sysctl，自动 FEC 协商将在链路伙伴未启用 FEC 或不支持 FEC 的情况下包含"FEC"：

```sh
sysctl dev.ice.<interface #>.allow_no_fec_modules_in_auto=1
```

注意：此标志目前在 Intel Ethernet 830 系列上不受支持。

要显示链路上协商的当前 FEC 设置：

```sh
sysctl dev.ice.<interface #>.negotiated_fec
```

要查看或设置链路上请求的 FEC 设置：

```sh
sysctl dev.ice.<interface #>.requested_fec
```

要查看链路的有效 FEC 模式：

```sh
sysctl -d dev.ice.<interface #>.requested_fec
```

### 速度与双工配置

速度和双工设置无法硬设置。

要让设备更改其在自动协商中将使用的速度或强制链路：

```sh
sysctl dev.ice.<interface #>.advertise_speed=<mask>
```

支持的速度因设备而异。根据设备支持的速度，速度掩码中使用的有效位可能包括：

```sh
0x0 - 自动
0x2 - 100 Mbps
0x4 - 1 Gbps
0x8 - 2.5 Gbps
0x10 - 5 Gbps
0x20 - 10 Gbps
0x80 - 25 Gbps
0x100 - 40 Gbps
0x200 - 50 Gbps
0x400 - 100 Gbps
0x800 - 200 Gbps
```

### 接口关闭时禁用物理链路

当 `link_active_on_if_down` sysctl 设置为"0"时，接口关闭时端口链路将断开。默认情况下，链路保持连接。

要在接口关闭时禁用链路：

```sh
sysctl dev.ice.<interface #>.link_active_on_if_down=0
```

### 固件日志

`ice` 驱动允许为支持的事件类别生成固件日志，以帮助客户支持调试问题。有关此功能的概述和附加提示，请参见"Intel Ethernet Adapters and Devices User Guide"。

从高层来看，要捕获固件日志：

- 设置固件日志配置。
- 执行必要的步骤以重现问题。
- 捕获固件日志。
- 停止捕获固件日志。
- 根据需要重置固件日志设置。
- 与客户支持合作调试问题。

注意：固件日志以二进制格式生成，必须由客户支持解码。收集的信息仅与用于调试的固件和硬件相关。

驱动加载后，将在驱动 sysctl 列表的 debug 部分下创建 `fw_log` sysctl 节点。驱动将这些事件分组为称为"模块"的类别。支持的模块包括：

**`general`** 常规（位 0）
**`ctrl`** 控制（位 1）
**`link`** 链路管理（位 2）
**`link_topo`** 链路拓扑检测（位 3）
**`dnl`** 链路控制技术（位 4）
**`i2c`** I2C（位 5）
**`sdp`** SDP（位 6）
**`mdio`** MDIO（位 7）
**`adminq`** 管理队列（位 8）
**`hdma`** 主机 DMA（位 9）
**`lldp`** LLDP（位 10）
**`dcbx`** DCBx（位 11）
**`dcb`** DCB（位 12）
**`xlr`** XLR（功能级重置；位 13）
**`nvm`** NVM（位 14）
**`auth`** 认证（位 15）
**`vpd`** 重要产品数据（位 16）
**`iosf`** Intel 片上系统结构（位 17）
**`parser`** 解析器（位 18）
**`sw`** 交换（位 19）
**`scheduler`** 调度器（位 20）
**`txq`** TX 队列管理（位 21）
**`acl`** ACL（访问控制列表；位 22）
**`post`** Post（位 23）
**`watchdog`** 看门狗（位 24）
**`task_dispatch`** 任务分发器（位 25）
**`mng`** 可管理性（位 26）
**`synce`** SyncE（位 27）
**`health`** 健康（位 28）
**`tsdrv`** 时间同步（位 29）
**`pfreg`** PF 注册（位 30）
**`mdlver`** 模块版本（位 31）

可以修改固件日志的详细级别。每个模块只能设置一个日志级别，每个级别包含低于它的详细级别。例如，将级别设置为"normal"也将记录警告和错误消息。可用的详细级别：

- 0 = 无
- 1 = 错误
- 2 = 警告
- 3 = 常规
- 4 = 详细

要为模块设置所需的详细级别，使用以下 sysctl 命令然后注册：

```sh
sysctl dev.ice.<interface #>.debug.fw_log.severity.<module>=<level>
```

例如：

```sh
sysctl dev.ice.0.debug.fw_log.severity.link=1
sysctl dev.ice.0.debug.fw_log.severity.link_topo=2
sysctl dev.ice.0.debug.fw_log.register=1
```

要在引导后但驱动初始化之前记录固件消息，使用 [kenv(1)](../man1/kenv.1.md) 设置可调参数。`on_load` 设置告诉设备在驱动加载期间尽快注册变量。例如：

```sh
kenv dev.ice.0.debug.fw_log.severity.link=1
kenv dev.ice.0.debug.fw_log.severity.link_topo=2
kenv dev.ice.0.debug.fw_log.on_load=1
```

要查看固件日志并将其重定向到文件，使用以下命令：

```sh
dmesg > log_output
```

注意：记录大量模块或过高的详细级别会向 dmesg 添加多余消息，可能妨碍调试工作。

### 调试转储

Intel Ethernet 800 系列设备支持调试转储，允许从固件收集事件"集群"的运行时寄存器值，然后将结果写入单个转储文件，用于调试现场复杂问题。

此调试转储包含设备及其现有硬件配置的快照，如交换表、发送调度器表和其他信息。调试转储捕获指定集群的当前状态，是整个设备的无状态快照。

注意：与固件日志一样，调试转储的内容不是人类可读的。请与客户支持合作解码文件。

调试转储按设备而非按 PF 进行。

调试转储将所有信息写入单个文件。

要在 FreeBSD 中生成调试转储文件，请执行以下操作：

使用位掩码和以下命令指定要包含在转储文件中的集群：

```sh
sysctl dev.ice.<interface #>.debug.dump.clusters=<bitmask>
```

要将完整的集群位掩码和参数列表打印到屏幕，传递 `-d` 参数。例如：

```sh
sysctl -d dev.ice.0.debug.dump.clusters
```

`clusters` 的可能位掩码值：

- 0 - 转储所有集群（仅在 Intel Ethernet E810 系列和 Intel Ethernet E830 系列上支持）
- 0x1 - 交换
- 0x2 - ACL
- 0x4 - Tx 调度器
- 0x8 - 配置文件配置
- 0x20 - 链路
- 0x80 - DCB
- 0x100 - L2P
- 0x400000 - 可管理性事务（仅在 Intel Ethernet E810 系列上支持）

例如，要转储交换、DCB 和 L2P 集群，使用以下命令：

```sh
sysctl dev.ice.0.debug.dump.clusters=0x181
```

要转储所有集群，使用以下命令：

```sh
sysctl dev.ice.0.debug.dump.clusters=0
```

注意：使用 0 将跳过可管理性事务数据。

如果未指定单个集群，驱动会将所有集群转储到单个文件。使用以下命令发出调试转储命令：

```sh
sysctl -b dev.ice.<interface #>.debug.dump.dump=1 > dump.bin
```

注意：如果 sysctl 未设置为"1"，驱动将不会收到命令。

将上面的"dump.bin"替换为首选文件名。

要在后续调试转储之前清除 `clusters` 掩码然后进行转储：

```sh
sysctl dev.ice.0.debug.dump.clusters=0
sysctl dev.ice.0.debug.dump.dump=1
```

### 调试 PHY 统计信息

ice 驱动支持从 Intel(R) Ethernet 810 系列设备获取 PHY 寄存器的值，以便在运行时调试链路和连接问题。

驱动提供以下信息：

- Rx 和 Tx 均衡参数
- RS FEC 可纠正和不可纠正块计数

使用以下 sysctl 读取 PHY 寄存器：

```sh
sysctl dev.ice.<interface #>.debug.phy_statistics
```

注意：寄存器的内容不是人类可读的。与固件日志和调试转储一样，请与客户支持合作解码文件。

### 发送均衡

某些 Intel(R) Ethernet 800 系列设备允许启用发送均衡功能以改善特定条件下的发送性能。启用后，此功能应能在队列和/或 PF 与 VF 之间提供更一致的发送性能。

默认情况下，NVM 中禁用发送均衡。要启用此功能，使用以下方法之一持久更改设备设置：

- 使用以太网端口配置工具（EPCT）启用 `tx_balancing` 选项。更多信息请参见 EPCT 自述文件。
- 在 UEFI HII 中启用发送均衡设备设置。

驱动加载时，从 NVM 读取发送均衡设置并相应地配置设备。

注意：用户在 EPCT 或 HII 中对发送均衡的选择在重启后保持不变。系统必须重启才能使所选设置生效。

此设置为设备范围。

驱动、NVM 和 DDP 包都必须支持此功能才能启用该功能。

### 温度监控

Intel(R) Ethernet 810 系列和 Intel(R) Ethernet 830 系列设备可通过以下命令显示温度数据（摄氏度）：

```sh
sysctl dev.ice.<interface #>.temp
```

### 网络内存缓冲区分配

FreeBSD 默认可能有较少的网络内存缓冲区（mbuf）。如果可用 mbuf 数量过低，可能导致驱动初始化失败和/或导致系统无响应。通过运行 `netstat` `-m` 检查系统是否处于 mbuf 不足状态。通过编辑 **/etc/sysctl.conf** 中的以下行来增加 mbuf 数量：

```sh
kern.ipc.nmbclusters
kern.ipc.nmbjumbop
kern.ipc.nmbjumbo9
kern.ipc.nmbjumbo16
kern.ipc.nmbufs
```

应分配的内存量因系统而异，可能需要一些试错。此外，在 **/etc/sysctl.conf** 中增加以下值可能有助于提高网络性能：

```sh
kern.ipc.maxsockbuf
net.inet.tcp.sendspace
net.inet.tcp.recvspace
net.inet.udp.maxdgram
net.inet.udp.recvspace
```

### 附加工具

Intel 提供了附加工具来帮助配置和更新此驱动涵盖的适配器。这些工具可以直接从 Intel 下载，下载地址为 Lk <https://downloadcenter.intel.com> ，通过搜索其名称：

- 要更改 E810-C 适配器上 QSFP28 端口的行为，使用 Intel **Ethernet Port Configuration Tool - FreeBSD.**
- 要更新适配器上的固件，使用 Intel **Non-Volatile Memory (NVM) Update Utility for Intel Ethernet Network Adapters E810 series - FreeBSD**

### 光模块与自动协商

基于 100GBASE-SR4、有源光缆（AOC）和有源铜缆（ACC）的模块不支持 IEEE 规范中的自动协商。要使用这些模块获得链路，必须在链路伙伴的交换机端口上关闭自动协商。

请注意，适配器还支持所有符合 SFF-8431 v4.1 和 SFF-8472 v10.4 规范的无源和有源限幅直连电缆。

### PCI-Express 插槽带宽

某些 PCIe x8 插槽实际上配置为 x4 插槽。这些插槽对于双端口和四端口设备的全线速带宽不足。此外，如果将支持 PCIe v4.0 或 v3.0 的适配器放入 PCIe v2.x 插槽，将无法达到全带宽。

驱动检测到这种情况并在系统日志中写入以下消息：

> PCI-Express bandwidth available for this device
> may be insufficient for optimal performance.
> Please move the device to a different PCI-e link
> with more lanes and/or higher transfer rate.

如果发生此错误，将适配器移至真正的 PCIe x8 或 x16 插槽可解决问题。为获得最佳性能，将设备安装在以下 PCI 插槽中：

- 任何支持 100Gbps 的 Intel(R) Ethernet 800 系列设备：安装在 PCIe v4.0 x8 或 v3.0 x16 插槽中
- 支持 200Gbps 的 Intel(R) Ethernet 830 系列设备：安装在 PCIe v5.0 x8 或 v4.0 x16 插槽中

有关硬件需求的问题，请参阅适配器附带的文档。

## 硬件

`ice` 驱动支持以下 Intel 800 系列 1Gb 至 200Gb 以太网控制器：

- Intel Ethernet Controller E810-C
- Intel Ethernet Controller E810-XXV
- Intel Ethernet Connection E822-C
- Intel Ethernet Connection E822-L
- Intel Ethernet Connection E823-C
- Intel Ethernet Connection E823-L
- Intel Ethernet Connection E825-C
- Intel Ethernet Connection E830-C
- Intel Ethernet Connection E830-CC
- Intel Ethernet Connection E830-L
- Intel Ethernet Connection E830-XXV
- Intel Ethernet Connection E835-C
- Intel Ethernet Connection E835-CC
- Intel Ethernet Connection E835-L
- Intel Ethernet Connection E835-XXV

`ice` 驱动支持此系列中部分带有 SFP28/QSFP28 笼的适配器，这些适配器的固件要求使用 Intel 认证模块；以下列出了这些认证模块。驱动无法禁用此认证检查。

`ice` 驱动支持使用以下 QSFP28 模块的 100Gb 以太网适配器：

- Intel 100G QSFP28 100GBASE-SR4 E100GQSFPSR28SRX
- Intel 100G QSFP28 100GBASE-SR4 SPTMBP1PMCDF
- Intel 100G QSFP28 100GBASE-CWDM4 SPTSBP3CLCCO
- Intel 100G QSFP28 100GBASE-DR SPTSLP2SLCDF

`ice` 驱动支持使用以下 SFP28 模块的 25Gb 和 10Gb 以太网适配器：

- Intel 10G/25G SFP28 25GBASE-SR E25GSFP28SR
- Intel 25G SFP28 25GBASE-SR E25GSFP28SRX（扩展温度）
- Intel 25G SFP28 25GBASE-LR E25GSFP28LRX（扩展温度）

`ice` 驱动支持使用以下 SFP+ 模块的 10Gb 和 1Gb 以太网适配器：

- Intel 1G/10G SFP+ 10GBASE-SR E10GSFPSR
- Intel 1G/10G SFP+ 10GBASE-SR E10GSFPSRG1P5
- Intel 1G/10G SFP+ 10GBASE-SR E10GSFPSRG2P5
- Intel 10G SFP+ 10GBASE-SR E10GSFPSRX（扩展温度）
- Intel 1G/10G SFP+ 10GBASE-LR E10GSFPLR

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。有关将 iflib sysctl 变量用作可调参数的更多信息，请参见 [iflib(4)](iflib.4.md) 手册页。

**`hw.ice.enable_health_events`** 设置为 1 可在所有设备上启用固件健康事件报告。默认启用。如果启用，当驱动收到固件健康事件消息时，它将向内核消息缓冲区打印事件描述，并在适用时提供可能采取的补救措施。

**`hw.ice.irdma`** 设置为 1 可启用 RDMA 客户端接口，[irdma(4)](irdma.4.md) 驱动需要此接口。默认启用。

**`hw.ice.rdma_max_msix`** 设置为 [irdma(4)](irdma.4.md) 驱动分配使用的每设备 MSI-X 向量最大数量。默认为 64。

**`hw.ice.debug.enable_tx_fc_filter`** 设置为 1 可在所有设备上启用 Tx 流控制过滤器。默认启用。如果启用，硬件将丢弃任何非源自硬件的 Ethertype 0x8808 控制帧。

**`hw.ice.debug.enable_tx_lldp_filter`** 设置为 1 可在所有设备上启用 Tx LLDP 过滤器。默认启用。如果启用，硬件将丢弃任何非源自硬件的 Ethertype 0x88cc LLDP 帧。必须禁用此功能才能使用 LLDP 守护进程软件，如 lldpd(8)。

**`hw.ice.debug.ice_tx_balance_en`** 设置为 1 可允许驱动在 DDP 包配置时使用 5 层 Tx 调度器树拓扑。默认启用。

## SYSCTL 变量

**`dev.ice.#.current_speed`** 显示接口的当前链路速度。应与 [ifconfig(8)](../man8/ifconfig.8.md) 显示的使用中介质类型的速度匹配。

**`dev.ice.#.fw_version`** 显示适配器的当前固件和 NVM 版本。此信息应随任何支持请求一起提交。

**`dev.ice.#.ddp_version`** 显示下载到适配器的当前 DDP 包版本。此信息应随任何支持请求一起提交。

**`dev.ice.#.pba_number`** 显示产品板组件编号。可用于帮助识别使用中的适配器类型。根据适配器类型，此 sysctl 可能不存在。

**`dev.ice.#.hw.mac.*`** 此 sysctl 树包含硬件为端口收集的统计信息。

## 中断风暴

需要注意的是，100G 操作可能产生大量中断，通常被内核错误地解释为风暴状态。建议通过将 `hw.intr_storm_threshold` 设置为 0 来解决此问题。

## IOVCTL 选项

使用 iovctl(8) 时，驱动支持为创建的 VF（虚拟功能）提供附加可选参数：

**mac-addr** (unicast-mac) 设置 VF 将使用的以太网 MAC 地址。如果未指定，VF 将使用随机生成的 MAC 地址，并将"allow-set-mac"设置为 true。

**mac-anti-spoof** (bool) 防止 VF 发送源地址与其自身不匹配的以太网帧。默认启用。

**allow-set-mac** (bool) 允许 VF 设置自己的以太网 MAC 地址。默认不允许。

**allow-promisc** (bool) 允许 VF 检查发送到其创建端口的所有流量。默认禁用。

**num-queues** (uint16_t) 指定 VF 将拥有的队列数量。默认情况下，设置为 VF 支持的 MSI-X 向量数减一。

**mirror-src-vsi** (uint16_t) 通过将此值设置为 -1 以外的值，指定 VF 将从哪个 VSI 镜像流量。来自该 VSI 的所有流量将镜像到此 VF。可用作 Sx RDMA Monitoring 部分中描述的方法之外的另一种镜像 RDMA 流量到其他接口的方法。不受"allow-promisc"参数影响。

**max-vlan-allowed** (uint16_t) 指定 VF 可使用的最大 VLAN 过滤器数量。在 VLAN 上接收流量需要硬件过滤器，这是有限资源；此参数用于防止 VF 饿死其他 VF 或 PF 的过滤器资源。默认设置为 16。

**max-mac-filters** (uint16_t) 指定 VF 可使用的最大 MAC 地址过滤器数量。每个允许的 MAC 地址需要硬件过滤器，这是有限资源；此参数用于防止 VF 饿死其他 VF 或 PF 的过滤器资源。VF 的默认 MAC 地址不计入此限制。默认设置为 64。

使用 iovctl(8) 的 `-S` 选项可找到最新的参数及其默认值列表。

有关标准和必需参数的更多信息，请参见 iovctl.conf(5)。

## 支持

如需一般信息和支持，请访问 Intel 支持网站：Lk <http://www.intel.com/support/> 。

如果使用受支持的适配器发现此驱动的问题，请将与问题相关的所有具体信息发送邮件至 <freebsd@intel.com>。

## 参见

[iflib(4)](iflib.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`ice` 设备驱动最早出现在 FreeBSD 12.2 中。

## 作者

`ice` 驱动由 Intel Corporation <freebsd@intel.com> 编写。
