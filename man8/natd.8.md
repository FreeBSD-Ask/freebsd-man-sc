# natd(8)

`natd` — 网络地址转换守护进程

## 名称

`natd`

## 概要

`natd [-unregistered_only | -u] [-log | -l] [-proxy_only] [-reverse] [-deny_incoming | -d] [-use_sockets | -s] [-same_ports | -m] [-udp_eim] [-verbose | -v] [-dynamic] [-in_port | -i port] [-out_port | -o port] [-port | -p port] [-alias_address | -a address] [-target_address | -t address] [-interface | -n interface] [-proxy_rule proxyspec] [-redirect_port linkspec] [-redirect_proto linkspec] [-redirect_address linkspec] [-config | -f configfile] [-instance instancename] [-globalport port] [-log_denied] [-log_facility facility_name] [-punch_fw firewall_range] [-skinny_port port] [-log_ipfw_denied] [-pid_file | -P pidfile] [-exit_delay | -P ms]`

## 描述

`natd` 工具提供了与 FreeBSD 下 [divert(4)](../man4/divert.4.md) 套接字配合使用的网络地址转换功能。

（如果你需要在 PPP 链路上进行 NAT，ppp(8) 提供了 `-nat` 选项，可实现 `natd` 的大部分功能，并使用相同的 libalias(3) 库。）

`natd` 工具通常作为守护进程在后台运行。它在原始 IP 数据包进出机器时接收它们，并可能在将它们重新注入 IP 数据包流之前对其进行更改。

它更改所有发往其他主机的数据包，使其源 IP 地址为当前机器的地址。对于以这种方式更改的每个数据包，都会创建一个内部表条目来记录此事实。源端口号也会被更改，以指示应用于该数据包的表条目。收到目标 IP 为当前主机的数据包时，将根据此内部表进行检查。如果找到条目，则使用它来确定要放入数据包的正确目标 IP 地址和端口。

以下命令行选项可用：

**`-log | -l`** 将各种别名统计信息记录到 **/var/log/alias.log** 文件。此文件在每次启动 `natd` 时被截断。

**`-deny_incoming | -d`** 不传递在内部转换表中没有条目的传入数据包。如果不使用此选项，则此类数据包将使用下文 `-target_address` 中的规则进行更改，并在内部转换表中创建条目。

**`-log_denied`** 通过 syslog(3) 记录被拒绝的传入数据包（另见 `-log_facility`）。

**`-log_facility`** `facility_name` 通过 syslog(3) 记录信息时使用指定的日志设施。参数 `facility_name` 是 syslog.conf(5) 中指定的关键字之一。

**`-use_sockets | -s`** 分配 socket(2) 以建立 FTP 数据或 IRC DCC 发送连接。此选项使用更多系统资源，但在端口号冲突时保证连接成功。

**`-same_ports | -m`** 尝试在更改传出数据包时保持相同的端口号。使用此选项，RPC 等协议将有更好的工作机会。如果无法保持端口号，将按正常方式静默更改。

**`-udp_eim`** 启用后，UDP 数据包使用 RFC 4787 的端点无关映射（EIM）（RFC 3489 的"全锥"NAT）。来自同一内部地址:端口的所有数据包都映射到相同的 NAT 地址:端口，无论其目标地址:端口如何。如果过滤规则允许，且 *deny_incoming* 被禁用，任何其他外部地址:端口也可以通过其映射的 NAT 地址:端口向该内部地址:端口发送数据。这与应用程序更兼容，可以减少端口转发的需要，但可扩展性较差，因为每个 NAT 地址:端口最多只能同时被一个内部地址:端口使用。禁用时，UDP 数据包使用端点相关映射（EDM）（"对称"NAT）。从特定内部地址:端口到不同外部地址:端口的每个连接都映射到随机且不可预测的 NAT 地址:端口。EDM NAT 后面的两个应用程序只能通过 NAT 上的端口转发或通过中间服务器隧道来相互连接。

**`-verbose | -v`** 启动时不调用 daemon(3)。而是保持附加到控制终端，并将所有数据包更改显示到标准输出。此选项仅用于调试目的。

**`-unregistered_only | -u`** 仅更改具有 *unregistered* 源地址的传出数据包。根据 RFC 1918，未注册源地址为 10.0.0.0/8、172.16.0.0/12 和 192.168.0.0/16。

**`-redirect_port`** `proto targetIP:targetPORT[-targetPORT] [aliasIP:]aliasPORT[-aliasPORT] [remoteIP[:remotePORT[-remotePORT]]]` 将到达给定端口的传入连接重定向到另一主机和端口。参数 `proto` 为 `tcp` 或 `udp`，`targetIP` 为所需的目标 IP 地址，`targetPORT` 为所需的目标端口号或范围，`aliasPORT` 为请求的端口号或范围，`aliasIP` 为别名地址。参数 `remoteIP` 和 `remotePORT` 可用于在必要时更精确地指定连接。如果未指定 `remotePORT`，则假定为所有端口。参数 `targetIP`、`aliasIP` 和 `remoteIP` 可以作为 IP 地址或主机名给出。`targetPORT`、`aliasPORT` 和 `remotePORT` 范围在数值上不必相同，但必须具有相同大小。当 `targetPORT`、`aliasPORT` 或 `remotePORT` 指定单个值（非范围）时，可以作为服务名给出，在 [services(5)](../man5/services.5.md) 数据库中搜索。例如，参数

```sh
tcp inside1:telnet 6666
```

表示发往本机端口 6666 的传入 TCP 数据包将被发送到 inside1 机器的 telnet 端口。

```sh
tcp inside2:2300-2399 3300-3399
```

将端口 3300-3399 上的传入连接重定向到主机 inside2 的端口 2300-2399。映射为 1:1，即端口 3300 映射到 2300，3301 映射到 2301，依此类推。

**`-redirect_proto`** `proto localIP [publicIP [remoteIP]]` 将发往 `publicIP` 地址的协议 `proto`（参见 [protocols(5)](../man5/protocols.5.md)）传入 IP 数据包重定向到 `localIP` 地址，反之亦然。如果未指定 `publicIP`，则使用默认别名地址。如果指定了 `remoteIP`，则只有来自/发往 `remoteIP` 的数据包才匹配规则。

**`-redirect_address`** `localIP publicIP` 将公共 IP 地址的流量重定向到本地网络上的机器。此功能称为 *静态 NAT*。通常，如果你的 ISP 为你分配了一小块 IP 地址，静态 NAT 很有用，但也可用于单地址情况：

```sh
redirect_address 10.0.0.8 0.0.0.0
```

上述命令将所有传入流量重定向到机器 10.0.0.8。如果多个地址别名指定相同的公共地址，如下所示：

```sh
redirect_address 192.168.0.2 public_addr
redirect_address 192.168.0.3 public_addr
redirect_address 192.168.0.4 public_addr
```

传入流量将被定向到最后一个转换的本地地址（192.168.0.4），但来自前两个地址的传出流量仍将被别名化，表现为来自指定的 `public_addr`。

**`-redirect_port`** `proto targetIP:targetPORT[,targetIP:targetPORT[,...]] [aliasIP:]aliasPORT [remoteIP[:remotePORT]]`

**`-redirect_address`** `localIP[,localIP[,...]] publicIP` 这些形式的 `-redirect_port` 和 `-redirect_address` 用于透明地卸载单个服务器上的网络负载，并将负载分布到服务器池中。此功能称为 *LSNAT*（RFC 2391）。例如，参数

```sh
tcp www1:http,www2:http,www3:http www:http
```

表示主机 www 的传入 HTTP 请求将被透明地重定向到 www1、www2 或 www3 之一，主机的选择仅基于轮询，而不考虑网络负载。

**`-dynamic`** 如果使用 `-n` 或 `-interface` 选项，`natd` 将监视路由套接字以获取所传递 `interface` 的更改。如果接口的 IP 地址发生更改，`natd` 将动态更改其别名地址概念。

**`-in_port | -i`** `port` 从 [divert(4)](../man4/divert.4.md) 端口 `port` 读取和写入，将所有数据包视为"传入"。

**`-out_port | -o`** `port` 从 [divert(4)](../man4/divert.4.md) 端口 `port` 读取和写入，将所有数据包视为"传出"。

**`-port | -p`** `port` 从 [divert(4)](../man4/divert.4.md) 端口 `port` 读取和写入，使用 [divert(4)](../man4/divert.4.md) 中指定的规则区分"传入"或"传出"数据包。如果 `port` 不是数字，则在 [services(5)](../man5/services.5.md) 数据库中搜索。如果未指定此选项，将使用名为 `natd` 的 divert 端口作为默认值。

**`-alias_address | -a`** `address` 使用 `address` 作为别名地址。如果未指定 `-proxy_only` 选项，则必须使用此选项或 `-interface` 选项（但不可同时使用）。指定的地址通常是分配给"公共"网络接口的地址。所有 *传出* 的数据包将以等于 `address` 的源地址重写。所有 *传入* 的数据包将被检查以查看是否匹配任何已设置别名的传出连接。如果匹配，则相应地更改数据包。如果不匹配，则检查并执行所有 `-redirect_port`、`-redirect_proto` 和 `-redirect_address` 分配。如果无法执行其他操作且未指定 `-deny_incoming`，则使用下文 `-target_address` 选项中指定的规则将数据包传递到本地机器。

**`-t | -target_address`** `address` 设置目标地址。当与任何预先存在的链接无关的传入数据包到达主机时，它将被发送到指定的 `address`。目标地址可设为 `255.255.255.255`，在这种情况下，所有新的传入数据包都转到由 `-alias_address` 或 `-interface` 设置的别名地址。如果不使用此选项，或以参数 `0.0.0.0` 调用，则所有新的传入数据包都转到数据包中指定的地址。这允许外部机器直接与内部机器通信，前提是它们能将数据包路由到该机器。

**`-interface | -n`** `interface` 使用 `interface` 确定别名地址。如果与 `interface` 关联的 IP 地址可能更改，还应使用 `-dynamic` 选项。如果未指定此选项，则必须使用 `-alias_address` 选项。指定的 `interface` 通常是"公共"（或"外部"）网络接口。

**`-config | -f`** `file` 从 `file` 读取配置。`file` 应包含选项列表，每行一个，格式与上述命令行选项的长形式相同。例如，行

```sh
alias_address 158.152.17.1
```

将指定别名地址为 158.152.17.1。不接受参数的选项在配置文件中以 `yes` 或 `no` 参数指定。例如，行

```sh
log yes
```

等同于 `-log`。选项可以划分为多个部分。每个部分应用于自己的 `natd` 实例。此功能允许为一个 `natd` 进程配置多个 NAT 实例。始终存在的第一个实例是"default"实例。每个其他实例应以

```sh
instance `instance_name`
```

开头，接下来应放置配置选项。示例：

```sh
# default instance
port 8668
alias_address 158.152.17.1

# second instance
instance dsl1
port 8888
alias_address 192.168.0.1
```

尾随空格和空行被忽略。`#` 符号将该行其余部分标记为注释。

**`-instance`** `instancename` 此选项将命令行选项处理切换为配置实例 `instancename`（必要时创建它），直到下一个 `-instance` 选项或命令行结束。使用 `-config` 选项指定的配置文件设置多个实例比在命令行上更容易。

**`-globalport`** `port` 从 [divert(4)](../man4/divert.4.md) 端口 `port` 读取和写入，将所有数据包视为"传出"。此选项旨在用于多个实例：在此端口上接收的数据包将针对每个已配置实例的内部转换表进行检查。如果找到条目，则根据该条目对数据包设置别名。如果在任何实例中均未找到条目，则数据包保持不变地传递，且不会创建新条目。详见 MULTIPLE INSTANCES 章节。

**`-reverse`** 此选项使 `natd` 反转处理"传入"和"传出"数据包的方式，使其能在"内部"网络接口而非"外部"接口上运行。这在某些透明代理情况下很有用，当传出流量被重定向到本地机器且 `natd` 运行在内部接口上时（通常运行在外部接口上）。

**`-proxy_only`** 强制 `natd` 仅执行透明代理。不执行正常的地址转换。

**`-proxy_rule`** `[type encode_ip_hdr | encode_tcp_stream] port xxxx server a.b.c.d:yyyy` 启用透明代理。通过本主机发往任何其他主机的具有给定端口的传出 TCP 数据包被重定向到给定的服务器和端口。可选地，原始目标地址可以编码到数据包中。使用 `encode_ip_hdr` 将此信息放入 IP 选项字段，或使用 `encode_tcp_stream` 将数据注入 TCP 流的开头。

**`-punch_fw`** `basenumber:count` 此选项指示 `natd` 在基于 [ipfirewall(4)](../man4/ipfirewall.4.md) 的防火墙中为 FTP/IRC DCC 连接"打洞"。这是通过安装临时防火墙规则来动态完成的，这些规则允许特定连接（且仅该连接）通过防火墙。相应的连接终止后，规则将被移除。从规则号 `basenumber` 开始最多 `count` 条规则将用于打防火墙洞。启动时将清除该范围内的所有规则。当内核处于安全级别 3 时此选项无效，更多信息请参见 [init(8)](init.8.md)。

**`-skinny_port`** `port` 此选项允许你指定用于 Skinny Station 协议的 TCP 端口。Skinny 由 Cisco IP 电话用于与 Cisco Call Manager 通信以建立 IP 语音呼叫。默认情况下，不执行 Skinny 别名处理。Skinny 的典型端口值为 2000。

**`-log_ipfw_denied`** 当数据包因 [ipfw(8)](ipfw.8.md) 规则阻止而无法重新注入时记录日志。这是 `-verbose` 的默认行为。

**`-pid_file | -P`** `file` 指定用于存储进程 ID 的替代文件。默认为 **/var/run/natd.pid**。

**`-exit_delay`** `ms` 指定信号后守护进程退出前的延迟（毫秒）。默认为 `10000`。

## 运行 NATD

尝试运行 `natd` 之前，需要以下步骤：

1. 构建具有以下选项的自定义内核：

```sh
options IPFIREWALL
options IPDIVERT
```

有关构建自定义内核的详细说明，请参阅手册。

2. 确保你的机器充当网关。这可以通过在 **/etc/rc.conf** 文件中指定行

```sh
gateway_enable=YES
```

或使用命令

```sh
sysctl net.inet.ip.forwarding=1
```

来完成。

3. 如果使用 `-interface` 选项，请确保接口已配置。例如，如果你想指定 `tun0` 作为 `interface`，且在该接口上使用 ppp(8)，则必须确保在启动 `natd` 之前启动 `ppp`。

运行 `natd` 相当简单。以下命令

```sh
natd -interface ed0
```

在大多数情况下就足够了（替换正确的接口名）。有关如何配置以在启动时自动运行的说明，请查看 [rc.conf(5)](../man5/rc.conf.5.md)。`natd` 运行后，必须确保流量被转移到 `natd`：

1. 你需要根据需要调整 **/etc/rc.firewall** 脚本。如果你不想设置防火墙，以下行即可：

```sh
/sbin/ipfw -f flush
/sbin/ipfw add divert natd all from any to any via ed0
/sbin/ipfw add pass all from any to any
```

第二行取决于你的接口（根据需要更改 `ed0`）。你应该意识到，使用这些防火墙设置，本地网络上的每个人都可以使用你的主机作为网关来伪造其源地址。如果本地网络上有其他主机，强烈建议创建仅允许与受信任主机之间通信的防火墙规则。如果指定实际的防火墙规则，最好在脚本开头指定第二行，以便 `natd` 在数据包被防火墙丢弃之前看到所有数据包。经 `natd` 转换后，数据包在导致转移的规则编号之后的规则编号处重新进入防火墙（如果同一编号有多个规则，则不是下一条规则）。

2. 通过在 **/etc/rc.conf** 中设置

```sh
firewall_enable=YES
```

来启用防火墙。这告诉系统启动脚本运行 **/etc/rc.firewall** 脚本。如果不想现在重启，只需从控制台手动运行。切勿从远程会话运行此命令，除非将其放入后台。否则，刷新后你将被锁定，**/etc/rc.firewall** 的执行将在此点停止——永久阻止所有访问。在后台运行脚本应该足以防止此灾难。

## 多实例

需要对多个外部 IP 地址进行别名化的情况并不少见。虽然传统上通过运行多个具有独立配置的 `natd` 进程来实现，但 `natd` 可以在单个进程中拥有多个别名化实例，也允许它们彼此之间不那么独立。例如，让我们看一个在具有两个外部接口 `sis0`（IP 为 1.2.3.4）和 `sis2`（IP 为 2.3.4.5）的机器上对两个到不同提供商的通道进行负载均衡的常见任务：

```sh
          net 1.2.3.0/24
1.2.3.1 ------------------ sis0
(router)                (1.2.3.4)
                                 net 10.0.0.0/24
                          sis1 ------------------- 10.0.0.2
                       (10.0.0.1)
          net 2.3.4.0/24
2.3.4.1 ------------------ sis2
(router)                (2.3.4.5)
```

默认路由通过 `sis0` 出去。

内部机器（10.0.0.2）可通过两个外部 IP 在 TCP 端口 122 上访问，传出连接在 `sis0` 和 `sis2` 之间随机选择路径。

其工作方式是 `natd.conf` 构建别名化引擎的两个实例。

除了这些实例的私有 [divert(4)](../man4/divert.4.md) 套接字外，还创建了名为"globalport"的第三个套接字；通过此套接字发送到 `natd` 的数据包将针对所有实例进行匹配，如果找到现有条目则进行转换，如果没有条目则保持不变。以下行放入 **/etc/natd.conf**：

```sh
log
deny_incoming
verbose

instance default
interface sis0
port 1000
redirect_port tcp 10.0.0.2:122 122

instance sis2
interface sis2
port 2000
redirect_port tcp 10.0.0.2:122 122

globalport 3000
```

并使用以下 [ipfw(8)](ipfw.8.md) 规则：

```sh
ipfw -f flush

ipfw add      allow ip from any to any via sis1

ipfw add      skipto 1000 ip from any to any in via sis0
ipfw add      skipto 2000 ip from any to any out via sis0
ipfw add      skipto 3000 ip from any to any in via sis2
ipfw add      skipto 4000 ip from any to any out via sis2

ipfw add 1000 count ip from any to any

ipfw add      divert 1000 ip from any to any
ipfw add      allow ip from any to any

ipfw add 2000 count ip from any to any

ipfw add      divert 3000 ip from any to any

ipfw add      allow ip from 1.2.3.4 to any
ipfw add      skipto 5000 ip from 2.3.4.5 to any

ipfw add      prob .5 skipto 4000 ip from any to any

ipfw add      divert 1000 ip from any to any
ipfw add      allow ip from any to any

ipfw add 3000 count ip from any to any

ipfw add      divert 2000 ip from any to any
ipfw add      allow ip from any to any

ipfw add 4000 count ip from any to any

ipfw add      divert 2000 ip from any to any

ipfw add 5000 fwd 2.3.4.1 ip from 2.3.4.5 to not 2.3.4.0/24
ipfw add      allow ip from any to any
```

这里从内部网络到 Internet 的数据包通过 `sis0`（规则号 2000）出去，并被 `globalport` 套接字（3000）捕获。之后，要么在两个实例之一的转换表中找到匹配，要么以相同概率将数据包传递到另外两个 [divert(4)](../man4/divert.4.md) 端口（1000 或 2000）之一。这确保了负载均衡以每流为基础完成（即，来自单个 TCP 连接的数据包始终通过同一接口流动）。源 IP 为非默认接口（`sis2`）的已转换数据包被转发到该接口上适当的路由器。

## 参见

libalias(3), [divert(4)](../man4/divert.4.md), [protocols(5)](../man5/protocols.5.md), [rc.conf(5)](../man5/rc.conf.5.md), [services(5)](../man5/services.5.md), syslog.conf(5), [init(8)](init.8.md), [ipfw(8)](ipfw.8.md), ppp(8)

## 历史

`natd` 工具出现于 FreeBSD 3.0。

## 作者

此程序是许多人在不同时间努力的结果：

Archie Cobbs <archie@FreeBSD.org>（divert 套接字）Charles Mott <cm@linktel.net>（数据包别名化）Eivind Eklund <perhaps@yes.no>（IRC 支持及杂项添加）Ari Suutari <suutari@iki.fi>（natd）Dru Nelson <dnelson@redwoodsoft.com>（早期 PPTP 支持）Brian Somers <brian@awfulhak.org>（粘合）Ruslan Ermilov <ru@FreeBSD.org>（natd、数据包别名化、粘合）Poul-Henning Kamp <phk@FreeBSD.org>（多实例）
