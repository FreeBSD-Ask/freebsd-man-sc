# ng_device(4)

`ng_device` — 设备 netgraph 节点类型

## 名称

`ng_device`

## 概要

`#include <netgraph/ng_device.h>`

## 描述

`device` 节点既是 netgraph 节点，也是系统设备接口。创建 `device` 节点时，会出现新的设备条目，可通过常规文件操作（如 open(2)、close(2)、read(2)、write(2) 等）访问。

第一个节点创建为 **/dev/ngd0**，后续节点为 **/dev/ngd1**、**/dev/ngd2** 等。

## 钩子

`device` 节点有一个具有任意名称的钩子。所有通过钩子进入的数据将呈现给设备供 read(2) 读取。所有通过 write(2) 从设备条目进入的数据将转发到钩子。

## 控制消息

`device` 节点支持通用控制消息，外加以下消息：

**`NGM_DEVICE_GET_DEVNAME`** 返回与节点对应的设备名。

**`NGM_DEVICE_ETHERALIGN`** 在运行于要求严格对齐的体系结构上时，将系统 ETHER_ALIGN 偏移应用于从节点钩子发出的 mbuf。当通过 device 节点注入的数据最终作为以太网数据包送入协议栈（例如通过 [ng_eiface(4)](ng_eiface.4.md) 节点）时，使用此选项。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在钩子断开时关闭。关联的设备条目被移除并可供未来的 `device` 节点使用。

## 参见

[netgraph(4)](netgraph.4.md), ngctl(8)

## 历史

`device` 节点类型首次实现于 FreeBSD 5.0。

## 作者

Mark Santcroos <marks@ripe.net> Gleb Smirnoff <glebius@FreeBSD.org>
