# rping.1

`rping` — RDMA CM 连接和 RDMA ping-pong 测试

## 名称

`rping`

## 概要

`rping -s [-v] [-V] [-d] [-P] [-a address] [-p port] [-C message_count] [-S message_size]`

`rping -c [-v] [-V] [-d] [-I address] -a address [-p port] [-C message_count] [-S message_size]`

## 描述

使用 librdmacm 在两个节点之间建立可靠的 RDMA 连接，可选地在节点之间执行 RDMA 传输，然后断开连接。

## 选项

**`-s`** 作为服务器运行。

**`-c`** 作为客户端运行。

**`-a`** `address` 在服务器上，指定绑定连接的网络地址。使用 IPv6 绑定到任意地址用 `-a ::0`。在客户端，指定要连接的服务器地址。

**`-I`** `address` 要绑定的地址，作为使用的源 IP 地址。如果在同一网络上有多个地址或复杂路由，这很有用。

**`-p`** 监听服务器的端口号。

**`-v`** 显示 ping 数据。

**`-V`** 验证 ping 数据。

**`-d`** 显示调试信息。

**`-C`** `message_count` 在每个连接上传输的消息数量。（默认无限）

**`-S`** `message_size` 每条传输消息的大小，以字节为单位。（默认 100）

**`-P`** 以持久模式运行服务器。这允许多个 `rping` 客户端连接到单个服务器实例。服务器将运行直到被杀死。

## 注意事项

由于此测试将 RDMA 资源映射到用户空间，用户必须确保拥有可用的系统资源和权限。详见 libibverbs README 文件。

## 参见

rdma_cm(7), ucmatose(1), udaddy(1), mckey(1)
