# cgem(4)

`cgem` — Cadence GEM 千兆以太网驱动

## 名称

`cgem`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device ether
> device miibus
> device cgem

## 描述

`cgem` 驱动为 Cadence GEM（千兆以太网 MAC）提供支持。Cadence GEM 用于某些 SoC（片上系统）设备，如 Xilinx Zynq-7000、Xilinx Zynq UltraScale+ 和 SiFive HiFive Unleashed。

`cgem` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可使用 [ifconfig(8)](../man8/ifconfig.8.md) 或通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseT`** 设置双绞线上的 1000Mbps（千兆以太网）操作。GEM 仅支持 `full-duplex` 模式下的 1000Mbps。

`cgem` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

驱动提供对 TCP/UDP/IP 校验和卸载的支持（虽然默认禁用）。设备和驱动还支持用于 VLAN 的 1536 字节帧（vlanmtu）。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`dev.cgem.%d.rxbufs`** 分配给硬件的接收缓冲区数。默认值为 256。最大值为 511。如果在接口 UP 时增加此数字，它将不会生效，直到收到下一个数据包。如果在接口 UP 时减少此数字，缓冲区不会立即从接收缓冲环中移除，但随着数据包的接收，缓冲区数量将减少，直到达到新值。

**`dev.cgem.%d.rxhangwar`** 此可调参数启用一种变通方法以从接收挂起中恢复。默认值为 1。设置为 0 禁用此变通方法。

以下只读变量作为 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`dev.cgem.%d._rxoverruns`** 此变量计数接收数据包缓冲区溢出中断的次数。

**`dev.cgem.%d._rxnobufs`** 此变量计数由于 GEM 缓冲环变空而引起的中断次数。

**`dev.cgem.%d._rxdmamapfails`** 此变量是接收路径中 bus_dmamap_load_mbuf_sg(9) 失败的次数。

**`dev.cgem.%d._txfull`** GEM 发送环已满的次数。

**`dev.cgem.%d._txdmamapfails`** 此变量是发送路径中 bus_dmamap_load_mbuf_sg(9) 失败的次数。

**`dev.cgem.%d._txdefrags`** 此变量是由于排队等待发送的数据包 DMA 段过多而需要调用 m_defrag(9) 的次数。

**`dev.cgem.%d._txdefragfails`** 此变量是 m_defrag(9) 失败的次数。

**`dev.cgem.%d.stats.*`** 以下变量是硬件提供的有用 MAC 计数器：

**`dev.cgem.%d.stats.tx_bytes`** 无错误传输帧的字节数的 64 位计数器。

**`dev.cgem.%d.stats.tx_frames`** 除暂停帧外无错误传输的帧计数器。

**`dev.cgem.%d.stats.tx_frames_bcast`** 除暂停帧外无错误传输的广播帧计数器。

**`dev.cgem.%d.stats.tx_frames_multi`** 除暂停帧外无错误传输的多播帧计数器。

**`dev.cgem.%d.stats.tx_frames_pause`** 无错误传输的暂停帧计数器。

**`dev.cgem.%d.stats.tx_frames_64b`** 无错误传输的 64 字节帧计数器。

**`dev.cgem.%d.stats.tx_frames_65to127b`** 无错误传输的 65 至 127 字节帧计数器。

**`dev.cgem.%d.stats.tx_frames_128to255b`** 无错误传输的 128 至 255 字节帧计数器。

**`dev.cgem.%d.stats.tx_frames_256to511b`** 无错误传输的 256 至 511 字节帧计数器。

**`dev.cgem.%d.stats.tx_frames_512to1023b`** 无错误传输的 512 至 1023 字节帧计数器。

**`dev.cgem.%d.stats.tx_frames_1024to1536b`** 无错误传输的 1024 至 1536 字节帧计数器。

**`dev.cgem.%d.stats.tx_under_runs`** 由于发送欠载而未传输的帧计数器。

**`dev.cgem.%d.stats.tx_single_collisn`** 在成功传输之前经历单次冲突的帧计数器。

**`dev.cgem.%d.stats.tx_multi_collisn`** 在成功传输之前经历 2 至 15 次冲突的帧计数器。

**`dev.cgem.%d.stats.tx_excsv_collisn`** 由于经历 16 次冲突而未能传输的帧计数器。

**`dev.cgem.%d.stats.tx_late_collisn`** 经历迟发冲突的帧计数器。

**`dev.cgem.%d.stats.tx_deferred_frames`** 由于在首次尝试传输时载波侦听处于活动状态而经历延迟的帧计数器。

**`dev.cgem.%d.stats.tx_carrier_sense_errs`** 传输期间未看到载波侦听，或在无冲突的传输帧中载波侦听在断言之后又被取消断言的传输帧计数器。

**`dev.cgem.%d.stats.rx_bytes`** 除暂停帧外无错误接收字节数的 64 位计数器。

**`dev.cgem.%d.stats.rx_frames`** 除暂停帧外无错误接收帧计数器。

**`dev.cgem.%d.stats.rx_frames_bcast`** 除暂停帧外无错误接收的广播帧计数器。

**`dev.cgem.%d.stats.rx_frames_multi`** 除暂停帧外无错误接收的多播帧计数器。

**`dev.cgem.%d.stats.rx_frames_pause`** 无错误接收的暂停帧计数器。

**`dev.cgem.%d.stats.rx_frames_64b`** 无错误接收的 64 字节帧计数器。

**`dev.cgem.%d.stats.rx_frames_65to127b`** 无错误接收的 65 至 127 字节帧计数器。

**`dev.cgem.%d.stats.rx_frames_128to255b`** 无错误接收的 128 至 255 字节帧计数器。

**`dev.cgem.%d.stats.rx_frames_256to511b`** 无错误接收的 256 至 511 字节帧计数器。

**`dev.cgem.%d.stats.rx_frames_512to1023b`** 无错误接收的 512 至 1023 字节帧计数器。

**`dev.cgem.%d.stats.rx_frames_1024to1536b`** 无错误接收的 1024 至 1536 字节帧计数器。

**`dev.cgem.%d.stats.rx_frames_undersize`** 接收到的长度小于 64 字节且不具有 CRC 错误或对齐错误的帧计数器。

**`dev.cgem.%d.stats.rx_frames_oversize`** 接收到的超过 1536 字节且不具有 CRC 错误或对齐错误的帧计数器。

**`dev.cgem.%d.stats.rx_frames_jabber`** 接收到的超过 1536 字节且具有 CRC 错误、对齐错误或接收符号错误的帧计数器。

**`dev.cgem.%d.stats.rx_frames_fcs_errs`** 接收到的具有错误 CRC 且长度在 64 至 1536 字节之间的帧计数器。

**`dev.cgem.%d.stats.rx_frames_length_errs`** 接收到的长度短于从长度字段中提取的值的帧计数器。

**`dev.cgem.%d.stats.rx_symbol_errs`** 接收符号错误计数器。

**`dev.cgem.%d.stats.rx_align_errs`** 不是整数字节数的接收帧计数器。

**`dev.cgem.%d.stats.rx_resource_errs`** 由 MAC 成功接收但由于没有可用接收缓冲区而无法复制到内存的帧计数器。

**`dev.cgem.%d.stats.rx_overrun_errs`** 地址被识别但由于接收溢出而未复制到内存的帧计数器。

**`dev.cgem.%d.stats.rx_frames_ip_hdr_csum_errs`** 启用校验和卸载时由于 IP 头部校验和不正确而丢弃的帧计数器。

**`dev.cgem.%d.stats.rx_frames_tcp_csum_errs`** 启用校验和卸载时由于 TCP 校验和不正确而丢弃的帧计数器。

**`dev.cgem.%d.stats.rx_frames_udp_csum_errs`** 启用校验和卸载时由于 UDP 校验和不正确而丢弃的帧计数器。

## 参见

[miibus(4)](miibus.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "Zynq-7000 SoC Technical Reference Manual (Xilinx doc UG585)"。

## 历史

`cgem` 设备驱动首次出现于 FreeBSD 10.0。

## 作者

`cgem` 驱动和本手册页由 Thomas Skibo <thomasskibo@yahoo.com> 编写。

## 缺陷

GEM 可以执行 TCP/UDP/IP 校验和卸载。然而，启用发送校验和卸载时，GEM 会为其传输的所有数据包生成并替换校验和。在转发数据包的系统中，设备可能潜在地更正在传输中损坏的数据包的校验和。因此，校验和卸载默认禁用，但可使用 ifconfig(8) 启用。

启用接收校验和卸载时，设备将丢弃具有错误 TCP/UDP/IP 校验和的数据包。错误的数据包不会计入任何 [netstat(1)](../man1/netstat.1.md) 统计信息。有 [sysctl(8)](../man8/sysctl.8.md) 变量可计数硬件丢弃的数据包（见下文）。

Zynq-7000 中使用的 GEM 存在一个 bug，使得接收器在高负载下可能冻结。此问题在 Zynq-7000 SoC 技术参考手册（Xilinx UG585 v1.7）第 16.7 节“已知问题”中描述。`cgem` 驱动实现了手册中建议的变通方法。据信 Zynq UltraScale+ 和 SiFive SoC 中不存在此 bug，因此在那些实例中禁用变通方法，而在所有其他实例中启用。可通过将 `dev.cgem.%d.rxhangwar` [sysctl(8)](../man8/sysctl.8.md) 变量设置为 0 来禁用变通方法。
