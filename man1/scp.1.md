# scp.1

`scp` — OpenSSH 安全文件复制

## 名称

`scp`

## 概要

`scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config] [-i identity_file] [-J destination] [-l limit] [-o ssh_option] [-P port] [-S program] [-X sftp_option] source ... target`

## 描述

`scp` 在网络上的主机之间复制文件。

`scp` 通过 [ssh(1)](ssh.1.md) 连接使用 SFTP 协议进行数据传输，并使用与登录会话相同的认证机制和安全保障。

如果认证需要密码或口令，`scp` 会提示输入。

`source` 和 `target` 可以指定为本地路径名、形式为 `[user@]host:[path]` 的远程主机（带可选路径），或形式为 `scp://[user@]host[:port][/path]` 的 URI。本地文件名可使用绝对或相对路径名显式指定，以避免 `scp` 将包含“:”的文件名视为主机说明符。

在两台远程主机之间复制时，如果使用 URI 格式，且使用了 `-R` 选项，则 `target` 上不能指定 `port`。

选项如下：

**`-3`** 在两台远程主机之间复制时，数据通过本地主机中转。此模式为默认模式，但参见 `-R` 选项以直接在两台远程主机之间复制数据。注意，使用传统 SCP 协议（通过 `-O` 标志）时，此选项为第二台主机选择批处理模式，因为 `scp` 无法同时向两台主机询问密码或口令。

**`-4`** 强制 `scp` 仅使用 IPv4 地址。

**`-6`** 强制 `scp` 仅使用 IPv6 地址。

**`-A`** 允许将 ssh-agent(1) 转发到远程系统。默认不转发认证代理。

**`-B`** 选择批处理模式（阻止询问密码或口令）。

**`-C`** 启用压缩。将 `-C` 标志传递给 [ssh(1)](ssh.1.md) 以启用压缩。

**`-c`** `cipher` 选择用于加密数据传输的密码。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-D`** `sftp_server_path` 直接连接到本地 SFTP 服务器程序，而非通过 [ssh(1)](ssh.1.md) 连接远程服务器。此选项在调试客户端和服务器时可能有用。

**`-F`** `ssh_config` 为 `ssh` 指定一个替代的每用户配置文件。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-i`** `identity_file` 选择从中读取公钥认证身份（私钥）的文件。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-J`** `destination` 首先建立到 `destination` 所描述跳转主机的 `ssh` 连接，然后从那里建立到最终目标的 TCP 转发，从而连接到目标主机。可以通过逗号分隔指定多个跳转跳。这是指定 `ProxyJump` 配置指令的快捷方式。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-l`** `limit` 限制使用的带宽，以 Kbit/s 为单位指定。

**`-O`** 使用传统 SCP 协议而非 SFTP 协议进行文件传输。对于不实现 SFTP 的服务器、为了向后兼容特定的文件名通配模式，以及为较旧的 SFTP 服务器扩展以“~”为前缀的路径，可能需要强制使用 SCP 协议。

**`-o`** `ssh_option` 可用于以 ssh_config(5) 中使用的格式向 `ssh` 传递选项。这对于指定没有单独 `scp` 命令行标志的选项很有用。有关下列选项及其可能值的完整详情，参见 ssh_config(5)。

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

**`nrequests`**=`value` 控制下载或上传期间任何时刻可能同时进行的 SFTP 读或写请求数量。默认最多 64 个请求可同时活动。

**`buffer`**=`value` 控制下载或上传期间单次 SFTP 读/写操作使用的最大缓冲区大小。默认使用 32KB 缓冲区。

**`-P`** `port` 指定要连接的远程主机上的端口。注意，此选项使用大写“P”，因为 `-p` 已保留用于保留文件的时间和模式位。

**`-p`** 保留源文件的修改时间、访问时间和文件模式位。

**`-q`** 静默模式：禁用进度指示器以及来自 [ssh(1)](ssh.1.md) 的警告和诊断消息。

**`-R`** 默认情况下，两台远程主机之间的复制通过本地主机中转。此选项改为通过连接到源主机并在那里执行 `scp` 来在两台远程主机之间复制。这要求源主机上运行的 `scp` 能够无需密码即可认证到目标主机。

**`-r`** 递归复制整个目录。注意，`scp` 会跟随目录树遍历中遇到的符号链接。

**`-S`** `program` 用于加密连接的 `program` 名称。该程序必须理解 [ssh(1)](ssh.1.md) 选项。

**`-T`** 禁用严格文件名检查。默认情况下，从远程主机复制文件到本地目录时，`scp` 会检查接收到的文件名是否与命令行上请求的文件名匹配，以防止远程端发送意外或不需要的文件。由于不同操作系统和 shell 解释文件名通配符的方式不同，这些检查可能导致所需文件被拒绝。此选项禁用这些检查，代价是完全信任服务器不会发送意外文件名。

**`-v`** 详细模式。使 `scp` 和 [ssh(1)](ssh.1.md) 打印有关进度的调试消息。这有助于调试连接、认证和配置问题。

**`-X`** `sftp_option` 指定控制 SFTP 协议行为某些方面的选项。有效选项为：

## 退出状态

`scp` 实用程序成功时退出值为 0，发生错误时大于 0。

## 参见

[sftp(1)](sftp.1.md), [ssh(1)](ssh.1.md), ssh-add(1), ssh-agent(1), [ssh-keygen(1)](ssh-keygen.1.md), ssh_config(5), sftp-server(8), sshd(8)

## 历史

`scp` 基于 BSD 源代码中加州大学董事会（Regents of the University of California）的 rcp 程序。

自 OpenSSH 9.0 起，`scp` 默认使用 SFTP 协议进行传输。

## 作者

Timo Rinne <tri@iki.fi> Tatu Ylonen <ylo@cs.hut.fi>

## 注意事项

传统 SCP 协议（由 `-O` 标志选择）需要执行远程用户的 shell 来进行 glob(3) 模式匹配。这要求对任何在远程 shell 中有特殊含义的字符（如引号字符）进行仔细引用。
