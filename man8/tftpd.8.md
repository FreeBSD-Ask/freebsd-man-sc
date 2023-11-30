  TFTPD(8)  

TFTPD(8)

FreeBSD System Manager's Manual

TFTPD(8)

[名称](#__u540D___u79F0_)
=======================

`tftpd` —

Internet 普通文件传输协议服务器

[概要](#__u6982___u8981_)
=======================

`tftpd` \[`-cdClnow`\] \[`-F` strftime-format\] \[`-s` directory\] \[`-u` user\] \[`-U` umask\] \[directory ...\]

[描述](#__u63CF___u8FF0_)
=======================

`tftpd` 实用程序是支持 Internet 普通文件传输协议 (RFC 1350) 的服务器。 TFTP 服务器在 ‘`tftp`’ 服务描述中指明的端口上运行；见 services(5) 。 服务器通常由 inetd(8) 启动。

tftp(1) 的使用不需要远程系统上的帐户或密码。 由于缺少身份验证信息， `tftpd` 将只允许访问公开可读的文件。 不允许包含字符串 “`/../`” 或以 “`../`” 开头的文件。 只有当文件已经存在并且可以公开写入时，才可以写入文件。 请注意，这将 “public” 的概念扩展为包括可以通过网络访问的所有主机上的所有用户；这可能不适用于所有系统，在启用 tftp 服务之前应考虑其影响。 服务器应具有具有最低权限的用户 ID。

可以通过在 inetd.conf(5) 中包含多达 20 个路径名作为服务器程序参数来使用目录列表调用 `tftpd` 来限制对文件的访问。 在这种情况下，访问仅限于名称以给定目录之一为前缀的文件。 给定的目录也被视为相对文件名请求的搜索路径。

`-s` 选项通过更改 `tftpd` 的根目录来提供额外的安全性，从而禁止对指定 directory 之外的访问。 因为 chroot(2) 需要超级用户权限，所以 `tftpd` 必须以 `root` 身份运行。 但是，在执行 chroot(2) 调用后， `tftpd` 会将其用户 ID 设置为指定 user 的用户 ID，如果未指定 `-u` 选项，则设置为 “`nobody`” 。

选项包括：

[`-c`](#c)

根据连接 IP 地址，通过 chroot(2) 更改连接主机的默认根目录。 这可以防止多个客户端同时写入同一个文件。 如果目录不存在，则拒绝客户端连接。 `-s` 需要 `-c` 选项，并且指定的 directory 用作基础。

[`-C`](#C)

操作与 `-c` 相同，但如果客户端 IP 的目录不存在，它会回退到通过 `-s` 指定的 directory 。

[`-F`](#F)

如果指定了 strftime(3) ，则使用此 `-W` 兼容格式字符串来创建后缀。 默认情况下使用字符串 "%Y%m%d" 。

[`-d,`](#d,) `-d` \[value\]

启用调试输出。 如果未指定 value ，则每个指定的 `-d` 实例将调试级别增加一。

如果指定了 value ，则将调试级别设置为 value 。 调试级别是在 src/libexec/tftpd/tftp-utils.h 中实现的位掩码。 有效值为 0 (DEBUG\_NONE), 1 (DEBUG\_PACKETS), 2, (DEBUG\_SIMPLE), 4 (DEBUG\_OPTIONS) 和 8 (DEBUG\_ACCESS) 。 通过对值进行逻辑或运算，可以在位掩码中组合多个调试值。 例如，指定 `-d` 15 将启用所有调试值。

[`-l`](#l)

使用带有 `LOG_FTP` 功能的 syslog(3) 记录所有请求。 **注意**: 还必须在 syslog 配置文件 syslog.conf(5) 中启用日志记录 `LOG_FTP` 消息。

[`-n`](#n)

抑制对不存在的相对文件名的请求的否定确认。

[`-o`](#o)

禁用对 RFC2347 样式 TFTP 选项的支持。

[`-s`](#s) directory

导致 `tftpd` 将其根目录更改为 directory 。 完成此操作后但在接受命令之前， `tftpd` 会将凭据切换到非特权用户。

[`-u`](#u) user

使用 `-s` 选项时，将凭据切换到 user (默认为 “`nobody`”) 。 用户必须按名称指定，而不是数字 UID。

[`-U`](#U) umask

为新创建的文件设置 umask 。 默认值为 (`S_IWGRP` | `S_IWOTH`) 。

[`-w`](#w)

允许写入请求以创建新文件。 默认情况下， `tftpd` 要求写入请求中指定的文件存在。 请注意，这仅适用于使用 `-u` 选项指定的用户可写的目录

[`-W`](#W)

与 `-w` 一样，但将 YYYYMMDD.nn 序列号附加到文件名的末尾。 请注意，字符串 YYYYMMDD 可以使用 `-F` 选项进行更改。

[参见](#__u53C2___u89C1_)
=======================

tftp(1), chroot(2), syslog(3), inetd.conf(5), services(5), syslog.conf(5), inetd(8)

支持以下 RFC： RFC 1350: The TFTP Protocol (Revision 2). RFC 2347: TFTP Option Extension. RFC 2348: TFTP Blocksize Option. RFC 2349: TFTP Timeout Interval and Transfer Size Options. RFC 7440: TFTP Windowsize Option.

这里提到了非标准 `rollover` 和 `blksize2` TFTP 选项： Extending TFTP, [http://www.compuphase.com/tftp.htm](http://www.compuphase.com/tftp.htm).

[历史](#__u5386___u53F2_)
=======================

`tftpd` 实用程序出现在 4.2BSD 中； `-s` 选项是在 FreeBSD 2.2 中引入的， `-u` 选项是在 FreeBSD 4.2 中引入的， `-c` 选项是在 FreeBSD 4.3 中引入的， `-F` 和 `-W` 选项是在 FreeBSD 7.4 中引入的。

在 FreeBSD 5.0 中引入了对超时间隔和传输大小选项 (RFC2349) 的支持，在 FreeBSD 7.4 中引入了对 TFTP 块大小选项 (RFC2348) 和 blksize2 选项的支持。

Edwin Groothuis <edwin@FreeBSD.org> 对 `tftpd` 和 tftp(1) 代码进行了重大重写以支持 RFC2348。

FreeBSD 13.0 中引入了对 windowssize 选项 (RFC7440) 的支持。

[笔记](#__u7B14___u8BB0_)
=======================

如果没有客户端和服务器支持块大小协商（RFC 2347 和 2348）或非标准 TFTP 翻转选项，则无法正确传输大于 33,553,919 字节（65535 块，最后一个 <512 字节）的文件。 作为一个组合，即使未指定翻转选项， `tftpd` 也接受在 65535 之后归零的块号序列。

许多 tftp 客户端不会传输超过 16,776,703 个八位字节（32767 个块）的文件，因为它们错误地使用带符号而不是无符号 16 位整数计算块号。

March 2, 2020

FreeBSD 13.1-RELEASE