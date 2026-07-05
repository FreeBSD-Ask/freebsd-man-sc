# ieee80211_radiotap.9

`ieee80211_radiotap` — 802.11 设备数据包捕获支持

## 名称

`ieee80211_radiotap`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
void
ieee80211_radiotap_attach(struct ieee80211com *,
    struct ieee80211_radiotap_header *th, int tlen, uint32_t tx_radiotap,
    struct ieee80211_radiotap_header *rh, int rlen, uint32_t rx_radiotap)

int
ieee80211_radiotap_active_vap(struct ieee80211vap *)

int
ieee80211_radiotap_active(struct ieee80211com *)

void
ieee80211_radiotap_tx(struct ieee80211vap *, struct mbuf *)
```

## 描述

802.11 驱动程序使用的 `net80211` 层包括对称为 `radiotap` 的设备无关数据包捕获格式的支持，该格式可被 [tcpdump(1)](../man1/tcpdump.1.md) 等工具理解。此设施设计用于捕获 802.11 流量，包括不属于正常 802.11 帧结构的信息。

Radiotap 的设计旨在平衡对硬件无关、可扩展捕获格式的需求与嵌入式系统上节省 CPU 和内存带宽的需求。这些考虑导致了一种格式，由标准前导后跟指示可选捕获字段存在的可扩展位图组成。支持 `radiotap` 的 `net80211` 设备驱动程序定义两个与 `net80211` 共享的打包结构。这些结构在开头嵌入 `ieee80211_radiotap_header` 结构的实例，后续字段按适当顺序排列，宏用于设置 `it_present` 位图的位以指示哪些字段存在并由驱动程序填写。然后通过 `ieee80211_radiotap_attach` 调用在此信息中提供，在成功 `ieee80211_ifattach` 请求之后。

设置 radiotap 后，驱动程序只需为发送/接收的帧填写每包捕获状态，并在传输路径中调度捕获状态（因为在数据包交给设备之前控制权不返回 `net80211` 层）。为最小化开销，仅当一个或多个进程主动捕获数据时才应完成此工作；这通过 `ieee80211_radiotap_active_vap` 和 `ieee80211_radiotap_active` 之一检查。在传输路径中，捕获工作如下所示：

```c
if (ieee80211_radiotap_active_vap(vap)) {
	... /* 记录传输状态 */
	ieee80211_radiotap_tx(vap, m); /* 捕获传输事件 */
}
```

而在接收路径中，捕获在 `net80211` 中处理，但状态必须在调度帧之前捕获：

```c
if (ieee80211_radiotap_active(ic)) {
	... /* 记录接收状态 */
}
...
ieee80211_input(...);	/* 数据包捕获在 net80211 中处理 */
```

以下字段为 `radiotap` 定义，按它们应出现在提供给 `net80211` 的缓冲区中的顺序排列。

**`IEEE80211_RADIOTAP_F_CFP`** 帧在无竞争期（CFP）期间发送/接收。

**`IEEE80211_RADIOTAP_F_SHORTPRE`** 帧以短前导发送/接收。

**`IEEE80211_RADIOTAP_F_WEP`** 帧已加密。

**`IEEE80211_RADIOTAP_F_FRAG`** 帧是 802.11 分片。

**`IEEE80211_RADIOTAP_F_FCS`** 帧内容包含 FCS。

**`IEEE80211_RADIOTAP_F_DATAPAD`** 帧内容可能在 802.11 头和数据有效载荷之间有填充，以将有效载荷对齐到 32 位边界。

**`IEEE80211_RADIOTAP_F_BADFCS`** 帧以无效 FCS 接收。

**`IEEE80211_RADIOTAP_F_SHORTGI`** 帧以短保护间隔发送/接收。

```c
#include <net80211/_ieee80211.h>
```

```c
#include <net80211/ieee80211_radiotap.h>
```

**`IEEE80211_RADIOTAP_TSFT`** 此字段包含 MAC 的 802.11 时间同步功能（TSF）的无符号 64 位值，以微秒为单位。理论上，对于每个接收到的帧，此值在 MPDU 的第一位到达 MAC 时记录。实际上，硬件以其他方式快照 TSF，不能在没有驱动程序调整的情况下假设此数据是准确的。

**`IEEE80211_RADIOTAP_FLAGS`** 此字段包含单个无符号 8 位值，包含一个或多个这些位标志：

**`IEEE80211_RADIOTAP_RATE`** 此字段包含单个无符号 8 位值，即数据速率。传统速率以 500Kbps 为单位。MCS 速率（用于 802.11n/HT 信道）设置高位，MCS 在低 7 位中。

**`IEEE80211_RADIOTAP_CHANNEL`** 此字段包含两个无符号 16 位值。第一个值是帧发送/接收信道的中心频率。第二个值是包含指定信道属性的标志的位图。此字段已弃用，推荐使用 `IEEE80211_RADIOTAP_XCHANNEL`，但可用于节省传统设备捕获文件中的空间。

**`IEEE80211_RADIOTAP_DBM_ANTSIGNAL`** 此字段包含单个有符号 8 位值，指示天线处的 RF 信号功率，以与 1mW 的分贝差表示。

**`IEEE80211_RADIOTAP_DBM_ANTNOISE`** 此字段包含单个有符号 8 位值，指示天线处的 RF 噪声功率，以与 1mW 的分贝差表示。

**`IEEE80211_RADIOTAP_DBM_TX_POWER`** 以 1mW 参考的分贝表示的传输功率。此字段是单个有符号 8 位值。这是在天线端口测量的绝对功率电平。

**`IEEE80211_RADIOTAP_ANTENNA`** 此字段包含单个无符号 8 位值，指定用于传输或接收帧的天线。天线编号是设备特定的，但通常主天线的编号最低。在传输时可能看到值为零，通常意味着天线选择留给设备。

**`IEEE80211_RADIOTAP_DB_ANTSIGNAL`** 此字段包含单个无符号 8 位值，指示天线处的 RF 信号功率，以与任意固定参考的分贝差表示。

**`IEEE80211_RADIOTAP_DB_ANTNOISE`** 此字段包含单个无符号 8 位值，指示天线处的 RF 噪声功率，以与任意固定参考的分贝差表示。

**`IEEE80211_RADIOTAP_XCHANNEL`** 此字段包含四个值：描述信道属性的 32 位无符号标志位图、以 MHz 为单位的 16 位无符号频率（通常是信道中心）、8 位无符号 IEEE 信道号和以 .5 dBm 为单位保持最大监管传输功率上限的有符号 8 位值（共 8 字节）。信道标志定义于：（仅子集 found in）此属性取代 `IEEE80211_RADIOTAP_CHANNEL`，是完全表达所有信道属性和信道频率与 IEEE 信道号之间映射的唯一方式。

## 实例

Intersil Prism 驱动程序的 Radiotap 接收定义：

```c
#define WI_RX_RADIOTAP_PRESENT \
        ((1 << IEEE80211_RADIOTAP_TSFT) \
         (1 << IEEE80211_RADIOTAP_FLAGS) | \
         (1 << IEEE80211_RADIOTAP_RATE) | \
         (1 << IEEE80211_RADIOTAP_CHANNEL) | \
         (1 << IEEE80211_RADIOTAP_DB_ANTSIGNAL) | \
         (1 << IEEE80211_RADIOTAP_DB_ANTNOISE))
struct wi_rx_radiotap_header {
        struct ieee80211_radiotap_header wr_ihdr;
        uint64_t       wr_tsf;
        uint8_t        wr_flags;
        uint8_t        wr_rate;
        uint16_t       wr_chan_freq;
        uint16_t       wr_chan_flags;
        uint8_t        wr_antsignal;
        uint8_t        wr_antnoise;
} __packed __aligned(8);
```

以及 Atheros 驱动程序的传输定义：

```c
#define ATH_TX_RADIOTAP_PRESENT (               \
        (1 << IEEE80211_RADIOTAP_FLAGS)         | \
        (1 << IEEE80211_RADIOTAP_RATE)          | \
        (1 << IEEE80211_RADIOTAP_DBM_TX_POWER)  | \
        (1 << IEEE80211_RADIOTAP_ANTENNA)       | \
        (1 << IEEE80211_RADIOTAP_XCHANNEL)      | \
        0)
struct ath_tx_radiotap_header {
        struct ieee80211_radiotap_header wt_ihdr;
        uint8_t        wt_flags;
        uint8_t        wt_rate;
        uint8_t        wt_txpower;
        uint8_t        wt_antenna;
        uint32_t       wt_chan_flags;
        uint16_t       wt_chan_freq;
        uint8_t        wt_chan_ieee;
        int8_t         wt_chan_maxpow;
} __packed;
```

## 参见

[tcpdump(1)](../man1/tcpdump.1.md), [bpf(4)](../man4/bpf.4.md), [ieee80211(9)](ieee80211.9.md)

## 历史

`net80211` 定义首次出现于 NetBSD 1.5。

## 作者

本手册页的原始版本由 Bruce M. Simpson <bms@FreeBSD.org> 和 Darron Broad <darron@kewl.org> 编写。
