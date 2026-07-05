# OF\_getprop.9

`OF_getprop` — 访问设备树节点的属性

## 名称

`OF_getprop`, `OF_getproplen`, `OF_getencprop`, `OF_hasprop`, `OF_searchprop`, `OF_searchencprop`, `OF_getprop_alloc`, `OF_getencprop_alloc`, `OF_getprop_alloc_multi`, `OF_getencprop_alloc_multi`, `OF_prop_free`, `OF_nextprop`, `OF_setprop`

## 概要

```c
#include <dev/ofw/ofw_bus.h>
#include <dev/ofw/ofw_bus_subr.h>

ssize_t
OF_getproplen(phandle_t node, const char *propname)

ssize_t
OF_getprop(phandle_t node, const char *propname, void *buf, size_t len)

ssize_t
OF_getencprop(phandle_t node, const char *prop, pcell_t *buf, size_t len)

bool
OF_hasprop(phandle_t node, const char *propname)

ssize_t
OF_searchprop(phandle_t node, const char *propname, void *buf, size_t len)

ssize_t
OF_searchencprop(phandle_t node, const char *propname, pcell_t *buf,
    size_t len)

ssize_t
OF_getprop_alloc(phandle_t node, const char *propname, void **buf)

ssize_t
OF_getencprop_alloc(phandle_t node, const char *propname, pcell_t **buf)

ssize_t
OF_getprop_alloc_multi(phandle_t node, const char *propname, int elsz,
    void **buf)

ssize_t
OF_getencprop_alloc_multi(phandle_t node, const char *propname, int elsz,
    pcell_t **buf)

void
OF_prop_free(void *buf)

int
OF_nextprop(phandle_t node, const char *propname, char *buf, size_t len)

int
OF_setprop(phandle_t node, const char *propname, const void *buf, size_t len)
```

## 描述

设备节点可以有关联的属性。属性由名称和值组成。名称是 1 到 31 个字符长的人类可读字符串。值是零个或多个字节的数组，编码特定信息。这些字节的含义取决于驱动程序如何解释它们。属性可以编码字节数组、文本字符串、无符号 32 位值或这些类型的任意组合。

值为零长度的属性通常表示布尔信息。如果该属性存在，则表示真，否则表示假。

字节数组编码为字节序列，表示 MAC 地址等值。

文本字符串是 n 个可打印字符的序列。它被编码为长度为 n + 1 字节的字节数组，字符以字节表示，加上一个终止空字符。

无符号 32 位值（有时也称为 cell）以大端序的 4 字节序列编码。

`OF_getproplen` 返回由 `node` 标识的节点中与属性 `propname` 关联的值的长度，或者如果属性存在但没有关联值则返回 0。如果 `propname` 不存在，则返回 -1。

`OF_getprop` 将设备节点 `node` 的属性 `propname` 关联的值中最多 `len` 字节复制到 `buf` 指定的内存中。返回值的实际大小，如果属性不存在则返回 -1。

`OF_getencprop` 将最多 `len` 字节复制到 `buf` 指定的内存中，然后将 cell 值从大端序转换为主机字节序。返回值的实际大小（以字节为单位），如果属性不存在则返回 -1。`len` 必须是 4 的倍数。

`OF_hasprop` 如果设备节点 `node` 具有 `propname` 指定的属性则返回 `true`，如果属性不存在则返回 `false`。

`OF_searchprop` 从设备节点 `node` 开始，递归查找由 `propname` 指定的属性，然后是父节点，直到根节点。如果找到属性，该函数将与该属性关联的值中最多 `len` 字节复制到 `buf` 指定的内存中。返回值的实际大小（以字节为单位），如果属性不存在则返回 -1。

`OF_searchencprop` 从设备节点 `node` 开始，递归查找由 `propname` 指定的属性，然后是父节点，直到根节点。如果找到属性，该函数将与该属性关联的值中最多 `len` 字节复制到 `buf` 指定的内存中，然后将 cell 值从大端序转换为主机字节序。返回值的实际大小（以字节为单位），如果属性不存在则返回 -1。

`OF_getprop_alloc` 分配足够大的内存来容纳设备节点 `node` 的属性 `propname` 关联的值，并将该值复制到新分配的内存区域。返回值的实际大小，并将分配内存的地址存储在 `*buf` 中。如果属性具有零大小的值，则 `*buf` 设置为 NULL。如果属性不存在或内存分配失败则返回 -1。分配的内存不再需要时应通过调用 `OF_prop_free` 释放。该函数在分配内存时可能会睡眠。

`OF_getencprop_alloc` 分配足够的内存来容纳设备节点 `node` 的属性 `propname` 关联的值，将该值复制到新分配的内存区域，然后将 cell 值从大端序转换为主机字节序。返回值的实际大小，并将分配内存的地址存储在 `*buf` 中。如果属性具有零长度值，则 `*buf` 设置为 NULL。如果属性不存在、内存分配失败或值的大小不能被 cell 大小（4 字节）整除则返回 -1。分配的内存不再需要时应通过调用 `OF_prop_free` 释放。该函数在分配内存时可能会睡眠。

`OF_getprop_alloc_multi` 分配足够大的内存来容纳设备节点 `node` 的属性 `propname` 关联的值，并将该值复制到新分配的内存区域。该值应为零个或多个长度为 `elsz` 字节的元素数组。返回值中的元素数量，并将分配内存的地址存储在 `*buf` 中。如果属性具有零大小的值，则 `*buf` 设置为 NULL。如果属性不存在、内存分配失败或值的大小不能被 `elsz` 整除则返回 -1。分配的内存不再需要时应通过调用 `OF_prop_free` 释放。该函数在分配内存时可能会睡眠。

`OF_getencprop_alloc_multi` 分配足够大的内存来容纳设备节点 `node` 的属性 `propname` 关联的值，将该值复制到新分配的内存区域，然后将 cell 值从大端序转换为主机字节序。该值应为零个或多个长度为 `elsz` 字节的元素数组。返回值中的元素数量，并将分配内存的地址存储在 `*buf` 中。如果属性具有零大小的值，则 `*buf` 设置为 NULL。如果属性不存在、内存分配失败或值的大小不能被 `elsz` 整除则返回 -1。分配的内存不再需要时应通过调用 `OF_prop_free` 释放。该函数在分配内存时可能会睡眠。

`OF_prop_free` 释放由 `OF_getprop_alloc`、`OF_getencprop_alloc`、`OF_getprop_alloc_multi`、`OF_getencprop_alloc_multi` 分配的 `buf` 处的内存。

`OF_nextprop` 将 `propname` 属性之后的下一个属性的名称最多 `size` 字节复制到 `buf` 中。如果 `propname` 为 NULL，则函数复制设备节点 `node` 的第一个属性的名称。如果 `propname` 无效或存在内部错误，`OF_nextprop` 返回 -1；如果 `propname` 之后没有更多属性则返回 0，否则返回 1。

`OF_setprop` 将设备节点 `node` 中属性 `propname` 的值设置为从 `buf` 指定地址开始、长度为 `len` 字节的值。如果属性不存在，函数会尝试创建它。`OF_setprop` 返回新值的实际大小，如果属性值无法更改或无法创建新属性则返回 -1。

## 实例

```c
phandle_t node;
phandle_t hdmixref, hdminode;
device_t hdmi;
uint8_t mac[6];
char *model;
/*
 * 获取字节数组属性
 */
if (OF_getprop(node, "eth,hwaddr", mac, sizeof(mac)) != sizeof(mac))
    return;
/*
 * 获取内部节点引用及关联的设备
 */
if (OF_getencprop(node, "hdmi", &hdmixref) <= 0)
    return;
hdmi = OF_device_from_xref(hdmixref);
/*
 * 获取 HDMI framer 节点的 model 属性的字符串值
 */
hdminode = OF_node_from_xref(hdmixref);
if (OF_getprop_alloc(hdminode, "model", (void **)&model) <= 0)
    return;
```

## 参见

[OF_device_from_xref(9)](OF_device_from_xref.9.md), [OF_node_from_xref(9)](OF_node_from_xref.9.md)

## 作者

本手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。
