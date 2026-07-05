# netintro.4

`networking` — 网络设施简介

## 名称

`networking`

## 概要

`#include <sys/types.h>`

`#include <sys/time.h>`

`#include <sys/socket.h>`

`#include <net/if.h>`

`#include <net/route.h>`

## 描述

本节是对系统中可用网络设施的总体介绍。第 4 节这部分中的文档分为三个领域：*协议族*（domains）、*协议*以及*网络接口*。

所有网络协议都与特定的*协议族*相关联。协议族为协议实现提供基本服务，使其能在特定的网络环境中运作。这些服务可能包括数据包分片与重组、路由、寻址以及基本传输。一个协议族可支持多种寻址方式，尽管目前的协议实现并不支持。一个协议族通常由若干协议组成，每种 socket(2) 类型对应一个协议。并不要求协议族支持所有 socket 类型。一个协议族可包含多个支持相同 socket 抽象的协议。

协议支持 socket(2) 中详述的某种 socket 抽象。可通过创建具有适当类型和协议族的 socket 来访问特定协议，也可在创建 socket 时显式请求该协议。协议通常只接受一种地址格式，通常由协议族/网络体系结构设计中固有的寻址结构决定。基本 socket 抽象的某些语义是协议特定的。所有协议都应支持其特定 socket 类型的基本模型，但还可提供非标准设施或对机制的扩展。例如，支持 `SOCK_STREAM` 抽象的协议可能允许每条带外消息传输多于一个字节的带外数据。

网络接口类似于设备接口。网络接口构成网络子系统的最低层，与实际传输硬件交互。一个接口可支持一个或多个协议族和/或地址格式。每个网络接口条目的概要部分给出了相关驱动程序的示例规范，用于向 [config(8)](../man8/config.8.md) 程序提供系统描述。诊断部分列出了由于设备操作错误可能出现在控制台和/或系统错误日志 **`/var/log/messages`** 中的消息（参见 syslogd(8)）。

## 协议

系统目前支持 Internet 协议、Xerox Network Systems(tm) 协议以及部分 ISO OSI 协议。为 Internet 的 IP 协议层和 Xerox NS 的 IDP 协议提供了原始 socket 接口。有关每个协议族支持的更多信息，请参阅本节中相应的手册页。

## 寻址

每个协议族都关联一种地址格式。所有网络地址遵循一种通用结构，称为 sockaddr，如下所述。然而，每个协议施加了更细致、更具体的结构，通常会重命名该变体，这在前述协议族手册页中讨论。

```sh
struct sockaddr {
    u_char	sa_len;
    u_char	sa_family;
    char	sa_data[14];
};
```

字段 `sa_len` 包含结构的总长度，可能超过 16 字节。系统已知的 `sa_family` 地址值如下（还定义了供将来可能实现的其他格式）：

```sh
#define    AF_UNIX      1    /* 本机（管道、portal） */
#define    AF_INET      2    /* 互联网：UDP、TCP 等 */
#define    AF_NS        6    /* Xerox NS 协议 */
#define    AF_CCITT     10   /* CCITT 协议，X.25 等 */
#define    AF_HYLINK    15   /* NSC Hyperchannel */
#define    AF_ISO       18   /* ISO 协议 */
```

## 路由

FreeBSD 提供了一些数据包路由设施。内核维护一个路由信息数据库，用于在传输数据包时选择适当的网络接口。

用户进程（或可能多个协作的进程）通过在一种特殊类型的 socket 上发送消息来维护此数据库。这取代了早期版本中使用的固定大小 ioctl(2)。

此设施在 [route(4)](route.4.md) 中描述。

## 接口

系统中的每个网络接口对应一条可发送和接收消息的路径。网络接口通常有关联的硬件设备，但某些接口（如回环接口 [lo(4)](lo.4.md)）没有。

可使用以下 ioctl(2) 调用操作网络接口。Fn ioctl 在所需域中的 socket（通常为 `SOCK_DGRAM` 类型）上执行。早期版本中支持的大多数请求采用 `ifreq` 结构作为参数。此结构的形式如下：

```sh
struct	ifreq {
#define    IFNAMSIZ    16
    char    ifr_name[IFNAMSIZ];        /* 接口名，例如 "en0" */
    union {
        struct    sockaddr ifru_addr;
        struct    sockaddr ifru_dstaddr;
        struct    sockaddr ifru_broadaddr;
        struct    ifreq_buffer ifru_buffer;
        short     ifru_flags[2];
        short     ifru_index;
        int       ifru_metric;
        int       ifru_mtu;
        int       ifru_phys;
        int       ifru_media;
        caddr_t   ifru_data;
        int       ifru_cap[2];
    } ifr_ifru;
#define ifr_addr      ifr_ifru.ifru_addr      /* 地址 */
#define ifr_dstaddr   ifr_ifru.ifru_dstaddr   /* 点对点链路的另一端 */
#define ifr_broadaddr ifr_ifru.ifru_broadaddr /* 广播地址 */
#define ifr_buffer    ifr_ifru.ifru_buffer    /* 用户提供的缓冲区及其长度 */
#define ifr_flags     ifr_ifru.ifru_flags[0]  /* 标志（低 16 位） */
#define ifr_flagshigh ifr_ifru.ifru_flags[1]  /* 标志（高 16 位） */
#define ifr_metric    ifr_ifru.ifru_metric    /* 度量值 */
#define ifr_mtu       ifr_ifru.ifru_mtu       /* MTU */
#define ifr_phys      ifr_ifru.ifru_phys      /* 物理线路 */
#define ifr_media     ifr_ifru.ifru_media     /* 物理媒体 */
#define ifr_data      ifr_ifru.ifru_data      /* 供接口使用 */
#define ifr_reqcap    ifr_ifru.ifru_cap[0]    /* 请求的能力 */
#define ifr_curcap    ifr_ifru.ifru_cap[1]    /* 当前能力 */
#define ifr_index     ifr_ifru.ifru_index     /* 接口索引 */
};
```

获取地址的 Fn Ioctl 请求以及设置和获取其他数据的请求仍然得到完全支持，并使用 `ifreq` 结构：

**`SIOCGIFADDR`** 获取协议族的接口地址。

**`SIOCGIFDSTADDR`** 获取协议族和接口的点对点地址。

**`SIOCGIFBRDADDR`** 获取协议族和接口的广播地址。

**`SIOCSIFCAP`** 尝试将接口的启用能力字段设置为 `ifreq` 结构的 `ifr_reqcap` 字段值。注意，根据特定接口特性，某些能力可能看起来硬编码为启用，或切换一个能力会影响其他能力的状态。支持的能力字段为只读，`ifr_curcap` 字段在此调用中未使用。

**`SIOCGIFCAP`** 获取接口能力字段。支持的能力和已启用的能力值将分别返回到 `ifreq` 结构的 `ifr_reqcap` 和 `ifr_curcap` 字段中。

**`SIOCGIFDESCR`** 获取接口描述，通过 `ifru_buffer` 结构的 `buffer` 字段返回。在作为参数传入的 `ifru_buffer` 结构的 `length` 字段中应定义用户提供的缓冲区长度，且该长度应包括结尾的 nul 字符。如果没有足够的空间容纳接口描述长度，则不会进行复制，`ifru_buffer` 的 `buffer` 字段将设置为 NULL。无论缓冲区本身是否足以容纳数据，内核都会在返回时将缓冲区长度存储在 `length` 字段中。

**`SIOCSIFDESCR`** 将接口描述设置为 `ifru_buffer` 结构 `buffer` 字段的值，`length` 字段指定其长度（包括结尾的 nul）。

**`SIOCSIFFLAGS`** 设置接口标志字段。如果接口被标记为 down，会通知当前通过该接口路由数据包的所有进程；某些接口可能被重置，以便不再接收传入数据包。再次标记为 up 时，接口将被重新初始化。

**`SIOCGIFFLAGS`** 获取接口标志。

**`SIOCSIFMETRIC`** 设置接口路由度量值。该度量值仅由用户级路由器使用。

**`SIOCGIFMETRIC`** 获取接口度量值。

**`SIOCIFCREATE`** 尝试创建指定的接口。如果接口名不带单元号给出，系统将尝试以任意单元号创建新接口。成功返回时，`ifr_name` 字段将包含新接口名。

**`SIOCIFDESTROY`** 尝试销毁指定的接口。

有两个请求使用了新的结构：

**`SIOCAIFADDR`** 在某些协议中，一个接口可关联多个地址。此请求提供了添加额外地址（或在指定地址族的默认地址时修改主地址特性）的方法。不必分别调用设置目的地址或广播地址或网络掩码（现在是多种协议的必备特性），而是使用单独的结构同时指定这三个方面（见下文）。可以使用针对每个族稍作定制的此结构版本（将每个 sockaddr 替换为族特定类型之一）。当 sockaddr 本身大于默认大小时，需要修改 Fn ioctl 标识符本身以包含总大小，如 Fn ioctl 中所述。

**`SIOCDIFADDR`** 此请求从与接口关联的列表中删除指定地址。它也使用 `ifaliasreq` 结构，以允许协议支持多个掩码或目的地址，并采用这样的约定：指定默认地址意味着删除原始 socket 打开时所属地址族中该接口的第一个地址。

**`SIOCGIFALIAS`** 此请求提供了从接口获取附加地址以及网络掩码和广播/目的地址的方法。它也使用 `ifaliasreq` 结构。

**`SIOCGIFCONF`** 获取接口配置列表。此请求采用 `ifconf` 结构（见下文）作为值-结果参数。`ifc_len` 字段最初应设置为 `ifc_buf` 所指向缓冲区的大小。返回时它将包含配置列表的字节长度。

**`SIOCIFGCLONERS`** 获取可克隆接口列表。此请求采用 `if_clonereq` 结构（见下文）作为值-结果参数。`ifcr_count` 字段应设置为 `ifcr_buffer` 所指向缓冲区能容纳的 `IFNAMSIZ` 大小字符串数量。返回时，`ifcr_total` 将设置为可克隆接口的总数，`ifcr_buffer` 所指向的缓冲区将填充以 `IFNAMSIZ` 边界对齐的可克隆接口名称。

```sh
/*
* SIOCAIFADDR 请求中使用的结构。
*/
struct ifaliasreq {
        char    ifra_name[IFNAMSIZ];   /* 接口名，例如 "en0" */
        struct  sockaddr        ifra_addr;
        struct  sockaddr        ifra_broadaddr;
        struct  sockaddr        ifra_mask;
};
```

```sh
/*
* SIOCGIFCONF 请求中使用的结构。
* 用于检索机器的接口配置
* （对于必须知道所有可访问网络的程序
* 很有用）。
*/
struct ifconf {
    int   ifc_len;		/* 关联缓冲区的大小 */
    union {
        caddr_t    ifcu_buf;
        struct     ifreq *ifcu_req;
    } ifc_ifcu;
#define ifc_buf ifc_ifcu.ifcu_buf /* 缓冲区地址 */
#define ifc_req ifc_ifcu.ifcu_req /* 返回的结构数组 */
};
```

```sh
/* SIOCIFGCLONERS 请求中使用的结构。 */
struct if_clonereq {
        int     ifcr_total;     /* 总克隆器（输出） */
        int     ifcr_count;     /* 用户缓冲区中可容纳的数量 */
        char    *ifcr_buffer;   /* 克隆器名称缓冲区 */
};
```

```sh
/* SIOCGIFDESCR 和 SIOCSIFDESCR 请求中使用的结构 */
struct ifreq_buffer {
        size_t  length;         /* 缓冲区长度 */
        void   *buffer;         /* 指向用户空间缓冲区的指针 */
};
```

## 参见

ioctl(2), socket(2), [intro(4)](intro.4.md), [config(8)](../man8/config.8.md), [routed(8)](../man8/routed.8.md), [ifnet(9)](../man9/ifnet.9.md)

## 历史

`netintro` 手册页首次出现于 4.3BSD。
