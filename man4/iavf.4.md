# iavf.4

`iavf` — Intel Ethernet 自适应虚拟功能驱动

## 名称

`iavf`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iflib
> device iavf

`要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_iavf_load="YES"
```

## 描述

`iavf` 驱动为从特定 Intel Ethernet 设备创建的任何 PCI 虚拟功能提供支持。此驱动与绑定到以下设备的虚拟功能兼容：

- Intel® Ethernet Controller E810-C
- Intel® Ethernet Controller E810-XXV
- Intel® Ethernet Connection E822-C
- Intel® Ethernet Connection E822-L
- Intel® Ethernet Connection E823-C
- Intel® Ethernet Connection E823-L
- Intel® Ethernet Controller I710
- Intel® Ethernet Controller X710
- Intel® Ethernet Controller XL710
- Intel® Ethernet Network Connection X722
- Intel® Ethernet Controller XXV710
- Intel® Ethernet Controller V710

此 VF 驱动对应的物理功能（PF）驱动为：

- [ice(4)](ice.4.md)
- [ixl(4)](ixl.4.md)

有关硬件需求的问题，请参阅 Intel Ethernet 适配器附带的文档。列出的所有硬件需求均适用于 FreeBSD。

### VF 驱动

VF 驱动通常用于虚拟化环境中，其中主机驱动管理 SR-IOV，并向客户机提供 VF 设备。

在 FreeBSD 客户机中，将加载 iavf 驱动，并使用分配给它的 VF 设备运行。

VF 驱动提供与核心驱动大部分相同的功能，但实际上从属于主机。对许多控件的访问通过所谓的"Admin 队列"向主机发请求来完成。这些是启动和初始化事件；但一旦开始运行，设备是自包含的，应能达到接近原生的性能。

VF 环境的一些显著限制：

- PF 可以配置 VF 允许混杂模式，使用 iovctl.conf(5) 中的配置参数；否则，混杂模式将无法工作
- PF 不提供介质信息，因此活动介质在 [ifconfig(8)](../man8/ifconfig.8.md) 中始终显示为 auto

### 自适应虚拟功能

自适应虚拟功能（AVF）允许虚拟功能驱动（VF）适应其所关联的物理功能驱动（PF）不断变化的功能集。这使系统管理员能够更新 PF 而无需更新与之关联的所有 VF。所有 AVF 都有一个共同的设备 ID 和品牌字符串。

AVF 具有一组称为"基本模式"的最小功能集，但根据 AVF 所关联的 PF 中可用的功能，可能提供附加功能。以下是基本模式功能：

- 4 个队列对（QP）和用于 Tx/Rx 的关联配置状态寄存器（CSR）
- iavf 描述符和环形格式
- 描述符回写完成
- 1 个控制队列，带有 iavf 描述符、CSR 和环形格式
- 5 个 MSI-X 中断向量和对应的 iavf CSR
- 1 个中断节流率（ITR）索引
- 每个 VF 1 个虚拟站接口（VSI）
- 1 个流量类（TC），TC0
- 接收端缩放（RSS），具有 64 条目间接表和密钥，通过 PF 配置
- 每个 VF 保留 1 个单播 MAC 地址
- Intel® Ethernet 800 系列设备上每个 VF 8 个 MAC 地址过滤器
- Intel® Ethernet 700 系列设备上每个 VF 16 个 MAC 地址过滤器
- 无状态卸载——非隧道校验和
- AVF 设备 ID
- HW 邮箱用于 VF 到 PF 的通信

## 配置与调优

### 重要的系统配置更改

需要注意的是，100G 操作可能产生大量中断，通常被内核错误地解释为风暴状态。建议通过将 `hw.intr_storm_threshold` 设置为 0 来解决此问题。

默认值为 1000。

使用大 MTU 可获得最佳吞吐量结果；尽可能使用 9706。每个环的默认描述符数为 1024。根据你的使用场景，增加此值可能会提高性能。

### 不使用 iflib 的配置

[iflib(4)](iflib.4.md) 是 FreeBSD 网络接口驱动的通用框架，使用一组共享的 sysctl 名称。

默认的 `iavf` 驱动依赖它，但可以在不使用它的情况下编译。

### Jumbo 帧

Jumbo 帧支持通过将最大传输单元（MTU）更改为大于默认值 1500 的值来启用。

使用 [ifconfig(8)](../man8/ifconfig.8.md) 命令增加 MTU 大小。

要确认两个特定设备之间使用的 MTU，使用 [route(8)](../man8/route.8.md)：

```sh
route get <destination_IP_address>
```

注意：

- Jumbo 帧的最大 MTU 设置为 9706。这对应于 9728 字节的最大 jumbo 帧大小。
- 此驱动将尝试使用多个页大小的缓冲区来接收每个 jumbo 数据包。这有助于避免分配接收数据包时的缓冲区不足问题。
- 使用 jumbo 帧时，丢包可能对吞吐量产生更大影响。如果在启用 jumbo 帧后观察到性能下降，启用流控制可能会缓解此问题。

### 校验和卸载

校验和卸载支持 TCP 和 UDP 数据包，并在发送和接收方向均受支持。

TSO（TCP 分段卸载）支持 IPv4 和 IPv6。这两个功能均通过 [ifconfig(8)](../man8/ifconfig.8.md) 启用和禁用。

注意：

- TSO 需要 Tx 校验和；如果禁用 Tx 校验和，则 TSO 也将被禁用。

### LRO

LRO（大接收卸载）可提高 Rx 性能。但是，它与数据包转发工作负载不兼容。你应仔细评估环境，在可能时启用 LRO。

### Rx 和 Tx 描述符环

允许你独立设置 Rx 和 Tx 描述符环。通过以下 [iflib(4)](iflib.4.md) sysctl 设置：

**dev.iavf.#.iflib.override_nrxds**

**dev.iavf.#.iflib.override_ntxds**

### 链路级流控制（LFC）

VF 驱动无法访问流控制设置。必须从主机端管理。

## 参见

arp(4), [ice(4)](ice.4.md), [iflib(4)](iflib.4.md), [ixl(4)](ixl.4.md), [netintro(4)](netintro.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

有关功能的更多信息，请参见"Intel® Ethernet Adapters and Devices User Guide"。可从 Intel 网站以下任一地址获取：

- Lk <https://cdrdv2.intel.com/v1/dl/getContent/705831>
- Lk <https://www.intel.com/content/www/us/en/download/19373/adapter-user-guide-for-intel-ethernet-adapters.html>

有关如何识别你的适配器以及最新 Intel 网络驱动的信息，请参阅 Intel 支持网站：<Lk <http://www.intel.com/support>>

## 注意事项

### 驱动缓冲区溢出修复

修复 CVE-2016-8105（在 Intel SA-00069 <Lk <https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00069.html>> 中引用）的修复已包含在此版本及更高版本的驱动中。

### 网络内存缓冲区分配

FreeBSD 默认可能有较少的网络内存缓冲区（mbuf）。如果你的 mbuf 值过低，可能导致驱动初始化失败和/或导致系统无响应。可以通过运行 `netstat -m` 检查系统是否处于 mbuf 不足状态。通过编辑 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中的以下行来增加 mbuf 数量：

```sh
kern.ipc.nmbclusters
kern.ipc.nmbjumbop
kern.ipc.nmbjumbo9
kern.ipc.nmbjumbo16
kern.ipc.nmbufs
```

你分配的内存量因系统而异，可能需要一些试错。此外，在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中增加以下值可能有助于提高网络性能：

```sh
kern.ipc.maxsockbuf
net.inet.tcp.sendspace
net.inet.tcp.recvspace
net.inet.udp.maxdgram
net.inet.udp.recvspace
```

### UDP 压力测试丢包问题

在使用 `iavf` 驱动的小数据包 UDP 压力下，系统可能由于套接字缓冲区已满而丢弃 UDP 数据包。将 PF 驱动的流控制变量设置为最小值可能会解决此问题。

### 路由/桥接时禁用 LRO

转发流量时必须关闭 LRO。

## 支持

如需一般信息，请访问 Intel 支持网站 <Lk <http://www.intel.com/support/>。>

如果在受支持的内核和受支持的适配器上发现已发布源代码的问题，请将与问题相关的具体信息发送邮件至 <freebsd@intel.com>。

## 法律条款

Intel® 是 Intel Corporation 或其子公司在美国和/或其他国家的商标或注册商标。

其他名称和品牌可能被视为他人的财产。

## 历史

`iavf` 设备驱动最早以 `ixlv` 的名称出现在 FreeBSD 10.1 中。它在 FreeBSD 12.4 中被转换为使用 [iflib(4)](iflib.4.md) 并更名。

## 作者

`ixlv` 驱动由 Intel Corporation <freebsd@intel.com> 编写
