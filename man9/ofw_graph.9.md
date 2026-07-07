# ofw_graph(9)

`ofw_graph` — DTS graph 绑定的辅助函数

## 名称

`ofw_graph`, `ofw_graph_get_port_by_idx`, `ofw_graph_port_get_num_endpoints`, `ofw_graph_get_endpoint_by_idx`, `ofw_graph_get_remote_endpoint`, `ofw_graph_get_remote_parent`, `ofw_graph_get_device_by_port_ep`

## 概要

```c
#include <dev/ofw/openfirm.h>
```

```c
#include <dev/ofw/ofw_graph.h>
```

```c
phandle_t
ofw_graph_get_port_by_idx(phandle_t node, uint32_t idx)

size_t
ofw_graph_port_get_num_endpoints(phandle_t port)

phandle_t
ofw_graph_get_endpoint_by_idx(phandle_t port, uint32_t idx)

phandle_t
ofw_graph_get_remote_endpoint(phandle_t endpoint)

phandle_t
ofw_graph_get_remote_parent(phandle_t remote)

device_t
ofw_graph_get_device_by_port_ep(phandle_t node, uint32_t port_id, uint32_t ep_id)
```

## 描述

`ofw_graph` 函数是用于解析 DTS graph 绑定的辅助函数。

`ofw_graph_get_port_by_idx` 返回 id 为 `idx` 的端口。它会首先检查名为 `port@idx` 的节点，然后回退到检查 `ports` 子节点中是否有匹配该 id 的子节点。如果没有找到匹配 `idx` 的端口，函数返回 0。

`ofw_graph_port_get_num_endpoints` 返回一个端口节点拥有的端点数量。

`ofw_graph_get_endpoint_by_idx` 返回 id 为 `idx` 的端点。它会首先检查是否存在名为 `endpoint` 的单一子节点，如果存在则返回它。如果存在多个端点，它将检查 `reg` 属性并返回正确的 `phandle_t`，如果没有匹配的则返回 0。

`ofw_graph_get_remote_endpoint` 返回 `remote-endpoint` 属性（如果存在），否则返回 0。

`ofw_graph_get_remote_parent` 返回对应于 `remote-endpoint` phandle 的设备节点，如果没有则返回 0。`ofw_graph_get_device_by_port_ep` 返回与该端口和端点关联的设备，如果没有则返回 `NULL`。设备驱动程序应事先调用 `OF_device_register_xref`。

## 历史

`ofw_graph` 函数首次出现在 FreeBSD 13.0 中。`ofw_graph` 函数和手册页由 Emmanuel Vadot <manu@FreeBSD.org> 编写。
