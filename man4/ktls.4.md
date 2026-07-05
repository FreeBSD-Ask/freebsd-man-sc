# ktls.4

`ktls` — 内核传输层安全

## 名称

`ktls`

## 概要

`options KERN_TLS`

## 描述

`ktls` 设施允许内核对 TCP 套接字执行传输层安全（TLS）成帧。使用 `ktls` 时，使用 TLS 的套接字的初始握手在用户态执行。会话密钥协商后，通过 `TCP_TXTLS_ENABLE` 和 `TCP_RXTLS_ENABLE` 套接字选项提供给内核。两个套接字选项都接受 `struct tls_enable` 结构作为参数。此结构的成员描述用于 TLS 会话的密码套件并提供用于相应方向的会话密钥。

`ktls` 仅允许在每个方向设置一次会话密钥。因此，应用程序在使用 `ktls` 时必须禁用密钥更新。

### 模式

`ktls` 可在不同模式下运行。给定套接字可在发送和接收方向使用不同模式，或者套接字可能仅卸载单个方向。可用模式为：

**`TCP_TLS_MODE_NONE`** 未启用 `ktls`。

**`TCP_TLS_MODE_SW`** TLS 记录在套接字层中通过 crypto(9) 在内核中加密或解密。通常加密或解密在软件中执行，但也可由协处理器执行。

**`TCP_TLS_MODE_IFNET`** TLS 记录由网络接口卡（NIC）加密或解密。在此模式下，网络栈不处理加密数据。相反，NIC 在传输时加密 TLS 记录，或在接收到的 TLS 记录提供给主机之前解密。支持此功能的网络接口将通过 [ifconfig(8)](../man8/ifconfig.8.md) 报告通告 `TXTLS4`（IPv4）和/或 `TXTLS6`（IPv6）功能。这些功能也可由 [ifconfig(8)](../man8/ifconfig.8.md) 控制。如果网络接口支持 TLS 卸载的速率限制（也称为数据包调节），接口将通告 `TXTLS_RTLMT` 功能。

**`TCP_TLS_MODE_TOE`** TLS 记录由 NIC 使用 TCP 卸载引擎（TOE）加密。这与 `TCP_TLS_MODE_IFNET` 类似，网络栈不处理加密数据。但是，此模式与 TOE 协同工作以处理 TCP 和 TLS 之间的交互。

### 发送

通过成功设置 `TCP_TXTLS_ENABLE` 套接字选项启用 TLS 发送后，写入套接字的所有数据都将存储在 TLS 记录中并加密。大多数数据在应用层 TLS 记录中传输，内核选择如何在 TLS 记录之间分区数据。可通过 sendmsg(2) 发送具有固定长度和记录类型的单个 TLS 记录，TLS 记录类型在 `TLS_SET_RECORD_TYPE` 控制消息中设置。此控制消息的有效负载是保存所需 TLS 记录类型的单个字节。这可用于发送应用数据以外的类型的 TLS 记录（例如握手消息），或发送具有特定内容的应用数据记录（例如空片段）。

套接字的当前 TLS 发送模式可通过 `TCP_TXTLS_MODE` 套接字选项查询。使用 TLS 发送卸载的套接字还可设置 `TCP_TXTLS_MODE` 套接字选项以在 `TCP_TLS_MODE_SW` 和 `TCP_TLS_MODE_IFNET` 之间切换。

### 接收

通过成功设置 `TCP_RXTLS_ENABLE` 套接字选项启用 TLS 接收后，从套接字读取的所有数据都将作为解密的 TLS 记录返回。每个接收到的 TLS 记录必须使用 recvmsg(2) 从套接字读取。每个接收到的 TLS 记录将包含 `TLS_GET_RECORD` 控制消息以及解密的有效负载。控制消息包含 `struct tls_get_record`，其中包括 TLS 记录头中的字段。如果接收到无效或损坏的 TLS 记录，recvmsg(2) 将失败并返回以下错误之一：

**[Er** EINVAL] TLS 记录头中的版本字段与用于启用内核内 TLS 的 `struct tls_enable` 结构所需的版本不匹配。

**[Er** EMSGSIZE] TLS 记录长度过小或过大。

**[Er** EMSGSIZE] 连接在发送截断的 TLS 记录后关闭。

**[Er** EBADMSG] TLS 记录未能匹配包含的认证标签。

套接字的当前 TLS 接收模式可通过 `TCP_RXTLS_MODE` 套接字选项查询。目前无法更改模式。

### Sysctl 节点

`ktls` 在 `kern.ipc.tls` 节点下使用多个 sysctl 节点。下面描述了其中几个：

**`kern.ipc.tls.enable`** 确定是否可创建新的内核 TLS 会话。

**`kern.ipc.tls.rx_enable`** 确定是否可创建新的内核 TLS 接收会话。

**`kern.ipc.tls.cbc_enable`** 确定是否可创建使用 AES-CBC 密码套件的新的内核 TLS 会话。

**`kern.ipc.tls.sw`** 包含使用 `TCP_TLS_MODE_SW` 的 TLS 会话统计信息的节点树。

**`kern.ipc.tls.ifnet`** 包含使用 `TCP_TLS_MODE_IFNET` 的 TLS 会话统计信息的节点树。

**`kern.ipc.tls.toe`** 包含使用 `TCP_TLS_MODE_TOE` 的 TLS 会话统计信息的节点树。

**`kern.ipc.tls.stats`** 包含各种内核 TLS 统计信息的节点树。

`kern.ipc.mb_use_ext_pgs` sysctl 控制内核是否可使用未映射的 mbuf。TLS 发送需要这些 mbuf。

### 受支持的硬件

[cxgbe(4)](cxgbe.4.md) 和 mlx5en(4) 驱动包括对 `TCP_TLS_MODE_IFNET` 模式的支持。

[cxgbe(4)](cxgbe.4.md) 驱动包括对 `TCP_TLS_MODE_TOE` 模式的支持。

### 受支持的库

OpenSSL 3.0 及更高版本包括对 `ktls` 的支持。`security/openssl*` 和 `security/gnutls` Ports 也可通过启用 `KTLS` 选项来构建以支持 `ktls`。基本系统中的 OpenSSL 在使用 `WITH_OPENSSL_KTLS` 构建时包括 KTLS 支持。

使用受支持库的应用程序通常无需任何更改即可与 `ktls` 一起工作，前提是它们使用标准接口如 SSL_read(3) 和 SSL_write(3)。使用 SSL_sendfile(3) 可获得额外性能。

## 实现说明

`ktls` 假定在执行软件加密和解密时存在物理内存的直接映射。因此，它仅在具有直接映射的架构上受支持。

## 参见

[cxgbe(4)](cxgbe.4.md), mlx5en(4), tcp(4), [src.conf(5)](../man5/src.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md), crypto(9)

## 历史

内核 TLS 最早出现于 FreeBSD 13.0。
