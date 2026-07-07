# ng_lmi(4)

`ng_lmi` — 帧中继 LMI 协议 netgraph 节点类型

## 名称

`ng_lmi`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_lmi.h>`

## 描述

`lmi` 节点类型执行帧中继 LMI 协议。它支持 ITU Annex A、ANSI Annex D 和 Group-of-four LMI 类型。还支持 LMI 类型的自动检测。

要启用特定 LMI 类型，将相应的钩子（`annexA`、`annexD` 或 `group4`）连接到 [ng_frame_relay(4)](ng_frame_relay.4.md) 节点的 DLCI 0 或 1023。通常，Annex A 和 Annex D 位于 DLCI 0，而 Group-of-four 位于 DLCI 1023。

要启用 LMI 类型自动检测，将 `auto0` 钩子连接到 DLCI 0，`auto1023` 钩子连接到 DLCI 1023。节点会尝试自动确定交换机上运行的 LMI 类型，并进入该模式。

任何给定时间只能有一个固定 LMI 类型或自动检测处于活动状态。

可以随时使用 `NGM_LMI_GET_STATUS` 控制消息查询 LMI 协议和每个 DLCI 通道的当前状态。此节点还支持 `NGM_TEXT_STATUS` 控制消息。

## 钩子

本节点类型支持以下钩子：

**`annexA`** ITU Annex A LMI 钩子。

**`annexD`** ANSI Annex D LMI 钩子。

**`group4`** Group-of-four LMI 钩子。

**`auto0`** DLCI 0 的自动检测钩子。

**`auto1023`** DLCI 1023 的自动检测钩子。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

```sh
#define NGM_LMI_STAT_ARYSIZE   (1024/8)
struct nglmistat {
  u_char  proto[12];	/* 活动 proto（与钩子名相同） */
  u_char  hook[12];	/* 活动钩子 */
  u_char  fixed;	/* 如果设置为固定 LMI 模式 */
  u_char  autod;	/* 如果当前正在自动检测 */
  u_char  seen[NGM_LMI_STAT_ARYSIZE];	/* 曾见过的 DLCI */
  u_char  up[NGM_LMI_STAT_ARYSIZE];	/* 当前处于 up 状态的 DLCI */
};
```

**`NGM_LMI_GET_STATUS`** 此命令以 `struct nglmistat` 形式返回状态信息：

**`NGM_TEXT_STATUS`** 此通用消息返回节点状态的可读版本。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_frame_relay(4)](ng_frame_relay.4.md), ngctl(8)

> "ANSI T1.617-1991 Annex D".

> "ITU-T Q.933 Digital Subscriber Signaling System No. 1 - Signaling Specification for Frame Mode Basic Call Control, Annex A".

## 历史

`lmi` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
