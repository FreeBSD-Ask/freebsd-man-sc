# ng_gif(4)

`ng_gif` — 通用隧道接口 netgraph 节点类型

## 名称

`ng_gif`

## 概要

`#include <netgraph/ng_gif.h>`

## 描述

`ng_gif` netgraph 节点类型允许 [gif(4)](gif.4.md) 接口与 [netgraph(4)](netgraph.4.md) 网络子系统交互。一旦 `ng_gif` 模块加载到内核中，系统中的每个 [gif(4)](gif.4.md) 接口都会自动创建一个节点。每个节点会尝试以关联接口的名称为自己命名。只要接口本身存在，所有 `ng_gif` 节点都会持续存在。

该节点类型支持两个钩子：`lower` 和 `orphans`。钩子名 `divert` 可作为 `lower` 的别名使用，提供与 [ng_ether(4)](ng_ether.4.md) 的兼容性。实际上这两个名称代表同一个钩子。

`lower` 钩子连接到原始 [gif(4)](gif.4.md) 设备。连接后，所有传入的数据包都会从该钩子分流出去。写入该钩子的数据会作为原始封装数据包由设备发送。`lower` 连接后，正常的发出数据包不受影响。

`orphans` 钩子等价于 `lower`，区别在于只有无法识别的数据包（否则会被丢弃）会被写入该钩子，而正常的传入流量不受影响。`orphans` 和 `lower` 在任何时候最多只能连接其中一个。

在所有情况下，帧都是带有地址族前缀的原始数据包。

当没有钩子连接时，数据包正常向上和向下流动。

## 钩子

本节点类型支持以下钩子：

**`lower`** 连接到下层设备链路层。

**`orphans`** 类似于 `lower`，但只接收无法识别的数据包。

## 控制消息

本节点类型仅支持通用控制消息。

## 实例

以下命令将 `gif0` 接口接收的所有无法识别的数据包以十六进制和 ASCII 形式解码后输出到标准输出：

```sh
nghook -a gif0: orphans
```

## 参见

[gif(4)](gif.4.md), [netgraph(4)](netgraph.4.md), [netintro(4)](netintro.4.md), [ifconfig(8)](../man8/ifconfig.8.md), ngctl(8), nghook(8)

## 作者

Brooks Davis <brooks@FreeBSD.org>
