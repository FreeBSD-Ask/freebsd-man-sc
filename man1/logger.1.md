  LOGGER(1)  

LOGGER(1)

FreeBSD General Commands Manual

LOGGER(1)

[名称](#__u540D___u79F0_)
=======================

`logger` —

在系统日志中创建条目

[概要](#__u6982___u8981_)
=======================

`logger` \[`-46Ais`\] \[`-f` file\] \[`-H` hostname\] \[`-h` host\] \[`-P` port\] \[`-p` pri\] \[`-S` addr:port\] \[`-t` tag\] \[message ...\]

[描述](#__u63CF___u8FF0_)
=======================

`logger` 实用程序为 syslog(3) 系统日志模块提供了一个 shell 命令接口。

可以使用以下选项：

[`-4`](#4)

强制 `logger` 仅使用 IPv4 地址。

[`-6`](#6)

强制 `logger` 仅使用 IPv6 地址。

[`-A`](#A)

默认情况下，即使主机有多个 A 或 AAAA 记录， `logger` 也会尝试仅将消息发送到一个地址。 如果指定了此选项，则 `logger` 会尝试将消息发送到所有地址。

[`-i`](#i)

用每一行记录 logger 进程的进程 ID。

[`-s`](#s)

将消息记录到标准错误以及系统日志。

[`-f`](#f) file

将指定文件的内容读入 syslog。 如果还指定了消息，则忽略此选项。

[`-H`](#H) hostname

将消息头中的主机名设置为指定值。 如果未指定，将使用 gethostname(3) 的主机部分。

[`-h`](#h) host

将消息发送到远程系统 host ，而不是在本地记录它。 请注意， `logger` 当前支持 `AF_INET` (IPv4), `AF_INET6` (IPv6) 和 `AF_LOCAL` (Unix-domain 套接字) 地址系列。 以下地址格式在 host 中有效：

[`AF_INET`](#AF_INET)

192.168.2.1

[`AF_INET6`](#AF_INET6)

2001:db8::1

[`AF_LOCAL`](#AF_LOCAL)

/var/run/log

[`-P`](#P) port

将消息发送到远程系统上的指定 port 号，可以指定为服务名称或十进制数。 默认为 “`syslog`” 。 如果使用了未知的服务名称，则 `logger` 会打印警告并回退到端口 514。

[`-p`](#p) pri

输入具有指定优先级的消息。 优先级可以用数字或 `facility.level` 对指定。 例如， “`-p` `local3.info`” 将消息记录为 local3 工具中的 informational 。 默认为 “`user.notice`” 。

[`-S`](#S) addr:port

使用 `-h` 选项时指定源地址和/或源端口。 当启用 `-A` 标志时，所有远程地址都将使用相同的地址。 请注意， addr 中的数字 IPv6 地址必须用 “\[” 和 “\]” 括起来。

[`-t`](#t) tag

用指定的 tag 而不是当前登录名的默认值标记日志中的每一行。

message

将消息写入日志；如果未指定且未提供 `-f` 标志，则记录标准输入。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `logger` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

logger 系统重新启动 logger -p local0.notice -t HOSTIDM -f /dev/idmc 

[参见](#__u53C2___u89C1_)
=======================

syslog(3), syslogd(8)

[标准](#__u6807___u51C6_)
=======================

`logger` 命令预计与 IEEE Std 1003.2 (“POSIX.2”) 兼容。

December 5, 2017

FreeBSD 13.1-RELEASE