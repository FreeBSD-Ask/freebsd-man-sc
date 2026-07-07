# ixl(4)

`ixl` — Intel Ethernet 700 系列驱动

## 名称

`ixl`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iflib
> device ixl

`要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_ixl_load="YES"
```

## 描述

### 特性

`ixl` 驱动为 Intel Ethernet 700 系列中的任何 PCI Express 适配器或 LOM（LAN On Motherboard）提供支持。截至本文撰写时，该系列包括以下型号的设备：

- XL710 (40G)
- X710 (10G)
- XXV710 (25G)
- X722 (10G)

该驱动支持 Jumbo Frames、TX/RX 校验和卸载、TCP 分段卸载（TSO）、大接收卸载（LRO）、VLAN 标签插入/提取、VLAN 校验和卸载、VLAN TSO 以及接收端转向（RSS），以上功能均同时支持 IPv4 和 IPv6。有关硬件信息和硬件需求相关问题，请参阅 Lk <http://support.intel.com/> 。

通过接口 MTU 设置提供对 Jumbo Frames 的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 可将适配器配置为接收和发送 Jumbo Frames。Jumbo Frames 的最大 MTU 大小为 9706。

卸载也通过接口控制，例如，可以设置和取消设置 IPv4 和 IPv6 的校验和、TSO4 和/或 TSO6，最后是 LRO。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

### 附加工具

Intel 提供了附加工具来帮助配置和更新此驱动涵盖的适配器。这些工具可以直接从 Intel 下载，下载地址为 Lk <https://downloadcenter.intel.com> ，通过搜索其名称，或通过安装某些软件包：

- 要更改 XL710 适配器上 QSFP+ 端口的行为，使用 Intel QCU（QSFP+ configuration utility）；通过 *sysutils/intel-qcu* 软件包安装。
- 要更新适配器上的固件，使用 Intel Non-Volatile Memory (NVM) Update Utility；通过 *sysutils/intel-nvmupdate-10g*、*sysutils/intel-nvmupdate-40g* 或 *sysutils/intel-nvmupdate-100g* 软件包安装。
- 驱动由 Intel 在 FreeBSD 内核之外提供；安装 *net/intel-ixl-kmod* 软件包以获取最新驱动。

## 硬件

`ixl` 驱动支持 Intel Ethernet 700 系列。此系列中大多数带有 SFP+/SFP28/QSFP+ 笼的适配器的固件要求使用 Intel 认证模块；以下列出了这些认证模块。驱动无法禁用此认证检查。

`ixl` 驱动支持使用以下 QSFP+ 模块的 40Gb 以太网适配器：

- Intel 4x10G/40G QSFP+ 40GBASE-SR4 E40GQSFPSR
- Intel 4x10G/40G QSFP+ 40GBASE-LR4 E40GQSFPLR

`ixl` 驱动支持使用以下 SFP28 模块的 25Gb 以太网适配器：

- Intel 10G/25G SFP28 25GBASE-SR E25GSFP28SR
- Intel 10G/25G SFP28 25GBASE-SR E25GSFP28SRX（扩展温度）

`ixl` 驱动支持使用以下 SFP+ 模块的 25Gb 和 10Gb 以太网适配器：

- Intel 1G/10G SFP+ SR FTLX8571D3BCV-IT
- Intel 1G/10G SFP+ SR AFBR-703SDZ-IN2
- Intel 1G/10G SFP+ LR FTLX1471D3BCV-IT
- Intel 1G/10G SFP+ LR AFCT-701SDZ-IN2
- Intel 1G/10G SFP+ 10GBASE-SR E10GSFPSR
- Intel 10G SFP+ 10GBASE-SR E10GSFPSRX（扩展温度）
- Intel 1G/10G SFP+ 10GBASE-LR E10GSFPLR

注意，适配器还支持所有符合 SFF-8431 v4.1 和 SFF-8472 v10.4 规范的无源和有源限幅直连电缆。

此列表并不完整；请查阅产品文档以获取受支持介质的最新列表。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

```sh
0 - 最佳可用方法
1 - 通过 I2CPARAMS 寄存器位操作
2 - 通过 I2CCMD 寄存器读写
3 - 使用 Admin Queue 命令（默认最佳）
```

**`hw.ixl.rx_itr`** RX 中断率值，默认设置为 62（124 微秒）。

**`hw.ixl.tx_itr`** TX 中断率值，默认设置为 122（244 微秒）。

**`hw.ixl.i2c_access_method`** 驱动通过 [sysctl(8)](../man8/sysctl.8.md) 或详细的 [ifconfig(8)](../man8/ifconfig.8.md) 信息显示进行 I2C 读写时使用的访问方法：使用 Admin Queue 仅在固件版本 1.7 或更新的 710 设备上受支持。默认设置为 0。

**`hw.ixl.enable_tx_fc_filter`** 过滤掉非适配器源发出的 Ethertype 0x8808 数据包。这可防止（可能不可信的）软件或 [iavf(4)](iavf.4.md) 设备发出流控制数据包并造成 DoS（拒绝服务）事件。默认启用。

**`hw.ixl.enable_head_writeback`** 当驱动查找硬件处理的最后一个 TX 描述符时，使用硬件写入内存的值，而非扫描描述符环查找已完成的描述符。默认启用；禁用可模拟 ix(4) 中的 TX 行为。

## SYSCTL 过程

**`dev.ixl.#.fc`** 设置适配器将在链路上通告的 802.3x 流控制模式。值为 0 时禁用流控制，3 启用全双工流控制，1 为 RX，2 为 TX 暂停。协商后的流控制设置可在 [ifconfig(8)](../man8/ifconfig.8.md) 中接口的 media 字段中查看。

**`dev.ixl.#.advertise_speed`** 设置接口将在链路上通告的速度。`dev.ixl.#.supported_speeds` 包含允许设置的速度。

**`dev.ixl.#.current_speed`** 显示当前速度。

**`dev.ixl.#.fw_version`** 显示适配器的当前固件和 NVM 版本。

**`dev.ixl.#.debug.switch_vlans`** 设置硬件自身用于处理内部服务的 Ethertype。具有此 Ethertype 的帧将被静默丢弃。默认值为 `0x88a8`，这是 IEEE 802.1ad VLAN 堆叠的知名编号。如果需要 802.1ad 支持，请将此编号设置为任何其他 Ethertype，即 `0xffff`。

## 中断风暴

需要注意的是，40G 操作可能产生大量中断，通常被内核错误地解释为风暴状态。建议通过设置以下参数解决此问题：

**`hw.intr_storm_threshold: 0`**

## IOVCTL 选项

使用 iovctl(8) 时，驱动支持为创建的 VF（虚拟功能）提供附加可选参数：

**mac-addr** (unicast-mac) 设置 VF 将使用的以太网 MAC 地址。如果未指定，VF 将使用随机生成的 MAC 地址。

**mac-anti-spoof** (bool) 防止 VF 发送源地址与其自身不匹配的以太网帧。

**allow-set-mac** (bool) 允许 VF 设置自己的以太网 MAC 地址。

**allow-promisc** (bool) 允许 VF 检查发送到端口的所有流量。

**num-queues** (uint16_t) 指定 VF 将拥有的队列数量。默认情况下，此值设置为 VF 支持的 MSI-X 向量数减一。

使用 iovctl(8) 的 `-S` 选项可找到最新的参数及其默认值列表。

## 支持

如需一般信息和支持，请访问 Intel 支持网站：Lk <http://support.intel.com/> 。

如果使用受支持的适配器发现此驱动的问题，请将与问题相关的所有具体信息发送邮件至 <freebsd@intel.com>。

## 参见

arp(4), [iavf(4)](iavf.4.md), [iflib(4)](iflib.4.md), netintro(4), vlan(4), [ifconfig(8)](../man8/ifconfig.8.md), iovctl(8)

## 历史

`ixl` 设备驱动最早出现于 FreeBSD 10.1。它在 FreeBSD 12 中被转换为使用 iflib(9)。

## 作者

`ixl` 驱动由 Jack Vogel <jfv@freebsd.org> 和 Eric Joyner <erj@freebsd.org> 编写。
