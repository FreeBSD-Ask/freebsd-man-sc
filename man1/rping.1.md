  RPING(1)  

RPING(1)

librdmacm

RPING(1)

[名称](#__u540D___u79F0_)
=======================

rping - RDMA CM 连接和 RDMA 双向测试。

[概要](#__u6982___u8981_)
=======================

_rping_ -s \[-v\] \[-V\] \[-d\] \[-P\] \[-a address\] \[-p port\] \[-C message\_count\] \[-S message\_size\] _rping_ -c \[-v\] \[-V\] \[-d\] \[-I address\] -a address \[-p port\] \[-C message\_count\] \[-S message\_size\] 

[描述](#__u63CF___u8FF0_)
=======================

使用 librdmacm 在两个节点之间建立可靠的 RDMA 连接，可选择在节点之间执行 RDMA 传输，然后断开连接。

[选项](#__u9009___u9879_)
=======================

\-s

作为服务器运行。

\-c

作为客户端运行。

\-a address

在服务器上，指定要将连接绑定到的网络地址。要使用 IPv6 绑定到任何地址，请使用 -a ::0 。在客户端上，指定要连接的服务器地址。

\-I address

要绑定到的地址作为要使用的源 IP 地址。如果您在同一网络或复杂路由上有多个地址，这将很有用。

\-p

监听服务器的端口号。

\-v

显示 ping 数据。

\-V

验证 ping 数据。

\-d

显示调试信息。

\-C message\_count

通过每个连接传输的消息数。（默认无限）

\-S message\_size

传输的每条消息的大小，以字节为单位。（默认 100）

\-P

以持久模式运行服务器。这允许多个 rping 客户端连接到单个服务器实例。服务器将一直运行直到被杀死。

[NOTES](#NOTES)
===============

由于此测试将 RDMA 资源映射到用户空间，因此用户必须确保他们拥有可用的系统资源和权限。有关更多详细信息，请参阅 libibverbs README 文件。

[参见](#__u53C2___u89C1_)
=======================

rdma\_cm(7), ucmatose(1), udaddy(1), mckey(1)

2007-05-15

librdmacm