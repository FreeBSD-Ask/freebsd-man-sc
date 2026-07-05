# sctp.4

`sctp` — Internet Stream Control Transmission Protocol（互联网流控制传输协议）

## 名称

`sctp`

## 概要

`options SCTP options SCTP_SUPPORT`

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

`Ft int Fn socket AF_INET SOCK_STREAM IPPROTO_SCTP Ft int Fn socket AF_INET SOCK_SEQPACKET IPPROTO_SCTP`

## 描述

SCTP 协议提供可靠、流量控制的双向数据传输。它是面向消息的协议，可支持 `SOCK_STREAM` 和 `SOCK_SEQPACKET` 抽象。SCTP 使用标准 Internet 地址格式，此外还提供每主机的“port addresses”（端口地址）集合。因此，每个地址由指定主机和网络的 Internet 地址组成，主机上的特定 SCTP 端口标识对端实体。

SCTP 中有两种编程模型。第一种使用 `SOCK_STREAM` 抽象。在此抽象中，使用 SCTP 协议的套接字是“active”（主动）或“passive”（被动）的。主动套接字向被动套接字发起连接。默认情况下，SCTP 套接字创建为主动；要创建被动套接字，必须在使用 bind(2) 或 sctp_bindx(3) 系统调用绑定套接字后使用 listen(2) 系统调用。只有被动套接字可使用 accept(2) 调用接受传入连接。只有主动套接字可使用 connect(2) 调用发起连接。

另一个抽象 `SOCK_SEQPACKET` 提供“connectionless”（无连接）操作模式，用户可以向某地址发送（使用任何携带套接字地址的有效发送调用），关联将由底层 SCTP 传输栈隐式建立。此抽象是唯一能够在四次握手的第三段发送数据的抽象。用户仍必须调用 listen(2) 以允许套接字接受连接。但调用 listen(2) 并不限制用户仍可向其他对端发起隐式连接。

SCTP 协议直接支持多宿主。因此，当使用“通配符”地址 `INADDR_ANY` 绑定套接字时，SCTP 栈将通知对端关于被认为在对端范围内的所有本地地址。对端随后可能有多条路径到达本地主机。

SCTP 传输协议还是多流的。多流是指发送子有序消息流的能力。用户通过在某个扩展发送调用（如 sctp_send(3) 函数调用）中指定特定流来执行此操作。在不同流上发送消息将允许并行交付数据，即流 1 中的消息丢失不会阻止流 2 中发送的消息的交付。

SCTP 传输协议还提供无序服务。无序服务允许发送和交付消息而不考虑任何其他消息的顺序。

SCTP 内核实现可以编译进内核，或作为模块动态加载。要支持栈的动态加载，内核必须使用 `options SCTP_SUPPORT` 编译。

### 扩展

FreeBSD 的 SCTP 实现还支持以下扩展：

**sctp** 部分可靠性 此扩展允许根据用户指定的参数跳过消息并不予交付。

**sctp** 动态寻址 此扩展允许从现有关联中动态添加和删除地址。

**sctp** 认证 此扩展允许用户认证特定对端块（包括数据），以验证发送消息的对端确实是建立关联的对端。还提供共享密钥选项，使两个栈可以预共享密钥。

**packet** drop 某些路由器支持一种特殊的卫星协议，会报告因损坏导致的丢失。这允许重传而不会后续损失带宽利用率。

**stream** reset 此扩展允许任一侧的用户重置任何或所有流使用的流序列号。

### 套接字选项

SCTP 支持多个套接字选项，可使用 setsockopt(2) 设置，使用 getsockopt(2) 或 sctp_opt_info(3) 测试：

**`SCTP_NODELAY`** 在大多数情况下，SCTP 在数据呈现时即发送；当有未确认的未完成数据时，它会收集少量输出，在收到确认后一次发送单个数据包。对于某些客户端（如发送一系列鼠标事件但无回复的窗口系统），这种打包可能导致显著延迟。布尔选项 `SCTP_NODELAY` 禁用此算法。

**`SCTP_RTOINFO`** 此选项返回有关关联“Retransmission Time Out”（重传超时）的特定信息。也可用于更改默认值。

**`SCTP_ASSOCINFO`** 此选项返回有关请求的关联的特定信息。

**`SCTP_INITMSG`** 此选项允许在隐式建立关联时获取或设置默认发送参数。它允许更改诸如允许入站的最大流数和向对端请求的流数等内容。

**`SCTP_AUTOCLOSE`** 对于一对多模型（`SOCK_SEQPACKET`），关联是隐式建立的。此选项允许用户指定允许关联维持的默认空闲秒数。空闲计时器（其中未发送或未从对端接收到用户消息）后，关联将被优雅关闭。此值的默认值为 0，即无限制（即不自动关闭）。

**`SCTP_SET_PEER_PRIMARY_ADDR`** 动态地址扩展允许对端请求将其某个地址设为主地址。此选项允许调用方向对端发出此类请求。注意，如果对端不同样支持动态地址扩展，此调用将失败。注意调用方必须提供在关联建立期间或动态告知对端的有效本地地址。

**`SCTP_PRIMARY_ADDR`** 此选项允许设置调用方希望发送到的主地址。调用方提供要设为主地址的对端地址。

**`SCTP_ADAPTATION_LAYER`** 动态地址扩展还允许用户在关联建立时传递 32 位不透明值。此选项允许用户设置或获取此值。

**`SCTP_DISABLE_FRAGMENTS`** 默认情况下，SCTP 会将用户消息分片为适合网络的多个片段，然后在接收时将片段重组为单个用户消息。如果改为启用此选项，则任何超过路径最大传输单元（P-MTU）的发送都将失败，且消息不会发送。

**`SCTP_PEER_ADDR_PARAMS`** 此选项允许用户设置或获取特定对端地址参数。

**`SCTP_DEFAULT_SEND_PARAM`** 当用户不使用某个扩展发送调用（例如 sctp_sendmsg(3)）时，一组默认值应用于每次发送。这些值包括发送到的流号以及每协议 ID 等内容。此选项允许调用方获取和设置这些值。如果用户更改了这些默认值，则每当发送方未提供信息时（即使用非扩展 API），这些新值将用作默认值。

**`SCTP_EVENTS`** SCTP 有非数据事件可以传达给应用程序。默认情况下这些都被禁用，因为它们到达数据路径时在接收到的消息上设置了特殊标志 `MSG_NOTIFICATION`。此选项允许调用方获取当前正在接收的事件以及设置他们可能感兴趣的接收的不同事件。

**`SCTP_I_WANT_MAPPED_V4_ADDR`** SCTP 同时支持 IPV4 和 IPV6。由于 SCTP 是多宿主的，关联可以跨 IPV4 和 IPV6 地址。默认情况下，当打开 IPV6 套接字时，当数据从对端的 V4 地址到达套接字时，V4 地址将以地址族 AF_INET 呈现。如果不希望如此，则可以启用此选项，将所有 V4 地址转换为映射的 V6 表示。

**`SCTP_MAXSEG`** 默认情况下，SCTP 根据对端的最小 P-MTU 选择消息分片点。此选项允许调用方将其设置为更小的值。注意，虽然用户可以更改此值，但如果 P-MTU 小于用户设置的值，则 P-MTU 值将覆盖任何用户设置。

**`SCTP_DELAYED_SACK`** 此选项允许用户设置和获取 SCTP 使用的延迟确认时间（以毫秒为单位）和确认频率。默认延迟确认时间为 200 毫秒，默认确认频率为 2。

**`SCTP_PARTIAL_DELIVERY_POINT`** SCTP 有时需要在整个消息到达之前开始交付非常大的消息。默认情况下，SCTP 等待直到传入消息大于接收缓冲区的四分之一。此选项允许用较小的值覆盖栈值。

**`SCTP_FRAGMENT_INTERLEAVE`** SCTP 有时会开始部分交付（如上所述）。在正常情况下，连续读取将继续返回消息的其余部分，必要时阻塞，直到读取该消息的全部。然而，这意味着其他消息可能已到达并准备好交付，但被阻塞在部分交付的消息之后。如果启用此选项，当部分交付的消息没有更多数据要接收时，则后续读取可能返回准备交付的不同消息。默认情况下此选项关闭，因为用户必须使用扩展 API 才能区分消息（通过流和流序列号）。

**`SCTP_AUTH_CHUNK`** 默认情况下仅认证动态寻址块。此选项允许用户请求额外认证某个块。注意，对此选项的连续调用将起作用并继续添加需要认证的更多块。注意此选项仅影响未来的关联，不影响现有关联。

**`SCTP_AUTH_KEY`** 此选项允许用户指定共享密钥，稍后可用于认证对端。

**`SCTP_HMAC_IDENT`** 此选项允许获取或设置用于认证对端的 HMAC 算法列表。注意 HMAC 值按优先级顺序排列，第一个 HMAC 标识符是最首选的，最后一个是最不首选的。

**`SCTP_AUTH_ACTIVE_KEY`** 此选项允许激活密钥以生成认证信息。注意对端必须具有相同密钥，否则数据将被丢弃。

**`SCTP_AUTH_DELETE_KEY`** 此选项允许删除旧密钥。

**`SCTP_USE_EXT_RECVINFO`** sockets api 文档允许使用扩展的发送/接收信息结构。扩展结构包括与下一条要接收的消息（在当前接收完成后）相关的附加字段（如果已知此类信息）。默认情况下系统不传递此信息。此选项允许用户请求此信息。

**`SCTP_AUTO_ASCONF`** 默认情况下，当绑定到所有地址且系统管理员启用了自动动态地址时，SCTP 栈会通过将此选项设置为 true 自动将地址更改生成为对任何对端的添加和删除请求。此选项允许端点禁用该行为。

**`SCTP_MAXBURST`** 默认情况下，SCTP 实现微突发控制，以便在拥塞窗口打开时不会产生大量数据包突发。默认突发限制为 4。此选项允许用户更改此值。

**`SCTP_CONTEXT`** 许多 sctp 扩展调用具有 context 字段。context 字段是 32 位不透明值，将在发送失败时返回。此选项允许调用方设置用户未提供时使用的默认 context 值。

**`SCTP_EXPLICIT_EOR`** 默认情况下，单次发送是一条完整消息。SCTP 生成隐含的记录边界。如果启用此选项，则所有发送都是同一消息的一部分，直到用户在 sctp_sndrcvinfo flags 字段中传递特殊标志 `SCTP_EOR` 指示记录结束。这实际上使所有发送成为同一消息的一部分，直到用户另行指定。这意味着调用方在 `SCTP_EOR` 传递给 SCTP 之前不得更改流号，否则将返回错误。

**`SCTP_STATUS`** 此选项是只读选项，返回有关指定关联的各种状态信息。

**`SCTP_GET_PEER_ADDR_INFO`** 此只读选项返回有关对端地址的信息。

**`SCTP_PEER_AUTH_CHUNKS`** 此只读选项返回对端要求认证的块列表。

**`SCTP_LOCAL_AUTH_CHUNKS`** 此只读选项返回必须认证的本地必需块列表。

**`SCTP_RESET_STREAMS`** 此套接字选项用于使一个流序列号或所有流序列号重置。注意对端 SCTP 端点也必须支持流重置扩展。

### MIB 变量

SCTP 协议在 sysctl(3) MIB 的 `net.inet.sctp` 分支中实现多个变量。

**`default_cc_module`** 默认拥塞控制模块。默认值为 0。最小值为 0，最大值为 3。值 0 启用默认拥塞控制算法。值 1 启用高速拥塞控制算法。值 2 启用 HTCP 拥塞控制算法。值 3 启用数据中心拥塞控制（DCCC）算法。

**`initial_cwnd`** 定义以 MTU 为单位的初始拥塞窗口大小。

**`cwnd_maxburst`** 发送时使用拥塞控制而非“盲”逻辑来限制最大突发。默认值为 1。可设置为 0 或 1。

**`ecn_enable`** 启用显式拥塞通知（ECN）。默认值为 1。可设置为 0 或 1。

**`rttvar_steady_step`** DCCC 尝试降低拥塞窗口所需的相同带宽测量次数。默认值为 20。最小值为 0，最大值为 65535。

**`rttvar_eqret`** 往返时间和带宽保持不变时 DCCC 是否减小拥塞窗口大小。默认值为 0。可设置为 0 或 1。

**`rttvar_bw`** DCCC 在往返时间计算中用于带宽平滑的位移量。默认值为 4。最小值为 0，最大值为 32。

**`rttvar_rtt`** DCCC 在往返时间计算中用于往返时间平滑的位移量。默认值为 5。最小值为 0，最大值为 32。

**`use_dcccecn`** 使用 DCCC 时启用 ECN。默认值为 1。可设置为 0 或 1。

**`getcred`** 获取 SCTP 连接的 ucred。

**`assoclist`** 活动 SCTP 关联列表。

**`stats`** SCTP 统计信息（struct sctp_stat）。

**`diag_info_code`** 诊断信息错误原因代码。

**`blackhole`** 启用 SCTP 黑洞。更多细节参见 [blackhole(4)](blackhole.4.md)。

**`sendall_limit`** 设置 SCTP_SENDALL 标志时可传输的最大消息大小（以字节为单位）。

**`buffer_splitting`** 启用发送/接收缓冲区拆分。

**`vtag_time_wait`** Vtag 等待时间（以秒为单位），0 禁用。

**`nat_friendly_init`** 在 INIT 上启用发送 NAT 友好的 SCTP 选项。

**`enable_sack_immediately`** 启用发送 SACK-IMMEDIATELY 位。

**`udp_tunneling_port`** 设置 SCTP/UDP 隧道端口。

**`mobility_fasthandoff`** 启用 SCTP 快速切换。

**`mobility_base`** 启用 SCTP 基础移动性

**`default_frag_interleave`** 默认片段交错级别。

**`default_ss_module`** 默认流调度模块。

**`log_level`** Ltrace/KTR 跟踪日志级别。

**`max_retran_chunk`** 关联中止前 DATA 块的重传次数。

**`min_residual`** 拆分第二部分中的最小残余数据块。

**`strict_data_order`** 强制严格数据排序，控制嵌入数据时中止。

**`abort_at_limit`** 一对一达到 qlimit 时中止。

**`hb_max_burst`** 确认心跳最大突发。

**`do_sctp_drain`** 系统内存 mbuf 不足时刷新接收队列中 TSN 高于累积 TSN 的块。

**`max_chained_mbufs`** 链上小 mbuf 的默认最大数量。

**`abc_l_var`** SCTP ABC 每个 SACK 最大增量（L）。

**`nat_friendly`** SCTP NAT 友好操作。

**`cmt_use_dac`** CMT DAC 开/关标志。

**`cmt_on_off`** CMT 设置。

**`outgoing_streams`** 默认出站流数。

**`incoming_streams`** 默认入站流数。

**`add_more_on_output`** 空间上何时值得尝试向套接字发送缓冲区添加更多内容。

**`path_pf_threshold`** 默认可能失败阈值。

**`path_rtx_max`** 每路径默认最大重传次数。

**`assoc_rtx_max`** 每关联默认最大重传次数。

**`init_rtx_max`** INIT 块默认最大重传次数。

**`valid_cookie_life`** 默认 cookie 生存期（以秒为单位）。

**`init_rto_max`** 关联建立期间默认最大重传超时（以 ms 为单位）。

**`rto_initial`** 默认初始重传超时（以 ms 为单位）。

**`rto_min`** 默认最小重传超时（以 ms 为单位）。

**`rto_max`** 默认最大重传超时（以 ms 为单位）。

**`secret_lifetime`** 默认密钥生存期（以秒为单位）。

**`shutdown_guard_time`** 关闭保护计时器（以秒为单位）（0 表示 5 倍 RTO.Max）。

**`pmtu_raise_time`** 默认 PMTU 提升计时器（以秒为单位）。

**`heartbeat_interval`** 默认心跳间隔（以 ms 为单位）。

**`asoc_resource`** 关联中缓存的最大资源数。

**`sys_resource`** 系统中缓存的最大资源数。

**`sack_freq`** 默认 SACK 频率。

**`delayed_sack_time`** 默认延迟 SACK 计时器（以 ms 为单位）。

**`chunkscale`** 用于缩放块和消息数量的可调参数。

**`min_split_point`** 拆分块时的最小大小。

**`pcbhashsize`** PCB 哈希表大小的可调参数。

**`tcbhashsize`** TCB 哈希表大小的可调参数。

**`maxchunks`** 每关联队列上的默认最大块数。

**`fr_maxburst`** 快速重传时 SCTP 端点的默认最大突发。

**`maxburst`** SCTP 端点的默认最大突发。

**`peer_chkoh`** 每发送一块从对端 rwnd 扣除的量。

**`strict_sacks`** 启用 SCTP 严格 SACK 检查。

**`pktdrop_enable`** 启用 SCTP PKTDROP。

**`nrsack_enable`** 启用 SCTP NR-SACK。

**`reconfig_enable`** 启用 SCTP RE-CONFIG。

**`asconf_enable`** 启用 SCTP ASCONF。

**`auth_enable`** 启用 SCTP AUTH。

**`pr_enable`** 启用 PR-SCTP。

**`auto_asconf`** 启用 SCTP Auto-ASCONF。

**`recvspace`** 最大入站 SCTP 缓冲区大小。

**`sendspace`** 最大出站 SCTP 缓冲区大小。

****拥塞**控制**

****其他****

## 参见

accept(2), bind(2), connect(2), listen(2), sctp_bindx(3), sctp_connectx(3), sctp_opt_info(3), sctp_recvmsg(3), sctp_sendmsg(3), [blackhole(4)](blackhole.4.md)

## 缺陷

`sctp` 内核模块无法卸载。
