  AUTHPF(8)  

AUTHPF(8)

FreeBSD System Manager's Manual

AUTHPF(8)

[名称](#__u540D___u79F0_)
=======================

`authpf`, `authpf-noip` —

验证网关用户 shell

[概要](#__u6982___u8981_)
=======================

`authpf` `authpf-noip`

[描述](#__u63CF___u8FF0_)
=======================

`authpf` 是用于验证网关的用户 shell。 它用于在用户进行身份验证并使用 sshd(8) 启动会话时更改 pf(4) 规则，并在用户会话退出时撤消这些更改。 典型用途是在允许用户使用 Internet 之前对用户进行身份验证的网关，或允许不同用户进入不同位置的网关。 结合正确设置的过滤规则和安全开关， `authpf` 可用于确保用户对其网络流量负责。 它适用于只能通过 ssh(1) 连接的用户，并且需要启用 pf(4) 子系统和安装在 /dev/fd 的 fdescfs(5) 文件系统。

`authpf-noip` 是一个用户 shell，它允许从同一个 IP 地址进行多个连接。 它主要在通过网关系统建立隧道连接的情况下很有用，并且可以直接与用户名相关联。 在按 IP 地址对连接进行分类时无法确保问责制；在这种情况下，客户端的 IP 地址不会通过 client\_ip 宏或 authpf\_users 表提供给数据包过滤器。 此外，与客户端 IP 地址关联的状态在会话结束时不会被清除。

要使用 `authpf` 或 `authpf-noip`, 用户的 shell 需要设置为 /usr/sbin/authpf 或 /usr/sbin/authpf-noip 。

`authpf` 使用 pf.conf(5) 语法来更改单个用户或客户端 IP 地址的过滤器和转换规则，只要用户保持活动的 ssh(1) 会话，并将会话的成功开始和结束记录到 syslogd(8) 。 `authpf` 通过 `SSH_CLIENT` 环境变量检索客户端的连接 IP 地址，并在执行额外的访问检查后，读取模板文件以确定要添加的过滤器和转换规则（如果有），并在 authpf\_users 表。 在会话退出时，启动时添加的相同规则和表条目将被删除，并且与客户端 IP 地址关联的所有状态都将被清除。

每个 `authpf` 进程将其规则存储在所有 `authpf` 进程共享的 pf(4) anchor 内的单独规则集中。 默认情况下，使用 anchor 名称 "authpf" ，并且规则集名称等于 `authpf` 进程的用户名和 PID，如 "username(pid)" 。 需要将以下规则添加到主规则集 /etc/pf.conf 以评估任何 `authpf` 规则：

nat-anchor "authpf/\*" rdr-anchor "authpf/\*" binat-anchor "authpf/\*" anchor "authpf/\*" 

pf(4) 需要锚名称末尾的 "/\*" 来处理 `authpf` 附加到锚的规则集。

[过滤和翻译规则](#__u8FC7___u6EE4___u548C___u7FFB___u8BD1___u89C4___u5219_)
====================================================================

`authpf` 的过滤器和翻译规则使用 pf.conf(5) 中描述的相同格式。 唯一的区别是这些规则可能（并且可能应该）使用宏 _user\_ip_, 只要运行 `authpf` 就会为其分配连接 IP 地址。 此外，宏 _user\_id_ 被分配了用户名。

过滤器和翻译规则存储在名为 authpf.rules 的文件中。 该文件将首先在 /etc/authpf/users/$USER/ 中搜索，然后在 /etc/authpf/ 中搜索。 如果两个文件都存在，则只使用其中一个文件。

/etc/authpf/users/$USER/ 目录中的每用户规则旨在用于单个用户需要非默认规则时。 确保用户不能编写或更改这些配置文件非常重要。

authpf.rules 文件必须存在于上述位置之一才能运行 `authpf` 。

[配置](#__u914D___u7F6E_)
=======================

选项由 /etc/authpf/authpf.conf 文件控制。 如果文件为空，则所有配置选项都使用默认值。 该文件由 `name=value` 形式的对组成，每行一个。目前，允许的值如下：

anchor=name

使用指定的 anchor 名称而不是 "authpf" 。

table=name

使用指定的 table 名而不是 "authpf\_users" 。

[用户留言](#__u7528___u6237___u7559___u8A00_)
=========================================

成功调用后， `authpf` 会显示一条消息，告诉用户他或她已通过身份验证。 如果文件存在并且可读，它将另外显示文件 /etc/authpf/authpf.message-
的内容。

有两种方法可以为 `authpf` 提供的控制提供额外的粒度 - 可以将网关设置为显式允许已通过 ssh(1) 进行身份验证的用户并仅拒绝少数麻烦的个人访问。 这是通过在 /etc/authpf/banned/ 中创建一个以被禁止用户的登录名作为文件名的文件来完成的。 该文件的内容将显示给被禁止的用户，从而提供一种方法来通知用户他们已被禁止，如果他们想要恢复服务，他们可以去哪里以及如何到达那里。 这是默认行为。

也可以将 `authpf` 配置为仅允许特定用户访问。 这是通过在 /etc/authpf/authpf.allow 中列出他们的登录名（每行一个）来完成的。 一组用户也可以通过在组名前加 "%" 来表示，登录类的所有成员可以通过在登录类名前加 "@" 来表示。 如果在一行中找到 "\*" ，则所有用户名都匹配。 如果 `authpf` 无法验证用户使用网关的权限，它将打印一条简短消息并死掉。 应该注意的是，禁令优先于允许。

失败时，系统管理员会将消息记录到 syslogd(8) 。 用户看不到这些，但会被告知系统由于技术问题不可用。 如果文件存在并且可读，那么文件 /etc/authpf/authpf.problem 的内容也会显示出来。

[配置问题](#__u914D___u7F6E___u95EE___u9898_)
=========================================

`authpf` 只要用户保持活动会话，authpf 就会保持更改后的过滤规则。 然而，重要的是要记住，此会话的存在意味着用户已通过身份验证。 因此，配置 sshd(8) 以确保会话的安全以及确保用户连接的网络是安全的非常重要。 sshd(8) 应配置为使用 ClientAliveInterval 和 ClientAliveCountMax 参数，以确保 ssh 会话在无响应或使用 arp 或地址欺骗劫持会话时快速终止。 请注意，TCP keepalives 是不够的，因为它们不安全。 另请注意，应为 `authpf` 用户禁用各种 SSH 隧道机制，例如 AllowTcpForwarding 和 PermitTunnel, 以防止他们规避数据包过滤规则集施加的限制。

`authpf` 将删除在用户会话期间创建的状态表条目。 这确保了在控制 ssh(1) 会话关闭后不会有未经身份验证的流量通过。

`authpf` 专为网关机器而设计，这些机器通常没有常规（非管理）用户使用该机器。 管理员必须记住， `authpf` 可用于通过其运行环境修改过滤规则，因此可用于普通用户修改过滤规则（基于配置文件的内容）。 在机器有普通用户使用它的情况下，以及使用 `authpf` 作为其 shell 的用户，应通过使用 /etc/authpf/authpf.allow 或 /etc/authpf/banned/ 来阻止普通用户运行 `authpf` 设施。

`authpf` 修改包过滤和地址转换规则，因此需要仔细配置。 如果 /etc/authpf/authpf.conf 文件不存在， `authpf` 将不会运行并静默退出。 在考虑 `authpf` 对主要数据包过滤规则的影响后，系统管理员可以通过创建适当的 /etc/authpf/authpf.conf 文件来启用 `authpf` 。

[实例](#__u5B9E___u4F8B_)
=======================

**Control Files** - 为了说明用户特定的访问控制机制，让我们考虑一个名为 bob 的典型用户。 通常，只要 bob 可以验证自己， `authpf` 程序就会加载相应的规则。 进入 /etc/authpf/banned/ 目录。 如果鲍勃在当权者眼中失宠，他们可以通过创建文件 /etc/authpf/banned/bob 来禁止他使用网关，该文件包含一条关于为什么他被禁止使用网络。 一旦 bob 完成了适当的忏悔，他的访问权可以通过移动或删除文件 /etc/authpf/banned/bob 来恢复。

现在考虑一个包含 alice、bob、carol 和 dave 的工作组。 他们有一个无线网络，他们希望保护它免受未经授权的使用。 为此，他们创建了文件 /etc/authpf/authpf.allow ，其中列出了他们的登录 ID、以 "%" 开头的组或以 "@" 开头的登录类，每行一个。 此时，即使 eve 可以通过 sshd(8) 进行身份验证，她也不会被允许使用网关。 在工作组中添加和删除用户是维护允许的用户标识列表的简单问题。 如果 bob 再次惹恼了当权者，他们可以通过创建熟悉的 /etc/authpf/banned/bob 文件来禁止他使用网关。尽管 bob 已在允许文件中列出，但由于存在禁止文件，他无法使用此网关。

**Distributed Authentication** - 通常需要与分布式密码系统交互，而不是强制系统管理员保持大量本地密码文件同步。 OpenBSD 中的 login.conf(5)-
机制可用于 fork 正确的 shell。 为了实现这一点， login.conf(5) 应该有如下所示的条目：

shell-default:shell=/bin/csh default:\\ ... :shell=/usr/sbin/authpf daemon:\\ ... :shell=/bin/csh:\\ :tc=default: staff:\\ ... :shell=/bin/csh:\\ :tc=default: 

使用默认密码文件，所有用户都将获得 `authpf` 作为他们的 shell，除了将获得 /bin/csh 的 root。

**SSH Configuration** - 如前所述，必须正确配置 sshd(8) 以检测和阻止网络攻击。 为此，应将以下选项添加到 sshd\_config(5):

Protocol 2 ClientAliveInterval 15 ClientAliveCountMax 3 

这可确保在一分钟内终止无响应或欺骗会话，因为劫持者不应该能够欺骗 ssh keepalive 消息。

**Banners** - 一旦通过身份验证，就会向用户显示 /etc/authpf/authpf.message 的内容。 此消息可能是一个完整的屏幕，其中包含适当的使用策略、 /etc/motd 的内容或如下所示的简单内容：

这意味着您将被以下权力追究责任 对于来自您的机器的流量，所以请玩好。 

为了告诉用户在系统崩溃时去哪里， /etc/authpf/authpf.problem 可以包含如下内容：

Sorry, there appears to be some system problem. To report this problem so we can fix it, please phone 1-900-314-1597 or send an email to remove@bulkmailerz.net. 

**Packet Filter Rules** - 在此网关用于保护无线网络（具有数百个端口的集线器）的区域中，默认规则集以及每个用户的规则应该允许除了加密协议（如 ssh(1), ssl(8) 或 ipsec(4) 。 在安全交换的网络上，为获得身份验证帐户的访问者提供插件插孔，您可能希望允许所有内容。 在这种情况下，安全开关是一种试图防止地址表溢出攻击的开关。

示例 /etc/pf.conf:

\# by default we allow internal clients to talk to us using # ssh and use us as a dns server. internal\_if="fxp1" gateway\_addr="10.0.1.1" nat-anchor "authpf/\*" rdr-anchor "authpf/\*" binat-anchor "authpf/\*" block in on $internal\_if from any to any pass in quick on $internal\_if proto tcp from any to $gateway\_addr \\ port = ssh pass in quick on $internal\_if proto udp from any to $gateway\_addr \\ port = domain anchor "authpf/\*" 

**For a switched, wired net** - 这个例子 /etc/authpf/authpf.rules 没有真正的限制；它打开和关闭 IP 地址，记录 TCP 连接。

external\_if = "xl0" internal\_if = "fxp0" pass in log quick on $internal\_if proto tcp from $user\_ip to any pass in quick on $internal\_if from $user\_ip to any 

**For a wireless or shared net** - 此示例 /etc/authpf/authpf.rules 可用于不安全的网络（例如公共无线网络），我们可能需要更多限制。

internal\_if="fxp1" ipsec\_gw="10.2.3.4" # rdr ftp for proxying by ftp-proxy(8) rdr on $internal\_if proto tcp from $user\_ip to any port 21 \\ -> 127.0.0.1 port 8021 # allow out ftp, ssh, www and https only, and allow user to negotiate # ipsec with the ipsec server. pass in log quick on $internal\_if proto tcp from $user\_ip to any \\ port { 21, 22, 80, 443 } pass in quick on $internal\_if proto tcp from $user\_ip to any \\ port { 21, 22, 80, 443 } pass in quick proto udp from $user\_ip to $ipsec\_gw port = isakmp pass in quick proto esp from $user\_ip to $ipsec\_gw 

**Dealing with NAT** - 以下 /etc/authpf/authpf.rules 显示了如何使用标记处理 NAT：

ext\_if = "fxp1" ext\_addr = 129.128.11.10 int\_if = "fxp0" # nat and tag connections... nat on $ext\_if from $user\_ip to any tag $user\_ip -> $ext\_addr pass in quick on $int\_if from $user\_ip to any pass out log quick on $ext\_if tagged $user\_ip 

使用 `authpf` 添加的上述规则，对应于每个用户的 NAT 连接的出站连接将被记录，如下例所示，其中用户可以从规则集名称中识别。

\# tcpdump -n -e -ttt -i pflog0 Oct 31 19:42:30.296553 rule 0.bbeck(20267).1/0(match): pass out on fxp1: \\ 129.128.11.10.60539 > 198.137.240.92.22: S 2131494121:2131494121(0) win \\ 16384 <mss 1460,nop,nop,sackOK> (DF) 

**Using the authpf\_users table** - 只需使用-
"authpf\_users" table 即可在没有锚点的情况下实现简单的 `authpf` 设置。 例如，以下 pf.conf(5) 行将为登录用户提供 SMTP 和 IMAP 访问权限：

table <authpf\_users> persist pass in on $ext\_if proto tcp from <authpf\_users> \\ to port { smtp imap } 

还可以将 "authpf\_users" table 与锚点结合使用。 例如，可以通过仅查找来自登录用户的数据包的锚来加快 pf(4) 处理：

table <authpf\_users> persist anchor "authpf/\*" from <authpf\_users> rdr-anchor "authpf/\*" from <authpf\_users> 

**Tunneled users** - 通常 `authpf` 只允许每个客户端 IP 地址进行一个会话。 但是，在某些情况下，例如通过 ssh(1) 或 ipsec(4) 建立隧道连接时，可以根据用户的用户 ID 而不是客户端 IP 地址来授权连接。 在这种情况下，使用 `authpf-noip` 允许 NAT 网关后面的多个用户进行连接是合适的。 在下面的 /etc/authpf/authpf.rules 示例中，远程用户可以通过隧道将远程桌面会话连接到他们的工作站：

internal\_if="bge0" workstation\_ip="10.2.3.4" pass out on $internal\_if from (self) to $workstation\_ip port 3389 \\ user $user\_id 

[文件](#__u6587___u4EF6_)
=======================

/etc/authpf/authpf.conf

/etc/authpf/authpf.allow

/etc/authpf/authpf.rules

/etc/authpf/authpf.message

/etc/authpf/authpf.problem

[参见](#__u53C2___u89C1_)
=======================

pf(4), fdescfs(5), pf.conf(5), securelevel(7), ftp-proxy(8)

[历史](#__u5386___u53F2_)
=======================

`authpf` 程序最早出现在 OpenBSD 3.1 中。

[缺陷](#__u7F3A___u9677_)
=======================

配置问题很棘手。 验证 ssh(1) 连接可能是安全的，但如果网络不安全，则用户可能会将不安全的协议暴露给同一网络上的攻击者，或者使网络上的其他攻击者能够通过欺骗他们的 IP 地址来伪装成用户。

`authpf` 并非旨在防止用户拒绝向其他用户提供服务。

January 29 2014

FreeBSD 13.1-RELEASE