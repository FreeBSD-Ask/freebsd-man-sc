# iflibtxrx.9

`iflibtxrx` — 设备相关传输与接收函数

## 名称

`iflibtxrx`

## 概要

```c
#include <ifdi_if.h>
```

### 接口操作函数

```c
int
isc_txd_encap(void *sc, if_pkt_info_t pi)

void
isc_txd_flush(void *sc, uint16_t qid, uint32_t _pidx_or_credits_)

int
isc_txd_credits_update(void *sc, uint16_t qid, bool clear)

int
isc_rxd_available(void *sc, uint16_t qsid, uint32_t cidx)

void
isc_rxd_refill(void *sc, uint16_t qsid, uint8_t flid, uint32_t pidx,
    uint64_t *paddrs, caddr_t *vaddrs, uint16_t count)

void
isc_rxd_flush(void *sc, uint16_t qsid, uint8_t flid, uint32_t pidx)

int
isc_rxd_pkt_get(void *sc, if_rxd_info_t ri)
```

### 全局变量

```c
extern struct if_txrx
```

## 数据结构

处理数据包传输和接收的设备相关机制主要由上述命名的函数定义。if_pkt_info 数据结构包含数据包传输所需的统计信息和识别信息。而数据包接收的数据结构是 if_rxd_info 结构。

### if_pkt_info 结构

`struct if_pkt_info` 的字段如下：

**`ipi_len`** (`uint32_t`) 表示要在传输队列上发送的数据包大小。

**`ipi_segs`** (`bus_dma_segment_t *`) 指向 iflib 中定义的设备无关传输队列的 bus_dma_segment 的指针。

**`ipi_qsidx`** 按顺序分配给每个传输队列的唯一索引值。用于引用当前正在传输的队列。

**`ipi_nsegs`** (`uint16_t`) 要读入设备相关传输描述符的描述符数。

**`ipi_ndescs`** (`uint16_t`) 使用中的描述符数。通过从新的 pidx 值减去旧的 pidx 值计算。

**`ipi_flags`** (`uint16_t`) 按每包定义的标志。

**`ipi_pidx`** (`uint32_t`) 发送到 isc_encap 函数进行封装和后续传输的第一个 pidx 值。

**`ipi_new_pidx`** (`uint32_t`) isc_encap 函数终止后设置的值。此值将成为下次调用该函数时发送到 isc-encap 的第一个 pidx。

**`以下字段用于卸载处理`**

**`ipi_csum_flags`** (`uint64_t`) 描述校验和值的标志，按每包使用。

**`ipi_tso_segsz`** (`uint16_t`) TSO 段大小。

**`ipi_mflags`** (`uint16_t`) 描述 mbuf 操作参数的标志。

**`ipi_vtag`** (`uint16_t`) 包含以太网帧中的 VLAN 信息。

**`ipi_etype`** (`uint16_t`) 由 struct ether_vlan_header 包含的以太网头协议类型。

**`ipi_ehrdlen`** (`uint8_t`) 以太网头的长度。

**`ipi_ip_hlen`** (`uint8_t`) TCP 头的长度。

**`ipi_tcp_hlen`** (`uint8_t`) TCP 头的长度。

**`ipi_tcp_hflags`** (`uint8_t`) 描述 TCP 头操作参数的标志。

**`ipi_ipproto`** (`uint8_t`) 指定使用中的 IP 协议类型。例如 TCP、UDP 或 SCTP。

### if_rxd_info 结构

`struct if_rxd_info` 的字段如下：

**`iri_qsidx`** (`uint16_t`) 按顺序分配给每个接收队列的唯一索引值。用于引用当前正在接收的队列。

**`iri_vtag`** (`uint16_t`) 包含以太网帧中的 VLAN 信息。

**`iri_len`** (`uint16_t`) 表示接收到的数据包大小。

**`iri_next_offset`** (`uint16_t`) 表示下一个要接收的数据包的偏移值。Null 值表示数据包结束。

**`iri_cidx`** (`uint32_t`) 表示消费者队列中当前正在处理的数据包的索引值。

**`iri_flowid`** (`uint32_t`) 数据包的 RSS 哈希值。

**`iri_flags`** (`uint`) 描述接收数据包中包含的 mbuf 操作参数的标志。

**`iri_csum_flags`** (`uint32_t`) 描述接收数据包中包含的校验和值的标志。

**`iri_csum_data`** (`uint32_t`) [mbuf(9)](mbuf.9.md) 数据包头中包含的校验和数据。

**`iri_m`** (`struct mbuf *`) 用于管理自己接收队列的驱动程序的 mbuf。

**`iri_ifp`** (`struct ifnet *`) 返回接口结构的链接。由每个 softc 具有多个接口的驱动程序使用。

**`iri_rsstype`** (`uint8_t`) RSS 哈希类型的值。

**`iri_pad`** (`uint8_t`) 接收数据包含的任何填充的长度。

**`iri_qidx`** (`uint8_t`) 表示队列事件的类型。如果值 >= 0，则为 freelist id，否则为完成队列事件。

## 函数

所有函数调用仅与数据包传输或接收关联。作为以下所有函数第一个参数传递的 `void *sc` 表示驱动程序的 softc。

### 传输数据包函数

**Fn** `isc_txd_encap` 在接口上发送数据包的传输函数。if_pkt_info 数据结构包含描述数据包的数据信息字段。此函数成功返回 0，否则返回错误值。

**Fn** `isc_txd_flush` 在 isc_txd_encap 函数传输数据包后立即调用的刷新函数。它更新硬件生产者索引或在 qid 编号指定的队列中递增用于 pidx_or_credits 的描述符。这通常称为戳门铃寄存器。

**Fn** `isc_txd_credits_update` 信用函数推进缓冲区环并计算处理过的信用（描述符）。在 I/O 完成之前，它清除多段情况下的范围并更新处理过的数据包计数。函数返回处理过的信用数。

### 接收数据包函数

**Fn** `isc_rxd_available` 函数计算从 idx 给定位置的剩余描述符数。函数返回此值。

**Fn** `isc_rxd_refill` 从物理地址 paddrs 开始，函数将数据包读入 rx_ring，直到达到由 count 指定的值。vaddrs 通常不需要，为在数据包头中放置自己元数据的设备提供。

**Fn** `isc_rxd_flush` 刷新函数将队列集号 qid 中的空闲列表 flid 上的生产者指针更新为 pidx，以反映新缓冲区的存在。

**Fn** `isc_rxd_pkt_get` 处理单个软件描述符。rxr->rx_base[i] 包含描述接收到的数据包的描述符。关于 ri 引用的缓冲区的硬件特定信息在数据结构 if_rxd_info 中返回。

## 参见

[iflibdd(9)](iflibdd.9.md), [iflibdi(9)](iflibdi.9.md), [mbuf(9)](mbuf.9.md)

## 作者

本手册页由 Nicole Graziano 编写。
