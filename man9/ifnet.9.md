# ifnet.9

`if_t` — 用于操作网络接口的内核接口

## 名称

`if_t`, `ifnet`, `ifaddr`, `ifqueue`, `if_data`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/time.h>
```

```c
#include <sys/socket.h>
```

```c
#include <net/if.h>
```

```c
#include <net/if_var.h>
```

```c
#include <net/if_types.h>
```

### 接口操作函数

```c
if_t
if_alloc(u_char type)

if_t
if_alloc_dev(u_char type, device_t dev)

if_t
if_alloc_domain(u_char type, int numa_domain)

void
if_attach(if_t ifp)

void
if_detach(if_t ifp)

void
if_free(if_t ifp)

void
if_free_type(if_t ifp, u_char type)

void
if_down(if_t ifp)

int
ifioctl(struct socket *so, u_long cmd, caddr_t data, struct thread *td)

int
ifpromisc(if_t ifp, int pswitch)

int
if_allmulti(if_t ifp, int amswitch)

if_t
ifunit(const char *name)

if_t
ifunit_ref(const char *name)

void
if_up(if_t ifp)
```

### 接口地址函数

```c
struct ifaddr *
ifa_ifwithaddr(struct sockaddr *addr)

struct ifaddr *
ifa_ifwithdstaddr(struct sockaddr *addr, int fib)

struct ifaddr *
ifa_ifwithnet(struct sockaddr *addr, int ignore_ptp, int fib)

struct ifaddr *
ifaof_ifpforaddr(struct sockaddr *addr, if_t ifp)

void
ifa_ref(struct ifaddr *ifa)

void
ifa_free(struct ifaddr *ifa)
```

### 接口多播地址函数

```c
int
if_addmulti(if_t ifp, struct sockaddr *sa, struct ifmultiaddr **ifmap)

int
if_delmulti(if_t ifp, struct sockaddr *sa)

struct ifmultiaddr *
if_findmulti(if_t ifp, struct sockaddr *sa)
```

### 输出队列访问器

```c
if_dequeue(if_t ifp, struct mbuf *m)
```

### 输出队列宏

```c
IF_DEQUEUE(struct ifqueue *ifq, struct mbuf *m)
```

### if_t 访问器

```c
uint64_t
if_setbaudrate(if_t ifp, uint64_t baudrate)

uint64_t
if_getbaudrate(const if_t ifp)

int
if_setcapabilities(if_t ifp, int capabilities)

int
if_setcapabilitiesbit(if_t ifp, int setbit, int clearbit)

int
if_getcapabilities(const if_t ifp)

int
if_togglecapenable(if_t ifp, int togglecap)

int
if_setcapenable(if_t ifp, int capenable)

int
if_setcapenablebit(if_t ifp, int setcap, int clearcap)

int
if_getcapenable(const if_t ifp)

int
if_setcapabilities2(if_t ifp, int capabilities)

int
if_setcapabilities2bit(if_t ifp, int setbit, int clearbit)

int
if_getcapabilities2(const if_t ifp)

int
if_togglecapenable2(if_t ifp, int togglecap)

int
if_setcapenable2(if_t ifp, int capenable)

int
if_setcapenable2bit(if_t ifp, int setcap, int clearcap)

int
if_getcapenable2(const if_t ifp)

int
if_getdunit(const if_t ifp)

int
if_getindex(const if_t ifp)

int
if_getidxgen(const if_t ifp)

const char *
if_getdname(const if_t ifp)

void
if_setdname(if_t ifp, const char *name)

const char *
if_name(if_t ifp)

int
if_setname(if_t ifp, const char *name)

void
if_setdescr(if_t ifp, char *descrbuf)

char *
if_allocdescr(size_t sz, int malloc_flag)

void
if_freedescr(char *descrbuf)

int
if_getalloctype(const if_t ifp)

int
if_gettype(const if_t ifp)

int
if_setdev(if_t ifp, void *dev)

int
if_setdrvflagbits(if_t ifp, int if_setflags, int clear_flags)

int
if_getdrvflags(const if_t ifp)

int
if_setdrvflags(if_t ifp, int flags)

int
if_getlinkstate(if_t ifp)

int
if_clearhwassist(if_t ifp)

int
if_sethwassistbits(if_t ifp, int toset, int toclear)

int
if_sethwassist(if_t ifp, int hwassist_bit)

int
if_gethwassist(const if_t ifp)

int
if_togglehwassist(if_t ifp, int toggle_bits)

int
if_setsoftc(if_t ifp, void *softc)

void *
if_getsoftc(if_t ifp)

void
if_setllsoftc(if_t ifp, void *softc)

void *
if_getllsoftc(if_t ifp)

u_int
if_getfib(if_t ifp)

uint8_t
if_getaddrlen(if_t ifp)

int
if_gethwaddr(const if_t ifp, struct ifreq *)

const uint8_t *
if_getbroadcastaddr(const if_t ifp)

void
if_setbroadcastaddr(if_t ifp, const uint8_t *)

int
if_setmtu(if_t ifp, int mtu)

int
if_getmtu(const if_t ifp)

int
if_getmtu_family(const if_t ifp, int family)

void
if_notifymtu(if_t ifp)

int
if_setflagbits(if_t ifp, int set, int clear)

int
if_setflags(if_t ifp, int flags)

int
if_getflags(const if_t ifp)

int
if_getnumadomain(if_t ifp)

int
if_sendq_empty(if_t ifp)

int
if_setsendqready(if_t ifp)

int
if_setsendqlen(if_t ifp, int tx_desc_count)

int
if_sethwtsomax(if_t ifp, u_int if_hw_tsomax)

int
if_sethwtsomaxsegcount(if_t ifp, u_int if_hw_tsomaxsegcount)

int
if_sethwtsomaxsegsize(if_t ifp, u_int if_hw_tsomaxsegsize)

u_int
if_gethwtsomax(const if_t ifp)

u_int
if_gethwtsomaxsegcount(const if_t ifp)

u_int
if_gethwtsomaxsegsize(const if_t ifp)

void
if_setnetmapadapter(if_t ifp, struct netmap_adapter *na)

struct netmap_adapter *
if_getnetmapadapter(if_t ifp)

void
if_input(if_t ifp, struct mbuf *sendmp)

int
if_sendq_prepend(if_t ifp, struct mbuf *m)

struct mbuf *
if_dequeue(if_t ifp)

int
if_setifheaderlen(if_t ifp, int len)

void
if_setrcvif(struct mbuf *m, if_t ifp)

void
if_setvtag(struct mbuf *m, u_int16_t tag)

u_int16_t
if_getvtag(struct mbuf *m)

int
if_vlantrunkinuse(if_t ifp)

caddr_t
if_getlladdr(const if_t ifp)

struct vnet *
if_getvnet(const if_t ifp)

void *
if_gethandle(u_char)

void
if_bpfmtap(if_t ifp, struct mbuf *m)

void
if_etherbpfmtap(if_t ifp, struct mbuf *m)

void
if_vlancap(if_t ifp)

int
if_transmit(if_t ifp, struct mbuf *m)

void
if_init(if_t ifp, void *ctx)

int
if_resolvemulti(if_t ifp, struct sockaddr **, struct sockaddr *)

uint64_t
if_getcounter(if_t ifp, ift_counter counter)

struct label *
if_getmaclabel(if_t ifp)

void
if_setmaclabel(if_t ifp, struct label *label)

struct bpf_if *
if_getbpf(if_t ifp)

uint8_t
if_getpcp(if_t ifp)

void *
if_getl2com(if_t ifp)

struct ifvlantrunk *
if_getvlantrunk(if_t ifp)

bool
if_altq_is_enabled(if_t ifp)
```

### struct ifnet 成员函数

```c
void
(*if_input)(if_t ifp, struct mbuf *m)

int
(*if_output)(if_t ifp, struct mbuf *m, const struct sockaddr *dst,
    struct route *ro)

void
(*if_start)(if_t ifp)

int
(*if_transmit)(if_t ifp, struct mbuf *m)

void
(*if_qflush)(if_t ifp)

int
(*if_ioctl)(if_t ifp, u_long cmd, caddr_t data)

void
(*if_init)(void *if_softc)

int
(*if_resolvemulti)(if_t ifp, struct sockaddr **retsa,
    struct sockaddr *addr)
```

### struct ifaddr 成员函数

```c
void
(*ifa_rtrequest)(int cmd, struct rtentry *rt, struct rt_addrinfo *info)
```

### 全局变量

```c
extern struct ifnethead ifnet;
extern int if_index;
extern int ifqmaxlen;
```

## 数据结构

处理网络接口的内核机制主要存在于 `ifnet`、`if_data`、`ifaddr` 和 `ifmultiaddr` 结构中，定义于

```c
#include <net/if.h>
```

和

```c
#include <net/if_var.h>
```

以及上述命名并定义在 **/sys/net/if.c** 中的函数。打算由用户程序使用的那些接口定义于

```c
#include <net/if.h>
```

这些包括接口标志、`if_data` 结构，以及定义 [route(4)](../man4/route.4.md) 路由套接字和 sysctl(3) 中接口相关消息外观的结构。头文件

```c
#include <net/if_var.h>
```

定义了内核内部接口，包括 `ifnet`、`ifaddr` 和 `ifmultiaddr` 结构以及操作它们的函数。（少数用户程序需要

```c
#include <net/if_var.h>
```

因为它是某些其他头文件如

```c
#include <netinet/if_ether.h>
```

的先决条件。对这两个文件的大多数引用可以通过

```c
#include <net/ethernet.h>
```

替换。系统使用 [queue(3)](../man3/queue.3.md) 中定义的 `TAILQ` 宏维护接口链表；此列表由名为 `ifnet` 的 `struct ifnethead` 头部组成。此列表的元素类型为 `struct ifnet`，大多数按此操作接口的内核例程接受或返回指向这些结构的指针。每个接口结构包含一个用于统计和信息的 `if_data` 结构。每个接口还有一个由 `ifaddr` 结构描述的接口地址 `TAILQ`。描述接口实现的链路层（如果有）的 `AF_LINK` 地址（见 link_addr(3)）通过 `if_addr` 结构访问。（一些简单接口不提供任何链路层地址；此结构虽然仍然存在，但仅用于标识接口名称和索引。）

最后，那些支持接收多播数据报的接口有一个由 `ifmultiaddr` 结构描述的多播组成员资格 `TAILQ`。这些成员资格采用引用计数。

接口还与定义为 `struct ifqueue` 的输出队列关联；此结构用于在接口正在发送另一个数据包时保存数据包。

### ifnet 访问器

`if_t` 的访问器如下：

**Fn** `if_getbaudrate` `if_setbaudrate` (`u_long`) 接口的线路速率，以每秒位数为单位。

**Fn** `if_setcapabilities` `if_setcapabilitiesbit` `if_getcapabilities` (`int`) 描述接口支持的能力的标志（见下文）。

**Fn** `if_getcapenable` `if_setcapenable` `if_setcapenablebit` `if_togglecapenable` (`int`) 描述接口已启用能力的标志（见下文）。

**Fn** `if_getcapabilities2` `if_setcapabilities2` `if_setcapabilities2bit`

**Fn** `if_getcapenable2` `if_setcapenable2` `if_setcapenable2bit` `if_togglecapenable2`

**Fn** `if_getdunit` (`int`) 分配给由特定驱动程序管理的每个接口的唯一编号。如果设备未关联单元号，驱动程序可以选择将其设置为 `IF_DUNIT_NONE`。（由驱动程序初始化，通常通过 `if_initname`。）

**Fn** `if_getindex` (`u_short`) 返回附加设备时分配的唯一编号。此编号可用于 `struct sockaddr_dl` 中按索引引用特定接口（见 link_addr(3)）。这由 `if_alloc` 初始化。

**Fn** `if_getidxgen`

**Fn** `if_getdname` `if_setdname` (`const char *`) 驱动程序的名称。这由驱动程序初始化（通常通过 `if_initname`）。

**Fn** `if_name` `if_setname` (`char *`) 接口的名称（例如 `fxp0` 或“`lo0`”）。这由驱动程序初始化，通常通过 `if_initname`。

**Fn** `if_getalloctype` (`u_char`) 接口在分配时的类型。它用于缓存传递给 `if_alloc` 的类型，但与 `if_type` 不同，驱动程序不会更改它。

**Fn** `if_gettype`

**Fn** `if_setdev`

**Fn** `if_getdrvflags` `if_setdrvflags` `if_setdrvflagbits`

**Fn** `if_getlinkstate`

**Fn** `if_clearhwassist` `if_sethwassistbits` `if_gethwassist` `if_sethwassist` `if_togglehwassist` (`u_long`) 对*出站*数据包卸载计算任务的能力的详细解释。接口驱动程序必须使此字段与 `if_capenable` 的当前值保持一致。

**Fn** `if_getsoftc` `if_setsoftc` (`void *`) 指向驱动程序私有状态块的指针。这由驱动程序在附加时初始化。

**Fn** `if_setllsoftc`

**Fn** `if_getllsoftc`

**Fn** `if_getfib`

**Fn** `if_getaddrlen`

**Fn** `if_gethwaddr`

**Fn** `if_getbroadcastaddr` `if_setbroadcastaddr` 访问接口广播地址。

**Fn** `if_setmtu`

**Fn** `if_getmtu` 访问接口 MTU。

**Fn** `if_setflags` `if_getflags` `if_setflagbits` (`int`) 描述此接口操作参数的标志（见下文）。这些标志由通用代码操作。

**Fn** `if_getnumadomain` (`uint8_t`) 与接口关联的硬件设备的 NUMA 域。除非内核支持 NUMA、系统是 NUMA 系统且 ifnet 使用 `if_alloc_dev` 或 `if_alloc_domain` 分配，否则用通配符值填充。

**Fn** `if_sendq_empty`

**Fn** `if_setsendqready`

**Fn** `if_setsendqlen`

**Fn** `if_sethwtsomax` `if_gethwtsomax`

**Fn** `if_sethwtsomaxsegcount` `if_gethwtsomaxsegcount`

**Fn** `if_sethwtsomaxsegsize` `if_gethwtsomaxsegsize`

**Fn** `if_setnetmapadapter` `if_getnetmapadapter`

**Fn** `if_setifheaderlen`

**Fn** `if_setrcvif`

**Fn** `if_setvtag` `if_getvtag`

**Fn** `if_vlantrunkinuse`

**Fn** `if_getlladdr`

**Fn** `if_getvnet` (`struct vnet *`) 指向虚拟网络栈实例的指针。这由 `if_attach` 初始化。

**Fn** `if_gethandle`

**Fn** `if_vlancap`

**Fn** `if_getcounter`

**Fn** `if_getmaclabel` `if_setmaclabel`

**Fn** `if_getbpf` (`struct bpf_if *`) 数据包过滤器 [bpf(4)](../man4/bpf.4.md) 的每接口不透明数据。这由 `bpf_attach` 初始化。

**Fn** `if_getpcp`

**Fn** `if_getl2com` 指向接口层 2 协议的公共数据的指针。这由 `if_alloc` 初始化。`if_getvlantrunk` `if_t ifp` (`struct ifvlantrunk *`) 指向 802.1Q 中继结构的指针，[vlan(4)](../man4/vlan.4.md)。这由驱动程序特定的 `if_ioctl` 例程初始化。

**Fn** `if_getdrvflags` `if_setdrvflags` `if_setdrvflagbits` (`int`) 描述此接口操作状态的标志（见下文）。这些标志由驱动程序操作。

**Fn** `if_addmulti` `if_delmulti` `if_findmulti` 添加、删除和查找分配给此接口的多播地址。

**Fn** `if_getifaddr` (`struct ifaddr *`) 获取指向接口链路层地址的指针。

**Fn** `if_getbroadcastaddr` `if_setbroadcastaddr` (`const u_int8_t *`) 用于具有可变地址长度的协议的链路层广播字节串。

**Fn** `if_getafdata` (`void *`) 地址族相关数据区域。

**Fn** `if_addgroup` `if_delgroup` 在接口中添加和删除组。

对 `ifnet` 结构的引用通过调用 `if_ref` 函数获得，通过调用 `if_rele` 函数释放。它们用于允许遍历全局接口列表的内核代码释放 `ifnet` 锁但保持 `ifnet` 结构稳定。

此外还有许多函数指针，驱动程序必须初始化它们以完成与通用接口层的接口：

```c
#include <sys/sockio.h>
```

**Fn** `if_input` 根据数据包的链路层头将数据包传递给适当的上层。此例程从中断处理程序调用或用于模拟在此接口上接收数据包。实现 `if_input` 的单个函数可在使用相同链路层成帧（例如以太网）的多个驱动程序之间共享。

**Fn** `if_output` 在接口 `ifp` 上输出数据包，或者如果接口已活动则将其排队到输出队列。

**Fn** `if_transmit` 在接口上传输数据包，或者如果接口正在使用则将其排队。如果设备的软件和硬件队列都满，此函数将返回 `ENOBUFS`。此函数必须在 `if_attach` 之后安装以覆盖默认实现。公开此函数是为了允许驱动程序管理自己的队列并减少由频繁无谓的入队/出队对到 ifq 引起的延迟。建议的内部软件排队机制是 buf_ring。

**Fn** `if_qflush` 当接口标记为关闭时释放在内部管理的队列中的 mbuf。此函数必须在 `if_attach` 之后安装以覆盖默认实现。公开此函数是为了允许驱动程序管理自己的队列并减少由频繁无谓的入队/出队对到 ifq 引起的延迟。建议的内部软件排队机制是 buf_ring。

**Fn** `if_start` 在接口上启动排队输出。公开此函数是为了使某些接口类在所有驱动程序之间共享 `if_output`。仅在未设置 `IFF_DRV_OACTIVE` 标志时可调用 `if_start`。（因此，`IFF_DRV_OACTIVE` 字面意思不是输出活动，而是设备的内部输出队列已满。）请注意此函数很快将被弃用。

**Fn** `if_ioctl` 处理与接口相关的 ioctl(2) 请求（定义于 初步处理由通用例程 `ifioctl` 完成，以检查适当的特权、定位正在操作的接口并执行某些通用操作如翻转标志和刷新队列。有关更多信息，请参阅下面 `ifioctl` 的描述。

**Fn** `if_init` 初始化并启动硬件，例如重置芯片并启用接收器单元。应将接口标记为运行但非活动（`IFF_DRV_RUNNING`，`~IIF_DRV_OACTIVE`）。

**Fn** `if_resolvemulti` 检查请求的多播组成员资格 `addr` 的有效性，如有必要计算对应于该地址的链路层组，并在 `*retsa` 中返回。成功返回零，失败返回错误代码。

### 接口标志

接口标志用于许多不同目的。一些标志仅指示有关接口类型及其能力的信息；其他标志被动态操作以反映接口的当前状态。前一种标志在此表中标记为 <S>；后者标记为 <D>。以“IFF_DRV_”开头的标志存储在 `if_drv_flags` 中；所有其他标志存储在 `if_flags` 中。

宏 `IFF_CANTCHANGE` 定义了用户程序无法使用 `SIOCSIFFLAGS` 命令对 ioctl(2) 设置的位；这些在以下列表中用星号（`*`）表示。

**`IFF_UP`** <D> 接口已由用户级代码配置为启用。
**`IFF_BROADCAST`** <S*> 接口支持广播。
**`IFF_DEBUG`** <D> 用于启用/禁用驱动程序调试代码。
**`IFF_LOOPBACK`** <S> 接口是回环设备。
**`IFF_POINTOPOINT`** <S*> 接口是点对点的；“广播”地址实际上是另一端的地址。
**`IFF_DRV_RUNNING`** <D*> 接口已配置并成功分配了动态资源。可能仅对接口内部有用。
**`IFF_NOARP`** <D> 在此接口上禁用网络地址解析。
**`IFF_PROMISC`** <D*> 此接口处于混杂模式。
**`IFF_PPROMISC`** <D> 此接口处于永久混杂模式（隐含 `IFF_PROMISC`）。
**`IFF_ALLMULTI`** <D*> 此接口处于全多播模式（由多播路由器使用）。
**`IFF_PALLMULTI`** <D> 此接口处于永久全多播模式（隐含 `IFF_ALLMULTI`）。
**`IFF_DRV_OACTIVE`** <D*> 接口的硬件输出队列（如果有）已满；输出数据包将被排队。
**`IFF_SIMPLEX`** <S*> 接口无法听到自己的传输。
**`IFF_LINK0`**
**`IFF_LINK1`**
**`IFF_LINK2`** <D> 链路层的控制标志。（目前被滥用于在某些设备上的多个物理层之间进行选择。）
**`IFF_MULTICAST`** <S*> 此接口支持多播。
**`IFF_CANTCONFIG`** <S*> 接口无法以有意义的方式配置。主要用于在接口列表中注册的 `IFT_USB` 接口。
**`IFF_MONITOR`** <D> 此接口阻止数据包传输并在 BPF 处理后丢弃传入数据包。用于监控网络流量但不与相关网络交互。
**`IFF_STATICARP`** <D> 用于启用/禁用此接口上的 ARP 请求。
**`IFF_DYING`** <D*> 当此接口的 `ifnet` 结构正在释放且仍有 `if_refcount` 引用时设置。

### 接口能力标志

接口能力是接口可能支持也可能不支持的专用功能。这些能力非常特定于硬件，启用时允许将特定网络处理卸载到接口或提供特定功能供其他内核部分使用。

应强调的是，能力可以完全不受控制（即始终启用且无法禁用）或允许对其自身的有限控制（例如依赖于另一能力的状态）。此类特性完全由特定接口的硬件和驱动程序决定。只有驱动程序拥有关于是否以及如何控制接口能力的知识。因此，`if_capenable` 中的能力标志永远不应由接口驱动程序以外的内核代码直接修改。对 `ifioctl` 的 `SIOCSIFCAP` 命令是尝试更改接口上 `if_capenable` 的专用手段。用户态代码应使用 ioctl(2)。

系统当前支持以下能力：

**`IFCAP_RXCSUM`** 此接口可以在接收数据时执行校验和验证。某些接口没有足够的缓冲区存储来完整存储超过某个 MTU 大小的帧。如果 MTU 设置高于硬编码限制，接口的驱动程序可能会禁用硬件校验和验证。

**`IFCAP_TXCSUM`** 此接口可以在传输数据时执行校验和计算。

**`IFCAP_HWCSUM`** (`IFCAP_RXCSUM | IFCAP_TXCSUM`) 的简写。

**`IFCAP_NETCONS`** 此接口可作为网络控制台。

**`IFCAP_VLAN_MTU`** [vlan(4)](../man4/vlan.4.md) 驱动程序可以在软件标记模式下在此接口上操作，而无需将 [vlan(4)](../man4/vlan.4.md) 接口上的 MTU 降低到 1500 字节以下。这意味着此接口能够处理比以太网规范允许的稍长的帧。

**`IFCAP_VLAN_HWTAGGING`** 此接口可以在输出时进行 VLAN 标记，并在输入时按其 VLAN 标记对帧进行多路分解。

**`IFCAP_JUMBO_MTU`** 此以太网接口可以传输和接收长达 9000 字节的帧。

**`IFCAP_POLLING`** 此接口支持 [polling(4)](../man4/polling.4.md)。详见下文。

**`IFCAP_VLAN_HWCSUM`** 此接口可以在 [vlan(4)](../man4/vlan.4.md) 接口上对传输和接收数据进行校验和计算（隐含 `IFCAP_HWCSUM`）。

**`IFCAP_TSO4`** 此以太网接口支持 TCP4 分段卸载。

**`IFCAP_TSO6`** 此以太网接口支持 TCP6 分段卸载。

**`IFCAP_TSO`** (`IFCAP_TSO4 | IFCAP_TSO6`) 的简写。

**`IFCAP_TOE4`** 此以太网接口支持 TCP4 卸载引擎。

**`IFCAP_TOE6`** 此以太网接口支持 TCP6 卸载引擎。

**`IFCAP_TOE`** (`IFCAP_TOE4 | IFCAP_TOE6`) 的简写。

**`IFCAP_WOL_UCAST`** 此以太网接口支持在任何单播数据包上唤醒。

**`IFCAP_WOL_MCAST`** 此以太网接口支持在任何多播数据包上唤醒。

**`IFCAP_WOL_MAGIC`** 此以太网接口支持在任何魔术数据包（如 wake(8) 发送的那些）上唤醒。

**`IFCAP_WOL`** (`IFCAP_WOL_UCAST | IFCAP_WOL_MCAST | IFCAP_WOL_MAGIC`) 的简写。

**`IFCAP_VLAN_HWFILTER`** 此接口支持在 [vlan(4)](../man4/vlan.4.md) 接口上进行硬件帧过滤。

**`IFCAP_VLAN_HWTSO`** 此接口支持在 [vlan(4)](../man4/vlan.4.md) 接口上进行 TCP 分段卸载（隐含 `IFCAP_TSO`）。

**`IFCAP_LINKSTATE`** 此以太网接口支持动态链路状态更改。

**`IFCAP_NETMAP`** 此以太网接口支持 [netmap(4)](../man4/netmap.4.md)。

高级网络接口将某些计算任务从主机 CPU 卸载到板上的能力主要限于 TCP/IP。因此，与接口关联的单独字段（见下文 `ifnet.if_data.ifi_hwassist`）保留了其特定于 TCP/IP 处理的已启用能力的详细描述。TCP/IP 模块查询此字段以查看接口可以在*出站*数据包上执行哪些任务。为该字段定义的标志是 `mbuf.m_pkthdr.csum_flags` 标志的超集，即：

**`CSUM_IP`** 接口将计算 IP 校验和。

**`CSUM_TCP`** 接口将计算 TCP 校验和。

**`CSUM_UDP`** 接口将计算 UDP 校验和。

接口通过在包含数据包的 `mbuf 链` 的 `mbuf.m_pkthdr.csum_flags` 字段中设置相应标志，通知 TCP/IP 模块前者对*入站*数据包执行的任务。详见 [mbuf(9)](mbuf.9.md)。

网络接口在 [polling(4)](../man4/polling.4.md) 模式下操作的能力涉及不同全局变量和每接口字段中的几个标志。接口 `if_capabilities` 中设置的能力标志 `IFCAP_POLLING` 表示特定接口支持 [polling(4)](../man4/polling.4.md)。如果在 `if_capabilities` 中设置，同一标志可以在 `ifioctl` 中在接口的 `if_capenable` 中标记或清除，从而分别启动将接口切换到 [polling(4)](../man4/polling.4.md) 模式或中断模式。实际模式更改由驱动程序特定的 `if_ioctl` 例程管理。[polling(4)](../man4/polling.4.md) 处理程序返回处理的数据包数。

### if_data 结构

`if_data` 结构包含管理程序使用的统计信息和识别信息，并通过 sysctl(3) MIB 的 [ifmib(4)](../man4/ifmib.4.md) 分支导出到用户程序。`if_data` 结构的以下元素由接口初始化，在正常操作过程中不应显著变化：

```c
#include <net/if_types.h>
```

**`ifi_type`** (`u_char`) 接口的类型，定义于并在下面的 Sx 接口类型 节中描述。

**`ifi_physical`** (`u_char`) 旨在表示支持多个物理层的设备上的物理层选择；从未实现。

**`ifi_addrlen`** (`u_char`) 此设备上链路层地址的长度，如果没有则为零。用于初始化引用此接口的 `sockaddr_dl` 结构中的地址长度字段。

**`ifi_hdrlen`** (`u_char`) 驱动程序在传输前可能添加到数据包的任何链路层头的最大长度。通用代码计算所有接口的最大值，并使用该值影响数据在 `mbuf` 中的放置，以尝试确保始终有足够的空间添加链路层头而无需分配额外的 `mbuf`。

**`ifi_datalen`** (`u_char`) `if_data` 结构的长度。在 `struct ifdata` 长度增加的情况下允许路由套接字 ABI 的某些稳定化。

**`ifi_mtu`** (`u_long`) 介质的最大传输单元，不包括任何链路层开销。

**`ifi_metric`** (`u_long`) 由用户模式路由进程解释的无量纲度量。

**`ifi_epoch`** (`time_t`) 接口附加或以下统计信息重置时的系统正常运行时间。这旨在用于设置 SNMP 变量 `ifCounterDiscontinuityTime`。它也可用于确定对同一索引接口的两次连续查询是否返回了同一接口的结果。

该结构还包含适用于各种不同接口类型的通用统计信息（除注明外，所有成员类型为 `u_long`）：

**`ifi_link_state`** (`u_char`) 以太网接口的当前链路状态。可能值见 Sx 接口链路状态 节。

**`ifi_ipackets`** 接收的数据包数。

**`ifi_ierrors`** 检测到的接收错误数（例如 FCS 错误、DMA 溢出等）。通常可以通过链路特定 MIB 获得更详细的分解。

**`ifi_opackets`** 传输的数据包数。

**`ifi_oerrors`** 检测到的输出错误数（例如迟冲突、DMA 溢出等）。通常可以通过链路特定 MIB 获得更详细的分解。

**`ifi_collisions`** CSMA 接口输出检测到的冲突总数。（此成员有时被其他类型的接口[滥用]用于其他输出错误计数。）

**`ifi_ibytes`** 接收的总流量，以字节为单位。

**`ifi_obytes`** 传输的总流量，以字节为单位。

**`ifi_imcasts`** 通过链路层多播发送的接收数据包数。

**`ifi_omcasts`** 通过链路层多播发送的数据包数。

**`ifi_iqdrops`** 输入上丢弃的数据包数。很少实现。

**`ifi_oqdrops`** 输出上丢弃的数据包数。

**`ifi_noproto`** 未知网络层协议的接收数据包数。

**`ifi_lastchange`** (`struct timeval`) 接口上次管理更改的时间（SNMP 所需）。

### 接口类型

头文件

```c
#include <net/if_types.h>
```

为许多不同类型的接口定义符号常量。最常见的是：

**`IFT_OTHER`** 以下都不是
**`IFT_ETHER`** 以太网
**`IFT_ISO88023`** ISO 8802-3 CSMA/CD
**`IFT_ISO88024`** ISO 8802-4 令牌总线
**`IFT_ISO88025`** ISO 8802-5 令牌环
**`IFT_ISO88026`** ISO 8802-6 DQDB MAN
**`IFT_FDDI`** FDDI
**`IFT_PPP`** Internet 点对点协议（ppp(8)）
**`IFT_LOOP`** 回环（[lo(4)](../man4/lo.4.md)）接口
**`IFT_SLIP`** 串行线 IP
**`IFT_PARA`** 并口 IP（“PLIP”）
**`IFT_ATM`** 异步传输模式
**`IFT_USB`** USB 接口

### 接口链路状态

当前定义了以下链路状态：

**`LINK_STATE_UNKNOWN`** 链路处于无效或未知状态。
**`LINK_STATE_DOWN`** 链路已断。
**`LINK_STATE_UP`** 链路已通。

### ifaddr 结构

每个接口都与一个地址列表（或者更确切地说是 `TAILQ`）关联，根植于接口结构的 `if_addrhead` 成员。此列表中的第一个元素始终是表示接口本身的 `AF_LINK` 地址；多访问网络驱动程序应在调用 `if_attach` 后通过填写其链路层地址来完成此结构。结构的其他成员表示通过 `SIOCAIFADDR` 命令对 ioctl(2)（在适当协议族的套接字上调用）配置的网络层地址。此列表的元素由 `ifaddr` 结构组成。大多数协议将声明其自己特定于协议的接口地址结构，但都以 `struct ifaddr` 开头，后者提供所有协议中最常用的功能。接口地址采用引用计数。

`struct ifaddr` 的成员如下：

**`ifa_addr`** (`struct sockaddr *`) 接口的本地地址。

**`ifa_dstaddr`** (`struct sockaddr *`) 点对点接口的远程地址，以及广播接口的广播地址。（`ifa_broadaddr` 是 `ifa_dstaddr` 的宏。）

**`ifa_netmask`** (`struct sockaddr *`) 多访问接口的网络掩码，以及点对点接口的混淆生成器。

**`ifa_ifp`** (`if_t`) 返回接口结构的链接。

**`ifa_link`** (`TAILQ_ENTRY ifaddr`) [queue(3)](../man3/queue.3.md) 用于每个接口上地址列表的胶水。

**`ifa_rtrequest`** 见下文。

**`ifa_flags`** (`u_short`) 一些将用于路由表中表示此地址的路由的标志。

**`ifa_refcnt`** (`short`) 引用计数。

对 `ifaddr` 结构的引用通过调用 `ifa_ref` 函数获得，通过调用 `ifa_free` 函数释放。

`ifa_rtrequest` 是指向函数的指针，该函数接收来自路由代码（`rtrequest`）的调用，以在添加或删除路由请求时执行链路层特定操作。`cmd` 参数指示相关请求：`RTM_ADD` 或 `RTM_DELETE`。`rt` 参数是相关路由；`info` 参数包含正在操作的具体目标。

## 函数

通用接口代码提供的函数可分为两组：操作接口的函数和操作接口地址的函数。除这些函数外，还可能存在由在不同硬件上实现特定链路层的许多驱动程序使用的链路层支持例程；有关更多详细信息，请参阅该链路层的文档。

### ifmultiaddr 结构

每个支持多播的接口都与一个多播组成员资格列表关联，该列表在低级别指示应接受哪些链路层多播地址（如果有），在高级别指示用户进程对哪些网络层多播组表达了兴趣。

结构的元素如下：

**`ifma_link`** (`LIST_ENTRY ifmultiaddr`) [queue(3)](../man3/queue.3.md) 宏胶水。

**`ifma_addr`** (`struct sockaddr *`) 指向此记录表示的地址的指针。各种地址族的成员资格以任意顺序存储。

**`ifma_lladdr`** (`struct sockaddr *`) 指向 `ifma_addr` 中的网络层多播地址映射到的链路层多播地址（如果有）的指针，否则为空指针。如果此元素非空，此成员资格还持有对该链路层地址的另一成员资格的不可见引用。

**`ifma_refcount`** (`u_int`) 此特定成员资格请求的引用计数。

### 接口操作函数

**`SIOCGIFCONF`** 获取接口配置。（无调用下到驱动程序。）
**`SIOCSIFNAME`** 设置接口名称。发送 `RTM_IFANNOUNCE` 离开和到达消息，以便依赖接口名称的路由代码更新其接口列表。调用者必须具有适当特权。（无调用下到驱动程序。）
**`SIOCGIFCAP`**
**`SIOCGIFDATA`**
**`SIOCGIFFIB`**
**`SIOCGIFFLAGS`**
**`SIOCGIFMETRIC`**
**`SIOCGIFMTU`**
**`SIOCGIFPHYS`** 获取接口能力、数据、FIB、标志、度量、MTU、介质选择。（无调用下到驱动程序。）
**`SIOCSIFCAP`** 启用或禁用接口能力。调用者必须具有适当特权。在调用驱动程序特定的 `if_ioctl` 例程之前，请求的已启用能力掩码将针对接口支持的能力掩码 `if_capabilities` 进行检查。请求启用不支持的能力是无效的。其余工作应由驱动程序完成，包括适当地更新 `if_capenable` 和 `if_data.ifi_hwassist`。
**`SIOCGIFCAPNV`** `SIOCGIFCAP` ioctl 的 [nv(9)](nv.9.md) 版本。调用者必须提供指向 `struct ifreq_cap_nv` 的指针作为 `data`，其中成员 `buffer` 指向包含 `buf_length` 字节的某个缓冲区。描述设备能力的序列化 nvlist 写入缓冲区。如果缓冲区太短，结构更新为 `buffer` 成员设置为 `NULL`，`length` 设置为最小所需长度，并返回错误 `EFBIG`。简单能力的返回 nvlist 元素是布尔值，由名称标识。布尔元素的存在意味着接口支持相应能力。元素的值描述当前配置状态：`true` 表示能力已启用，`false` 表示已禁用。驱动程序通过在 `if_capabilities` 中设置 `IFCAP_NV` 不可修改能力位来指示对 `SIOCGIFCAPNV` 和 `SIOCSIFCAPNV` 请求的支持。
**`SIOCSIFCAPNV`** `SIOCSIFCAP` ioctl 的 [nv(9)](nv.9.md) 版本。调用者必须提供指向 `struct ifreq_cap_nv` 的指针作为 `data`，其中成员 `buffer` 指向 `length` 字节的序列化 nvlist。nvlist 的每个元素描述一个能力的请求更新，由元素名称标识。对于简单能力，元素必须为布尔值。其 `true` 值表示调用者请求启用该能力，`false` 值表示禁用。只有 nvlist 中列出的能力受调用影响。
**`SIOCSIFFIB`** 设置接口 FIB。调用者必须具有适当特权。FIB 值从 0 开始，大于或等于 `net.fibs` 的值被视为无效。
**`SIOCSIFFLAGS`** 更改接口标志。调用者必须具有适当特权。如果请求更改 `IFF_UP` 标志，则根据情况调用 `if_up` 或 `if_down`。`IFF_CANTCHANGE` 中列出的标志被屏蔽掉，接口结构中的 `if_flags` 字段被更新。最后，调用驱动程序 `if_ioctl` 例程以执行请求的任何设置。
**`SIOCSIFMETRIC`**
**`SIOCSIFPHYS`** 更改接口度量或介质。调用者必须具有适当特权。
**`SIOCSIFMTU`** 更改接口 MTU。调用者必须具有适当特权。小于 72 或大于 65535 的 MTU 值被视为无效。调用驱动程序 `if_ioctl` 例程以实现更改；它负责任何额外的健全性检查以及实际修改接口结构中的 MTU。
**`SIOCADDMULTI`**
**`SIOCDELMULTI`** 在接口上添加或删除永久多播组成员资格。调用者必须具有适当特权。调用 `if_addmulti` 或 `if_delmulti` 函数以执行操作；qq.v。
**`SIOCAIFADDR`**
**`SIOCDIFADDR`** 调用套接字的协议控制例程以实现请求的操作。

**Fn** `if_alloc` 分配并初始化 `struct ifnet`。初始化包括分配接口索引，可能包括在 `if_l2com` 中分配 `type` 特定结构。

**Fn** `if_alloc_dev` 像 `if_alloc` 一样分配并初始化 `struct ifnet`，增加 ifnet 可以标记为从调用者传递的 `dev` 参数派生的适当 NUMA 域。

**Fn** `if_alloc_domain` 像 `if_alloc` 一样分配并初始化 `struct ifnet`，增加 ifnet 将通过调用者传递的 `numa_domain` 参数标记为 NUMA 域。

**Fn** `if_attach` 将指定接口 `ifp` 链接到网络接口列表。同时初始化该接口上的地址列表，并创建一个链路层 `ifaddr` 结构作为该列表中的第一个元素。（指向此地址结构的指针保存在 `ifnet` 结构中。）`ifp` 必须由 `if_alloc`、`if_alloc_dev` 或 `if_alloc_domain` 分配。

**Fn** `if_detach` 关闭并从接口列表中取消链接指定的 `ifp`。

**Fn** `if_free` 将给定的 `ifp` 释放回系统。如果接口曾经附加过，则必须先将其分离。

**Fn** `if_free_type` 与 `if_free` 相同，但使用给定的 `type` 来释放 `if_l2com` 而不是 `if_type` 中的类型。这旨在用于更改其接口类型的驱动程序。

**Fn** `if_down` 将接口 `ifp` 标记为关闭（即未设置 `IFF_UP`），刷新其输出队列，通知协议转换，并从 [route(4)](../man4/route.4.md) 路由套接字生成消息。

**Fn** `if_up` 将接口 `ifp` 标记为启用，通知协议转换，并从 [route(4)](../man4/route.4.md) 路由套接字生成消息。

**Fn** `ifpromisc` 添加或删除对 `ifp` 的混杂引用。如果 `pswitch` 为真，添加引用；如果为假，删除引用。在引用计数从零到一和从一到零的转换时，适当设置 `IFF_PROMISC` 标志并调用 `if_ioctl` 以在所需模式下设置接口。

**Fn** `if_allmulti` 与 `ifpromisc` 相同，但用于全多播（`IFF_ALLMULTI`）标志而不是混杂标志。

**Fn** `ifunit` 返回名为 `name` 的接口的 `ifnet` 指针。

**Fn** `ifunit_ref` 返回名为 `name` 的接口的引用计数（通过 `ifa_ref`）`ifnet` 指针。这是优于 `ifunit` 的首选函数。调用者负责在使用完 ifnet 后用 `if_rele` 释放引用。

**Fn** `ifioctl` 处理由线程 `td` 在套接字 `so` 上发出的、带数据参数 `data` 的 ioctl 请求 `cmd`。这是处理来自用户模式的所有接口配置请求的主例程。它通常仅从套接字层 ioctl(2) 处理程序调用，且仅用于类“`i`”的命令。任何无法识别的命令将下传到套接字 `so` 的协议进行进一步解释。以下命令由 `ifioctl` 处理：

### 接口地址函数

存在若干函数用于在给定地址的情况下查找接口地址结构。`ifa_ifwithaddr` 返回本地地址或广播地址精确匹配参数 `addr` 的接口地址。`ifa_ifwithdstaddr` 返回远程（“目标”）地址为 `addr` 且 fib 为 `fib` 的点对点接口的接口地址。如果 `fib` 为 `RT_ALL_FIBS`，则返回第一个匹配 `addr` 的接口地址。

`ifa_ifwithnet` 返回在配置的网络掩码下匹配指定地址 `addr` 的最具体的接口地址，或如果找到，则返回远程地址为 `addr` 的点对点接口地址。如果 `ignore_ptp` 为真，跳过点对点接口地址。`fib` 参数的处理方式与 `ifa_ifwithdstaddr` 相同。

`ifaof_ifpforaddr` 返回在配置的网络掩码下在接口 `ifp` 上配置的匹配地址 `addr` 的最具体地址。如果接口是点对点的，仅返回远程地址精确为 `addr` 的接口地址。

如果找不到此类地址，所有这些函数返回空指针。

### 接口多播地址函数

`if_addmulti`、`if_delmulti` 和 `if_findmulti` 函数分别提供请求和放弃多播组成员资格以及查询接口成员资格列表的支持。`if_addmulti` 函数接受指向接口 `ifp` 和通用地址 `sa` 的指针。它还接受指向 `struct ifmultiaddr *` 的指针，成功返回时填充组成员资格控制块的地址。`if_addmulti` 函数执行以下四步过程：

- 调用接口的 `if_resolvemulti` 入口点以确定与此成员资格请求对应的链路层地址（如果有），并给链路层机会在其希望时否决此成员资格请求。
- 检查接口的组成员资格列表中是否存在此组的现有成员资格。如果未找到，分配新的；如果找到，递增其引用计数。
- 如果 `if_resolvemulti` 例程返回对应于组的链路层地址，对该地址重复上一步。
- 如果因添加了新成员资格而需要更改接口的多播地址过滤器，调用接口的 `if_ioctl` 例程（`cmd` 参数为 `SIOCADDMULTI`）以请求其这样做。

`if_delmulti` 函数给定接口 `ifp` 和地址 `sa`，反转此过程。两个函数成功返回零，失败返回标准错误号。

`if_findmulti` 函数检查接口 `ifp` 的成员资格列表中是否有匹配 `sa` 的地址，如果找到则返回指向该 `struct ifmultiaddr` 的指针，否则返回空指针。

## 参见

ioctl(2), link_addr(3), [queue(3)](../man3/queue.3.md), sysctl(3), [bpf(4)](../man4/bpf.4.md), [ifmib(4)](../man4/ifmib.4.md), [lo(4)](../man4/lo.4.md), [netintro(4)](../man4/netintro.4.md), [polling(4)](../man4/polling.4.md), [config(8)](../man8/config.8.md), ppp(8), [mbuf(9)](mbuf.9.md), [rtentry(9)](rtentry.9.md)

> Gary R. Wright, W. Richard Stevens, *TCP/IP Illustrated*, Vol. 2, Addison-Wesley, ISBN 0-201-63354-X.

## 作者

本手册页由 Garrett A. Wollman 编写。
