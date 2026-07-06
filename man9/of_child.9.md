# OF\_child.9

`OF_child` — 导航设备树

## 名称

`OF_child`, `OF_parent`, `OF_peer`

## 概要

```c
#include <dev/ofw/ofw_bus.h>
#include <dev/ofw/ofw_bus_subr.h>

phandle_t
OF_child(phandle_t node)

phandle_t
OF_parent(phandle_t node)

phandle_t
OF_peer(phandle_t node)
```

## 描述

`OF_child` 返回 `node` 的第一个子节点的 phandle 值。如果没有子节点，则返回零。

`OF_parent` 返回 `node` 的父节点的 phandle。如果 `node` 是根节点，则返回零。

`OF_peer` 返回 `node` 的下一个兄弟节点的 phandle 值。如果没有兄弟节点，则返回零。

## 实例

```c
phandle_t node, child;
 ...
for (child = OF_child(node); child != 0; child = OF_peer(child)) {
	...
}
```

## 参见

[OF_finddevice(9)](of_finddevice.9.md)

## 作者

本手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。
