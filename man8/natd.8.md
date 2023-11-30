  NATD(8)  

NATD(8)

FreeBSD System Manager's Manual

NATD(8)

[名称](#__u540D___u79F0_)
=======================

`natd` —

网络地址转换守护进程

[概要](#__u6982___u8981_)
=======================

`natd` \[`-unregistered_only` | `-u`\] \[`-log` | `-l`\] \[`-proxy_only`\] \[`-reverse`\] \[`-deny_incoming` | `-d`\] \[`-use_sockets` | `-s`\] \[`-same_ports` | `-m`\] \[`-verbose` | `-v`\] \[`-dynamic`\] \[`-in_port` | `-i` port\] \[`-out_port` | `-o` port\] \[`-port` | `-p` port\] \[`-alias_address` | `-a` address\] \[`-target_address` | `-t` address\] \[`-interface` | `-n` interface\] \[`-proxy_rule` proxyspec\] \[`-redirect_port` linkspec\] \[`-redirect_proto` linkspec\] \[`-redirect_address` linkspec\] \[`-config` | `-f` configfile\] \[`-instance` instancename\] \[`-globalport` port\] \[`-log_denied`\] \[`-log_facility` facility\_name\] \[`-punch_fw` firewall\_range\] \[`-skinny_port` port\] \[`-log_ipfw_denied`\] \[`-pid_file` | `-P` pidfile\] \[`-exit_delay` | `-P` ms\]

[描述](#__u63CF___u8FF0_)
=======================

`natd` 实用程序提供了一个网络地址转换工具，用于在 FreeBSD 下与 divert(4) 套接字一起使用。

（如果您需要在 PPP 链接上进行 NAT， ppp(8) 提供了 `-nat` 选项，该选项提供了大部分 `natd` 功能，并使用相同的 libalias(3) 库。)

`natd` 实用程序通常作为守护程序在后台运行。 它在原始 IP 数据包进出机器时被传递，并且可能会在将它们重新注入 IP 数据包流之前对其进行更改。

它会更改所有发往另一台主机的数据包，以便它们的源 IP 地址是当前机器的源 IP 地址。 对于以这种方式更改的每个数据包，都会创建一个内部表条目来记录这一事实。 源端口号也被更改以指示应用于数据包的表条目。 根据该内部表检查使用当前主机的目标 IP 接收的数据包。 如果找到条目，则使用它来确定正确的目标 IP 地址和端口以放入数据包中。

以下命令行选项可用：

[`-log`](#log) | [`-l`](#l)

将各种别名统计信息和信息记录到文件 /var/log/alias.log 中。 每次启动 `natd` 时都会截断此文件。

[`-deny_incoming`](#deny_incoming) | [`-d`](#d)

不要传递在内部转换表中没有条目的传入数据包。

如果不使用此选项，则将使用下面的 `-target_address` 中的规则更改此类数据包，并且将在内部转换表中创建条目。

[`-log_denied`](#log_denied)

通过 syslog(3) 记录被拒绝的传入数据包（另请参见 `-log_facility` ) 。

[`-log_facility`](#log_facility) facility\_name

通过 syslog(3) 记录信息时使用指定的日志工具。 参数 facility\_name 是 syslog.conf(5) 中指定的关键字之一。

[`-use_sockets`](#use_sockets) | [`-s`](#s)

分配一个 socket(2)-
以建立 FTP 数据或 IRC DCC 发送连接。 此选项使用更多系统资源，但在端口号冲突时保证连接成功。

[`-same_ports`](#same_ports) | [`-m`](#m)

更改传出数据包时尝试保持相同的端口号。 使用此选项，诸如 RPC 之类的协议将有更好的工作机会。 如果无法维护端口号，它将按正常方式静默更改。

[`-verbose`](#verbose) | [`-v`](#v)

不要在启动时调用 daemon(3) 。相反，保持连接到控制终端并将所有数据包更改显示到标准输出。此选项应仅用于调试目的。

[`-unregistered_only`](#unregistered_only) | [`-u`](#u)

仅更改具有未注册 _unregistered_ 的传出数据包。 根据 RFC 1918，未注册的源地址为 10.0.0.0/8、172.16.0.0/12 和 192.168.0.0/16。

[`-redirect_port`](#redirect_port) proto targetIP:targetPORT\[-targetPORT\] \[aliasIP:\]aliasPORT\[-aliasPORT\] \[remoteIP\[:remotePORT\[-remotePORT\]\]\]

将到达给定端口的传入连接重定向到另一个主机和端口。 参数 proto 是 tcp 或 udp, targetIP 是所需的目标 IP 地址， targetPORT 是所需的目标端口号或范围， aliasPORT 是请求的端口号或范围， aliasIP 是别名地址。 如有必要，参数 remoteIP 和 remotePORT 可用于更准确地指定连接。 如果未指定 remotePORT ，则假定为所有端口。

参数 targetIP, aliasIP 和 remoteIP 可以作为 IP 地址或主机名给出。 targetPORT, aliasPORT 和 remotePORT 范围在数字上不必相同，但必须具有相同的大小。 当 targetPORT, aliasPORT 或 remotePORT 指定一个奇异值（不是范围）时，它可以作为在 services(5) 数据库中搜索的服务名称给出。

例如，论据

`tcp inside1:telnet 6666`

表示发往该机器上端口 6666 的传入 TCP 数据包将被发送到 inside1 机器上的 telnet 端口。

`tcp inside2:2300-2399 3300-3399`

将端口 3300-3399 上的传入连接重定向到主机 inside2，端口 2300-2399。 映射是 1:1 表示端口 3300 映射到 2300，3301 映射到 2301，等等。

[`-redirect_proto`](#redirect_proto) proto localIP \[publicIP \[remoteIP\]\]

将目标为 publicIP 地址的协议 proto (请参阅 protocols(5)) 的传入 IP 数据包重定向到 localIP 地址，反之亦然。

如果未指定 publicIP ，则使用默认别名地址。 如果指定了 remoteIP ，那么只有来自/到 remoteIP 的数据包才会匹配该规则。

[`-redirect_address`](#redirect_address) localIP publicIP

将公共 IP 地址的流量重定向到本地网络上的计算机。 此功能称为 _static NAT_ 。 如果您的 ISP 为您分配了一小块 IP 地址，通常静态 NAT 很有用，但它甚至可以用于单个地址的情况：

`redirect_address 10.0.0.8 0.0.0.0`

上述命令会将所有传入流量重定向到机器 10.0.0.8。

如果多个地址别名指定同一个公共地址如下

redirect\_address 192.168.0.2 public\_addr redirect\_address 192.168.0.3 public\_addr redirect\_address 192.168.0.4 public\_addr 

传入流量将被定向到最后转换的本地地址 (192.168.0.4)，但来自前两个地址的传出流量仍将通过别名出现在指定的 public\_addr 中。

[`-redirect_port`](#redirect_port_2) proto targetIP:targetPORT\[,targetIP:targetPORT\[,...\]\] \[aliasIP:\]aliasPORT \[remoteIP\[:remotePORT\]\]

[`-redirect_address`](#redirect_address_2) localIP\[,localIP\[,...\]\] publicIP

这些形式的 `-redirect_port` 和 `-redirect_address` 用于透明地卸载单个服务器上的网络负载并在服务器池中分配负载。 此功能称为 _LSNAT_ (RFC 2391)。例如，论据

`tcp www1:http,www2:http,www3:http www:http`

意味着对主机 www 的传入 HTTP 请求将透明地重定向到 www1、www2 或 www3 之一，其中主机只是在循环的基础上选择的，而不考虑网络上的负载。

[`-dynamic`](#dynamic)

如果使用了 `-n` 或 `-interface` 选项， `natd` 将监视路由套接字以了解对传递的 interface 的更改。 如果接口的 IP 地址发生变化， `natd` 将动态改变其别名地址的概念。

[`-in_port`](#in_port) | [`-i`](#i) port

读取和写入 divert(4) 端口 port, 将所有数据包视为 “incoming” 。

[`-out_port`](#out_port) | [`-o`](#o) port

读取和写入 divert(4) 端口 port, 将所有数据包视为 “outgoing” 。

[`-port`](#port) | [`-p`](#p) port

读取和写入 divert(4) 端口 port, 使用 divert(4) 中指定的规则将数据包区分为 “incoming” 和 “outgoing” 。 如果 port 不是数字，则在 services(5) 数据库中搜索。 如果未指定此选项，将使用名为 natd 的转移端口作为默认值。

[`-alias_address`](#alias_address) | [`-a`](#a) address

使用 address 为别名地址。 如果未指定 `-proxy_only` 选项，则必须使用此选项或 `-interface` 选项（但不能同时使用两者）。 指定的地址通常是分配给 “public” 网络接口的地址。

所有 _out_ 的数据都将被重写为源地址等于 address 。 将检查所有 _in_ 的数据以查看它是否与任何已别名的传出连接匹配。 如果是，则相应地更改数据包。 如果不是，则检查所有 `-redirect_port`, `-redirect_proto` 和 `-redirect_address` 分配并采取行动。 如果无法进行其他操作并且未指定 `-deny_incoming` ，则使用以下 `-target_address` 选项中指定的规则将数据包传递到本地计算机。

[`-t`](#t) | [`-target_address`](#target_address) address

设置目标地址。 当与任何预先存在的链接无关的传入数据包到达主机时，它将被发送到指定的 address 。

目标地址可以设置为 255.255.255.255 ，在这种情况下，所有新传入的数据包都会转到 `-alias_address` 或 `-interface` 设置的别名地址。

如果不使用此选项，或使用参数 0.0.0.0 调用此选项，则所有新传入的数据包都会转到数据包中指定的地址。 如果外部机器可以将数据包路由到相关机器，这允许外部机器直接与内部机器对话。

[`-interface`](#interface) | [`-n`](#n) interface

使用 interface 确定别名地址。 如果与 interface 关联的 IP 地址可能会更改，则还应使用 `-dynamic` 选项。 如果未指定此选项，则必须使用 `-alias_address` 选项。

指定的 interface 通常是 “public” (或 “external”) 网络接口。

[`-config`](#config) | [`-f`](#f) file

从 file 中读取配置。 file 应该包含一个选项列表，每行一个，格式与上述命令行选项的长格式相同。 例如，

`alias_address 158.152.17.1`

将指定别名地址 158.152.17.1。 不带参数的选项在配置文件中用 yes 或 no 参数指定。例如，

`log yes`

与 `-log` 同义。

选项可以分为几个部分。 每个部分都适用于自己的 `natd` 实例。 此功能允许为多个 NAT 实例配置一个 `natd` 进程。 始终存在的第一个实例是 "default" 实例。每个另一个实例都应该以

`instance instance_name`

在下一个应该放置一个配置选项。例子：

`# default instance`

`port 8668`

`alias_address 158.152.17.1`

`# second instance`

`instance dsl1`

`port 8888`

`alias_address 192.168.0.1`

尾随空格和空行被忽略。 ‘`#`’ 符号将把该行的其余部分标记为注释。

[`-instance`](#instance) instancename

此选项切换命令行选项处理以配置实例 instancename （必要时创建它），直到下一个 `-instance` 选项或命令行结束。 在使用 `-config` 选项指定的配置文件中设置多个实例比在命令行上更容易。

[`-globalport`](#globalport) port

读取和写入 divert(4) 端口 port ，将所有数据包视为 “outgoing” 。 此选项旨在与多个实例一起使用：在此端口上接收的数据包将根据每个配置实例的内部转换表进行检查。 如果找到条目，则根据该条目对数据包进行别名。 如果在任何实例中都没有找到条目，则数据包原封不动地传递，并且不会创建新条目。 有关更多详细信息，请参阅 [多个实例](#__u591A___u4E2A___u5B9E___u4F8B_) 部分。

[`-reverse`](#reverse)

此选项使 `natd` 反转它处理 “incoming” 和 “outgoing” 数据包的方式，允许它在 “internal” 网络接口而不是 “external” 网络接口上运行。

当传出流量被重定向到本地机器并且 `natd` 在内部接口上运行（它通常在外部接口上运行）时，这在某些透明代理情况下很有用。

[`-proxy_only`](#proxy_only)

强制 `natd` 仅执行透明代理。 不执行正常的地址转换。

[`-proxy_rule`](#proxy_rule) \[type encode\_ip\_hdr | encode\_tcp\_stream\] port xxxx server a.b.c.d:yyyy

启用透明代理。 通过该主机到任何其他主机的具有给定端口的传出 TCP 数据包被重定向到给定的服务器和端口。 可选地，可以将原始目标地址编码到数据包中。 使用 encode\_ip\_hdr 将此信息放入 IP 选项字段或使用 encode\_tcp\_stream 将数据注入 TCP 流的开头。

[`-punch_fw`](#punch_fw) basenumber:count

此选项指示 `natd` 在基于 ipfirewall(4) 的防火墙中为 FTP/IRC DCC 连接 “punch holes” 。 这是通过安装允许特定连接（并且仅该连接）通过防火墙的临时防火墙规则来动态完成的。 一旦相应的连接终止，规则就会被删除。

从规则编号 basenumber 开始的最大 count 规则将用于打防火墙孔。 启动时将清除所有规则的范围。 当内核处于安全级别 3 时，此选项无效，有关详细信息，请参阅 init(8) 。

[`-skinny_port`](#skinny_port) port

此选项允许您指定用于 Skinny Station 协议的 TCP 端口。 思科 IP 电话使用 Skinny 与思科呼叫管理器进行通信，以设置 IP 语音呼叫。 默认情况下，不执行 Skinny 别名。 Skinny 的典型端口值为 2000。

[`-log_ipfw_denied`](#log_ipfw_denied)

当由于 ipfw(8) 规则阻止数据包而无法重新注入数据包时记录。 这是 `-verbose` 的默认设置。

[`-pid_file`](#pid_file) | [`-P`](#P) file

指定用于存储进程 ID 的备用文件。 默认值为 /var/run/natd.pid 。

[`-exit_delay`](#exit_delay) ms

指定信号后守护进程退出前的延迟（毫秒）。 默认值为 10000 。

[运行 NATD](#__u8FD0___u884C__NATD)
=================================

在尝试运行 `natd` 之前，需要执行以下步骤：

1.  使用以下选项构建自定义内核：
    
    options IPFIREWALL options IPDIVERT 
    
    有关构建自定义内核的详细说明，请参阅手册。
    
2.  确保您的机器充当网关。 这可以通过指定行来完成
    
    `gateway_enable=YES`
    
    在 /etc/rc.conf 文件中或使用命令
    
    `sysctl net.inet.ip.forwarding=1`
    
3.  如果您使用 `-interface` 选项，请确保您的接口已配置。 例如，如果您希望指定 ‘`tun0`’ 作为 interface ，并您在该接口上使用 ppp(8) ，您必须确保在启动 `natd` 之前启动 `ppp` 。

运行 `natd` 相当简单。

`natd -interface ed0`

在大多数情况下就足够了（替换正确的接口名称）。 请检查 rc.conf(5) 以了解如何将其配置为在引导期间自动启动。 一旦 `natd` 运行，您必须确保将流量转移到 `natd`:

1.  您将需要调整 /etc/rc.firewall 脚本以适应口味。 如果您对拥有防火墙不感兴趣，可以使用以下几行：
    
    /sbin/ipfw -f flush /sbin/ipfw add divert natd all from any to any via ed0 /sbin/ipfw add pass all from any to any 
    
    第二行取决于您的界面（根据需要更改 ‘`ed0`’ )。
    
    您应该知道，通过这些防火墙设置，您本地网络上的每个人都可以使用您的主机作为网关来伪造他的源地址。 如果您的本地网络上有其他主机，强烈建议您创建防火墙规则，只允许进出受信任主机的流量。
    
    如果您指定真正的防火墙规则，最好在脚本的开头指定第 2 行，以便 `natd` 在所有数据包被防火墙丢弃之前看到它们。
    
    经过 `natd` 转换后，数据包在导致转移的规则编号之后的规则编号处重新进入防火墙（如果有多个相同编号的规则，则不是下一条规则）。
    
2.  通过设置启用防火墙
    
    `firewall_enable=YES`
    
    在 /etc/rc.conf 中。 这告诉系统启动脚本运行 /etc/rc.firewall-
    脚本。 如果您现在不想重新启动，只需从控制台手动运行它。 除非您将其置于后台，否则切勿从远程会话中运行它。 如果这样做，您将在刷新发生后将自己锁定，并且 /etc/rc.firewall 的执行将在此时停止 - 永久阻止所有访问。 在后台运行脚本应该足以防止这场灾难。
    

[多个实例](#__u591A___u4E2A___u5B9E___u4F8B_)
=========================================

需要为多个外部 IP 地址设置别名的情况并不少见。 虽然传统上这是通过运行多个具有独立配置的 `natd` 进程来实现的，但 `natd` 可以在单个进程中拥有多个别名实例，这也允许它们彼此不那么独立。 例如，让我们看看在具有两个外部接口 ‘`sis0`’ (with IP 1.2.3.4) 和 ‘`sis2`’ (with IP 2.3.4.5) 的机器上对不同供应商的两个通道进行负载平衡的常见任务：

 net 1.2.3.0/24 1.2.3.1 ------------------ sis0 (router) (1.2.3.4) net 10.0.0.0/24 sis1 ------------------- 10.0.0.2 (10.0.0.1) net 2.3.4.0/24 2.3.4.1 ------------------ sis2 (router) (2.3.4.5) 

默认路由通过 ‘`sis0`’ 输出。

内部机器 (10.0.0.2) 可通过两个外部 IP 在 TCP 端口 122 上访问，并且传出连接在 ‘`sis0`’ 和 ‘`sis2`’ 之间随机选择路径。

它的工作方式是 natd.conf 构建别名引擎的两个实例。

除了这些实例的私有 divert(4) 套接字之外，还创建了第三个名为 “globalport” 的套接字；通过这个发送到 `natd` 的数据包将与所有实例匹配并在找到现有条目时进行转换，如果未找到条目则保持不变。 以下行被放入 /etc/natd.conf:

log deny\_incoming verbose instance default interface sis0 port 1000 redirect\_port tcp 10.0.0.2:122 122 instance sis2 interface sis2 port 2000 redirect\_port tcp 10.0.0.2:122 122 globalport 3000 

并使用以下 ipfw(8) 规则：

ipfw -f flush ipfw add allow ip from any to any via sis1 ipfw add skipto 1000 ip from any to any in via sis0 ipfw add skipto 2000 ip from any to any out via sis0 ipfw add skipto 3000 ip from any to any in via sis2 ipfw add skipto 4000 ip from any to any out via sis2 ipfw add 1000 count ip from any to any ipfw add divert 1000 ip from any to any ipfw add allow ip from any to any ipfw add 2000 count ip from any to any ipfw add divert 3000 ip from any to any ipfw add allow ip from 1.2.3.4 to any ipfw add skipto 5000 ip from 2.3.4.5 to any ipfw add prob .5 skipto 4000 ip from any to any ipfw add divert 1000 ip from any to any ipfw add allow ip from any to any ipfw add 3000 count ip from any to any ipfw add divert 2000 ip from any to any ipfw add allow ip from any to any ipfw add 4000 count ip from any to any ipfw add divert 2000 ip from any to any ipfw add 5000 fwd 2.3.4.1 ip from 2.3.4.5 to not 2.3.4.0/24 ipfw add allow ip from any to any 

在这里，从内部网络到 Internet 的数据包通过 ‘`sis0`’ （规则号 2000）发出并被 `globalport` 套接字（3000）捕获。 之后，要么在两个实例之一的转换表中找到匹配项，要么以相同的概率将数据包传递到另外两个 divert(4) 端口（1000 或 2000）之一。 这确保了负载平衡是在每个流的基础上完成的（即，来自单个 TCP 连接的数据包总是流经相同的接口）。 具有非默认接口 (‘`sis2`’) 的源 IP 的已转换数据包被转发到该接口上的相应路由器。

[参见](#__u53C2___u89C1_)
=======================

libalias(3), divert(4), protocols(5), rc.conf(5), services(5), syslog.conf(5), init(8), ipfw(8), ppp(8)

[历史](#__u5386___u53F2_)
=======================

`natd` 实用程序出现在 FreeBSD 3.0 中。

[作者](#__u4F5C___u8005_)
=======================

这个计划是许多人在不同时期努力的结果：

Archie Cobbs <[archie@FreeBSD.org](mailto:archie@FreeBSD.org)\> (转移套接字) Charles Mott <[cm@linktel.net](mailto:cm@linktel.net)\> (数据包别名) Eivind Eklund <[perhaps@yes.no](mailto:perhaps@yes.no)\> (IRC 支持和其他补充) Ari Suutari <[suutari@iki.fi](mailto:suutari@iki.fi)\> (natd) Dru Nelson <[dnelson@redwoodsoft.com](mailto:dnelson@redwoodsoft.com)\> (早期 PPTP 支持) Brian Somers <[brian@awfulhak.org](mailto:brian@awfulhak.org)\> (glue) Ruslan Ermilov <[ru@FreeBSD.org](mailto:ru@FreeBSD.org)\> (natd, packet aliasing, glue) Poul-Henning Kamp <[phk@FreeBSD.org](mailto:phk@FreeBSD.org)\> (多个实例)

October 5, 2016

FreeBSD 13.1-RELEASE