  SFTP(1)  

SFTP(1)

FreeBSD General Commands Manual

SFTP(1)

[名称](#__u540D___u79F0_)
=======================

`sftp` —

安全文件传输程序

[概要](#__u6982___u8981_)
=======================

`sftp` \[`-46aCfpqrv`\] \[`-B` buffer\_size\] \[`-b` batchfile\] \[`-c` cipher\] \[`-D` sftp\_server\_path\] \[`-F` ssh\_config\] \[`-i` identity\_file\] \[`-l` limit\] \[`-o` ssh\_option\] \[`-P` port\] \[`-R` num\_requests\] \[`-S` program\] \[`-s` subsystem | sftp\_server\] destination

[描述](#__u63CF___u8FF0_)
=======================

`sftp` 是一个文件传输程序，类似于 ftp(1), 它通过加密的 ssh(1) 传输执行所有操作。 它还可能使用 ssh 的许多功能，例如公钥认证和压缩。

destination 可以指定为 \[user@\]host\[:path\] 或 sftp://\[user@\]host\[:port\]\[/path\] 形式的 URI。

如果 destination 包含 path 且不是目录，如果使用非交互式身份验证方法， `sftp` 将自动检索文件；否则它将在成功的交互式身份验证后这样做。

如果没有指定 path ，或者 path 是目录， `sftp` 将登录到指定的 host 并进入交互命令模式，如果指定了则切换到远程目录。 可选的尾部斜杠可用于强制将 path 解释为目录。

由于目标格式使用冒号字符将主机名与路径名或端口号分隔开来，因此 IPv6 地址必须用方括号括起来以避免歧义。

选项如下：

[`-4`](#4)

强制 `sftp` 仅使用 IPv4 地址。

[`-6`](#6)

强制 `sftp` 仅使用 IPv6 地址。

[`-a`](#a)

尝试继续中断传输，而不是覆盖现有的部分或完整文件副本。 如果部分内容与正在传输的内容不同，则生成的文件可能已损坏。

[`-B`](#B) buffer\_size

指定 `sftp` 在传输文件时使用的缓冲区大小。 更大的缓冲区需要更少的往返行程，但代价是更高的内存消耗。 默认值为 32768 字节。

[`-b`](#b) batchfile

批处理模式从输入 batchfile 而不是 _stdin_ 读取一系列命令。 由于它缺乏用户交互，因此应与非交互式身份验证结合使用，以避免在连接时输入密码（有关详细信息，请参阅 sshd(8) 和 ssh-keygen(1) )。 ‘-’ 的 batchfile 可用于指示标准输入。 如果以下任何命令失败， `sftp` 将中止： `get`, `put`, `reget`, `reput, rename`, `ln`, `rm`, `mkdir`, `chdir`, `ls`, `lchdir`, `chmod`, `chown`, `chgrp`, `lpwd`, `df`, `symlink`, 和 `lmkdir` 。 可以通过在命令前加上 ‘-’ 字符（例如， `-rm /tmp/blah*` ）来逐个命令地抑制错误终止。

[`-C`](#C)

启用压缩（通过 ssh 的 `-C` 标志）。

[`-c`](#c) cipher

选择用于加密数据传输的密码。 此选项直接传递给 ssh(1) 。

[`-D`](#D) sftp\_server\_path

直接连接到本地 sftp 服务器（而不是通过 ssh(1) ）。 此选项在调试客户端和服务器时可能很有用。

[`-F`](#F) ssh\_config

为 ssh(1) 指定替代的每用户配置文件。 此选项直接传递给 ssh(1) 。

[`-f`](#f)

请求文件在传输后立即刷新到磁盘。 上传文件时，仅当服务器实现 "fsync@openssh.com" 扩展时才启用此功能。

[`-i`](#i) identity\_file

选择从中读取用于公钥认证的身份（私钥）的文件。 此选项直接传递给 ssh(1) 。

[`-l`](#l) limit

限制使用的带宽，以 Kbit/s 为单位。

[`-o`](#o) ssh\_option

可用于以 ssh\_config(5) 中使用的格式将选项传递给 `ssh` 。 这对于指定没有单独的 `sftp` 命令行标志的选项很有用。 例如，要指定备用端口，请使用： `sftp -oPort=24` 。 有关下面列出的选项及其可能值的完整详细信息，请参阅 ssh\_config(5) 。

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

指定要连接到远程主机上的端口。

[`-p`](#p)

保留传输的原始文件的修改时间、访问时间和模式。

[`-q`](#q)

安静模式：禁用进度表以及来自 ssh(1) 的警告和诊断消息。

[`-R`](#R) num\_requests

指定任何时候可能有多少请求未完成。 增加此值可能会略微提高文件传输速度，但会增加内存使用量。 默认值为 64 个未完成的请求。

[`-r`](#r)

上传和下载时递归复制整个目录。 请注意， `sftp` 不遵循树遍历中遇到的符号链接。

[`-S`](#S) program

用于加密连接的 program 的名称。 该程序必须了解 ssh(1) 选项。

[`-s`](#s) subsystem | sftp\_server

指定远程主机上的 SSH2 子系统或 sftp 服务器的路径。 当远程 sshd(8) 没有配置 sftp 子系统时，路径很有用。

[`-v`](#v)

提高日志记录级别。 此选项也传递给 ssh。

[交互式命令](#__u4EA4___u4E92___u5F0F___u547D___u4EE4_)
==================================================

一旦进入交互模式， `sftp` 就会理解一组类似于 ftp(1) 的命令。 命令不区分大小写。 包含空格的路径名必须用引号引起来。 glob(3) 识别的路径名中包含的任何特殊字符都必须使用反斜杠 (‘\\’) 进行转义。

[`bye`](#bye)

退出 `sftp` 。

[`cd`](#cd) \[path\]

将远程目录更改为 path 。 如果未指定 path ，则将目录更改为会话开始的目录。

[`chgrp`](#chgrp) grp path

将文件 path 组更改为 grp 。 path 可能包含 glob(7) 字符并且可能匹配多个文件。 grp 必须是数字 GID。

[`chmod`](#chmod) mode path

将文件 path 的权限更改为 mode 。 path 可能包含 glob(7) 字符并且可能匹配多个文件。

[`chown`](#chown) own path

将文件 path 的所有者更改为 own 。 path 可能包含 glob(7) 字符并且可能匹配多个文件。 own 必须是数字 UID。

[`df`](#df) \[`-hi`\] \[path\]

显示保存当前目录（或 path ，如果指定）的文件系统的使用信息。 如果指定了 `-h` 标志，容量信息将使用 "human-readable" 后缀显示。 `-i` 标志请求显示除容量信息之外的 inode 信息。 此命令仅在实现 “statvfs@openssh.com” 扩展的服务器上受支持。

[`exit`](#exit)

退出 `sftp` 。

[`get`](#get) \[`-afPpr`\] remote-path \[local-path\]

检索 remote-path 并将其存储在本地计算机上。 如果未指定本地路径名，则为其赋予与远程计算机上相同的名称。 remote-path 可能包含 glob(7) 字符并且可能匹配多个文件。 如果是这样并且指定了 local-path ，则 local-path 必须指定一个目录。

如果指定了 `-a` 标志，则尝试恢复现有文件的部分传输。 请注意，恢复假定本地文件的任何部分副本与远程副本匹配。 如果远程文件内容与部分本地副本不同，则生成的文件可能已损坏。

如果指定了 `-f` 标志，则在文件传输完成后将调用 fsync(2) 以将文件刷新到磁盘。

如果指定了 `-P` 或 `-p` 标志，那么也会复制完整的文件权限和访问时间。

如果指定了 `-r` 标志，则目录将被递归复制。 请注意， `sftp` 在执行递归传输时不遵循符号链接。

[`help`](#help)

显示帮助文本。

[`lcd`](#lcd) \[path\]

将本地目录更改为 path 。 如果未指定 path ，则将目录更改为本地用户的主目录。

[`lls`](#lls) \[ls-options \[path\]\]

如果未指定 path ，则显示 path 或当前目录的本地目录列表。 ls-options 可以包含本地系统的 ls(1) 命令支持的任何标志。 path 可能包含 glob(7) 字符并且可能匹配多个文件。

[`lmkdir`](#lmkdir) path

创建 path 指定的本地目录。

[`ln`](#ln) \[`-s`\] oldpath newpath

创建从 oldpath 到 newpath 的链接。 如果指定了 `-s` 标志，则创建的链接是符号链接，否则是硬链接。

[`lpwd`](#lpwd)

打印本地工作目录。

[`ls`](#ls) \[`-1afhlnrSt`\] \[path\]

如果未指定 path ，则显示 path 或当前目录的远程目录列表。 path 可能包含 glob(7) 字符并且可能匹配多个文件。

以下标志被识别并相应地改变 `ls` 的行为：

[`-1`](#1)

产生单一的柱状输出。

[`-a`](#a_2)

列出以点 (‘.’) 开头的文件。

[`-f`](#f_2)

不要对列表进行排序。 默认排序顺序是字典顺序。

[`-h`](#h)

当与长格式选项一起使用时，请使用单位后缀：字节、千字节、兆字节、千兆字节、太字节、千兆字节和艾字节，以便使用 2 的幂来将位数减少到四位或更少（K=1024，M =1048576 等）。

[`-l`](#l_2)

显示其他详细信息，包括权限和所有权信息。

[`-n`](#n)

生成一个长列表，其中以数字形式显示用户和组信息。

[`-r`](#r_2)

颠倒列表的排序顺序。

[`-S`](#S_2)

按文件大小对列表进行排序。

[`-t`](#t)

按上次修改时间对列表进行排序。

[`lumask`](#lumask) umask

将本地 umask 设置为 umask 。

[`mkdir`](#mkdir) path

创建由 path 指定的远程目录。

[`progress`](#progress)

切换进度表的显示。

[`put`](#put) \[`-afPpr`\] local-path \[remote-path\]

上传 local-path 并将其存储在远程计算机上。 如果未指定远程路径名，则为其赋予与本地计算机上相同的名称。 local-path 可能包含 glob(7) 字符并且可能匹配多个文件。 如果是这样并且指定了 remote-path ，则 remote-path 必须指定一个目录。

如果指定了 `-a` 标志，则尝试恢复现有文件的部分传输。 请注意，恢复假定远程文件的任何部分副本与本地副本匹配。 如果本地文件内容与远程本地副本不同，则生成的文件可能已损坏。

如果指定了 `-f` 标志，则在文件传输后将向服务器发送请求以调用 fsync(2) 。 请注意，这仅由实现 "fsync@openssh.com" 扩展的服务器支持。

如果指定了 `-P` 或 `-p`-
标志，那么也会复制完整的文件权限和访问时间。

如果指定了 `-r` 标志，则目录将被递归复制。 请注意， `sftp` 在执行递归传输时不遵循符号链接。

[`pwd`](#pwd)

显示远程工作目录。

[`quit`](#quit)

退出 `sftp` 。

[`reget`](#reget) \[`-Ppr`\] remote-path \[local-path\]

继续下载 remote-path 。 等价于设置 `-a` 标志的 `get` 。

[`reput`](#reput) \[`-Ppr`\] \[local-path\] remote-path

继续上传 \[local-path\] 等价于设置 `-a` 标志的 `put` 。

[`rename`](#rename) oldpath newpath

将远程文件从 oldpath 重命名为 newpath 。

[`rm`](#rm) path

删除 path 指定的远程文件。

[`rmdir`](#rmdir) path

删除 path 指定的远程目录。

[`symlink`](#symlink) oldpath newpath

创建从 oldpath 到 newpath 的符号链接。

[`version`](#version)

显示 `sftp` 协议版本。

[`!`](#!)command

在本地 shell 中执行 command 。

[`!`](#!_2)

逃到本地 shell。

[`?`](#?)

帮助的同义词。

[参见](#__u53C2___u89C1_)
=======================

ftp(1), ls(1), scp(1), ssh(1), ssh-add(1), ssh-keygen(1), ssh\_config(5), glob(7), sftp-server(8), sshd(8) T. Ylonen and S. Lehtinen, SSH File Transfer Protocol, draft-ietf-secsh-filexfer-00.txt, January 2001, work in progress material.

September 20, 2018

FreeBSD 13.1-RELEASE