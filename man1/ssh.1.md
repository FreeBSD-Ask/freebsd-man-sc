  SSH(1)  

SSH(1)

FreeBSD General Commands Manual

SSH(1)

[名称](#__u540D___u79F0_)
=======================

`ssh` —

OpenSSH SSH 客户端（远程登录程序）

[概要](#__u6982___u8981_)
=======================

`ssh` \[`-46AaCfGgKkMNnqsTtVvXxYy`\] \[`-B` bind\_interface\] \[`-b` bind\_address\] \[`-c` cipher\_spec\] \[`-D` \[bind\_address:\]port\] \[`-E` log\_file\] \[`-e` escape\_char\] \[`-F` configfile\] \[`-I` pkcs11\] \[`-i` identity\_file\] \[`-J` destination\] \[`-L` address\] \[`-l` login\_name\] \[`-m` mac\_spec\] \[`-O` ctl\_cmd\] \[`-o` option\] \[`-p` port\] \[`-Q` query\_option\] \[`-R` address\] \[`-S` ctl\_path\] \[`-W` host:port\] \[`-w` local\_tun\[:remote\_tun\]\] destination \[command\]

[描述](#__u63CF___u8FF0_)
=======================

`ssh` （SSH 客户端）是一个用于登录远程机器并在远程机器上执行命令的程序。 它旨在通过不安全的网络在两个不受信任的主机之间提供安全的加密通信。 X11 连接、任意 TCP 端口和 UNIX\-domain 套接字也可以通过安全通道转发。

`ssh` 连接并登录到指定的 destination, 可以指定为 \[user@\]hostname 或 ssh://\[user@\]hostname\[:port\] 形式的 URI。 用户必须使用几种方法之一向远程机器证明他/她的身份（见下文）。

如果指定了 command ，它将在远程主机而不是登录 shell 上执行。

选项如下：

[`-4`](#4)

强制 `ssh` 仅使用 IPv4 地址。

[`-6`](#6)

强制 `ssh` 仅使用 IPv6 地址。

[`-A`](#A)

启用身份验证代理连接的转发。 这也可以在配置文件中基于每个主机指定。

应谨慎启用代理转发。能够绕过远程主机上的文件权限（对于代理的 UNIX\-domain 套接字）的用户可以通过转发连接访问本地代理。 攻击者无法从代理获取密钥材料，但是他们可以对密钥执行操作，使他们能够使用加载到代理中的身份进行身份验证。

[`-a`](#a)

禁用身份验证代理连接的转发。

[`-B`](#B) bind\_interface

在尝试连接到目标主机之前绑定到 bind\_interface 的地址。 这仅对具有多个地址的系统有用。

[`-b`](#b) bind\_address

使用本地机器上的 bind\_address 作为连接的源地址。 仅对具有多个地址的系统有用。

[`-C`](#C)

请求压缩所有数据（包括标准输入、标准输出、标准错误和转发 X11、TCP 和 UNIX\-domain 域连接的数据）。 压缩算法与 gzip(1) 使用的相同。 压缩在调制解调器线路和其他慢速连接上是可取的，但只会减慢快速网络上的速度。 可以在配置文件中逐个主机设置默认值；请参阅 `Compression` 选项。

[`-c`](#c) cipher\_spec

选择用于加密会话的密码规范。 cipher\_spec 是按优先顺序列出的以逗号分隔的密码列表。 有关详细信息，请参阅 ssh\_config(5) 中的 `Ciphers` 关键字。

[`-D`](#D) \[bind\_address:\]port

指定本地 “dynamic” 应用程序级端口转发。 这通过分配一个套接字来侦听本地端的 port 来工作，可选地绑定到指定的 bind\_address 。 每当与此端口建立连接时，都会通过安全通道转发连接，然后使用应用程序协议来确定从远程机器连接到哪里。 目前支持 SOCKS4 和 SOCKS5 协议， `ssh` 将充当 SOCKS 服务器。 只有 root 可以转发特权端口。 动态端口转发也可以在配置文件中指定。

可以通过将地址括在方括号中来指定 IPv6 地址。 只有超级用户可以转发特权端口。 默认情况下，本地端口根据 `GatewayPorts` 设置进行绑定。 但是，可以使用显式 bind\_address 将连接绑定到特定地址。 “localhost” 的 bind\_address 表示监听端口只绑定本地使用，而空地址或 ‘\*’ 表示该端口应该可用于所有接口。

[`-E`](#E) log\_file

将调试日志附加到 log\_file 而不是标准错误。

[`-e`](#e) escape\_char

为带有 pty 的会话设置转义字符（默认值： ‘`~`’ ) 。 转义字符仅在行首被识别。 转义字符后跟一个点 (‘`.`’) 关闭连接；后跟 control-Z 挂起连接；然后它自己发送一次转义字符。 将字符设置为 “none” 会禁用任何转义并使会话完全透明。

[`-F`](#F) configfile

指定替代的每用户配置文件。 如果在命令行中给出了配置文件，系统范围的配置文件 (/etc/ssh/ssh\_config) 将被忽略。 每个用户配置文件的默认值是 ~/.ssh/config 。

[`-f`](#f)

在命令执行之前请求 `ssh` 进入后台。 如果 `ssh` 将要求输入密码或密码，但用户希望它在后台使用，这很有用。 这意味着 `-n` 。 在远程站点启动 X11 程序的推荐方法是使用 `ssh -f host xterm` 之类的方法。

如果 `ExitOnForwardFailure` 配置选项设置为 “yes”, 则使用 `-f` 启动的客户端将等待所有远程端口转发成功建立，然后将其置于后台。

[`-G`](#G)

在评估 `Host` 和 `Match` 块并退出后，导致 `ssh` 打印其配置。

[`-g`](#g)

允许远程主机连接到本地转发端口。 如果在多路复用连接上使用，则必须在主进程上指定此选项。

[`-I`](#I) pkcs11

指定 PKCS#11 共享库 `ssh` 应用于与提供用户私有 RSA 密钥的 PKCS#11 令牌通信。

[`-i`](#i) identity\_file

选择从中读取用于公钥认证的身份（私钥）的文件。 默认为 ~/.ssh/id\_dsa, ~/.ssh/id\_ecdsa, ~/.ssh/id\_ed25519 和 ~/.ssh/id\_rsa 。 身份文件也可以在配置文件中基于每个主机指定。 可以有多个 `-i` 选项（以及在配置文件中指定的多个身份）。 如果 `CertificateFile` 指令没有明确指定证书， `ssh` 还将尝试从通过将 \-cert.pub 附加到身份文件名获得的文件名中加载证书信息。

[`-J`](#J) destination

连接到目标主机，方法是首先与 destination 描述的跳转主机建立 `ssh` 连接，然后从那里建立到最终目标的 TCP 转发。 可以指定多个跳转跃点，用逗号分隔。 这是指定 `ProxyJump` 配置指令的快捷方式。

[`-K`](#K)

启用基于 GSSAPI 的身份验证并将 GSSAPI 凭据转发（委托）到服务器。

[`-k`](#k)

禁用将 GSSAPI 凭据转发（委托）到服务器。

[`-L`](#L) \[bind\_address:\]port:host:hostport

[`-L`](#L_2) \[bind\_address:\]port:remote\_socket

[`-L`](#L_3) local\_socket:host:hostport

[`-L`](#L_4) local\_socket:remote\_socket

指定到本地（客户端）主机上的给定 TCP 端口或 Unix 套接字的连接将被转发到远程端的给定主机和端口或 Unix 套接字。 这通过分配一个套接字来侦听本地端的 TCP port （可选地绑定到指定的 bind\_address 或 Unix 套接字来工作。 每当与本地端口或套接字建立连接时，都会通过安全通道转发连接，并从远程计算机与 host 端口 hostport 或 Unix 套接字 remote\_socket 建立连接。

端口转发也可以在配置文件中指定。 只有超级用户可以转发特权端口。 可以通过将地址括在方括号中来指定 IPv6 地址。

默认情况下，本地端口根据 `GatewayPorts` 设置进行绑定。 但是，可以使用显式 bind\_address 将连接绑定到特定地址。 “localhost” 的 bind\_address 表示监听端口只绑定本地使用，而空地址或 ‘\*’ 表示该端口应该可用于所有接口。

[`-l`](#l) login\_name

指定在远程计算机上登录的用户。 这也可以在配置文件中基于每个主机指定。

[`-M`](#M)

将 `ssh` 客户端置于 “master” 模式以进行连接共享。 多个 `-M` 选项将 `ssh` 置于 “master” 模式，但需要在每次更改多路复用状态的操作（例如打开新会话）之前使用 ssh-askpass(1) 进行确认。 详见 ssh\_config(5) 中对 `ControlMaster` 的描述。

[`-m`](#m) mac\_spec

MAC（消息验证码）算法的逗号分隔列表，按优先顺序指定。 有关详细信息，请参阅 `MACs` 关键字。

[`-N`](#N)

不要执行远程命令。 这对于仅转发端口很有用。

[`-n`](#n)

从 /dev/null 重定向标准输入（实际上，阻止从标准输入读取）。 这必须在 `ssh` 在后台运行时使用。 一个常见的技巧是使用它在远程机器上运行 X11 程序。 例如， `ssh -n shadows.cs.hut.fi emacs &` 将在 shadows.cs.hut.fi 上启动一个 emacs，X11 连接将通过加密通道自动转发。 `ssh` 程序将被置于后台。 （如果 `ssh` 需要询问密码或密码短语，这将不起作用；另请参阅 `-f` 选项。）

[`-O`](#O) ctl\_cmd

控制一个活动的连接多路复用主进程。 指定 `-O` 选项时，将解释 ctl\_cmd 参数并将其传递给主进程。 有效命令有： “check” (检查主进程是否正在运行), “forward” (请求转发而不执行命令), “cancel” (取消转发), “exit” (请求主进程退出) 和 “stop” (请求主设备停止接受进一步的多路复用请求)。

[`-o`](#o) option

可用于以配置文件中使用的格式给出选项。 这对于指定没有单独命令行标志的选项很有用。 有关下面列出的选项及其可能值的完整详细信息，请参阅 ssh\_config(5) 。

AddKeysToAgent

AddressFamily

BatchMode

BindAddress

CanonicalDomains

CanonicalizeFallbackLocal

CanonicalizeHostname

CanonicalizeMaxDots

CanonicalizePermittedCNAMEs

CASignatureAlgorithms

CertificateFile

ChallengeResponseAuthentication

CheckHostIP

Ciphers

ClearAllForwardings

Compression

ConnectionAttempts

ConnectTimeout

ControlMaster

ControlPath

ControlPersist

DynamicForward

EscapeChar

ExitOnForwardFailure

FingerprintHash

ForwardAgent

ForwardX11

ForwardX11Timeout

ForwardX11Trusted

GatewayPorts

GlobalKnownHostsFile

GSSAPIAuthentication

GSSAPIDelegateCredentials

HashKnownHosts

Host

HostbasedAuthentication

HostbasedKeyTypes

HostKeyAlgorithms

HostKeyAlias

HostName

IdentitiesOnly

IdentityAgent

IdentityFile

IPQoS

KbdInteractiveAuthentication

KbdInteractiveDevices

KexAlgorithms

LocalCommand

LocalForward

LogLevel

MACs

Match

NoHostAuthenticationForLocalhost

NumberOfPasswordPrompts

PasswordAuthentication

PermitLocalCommand

PKCS11Provider

Port

PreferredAuthentications

ProxyCommand

ProxyJump

ProxyUseFdpass

PubkeyAcceptedKeyTypes

PubkeyAuthentication

RekeyLimit

RemoteCommand

RemoteForward

RequestTTY

SendEnv

ServerAliveInterval

ServerAliveCountMax

SetEnv

StreamLocalBindMask

StreamLocalBindUnlink

StrictHostKeyChecking

TCPKeepAlive

Tunnel

TunnelDevice

UpdateHostKeys

User

UserKnownHostsFile

VerifyHostKeyDNS

VersionAddendum

VisualHostKey

XAuthLocation

[`-p`](#p) port

远程主机上要连接的端口。 这可以在配置文件中基于每个主机指定。

[`-Q`](#Q) query\_option

查询指定版本 2 支持的算法的 `ssh` 。 可用的功能有： cipher (支持的对称密码), cipher-auth (支持经过身份验证的加密的支持的对称密码), help (支持与 `-Q` 标志一起使用的查询术语), mac (支持的消息完整性代码), kex (密钥交换算法), key (密钥类型), key-cert (证书密钥类型), key-plain (非证书密钥类型), protocol-version (支持的SSH协议版本) 和 sig (支持的签名算法)。

[`-q`](#q)

静音模式。 导致大多数警告和诊断消息被抑制。

[`-R`](#R) \[bind\_address:\]port:host:hostport

[`-R`](#R_2) \[bind\_address:\]port:local\_socket

[`-R`](#R_3) remote\_socket:host:hostport

[`-R`](#R_4) remote\_socket:local\_socket

[`-R`](#R_5) \[bind\_address:\]port

指定到远程（服务器）主机上给定 TCP 端口或 Unix 套接字的连接将被转发到本地端。

这通过分配一个套接字来监听 port 或远程端的 Unix 套接字来工作。 每当与此端口或 Unix 套接字建立连接时，都会通过安全通道转发连接，并从本地计算机建立到由 host 端口 hostport 或 local\_socket, 指定的显式目标，或者，如果没有显式目标指定后， `ssh` 将充当 SOCKS 4/5 代理并将连接转发到远程 SOCKS 客户端请求的目的地。

端口转发也可以在配置文件中指定。 只有在远程计算机上以 root 身份登录时才能转发特权端口。 可以通过将地址括在方括号中来指定 IPv6 地址。

默认情况下，服务器上的 TCP 侦听套接字将仅绑定到环回接口。这可以通过指定一个 bind\_address 来覆盖。 空的 bind\_address 或地址 ‘`*`’ 表示远程套接字应侦听所有接口。 只有启用了服务器的 `GatewayPorts` 选项（请参阅 sshd\_config(5) ），指定远程 bind\_address 才会成功。

如果 port 参数为 ‘`0`’, 监听端口将在服务器上动态分配并在运行时报告给客户端。 当与 `-O forward` 一起使用时，分配的端口将被打印到标准输出。

[`-S`](#S) ctl\_path

指定用于连接共享的控制套接字的位置，或字符串 “none” 以禁用连接共享。 详见 ssh\_config(5) 中对 `ControlPath` 和 `ControlMaster` 的描述。

[`-s`](#s)

可用于请求调用远程系统上的子系统。 子系统有助于将 SSH 用作其他应用程序的安全传输（例如 sftp(1) ) 。 子系统被指定为远程命令。

[`-T`](#T)

禁用伪终端分配。

[`-t`](#t)

强制伪终端分配。 这可用于在远程机器上执行任意基于屏幕的程序，这非常有用，例如在实现菜单服务时。 多个 `-t` 选项强制分配 tty，即使 `ssh` 没有本地 tty。

[`-V`](#V)

显示版本号并退出。

[`-v`](#v)

详细模式。 使 `ssh` 打印有关其进度的调试消息。 这有助于调试连接、身份验证和配置问题。 多个 `-v` 选项会增加详细程度。 最大值为 3。

[`-W`](#W) host:port

请求将客户端上的标准输入和输出通过安全通道转发到 port 上的 host 。 隐含 `-N` `-、` `-T` `-、` `ExitOnForwardFailure` 和 `ClearAllForwardings`, 尽管这些可以在配置文件中覆盖或使用 `-o` 命令行选项。

[`-w`](#w) local\_tun\[:remote\_tun\]

使用客户端 (local\_tun) 和服务器 (remote\_tun) 之间的指定 tun(4) 设备请求隧道设备转发。

这些设备可以通过数字 ID 或关键字 “any” 来指定，它使用下一个可用的隧道设备。 如果未指定 remote\_tun ，则默认为 “any” 。 另请参见 ssh\_config(5) 中的 `Tunnel` 和 `TunnelDevice` 指令。

如果 `Tunnel` 指令未设置，它将被设置为默认隧道模式，即 “point-to-point” 。 如果需要不同的 `Tunnel` 转发模式，则应在 `-w` 之前指定。

[`-X`](#X)

启用 X11 转发。 这也可以在配置文件中基于每个主机指定。

应谨慎启用 X11 转发。具有绕过远程主机文件权限的用户（对于用户的X授权数据库）可以通过转发连接访问本地X11显示器。 然后，攻击者可能能够执行诸如击键监控之类的活动。

因此，X11 转发默认受到 X11 SECURITY 扩展限制。 有关更多信息，请参阅 ssh\_config(5) 中的 `ssh` `-Y` 选项和 `ForwardX11Trusted` 指令。

[`-x`](#x)

禁用 X11 转发。

[`-Y`](#Y)

启用受信任的 X11 转发。 受信任的 X11 转发不受 X11 SECURITY 扩展控制的约束。

[`-y`](#y)

使用 syslog(3) 系统模块发送日志信息。 默认情况下，此信息被发送到 stderr。

`ssh` 还可以从每个用户的配置文件和系统范围的配置文件中获取配置数据。 文件格式和配置选项在 ssh\_config(5) 中描述。

[验证](#__u9A8C___u8BC1_)
=======================

OpenSSH SSH 客户端支持 SSH 协议 2。

可用于身份验证的方法有：基于 GSSAPI 的身份验证、基于主机的身份验证、公钥身份验证、质询响应身份验证和密码身份验证。 身份验证方法按上面指定的顺序尝试，但 `PreferredAuthentications` 可用于更改默认顺序。

基于主机的身份验证工作如下：如果用户登录的机器在远程机器上的 /etc/hosts.equiv 或 /etc/shosts.equiv 中列出，并且双方的用户名相同，或者如果文件 ~/.rhosts 或 ~/.shosts 存在于远程计算机上用户的主目录中，并包含一行包含客户端计算机名称和该计算机上用户名称的行，该用户被视为登录。 此外，服务器 _必须_ 能够验证客户端的主机密钥（请参阅下面的 /etc/ssh/ssh\_known\_hosts 和 ~/.ssh/known\_hosts 的描述）才能允许登录。 这种身份验证方法可以消除由于 IP 欺骗、DNS 欺骗和路由欺骗造成的安全漏洞。 \[管理员注意： /etc/hosts.equiv 、 ~/.rhosts 和一般的 rlogin/rsh 协议本质上是不安全的，如果需要安全应该禁用。\]

公钥认证的工作原理如下：该方案基于公钥密码术，使用加密和解密使用单独的密钥完成的密码系统，从加密密钥中导出解密密钥是不可行的。 这个想法是每个用户创建一个公钥/私钥对来进行身份验证。 服务器知道公钥，只有用户知道私钥。 `ssh` 使用 DSA、ECDSA、Ed25519 或 RSA 算法之一自动实现公钥认证协议。 ssl(8) 的历史部分包含对 DSA 和 RSA 算法的简要讨论。

文件 ~/.ssh/authorized\_keys 列出了允许登录的公钥。当用户登录时， `ssh` 程序告诉服务器它想使用哪个密钥对进行身份验证。 客户端证明它可以访问私钥，服务器检查相应的公钥是否被授权接受该帐户。

在使用不同的方法完成认证后，服务器可能会通知客户端阻止公钥认证成功的错误。 这些可以通过将 `LogLevel` 增加到 `DEBUG` 或更高来查看（例如，通过使用 `-v` 标志）。

用户通过运行 ssh-keygen(1) 创建他/她的密钥对。 这会将私钥存储在 ~/.ssh/id\_dsa (DSA), ~/.ssh/id\_ecdsa (ECDSA), ~/.ssh/id\_ed25519 (Ed25519) 或 ~/.ssh/id\_rsa (RSA) 中并存储公共键入 ~/.ssh/id\_dsa.pub (DSA), ~/.ssh/id\_ecdsa.pub (ECDSA), ~/.ssh/id\_ed25519.pub (Ed25519) 或 ~/.ssh/id\_rsa.pub (RSA) 在用户的主目录中。 然后，用户应该将公钥复制到远程机器上他/她的主目录中的 ~/.ssh/authorized\_keys 。 authorized\_keys 文件对应于传统的 ~/.rhosts 文件，每行有一个密钥，尽管行可能很长。 之后，用户无需输入密码即可登录。

公钥认证的变体以证书认证的形式提供：使用签名证书而不是一组公钥/私钥。 这样做的好处是可以使用单个受信任的证书颁发机构来代替许多公钥/私钥。 有关更多信息，请参阅 ssh-keygen(1) 的证书部分。

使用公钥或证书身份验证最方便的方法可能是使用身份验证代理。 有关详细信息，请参阅 ssh-agent(1) 和（可选） ssh\_config(5) 中的 `AddKeysToAgent` 指令。

质询-响应认证的工作原理如下：服务器发送任意 “challenge” 文本，并提示响应。 质询-响应身份验证的示例包括 BSD 身份验证（参见 login.conf(5)) 和 PAM（一些非 non-OpenBSD 系统）。

最后，如果其他身份验证方法失败， `ssh` 会提示用户输入密码。 将密码发送到远程主机进行检查；但是，由于所有通信都是加密的，因此在网络上收听的人无法看到密码。

`ssh` 自动维护并检查一个数据库，该数据库包含它曾经使用过的所有主机的标识。 主机密钥存储在用户主目录的 ~/.ssh/known\_hosts 中。 此外，文件 /etc/ssh/ssh\_known\_hosts 会自动检查已知主机。 任何新主机都会自动添加到用户文件中。 如果主机的标识发生变化， `ssh` 会对此发出警告并禁用密码验证，以防止服务器欺骗或中间人攻击，否则这些攻击可用于规避加密。 `StrictHostKeyChecking` 选项可用于控制对主机密钥未知或已更改的计算机的登录。

当服务器接受用户的身份时，服务器要么在非交互式会话中执行给定的命令，要么，如果没有指定命令，则登录到机器并为用户提供一个普通的 shell 作为交互式会话。 所有与远程命令或 shell 的通信都将被自动加密。

如果请求交互式会话，则默认情况下， `ssh` 只会在客户端有交互式会话时请求一个伪终端 (pty)。 标志 `-T` 和 `-t` 可用于覆盖此行为。

如果已分配伪终端，则用户可以使用下面提到的转义字符。

如果没有分配伪终端，则会话是透明的，可用于可靠地传输二进制数据。 在大多数系统上，将转义字符设置为 “none” 也会使会话透明，即使使用了 tty。

当远程机器上的命令或 shell 退出并且所有 X11 和 TCP 连接都已关闭时，会话终止。

[转义字符](#__u8F6C___u4E49___u5B57___u7B26_)
=========================================

当请求伪终端时， `ssh` 通过使用转义字符支持许多功能。

当请求伪终端时， `~~` 通过使用转义字符支持许多功能。 单个波浪号字符可以发送为 `~~` 或在波浪号后跟一个字符而不是下面描述的字符。 转义字符必须始终跟随换行符才能被解释为特殊字符。 可以使用 `EscapeChar` 配置指令在配置文件中更改转义字符，也可以通过 `-e` 选项在命令行中更改转义字符。

支持的转义（假设默认的 ‘`~`’) 是:

[`~.`](#~.)

断开。

[`~^Z`](#~_Z)

后台 `ssh` 。

[`~#`](#~_)

列出转发的连接。

[`~&`](#~&)

等待转发连接 /X11 会话终止时注销时的后台 `ssh` 。

[`~?`](#~?)

显示转义字符列表。

[`~B`](#~B)

向远程系统发送 BREAK（仅当对等方支持时才有用）。

[`~C`](#~C)

打开命令行。 目前，这允许使用 `-L` `-、` `-R` 和 `-D` 选项添加端口转发（见上文）。 它还允许取消现有的端口转发，其中 `-KL`\[bind\_address:\]port 用于本地, `-KR`\[bind\_address:\]port 端口用于远程, `-KD` \[bind\_address:\]port 用于动态端口转发。 如果在 ssh\_config(5) 中启用了 `PermitLocalCommand` 选项， `!`command 允许用户执行本地命令。 使用 `-h` 选项可获得基本帮助。

[`~R`](#~R)

请求重新加密连接（仅在对等方支持时才有用）。

[`~V`](#~V)

将错误写入 stderr 时降低详细程度 (`LogLevel`) 。

[`~v`](#~v)

将错误写入 stderr 时增加详细程度 (`LogLevel`) 。

[TCP 转发](#TCP___u8F6C___u53D1_)
===============================

可以在命令行或配置文件中指定通过安全通道转发任意 TCP 连接。 TCP 转发的一种可能应用是与邮件服务器的安全连接。另一个是通过防火墙。

在下面的示例中，我们研究了 IRC 客户端和服务器之间的加密通信，即使 IRC 服务器不直接支持加密通信。 它的工作原理如下：用户使用 `ssh` 连接到远程主机，指定用于将连接转发到远程服务器的端口。 之后就可以在客户端机器上启动要加密的服务，连接到同一个本地端口， `ssh` 会加密转发连接。

以下示例将 IRC 会话从客户端机器 “127.0.0.1” （localhost）传送到远程服务器 “server.example.com”:

$ ssh -f -L 1234:localhost:6667 server.example.com sleep 10 $ irc -c '#users' -p 1234 pinky 127.0.0.1 

这通过隧道连接到 IRC 服务器 “server.example.com”, 加入频道 “#users”, 昵称 “pinky”, 使用端口 1234。 使用哪个端口无关紧要，只要它大于 1023（请记住，只有 root 可以打开特权端口上的套接字）并且不与任何已在使用的端口冲突。 连接被转发到远程服务器上的端口 6667，因为这是 IRC 服务的标准端口。

`-f` 选项背景 `ssh` 和远程命令 “sleep 10” 指定允许一段时间（在示例中为 10 秒）来启动要通过隧道传输的服务。 如果在指定时间内没有建立连接， `ssh` 将退出。

[X11 转发](#X11___u8F6C___u53D1_)
===============================

如果 `ForwardX11` 变量设置为 “yes” (或参见上面 `-X` `-、` `-x` 和 `-Y` 选项的说明）并且用户正在使用 X11（设置了 `DISPLAY` 环境变量），则与 X11 的连接显示自动转发到远程端，任何从 shell（或命令）启动的 X11 程序都将通过加密通道，并从本地机器连接到真正的 X 服务器。 用户不应手动设置 `DISPLAY` 。可以在命令行或配置文件中配置 X11 连接的转发。

`DISPLAY` 设置的 `ssh` 值将指向服务器机器，但显示编号大于零。 这是正常的，因为 `ssh` 在服务器机器上创建了一个 “proxy” X 服务器，用于通过加密通道转发连接。

`ssh` 也会在服务器机器上自动设置 Xauthority 数据。 为此，它会生成一个随机的授权cookie，将其存储在服务器上的Xauthority中，并验证任何转发的连接是否携带此cookie，并在连接打开时将其替换为真实的cookie。 真正的身份验证 cookie 永远不会发送到服务器机器（并且没有 cookie 以明文形式发送）。

如果 `ForwardAgent` 变量设置为 “yes” (或参见上面 `-A` 和 `-a` 选项的描述）并且用户正在使用身份验证代理，则与代理的连接会自动转发到远程端。

[验证主机密钥](#__u9A8C___u8BC1___u4E3B___u673A___u5BC6___u94A5_)
===========================================================

首次连接到服务器时，会向用户显示服务器公钥的指纹（除非已禁用 `StrictHostKeyChecking` 选项）。 可以使用 ssh-keygen(1) 确定指纹：

`$ ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key`

如果指纹是已知的，则可以对其进行匹配，并且可以接受或拒绝密钥。 如果服务器的传统 (MD5) 指纹可用，则可以使用 ssh-keygen(1) `-E` 选项将指纹算法降级以匹配。

由于仅通过查看指纹字符串很难比较主机密钥，因此还支持使用 _random art_ 直观地比较主机密钥。 通过将 `VisualHostKey` 选项设置为 “yes”, 每次登录服务器时都会显示一个小的 ASCII 图形，无论会话本身是否是交互式的。 通过学习已知服务器产生的模式，用户可以很容易地发现主机密钥在显示完全不同的模式时发生了变化。 然而，因为这些模式不是明确的，所以看起来与记忆的模式相似的模式只会给出主机密钥相同的良好概率，不能保证证明。

要获取所有已知主机的指纹列表及其随机艺术，可以使用以下命令行：

`$ ssh-keygen -lv -f ~/.ssh/known_hosts`

如果指纹未知，则可以使用另一种验证方法：由 DNS 验证的 SSH 指纹。 一个额外的资源记录 (RR)，SSHFP，被添加到一个区域文件中，并且连接的客户端能够将指纹与所提供的密钥的指纹进行匹配。

在此示例中，我们将客户端连接到服务器 “host.example.com” 。 SSHFP 资源记录应首先添加到 host.example.com 的区域文件中：

$ ssh-keygen -r host.example.com. 

必须将输出行添加到区域文件中。 要检查该区域是否正在回答指纹查询：

`$ dig -t SSHFP host.example.com`

最后客户端连接：

$ ssh -o "VerifyHostKeyDNS ask" host.example.com \[...\] Matching host key fingerprint found in DNS. Are you sure you want to continue connecting (yes/no)? 

有关详细信息，请参阅 ssh\_config(5) 中的 `VerifyHostKeyDNS` 选项。

[基于 SSH 的虚拟私有网络](#__u57FA___u4E8E__SSH___u7684___u865A___u62DF___u79C1___u6709___u7F51___u7EDC_)
================================================================================================

`ssh` 包含对使用 tun(4) 网络伪设备的虚拟专用网络 (VPN) 隧道的支持，允许安全地加入两个网络。 sshd\_config(5) 配置选项 `PermitTunnel` 控制服务器是否支持此功能，以及在什么级别（第 2 层或第 3 层流量）。

以下示例将使用从 10.1.1.1 到 10.1.1.2 的点对点连接将客户端网络 10.0.50.0/24 与远程网络 10.0.99.0/24 连接，前提是运行在网关上的 SSH 服务器到远程网络，在 192.168.1.15，允许它。

在客户端：

\# ssh -f -w 0:1 192.168.1.15 true # ifconfig tun0 10.1.1.1 10.1.1.2 netmask 255.255.255.252 # route add 10.0.99.0/24 10.1.1.2 

在服务器上：

\# ifconfig tun1 10.1.1.2 10.1.1.1 netmask 255.255.255.252 # route add 10.0.50.0/24 10.1.1.1 

客户端访问可以通过 /root/.ssh/authorized\_keys 文件（见下文）和 `PermitRootLogin` 服务器选项进行更精细的调整。 如果 `PermitRootLogin` 设置为 “forced-commands-only” ，则以下条目将允许来自用户 “jane” 的 tun(4) 设备 1 和来自用户 “john” 的 tun 设备 2 上的连接：

tunnel="1",command="sh /etc/netstart tun1" ssh-rsa ... jane tunnel="2",command="sh /etc/netstart tun2" ssh-rsa ... john 

由于基于 SSH 的设置需要相当多的开销，因此它可能更适合临时设置，例如无线 VPN。 ipsecctl(8) 和 isakmpd(8) 等工具可以更好地提供更永久的 VPN。

[环境](#__u73AF___u5883_)
=======================

`ssh` 通常会设置以下环境变量：

[`DISPLAY`](#DISPLAY)

[`DISPLAY`](#DISPLAY_2) 变量指示 X11 服务器的位置。 它由 `ssh` 自动设置为指向 “hostname:n” 形式的值，其中 “hostname” 表示运行 shell 的主机， ‘n’ 是一个 ≥ 1 的整数。 `ssh` 使用这个特殊值通过安全通道转发 X11 连接。 用户通常不应显式设置 `DISPLAY` ，因为这会使 X11 连接不安全（并要求用户手动复制任何所需的授权 cookie）。

[`HOME`](#HOME)

设置为用户主目录的路径。

[`LOGNAME`](#LOGNAME)

[`USER`](#USER) 的同义词；设置为与使用此变量的系统兼容。

[`MAIL`](#MAIL)

设置为用户邮箱的路径。

[`PATH`](#PATH)

设置为编译 `ssh` 时指定的默认 `PATH`, 。

[`SSH_ASKPASS`](#SSH_ASKPASS)

如果 `ssh` 需要密码，如果它是从终端运行的，它将从当前终端读取密码。 如果 `ssh` 没有与之关联的终端，但设置了 `DISPLAY` 和 `SSH_ASKPASS` ，它将执行 `SSH_ASKPASS` 指定的程序并打开 X11 窗口以读取密码。 这在从 .xsession 或相关脚本调用 `ssh` 时特别有用。 （请注意，在某些机器上，可能需要从 /dev/null 重定向输入以使其工作。）

[`SSH_AUTH_SOCK`](#SSH_AUTH_SOCK)

标识用于与代理通信的 UNIX\-domain 套接字的路径。

[`SSH_CONNECTION`](#SSH_CONNECTION)

标识连接的客户端和服务器端。 该变量包含四个以空格分隔的值：客户端 IP 地址、客户端端口号、服务器 IP 地址和服务器端口号。

[`SSH_ORIGINAL_COMMAND`](#SSH_ORIGINAL_COMMAND)

如果执行强制命令，此变量包含原始命令行。 它可用于提取原始参数。

[`SSH_TTY`](#SSH_TTY)

这设置为与当前 shell 或命令关联的 tty（设备路径）的名称。 如果当前会话没有 tty，则不设置此变量。

[`SSH_TUNNEL`](#SSH_TUNNEL)

如果客户端请求隧道转发，则可以由 sshd(8) 设置为包含分配的接口名称。

[`SSH_USER_AUTH`](#SSH_USER_AUTH)

可选地由 sshd(8) 设置，该变量可能包含一个文件的路径名，该文件列出了在建立会话时成功使用的身份验证方法，包括使用的任何公钥。

[`TZ`](#TZ)

如果在启动守护程序时设置了此变量（即守护程序将值传递给新连接），则设置此变量以指示当前时区。

[`USER`](#USER_2)

设置为登录用户的名称。

此外， `ssh` 读取 ~/.ssh/environment, 如果文件存在并且允许用户更改其环境，则将格式为 “VARNAME=value” 的行添加到环境中。 有关详细信息，请参阅 sshd\_config(5) 中的 `PermitUserEnvironment` 选项。

[文件](#__u6587___u4EF6_)
=======================

~/.rhosts

此文件用于基于主机的身份验证（见上文）。 在某些机器上，如果用户的主目录位于 NFS 分区上，则该文件可能需要全世界可读，因为 sshd(8) 以 root 身份读取它。 此外，此文件必须归用户所有，并且不得对其他任何人具有写权限。 大多数机器的推荐权限是用户的读/写权限，其他人无法访问。

~/.shosts

该文件的使用方式与 .rhosts 完全相同，但允许基于主机的身份验证，而不允许使用 rlogin/rsh 登录。

~/.ssh/

此目录是所有用户特定配置和身份验证信息的默认位置。 没有一般要求将此目录的全部内容保密，但建议的权限是用户的读/写/执行权限，其他人无法访问。

~/.ssh/authorized\_keys

列出可用于以该用户身份登录的公钥（DSA、ECDSA、Ed25519、RSA）。 该文件的格式在 sshd(8) 手册页中描述。 该文件不是高度敏感的，但推荐的权限是用户的读/写权限，其他人无法访问。

~/.ssh/config

这是每个用户的配置文件。 文件格式和配置选项在 ssh\_config(5) 中描述。 由于存在滥用的可能性，因此该文件必须具有严格的权限：用户读/写，其他人不可写。

~/.ssh/environment

包含环境变量的附加定义；参见上面的 [环境](#__u73AF___u5883_) 。

~/.ssh/id\_dsa

~/.ssh/id\_ecdsa

~/.ssh/id\_ed25519

~/.ssh/id\_rsa

包含用于身份验证的私钥。 这些文件包含敏感数据，用户应该可以读取，但其他人不能访问（读/写/执行）。 如果其他人可以访问， `ssh` 将简单地忽略私钥文件。 可以在生成密钥时指定密码短语，该密钥将用于使用 AES-128 加密此文件的敏感部分。

~/.ssh/id\_dsa.pub

~/.ssh/id\_ecdsa.pub

~/.ssh/id\_ed25519.pub

~/.ssh/id\_rsa.pub

包含用于身份验证的公钥。 这些文件不敏感，任何人都可以（但不必）读取。

~/.ssh/known\_hosts

包含用户已登录的所有主机的主机密钥列表，这些主机尚未在系统范围内的已知主机密钥列表中。 有关此文件格式的更多详细信息，请参见 sshd(8) 。

~/.ssh/rc

此文件中的命令在用户登录时由 `ssh` 执行，就在用户的 shell（或命令）启动之前。 有关更多信息，请参阅 sshd(8) 手册页。

/etc/hosts.equiv

此文件用于基于主机的身份验证（见上文）。它应该只能由 root 写入。

/etc/shosts.equiv

该文件的使用方式与 hosts.equiv 完全相同，但允许基于主机的身份验证，而不允许使用 rlogin/rsh 登录。

/etc/ssh/ssh\_config

系统范围的配置文件。 文件格式和配置选项在 ssh\_config(5) 中描述。

/etc/ssh/ssh\_host\_key

/etc/ssh/ssh\_host\_dsa\_key

/etc/ssh/ssh\_host\_ecdsa\_key

/etc/ssh/ssh\_host\_ed25519\_key

/etc/ssh/ssh\_host\_rsa\_key

这些文件包含主机密钥的私有部分，用于基于主机的身份验证。

/etc/ssh/ssh\_known\_hosts

已知主机密钥的系统范围列表。 该文件应由系统管理员准备，以包含组织中所有机器的公共主机密钥。 它应该是世界可读的。 有关此文件格式的更多详细信息，请参见 sshd(8) 。

/etc/ssh/sshrc

此文件中的命令在用户登录时由 `ssh` 执行，就在用户的 shell（或命令）启动之前。 有关更多信息，请参阅 sshd(8) 手册页。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

`ssh` 以远程命令的退出状态退出，如果发生错误，则以 255 退出。

[参见](#__u53C2___u89C1_)
=======================

scp(1), sftp(1), ssh-add(1), ssh-agent(1), ssh-keygen(1), ssh-keyscan(1), tun(4), ssh\_config(5), ssh-keysign(8), sshd(8)

[标准](#__u6807___u51C6_)
=======================

S. Lehtinen and C. Lonvick, 安全 Shell (SSH) 协议分配编号, RFC 4250, January 2006.

T. Ylonen and C. Lonvick, 安全 Shell (SSH) 协议架构, RFC 4251, January 2006.

T. Ylonen and C. Lonvick, 安全 Shell (SSH) 身份验证协议, RFC 4252, January 2006.

T. Ylonen and C. Lonvick, 安全 Shell (SSH) 传输层协议, RFC 4253, January 2006.

T. Ylonen and C. Lonvick, 安全 Shell (SSH) 连接协议, RFC 4254, January 2006.

J. Schlyter and W. Griffin, 使用 DNS 安全地发布安全 Shell (SSH) 密钥指纹, RFC 4255, January 2006.

F. Cusack and M. Forssen, 安全外壳协议 (SSH) 的通用消息交换身份验证, RFC 4256, January 2006.

J. Galbraith and P. Remaker, 安全 Shell (SSH) 会话通道中断扩展, RFC 4335, January 2006.

M. Bellare, T. Kohno, and C. Namprempre, 安全 Shell (SSH) 传输层加密模式, RFC 4344, January 2006.

B. Harris, 安全 Shell (SSH) 传输层协议的改进的 Arcfour 模式, RFC 4345, January 2006.

M. Friedl, N. Provos, and W. Simpson, Diffie-Hellman Group Exchange for the Secure Shell (SSH) 传输层协议, RFC 4419, March 2006.

J. Galbraith and R. Thayer, 安全 Shell (SSH) 公钥文件格式, RFC 4716, November 2006.

D. Stebila and J. Green, 安全外壳传输层中的椭圆曲线算法集成, RFC 5656, December 2009.

A. Perrig and D. Song, 哈希可视化：提高现实世界安全性的新技术, 1999, International Workshop on Cryptographic Techniques and E-Commerce (CrypTEC '99).

[作者](#__u4F5C___u8005_)
=======================

OpenSSH 是 Tatu Ylonen 的原始免费 ssh 1.2.12 版本的衍生版本。 Aaron Campbell、Bob Beck、Markus Friedl、Niels Provos、Theo de Raadt 和 Dug Song 删除了许多错误，重新添加了新功能并创建了 OpenSSH。 Markus Friedl 贡献了对 SSH 协议版本 1.5 和 2.0 的支持。

September 20, 2018

FreeBSD 13.1-RELEASE