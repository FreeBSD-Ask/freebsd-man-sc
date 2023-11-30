  SCP(1)  

SCP(1)

FreeBSD General Commands Manual

SCP(1)

[名称](#__u540D___u79F0_)
=======================

`scp` —

安全复制（远程文件复制程序）

[概要](#__u6982___u8981_)
=======================

`scp` \[`-346BCpqrTv`\] \[`-c` cipher\] \[`-F` ssh\_config\] \[`-i` identity\_file\] \[`-l` limit\] \[`-o` ssh\_option\] \[`-P` port\] \[`-S` program\] source ... target

[描述](#__u63CF___u8FF0_)
=======================

`scp` 在网络上的主机之间复制文件。 它使用 ssh(1) 进行数据传输，并使用相同的身份验证并提供与 ssh(1) 相同的安全性。 如果身份验证需要密码或密码短语， `scp` 将询问它们。

source 和 target 可以指定为本地路径名、具有 \[user@\]host:\[path\], 形式的可选路径的远程主机，或 scp://\[user@\]host\[:port\]\[/path\] 。 本地文件名可以使用绝对或相对路径名明确，以避免 `scp` 将包含 ‘:’ 的文件名视为主机说明符。

在两个远程主机之间复制时，如果使用 URI 格式，则只有在使用 `-3` 选项时才能在 target 上指定 port 。

选项如下：

[`-3`](#3)

两个远程主机之间的副本通过本地主机传输。 如果没有此选项，数据将直接在两个远程主机之间复制。 请注意，此选项会禁用进度表。

[`-4`](#4)

强制 `scp` 仅使用 IPv4 地址。

[`-6`](#6)

强制 `scp` 仅使用 IPv6 地址。

[`-B`](#B)

选择批处理模式（防止要求输入密码或密码）。

[`-C`](#C)

压缩启用。 将 `-C` 标志传递给 ssh(1) 以启用压缩。

[`-c`](#c) cipher

选择用于加密数据传输的密码。 此选项直接传递给 ssh(1) 。

[`-F`](#F) ssh\_config

为 `ssh` 指定替代的每用户配置文件。 此选项直接传递给 ssh(1) 。

[`-i`](#i) identity\_file

选择从中读取用于公钥认证的身份（私钥）的文件。 此选项直接传递给 ssh(1) 。

[`-l`](#l) limit

限制使用的带宽，以 Kbit/s 为单位。

[`-o`](#o) ssh\_option

可用于以 ssh\_config(5) 中使用的格式将选项传递给 `ssh` 。 这对于指定没有单独的 `scp` 命令行标志的选项很有用。 有关下面列出的选项及其可能值的完整详细信息，请参阅 ssh\_config(5) 。

AddressFamily

BatchMode

BindAddress

BindInterface

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

Compression

ConnectionAttempts

ConnectTimeout

ControlMaster

ControlPath

ControlPersist

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

LogLevel

MACs

NoHostAuthenticationForLocalhost

NumberOfPasswordPrompts

PasswordAuthentication

PKCS11Provider

Port

PreferredAuthentications

ProxyCommand

ProxyJump

PubkeyAcceptedKeyTypes

PubkeyAuthentication

RekeyLimit

SendEnv

ServerAliveInterval

ServerAliveCountMax

SetEnv

StrictHostKeyChecking

TCPKeepAlive

UpdateHostKeys

User

UserKnownHostsFile

VerifyHostKeyDNS

[`-P`](#P) port

指定要连接到远程主机上的端口。 请注意，此选项以大写 ‘P’ 书写，因为 `-p` 已保留用于保存文件的时间和模式。

[`-p`](#p)

保留原始文件的修改时间、访问时间和模式。

[`-q`](#q)

安静模式：禁用进度表以及来自 ssh(1) 的警告和诊断消息。

[`-r`](#r)

递归复制整个目录。 请注意， `scp` 遵循在树遍历中遇到的符号链接。

[`-S`](#S) program

用于加密连接的 program 名称。 该程序必须了解 ssh(1) 选项。

[`-T`](#T)

禁用严格的文件名检查。 默认情况下，将文件从远程主机复制到本地目录时， `scp` 检查接收到的文件名是否与命令行上请求的文件名匹配，以防止远程端发送意外或不需要的文件。 由于各种操作系统和 shell 解释文件名通配符的方式不同，这些检查可能会导致想要的文件被拒绝。 此选项以完全信任服务器不会发送意外文件名为代价禁用这些检查。

[`-v`](#v)

详细模式。 使 `scp` 和 ssh(1) 打印有关其进度的调试消息。 这有助于调试连接、身份验证和配置问题。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `scp` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

sftp(1), ssh(1), ssh-add(1), ssh-agent(1), ssh-keygen(1), ssh\_config(5), sshd(8)

[历史](#__u5386___u53F2_)
=======================

`scp` 是基于加州大学 Regents 的 BSD 源代码中的 rcp 程序。

[作者](#__u4F5C___u8005_)
=======================

Timo Rinne <[tri@iki.fi](mailto:tri@iki.fi)\> Tatu Ylonen <[ylo@cs.hut.fi](mailto:ylo@cs.hut.fi)\>

September 20, 2018

FreeBSD 13.1-RELEASE