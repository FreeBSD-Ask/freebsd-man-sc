# ssh_config(5)

`ssh_config` — OpenSSH 客户端配置文件

## 名称

`ssh_config`

## 描述

[ssh(1)](../man1/ssh.1.md) 按以下顺序从以下来源获取配置数据：

- 命令行选项
- 用户的配置文件（`~/.ssh/config`）
- 系统范围的配置文件（**`/etc/ssh/ssh_config`**）

除非另有说明，对于每个参数，将使用第一个获得的值。配置文件包含由 `Host` 规格分隔的段落，该段落仅应用于与规格中给定模式之一匹配的主机。匹配的主机名通常是命令行中给出的那个（例外情况请参见 `CanonicalizeHostname` 选项）。

由于每个参数使用第一个获得的值，更特定于主机的声明应放在文件开头附近，而通用默认值放在末尾。

文件包含关键字-参数对，每行一对。以 `#` 开头的行和空行被解释为注释。参数可以选择性地用双引号（"）括起，以表示包含空格的参数。配置选项可以用空白或可选空白加恰好一个 `=` 分隔；后一种格式可用于避免在使用 `ssh`、`scp` 和 `sftp` 的 `-o` 选项指定配置选项时需要引用空白。

可能的关键字及其含义如下（注意关键字不区分大小写，参数区分大小写）：

```sh
ssh-ed25519,ecdsa-sha2-nistp256,
ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519@openssh.com,
sk-ecdsa-sha2-nistp256@openssh.com,
rsa-sha2-512,rsa-sha2-256
```

**`agent-connection`** 打开到 ssh-agent(1) 的连接。

**`direct-tcpip`**, `direct-streamlocal@openssh.com` 打开（分别）从 [ssh(1)](../man1/ssh.1.md) 本地转发（即 `LocalForward` 或 `DynamicForward`）建立的 TCP 或 Unix 套接字连接。

**`forwarded-tcpip`**, `forwarded-streamlocal@openssh.com` 打开（分别）代表 [ssh(1)](../man1/ssh.1.md) 远程转发（即 `RemoteForward`）建立到 sshd(8) 监听端的 TCP 或 Unix 套接字连接。

**`session`** 交互式主会话，包括 shell 会话、命令执行、[scp(1)](../man1/scp.1.md)、[sftp(1)](../man1/sftp.1.md) 等。

**`tun-connection`** 打开 `TunnelForward` 连接。

**`x11-connection`** 打开 X11 转发会话。

```sh
3des-cbc
aes128-cbc
aes192-cbc
aes256-cbc
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com
chacha20-poly1305@openssh.com
```

```sh
chacha20-poly1305@openssh.com,
aes128-gcm@openssh.com,aes256-gcm@openssh.com,
aes128-ctr,aes192-ctr,aes256-ctr
```

```sh
ssh-ed25519-cert-v01@openssh.com,
ecdsa-sha2-nistp256-cert-v01@openssh.com,
ecdsa-sha2-nistp384-cert-v01@openssh.com,
ecdsa-sha2-nistp521-cert-v01@openssh.com,
sk-ssh-ed25519-cert-v01@openssh.com,
sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,
webauthn-sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,
rsa-sha2-512-cert-v01@openssh.com,
rsa-sha2-256-cert-v01@openssh.com,
ssh-ed25519,
ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519@openssh.com,
sk-ecdsa-sha2-nistp256@openssh.com,
webauthn-sk-ecdsa-sha2-nistp256@openssh.com,
rsa-sha2-512,rsa-sha2-256
```

```sh
ssh-ed25519-cert-v01@openssh.com,
ecdsa-sha2-nistp256-cert-v01@openssh.com,
ecdsa-sha2-nistp384-cert-v01@openssh.com,
ecdsa-sha2-nistp521-cert-v01@openssh.com,
sk-ssh-ed25519-cert-v01@openssh.com,
sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,
webauthn-sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,
rsa-sha2-512-cert-v01@openssh.com,
rsa-sha2-256-cert-v01@openssh.com,
ssh-ed25519,
ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ecdsa-sha2-nistp256@openssh.com,
webauthn-sk-ecdsa-sha2-nistp256@openssh.com
sk-ssh-ed25519@openssh.com,
rsa-sha2-512,rsa-sha2-256
```

```sh
mlkem768x25519-sha256,
sntrup761x25519-sha512,sntrup761x25519-sha512@openssh.com,
curve25519-sha256,curve25519-sha256@libssh.org,
ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,
diffie-hellman-group-exchange-sha256,
diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,
diffie-hellman-group14-sha256
```

```sh
kex.c:*:1000,*:kex_exchange_identification():*,packet.c:*
```

```sh
umac-64-etm@openssh.com,umac-128-etm@openssh.com,
hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,
hmac-sha1-etm@openssh.com,
umac-64@openssh.com,umac-128@openssh.com,
hmac-sha2-256,hmac-sha2-512,hmac-sha1
```

- `PermitRemoteOpen` `host : port`
- `PermitRemoteOpen` `IPv4_addr : port`
- `PermitRemoteOpen` `[ IPv6_addr ] : port`

```sh
gssapi-with-mic,hostbased,publickey,
keyboard-interactive,password
```

```sh
ProxyCommand /usr/bin/nc -X connect -x 192.0.2.0:8080 %h %p
```

```sh
ssh-ed25519-cert-v01@openssh.com,
ecdsa-sha2-nistp256-cert-v01@openssh.com,
ecdsa-sha2-nistp384-cert-v01@openssh.com,
ecdsa-sha2-nistp521-cert-v01@openssh.com,
sk-ssh-ed25519-cert-v01@openssh.com,
sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,
webauthn-sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,
rsa-sha2-512-cert-v01@openssh.com,
rsa-sha2-256-cert-v01@openssh.com,
ssh-ed25519,
ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519@openssh.com,
sk-ecdsa-sha2-nistp256@openssh.com,
webauthn-sk-ecdsa-sha2-nistp256@openssh.com,
rsa-sha2-512,rsa-sha2-256
```

**`Host`** 限制以下声明（直到下一个 `Host` 或 `Match` 关键字）仅适用于与关键字后给定模式之一匹配的主机。如果提供了多个模式，它们应该用空白分隔。单个 `*` 作为模式可用于为所有主机提供全局默认值。主机通常是命令行中给出的 `hostname` 参数（例外情况请参见 `CanonicalizeHostname` 关键字）。模式条目可以通过在其前面加感叹号（‘!’）来取反。如果匹配了取反条目，则忽略该 `Host` 条目，无论该行上的任何其他模式是否匹配。因此，取反匹配对于为通配符匹配提供例外很有用。有关模式的更多信息，请参见 Sx PATTERNS。

**`Match`** 限制以下声明（直到下一个 `Host` 或 `Match` 关键字）仅在满足 `Match` 关键字后的条件时使用。匹配条件使用一个或多个条件或始终匹配的单个标记 `all` 指定。可用的条件关键字有：`canonical`、`final`、`exec`、`localnetwork`、`host`、`originalhost`、`tagged`、`command`、`user`、`localuser` 和 `version`。`all` 条件必须单独出现或紧随 `canonical` 或 `final` 之后。其他条件可以任意组合。除 `all`、`canonical` 和 `final` 外的所有条件都需要参数。条件可以通过在前面加感叹号（‘!’）来取反。`canonical` 关键字仅在主机名规范化后重新解析配置文件时匹配（参见 `CanonicalizeHostname` 选项）。这对于指定仅适用于规范主机名的条件很有用。`final` 关键字请求重新解析配置（无论是否启用了 `CanonicalizeHostname`），并且仅在此最终遍历期间匹配。如果启用了 `CanonicalizeHostname`，则 `canonical` 和 `final` 在同一遍历中匹配。`exec` 关键字在用户的 shell 下执行指定的命令。如果命令返回零退出状态，则条件被视为真。包含空白字符的命令必须加引号。`exec` 的参数接受 Sx TOKENS 章节中描述的标记。`localnetwork` 关键字将活动本地网络接口的地址与以 CIDR 格式提供的网络列表进行匹配。这对于在不同网络之间漫游的设备上改变有效配置可能很方便。注意，在许多情况下网络地址不是一个可信的条件（例如，当网络使用 DHCP 自动配置时），因此如果使用它来控制安全敏感的配置，应加以谨慎。其他关键字的条件必须是单个条目或逗号分隔的列表，并且可以使用 Sx PATTERNS 章节中描述的通配符和取反运算符。`host` 关键字的条件在 `Hostname` 或 `CanonicalizeHostname` 选项进行任何替换之后与目标主机名匹配。`originalhost` 关键字与命令行中指定的主机名匹配。`tagged` 关键字匹配由先前 `Tag` 指令或 [ssh(1)](../man1/ssh.1.md) 命令行中使用 `-P` 标志指定的标记名称。`command` 关键字匹配请求的远程命令，或正在调用的子系统名称（例如，对于 SFTP 会话为“sftp”）。空字符串将匹配未指定命令或标记的情况，即‘Match tag ""’。`version` 关键字与 [ssh(1)](../man1/ssh.1.md) 的版本字符串匹配，例如“OpenSSH_10.0”。`user` 关键字与远程主机上的目标用户名匹配。`localuser` 关键字与运行 [ssh(1)](../man1/ssh.1.md) 的本地用户名匹配（此关键字在系统范围的 `sftp` 文件中可能有用）。最后，`sessiontype` 关键字匹配请求的会话类型，可以是 `shell`（用于交互式会话）、`exec`（用于命令执行会话）、`subsystem`（用于子系统调用，如 [sftp(1)](../man1/sftp.1.md)）或 `none`（用于仅传输会话，例如当 [ssh(1)](../man1/ssh.1.md) 以 `-N` 标志启动时）。

**`AddKeysToAgent`** 指定是否应自动将密钥添加到运行中的 ssh-agent(1)。如果此选项设置为 `yes` 且从文件加载密钥，则密钥及其口令短语将以默认生存期添加到代理中，如同通过 ssh-add(1) 添加。如果此选项设置为 `ask`，[ssh(1)](../man1/ssh.1.md) 在添加密钥之前将需要使用 `SSH_ASKPASS` 程序进行确认（详见 ssh-add(1)）。如果此选项设置为 `confirm`，则每次使用密钥都必须确认，如同向 ssh-add(1) 指定了 `-c` 选项。如果此选项设置为 `no`，则不会将任何密钥添加到代理。或者，可以使用 sshd_config(5) 的 Sx TIME FORMATS 章节中描述的格式将此选项指定为时间间隔，以指定密钥在 ssh-agent(1) 中的生存期，之后将自动移除。参数必须为 `no`（默认）、`yes`、`confirm`（可选后跟时间间隔）、`ask` 或时间间隔。

**`AddressFamily`** 指定连接时使用的地址族。有效参数为 `any`（默认）、`inet`（仅使用 IPv4）或 `inet6`（仅使用 IPv6）。

**`BatchMode`** 如果设置为 `yes`，将禁用用户交互，如密码提示和主机密钥确认请求。此选项在脚本和其他批处理作业中很有用，因为没有用户在场与 [ssh(1)](../man1/ssh.1.md) 交互。参数必须为 `yes` 或 `no`（默认）。

**`BindAddress`** 在本地机器上使用指定地址作为连接的源地址。仅在具有多个地址的系统上有用。

**`BindInterface`** 在本地机器上使用指定接口的地址作为连接的源地址。

**`CanonicalDomains`** 当启用 `CanonicalizeHostname` 时，此选项指定要在其中搜索指定目标主机的域后缀列表。

**`CanonicalizeFallbackLocal`** 指定主机名规范化失败时是否报错失败。默认值 `yes` 将尝试使用系统解析器的搜索规则查找未限定的主机名。值为 `no` 将导致 [ssh(1)](../man1/ssh.1.md) 在启用了 `CanonicalizeHostname` 且目标主机名无法在 `CanonicalDomains` 指定的任何域中找到时立即失败。

**`CanonicalizeHostname`** 控制是否执行显式主机名规范化。默认值 `no` 不执行任何名称重写，让系统解析器处理所有主机名查找。如果设置为 `yes`，则对于不使用 `ProxyCommand` 或 `ProxyJump` 的连接，[ssh(1)](../man1/ssh.1.md) 将尝试使用 `CanonicalDomains` 后缀和 `CanonicalizePermittedCNAMEs` 规范化命令行中指定的主机名。如果 `CanonicalizeHostname` 设置为 `always`，则规范化也应用于代理连接。如果启用此选项，则使用新的目标名称再次处理配置文件，以拾取匹配的 `Host` 和 `Match` 段中的任何新配置。值为 `none` 禁用 `ProxyJump` 主机的使用。

**`CanonicalizeMaxDots`** 指定禁用规范化之前主机名中点字符的最大数量。默认值 1 允许单个点（即 hostname.subdomain）。

**`CanonicalizePermittedCNAMEs`** 指定规则以确定规范化主机名时是否应跟随 CNAME。规则由一个或多个 `source_domain_list`:`target_domain_list` 参数组成，其中 `source_domain_list` 是可能在规范化中跟随 CNAME 的域的模式列表，`target_domain_list` 是它们可能解析到的域的模式列表。例如，“\*.a.example.com:\*.b.example.com,\*.c.example.com”将允许匹配“\*.a.example.com”的主机名规范化为“\*.b.example.com”或“\*.c.example.com”域中的名称。单个参数“none”导致规范化时不考虑任何 CNAME。这是默认行为。

**`CASignatureAlgorithms`** 指定证书授权机构（CA）签名证书所允许的算法。默认为：如果指定列表以‘+’字符开头，则指定的算法将追加到默认集合而不是替换它。如果指定列表以‘-’字符开头，则指定的算法（包括通配符）将从默认集合中移除而不是替换它。[ssh(1)](../man1/ssh.1.md) 不会接受使用指定算法以外的算法签名的证书。

**`CertificateFile`** 指定从中读取用户证书的文件。必须单独提供相应的私钥才能使用此证书，可以通过 `IdentityFile` 指令或 [ssh(1)](../man1/ssh.1.md) 的 `-i` 标志、通过 ssh-agent(1) 或通过 `PKCS11Provider` 或 `SecurityKeyProvider`。`CertificateFile` 的参数可以使用波浪号语法引用用户主目录、Sx TOKENS 章节中描述的标记以及 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。可以在配置文件中指定多个证书文件；这些证书将按顺序尝试。多个 `CertificateFile` 指令将添加到用于认证的证书列表中。

**`ChannelTimeout`** 指定 [ssh(1)](../man1/ssh.1.md) 是否以及多快关闭不活动通道。超时指定为一个或多个以空白分隔的“type=interval”对，其中“type”必须是特殊关键字“global”或下面列表中的通道类型名称，可选包含通配符。超时值“interval”以秒为单位指定，或可以使用 Sx TIME FORMATS 章节中记录的任何单位。例如，“session=5m”将导致交互式会话在不活动 5 分钟后终止。指定零值禁用不活动超时。特殊超时“global”适用于所有活动通道的总体。任何活动通道上的流量都将重置超时，但当超时到期时，所有打开的通道都将被关闭。注意，此全局超时不被通配符匹配，必须显式指定。可用的通道类型名称包括：注意在上述所有情况下，终止不活动会话并不保证移除与会话关联的所有资源，例如与会话相关的 shell 进程或 X11 客户端可能继续执行。此外，终止不活动通道或会话不一定关闭 SSH 连接，也不阻止客户端请求相同类型的另一个通道。特别是，过期不活动转发会话并不阻止随后创建另一个相同的转发。默认是不因不活动而过期任何类型的通道。

**`CheckHostIP`** 如果设置为 `yes`，[ssh(1)](../man1/ssh.1.md) 还将额外检查 `known_hosts` 文件中的主机 IP 地址。这允许它检测由于 DNS 欺骗导致的主机密钥更改，并在此过程中将目标主机的地址添加到 `~/.ssh/known_hosts`，无论 `StrictHostKeyChecking` 的设置如何。如果选项设置为 `no`（默认），则不会执行检查。

**`Ciphers`** 指定允许的密码及其优先顺序。多个密码必须用逗号分隔。如果指定列表以‘+’字符开头，则指定的密码将追加到默认集合而不是替换它。如果指定列表以‘-’字符开头，则指定的密码（包括通配符）将从默认集合中移除而不是替换它。如果指定列表以‘^’字符开头，则指定的密码将置于默认集合的开头。支持的密码有：默认为：可用密码列表也可以使用“ssh -Q cipher”获取。

**`ClearAllForwardings`** 指定清除配置文件中或命令行中指定的所有本地、远程和动态端口转发。此选项主要用于从 [ssh(1)](../man1/ssh.1.md) 命令行清除配置文件中设置的端口转发，并由 [scp(1)](../man1/scp.1.md) 和 [sftp(1)](../man1/sftp.1.md) 自动设置。参数必须为 `yes` 或 `no`（默认）。

**`Compression`** 指定是否使用压缩。参数必须为 `yes` 或 `no`（默认）。

**`ConnectionAttempts`** 指定退出之前尝试的次数（每次一秒）。参数必须为整数。如果连接有时失败，这在脚本中可能有用。默认为 1。

**`ConnectTimeout`** 指定连接到 SSH 服务器时使用的超时（以秒为单位），而不是使用默认的系统 TCP 超时。此超时既应用于建立连接，也应用于执行初始 SSH 协议握手和密钥交换。

**`ControlMaster`** 启用通过单个网络连接共享多个会话。当设置为 `yes` 时，[ssh(1)](../man1/ssh.1.md) 将监听使用 `ControlPath` 参数指定的控制套接字上的连接。其他会话可以使用相同的 `ControlPath` 与 `ControlMaster` 设置为 `no`（默认）连接到此套接字。这些会话将尝试重用主实例的网络连接而不是发起新连接，但如果控制套接字不存在或未在监听，则回退到正常连接。设置为 `ask` 将导致 [ssh(1)](../man1/ssh.1.md) 监听控制连接，但需要使用 ssh-askpass(1) 确认。如果无法打开 `ControlPath`，[ssh(1)](../man1/ssh.1.md) 将继续而不连接到主实例。X11 和 ssh-agent(1) 转发在这些多路复用连接上受支持，但是转发的显示和代理将是属于主连接的那个，即无法转发多个显示或代理。另外两个选项允许机会性多路复用：尝试使用主连接，但如果不存在则回退到创建新连接。这些选项是：`auto` 和 `autoask`。后者像 `ask` 选项一样需要确认。

**`ControlPath`** 指定用于上述 `ControlMaster` 章节中描述的连接共享的控制套接字路径，或字符串 `none` 以禁用连接共享。`ControlPath` 的参数可以使用波浪号语法引用用户主目录、Sx TOKENS 章节中描述的标记以及 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。建议用于机会性连接共享的任何 `ControlPath` 至少包含 %h、%p 和 %r（或替代的 %C），并放置在其他用户不可写的目录中。这确保共享连接被唯一标识。

**`ControlPersist`** 与 `ControlMaster` 结合使用时，指定主连接在初始客户端连接关闭后应保持在后台打开（等待未来的客户端连接）。如果设置为 `no`（默认），则主连接不会进入后台，并在初始客户端连接关闭后立即关闭。如果设置为 `yes` 或 0，则主连接将无限期地保留在后台（直到被杀死或通过诸如“ssh -O exit”之类的机制关闭）。如果设置为以秒为单位的时间，或 sshd_config(5) 中记录的任何格式的时间，则后台主连接将在保持空闲（没有客户端连接）指定时间后自动终止。

**`DynamicForward`** 指定本地机器上的 TCP 端口通过安全通道转发，然后使用应用协议来确定从远程机器连接到哪里。参数必须为 [`bind_address`:]`port`。IPv6 地址可以通过用方括号括起地址来指定。默认情况下，本地端口根据 `GatewayPorts` 设置绑定。但是，可以使用显式 `bind_address` 将连接绑定到特定地址。`localhost` 的 `bind_address` 表示监听端口仅绑定用于本地使用，而空地址或‘\*’表示端口应可从所有接口使用。目前支持 SOCKS4 和 SOCKS5 协议，[ssh(1)](../man1/ssh.1.md) 将充当 SOCKS 服务器。可以指定多个转发，并可在命令行上给出额外转发。只有超级用户可以转发特权端口。

**`EnableEscapeCommandline`** 为交互式会话在 `EscapeChar` 菜单中启用命令行选项（默认 `~C`）。默认情况下，命令行被禁用。

**`EnableSSHKeysign`** 在全局客户端配置文件 **`/etc/ssh/ssh_config`** 中将此选项设置为 `yes` 可在 `HostbasedAuthentication` 期间启用辅助程序 [ssh-keysign(8)](../man8/ssh-keysign.8.md)。参数必须为 `yes` 或 `no`（默认）。此选项应放在非主机特定部分。详见 [ssh-keysign(8)](../man8/ssh-keysign.8.md)。

**`EscapeChar`** 设置转义字符（默认：`~`）。转义字符也可以在命令行上设置。参数应为单个字符、`^` 后跟一个字母，或 `none` 以完全禁用转义字符（使连接对二进制数据透明）。

**`ExitOnForwardFailure`** 指定如果 [ssh(1)](../man1/ssh.1.md) 无法设置所有请求的动态、隧道、本地和远程端口转发（例如，任一端无法绑定和监听指定端口），是否应终止连接。注意 `ExitOnForwardFailure` 不适用于通过端口转发建立的连接，例如，如果到最终转发目标的 TCP 连接失败，不会导致 [ssh(1)](../man1/ssh.1.md) 退出。参数必须为 `yes` 或 `no`（默认）。

**`FingerprintHash`** 指定显示密钥指纹时使用的哈希算法。有效选项为：`md5` 和 `sha256`（默认）。

**`ForkAfterAuthentication`** 请求 `ssh` 在命令执行之前转入后台。如果 `ssh` 将要询问密码或口令短语，但用户希望它在后台运行，这很有用。这意味着 `StdinNull` 配置选项设置为“yes”。在远程站点启动 X11 程序的推荐方式是使用类似 `ssh -f host xterm` 的命令，如果 `ForkAfterAuthentication` 配置选项设置为“yes”，则等同于 `ssh host xterm`。如果 `ExitOnForwardFailure` 配置选项设置为“yes”，则使用 `ForkAfterAuthentication` 配置选项设置为“yes”启动的客户端将等待所有远程端口转发成功建立后再转入后台。此关键字的参数必须为 `yes`（同 `-f` 选项）或 `no`（默认）。

**`ForwardAgent`** 指定到认证代理（如果有）的连接是否将被转发到远程机器。参数可以为 `yes`、`no`（默认）、代理套接字的显式路径或用于查找路径的环境变量名（以‘$’开头）。应谨慎启用代理转发。有能力绕过远程主机上文件权限的用户（对于代理的 Unix 域套接字）可以通过转发的连接访问本地代理。攻击者无法从代理获取密钥材料，但他们可以对密钥执行操作，使他们能够使用加载到代理中的身份进行认证。

**`ForwardX11`** 指定是否将通过安全通道自动重定向 X11 连接并设置 `DISPLAY`。参数必须为 `yes` 或 `no`（默认）。应谨慎启用 X11 转发。有能力绕过远程主机上文件权限的用户（对于用户的 X11 授权数据库）可以通过转发的连接访问本地 X11 显示。如果同时启用了 `ForwardX11Trusted` 选项，攻击者可能能够执行诸如击键监控之类的活动。

**`ForwardX11Timeout`** 使用 sshd_config(5) 的 Sx TIME FORMATS 章节中描述的格式为不受信任的 X11 转发指定超时。在此时间之后 [ssh(1)](../man1/ssh.1.md) 接收的 X11 连接将被拒绝。将 `ForwardX11Timeout` 设置为零将禁用超时并允许在连接的生命周期内进行 X11 转发。默认是在 20 分钟后禁用不受信任的 X11 转发。

**`ForwardX11Trusted`** 如果此选项设置为 `yes`，远程 X11 客户端将拥有对原始 X11 显示的完全访问权限。如果此选项设置为 `no`（默认），远程 X11 客户端将被视为不受信任，并被阻止窃取或篡改属于受信任 X11 客户端的数据。此外，用于会话的 xauth(1) 令牌将设置为 20 分钟后过期。在此时间之后，远程客户端将被拒绝访问。有关不受信任客户端所受限制的完整详细信息，请参见 X11 SECURITY 扩展规范。

**`GatewayPorts`** 指定是否允许远程主机连接到本地转发端口。默认情况下，[ssh(1)](../man1/ssh.1.md) 将本地端口转发绑定到回环地址。这阻止了其他远程主机连接到转发端口。`GatewayPorts` 可用于指定 ssh 应将本地端口转发绑定到通配符地址，从而允许远程主机连接到转发端口。参数必须为 `yes` 或 `no`（默认）。

**`GlobalKnownHostsFile`** 指定用于全局主机密钥数据库的一个或多个文件，以空白分隔。默认为 **`/etc/ssh/ssh_known_hosts`**、**`/etc/ssh/ssh_known_hosts2`**。

**`GSSAPIAuthentication`** 指定是否允许基于 GSSAPI 的用户认证。默认为 `no`。

**`GSSAPIDelegateCredentials`** 向服务器转发（委托）凭据。默认为 `no`。

**`HashKnownHosts`** 指示 [ssh(1)](../man1/ssh.1.md) 在将主机名和地址添加到 `~/.ssh/known_hosts` 时应对其进行哈希处理。这些哈希名称可以被 [ssh(1)](../man1/ssh.1.md) 和 sshd(8) 正常使用，但如果文件内容泄露，它们不会在视觉上显示标识信息。默认为 `no`。注意，已知主机文件中现有的名称和地址不会自动转换，但可以使用 [ssh-keygen(1)](../man1/ssh-keygen.1.md) 手动哈希。

**`HostbasedAcceptedAlgorithms`** 指定将用于基于主机的认证的签名算法，作为以逗号分隔的模式列表。或者，如果指定列表以‘+’字符开头，则指定的签名算法将追加到默认集合而不是替换它。如果指定列表以‘-’字符开头，则指定的签名算法（包括通配符）将从默认集合中移除而不是替换它。如果指定列表以‘^’字符开头，则指定的签名算法将置于默认集合的开头。此选项的默认为：[ssh(1)](../man1/ssh.1.md) 的 `-Q` 选项可用于列出支持的签名算法。它以前名为 HostbasedKeyTypes。

**`HostbasedAuthentication`** 指定是否尝试基于 rhosts 的公钥认证。参数必须为 `yes` 或 `no`（默认）。

**`HostKeyAlgorithms`** 指定客户端想要使用的主机密钥签名算法的优先顺序。或者，如果指定列表以‘+’字符开头，则指定的签名算法将追加到默认集合而不是替换它。如果指定列表以‘-’字符开头，则指定的签名算法（包括通配符）将从默认集合中移除而不是替换它。如果指定列表以‘^’字符开头，则指定的签名算法将置于默认集合的开头。此选项的默认为：如果目标主机已知主机密钥，则此默认会被修改以优先使用其算法。可用签名算法列表也可以使用“ssh -Q HostKeyAlgorithms”获取。

**`HostKeyAlias`** 指定在主机密钥数据库文件中查找或保存主机密钥以及验证主机证书时应使用的别名，而不是真实主机名。此选项对于隧道 SSH 连接或在单个主机上运行的多个服务器很有用。

**`Hostname`** 指定要登录的真实主机名。这可用于指定主机的昵称或缩写。`Hostname` 的参数接受 Sx TOKENS 章节中描述的标记。也允许数字 IP 地址（在命令行和 `Hostname` 规格中）。默认为命令行中给出的名称。

**`IdentitiesOnly`** 指定 [ssh(1)](../man1/ssh.1.md) 应仅使用已配置的认证身份和证书文件（默认文件，或在 `ssh` 文件中显式配置的文件，或在 [ssh(1)](../man1/ssh.1.md) 命令行上传递的文件），即使 ssh-agent(1) 或 `PKCS11Provider` 或 `SecurityKeyProvider` 提供更多身份。此关键字的参数必须为 `yes` 或 `no`（默认）。此选项用于 ssh-agent 提供许多不同身份的情况。

**`IdentityAgent`** 指定用于与认证代理通信的 UNIX 域套接字。此选项覆盖 `SSH_AUTH_SOCK` 环境变量，可用于选择特定代理。将套接字名称设置为 `none` 禁用认证代理的使用。如果指定字符串“SSH_AUTH_SOCK”，将从 `SSH_AUTH_SOCK` 环境变量读取套接字位置。否则，如果指定值以‘$’字符开头，则将其视为包含套接字位置的环境变量。`IdentityAgent` 的参数可以使用波浪号语法引用用户主目录、Sx TOKENS 章节中描述的标记以及 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。

**`IdentityFile`** 指定从中读取用户 ECDSA、认证器托管的 ECDSA、Ed25519、认证器托管的 Ed25519 或 RSA 认证身份的文件。还可以指定公钥文件，以使用 ssh-agent(1) 中加载的相应私钥（当本地不存在私钥文件时）。默认为 `~/.ssh/id_rsa`、`~/.ssh/id_ecdsa`、`~/.ssh/id_ecdsa_sk`、`~/.ssh/id_ed25519` 和 `~/.ssh/id_ed25519_sk`。此外，除非设置了 `IdentitiesOnly`认证代理表示的任何身份都将用于认证。如果未通过 `CertificateFile` 显式指定证书，[ssh(1)](../man1/ssh.1.md) 将尝试从通过在指定 `IdentityFile` 路径后追加 `-cert.pub` 获得的文件名加载证书信息。`IdentityFile` 的参数可以使用波浪号语法引用用户主目录或 Sx TOKENS 章节中描述的标记。或者，参数 `none` 可用于指示不应加载任何身份文件。可以在配置文件中指定多个身份文件；所有这些身份将按顺序尝试。多个 `IdentityFile` 指令将添加到尝试的身份列表中（此行为与其他配置指令的行为不同）。`IdentityFile` 可与 `IdentitiesOnly` 结合使用，以选择认证期间提供的代理中的身份。`IdentityFile` 还可与 `CertificateFile` 结合使用，以提供认证所需的任何证书。

**`IgnoreUnknown`** 指定在配置解析时遇到未知选项时要忽略的模式列表。如果 `ssh` 包含 [ssh(1)](../man1/ssh.1.md) 无法识别的选项，这可用于抑制错误。建议在配置文件中尽早列出 `IgnoreUnknown`，因为它不会应用于出现在它之前的未知选项。

**`Include`** 包含指定的配置文件。可以指定多个路径名，每个路径名可以包含 glob(7) 通配符、Sx TOKENS 章节中描述的标记、Sx ENVIRONMENT VARIABLES 章节中描述的环境变量，以及对于用户配置，类似 shell 的‘~’引用用户主目录。通配符将按字典顺序展开和处理。没有绝对路径的文件假定位于 `~/.ssh`（如果包含在用户配置文件中）或 **`/etc/ssh`**（如果从系统配置文件包含）。`Include` 指令可以出现在 `Match` 或 `Host` 块内，以执行条件包含。

**`IPQoS`** 指定连接的*差分服务字段代码点*（DSCP）值。接受的值为 `af11`、`af12`、`af13`、`af21`、`af22`、`af23`、`af31`、`af32`、`af33`、`af41`、`af42`、`af43`、`cs0`、`cs1`、`cs2`、`cs3`、`cs4`、`cs5`、`cs6`、`cs7`、`ef`、`le`、数字值或 `none` 以使用操作系统默认值。此选项可以接受一个或两个参数，以空白分隔。如果指定一个参数，它无条件地用作数据包类。如果指定两个值，第一个自动用于交互式会话，第二个用于非交互式会话。默认为 `ef`（加速转发）用于交互式会话，`none`（操作系统默认值）用于非交互式会话。

**`KbdInteractiveAuthentication`** 指定是否使用键盘交互认证。此关键字的参数必须为 `yes`（默认）或 `no`。`ChallengeResponseAuthentication` 是其已弃用的别名。

**`KbdInteractiveDevices`** 指定在键盘交互认证中使用的方法列表。多个方法名必须用逗号分隔。默认使用服务器指定的列表。可用方法因服务器支持而异。对于 OpenSSH 服务器，它可以是以下零个或多个：`bsdauth` 和 `pam`。

**`KexAlgorithms`** 指定将使用的允许的 KEX（密钥交换）算法及其优先顺序。选择的算法将是此列表中服务器也支持的第一个算法。多个算法必须用逗号分隔。如果指定列表以‘+’字符开头，则指定的算法将追加到默认集合而不是替换它。如果指定列表以‘-’字符开头，则指定的算法（包括通配符）将从默认集合中移除而不是替换它。如果指定列表以‘^’字符开头，则指定的算法将置于默认集合的开头。默认为：支持的密钥交换算法列表也可以使用“ssh -Q kex”获取。

**`KnownHostsCommand`** 指定用于获取主机密钥列表的命令，除了 `UserKnownHostsFile` 和 `GlobalKnownHostsFile` 中列出的之外。此命令在读取文件之后执行。它可以将主机密钥行写入标准输出，格式与通常文件相同（详见 [ssh(1)](../man1/ssh.1.md) 中的 Sx VERIFYING HOST KEYS 章节）。`KnownHostsCommand` 的参数接受 Sx TOKENS 章节中描述的标记。此命令可能每连接调用多次：一次在准备要使用的主机密钥算法偏好列表时，再次获取请求主机名的主机密钥，如果启用了 `CheckHostIP`，还有一次获取与服务器地址匹配的主机密钥。如果命令异常退出或返回非零退出状态，则连接终止。

**`LocalCommand`** 指定成功连接到服务器后在本地机器上执行的命令。命令字符串延伸到行尾，并使用用户的 shell 执行。`LocalCommand` 的参数接受 Sx TOKENS 章节中描述的标记。命令同步运行，并且无法访问产生它的 [ssh(1)](../man1/ssh.1.md) 的会话。它不应用于交互式命令。除非已启用 `PermitLocalCommand`，否则忽略此指令。

**`LocalForward`** 指定本地机器上的 TCP 端口或 Unix 域套接字通过安全通道转发到远程机器上指定的主机和端口（或 Unix 域套接字）。对于 TCP 端口，第一个参数必须是 [`bind_address`:]`port` 或 Unix 域套接字路径。第二个参数是目标，可以是 `host`:`hostport` 或 Unix 域套接字路径（如果远程主机支持）。IPv6 地址可以通过用方括号括起地址来指定。如果任一参数包含‘/’，该参数将被解释为（相应主机上的）Unix 域套接字而不是 TCP 端口。可以指定多个转发，并可在命令行上给出额外转发。只有超级用户可以转发特权端口。默认情况下，本地端口根据 `GatewayPorts` 设置绑定。但是，可以使用显式 `bind_address` 将连接绑定到特定地址。`localhost` 的 `bind_address` 表示监听端口仅绑定用于本地使用，而空地址或‘\*’表示端口应可从所有接口使用。Unix 域套接字路径可以使用 Sx TOKENS 章节中描述的标记和 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。

**`LogLevel`** 给出从 [ssh(1)](../man1/ssh.1.md) 记录消息时使用的详细级别。可能的值为：QUIET、FATAL、ERROR、INFO、VERBOSE、DEBUG、DEBUG1、DEBUG2 和 DEBUG3。默认为 INFO。DEBUG 和 DEBUG1 等效。DEBUG2 和 DEBUG3 各自指定更高级别的详细输出。

**`LogVerbose`** 指定对 LogLevel 的一个或多个覆盖。覆盖由一个或多个模式列表组成，匹配源文件、函数和行号以强制详细日志记录。例如，覆盖模式：将为 `kex.c` 的第 1000 行、Fn kex_exchange_identification 函数中的所有内容以及 `packet.c` 文件中的所有代码启用详细日志记录。此选项用于调试，默认不启用任何覆盖。

**`MACs`** 按优先顺序指定 MAC（消息认证码）算法。MAC 算法用于数据完整性保护。多个算法必须用逗号分隔。如果指定列表以‘+’字符开头，则指定的算法将追加到默认集合而不是替换它。如果指定列表以‘-’字符开头，则指定的算法（包括通配符）将从默认集合中移除而不是替换它。如果指定列表以‘^’字符开头，则指定的算法将置于默认集合的开头。包含“-etm”的算法在加密之后计算 MAC（encrypt-then-mac）。这些被认为更安全，建议使用。默认为：可用 MAC 算法列表也可以使用“ssh -Q mac”获取。

**`NoHostAuthenticationForLocalhost`** 禁用 localhost（回环地址）的主机认证。此关键字的参数必须为 `yes` 或 `no`（默认）。

**`NumberOfPasswordPrompts`** 指定放弃之前的密码提示次数。此关键字的参数必须为整数。默认为 3。

**`ObscureKeystrokeTiming`** 指定 [ssh(1)](../man1/ssh.1.md) 是否应尝试对网络流量的被动观察者隐藏击键间隔时间。如果启用，则对于交互式会话，[ssh(1)](../man1/ssh.1.md) 将以几十毫秒的固定间隔发送击键，并在输入停止后一段时间内发送虚假击键数据包。此关键字的参数必须为 `yes`、`no` 或形式为 `interval:milliseconds` 的间隔指定符（例如 `interval:80` 表示 80 毫秒）。默认是使用 20ms 数据包间隔隐藏击键。注意，较小的间隔将导致更高的虚假击键数据包速率。

**`PasswordAuthentication`** 指定是否使用密码认证。此关键字的参数必须为 `yes`（默认）或 `no`。

**`PermitLocalCommand`** 允许通过 `LocalCommand` 选项或使用 [ssh(1)](../man1/ssh.1.md) 中的 `!``command` 转义序列执行本地命令。参数必须为 `yes` 或 `no`（默认）。

**`PermitRemoteOpen`** 指定当 `RemoteForward` 用作 SOCKS 代理时允许远程 TCP 端口转发的目标。转发规格必须是以下形式之一：可以通过用空白分隔来指定多个转发。参数 `any` 可用于移除所有限制并允许任何转发请求。参数 `none` 可用于禁止所有转发请求。通配符‘\*’可用于主机或端口，分别允许所有主机或端口。否则，不对提供的名称执行模式匹配或地址查找。

**`PKCS11Provider`** 指定要使用的 PKCS#11 提供程序，或 `none` 表示不应使用任何提供程序（默认）。此关键字的参数是 [ssh(1)](../man1/ssh.1.md) 应使用的 PKCS#11 共享库路径，用于与提供用户认证密钥的 PKCS#11 令牌通信。

**`Port`** 指定在远程主机上连接的端口号。默认为 22。

**`PreferredAuthentications`** 指定客户端应尝试认证方法的顺序。这允许客户端优先使用一种方法（例如 `keyboard-interactive`）而非另一种方法（例如 `password`）。默认为：

**`ProxyCommand`** 指定用于连接服务器的命令。命令字符串延伸到行尾，并使用用户的 shell `exec` 指令执行，以避免残留的 shell 进程。`ProxyCommand` 的参数接受 Sx TOKENS 章节中描述的标记。命令基本上可以是任何内容，应从其标准输入读取并写入其标准输出。它最终应连接某台机器上运行的 sshd(8) 服务器，或在某处执行 `sshd -i`。主机密钥管理将使用所连接主机的 `Hostname`（默认为用户键入的名称）完成。将命令设置为 `none` 完全禁用此选项。注意 `CheckHostIP` 对于使用代理命令的连接不可用。此指令与 [nc(1)](../man1/nc.1.md) 及其代理支持结合使用很有用。例如，以下指令将通过 192.0.2.0 的 HTTP 代理连接：

**`ProxyJump`** 指定一个或多个跳转代理，形式为 [`user`@]`host`[:`port`] 或 ssh URI。多个代理可以用逗号分隔，将按顺序访问。设置此选项将导致 [ssh(1)](../man1/ssh.1.md) 先连接到指定的 `ProxyJump` 主机，然后从那里建立到最终目标的 TCP 转发，从而连接到目标主机。将主机设置为 `none` 完全禁用此选项。注意此选项将与 `ProxyCommand` 选项竞争——先指定的将阻止后者的后续实例生效。还注意目标主机的配置（通过命令行或配置文件提供）通常不应用于跳转主机。如果跳转主机需要特定配置，应使用 `~/.ssh/config`。

**`ProxyUseFdpass`** 指定 `ProxyCommand` 将连接的文件描述符传回 [ssh(1)](../man1/ssh.1.md)，而不是继续执行和传递数据。默认为 `no`。

**`PubkeyAcceptedAlgorithms`** 指定将用于公钥认证的签名算法，作为以逗号分隔的模式列表。如果指定列表以‘+’字符开头，则其后的算法将追加到默认集合而不是替换它。如果指定列表以‘-’字符开头，则指定的算法（包括通配符）将从默认集合中移除而不是替换它。如果指定列表以‘^’字符开头，则指定的算法将置于默认集合的开头。此选项的默认为：可用签名算法列表也可以使用“ssh -Q PubkeyAcceptedAlgorithms”获取。

**`PubkeyAuthentication`** 指定是否尝试公钥认证。此关键字的参数必须为 `yes`（默认）、`no`、`unbound` 或 `host-bound`。最后两个选项启用公钥认证，同时分别禁用或启用受限 ssh-agent(1) 转发所需的 OpenSSH 主机绑定认证协议扩展。

**`RefuseConnection`** 允许配置文件拒绝连接。如果指定此选项，则 [ssh(1)](../man1/ssh.1.md) 将在尝试连接远程主机之前立即终止，显示包含此关键字参数的错误消息，并返回非零退出状态。此选项可用于通过 `ssh` 向用户表达提醒或警告。

**`RekeyLimit`** 指定在重新协商会话密钥之前可以传输或接收的最大数据量，可选后跟重新协商会话密钥之前可能经过的最大时间量。第一个参数以字节为单位指定，可以带有‘K’、‘M’或‘G’后缀，分别表示千字节、兆字节或吉字节。默认在‘1G’和‘4G’之间，取决于密码。可选的第二个值以秒为单位指定，可以使用 sshd_config(5) 的 TIME FORMATS 章节中记录的任何单位。`RekeyLimit` 的默认值为 `default none`，表示在发送或接收了密码默认数量的数据后执行重新加密，不执行基于时间的重新加密。

**`RemoteCommand`** 指定成功连接到服务器后在远程机器上执行的命令。命令字符串延伸到行尾，并使用用户的 shell 执行。`RemoteCommand` 的参数接受 Sx TOKENS 章节中描述的标记。

**`RemoteForward`** 指定远程机器上的 TCP 端口或 Unix 域套接字通过安全通道转发。远程端口可以转发到本地机器上指定的主机和端口或 Unix 域套接字，或充当 SOCKS 4/5 代理，允许远程客户端从本地机器连接到任意目标。第一个参数是监听规格，可以是 [`bind_address`:]`port`，或者如果远程主机支持，是 Unix 域套接字路径。如果转发到特定目标，则第二个参数必须是 `host`:`hostport` 或 Unix 域套接字路径，否则如果未指定目标参数，则远程转发将建立为 SOCKS 代理。当充当 SOCKS 代理时，连接的目标可以由 `PermitRemoteOpen` 限制。IPv6 地址可以通过用方括号括起地址来指定。如果任一参数包含‘/’，该参数将被解释为（相应主机上的）Unix 域套接字而不是 TCP 端口。可以指定多个转发，并可在命令行上给出额外转发。只有以 root 身份登录远程机器时才能转发特权端口。Unix 域套接字路径可以使用 Sx TOKENS 章节中描述的标记和 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。如果 `port` 参数为 0，监听端口将在服务器上动态分配并在运行时报告给客户端。如果未指定 `bind_address`，默认仅绑定到回环地址。如果 `bind_address` 为‘\*’或空字符串，则请求转发在所有接口上监听。指定远程 `bind_address` 只有在服务器启用了 `GatewayPorts` 选项时才会成功（参见 sshd_config(5)）。

**`RequestTTY`** 指定是否为会话请求伪终端。参数可以是以下之一：`no`（从不请求 TTY）、`yes`（当标准输入为 TTY 时总是请求 TTY）、`force`（总是请求 TTY）或 `auto`（当打开登录会话时请求 TTY）。此选项对应 [ssh(1)](../man1/ssh.1.md) 的 `-t` 和 `-T` 标志。

**`RequiredRSASize`** 指定 [ssh(1)](../man1/ssh.1.md) 接受的最小 RSA 密钥大小（以位为单位）。小于此限制的用户认证密钥将被忽略。提供小于此限制的主机密钥的服务器将导致连接终止。默认为 `1024` 位。注意此限制只能从默认值提高。

**`RevokedHostKeys`** 指定已吊销的主机公钥。此文件中列出的密钥将被拒绝用于主机认证。注意，如果此文件不存在或不可读，则所有主机的主机认证都将被拒绝。密钥可以指定为文本文件（每行列出一个公钥），或指定为由 [ssh-keygen(1)](../man1/ssh-keygen.1.md) 生成的 OpenSSH 密钥吊销列表（KRL）。有关 KRL 的更多信息，请参见 [ssh-keygen(1)](../man1/ssh-keygen.1.md) 中的 KEY REVOCATION LISTS 章节。`RevokedHostKeys` 的参数可以使用波浪号语法引用用户主目录、Sx TOKENS 章节中描述的标记以及 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。

**`SecurityKeyProvider`** 指定加载任何 FIDO 认证器托管密钥时要使用的库路径，覆盖使用内置 USB HID 支持的默认值。如果指定值以‘$’字符开头，则将其视为包含库路径的环境变量。

**`SendEnv`** 指定本地 [environ(7)](../man7/environ.7.md) 中的哪些变量应发送到服务器。服务器也必须支持它，并且服务器必须配置为接受这些环境变量。注意，每当请求伪终端时，`TERM` 环境变量总是被发送，因为协议要求它。有关如何配置服务器，请参见 sshd_config(5) 中的 `AcceptEnv`。变量按名称指定，可以包含通配符。多个环境变量可以用空白分隔或分布在多个 `SendEnv` 指令中。有关模式的更多信息，请参见 Sx PATTERNS。可以通过在模式前加 `-` 来清除先前设置的 `SendEnv` 变量名。默认不发送任何环境变量。

**`ServerAliveCountMax`** 设置在 [ssh(1)](../man1/ssh.1.md) 未收到服务器任何消息的情况下可以发送的服务器存活消息数（见下文）。如果在发送服务器存活消息时达到此阈值，ssh 将断开与服务器的连接，终止会话。重要的是要注意，服务器存活消息的使用与 `TCPKeepAlive`（下文）非常不同。服务器存活消息通过加密通道发送，因此不可被伪造。`TCPKeepAlive` 启用的 TCP keepalive 选项可被伪造。服务器存活机制在客户端或服务器依赖了解连接何时变得无响应时很有价值。默认值为 3。例如，如果 `ServerAliveInterval`（见下文）设置为 15 且 `ServerAliveCountMax` 保留默认值，如果服务器变得无响应，ssh 将在大约 45 秒后断开连接。

**`ServerAliveInterval`** 设置以秒为单位的超时间隔，如果在此时间内未从服务器收到数据，[ssh(1)](../man1/ssh.1.md) 将通过加密通道发送消息请求服务器响应。默认为 0，表示不向服务器发送这些消息。

**`SessionType`** 可用于请求在远程系统上调用子系统，或完全阻止远程命令的执行。后者仅用于转发端口。此关键字的参数必须为 `none`（同 `-N` 选项）、`subsystem`（同 `-s` 选项）或 `default`（shell 或命令执行）。

**`SetEnv`** 直接以“NAME=VALUE”形式指定一个或多个要发送到服务器的环境变量及其内容。与 `SendEnv` 类似，`TERM` 变量除外，服务器必须准备接受环境变量。“VALUE”可以使用 Sx TOKENS 章节中描述的标记和 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。

**`StdinNull`** 从 **`/dev/null`** 重定向 stdin（实际上阻止从 stdin 读取）。当 `ssh` 在后台运行时，必须使用此选项或等效的 `-n` 选项。此关键字的参数必须为 `yes`（同 `-n` 选项）或 `no`（默认）。

**`StreamLocalBindMask`** 设置为本地或远程端口转发创建 Unix 域套接字文件时使用的八进制文件创建模式掩码（umask）。此选项仅用于到 Unix 域套接字文件的端口转发。默认值为 0177，创建仅所有者可读写的 Unix 域套接字文件。注意，并非所有操作系统都遵循 Unix 域套接字文件上的文件模式。

**`StreamLocalBindUnlink`** 指定在创建新的本地或远程端口转发的 Unix 域套接字文件之前是否移除现有的。如果套接字文件已存在且未启用 `StreamLocalBindUnlink`，`ssh` 将无法将端口转发到该 Unix 域套接字文件。此选项仅用于到 Unix 域套接字文件的端口转发。参数必须为 `yes` 或 `no`（默认）。

**`StrictHostKeyChecking`** 如果此标志设置为 `yes`，[ssh(1)](../man1/ssh.1.md) 将永远不会自动将主机密钥添加到 `~/.ssh/known_hosts` 文件，并拒绝连接到主机密钥已更改的主机。这提供了对中间人（MITM）攻击的最大保护，尽管当 **`/etc/ssh/ssh_known_hosts`** 文件维护不善或频繁连接到新主机时可能会令人烦恼。此选项强制用户手动添加所有新主机。如果此标志设置为 `accept-new`，则 ssh 将自动将新主机密钥添加到用户的 `known_hosts` 文件，但不允许连接到主机密钥已更改的主机。如果此标志设置为 `no` 或 `off`，ssh 将自动将新主机密钥添加到用户的已知主机文件，并允许连接到主机密钥已更改的主机（受一些限制）。如果此标志设置为 `ask`（默认），新主机密钥只有在用户确认后才添加到用户的已知主机文件，ssh 将拒绝连接到主机密钥已更改的主机。在所有情况下，已知主机的主机密钥都将自动验证。

**`SyslogFacility`** 给出从 [ssh(1)](../man1/ssh.1.md) 记录消息时使用的设施代码。可能的值为：DAEMON、USER、AUTH、LOCAL0、LOCAL1、LOCAL2、LOCAL3、LOCAL4、LOCAL5、LOCAL6、LOCAL7。默认为 USER。

**`TCPKeepAlive`** 指定系统是否应向另一端发送 TCP keepalive 消息。如果发送它们，将正确注意到连接的死亡或其中一台机器的崩溃。然而，这意味着如果路由暂时不可用，连接将死亡，一些人觉得这很烦人。默认为 `yes`（发送 TCP keepalive 消息），客户端将注意到网络断开或远程主机死亡。这在脚本中很重要，许多用户也希望如此。要禁用 TCP keepalive 消息，值应设置为 `no`。另请参见 `ServerAliveInterval` 以了解协议级 keepalive。

**`Tag`** 指定一个配置标记名称，稍后可由 `Match` 指令用于选择配置块。

**`Tunnel`** 请求客户端和服务器之间的 [tun(4)](../man4/tun.4.md) 设备转发。参数必须为 `yes`、`point-to-point`（第 3 层）、`ethernet`（第 2 层）或 `no`（默认）。指定 `yes` 请求默认隧道模式，即 `point-to-point`。

**`TunnelDevice`** 指定在客户端（`local_tun`）和服务器（`remote_tun`）上打开的 [tun(4)](../man4/tun.4.md) 设备。参数必须为 `local_tun`[:`remote_tun`]。设备可以按数字 ID 或关键字 `any` 指定，`any` 使用下一个可用的隧道设备。如果未指定 `remote_tun`，默认为 `any`。默认为 `any:any`。

**`UpdateHostKeys`** 指定 [ssh(1)](../man1/ssh.1.md) 是否应接受认证完成后服务器发送的额外主机密钥通知，并将它们添加到 `UserKnownHostsFile`。参数必须为 `yes`、`no` 或 `ask`。此选项允许学习服务器的备用主机密钥，并通过允许服务器在移除旧密钥之前发送替换公钥来支持平滑的密钥轮换。只有当用于认证主机的密钥已经被信任或用户显式接受、主机通过 `UserKnownHostsFile`（即非 `GlobalKnownHostsFile`）认证、主机使用普通密钥而非证书认证时，才接受额外主机密钥。如果用户未覆盖默认的 `UserKnownHostsFile` 设置且未启用 `VerifyHostKeyDNS`，则 `UpdateHostKeys` 默认启用，否则 `UpdateHostKeys` 将设置为 `no`。如果 `UpdateHostKeys` 设置为 `ask`，则将要求用户确认对 known_hosts 文件的修改。确认目前与 `ControlPersist` 不兼容，如果启用了它，将被禁用。目前，只有 OpenSSH 6.8 及更高版本的 sshd(8) 支持用于通知客户端所有服务器主机密钥的“hostkeys@openssh.com”协议扩展。

**`User`** 指定要登录的用户。当在不同机器上使用不同用户名时，这很有用。这省去了在命令行上记得给出用户名的麻烦。`User` 的参数可以使用 Sx TOKENS 章节中描述的标记（%r 和 %C 除外）以及 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。

**`UserKnownHostsFile`** 指定用于用户主机密钥数据库的一个或多个文件，以空白分隔。每个文件名可以使用波浪号表示法引用用户主目录、Sx TOKENS 章节中描述的标记以及 Sx ENVIRONMENT VARIABLES 章节中描述的环境变量。值为 `none` 导致 [ssh(1)](../man1/ssh.1.md) 忽略任何用户特定的已知主机文件。默认为 `~/.ssh/known_hosts`、`~/.ssh/known_hosts2`。

**`VerifyHostKeyDNS`** 指定是否使用 DNS 和 SSHFP 资源记录验证远程密钥。如果此选项设置为 `yes`，客户端将隐式信任与 DNS 安全指纹匹配的密钥。不安全的指纹将按照此选项设置为 `ask` 处理。如果此选项设置为 `ask`，将显示指纹匹配信息，但用户仍需根据 `StrictHostKeyChecking` 选项确认新主机密钥。默认为 `no`。另请参见 [ssh(1)](../man1/ssh.1.md) 中的 Sx VERIFYING HOST KEYS。

**`VersionAddendum`** 可选地指定要追加到客户端在连接时发送的 SSH 协议横幅的附加文本。默认为 `none`。

**`VisualHostKey`** 如果此标志设置为 `yes`，除了在登录时和对于未知主机密钥打印指纹字符串外，还将打印远程主机密钥指纹的 ASCII 艺术表示。如果此标志设置为 `no`（默认），登录时不打印指纹字符串，对于未知主机密钥仅打印指纹字符串。

**`WarnWeakCrypto`** 控制当为连接协商的加密算法较弱或不推荐使用时是否警告用户。可以通过关闭特定警告或禁用所有警告来禁用警告。可以使用 `no-pq-kex` 标志禁用关于不使用后量子密钥交换的连接的警告。`no` 将禁用所有警告。默认等效于 `yes`，即启用所有警告。

**`XAuthLocation`** 指定 xauth(1) 程序的完整路径名。默认为 **`/usr/local/bin/xauth`**。

## PATTERNS

*模式*由零个或多个非空白字符、‘\*’（匹配零个或多个字符的通配符）或‘?’（匹配恰好一个字符的通配符）组成。例如，要为“.co.uk”域集合中的任何主机指定一组声明，可以使用以下模式：

```sh
Host *.co.uk
```

以下模式将匹配 192.168.0.[0-9] 网络范围内的任何主机：

```sh
Host 192.168.0.?
```

*模式列表*是以逗号分隔的模式列表。模式列表中的模式可以通过在前面加感叹号（‘!’）来取反。例如，要允许从组织中除“dialup”池之外的任何地方使用密钥，可以使用以下条目（在 authorized_keys 中）：

```sh
from="!*.dialup.example.com,*.example.com"
```

注意，取反匹配本身永远不会产生肯定结果。例如，尝试针对以下模式列表匹配“host3”将失败：

```sh
from="!host1,!host2"
```

这里的解决方案是包含一个会产生肯定匹配的项，例如通配符：

```sh
from="!host1,!host2,*"
```

## TOKENS

某些关键字的参数可以使用标记，这些标记在运行时展开。标记展开时不加引号或转义 shell 字符。用户有责任确保它们在使用上下文中是安全的。

`ssh` 中支持的标记有：

**%%** 字面量‘%’。
**%C** %l%h%p%r%j 的哈希。
**%d** 本地用户主目录。
**%f** 服务器主机密钥的指纹。
**%H** 正在搜索的 `known_hosts` 主机名或地址。
**%h** 远程主机名。
**%I** 描述 `KnownHostsCommand` 执行原因的字符串：按地址查找主机时为 `ADDRESS`（仅在启用 `CheckHostIP` 时）、按主机名搜索时为 `HOSTNAME`，或准备目标主机的主机密钥算法偏好列表时为 `ORDER`。
**%i** 本地用户 ID。
**%j** ProxyJump 选项的内容，如果未设置此选项则为空字符串。
**%K** base64 编码的主机密钥。
**%k** 如果指定了主机密钥别名，则为该别名，否则为命令行中给出的原始远程主机名。
**%L** 本地主机名。
**%l** 本地主机名，包括域名。
**%n** 原始远程主机名，如命令行中给出。
**%p** 远程端口。
**%r** 远程用户名。
**%T** 如果请求了隧道转发，分配的本地 [tun(4)](../man4/tun.4.md) 或 [tap(4)](../man4/tap.4.md) 网络接口，否则为“NONE”。
**%t** 服务器主机密钥的类型，例如 `ssh-ed25519`。
**%u** 本地用户名。

`CertificateFile`、`ControlPath`、`IdentityAgent`、`IdentityFile`、`Include`、`KnownHostsCommand`、`LocalForward`、`Match exec`、`RemoteCommand`、`RemoteForward`、`RevokedHostKeys`、`UserKnownHostsFile` 和 `VersionAddendum` 接受标记 %%、%C、%d、%h、%i、%j、%k、%L、%l、%n、%p、%r 和 %u。

`KnownHostsCommand` 额外接受标记 %f、%H、%I、%K 和 %t。

`Hostname` 接受标记 %% 和 %h。

`LocalCommand` 接受所有标记。

`ProxyCommand` 和 `ProxyJump` 接受标记 %%、%h、%n、%p 和 %r。

注意，其中某些指令构建通过 shell 执行的命令。由于 [ssh(1)](../man1/ssh.1.md) 不对在 shell 命令中具有特殊含义的字符（如引号）进行过滤或转义，用户有责任确保传递给 [ssh(1)](../man1/ssh.1.md) 的参数不包含此类字符，并且标记在使用时已适当加引号。

## 环境变量

某些关键字的参数可以在运行时从客户端的环境变量中展开，方法是用 `${}` 括起它们，例如 `${HOME}/.ssh` 将引用用户的 .ssh 目录。如果指定的环境变量不存在，将返回错误并忽略该关键字的设置。

关键字 `CertificateFile`、`ControlPath`、`IdentityAgent`、`IdentityFile`、`Include`、`KnownHostsCommand` 和 `UserKnownHostsFile` 支持环境变量。关键字 `LocalForward` 和 `RemoteForward` 仅对 Unix 域套接字路径支持环境变量。

## 文件

**`~/.ssh/config`** 这是每用户配置文件。此文件的格式如上所述。此文件由 SSH 客户端使用。由于可能被滥用，此文件必须具有严格权限：用户可读写，其他人不可写。

**`/etc/ssh/ssh_config`** 系统范围的配置文件。此文件为用户配置文件中未指定的值以及没有配置文件的用户提供默认值。此文件必须对所有用户可读。

## 参见

[ssh(1)](../man1/ssh.1.md)

## 作者

OpenSSH 是 Tatu Ylonen 发布的原始且免费的 ssh 1.2.12 版本的衍生作品。Aaron Campbell、Bob Beck、Markus Friedl、Niels Provos、Theo de Raadt 和 Dug Song 修复了许多 bug，重新添加了新功能并创建了 OpenSSH。Markus Friedl 贡献了对 SSH 协议版本 1.5 和 2.0 的支持。
