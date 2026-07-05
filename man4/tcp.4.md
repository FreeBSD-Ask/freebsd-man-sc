# tcp.4

`tcp` — Internet 传输控制协议

## 名称

`tcp`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <netinet/tcp.h>`

`Ft int Fn socket AF_INET SOCK_STREAM 0`

## 描述

TCP 协议提供可靠、流量控制的双向数据传输。它是一种字节流协议，用于支持 `SOCK_STREAM` 抽象。TCP 使用标准 Internet 地址格式，此外还提供每主机的“端口地址”集合。因此，每个地址由指定主机和网络的 Internet 地址组成，主机上的特定 TCP 端口标识对端实体。

使用 TCP 协议的套接字要么是“主动”的，要么是“被动”的。主动套接字向被动套接字发起连接。默认情况下，TCP 套接字创建为主动；要创建被动套接字，必须在用 bind(2) 系统调用绑定套接字后使用 listen(2) 系统调用。只有被动套接字可使用 accept(2) 调用接受传入连接。只有主动套接字可使用 connect(2) 调用发起连接。

被动套接字可以“欠指定”其位置以匹配来自多个网络的传入连接请求。这种技术称为 “通配地址”，允许单个服务器向多个网络上的客户端提供服务。要创建在所有网络上监听的套接字，必须绑定 Internet 地址 `INADDR_ANY`。此时仍可指定 TCP 端口；如果不指定端口，系统将分配一个。连接建立后，套接字的地址由对端实体的位置固定。分配给套接字的地址是与通过其收发数据包的网络接口关联的地址。通常，此地址对应于对端实体所在的网络。

TCP 支持许多套接字选项，可使用 setsockopt(2) 设置、使用 getsockopt(2) 测试：

```sh
SipHash24(key=16-byte-psk, msg=cookie-sent-to-client)
```

**`TCP_REUSPORT_LB_NUMA_NODOM`** 移除此监听套接字的 NUMA 过滤。

**`TCP_REUSPORT_LB_NUMA_CURDOM`** 过滤与调用线程当前执行的域相关联的流量。通常在进程或线程从其父进程继承监听套接字并将其 CPU 亲和性设置为特定核心后使用。

**`TCP_INFO`** 可以通过将只读选项 `TCP_INFO` 传递给 getsockopt(2) 来检索有关套接字底层 TCP 会话的信息。它接受单个参数：指向 `struct tcp_info` 实例的指针。此 API 可能会更改；请查阅源代码以确定此选项当前填充了哪些字段。FreeBSD 特有的扩展包括发送窗口大小、接收窗口大小和带宽控制的窗口空间。

**`TCP_CCALGOOPT`** 设置或查询拥塞控制算法特定参数。详见 [mod_cc(4)](mod_cc.4.md)。

**`TCP_CONGESTION`** 选择或查询 TCP 用于连接的拥塞控制算法。详见 [mod_cc(4)](mod_cc.4.md)。

**`TCP_FASTOPEN`** 启用或禁用 TCP Fast Open（TFO）。要使用此选项，内核必须使用 `TCP_RFC7413` 选项构建。可在调用 listen(2) 之前或之后在套接字上设置此选项。在已设置的监听套接字上清除此选项对现有 TFO 连接或正在进行的 TFO 连接没有影响；它仅阻止建立新的 TFO 连接。对于被动创建的套接字，可查询 `TCP_FASTOPEN` 套接字选项以确定连接是否使用 TFO 建立。注意，通过 TFO SYN 建立但回退到使用非 TFO SYN|ACK 的连接将设置 `TCP_FASTOPEN` 套接字选项。除 RFC7413 中定义的功能外，此实现还支持预共享密钥（PSK）操作模式，其中 TFO 服务器要求客户端拥有共享密钥才能成功与服务器建立 TFO 连接。例如，在 TFO 服务器同时暴露给内部和外部客户端且只希望允许来自内部客户端的 TFO 连接的环境中，这很有用。在 PSK 模式下，服务器照常生成 TFO cookie 并发送给请求的客户端。但是，在验证来自客户端 TFO SYN 中的 cookie 时，服务器要求客户端提供的 cookie 等于多个并发的有效预共享密钥，因此系统中可实现基于时间的滚动 PSK 失效策略。并发预共享密钥的默认数量为 2。可使用 `TCP_RFC7413_MAX_PSKS` 内核选项调整。

**`TCP_FUNCTION_BLK`** 选择或查询 TCP 用于此连接的功能集。允许用户选择备用 TCP 栈。备用 TCP 栈必须已加载到内核中。要列出可用的 TCP 栈，参见下文 Sx FIB 支持 TCP 套接字支持 FIB 感知。它们继承创建套接字的进程的 FIB，或对于由 accept(2) 创建的套接字，继承监听套接字的 FIB。特别是，FIB 不从接收发起 SYN 数据包的接口继承。当传入连接请求到达监听套接字时，初始握手也在监听套接字的 FIB 中进行，而不是接收数据包的 FIB。默认情况下，TCP 监听套接字可接受来自任何 FIB 的连接。如果 `net.inet.tcp.bind_all_fibs` 可调参数设为 0，监听套接字将仅接受源自该 FIB 监听套接字的连接。来自其他 FIB 的连接请求将被视为目标地址和端口上没有监听套接字。在此模式下，同一用户拥有的多个监听套接字可以在同一地址和端口上监听，只要它们属于不同的 FIB，类似于 `SO_REUSEPORT` 套接字选项的行为。如果可调参数设为 0，则添加到使用 `SO_REUSEPORT_LB` 套接字选项创建的负载均衡组的所有套接字必须属于同一 FIB。Sx MIB（sysctl）变量章节。要列出默认 TCP 栈，参见 Sx MIB（sysctl）变量章节中的 `functions_default`。

**`TCP_KEEPINIT`** 此 setsockopt(2) 选项接受 `u_int` 类型的每套接字超时参数（秒），用于新的、未建立的 TCP 连接。有关以毫秒为单位的全局默认值，参见下文 Sx MIB（sysctl）变量章节中的 `keepinit`。

**`TCP_KEEPIDLE`** 此 setsockopt(2) 选项接受 `u_int` 参数（秒），表示在为此套接字的连接发送保活探测（如果启用）之前连接必须空闲的时间。如果在监听套接字上设置，该值将由 accept(2) 创建的新套接字继承。有关以毫秒为单位的全局默认值，参见下文 Sx MIB（sysctl）变量章节中的 `keepidle`。

**`TCP_KEEPINTVL`** 此 setsockopt(2) 选项接受 `u_int` 参数，设置发送给对端的保活探测之间的每套接字间隔（秒）。如果在监听套接字上设置，该值将由 accept(2) 创建的新套接字继承。有关以毫秒为单位的全局默认值，参见下文 Sx MIB（sysctl）变量章节中的 `keepintvl`。

**`TCP_KEEPCNT`** 此 setsockopt(2) 选项接受 `u_int` 参数，允许在丢弃连接之前调整每套接字的探测次数（无响应）。如果在监听套接字上设置，该值将由 accept(2) 创建的新套接字继承。有关全局默认值，参见下文 Sx MIB（sysctl）变量章节中的 `keepcnt`。

**`TCP_NODELAY`** 在大多数情况下，TCP 在数据呈现时发送；当未确认的未完成数据尚未被确认时，它会收集少量输出，以便在收到确认后作为单个数据包发送。对于少数客户端（如发送无回复鼠标事件流的窗口系统），这种打包可能造成显著延迟。布尔选项 `TCP_NODELAY` 禁用此算法。

**`TCP_MAXSEG`** 默认情况下，发送方和接收方 TCP 会自行协商确定每个连接使用的最大段大小。`TCP_MAXSEG` 选项允许用户确定此协商的结果，并在需要时减小它。

**`TCP_MAXUNACKTIME`** 此 setsockopt(2) 选项接受 `u_int` 参数，设置每套接字的间隔（秒），在此期间连接必须取得进展。进展定义为在设定的时间段内至少有 1 字节被确认。如果连接未能取得进展，TCP 栈将以重置终止连接。注意，默认值为零，表示不进行进展检查。

**`TCP_NOOPT`** TCP 通常在每个数据包中发送许多选项，对应此实现中提供的各种 TCP 扩展。布尔选项 `TCP_NOOPT` 用于在每个连接上禁用 TCP 选项使用。

**`TCP_NOPUSH`** 按惯例，发送方 TCP 在每次用户调用 write(2) 或 writev(2) 结束时设置“push”位，并（如果允许）立即开始传输。当此选项设为非零值时，TCP 将延迟发送任何数据，直到套接字关闭或内部发送缓冲区填满。

**`TCP_MD5SIG`** 此选项允许对指定套接字的写入使用 MD5 摘要（也称为 TCP-MD5）。出站流量被摘要；入站流量的摘要被验证。在套接字上启用此选项时，所有入站和出站 TCP 段都必须用 MD5 摘要签名。在 FreeBSD 路由器部署中，一个常见用途是使基于 BGP 的路由器能在对等点与 Cisco 设备互操作。对此功能的支持符合 RFC 2385。要使此选项正常工作，管理员必须使用 setkey(8) 实用程序将 tcp-md5 密钥条目添加到系统的安全关联数据库（SADB）中。此条目目前只能按主机指定。如果找不到目标的 SADB 条目，系统不会发送任何出站段并丢弃所有入站段。但是，在连接协商期间，如果主机之间不存在 SADB 条目，将接受非签名段。当接受非签名段时，已建立的连接不受 MD5 摘要保护。

**`TCP_STATS`** 使用 [stats(3)](../man3/stats.3.md) 框架管理连接级统计信息的收集。每个丢弃的段都会计入 TCP 协议统计信息。

**`TCP_TXTLS_ENABLE`** 为写入此套接字的数据启用内核中传输层安全（TLS）。详见 [ktls(4)](ktls.4.md)。

**`TCP_TXTLS_MODE`** 整数参数可用于获取或设置套接字的当前 TLS 传输模式。详见 [ktls(4)](ktls.4.md)。

**`TCP_RXTLS_ENABLE`** 为从此套接字读取的数据启用内核中 TLS。详见 [ktls(4)](ktls.4.md)。

**`TCP_REUSPORT_LB_NUMA`** 更改已建立的 TCP 监听套接字的 NUMA 亲和性过滤。此选项接受单个整数参数，指定要为此监听套接字过滤的 NUMA 域。参数还可以有以下特殊值：

**`TCP_REMOTE_UDP_ENCAPS_PORT`** 设置和获取远程 UDP 封装端口。只能在已关闭的 TCP 套接字上设置。

setsockopt(2) 调用的选项级别是 TCP 的协议号，可从 getprotobyname(3) 或 `IPPROTO_TCP` 获取。所有选项均声明于

`#include <netinet/tcp.h>`

IP 传输级别的选项可与 TCP 一起使用；参见 [ip(4)](ip.4.md)。源路由传入连接请求会被记录，响应时使用反向源路由。

TCP 的默认拥塞控制算法是 [cc_cubic(4)](cc_cubic.4.md)。可使用 [mod_cc(4)](mod_cc.4.md) 框架提供其他拥塞控制算法。

### MIB（sysctl）变量

TCP 协议在 sysctl(3) MIB 的 `net.inet.tcp` 分支下实现许多变量，也可使用 [sysctl(8)](../man8/sysctl.8.md) 读取或修改。

**0** 禁用 ECN。
**1** 允许传入连接请求 ECN。出站连接将请求 ECN。
**2** 允许传入连接请求 ECN。出站连接不请求 ECN。（默认）
**3** 在传入连接上协商 Accurate ECN、ECN 或无 ECN。出站连接将请求 Accurate ECN，并根据服务器能力回退到 ECN。
**4** 在传入连接上协商 Accurate ECN、ECN 或无 ECN。出站连接不请求 ECN。

**0** 禁用主机缓存。
**1** 启用主机缓存。（默认）

**0** 修剪主机缓存时不清除所有条目（默认）。
**1** 下次修剪时清除所有条目。
**2** 清除所有条目并重新设置哈希盐。

**0** 禁用路径 MTU 黑洞检测。
**1** 为 IPv4 和 IPv6 启用路径 MTU 黑洞检测。
**2** 仅对 IPv4 启用路径 MTU 黑洞检测。
**3** 仅对 IPv6 启用路径 MTU 黑洞检测。

**0** 禁用窗口缩放和时间戳选项。
**1** 启用窗口缩放和时间戳选项。
**2** 仅启用窗口缩放。
**3** 仅启用时间戳选项。

**`ack_war_timewindow`, `ack_war_cnt`** RFC 5961 中定义的挑战 ACK 节流算法限制每个 TCP 连接在 `ack_war_timewindow` 指定的时间间隔（毫秒）内发送的挑战 ACK 数量为 `ack_war_cnt`。将 `ack_war_timewindow` 或 `ack_war_cnt` 设为零可禁用挑战 ACK 节流。

**`always_keepalive`** 假定所有 TCP 连接都设置了 `SO_KEEPALIVE`，内核将定期向远程主机发送数据包以验证连接是否仍然存活。

**`blackhole`** 如果启用，当连接尝试到达没有套接字接受连接的端口时，禁用发送 RST。参见 [blackhole(4)](blackhole.4.md)。

**`blackhole_local`** 参见 [blackhole(4)](blackhole.4.md)。

**`cc`** `net.inet.tcp.cc` 节点下有许多拥塞控制变量。参见 [mod_cc(4)](mod_cc.4.md)。

**`cc.newreno`** `net.inet.tcp.cc.newreno` 节点下有 NewReno 拥塞控制变量。参见 [cc_newreno(4)](cc_newreno.4.md)。

**`delacktime`** 发送延迟 ACK 之前的最大时间（毫秒）。

**`delayed_ack`** 延迟 ACK 以尝试将其搭载到数据包或另一个 ACK 上。

**`do_prr`** 使用 RFC6937 中描述的比例速率减少（PRR）算法执行 SACK 丢失恢复。这提高了在 ACK 稀疏或突发丢失环境中的重传效率，因为 ACK 时钟耗尽的机会减少，防止了冗长且降低性能的基于 RTO 的丢失恢复（默认为 true）。

**`do_tcpdrain`** 当系统 mbuf 不足时刷新 TCP 重装队列中的数据包。

**`drop_synfin`** 丢弃同时设置 SYN 和 FIN 的 TCP 数据包。

**`ecn.enable`** 启用 TCP 显式拥塞通知（ECN）支持。ECN 允许 TCP 发送方降低传输速率以避免丢包。

**`ecn.maxretries`** 在禁用特定连接的 ECN 之前的重试次数（SYN 或 SYN/ACK 重传）。在网络路径中存在损坏的防火墙时，这有助于建立连接。

**`fast_finwait2_recycle`** 当套接字被标记为 `SBS_CANTRCVMORE`（没有用户进程打开套接字，套接字上接收的数据无法读取）时，更快地回收 TCP `FIN_WAIT_2` 连接。此处使用的超时为 `finwait2_timeout`。

**`fastopen.acceptany`** 非零时，所有客户端提供的 TFO cookie 都将被视为有效。默认为 0。

**`fastopen.autokey`** 当此项和 `net.inet.tcp.fastopen.server_enable` 非零时，将在指定秒数后自动生成新密钥。默认为 120。

**`fastopen.ccache_bucket_limit`** 客户端 cookie 缓存桶中的最大条目数。默认值可通过 `TCP_FASTOPEN_CCACHE_BUCKET_LIMIT_DEFAULT` 内核选项调整，或通过在 [loader(8)](../man8/loader.8.md) 中设置 `net.inet.tcp.fastopen_ccache_bucket_limit` 调整。

**`fastopen.ccache_buckets`** 客户端 cookie 缓存桶的数量。只读。该值可通过 `TCP_FASTOPEN_CCACHE_BUCKETS_DEFAULT` 内核选项调整，或通过在 [loader(8)](../man8/loader.8.md) 中设置 `fastopen.ccache_buckets` 调整。

**`fastopen.ccache_list`** 打印客户端 cookie 缓存。只读。

**`fastopen.client_enable`** 为零时，无法创建新的主动（即客户端）TFO 连接。从启用到禁用的转换时，客户端 cookie 缓存将被清除并禁用。从启用到禁用的转换不影响任何正在进行的主动 TFO 连接；它仅阻止建立新连接。默认为 1。

**`fastopen.keylen`** 密钥长度（字节）。只读。

**`fastopen.maxkeys`** 支持的最大密钥数。只读。

**`fastopen.maxpsks`** 支持的最大预共享密钥数。只读。

**`fastopen.numkeys`** 当前已安装的密钥数。只读。

**`fastopen.numpsks`** 当前已安装的预共享密钥数。只读。

**`fastopen.path_disable_time`** 当尝试创建新的主动（即客户端）TFO 连接时发生失败，同一路径上（由元组 {client_ip, server_ip, server_port} 确定）的新主动连接将在此秒数内被强制为非 TFO。注意，路径禁用机制依赖于客户端 cookie 缓存条目中存储的状态，因此如果由于资源压力在禁用期结束前重用了相应的客户端 cookie 缓存条目，给定路径的禁用时间可能会缩短。默认为 `TCP_FASTOPEN_PATH_DISABLE_TIME_DEFAULT`。

**`fastopen.psk_enable`** 非零时，为所有 TFO 服务器启用预共享密钥（PSK）模式。从启用到禁用的转换时，所有已安装的预共享密钥都将被移除。默认为 0。

**`fastopen.server_enable`** 为零时，无法创建新的被动（即服务器）TFO 连接。从启用到禁用的转换时，所有已安装的密钥和预共享密钥都将被移除。从禁用到启用的转换时，如果 `fastopen.autokey` 非零且没有已安装的密钥，将立即生成新密钥。从启用到禁用的转换不影响任何正在进行的被动 TFO 连接；它仅阻止建立新连接。默认为 0。

**`fastopen.setkey`** 通过向此 sysctl 写入 `net.inet.tcp.fastopen.keylen` 字节来安装新密钥。

**`fastopen.setpsk`** 通过向此 sysctl 写入 `net.inet.tcp.fastopen.keylen` 字节来安装新预共享密钥。

**`finwait2_timeout`** 用于快速回收 TCP `FIN_WAIT_2` 连接（`fast_finwait2_recycle`）的超时。默认为 60 秒。

**`functions_available`** 可用 TCP 功能块（TCP 栈）列表。

**`functions_default`** 默认 TCP 功能块（TCP 栈）。

**`hostcache`** TCP 主机缓存用于缓存连接详情和指标，以提高同一主机之间未来连接的性能。在 TCP 连接完成时，主机将在某段定义的时间段内缓存该连接的信息。此节点下有许多 `hostcache` 变量。参见 `hostcache.enable`。

**`hostcache.bucketlimit`** 同一哈希的最大条目数。默认为 30。

**`hostcache.cachelimit`** hostcache 的总体条目限制。默认为 `hashsize` * `bucketlimit`。

**`hostcache.count`** 主机缓存中的当前条目数。

**`hostcache.enable`** 启用/禁用主机缓存：

**`hostcache.expire`** 自上次访问以来条目在主机缓存中保留的时间（秒）。默认为 3600（1 小时）。

**`hostcache.hashsize`** TCP hostcache 哈希表的大小。此数字必须是 2 的幂，否则将被拒绝。默认为 512。

**`hostcache.histo`** 提供 hostcache 哈希利用率的直方图。

**`hostcache.list`** 提供主机缓存中所有当前条目的完整列表。

**`hostcache.prune`** 修剪过期主机缓存条目之间的时间间隔（秒）。默认为 300（5 分钟）。

**`hostcache.purge`** 在下次修剪主机缓存条目时使所有条目过期。任何非零设置在清除运行后都将重置为零。

**`hostcache.purgenow`** 一旦设为任何值就立即清除所有条目。设为 2 还将重新设置哈希盐。

**`icmp_may_rst`** 某些 ICMP 不可达消息可以中止处于 SYN-SENT 状态的连接。

**`initcwnd_segments`** 启用以段数为单位指定初始拥塞窗口的能力。默认值为 10，如 RFC 6928 所建议。即时更改此值不会影响使用 hostcache 中拥塞窗口的连接。注意：这 regulates 在第一个 RTT 中允许发送的数据包突发。该值应与链路容量相关。对于低容量链路，应从较小值开始。如果路由器缓冲区较小或链路经历拥塞，大突发可能导致缓冲区溢出和丢包。

**`insecure_rst`** 使用 RFC793 中定义的标准而非 RFC5961 来接受 RST 段。默认为 false。

**`insecure_syn`** 使用 RFC793 中定义的标准而非 RFC5961 来接受 SYN 段。默认为 false。

**`insecure_ack`** 使用 RFC793 中定义的标准来验证 SEG.ACK。默认为 false。

**`isn_reseed_interval`** 指定 RFC 1948 初始序列号计算中使用的秘密数据多久重新设置一次的间隔（秒）。默认情况下，此变量设为零，表示不会重新设置。重新设置不应是必要的，并且会破坏 `TIME_WAIT` 回收几分钟。

**`keepcnt`** 在丢弃连接之前发送的保活探测次数（无响应）。默认为 8 个数据包。

**`keepidle`** 在发送保活探测（如果启用）之前连接必须空闲的时间量（毫秒）。默认为 7200000 毫秒（7.2M 毫秒，2 小时）。

**`keepinit`** 新的、未建立的 TCP 连接的超时（毫秒）。默认为 75000 毫秒（75K 毫秒，75 秒）。

**`keepintvl`** 当 `keepidle` 探测未收到响应时，发送给远程机器的保活探测之间的间隔（毫秒）。默认为 75000 毫秒（75K 毫秒，75 秒）。

**`log_in_vain`** 记录所有到没有套接字接受连接的端口的连接尝试。值为 1 时仅记录 SYN（连接建立）数据包。值为 2 时记录到关闭端口的任何 TCP 数据包。任何未列出的值都禁用日志记录（默认为 0，即禁用日志记录）。

**`minmss`** 最小 TCP 最大段大小；用于防止来自不合理低 MSS 的拒绝服务攻击。

**`msl`** 数据包的最大段生存期（毫秒）。

**`msl_local`** 当两端点都是本地时，数据包的最大段生存期（毫秒）。`msl_local` 仅在已弃用的 `nolocaltimewait` 为零时使用。

**`mssdflt`** 当未从 MSS 协商中收到相反建议时，IPv4 的 TCP 最大段大小（“MSS”）的默认值。

**`newcwv`** 启用 RFC 7661 中描述的新拥塞窗口验证机制。这在 TCP 受应用限制且网络带宽未完全利用期间温和地减小拥塞窗口。这可以防止应用程序以更高速度开始传输数据时的自致丢包。

**`nolocaltimewait`** 抑制两端点都是本地的连接的 TCP `TIME_WAIT` 状态创建。默认为 0。`nolocaltimewait` 已弃用，将在 FreeBSD 16 中移除。可改用 `msl_local`。

**`path_mtu_discovery`** 启用路径 MTU 发现。

**`pcbcount`** 活动协议控制块数量（只读）。

**`perconn_stats_enable`** 控制使用 [stats(3)](../man3/stats.3.md) 框架的所有连接的默认统计信息收集。0 禁用，1 启用，2 启用跨日志 ID 连接组的随机采样，组内所有连接接收相同设置。

**`perconn_stats_sample_rates`** 一个由 template_spec=percent 键值对组成的 CSV 列表，当启用 [stats(3)](../man3/stats.3.md) 采样时控制每模板的采样率。

**`persmax`** 最大持续间隔（毫秒）。

**`persmin`** 最小持续间隔（毫秒）。

**`pmtud_blackhole_detection`** 启用自动路径 MTU 黑洞检测。在重传 MSS 大小的段时，操作系统会降低 MSS 以检查是否是 MTU 问题。如果当前 MSS 大于要尝试的配置值（`net.inet.tcp.pmtud_blackhole_mss` 和 `net.inet.tcp.v6pmtud_blackhole_mss`），则设为此值，否则 MSS 设为默认值（`net.inet.tcp.mssdflt` 和 `net.inet.tcp.v6mssdflt`）。设置：

**`pmtud_blackhole_mss`** 启用 PMTU 黑洞检测时 IPv4 要尝试的 MSS。

**`reass.cursegments`** 所有重装队列中当前段的总数。

**`reass.maxqueuelen`** 每个重装队列中允许的最大段数。默认情况下，系统根据每个 TCP 连接的接收缓冲区大小和最大段大小（MSS）选择限制。应用于会话重装队列的实际限制将是系统计算的自动限制和用户指定的 `reass.maxqueuelen` 限制中的较小者。

**`reass.maxsegments`** 所有重装队列中段总数的最大限制。该限制可作为可调参数调整。

**`recvbuf_auto`** 随着连接的进行启用自动接收缓冲区大小调整。

**`recvbuf_max`** 自动接收缓冲区的最大大小。

**`recvspace`** 初始 TCP 接收窗口（缓冲区大小）。

**`retries`** 数据段丢失后发送的基于定时器的连续重传最大次数（默认和最大为 12）。

**`rexmit_drop_options`** 从连接的第三次及以后重传 SYN 段中丢弃 TCP 选项。

**`rexmit_initial`, `rexmit_min`, `rexmit_slop`, `rexmit_max`** 调整 TCP 的重传定时器计算。新连接以 `rexmit_initial` 定时器值开始。`rexmit_slop` 通常加到原始计算中，以考虑 SRTT（平滑往返时间）无法容纳的偶尔偏差，而最小值指定绝对最小值。虽然许多 TCP RFC 建议 1 秒最小值，但这些 RFC 往往关注流式行为，未能处理 1 秒最小值对有损交互连接（如 802.11b 无线链路）以及非常快但有损连接（在快速重传代码未覆盖的情况下）产生严重不利影响的事实。因此，我们使用 200ms 的 slop 和接近 0 的最小值，得到 200ms 的有效最小值（类似于 Linux）。初始值在执行 RTT 测量之前使用。`rexmit_min` 和 `rexmit_max` 设置连接可能具有的最小和最大定时器值。

**`rfc1323`** 实现 RFC 1323/RFC 7323 的窗口缩放和时间戳选项（默认为 1）。设置：

**`rfc3042`** 启用 RFC 3042 中描述的 Limited Transmit 算法。它有助于在有损链路上以及拥塞窗口较小时（如短传输中）避免超时。

**`rfc3390`** 启用对 RFC 3390 的支持，根据最大段大小允许新连接上可变大小的起始拥塞窗口。这通常有助于吞吐量，特别是对短传输和高带宽大传播延迟连接。

**`rfc6191`** 启用 RFC 6191 连接回收，当新连接启用 TCP 时间戳时，可在某些情况下更快地回收连接。

**`sack.enable`** 启用对 RFC 2018、TCP 选择性确认选项的支持，允许接收方通知发送方所有成功到达的段，使发送方仅重传丢失的段。

**`sack.globalholes`** 当前分配的全局 TCP SACK 孔数。

**`sack.globalmaxholes`** 跨所有连接的每系统最大 SACK 孔数。默认为 65536。

**`sack.lrd`** 为启用 SACK 的会话启用丢失重传检测，默认启用。在严重拥塞下，重传可能丢失，进而导致强制性重传超时（RTO），随后是慢启动。LRD 会尝试重发反复丢失的数据包，防止耗时 RTO 和降低性能的慢启动或 SACK 计分板清除。

**`sack.maxholes`** 每连接的最大 SACK 孔数。默认为 128。

**`sack.revised`** 启用 RFC6675 中的三种更新机制（默认为 true）。使用 RFC 6675 中描述的算法计算在途字节数，并在启用比例速率减少时也是改进。其次，当传输的尾部段丢失且没有额外数据准备发送时，Rescue Retransmission 有助于及时丢失恢复。如果 SACK 丢失恢复期间收到不带 SACK 块的部分 ACK，则立即重传尾部段，而不是等待重传超时。最后，当两个段加一字节被 SACK 时，即使未观察到传统重复 ACK，也会启用 SACK 丢失恢复。`sack.revised` 已弃用，将在 FreeBSD 16 中移除。`sack.enable` 将始终遵循 RFC6675。

**`sendbuf_auto`** 启用自动发送缓冲区大小调整。

**`sendbuf_auto_lowat`** 修改自动发送缓冲区增长阈值以考虑 `SO_SNDLOWAT`。

**`sendbuf_inc`** 自动发送缓冲区的增量步长。

**`sendbuf_max`** 自动发送缓冲区的最大大小。

**`sendspace`** 初始 TCP 发送窗口（缓冲区大小）。

**`syncache`** `net.inet.tcp.syncache` 节点下的变量记录在 [syncache(4)](syncache.4.md) 中。

**`syncookies`** 确定是否为出站 SYN-ACK 数据包生成 SYN cookie。SYN cookie 在 SYN flood 攻击期间是巨大的帮助，默认启用。（参见 syncookies(4)）

**`syncookies_only`** 参见 syncookies(4)。

**`tcbhashsize`** TCP 控制块哈希表大小（只读）。使用内核选项 `TCBHASHSIZE` 或在 [loader(8)](../man8/loader.8.md) 中设置 `net.inet.tcp.tcbhashsize` 调整。

**`tolerate_missing_ts`** 容忍已协商 TCP 时间戳支持的 TCP 连接的 TCP 段缺少时间戳（RFC 1323/RFC 7323）。截至 2021 年 6 月，已知多个 TCP 栈违反 RFC 7323，包括广泛部署的现代栈。因此默认为 1，即容忍缺少时间戳。

**`ts_offset_per_conn`** 初始化 TCP 时间戳时，使用每连接偏移而非每主机对偏移。默认使用 RFC 7323 中建议的每连接偏移。

**`tso`** 启用 TCP 分段卸载。

**`udp_tunneling_overhead`** 使用 UDP 封装时考虑的开销。由于中间盒的 MSS 钳制很可能不起作用，因此也支持大于 8（UDP 头大小）的值。支持的值在 8 到 1024 之间。默认为 8。

**`udp_tunneling_port`** 本地 UDP 封装端口。值为 0 表示禁用 UDP 封装。默认为 0。

**`v6mssdflt`** 当未从 MSS 协商中收到相反建议时，IPv6 的 TCP 最大段大小（“MSS”）的默认值。

**`v6pmtud_blackhole_mss`** 启用 PMTU 黑洞检测时 IPv6 要尝试的 MSS。参见 `pmtud_blackhole_detection`。

## 错误

套接字操作可能失败并返回以下错误之一：

**[Er EISCONN]** 当试图在已有连接的套接字上建立连接时；

**[Er ENOBUFS][Er ENOMEM]]]** 当系统内存不足以容纳内部数据结构时；

**[Er ETIMEDOUT]** 当连接因过度重传而被丢弃时；

**[Er ECONNRESET]** 当远程对端强制关闭连接时；

**[Er ECONNREFUSED]** 当远程对端主动拒绝建立连接时（通常因为没有进程监听该端口）；

**[Er EADDRINUSE]** 当尝试使用已分配的端口创建套接字时；

**[Er EADDRNOTAVAIL]** 当尝试为没有网络接口的网络地址创建套接字时；

**[Er EAFNOSUPPORT]** 当尝试将套接字绑定或连接到多播地址时。

**[Er EINVAL]** 当尝试在会话的无效点更改 TCP 功能块时；

**[Er ENOENT]** 当尝试使用不可用的 TCP 功能块时；

## 参见

getsockopt(2), setfib(2), socket(2), [stats(3)](../man3/stats.3.md), sysctl(3), [blackhole(4)](blackhole.4.md), [dtrace_mib(4)](dtrace_mib.4.md), [inet(4)](inet.4.md), [intro(4)](intro.4.md), [ip(4)](ip.4.md), [ktls(4)](ktls.4.md), [mod_cc(4)](mod_cc.4.md), [siftr(4)](siftr.4.md), [syncache(4)](syncache.4.md), [tcp_bbr(4)](tcp_bbr.4.md), [tcp_rack(4)](tcp_rack.4.md), setkey(8), [sysctl(8)](../man8/sysctl.8.md), [tcp_functions(9)](../man9/tcp_functions.9.md)

> V. Jacobson, B. Braden, D. Borman, "TCP Extensions for High Performance", RFC 1323.

> D. Borman, B. Braden, V. Jacobson, R. Scheffenegger, "TCP Extensions for High Performance", RFC 7323.

> A. Heffernan, "Protection of BGP Sessions via the TCP MD5 Signature Option", RFC 2385.

> K. Ramakrishnan, S. Floyd, D. Black, "The Addition of Explicit Congestion Notification (ECN) to IP", RFC 3168.

> A. Ramaiah, R. Stewart, M. Dalal, "Improving TCP's Robustness to Blind In-Window Attacks", RFC 5961.

> F. Gont, "Reducing the TIME-WAIT State Using TCP Timestamps", RFC 6191.

## 历史

TCP 协议出现于 4.2BSD。RFC 1323 中用于窗口缩放和时间戳的扩展添加于 4.4BSD。`TCP_INFO` 选项在 Linux 2.6 中引入，且*可能更改*。
