# ssh.1

`ssh` — OpenSSH 远程登录客户端

## 名称

`ssh`

## 概要

`ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address] [-c cipher_spec] [-D [bind_address:]port] [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file] [-J destination] [-L address] [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-P tag] [-p port] [-R address] [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]] destination [command [argument ...]]`

`ssh [-Q query_option]`

## 描述

`ssh`（SSH 客户端）是用于登录远程机器并在远程机器上执行命令的程序。它旨在通过不安全的网络在两个不受信任的主机之间提供安全的加密通信。X11 连接、任意 TCP 端口和 UNIX 域套接字也可以通过安全通道转发。

`ssh` 连接并登录到指定的 `destination`，可指定为 `[user@]hostname` 或形式为 `ssh://[user@]hostname[:port]` 的 URI。用户必须使用以下几种方法之一向远程机器证明其身份（见下文）。

如果指定了 `command`，它将在远程主机上执行，而非登录 shell。可将完整命令行指定为 `command`，也可带额外参数。如果提供参数，参数将以空格分隔附加到命令后，然后发送到服务器执行。

选项如下：

**AddKeysToAgent**

**AddressFamily**

**BatchMode**

**BindAddress**

**BindInterface**

**CASignatureAlgorithms**

**CanonicalDomains**

**CanonicalizeFallbackLocal**

**CanonicalizeHostname**

**CanonicalizeMaxDots**

**CanonicalizePermittedCNAMEs**

**CertificateFile**

**ChannelTimeout**

**CheckHostIP**

**Ciphers**

**ClearAllForwardings**

**Compression**

**ConnectTimeout**

**ConnectionAttempts**

**ControlMaster**

**ControlPath**

**ControlPersist**

**DynamicForward**

**EnableEscapeCommandline**

**EnableSSHKeysign**

**EscapeChar**

**ExitOnForwardFailure**

**FingerprintHash**

**ForkAfterAuthentication**

**ForwardAgent**

**ForwardX11**

**ForwardX11Timeout**

**ForwardX11Trusted**

**GSSAPIAuthentication**

**GSSAPIDelegateCredentials**

**GatewayPorts**

**GlobalKnownHostsFile**

**HashKnownHosts**

**Host**

**HostKeyAlgorithms**

**HostKeyAlias**

**HostbasedAcceptedAlgorithms**

**HostbasedAuthentication**

**Hostname**

**IPQoS**

**IdentitiesOnly**

**IdentityAgent**

**IdentityFile**

**IgnoreUnknown**

**Include**

**KbdInteractiveAuthentication**

**KbdInteractiveDevices**

**KexAlgorithms**

**KnownHostsCommand**

**LocalCommand**

**LocalForward**

**LogLevel**

**LogVerbose**

**MACs**

**NoHostAuthenticationForLocalhost**

**NumberOfPasswordPrompts**

**ObscureKeystrokeTiming**

**PKCS11Provider**

**PasswordAuthentication**

**PermitLocalCommand**

**PermitRemoteOpen**

**Port**

**PreferredAuthentications**

**ProxyCommand**

**ProxyJump**

**ProxyUseFdpass**

**PubkeyAcceptedAlgorithms**

**PubkeyAuthentication**

**RekeyLimit**

**RemoteCommand**

**RemoteForward**

**RequestTTY**

**RequiredRSASize**

**RevokedHostKeys**

**SecurityKeyProvider**

**SendEnv**

**ServerAliveCountMax**

**ServerAliveInterval**

**SessionType**

**SetEnv**

**StdinNull**

**StreamLocalBindMask**

**StreamLocalBindUnlink**

**StrictHostKeyChecking**

**SyslogFacility**

**TCPKeepAlive**

**Tag**

**Tunnel**

**TunnelDevice**

**UpdateHostKeys**

**User**

**UserKnownHostsFile**

**VerifyHostKeyDNS**

**VisualHostKey**

**XAuthLocation**

**`-4`** 强制 `ssh` 仅使用 IPv4 地址。

**`-6`** 强制 `ssh` 仅使用 IPv6 地址。

**`-A`** 启用从 ssh-agent(1) 等认证代理转发连接。这也可在配置文件中按主机指定。应谨慎启用代理转发。能够绕过远程主机上文件权限的用户（针对代理的 UNIX 域套接字）可通过转发的连接访问本地代理。攻击者无法从代理获取密钥材料，但他们可对密钥执行操作，使其能够使用代理中加载的身份进行认证。更安全的替代方案可能是使用跳转主机（参见 `-J`）。

**`-a`** 禁用认证代理连接的转发。

**`-B`** `bind_interface` 在尝试连接到目标主机之前绑定到 `bind_interface` 的地址。仅在具有多个地址的系统上有用。

**`-b`** `bind_address` 在本地机器上使用 `bind_address` 作为连接的源地址。仅在具有多个地址的系统上有用。

**`-C`** 请求压缩所有数据（包括 stdin、stdout、stderr，以及转发的 X11、TCP 和 UNIX 域连接的数据）。压缩算法与 [gzip(1)](gzip.1.md) 使用的相同。压缩在调制解调器线路和其他慢速连接上很理想，但在快速网络上只会减慢速度。默认值可在配置文件中按主机设置；参见 ssh_config(5) 中的 `Compression` 选项。

**`-c`** `cipher_spec` 选择用于加密会话的密码规范。`cipher_spec` 是按优先级顺序列出的逗号分隔密码列表。更多信息参见 ssh_config(5) 中的 `Ciphers` 关键字。

**`-D`** [`bind_address`:]`port` 指定本地“动态”应用级端口转发。这通过分配一个套接字在本地侦听 `port`（可选绑定到指定 `bind_address`）来工作。每当连接到此端口时，连接通过安全通道转发，然后使用应用协议确定从远程机器连接到哪里。目前支持 SOCKS4 和 SOCKS5 协议，`ssh` 将充当 SOCKS 服务器。只有 root 才能转发特权端口。动态端口转发也可在配置文件中指定。IPv6 地址可通过将地址括在方括号中指定。只有超级用户才能转发特权端口。默认情况下，本地端口根据 `GatewayPorts` 设置绑定。但是，可使用显式 `bind_address` 将连接绑定到特定地址。`bind_address` 为 “localhost” 表示侦听端口仅限本地使用，而空地址或 “*” 表示端口应可从所有接口访问。

**`-E`** `log_file` 将调试日志附加到 `log_file` 而非标准错误。

**`-e`** `escape_char` 设置具有 pty 的会话的转义字符（默认：`~`）。转义字符仅在行首被识别。转义字符后跟点（`.`）关闭连接；后跟 control-Z 挂起连接；后跟自身发送一次转义字符。将字符设置为 “none” 禁用任何转义并使会话完全透明。

**`-F`** `configfile` 指定替代的每用户配置文件。如果在命令行上给出配置文件，将忽略系统范围的配置文件（`/etc/ssh/ssh_config`）。每用户配置文件的默认值为 `~/.ssh/config`。如果设置为 “none”，则不读取任何配置文件。

**`-f`** 请求 `ssh` 在命令执行前转到后台。如果 `ssh` 将询问密码或口令但用户希望它在后台运行，这很有用。这隐含 `-n`。在远程站点启动 X11 程序的推荐方式是使用类似 `ssh -f host xterm` 的命令。如果 `ExitOnForwardFailure` 配置选项设置为 “yes”，则以 `-f` 启动的客户端将等待所有远程端口转发成功建立后再转入后台。详情参见 ssh_config(5) 中 `ForkAfterAuthentication` 的描述。

**`-G`** 使 `ssh` 在评估 `Host` 和 `Match` 块后打印其配置并退出。

**`-g`** 允许远程主机连接到本地转发的端口。如果在多路复用连接上使用，则此选项必须在主进程上指定。

**`-I`** `pkcs11` 指定 `ssh` 应用于与提供用户认证密钥的 PKCS#11 令牌通信的 PKCS#11 共享库。

**`-i`** `identity_file` 选择从中读取公钥认证身份（私钥）的文件。也可指定公钥文件以使用 ssh-agent(1) 中加载的相应私钥（当私钥文件在本地不存在时）。默认值为 `~/.ssh/id_rsa`、`~/.ssh/id_ecdsa`、`~/.ssh/id_ecdsa_sk`、`~/.ssh/id_ed25519` 和 `~/.ssh/id_ed25519_sk`。身份文件也可在配置文件中按主机指定。可以有多个 `-i` 选项（以及配置文件中指定的多个身份）。如果 `CertificateFile` 指令未显式指定证书，`ssh` 还将尝试从身份文件名附加 `-cert.pub` 得到的文件名加载证书信息。

**`-J`** `destination` 首先建立到 `destination` 描述的跳转主机的 `ssh` 连接，然后从那里建立到最终目标的 TCP 转发，从而连接到目标主机。可通过逗号分隔指定多个跳转跳。IPv6 地址可通过将地址括在方括号中指定。这是指定 `ProxyJump` 配置指令的快捷方式。注意，命令行上提供的配置指令通常应用于目标主机，而非任何指定的跳转主机。使用 `~/.ssh/config` 指定跳转主机的配置。

**`-K`** 启用基于 GSSAPI 的认证和向服务器转发（委托）GSSAPI 凭证。

**`-k`** 禁用向服务器转发（委托）GSSAPI 凭证。

**`-L`** [`bind_address`:]`port:host:hostport`

**`-L`** [`bind_address`:]`port:remote_socket`

**`-L`** `local_socket:host:hostport`

**`-L`** `local_socket:remote_socket` 指定本地（客户端）主机上给定 TCP 端口或 Unix 套接字的连接转发到远程的给定主机和端口或 Unix 套接字。这通过分配一个套接字侦听本地 TCP `port`（可选绑定到指定 `bind_address`）或 Unix 套接字来工作。每当连接到本地端口或套接字时，连接通过安全通道转发，并从远程机器连接到 `host` 端口 `hostport` 或 Unix 套接字 `remote_socket`。端口转发也可在配置文件中指定。只有超级用户才能转发特权端口。IPv6 地址可通过将地址括在方括号中指定。默认情况下，本地端口根据 `GatewayPorts` 设置绑定。但是，可使用显式 `bind_address` 将连接绑定到特定地址。`bind_address` 为 “localhost” 表示侦听端口仅限本地使用，而空地址或 “*” 表示端口应可从所有接口访问。

**`-l`** `login_name` 指定在远程机器上登录的用户。这也可在配置文件中按主机指定。

**`-M`** 将 `ssh` 客户端置于连接共享的“master”模式。多个 `-M` 选项将 `ssh` 置于“master”模式，但在每次更改多路复用状态的操作（例如打开新会话）之前需要使用 ssh-askpass(1) 确认。详情参见 ssh_config(5) 中 `ControlMaster` 的描述。

**`-m`** `mac_spec` 逗号分隔的 MAC（消息认证码）算法列表，按优先级顺序指定。更多信息参见 ssh_config(5) 中的 `MACs` 关键字。

**`-N`** 不执行远程命令。这仅用于转发端口。详情参见 ssh_config(5) 中 `SessionType` 的描述。

**`-n`** 将 stdin 从 **/dev/null** 重定向（实际上防止从 stdin 读取）。`ssh` 在后台运行时必须使用此选项。一个常见技巧是使用它在远程机器上运行 X11 程序。例如，`ssh -n shadows.cs.hut.fi emacs &` 将在 shadows.cs.hut.fi 上启动 emacs，X11 连接将通过加密通道自动转发。`ssh` 程序将转入后台。（如果 `ssh` 需要询问密码或口令，这将不起作用；另请参见 `-f` 选项。）详情参见 ssh_config(5) 中 `StdinNull` 的描述。

**`-O`** `ctl_cmd` 控制活动的连接多路复用主进程。指定 `-O` 选项时，`ctl_cmd` 参数被解释并传递给主进程。有效命令为：“check”（检查主进程是否正在运行）、“conninfo”（报告主连接的信息）、“channels”（报告打开通道的信息）、“forward”（请求转发而不执行命令）、“cancel”（取消转发）、“proxy”（以代理模式连接到运行中的多路复用主进程）、“exit”（请求主进程退出）和 “stop”（请求主进程停止接受进一步的多路复用请求）。

**`-o`** `option` 可用于以配置文件中使用的格式给出选项。这对于指定没有单独命令行标志的选项很有用。下列选项及其可能值的完整详情，参见 ssh_config(5)。

**`-P`** `tag` 指定标签名，可用于在 ssh_config(5) 中选择配置。更多信息参见 ssh_config(5) 中的 `Tag` 和 `Match` 关键字。

**`-p`** `port` 远程主机上要连接的端口。这可在配置文件中按主机指定。

**`-Q`** `query_option` 查询以下功能之一支持的算法：`cipher`（支持的对称密码）、`cipher-auth`（支持认证加密的对称密码）、`help`（支持用于 `-Q` 标志的查询术语）、`mac`（支持的消息完整性码）、`kex`（密钥交换算法）、`key`（密钥类型）、`key-ca-sign`（证书的有效 CA 签名算法）、`key-cert`（证书密钥类型）、`key-plain`（非证书密钥类型）、`key-sig`（所有密钥类型和签名算法）、`protocol-version`（支持的 SSH 协议版本）和 `sig`（支持的签名算法）。或者，ssh_config(5) 或 sshd_config(5) 中接受算法列表的任何关键字都可用作相应 query_option 的别名。

**`-q`** 安静模式。使大多数警告和诊断消息被抑制。

**`-R`** [`bind_address`:]`port:host:hostport`

**`-R`** [`bind_address`:]`port:local_socket`

**`-R`** `remote_socket:host:hostport`

**`-R`** `remote_socket:local_socket`

**`-R`** [`bind_address`:]`port` 指定远程（服务器）主机上给定 TCP 端口或 Unix 套接字的连接转发到本地。这通过分配一个套接字侦听远程 TCP `port` 或 Unix 套接字来工作。每当连接到此端口或 Unix 套接字时，连接通过安全通道转发，并从本地机器连接到 `host` 端口 `hostport` 或 `local_socket` 指定的显式目标；如果未指定显式目标，`ssh` 将充当 SOCKS 4/5 代理并将连接转发到远程 SOCKS 客户端请求的目标。端口转发也可在配置文件中指定。特权端口仅在以 root 身份登录远程机器时才能转发。IPv6 地址可通过将地址括在方括号中指定。默认情况下，服务器上的 TCP 侦听套接字仅绑定到环回接口。这可通过指定 `bind_address` 覆盖。空的 `bind_address` 或地址 `*` 表示远程套接字应在所有接口上侦听。指定远程 `bind_address` 仅在服务器启用 `GatewayPorts` 选项时才会成功（参见 sshd_config(5)）。如果 `port` 参数为 `0`，侦听端口将在服务器上动态分配并在运行时报告给客户端。与 `-O forward` 一起使用时，分配的端口将打印到标准输出。

**`-S`** `ctl_path` 指定用于连接共享的控制套接字位置，或字符串 “none” 以禁用连接共享。详情参见 ssh_config(5) 中 `ControlPath` 和 `ControlMaster` 的描述。

**`-s`** 可用于请求在远程系统上调用子系统。子系统有助于将 SSH 用作其他应用程序（例如 [sftp(1)](sftp.1.md)）的安全传输。子系统指定为远程命令。详情参见 ssh_config(5) 中 `SessionType` 的描述。

**`-T`** 禁用伪终端分配。

**`-t`** 强制伪终端分配。这可用于在远程机器上执行任意基于屏幕的程序，这非常有用，例如在实现菜单服务时。多个 `-t` 选项强制 tty 分配，即使 `ssh` 没有本地 tty。

**`-V`** 显示版本号并退出。

**`-v`** 详细模式。使 `ssh` 打印有关其进度的调试消息。这有助于调试连接、认证和配置问题。多个 `-v` 选项增加详细程度。最大为 3。

**`-W`** `host`:`port` 请求客户端的标准输入和输出通过安全通道转发到 `host` 上的 `port`。隐含 `-N`、`-T`、`ExitOnForwardFailure` 和 `ClearAllForwardings`，尽管这些可在配置文件中或使用 `-o` 命令行选项覆盖。

**`-w`** `local_tun`[:`remote_tun`] 请求在客户端（`local_tun`）和服务器（`remote_tun`）之间使用指定 [tun(4)](../man4/tun.4.md) 设备进行隧道设备转发。设备可按数字 ID 或关键字 “any” 指定，后者使用下一个可用的隧道设备。如果未指定 `remote_tun`，则默认为 “any”。另请参见 ssh_config(5) 中的 `Tunnel` 和 `TunnelDevice` 指令。如果未设置 `Tunnel` 指令，它将设置为默认隧道模式 “point-to-point”。如果需要不同的 `Tunnel` 转发模式，则应在 `-w` 之前指定。

**`-X`** 启用 X11 转发。这也可在配置文件中按主机指定。应谨慎启用 X11 转发。能够绕过远程主机上文件权限的用户（针对用户的 X 授权数据库）可通过转发的连接访问本地 X11 显示。攻击者随后可能能够执行诸如击键监控等活动。因此，X11 转发默认受 X11 SECURITY 扩展限制。更多信息参见 `ssh` `-Y` 选项和 ssh_config(5) 中的 `ForwardX11Trusted` 指令。

**`-x`** 禁用 X11 转发。

**`-Y`** 启用受信任的 X11 转发。受信任的 X11 转发不受 X11 SECURITY 扩展控制。

**`-y`** 使用 syslog(3) 系统模块发送日志信息。默认情况下，此信息发送到 stderr。

`ssh` 还可从每用户配置文件和系统范围配置文件获取配置数据。文件格式和配置选项在 ssh_config(5) 中描述。

## 认证

OpenSSH SSH 客户端支持 SSH 协议 2。

可用的认证方法有：基于 GSSAPI 的认证、基于主机的认证、公钥认证、键盘交互认证和密码认证。认证方法按上述顺序尝试，但 `PreferredAuthentications` 可用于更改默认顺序。

基于主机的认证工作方式如下：如果用户登录的机器列在远程机器的 `/etc/hosts.equiv` 或 `/etc/shosts.equiv` 中，用户非 root 且双方用户名相同，或者如果文件 `~/.rhosts` 或 `~/.shosts` 存在于远程机器上用户家目录中并包含一行含有客户端机器名和该机器上的用户名，则考虑该用户登录。此外，服务器**必须**能够验证客户端的主机密钥（参见下文 `/etc/ssh/ssh_known_hosts` 和 `~/.ssh/known_hosts` 的描述）才允许登录。此认证方法关闭了由于 IP 欺骗、DNS 欺骗和路由欺骗导致的安全漏洞。[管理员注意：`/etc/hosts.equiv`、`~/.rhosts` 以及 rlogin/rsh 协议通常本质上不安全，如果需要安全应禁用。]

公钥认证工作方式如下：该方案基于公钥密码学，使用加密和解密使用不同密钥的密码系统，且从加密密钥派生解密密钥不可行。其思想是每个用户为认证目的创建一个公钥/私钥对。服务器知道公钥，只有用户知道私钥。`ssh` 自动实现公钥认证协议，使用 ECDSA、Ed25519 或 RSA 算法之一。

文件 `~/.ssh/authorized_keys` 列出允许登录的公钥。用户登录时，`ssh` 程序告诉服务器它希望使用哪个密钥对进行认证。客户端证明它有权访问私钥，服务器检查相应的公钥是否被授权接受该账户。

服务器可在使用不同方法完成认证后通知客户端阻止公钥认证成功的错误。这些可通过将 `LogLevel` 增加到 `DEBUG` 或更高（例如使用 `-v` 标志）来查看。

用户通过运行 [ssh-keygen(1)](ssh-keygen.1.md) 创建其密钥对。这会将私钥存储在 `~/.ssh/id_ecdsa`（ECDSA）、`~/.ssh/id_ecdsa_sk`（认证器托管的 ECDSA）、`~/.ssh/id_ed25519`（Ed25519）、`~/.ssh/id_ed25519_sk`（认证器托管的 Ed25519）或 `~/.ssh/id_rsa`（RSA）中，并将公钥存储在用户家目录中的 `~/.ssh/id_ecdsa.pub`（ECDSA）、`~/.ssh/id_ecdsa_sk.pub`（认证器托管的 ECDSA）、`~/.ssh/id_ed25519.pub`（Ed25519）、`~/.ssh/id_ed25519_sk.pub`（认证器托管的 Ed25519）或 `~/.ssh/id_rsa.pub`（RSA）中。用户随后应将公钥复制到远程机器上其家目录中的 `~/.ssh/authorized_keys`。`authorized_keys` 文件对应于传统的 `~/.rhosts` 文件，每行一个密钥，尽管行可能非常长。此后，用户无需提供密码即可登录。

证书认证形式提供公钥认证的变体：使用签名证书而非一组公钥/私钥。这具有单个受信任的认证机构可替代许多公钥/私钥对的优点。更多信息参见 [ssh-keygen(1)](ssh-keygen.1.md) 的 CERTIFICATES 小节。

使用公钥或证书认证最方便的方式可能是使用认证代理。更多信息参见 ssh-agent(1) 和（可选）ssh_config(5) 中的 `AddKeysToAgent` 指令。

键盘交互认证工作方式如下：服务器发送任意“challenge”文本并提示响应，可能多次。键盘交互认证的示例包括 BSD 认证（参见 login.conf(5)）和 PAM（一些非 OpenBSD 系统）。

最后，如果其他认证方法失败，`ssh` 提示用户输入密码。密码发送到远程主机进行检查；但是，由于所有通信都已加密，监听网络的人无法看到密码。

`ssh` 自动维护并检查一个数据库，包含它曾经使用过的所有主机的标识。主机密钥存储在用户家目录中的 `~/.ssh/known_hosts`。此外，自动检查文件 `/etc/ssh/ssh_known_hosts` 中的已知主机。任何新主机都会自动添加到用户的文件中。如果主机的标识发生更改，`ssh` 会发出警告并禁用密码认证以防止服务器欺骗或中间人攻击，否则这些攻击可能用于绕过加密。`StrictHostKeyChecking` 选项可用于控制登录到主机密钥未知或已更改的机器。

当用户的身份被服务器接受时，服务器在非交互会话中执行给定命令，或者如果未指定命令，则登录到机器并为用户提供一个正常 shell 作为交互会话。与远程命令或 shell 的所有通信都将自动加密。

如果请求交互会话，`ssh` 默认仅在客户端具有 pty 时才为交互会话请求伪终端（pty）。`-T` 和 `-t` 标志可用于覆盖此行为。

如果已分配伪终端，用户可使用下面提到的转义字符。

如果未分配伪终端，会话是透明的，可用于可靠地传输二进制数据。在大多数系统上，将转义字符设置为 “none” 也会使会话透明，即使使用了 tty。

会话在远程机器上的命令或 shell 退出且所有 X11 和 TCP 连接已关闭时终止。

## 转义字符

请求伪终端时，`ssh` 通过使用转义字符支持许多功能。

单个波浪号字符可作为 `~~` 或在波浪号后跟除下面描述字符以外的字符发送。转义字符必须始终跟在换行符后才会被解释为特殊字符。转义字符可在配置文件中使用 `EscapeChar` 配置指令或在命令行上使用 `-e` 选项更改。

支持的转义（假设默认为 `~`）有：

**`~.`** 断开连接。

**`~^Z`** 将 `ssh` 转到后台。

**`~#`** 列出转发的连接。

**`~&`** 注销时在等待转发连接 / X11 会话终止时将 `ssh` 转到后台。

**`~?`** 显示转义字符列表。

**`~B`** 向远程系统发送 BREAK（仅在对方支持时有用）。

**`~C`** 打开命令行。目前这允许使用 `-L`、`-R` 和 `-D` 选项（见上文）添加端口转发。它还允许取消现有端口转发：本地使用 `-KL` [`bind_address`:]`port`，远程使用 `-KR` [`bind_address`:]`port`，动态使用 `-KD` [`bind_address`:]`port`。如果 ssh_config(5) 中启用了 `PermitLocalCommand` 选项，`!``command` 允许用户执行本地命令。使用 `-h` 选项可获得基本帮助。

**`~I`** 显示当前 SSH 连接的信息。

**`~R`** 请求重新协商连接密钥（仅在对方支持时有用）。

**`~V`** 当错误正写入 stderr 时降低详细程度（`LogLevel`）。

**`~v`** 当错误正写入 stderr 时增加详细程度（`LogLevel`）。

## TCP 转发

通过安全通道转发任意 TCP 连接可在命令行或配置文件中指定。TCP 转发的一个可能应用是与邮件服务器的安全连接；另一个是通过防火墙。

在下面的示例中，我们查看为 IRC 客户端加密通信，即使它连接的 IRC 服务器不直接支持加密通信。这工作如下：用户使用 `ssh` 连接到远程主机，指定用于转发连接的端口。之后可在本地启动程序，`ssh` 将加密并转发连接到远程服务器。

以下示例使用标准 IRC 端口 6667 从客户端到 IRC 服务器 “server.example.com” 隧道 IRC 会话，加入频道 “#users”，昵称 “pinky”：

```sh
$ ssh -f -L 6667:localhost:6667 server.example.com sleep 10
$ irc -c '#users' pinky IRC/127.0.0.1
```

`-f` 选项将 `ssh` 转到后台，并指定远程命令 “sleep 10” 以允许一定时间（示例中为 10 秒）启动将使用隧道的程序。如果在指定时间内未建立连接，`ssh` 将退出。

## X11 转发

如果 `ForwardX11` 变量设置为 “yes”（或参见上文 `-X`、`-x` 和 `-Y` 选项的描述）且用户使用 X11（设置了 `DISPLAY` 环境变量），到 X11 显示的连接将自动转发到远程，使得从 shell（或命令）启动的任何 X11 程序都将通过加密通道，并且到真实 X 服务器的连接将从本地机器建立。用户不应手动设置 `DISPLAY`。X11 连接转发可在命令行或配置文件中配置。

`ssh` 设置的 `DISPLAY` 值将指向服务器机器，但显示号大于零。这是正常的，因为 `ssh` 在服务器机器上创建一个“代理”X 服务器以通过加密通道转发连接。

`ssh` 还会自动在服务器机器上设置 Xauthority 数据。为此，它将生成一个随机授权 cookie，将其存储在服务器上的 Xauthority 中，并验证任何转发的连接携带此 cookie，并在连接打开时将其替换为真实 cookie。真实认证 cookie 永远不会发送到服务器机器（且不会以明文发送任何 cookie）。

如果 `ForwardAgent` 变量设置为 “yes”（或参见上文 `-A` 和 `-a` 选项的描述）且用户使用认证代理，到代理的连接将自动转发到远程。

## 验证主机密钥

首次连接到服务器时，服务器公钥的指纹将呈现给用户（除非已禁用 `StrictHostKeyChecking` 选项）。指纹可使用 [ssh-keygen(1)](ssh-keygen.1.md) 确定：

```sh
$ ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key
```

如果指纹已知，可进行匹配并接受或拒绝密钥。如果仅有服务器的传统（MD5）指纹可用，可使用 [ssh-keygen(1)](ssh-keygen.1.md) 的 `-E` 选项降级指纹算法以匹配。

由于仅通过查看指纹字符串比较主机密钥的困难性，还支持使用*随机艺术*直观比较主机密钥。通过将 `VisualHostKey` 选项设置为 “yes”，每次登录服务器时都会显示一个小 ASCII 图形，无论会话本身是否交互。通过了解已知服务器产生的模式，当显示完全不同的模式时，用户可以轻松发现主机密钥已更改。但是，由于这些模式并非明确，看起来与记住的模式相似的模式仅表示主机密钥相同的良好概率，而非保证证明。

要获取所有已知主机的指纹及其随机艺术的列表，可使用以下命令行：

```sh
$ ssh-keygen -lv -f ~/.ssh/known_hosts
```

如果指纹未知，可使用替代验证方法：DNS 验证的 SSH 指纹。向区域文件添加附加资源记录（RR）SSHFP，连接的客户端能够将指纹与呈现的密钥指纹匹配。

在此示例中，我们将客户端连接到服务器 “host.example.com”。应首先将 SSHFP 资源记录添加到 host.example.com 的区域文件：

```sh
$ ssh-keygen -r host.example.com.
```

输出行必须添加到区域文件。要检查区域是否响应指纹查询：

```sh
$ dig -t SSHFP host.example.com
```

最后客户端连接：

```sh
$ ssh -o "VerifyHostKeyDNS ask" host.example.com
[...]
Matching host key fingerprint found in DNS.
Are you sure you want to continue connecting (yes/no)?
```

更多信息参见 ssh_config(5) 中的 `VerifyHostKeyDNS` 选项。

## 基于 SSH 的虚拟专用网

`ssh` 支持使用 [tun(4)](../man4/tun.4.md) 网络伪设备进行虚拟专用网（VPN）隧道，允许两个网络安全地连接。sshd_config(5) 配置选项 `PermitTunnel` 控制服务器是否支持此功能以及支持级别（第 2 层或第 3 层流量）。

以下示例使用从 10.1.1.1 到 10.1.1.2 的点对点连接将客户端网络 10.0.50.0/24 与远程网络 10.0.99.0/24 连接，前提是在 192.168.1.15 上运行的 SSH 服务器（远程网络的网关）允许此操作。

在客户端上：

```sh
# ssh -f -w 0:1 192.168.1.15 true
# ifconfig tun0 10.1.1.1 10.1.1.2 netmask 255.255.255.252
# route add 10.0.99.0/24 10.1.1.2
```

在服务器上：

```sh
# ifconfig tun1 10.1.1.2 10.1.1.1 netmask 255.255.255.252
# route add 10.0.50.0/24 10.1.1.1
```

客户端访问可通过 `/root/.ssh/authorized_keys` 文件（见下文）和 `PermitRootLogin` 服务器选项更精细地调整。如果 `PermitRootLogin` 设置为 “forced-commands-only”，以下条目将允许用户 “jane” 在 [tun(4)](../man4/tun.4.md) 设备 1 上连接，用户 “john” 在 tun 设备 2 上连接：

```sh
tunnel="1",command="sh /etc/netstart tun1" ssh-rsa ... jane
tunnel="2",command="sh /etc/netstart tun2" ssh-rsa ... john
```

由于基于 SSH 的设置涉及相当大的开销，它可能更适合临时设置，例如无线 VPN。更永久的 VPN 最好由 ipsecctl(8) 和 isakmpd(8) 等工具提供。

## 环境变量

`ssh` 通常会设置以下环境变量：

**`DISPLAY`** `DISPLAY` 变量指示 X11 服务器的位置。`ssh` 自动将其设置为 “hostname:n” 形式的值，其中 “hostname” 指示 shell 运行的主机，“n”是大于等于 1 的整数。`ssh` 使用此特殊值通过安全通道转发 X11 连接。用户通常不应显式设置 `DISPLAY`，因为那将使 X11 连接不安全（并要求用户手动复制任何所需的授权 cookie）。

**`HOME`** 设置为用户家目录的路径。

**`LOGNAME`** `USER` 的同义词；为使用此变量的系统设置以保持兼容性。

**`MAIL`** 设置为用户邮箱的路径。

**`PATH`** 设置为编译 `ssh` 时指定的默认 `PATH`。

**`SSH_ASKPASS`** 如果 `ssh` 需要口令，且它是从终端运行的，它将从当前终端读取口令。如果 `ssh` 没有关联的终端但设置了 `DISPLAY` 和 `SSH_ASKPASS`，它将执行 `SSH_ASKPASS` 指定的程序并打开 X11 窗口读取口令。这在从 `.xsession` 或相关脚本调用 `ssh` 时特别有用。（注意，在某些机器上可能需要将输入从 **/dev/null** 重定向才能使此功能工作。）

**`SSH_ASKPASS_REQUIRE`** 允许进一步控制 askpass 程序的使用。如果此变量设置为 “never”，则 `ssh` 永远不会尝试使用它。如果设置为 “prefer”，则 `ssh` 在请求密码时将优先使用 askpass 程序而非 TTY。最后，如果变量设置为 “force”，则 askpass 程序将用于所有口令输入，无论是否设置了 `DISPLAY`。

**`SSH_AUTH_SOCK`** 标识用于与代理通信的 UNIX 域套接字路径。

**`SSH_CONNECTION`** 标识连接的客户端和服务器端。该变量包含四个空格分隔的值：客户端 IP 地址、客户端端口号、服务器 IP 地址和服务器端口号。

**`SSH_ORIGINAL_COMMAND`** 如果执行了强制命令，此变量包含原始命令行。它可用于提取原始参数。

**`SSH_TTY`** 设置为与当前 shell 或命令关联的 tty（设备路径）名称。如果当前会话没有 tty，则不设置此变量。

**`SSH_TUNNEL`** 由 sshd(8) 可选设置，包含客户端请求隧道转发时分配的接口名称。

**`SSH_USER_AUTH`** 由 sshd(8) 可选设置，此变量可能包含一个文件路径名，该文件列出会话建立时成功使用的认证方法，包括使用的任何公钥。

**`TZ`** 如果在守护进程启动时设置了此变量，则设置为指示当前时区（即守护进程将值传递给新连接）。

**`USER`** 设置为登录用户的名称。

此外，`ssh` 读取 `~/.ssh/environment`，并在文件存在且允许用户更改其环境时将 “VARNAME=value” 格式的行添加到环境中。更多信息参见 sshd_config(5) 中的 `PermitUserEnvironment` 选项。

## 文件

**`~/.rhosts`** 此文件用于基于主机的认证（见上文）。在某些机器上，如果用户的家目录位于 NFS 分区上，此文件可能需要全局可读，因为 sshd(8) 以 root 身份读取它。此外，此文件必须由用户拥有，且不得有其他人的写权限。大多数机器的推荐权限是用户读写，其他人不可访问。

**`~/.shosts`** 此文件的使用方式与 `.rhosts` 完全相同，但允许基于主机的认证而不允许使用 rlogin/rsh 登录。

**`~/.ssh/`** 此目录是所有用户特定配置和认证信息的默认位置。通常不需要将此目录的全部内容保密，但推荐权限是用户读/写/执行，其他人不可访问。

**`~/.ssh/authorized_keys`** 列出可用于以此用户登录的公钥（ECDSA、Ed25519、RSA）。此文件的格式在 sshd(8) 手册页中描述。此文件不太敏感，但推荐权限是用户读写，其他人不可访问。

**`~/.ssh/config`** 这是每用户配置文件。文件格式和配置选项在 ssh_config(5) 中描述。由于潜在的滥用，此文件必须具有严格权限：用户读写，其他人不可写。

**`~/.ssh/environment`** 包含环境变量的附加定义；参见上文的“环境变量”小节。

**`~/.ssh/id_ecdsa`**

**`~/.ssh/id_ecdsa_sk`**

**`~/.ssh/id_ed25519`**

**`~/.ssh/id_ed25519_sk`**

**`~/.ssh/id_rsa`** 包含用于认证的私钥。这些文件包含敏感数据，应由用户读取但其他人不可访问（读/写/执行）。如果私钥文件可被其他人访问，`ssh` 将直接忽略它。生成密钥时可指定口令，用于使用 AES-128 加密此文件的敏感部分。

**`~/.ssh/id_ecdsa.pub`**

**`~/.ssh/id_ecdsa_sk.pub`**

**`~/.ssh/id_ed25519.pub`**

**`~/.ssh/id_ed25519_sk.pub`**

**`~/.ssh/id_rsa.pub`** 包含用于认证的公钥。这些文件不敏感，可以（但不必）被任何人读取。

**`~/.ssh/known_hosts`** 包含用户登录过的所有主机的主机密钥列表，这些主机不在系统范围的已知主机密钥列表中。此文件格式的更多详情参见 sshd(8)。

**`~/.ssh/rc`** 用户登录时，`ssh` 在用户的 shell（或命令）启动之前执行此文件中的命令。更多信息参见 sshd(8) 手册页。

**`/etc/hosts.equiv`** 此文件用于基于主机的认证（见上文）。它应仅可由 root 写入。

**`/etc/shosts.equiv`** 此文件的使用方式与 `hosts.equiv` 完全相同，但允许基于主机的认证而不允许使用 rlogin/rsh 登录。

**`/etc/ssh/ssh_config`** 系统范围配置文件。文件格式和配置选项在 ssh_config(5) 中描述。

**`/etc/ssh/ssh_host_ecdsa_key`**

**`/etc/ssh/ssh_host_ed25519_key`**

**`/etc/ssh/ssh_host_rsa_key`** 这些文件包含主机密钥的私钥部分，用于基于主机的认证。

**`/etc/ssh/ssh_known_hosts`** 系统范围的已知主机密钥列表。此文件应由系统管理员准备，包含组织中所有机器的公共主机密钥。它应全局可读。此文件格式的更多详情参见 sshd(8)。

**`/etc/ssh/sshrc`** 用户登录时，`ssh` 在用户的 shell（或命令）启动之前执行此文件中的命令。更多信息参见 sshd(8) 手册页。

## 退出状态

`ssh` 以远程命令的退出状态退出，如果发生错误则以 255 退出。

## 参见

[scp(1)](scp.1.md), [sftp(1)](sftp.1.md), ssh-add(1), ssh-agent(1), [ssh-keygen(1)](ssh-keygen.1.md), ssh-keyscan(1), [tun(4)](../man4/tun.4.md), ssh_config(5), [ssh-keysign(8)](../man8/ssh-keysign.8.md), sshd(8)

## 标准

> S. Lehtinen, C. Lonvick, "The Secure Shell (SSH) Protocol Assigned Numbers", January 2006.

> T. Ylonen, C. Lonvick, "The Secure Shell (SSH) Protocol Architecture", January 2006.

> T. Ylonen, C. Lonvick, "The Secure Shell (SSH) Authentication Protocol", January 2006.

> T. Ylonen, C. Lonvick, "The Secure Shell (SSH) Transport Layer Protocol", January 2006.

> T. Ylonen, C. Lonvick, "The Secure Shell (SSH) Connection Protocol", January 2006.

> J. Schlyter, W. Griffin, "Using DNS to Securely Publish Secure Shell (SSH) Key Fingerprints", January 2006.

> F. Cusack, M. Forssen, "Generic Message Exchange Authentication for the Secure Shell Protocol (SSH)", January 2006.

> J. Galbraith, P. Remaker, "The Secure Shell (SSH) Session Channel Break Extension", January 2006.

> M. Bellare, T. Kohno, C. Namprempre, "The Secure Shell (SSH) Transport Layer Encryption Modes", January 2006.

> B. Harris, "Improved Arcfour Modes for the Secure Shell (SSH) Transport Layer Protocol", January 2006.

> M. Friedl, N. Provos, W. Simpson, "Diffie-Hellman Group Exchange for the Secure Shell (SSH) Transport Layer Protocol", March 2006.

> J. Galbraith, R. Thayer, "The Secure Shell (SSH) Public Key File Format", November 2006.

> D. Stebila, J. Green, "Elliptic Curve Algorithm Integration in the Secure Shell Transport Layer", December 2009.

> A. Perrig, D. Song, "Hash Visualization: a New Technique to improve Real-World Security", 1999, International Workshop on Cryptographic Techniques and E-Commerce (CrypTEC '99).

## 作者

OpenSSH 是 Tatu Ylonen 发布的原始免费 ssh 1.2.12 版本的衍生作品。Aaron Campbell、Bob Beck、Markus Friedl、Niels Provos、Theo de Raadt 和 Dug Song 修复了许多错误，重新添加了较新的功能并创建了 OpenSSH。Markus Friedl 贡献了对 SSH 协议版本 1.5 和 2.0 的支持。
