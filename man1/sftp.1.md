# sftp(1)

`sftp` — OpenSSH 安全文件传输

## 名称

`sftp`

## 概要

`sftp [-46AaCfNpqrv] [-B buffer_size] [-b batchfile] [-c cipher] [-D sftp_server_command] [-F ssh_config] [-i identity_file] [-J destination] [-l limit] [-o ssh_option] [-P port] [-R num_requests] [-S program] [-s subsystem | sftp_server] [-X sftp_option] destination`

## 描述

`sftp` 是一个文件传输程序，类似于 [ftp(1)](ftp.1.md)，通过加密的 [ssh(1)](ssh.1.md) 传输执行所有操作。它也可以使用 ssh 的许多功能，如公钥认证和压缩。

`destination` 可以指定为 `[user@]host[:path]` 或形式为 `sftp://[user@]host[:port][/path]` 的 URI。

如果 `destination` 包含 `path` 且不是目录，使用非交互式认证方法时 `sftp` 会自动获取文件；否则会在成功完成交互式认证后执行。

如果未指定 `path`，或 `path` 是目录，`sftp` 会登录到指定的 `host` 并进入交互式命令模式，如果指定了远程目录则切换到该目录。可使用可选的尾部斜杠强制将 `path` 解释为目录。

由于目标格式使用冒号字符分隔主机名和路径名或端口号，IPv6 地址必须用方括号括起以避免歧义。

选项如下：

**`-4`** 强制 `sftp` 仅使用 IPv4 地址。

**`-6`** 强制 `sftp` 仅使用 IPv6 地址。

**`-A`** 允许将 ssh-agent(1) 转发到远程系统。默认不转发认证代理。

**`-a`** 尝试继续中断的传输，而非覆盖现有的部分或完整文件副本。如果部分内容与正在传输的内容不同，则生成的文件可能已损坏。

**`-B`** `buffer_size` 指定 `sftp` 传输文件时使用的缓冲区大小。较大的缓冲区需要更少的往返次数，但内存消耗更高。默认为 32768 字节。

**`-b`** `batchfile` 批处理模式从输入 `batchfile` 而非 *stdin* 读取一系列命令。由于缺少用户交互，应与非交互式认证结合使用，以避免在连接时输入密码（详见 sshd(8) 和 [ssh-keygen(1)](ssh-keygen.1.md)）。`batchfile` 为“-”时可用于表示标准输入。如果以下任何命令失败，`sftp` 将中止：`get`、`put`、`reget`、`reput`、`rename`、`ln`、`rm`、`mkdir`、`chdir`、`ls`、`lchdir`、`copy`、`cp`、`chmod`、`chown`、`chgrp`、`lpwd`、`df`、`symlink` 和 `lmkdir`。可通过在命令前加“-”字符来逐命令抑制出错时终止（例如 ``-rm /tmp/blah*``）。可通过在命令前加“@”字符来抑制命令回显。这两个前缀可以任意顺序组合，例如 ``-@ls /bsd``。

**`-C`** 启用压缩（通过 ssh 的 `-C` 标志）。

**`-c`** `cipher` 选择用于加密数据传输的密码。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-D`** `sftp_server_command` 直接连接到本地 sftp 服务器（而非通过 [ssh(1)](ssh.1.md)）。可指定命令和参数，例如 `/path/sftp-server -el debug3`。此选项在调试客户端和服务器时可能有用。

**`-F`** `ssh_config` 为 [ssh(1)](ssh.1.md) 指定替代的每用户配置文件。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-f`** 请求文件在传输后立即刷新到磁盘。上传文件时，仅在服务器实现 "fsync@openssh.com" 扩展时才启用此功能。

**`-i`** `identity_file` 选择从中读取公钥认证身份（私钥）的文件。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-J`** `destination` 首先建立到 `destination` 所描述跳转主机的 `sftp` 连接，然后从那里建立到最终目标的 TCP 转发，从而连接到目标主机。可以通过逗号分隔指定多个跳转跳。这是指定 `ProxyJump` 配置指令的快捷方式。此选项直接传递给 [ssh(1)](ssh.1.md)。

**`-l`** `limit` 限制使用的带宽，以 Kbit/s 为单位指定。

**`-N`** 禁用静默模式，例如覆盖 `-b` 标志隐式设置的静默模式。

**`-o`** `ssh_option` 可用于以 ssh_config(5) 中使用的格式向 `ssh` 传递选项。这对于指定没有单独 `sftp` 命令行标志的选项很有用。例如，要指定备用端口：`sftp -oPort=24`。有关下列选项及其可能值的完整详情，参见 ssh_config(5)。

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

**`-P`** `port` 指定要连接的远程主机上的端口。

**`-p`** 保留所传输原始文件的修改时间、访问时间和模式。

**`-q`** 静默模式：禁用进度指示器以及来自 [ssh(1)](ssh.1.md) 的警告和诊断消息。

**`-R`** `num_requests` 指定任何时刻可能未完成的请求数。增大此值可能略微提高文件传输速度，但会增加内存使用量。默认为 64 个未完成请求。

**`-r`** 上传和下载时递归复制整个目录。注意，`sftp` 不跟随目录树遍历中遇到的符号链接。

**`-S`** `program` 用于加密连接的 `program` 名称。该程序必须理解 [ssh(1)](ssh.1.md) 选项。

**`-s`** `subsystem | sftp_server` 指定远程主机上的 SSH2 子系统或 sftp 服务器的路径。当远程 sshd(8) 未配置 sftp 子系统时，路径很有用。

**`-v`** 提高日志记录级别。此选项也传递给 ssh。

**`-X`** `sftp_option` 指定控制 SFTP 协议行为某些方面的选项。有效选项为：

**`nrequests`**=`value` 控制下载或上传期间任何时刻可能同时进行的 SFTP 读或写请求数量。默认最多 64 个请求可同时活动。

**`buffer`**=`value` 控制下载或上传期间单次 SFTP 读/写操作使用的最大缓冲区大小。默认使用 32KB 缓冲区。

## 交互式命令

进入交互模式后，`sftp` 理解一组类似于 [ftp(1)](ftp.1.md) 的命令。命令不区分大小写。包含空格的路径名必须用引号括起。路径名中包含的被 glob(3) 识别的任何特殊字符必须用反斜杠（“**\**”）转义。

**`bye`** 退出 `sftp`。

**`cd`** [`path`] 将远程目录切换到 `path`。如果未指定 `path`，则切换到会话开始时所在的目录。

**`chgrp`** [`-h`] `grp` `path` 将文件 `path` 的组更改为 `grp`。`path` 可包含 glob(7) 字符并可匹配多个文件。`grp` 必须是数字 GID。如果指定了 `-h` 标志，则不跟随符号链接。注意，这仅由实现 "lsetstat@openssh.com" 扩展的服务器支持。

**`chmod`** [`-h`] `mode` `path` 将文件 `path` 的权限更改为 `mode`。`path` 可包含 glob(7) 字符并可匹配多个文件。如果指定了 `-h` 标志，则不跟随符号链接。注意，这仅由实现 "lsetstat@openssh.com" 扩展的服务器支持。

**`chown`** [`-h`] `own` `path` 将文件 `path` 的属主更改为 `own`。`path` 可包含 glob(7) 字符并可匹配多个文件。`own` 必须是数字 UID。如果指定了 `-h` 标志，则不跟随符号链接。注意，这仅由实现 "lsetstat@openssh.com" 扩展的服务器支持。

**`copy`** `oldpath` `newpath` 将远程文件从 `oldpath` 复制到 `newpath`。注意，这仅由实现 "copy-data" 扩展的服务器支持。

**`cp`** `oldpath` `newpath` `copy` 命令的别名。

**`df`** [`-hi`] [`path`] 显示保存当前目录（或指定的 `path`）的文件系统的使用信息。如果指定了 `-h` 标志，容量信息将以“人类可读”的后缀显示。`-i` 标志请求除了容量信息外还显示 inode 信息。此命令仅由实现 “statvfs@openssh.com” 扩展的服务器支持。

**`exit`** 退出 `sftp`。

**`get`** [`-afpR`] `remote-path` [`local-path`] 获取 `remote-path` 并将其存储在本地机器上。如果未指定本地路径名，则赋予它与远程机器上相同的名称。`remote-path` 可包含 glob(7) 字符并可匹配多个文件。如果匹配多个文件且指定了 `local-path`，则 `local-path` 必须指定一个目录。如果指定了 `-a` 标志，则尝试恢复现有文件的部分传输。注意，恢复传输时假定本地文件的任何部分副本与远程副本匹配。如果远程文件内容与本地部分副本不同，则生成的文件可能已损坏。如果指定了 `-f` 标志，则在文件传输完成后调用 fsync(2) 将文件刷新到磁盘。如果指定了 `-p` 标志，则还会复制完整的文件权限和访问时间。如果指定了 `-R` 标志，则递归复制目录。注意，`sftp` 在执行递归传输时不跟随符号链接。

**`help`** 显示帮助文本。

**`lcd`** [`path`] 将本地目录切换到 `path`。如果未指定 `path`，则切换到本地用户的主目录。

**`lls`** [`ls-options` [`path`]] 显示 `path` 或当前目录（如果未指定 `path`）的本地目录列表。`ls-options` 可包含本地系统 [ls(1)](ls.1.md) 命令支持的任何标志。`path` 可包含 glob(7) 字符并可匹配多个文件。

**`lmkdir`** `path` 创建由 `path` 指定的本地目录。

**`ln`** [`-s`] `oldpath` `newpath` 创建从 `oldpath` 到 `newpath` 的链接。如果指定了 `-s` 标志，创建的链接为符号链接，否则为硬链接。

**`lpwd`** 打印本地工作目录。

**`ls`** [`-1afhlnrSt`] [`path`] 显示 `path` 或当前目录（如果未指定 `path`）的远程目录列表。`path` 可包含 glob(7) 字符并可匹配多个文件。以下标志被识别并相应地改变 `ls` 的行为：

**`-1`** 生成单列输出。

**`-a`** 列出以点（“.”）开头的文件。

**`-f`** 不对列表排序。默认排序顺序为字典序。

**`-h`** 与长格式选项一起使用时，使用单位后缀：Byte、Kilobyte、Megabyte、Gigabyte、Terabyte、Petabyte 和 Exabyte，以便用 2 的幂次将数字位数减少到四位或更少（K=1024，M=1048576 等）。

**`-l`** 显示包括权限和属主信息在内的附加详情。

**`-n`** 生成以数字形式呈现用户和组信息的长列表。

**`-r`** 反转列表的排序顺序。

**`-S`** 按文件大小对列表排序。

**`-t`** 按最后修改时间对列表排序。

**`lumask`** `umask` 将本地 umask 设置为 `umask`。

**`mkdir`** `path` 创建由 `path` 指定的远程目录。

**`progress`** 切换进度指示器的显示。

**`put`** [`-afpR`] `local-path` [`remote-path`] 上传 `local-path` 并将其存储在远程机器上。如果未指定远程路径名，则赋予它与本地机器上相同的名称。`local-path` 可包含 glob(7) 字符并可匹配多个文件。如果匹配多个文件且指定了 `remote-path`，则 `remote-path` 必须指定一个目录。如果指定了 `-a` 标志，则尝试恢复现有文件的部分传输。注意，恢复传输时假定远程文件的任何部分副本与本地副本匹配。如果本地文件内容与远程本地副本不同，则生成的文件可能已损坏。如果指定了 `-f` 标志，则向服务器发送请求，在文件传输完成后调用 fsync(2)。注意，这仅由实现 "fsync@openssh.com" 扩展的服务器支持。如果指定了 `-p` 标志，则还会复制完整的文件权限和访问时间。如果指定了 `-R` 标志，则递归复制目录。注意，`sftp` 在执行递归传输时不跟随符号链接。

**`pwd`** 显示远程工作目录。

**`quit`** 退出 `sftp`。

**`reget`** [`-fpR`] `remote-path` [`local-path`] 恢复下载 `remote-path`。等同于设置了 `-a` 标志的 `get`。

**`reput`** [`-fpR`] `local-path` [`remote-path`] 恢复上传 `local-path`。等同于设置了 `-a` 标志的 `put`。

**`rename`** `oldpath newpath` 将远程文件从 `oldpath` 重命名为 `newpath`。

**`rm`** `path` 删除由 `path` 指定的远程文件。

**`rmdir`** `path` 删除由 `path` 指定的远程目录。

**`symlink`** `oldpath newpath` 创建从 `oldpath` 到 `newpath` 的符号链接。

**`version`** 显示 `sftp` 协议版本。

**`!`** `command` 在本地 shell 中执行 `command`。

**`!`** 转义到本地 shell。

**`?`** help 的同义词。

## 参见

[ftp(1)](ftp.1.md), [ls(1)](ls.1.md), [scp(1)](scp.1.md), [ssh(1)](ssh.1.md), ssh-add(1), [ssh-keygen(1)](ssh-keygen.1.md), ssh_config(5), glob(7), sftp-server(8), sshd(8)

> T. Ylonen, S. Lehtinen, "SSH File Transfer Protocol", draft-ietf-secsh-filexfer-00.txt, January 2001, work in progress material.
