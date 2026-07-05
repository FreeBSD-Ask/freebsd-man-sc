# ng_mppc.4

`ng_mppc` — Microsoft MPPC/MPPE 压缩和加密 netgraph 节点类型

## 名称

`ng_mppc`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_mppc.h>`

## 描述

`mppc` 节点类型实现 PPP 协议的 Microsoft 点对点压缩（MPPC）和 Microsoft 点对点加密（MPPE）子协议。这些协议通常与点对点隧道协议（PPTP）一起使用。

该节点有两个钩子，`comp` 用于压缩，`decomp` 用于解压缩。通常其中一个或两个钩子会连接到 [ng_ppp(4)](ng_ppp.4.md) 节点类型的同名钩子。每个方向的流量相互独立。

## 钩子

本节点类型支持以下钩子：

**`comp`** 连接到 [ng_ppp(4)](ng_ppp.4.md) 的 `comp` 钩子。传入的帧会被压缩和/或加密，并从同一钩子发回。

**`decomp`** 连接到 [ng_ppp(4)](ng_ppp.4.md) 的 `decomp` 钩子。传入的帧会被解压缩和/或解密，并从同一钩子发回。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

```sh
/* MPPE 密钥长度 */
#define MPPE_KEY_LEN      16
/* MPPC/MPPE PPP 协商位 */
#define MPPC_BIT          0x00000001      /* mppc 压缩位 */
#define MPPE_40           0x00000020      /* 使用 40 位密钥 */
#define MPPE_56           0x00000080      /* 使用 56 位密钥 */
#define MPPE_128          0x00000040      /* 使用 128 位密钥 */
#define MPPE_BITS         0x000000e0      /* mppe 加密位 */
#define MPPE_STATELESS    0x01000000      /* 使用无状态模式 */
#define MPPC_VALID_BITS   0x010000e1      /* 可能的有效位 */
/* 会话配置 */
struct ng_mppc_config {
    u_char    enable;                 /* 启用 */
    uint32_t  bits;                   /* 配置位 */
    u_char    startkey[MPPE_KEY_LEN]; /* 起始密钥 */
};
```

**`NGM_MPPC_CONFIG_COMP`** 此命令重置并为传出流量方向（即压缩和/或加密）的会话配置节点。此命令接受 `struct ng_mppc_config` 作为参数：`enabled` 字段启用通过节点的流量。`bits` 字段包含 PPP 中由压缩控制协议（CCP）协商的位。`startkey` 仅在协商了 MPPE 时需要，且必须等于为 MPPE 定义的会话起始密钥。此密钥基于链路身份验证时使用的 MS-CHAP 凭据。

**`NGM_MPPC_CONFIG_DECOMP`** 此命令重置并为传入流量方向（即解压缩和/或解密）的会话配置节点。此命令接受 `struct ng_mppc_config` 作为参数。

**`NGM_MPPC_RESETREQ`** 此消息不包含任何参数，且是双向的。如果在解压缩期间检测到错误，此消息由节点发送给发起该会话的 `NGM_MPPC_CONFIG_DECOMP` 消息的发起者。接收方应通过向对端发送 PPP CCP Reset-Request 来响应。当本地 PPP 实体收到 CCP Reset-Request 时，此节点类型也可能收到此消息。节点会通过刷新其传出压缩和加密状态来响应，以便远程方可以重新同步。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在两个钩子都已断开时关闭。

## 编译

内核选项 `NETGRAPH_MPPC_COMPRESSION` 和 `NETGRAPH_MPPC_ENCRYPTION` 用于选择性地编译其中一种或两种功能。必须至少定义其中一个，否则此节点类型无用。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ppp(4)](ng_ppp.4.md), ngctl(8)

> G. Pall, "Microsoft Point-To-Point Compression (MPPC) Protocol", RFC 2118.

> G. S. Pall, G. Zorn, "Microsoft Point-To-Point Encryption (MPPE) Protocol", draft-ietf-pppext-mppe-04.txt.

> K. Hamzeh, G. Pall, W. Verthein, J. Taarud, W. Little, G. Zorn, "Point-to-Point Tunneling Protocol (PPTP)", RFC 2637.

## 作者

Archie Cobbs <archie@FreeBSD.org>

## 缺陷

在 PPP 中，加密应由加密控制协议（ECP）而非 CCP 处理。但 Microsoft 将压缩和加密都合并到其“压缩”算法中，这容易引起混淆。
