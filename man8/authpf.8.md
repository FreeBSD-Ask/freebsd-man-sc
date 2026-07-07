# authpf-noip(8)

`authpf` — 认证网关用户 shell

## 名称

`authpf`, `authpf-noip`

## 概要

`authpf` `authpf-noip`

## 描述

`authpf` 是用于认证网关的用户 shell。当用户通过 sshd(8) 认证并启动会话时，它用于修改 [pf(4)](../man4/pf.4.md) 规则；当用户会话退出时，它撤销这些更改。典型用途包括：在允许用户使用 Internet 之前先进行认证的网关，或者将不同用户引导至不同位置的网关。结合正确配置的过滤规则和安全交换机，`authpf` 可用于确保用户的网络流量具备可追溯性。它仅适用于能通过 [ssh(1)](../man1/ssh.1.md) 连接的用户，并且需要启用 [pf(4)](../man4/pf.4.md) 子系统以及挂载于 **/dev/fd** 的 [fdescfs(4)](../man4/fdescfs.4.md) 文件系统。

`authpf-noip` 是一种允许从同一 IP 地址发起多个连接的用户 shell。它主要适用于连接通过网关系统隧道传输、且可直接与用户名关联的场景。当按 IP 地址对连接进行分类时，它无法确保可追溯性；在这种情况下，客户端的 IP 地址不会通过 `client_ip` 宏或 `authpf_users` 表提供给包过滤器。此外，会话结束时与该客户端 IP 地址关联的状态也不会被清除。

要使用 `authpf` 或 `authpf-noip`，需将用户的 shell 设置为 **/usr/sbin/authpf** 或 **/usr/sbin/authpf-noip**。

只要用户保持活动的 [ssh(1)](../man1/ssh.1.md) 会话，`authpf` 就会使用 [pf.conf(5)](../man5/pf.conf.5.md) 语法为单个用户或客户端 IP 地址修改过滤和转换规则，并将成功开始和结束会话的事件记录到 syslogd(8)。`authpf` 通过 `SSH_CLIENT` 环境变量获取客户端的连接 IP 地址，在执行额外的访问检查后，读取模板文件以确定要添加哪些过滤和转换规则（如果有），并在 `authpf_users` 表中维护已连接用户的 IP 地址列表。会话退出时，启动时添加的相同规则和表项将被移除，与该客户端 IP 地址关联的所有状态也将被清除。

每个 `authpf` 进程将其规则存储在一个由所有 `authpf` 进程共享的 [pf(4)](../man4/pf.4.md) `anchor` 内的独立规则集中。默认使用 anchor 名称 “authpf”，规则集名称等于 `authpf` 进程的用户名和 PID，格式为 “username(pid)”。需要在主规则集 **/etc/pf.conf** 中添加以下规则，以便触发对任何 `authpf` 规则的求值：

```sh
nat-anchor "authpf/*"
rdr-anchor "authpf/*"
binat-anchor "authpf/*"
anchor "authpf/*"
```

anchor 名称末尾的 “/*” 是必需的，这样 [pf(4)](../man4/pf.4.md) 才能处理由 `authpf` 附加到 anchor 的规则集。

## 过滤与转换规则

`authpf` 的过滤和转换规则使用与 [pf.conf(5)](../man5/pf.conf.5.md) 中描述的相同格式。唯一区别在于，这些规则可以（且可能应该）使用宏 *user_ip*，每当运行 `authpf` 时，该宏会被赋予客户端的连接 IP 地址。此外，宏 *user_id* 会被赋予用户名。

过滤和转换规则存储在名为 `authpf.rules` 的文件中。系统会先在 **/etc/authpf/users/$USER/** 目录中查找此文件，然后在 **/etc/authpf/** 目录中查找。如果两处都存在，只会使用其中一个。

**/etc/authpf/users/$USER/** 目录中的每用户规则用于在需要为单个用户定制非默认规则时使用。务必确保用户无法写入或修改这些配置文件。

`authpf.rules` 文件必须存在于上述位置之一，`authpf` 才能运行。

## 配置

选项由 **/etc/authpf/authpf.conf** 文件控制。如果该文件为空，则所有配置选项使用默认值。该文件由 `name=value` 形式的键值对组成，每行一对。当前允许的值如下：

**anchor=name** 使用指定的 `anchor` 名称代替 “authpf”。

**table=name** 使用指定的 `table` 名称代替 “authpf_users”。

## 用户消息

成功调用时，`authpf` 会显示一条消息，告知用户已通过认证。如果文件 **/etc/authpf/authpf.message** 存在且可读，则还会显示该文件的内容。

有两种方法可以为 `authpf` 提供的控制提供更细粒度——可以将网关设置为显式允许已通过 [ssh(1)](../man1/ssh.1.md) 认证的用户，而仅拒绝少数捣乱者。方法是：在 **/etc/authpf/banned/** 目录中创建一个以被禁用户登录名命名的文件。该文件的内容会显示给被禁用户，从而提供一种告知用户其已被禁用、以及若想恢复服务应去何处寻求帮助的方法。这是默认行为。

也可以将 `authpf` 配置为仅允许特定用户访问。方法是：在 **/etc/authpf/authpf.allow** 中列出其登录名，每行一个。在组名前加 “%” 可表示一组用户，在登录类名前加 “@” 可表示该登录类的所有成员。如果某行只有 “*”，则匹配所有用户名。如果 `authpf` 无法验证用户是否有权使用网关，它会打印一条简短消息并退出。需要注意的是，禁用优先于允许。

失败时，消息会记录到 syslogd(8) 供系统管理员查看。用户看不到这些消息，但会被告知系统因技术问题不可用。如果文件 **/etc/authpf/authpf.problem** 存在且可读，则还会显示该文件的内容。

## 配置注意事项

只要用户保持活动会话，`authpf` 就会维持已修改的过滤规则。然而，必须记住该会话的存在即意味着用户已通过认证。因此，配置 sshd(8) 以确保会话安全、以及确保用户连接所经过的网络是安全的，这两点非常重要。sshd(8) 应配置为使用 `ClientAliveInterval` 和 `ClientAliveCountMax` 参数，以确保在 ssh 会话无响应，或有人使用 arp 或地址欺骗劫持会话时，能迅速终止该会话。请注意，TCP keepalive 不足以胜任此任务，因为它并不安全。还需注意，对 `authpf` 用户应禁用各种 SSH 隧道机制（如 `AllowTcpForwarding` 和 `PermitTunnel`），以防止他们绕过包过滤器规则集所施加的限制。

`authpf` 会移除用户会话期间创建的状态表项。这确保在控制性 [ssh(1)](../man1/ssh.1.md) 会话关闭后，不会有未经认证的流量被允许通过。

`authpf` 专为网关机器设计，这类机器通常没有普通（非管理性）用户使用。管理员必须记住，`authpf` 可用于通过其运行环境修改过滤规则，因此普通用户也可能利用它（基于配置文件的内容）修改过滤规则。如果一台机器既有普通用户使用，也有以 `authpf` 作为 shell 的用户，则应使用 **/etc/authpf/authpf.allow** 或 **/etc/authpf/banned/** 机制来阻止普通用户运行 `authpf`。

`authpf` 会修改包过滤器和地址转换规则，因此需要谨慎配置。如果 **/etc/authpf/authpf.conf** 文件不存在，`authpf` 将不会运行并静默退出。在考虑 `authpf` 可能对主包过滤规则产生的影响后，系统管理员可以通过创建合适的 **/etc/authpf/authpf.conf** 文件来启用 `authpf`。

## 实例

**控制文件** —— 为说明用户专属的访问控制机制，我们以一个名为 bob 的典型用户为例。正常情况下，只要 bob 能通过认证，`authpf` 程序就会加载相应的规则。现在介绍 **/etc/authpf/banned/** 目录。如果 bob 不知怎么在管理员眼中失宠，他们可以通过创建文件 **/etc/authpf/banned/bob** 来禁止他使用网关，文件中包含关于他为何被禁止使用网络的消息。一旦 bob 做出适当悔过，可以通过移动或删除文件 **/etc/authpf/banned/bob** 来恢复其访问权限。

现在考虑一个包含 alice、bob、carol 和 dave 的工作组。他们有一个无线网络，希望防止未经授权的使用。为此，他们创建文件 **/etc/authpf/authpf.allow**，其中列出他们的登录 ID、以 “%” 开头的组名或以 “@” 开头的登录类名，每行一个。此时，即使 eve 能通过 sshd(8) 认证，她也不被允许使用该网关。在工作组中添加和删除用户只需维护一个允许的用户 ID 列表。如果 bob 再次惹恼管理员，他们可以通过创建熟悉的 **/etc/authpf/banned/bob** 文件来禁止他使用网关。尽管 bob 列在允许文件中，但由于禁用文件的存在，他无法使用该网关。

**分布式认证** —— 通常希望与分布式密码系统对接，而不是强迫系统管理员保持大量本地密码文件同步。OpenBSD 中的 login.conf(5) 机制可用于派生出正确的 shell。为此，login.conf(5) 中应有类似如下的条目：

```sh
shell-default:shell=/bin/csh
default:\
	...
	:shell=/usr/sbin/authpf
daemon:\
	...
	:shell=/bin/csh:\
	:tc=default:
staff:\
	...
	:shell=/bin/csh:\
	:tc=default:
```

使用默认密码文件时，所有用户都会以 `authpf` 作为 shell，但 root 例外，其 shell 为 **/bin/csh**。

**SSH 配置** —— 如前所述，必须正确配置 sshd(8) 以检测和抵御网络攻击。为此，应在 sshd_config(5) 中添加以下选项：

```sh
Protocol 2
ClientAliveInterval 15
ClientAliveCountMax 3
```

这确保无响应或被伪造的会话在一分钟内被终止，因为劫持者无法伪造 ssh keepalive 消息。

**横幅信息** —— 用户通过认证后，会看到 **/etc/authpf/authpf.message** 的内容。该消息可以是一整屏的适当使用策略、**/etc/motd** 的内容，或简单如下：

```sh
This means you will be held accountable by the powers that be
for traffic originating from your machine, so please play nice.
```

要告知用户系统出故障时该去哪里求助，**/etc/authpf/authpf.problem** 可以包含类似如下的内容：

```sh
Sorry, there appears to be some system problem. To report this
problem so we can fix it, please phone 1-900-314-1597 or send
an email to remove@bulkmailerz.net.
```

**包过滤规则** —— 在该网关用于保护无线网络（带有数百个端口的集线器）的场景中，默认规则集以及每用户规则可能除了像 [ssh(1)](../man1/ssh.1.md)、ssl(8) 或 [ipsec(4)](../man4/ipsec.4.md) 这样的加密协议外，应允许很少的内容。在安全交换的网络中，为访客提供认证账户的插孔，你可能希望允许所有出站流量。在此语境下，安全交换机是指试图防止地址表溢出攻击的交换机。

示例 **/etc/pf.conf**：

```sh
# 默认情况下，我们允许内部客户端使用
# ssh 与我们通信，并将我们作为 dns 服务器。
internal_if="fxp1"
gateway_addr="10.0.1.1"
nat-anchor "authpf/*"
rdr-anchor "authpf/*"
binat-anchor "authpf/*"
block in on $internal_if from any to any
pass in quick on $internal_if proto tcp from any to $gateway_addr \
      port = ssh
pass in quick on $internal_if proto udp from any to $gateway_addr \
      port = domain
anchor "authpf/*"
```

**对于交换式有线网络** —— 此示例 **/etc/authpf/authpf.rules** 没有施加真正的限制；它只是开启和关闭 IP 地址，并记录 TCP 连接。

```sh
external_if = "xl0"
internal_if = "fxp0"

pass in log quick on $internal_if proto tcp from $user_ip to any
pass in quick on $internal_if from $user_ip to any
```

**对于无线或共享网络** —— 此示例 **/etc/authpf/authpf.rules** 可用于不安全的网络（如公共无线网络），在这种情况下我们可能需要更严格一些。

```sh
internal_if="fxp1"
ipsec_gw="10.2.3.4"

# rdr ftp，由 ftp-proxy(8) 代理
rdr on $internal_if proto tcp from $user_ip to any port 21 \
      -> 127.0.0.1 port 8021

# 仅允许出站 ftp、ssh、www 和 https，并允许用户与
# ipsec 服务器协商 ipsec。
pass in log quick on $internal_if proto tcp from $user_ip to any \
      port { 21, 22, 80, 443 }
pass in quick on $internal_if proto tcp from $user_ip to any \
      port { 21, 22, 80, 443 }
pass in quick proto udp from $user_ip to $ipsec_gw port = isakmp
pass in quick proto esp from $user_ip to $ipsec_gw
```

**处理 NAT** —— 以下 **/etc/authpf/authpf.rules** 展示了如何使用标记处理 NAT：

```sh
ext_if = "fxp1"
ext_addr = 129.128.11.10
int_if = "fxp0"
# nat 并为连接打标记...
nat on $ext_if from $user_ip to any tag $user_ip -> $ext_addr
pass in quick on $int_if from $user_ip to any
pass out log quick on $ext_if tagged $user_ip
```

通过 `authpf` 添加上述规则后，与每个用户 NAT 连接对应的出站连接将被记录，如下例所示，其中可通过规则集名称识别用户。

```sh
# tcpdump -n -e -ttt -i pflog0
Oct 31 19:42:30.296553 rule 0.bbeck(20267).1/0(match): pass out on fxp1: \
129.128.11.10.60539 > 198.137.240.92.22: S 2131494121:2131494121(0) win \
16384 <mss 1460,nop,nop,sackOK> (DF)
```

**使用 authpf_users 表** —— 简单的 `authpf` 设置可以不使用 anchor，仅通过 “authpf_users” `table` 实现。例如，以下 [pf.conf(5)](../man5/pf.conf.5.md) 行将为已登录用户提供 SMTP 和 IMAP 访问：

```sh
table <authpf_users> persist
pass in on $ext_if proto tcp from <authpf_users> \
        to port { smtp imap }
```

也可以将 “authpf_users” `table` 与 anchor 结合使用。例如，可以仅对来自已登录用户的数据包查找 anchor，从而加快 [pf(4)](../man4/pf.4.md) 处理速度：

```sh
table <authpf_users> persist
anchor "authpf/*" from <authpf_users>
rdr-anchor "authpf/*" from <authpf_users>
```

**通过隧道连接的用户** —— 通常 `authpf` 对每个客户端 IP 地址仅允许一个会话。但在某些情况下，例如连接通过 [ssh(1)](../man1/ssh.1.md) 或 [ipsec(4)](../man4/ipsec.4.md) 隧道传输时，可以基于用户的用户 ID 而非客户端 IP 地址对连接进行授权。此时适合使用 `authpf-noip`，以允许 NAT 网关后的多个用户连接。在以下 **/etc/authpf/authpf.rules** 示例中，远程用户可以将远程桌面会话隧道传输到其工作站：

```sh
internal_if="bge0"
workstation_ip="10.2.3.4"

pass out on $internal_if from (self) to $workstation_ip port 3389 \
       user $user_id
```

## 文件

**/etc/authpf/authpf.conf**
**/etc/authpf/authpf.allow**
**/etc/authpf/authpf.rules**
**/etc/authpf/authpf.message**
**/etc/authpf/authpf.problem**

## 参见

[fdescfs(4)](../man4/fdescfs.4.md), [pf(4)](../man4/pf.4.md), [pf.conf(5)](../man5/pf.conf.5.md), securelevel(7), [ftp-proxy(8)](ftp-proxy.8.md)

## 历史

`authpf` 程序首次出现在 OpenBSD 3.1 中。

## 缺陷

配置问题较为棘手。认证用的 [ssh(1)](../man1/ssh.1.md) 连接可能是安全的，但如果网络不安全，用户可能会向同一网络中的攻击者暴露不安全的协议，或者使网络上的其他攻击者能够通过伪造 IP 地址冒充该用户。

`authpf` 并非为防止用户对其他用户发起拒绝服务攻击而设计。
