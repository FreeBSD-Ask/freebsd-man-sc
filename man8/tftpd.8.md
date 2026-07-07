# tftpd(8)

`tftpd` — Internet 简单文件传输协议服务器

## 名称

`tftpd`

## 概要

`tftpd [-bCcdlnoSw] [-F strftime-format] [-s directory] [-U umask] [-u user] [directory ...]`

## 描述

`tftpd` 工具是一个支持 Internet 简单文件传输协议（RFC 1350）的服务器。TFTP 服务器在 `tftp` 服务描述中指示的端口上运行；参见 [services(5)](../man5/services.5.md)。该服务器通常由 [inetd(8)](inetd.8.md) 启动。

使用 tftp(1) 不需要在远程系统上有账户或密码。由于缺乏认证信息，`tftpd` 只允许访问公开可读的文件。包含字符串“`/../`”或以“`../`”开头的文件不被允许。只有当文件已经存在（除非使用 `-w` 选项）且公开可写（除非已 chroot 并使用 `-S` 选项）时，才能写入文件。注意，这将“公开”的概念扩展到包括可通过网络到达的所有主机上的所有用户；这在所有系统上可能并不合适，启用 tftp 服务前应考虑其影响。服务器应具有最低可能权限的用户 ID。

通过在 inetd.conf(5) 中作为服务器程序参数包含最多 20 个路径名来调用 `tftpd` 并附带目录列表，可以限制对文件的访问。在这种情况下，访问仅限于名称以给定目录之一为前缀的文件。给定的目录也作为相对文件名请求的搜索路径。

`-s` 选项通过更改 `tftpd` 的根目录提供额外的安全性，从而禁止访问指定 `directory` 之外的内容。由于 chroot(2) 需要超级用户权限，`tftpd` 必须以 `root` 运行。但是，在执行 chroot(2) 调用后，`tftpd` 会将其用户 ID 设置为指定 `user` 的 ID，如果未指定 `-u` 选项，则为“`nobody`”。

选项如下：

**`-b`** 默认情况下，`tftpd` 期望其输入套接字上有可用的初始消息。如果没有数据可用，服务器立即退出。如果指定了 `-b`，`tftpd` 将阻塞等待初始消息。

**`-c`** 通过 chroot(2) 根据连接的 IP 地址更改连接主机的默认根目录。这可防止多个客户端同时写入同一文件。如果目录不存在，拒绝客户端连接。`-c` 需要 `-s` 选项，指定的 `directory` 用作基础。

**`-C`** 与 `-c` 操作相同，但如果客户端 IP 没有对应目录，则回退到通过 `-s` 指定的 `directory`。

**`-F`** 如果指定了 `-W`，使用此 strftime(3) 兼容的格式字符串创建后缀。默认使用字符串“%Y%m%d”。

**`-d`** `[value]` 启用调试输出。如果未指定 `value`，则每指定一次 `-d`，调试级别增加一。如果指定了 `value`，则调试级别设置为 `value`。调试级别是在 **src/libexec/tftpd/tftp-utils.h** 中实现的位掩码。有效值为 0（DEBUG_NONE）、1（DEBUG_PACKETS）、2（DEBUG_SIMPLE）、4（DEBUG_OPTIONS）和 8（DEBUG_ACCESS）。多个调试值可以通过对这些值进行逻辑或运算组合到位掩码中。例如，指定 `-d` `15` 将启用所有调试值。

**`-l`** 使用 syslog(3) 记录所有请求，设施为 `LOG_FTP`。**注意：**还必须在 syslog 配置文件 syslog.conf(5) 中启用 `LOG_FTP` 消息的记录。

**`-n`** 抑制对不存在相对文件名请求的否定确认。

**`-o`** 禁用对 RFC2347 风格 TFTP 选项的支持。

**`-s`** `directory` 使 `tftpd` 将其根目录更改为 `directory`。这样做之后但在接受命令之前，`tftpd` 将切换凭据为非特权用户。

**`-S`** 如果 `tftpd` 在 chroot 下运行，该选项允许根据通用文件权限进行写请求，跳过文件必须公开可写的要求。非 chroot 运行时忽略此选项。

**`-u`** `user` 使用 `-s` 选项时切换凭据为 `user`（默认为“`nobody`”）。用户必须按名称指定，而不是数字 UID。

**`-U`** `umask` 为新创建的文件设置 `umask`。默认为 022（`S_IWGRP | S_IWOTH`）。

**`-w`** 允许写请求创建新文件。默认情况下，`tftpd` 要求写请求中指定的文件存在。注意，这仅在由 `-u` 选项指定的用户可写的目录中有效。

**`-W`** 与 `-w` 相同，但在文件名末尾追加 YYYYMMDD.nn 序列号。注意，字符串 YYYYMMDD 可以用 `-F` 选项更改。

## 参见

tftp(1), chroot(2), syslog(3), inetd.conf(5), [services(5)](../man5/services.5.md), syslog.conf(5), [inetd(8)](inetd.8.md)

支持以下 RFC：

> "RFC 1350: The TFTP Protocol (Revision 2)".

> "RFC 2347: TFTP Option Extension".

> "RFC 2348: TFTP Blocksize Option".

> "RFC 2349: TFTP Timeout Interval and Transfer Size Options".

> "RFC 7440: TFTP Windowsize Option".

非标准的 `rollover` 和 `blksize2` TFTP 选项在此提及：

> "Extending TFTP".

## 历史

`tftpd` 工具出现于 4.2BSD；`-s` 选项引入于 FreeBSD 2.2，`-u` 选项引入于 FreeBSD 4.2，`-c` 选项引入于 FreeBSD 4.3，`-F` 和 `-W` 选项引入于 FreeBSD 7.4，`-S` 选项引入于 FreeBSD 13.3。

对超时间隔和传输大小选项（RFC2349）的支持引入于 FreeBSD 5.0，对 TFTP 块大小选项（RFC2348）和 blksize2 选项的支持引入于 FreeBSD 7.4。

Edwin Groothuis <edwin@FreeBSD.org> 对 `tftpd` 和 tftp(1) 代码进行了重大重写以支持 RFC2348。

对 windowsize 选项（RFC7440）的支持引入于 FreeBSD 13.0。

## 注释

如果没有客户端和服务器支持块大小协商（RFC 2347 和 2348）或非标准 TFTP rollover 选项，则无法正确传输大于 33,553,919 字节（65535 个块，最后一个 <512 字节）的文件。作为一种权宜之计，`tftpd` 接受在 65535 后回绕到零的块编号序列，即使未指定 rollover 选项。

许多 tftp 客户端不会传输超过 16,776,703 字节（32767 个块）的文件，因为它们错误地使用有符号而非无符号 16 位整数来计算块编号。
