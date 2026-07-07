# OF_finddevice(9)

`OF_finddevice` — 在设备树中查找节点

## 名称

`OF_finddevice`

## 概要

```c
#include <dev/ofw/ofw_bus.h>
#include <dev/ofw/ofw_bus_subr.h>

phandle_t
OF_finddevice(const char *path)
```

## 描述

`OF_finddevice` 返回由 `path` 指定的节点的 phandle。如果在树中找不到该路径，则返回 -1。

## 实例

```c
phandle_t root, i2c;
root = OF_finddevice("/");
i2c = OF_finddevice("/soc/axi/i2c@a0e0000");
if (i2c != -1) {
    ...
}
```

## 参见

[OF_child(9)](of_child.9.md), [OF_parent(9)](of_child.9.md), [OF_peer(9)](of_child.9.md)

## 作者

本手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。

## 注意事项

返回值只能用相等运算符（等于、不等于）来检查，而不能用关系比较（小于、大于）。IEEE 1275 标准与 FreeBSD 的 phandle 内部表示之间存在差异：IEEE 1275 要求如果未找到路径，此函数的返回值为 -1。但 phandle_t 是无符号类型，因此不能与 -1 或 0 进行关系比较，这种比较始终为真或始终为假。
