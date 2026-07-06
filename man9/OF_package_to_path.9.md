# OF\_package\_to\_path.9

`OF_package_to_path` — 获取设备树节点的完全限定路径

## 名称

`OF_package_to_path`

## 概要

```c
#include <dev/ofw/ofw_bus.h>
#include <dev/ofw/ofw_bus_subr.h>

ssize_t
OF_package_to_path(phandle_t node, char *buf, size_t len)
```

## 描述

`OF_package_to_path` 将设备树节点 `node` 的完全限定路径最多 `len` 字节复制到 `buf` 指定的内存中。函数返回复制的字节数，出错时返回 -1。

## 参见

[OF_finddevice(9)](of_finddevice.9.md)

## 作者

本手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。
