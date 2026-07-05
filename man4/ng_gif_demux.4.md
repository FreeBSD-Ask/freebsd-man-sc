# ng_gif_demux.4

`ng_gif_demux` — 用于来自 [ng_gif(4)](ng_gif.4.md) 节点数据包的解复用器

## 名称

`ng_gif_demux`

## 概要

`#include <netgraph/ng_gif_demux.h>`

## 描述

`ng_gif_demux` netgraph 节点类型在 [netgraph(4)](netgraph.4.md) 网络子系统中对来自 [ng_gif(4)](ng_gif.4.md) 节点的输出进行解复用。

`gif` 钩子用于连接到 [ng_gif(4)](ng_gif.4.md) 节点的 `lower` 或 `orphans` 钩子。当在 `gif` 钩子上接收到 `inet`、`inet6`、`atalk`、`ipx`、`atm`、`natm` 和 `ns` 类型的帧时，会从对应的钩子输出。当在这些钩子之一上接收到帧时，会对其进行封装并通过 `gif` 钩子发送出去。

## 钩子

本节点类型支持以下钩子：

**`gif`** 连接到 [ng_gif(4)](ng_gif.4.md) 节点的 `lower` 或 `orphans` 钩子。

**`inet`** IP 帧的输入和输出钩子。

**`inet6`** IPv6 帧的输入和输出钩子。

**`atalk`** AppleTalk 帧的输入和输出钩子。

**`ipx`** IPX 帧的输入和输出钩子。

**`atm`** ATM 帧的输入和输出钩子。

**`natm`** NATM 帧的输入和输出钩子。

**`ns`** NS 帧的输入和输出钩子。

## 控制消息

本节点类型仅支持通用控制消息。

## 参见

[gif(4)](gif.4.md), [netgraph(4)](netgraph.4.md), [netintro(4)](netintro.4.md), [ng_gif(4)](ng_gif.4.md), [ifconfig(8)](../man8/ifconfig.8.md), ngctl(8), nghook(8)

## 作者

Brooks Davis <brooks@FreeBSD.org>
