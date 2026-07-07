# openfirm(4)

`openfirm` — Open Firmware 接口

## 名称

`openfirm`

## 概要

`#include <sys/types.h>`

`#include <sys/ioctl.h>`

`#include <dev/ofw/openfirmio.h>`

## 描述

**/dev/openfirm** 设备是 Open Firmware 设备树的接口。此接口具有高度风格化的特点。所有操作均使用 ioctl(2) 调用。这些调用引用 Open Firmware 设备树中的节点。节点由包句柄（package handle）表示，包句柄是描述数据区域的整数值。有时也会使用或返回包句柄 0，如下所述。

仅接受和/或返回节点包句柄的调用为此使用指向 `phandle_t` 的指针。其他调用使用指向 `struct ofiocdesc` 描述符的指针，该结构定义如下：

```sh
struct ofiocdesc {
	phandle_t	of_nodeid;
	int		of_namelen;
	const char	*of_name;
	int		of_buflen;
	char		*of_buf;
};
```

`of_nodeid` 成员是传入或返回的节点的包句柄。字符串通过 `of_name` 成员传入，长度为 `of_namelen`。`of_name` 的最大接受长度为 `OFIOCMAXNAME`。`of_buf` 成员用于返回字符串，但在 `OFIOCSET` 调用中也用于传入字符串。在后一种情况下，`of_buf` 的最大接受长度为 `OFIOCMAXVALUE`。通常，`of_buf` 以值-结果方式工作。进入 ioctl(2) 调用时，`of_buflen` 应反映缓冲区大小。返回时，`of_buflen` 会更新以反映缓冲区内容。

支持以下 ioctl(2) 调用：

**`OFIOCGETOPTNODE`** 使用 `phandle_t`。不接受参数，返回 **/options** 节点的包句柄。

**`OFIOCGETNEXT`** 使用 `phandle_t`。接受一个节点的包句柄，返回 Open Firmware 设备树中下一个节点的包句柄。最后一个节点之后的节点包句柄为 0。包句柄为 0 的节点之后的节点是第一个节点。

**`OFIOCGETCHILD`** 使用 `phandle_t`。接受一个节点的包句柄，返回该节点第一个子节点的包句柄。此子节点可能有兄弟节点，可使用 `OFIOCGETNEXT` 确定。如果该节点没有子节点，则返回包句柄 0。

**`OFIOCGET`** 使用 `struct ofiocdesc`。接受一个节点的包句柄和属性名称。返回属性值及其长度。如果该节点没有关联此属性，值的长度设为 -1。如果命名的属性存在但没有值，值的长度设为 0。

**`OFIOCGETPROPLEN`** 使用 `struct ofiocdesc`。接受一个节点的包句柄和属性名称。返回属性值的长度。此调用与 `OFIOCGET` 相同，只是仅返回属性值的长度。它可用于确定节点是否具有特定属性，或属性是否具有值，而无需为存储值提供内存。

**`OFIOCSET`** 使用 `struct ofiocdesc`。接受一个节点的包句柄、属性名称和属性值。返回实际写入的属性值和长度。如果值过长，Open Firmware 可能会选择截断；如果给定值对特定属性无效，则可能写入一个有效值。因此应检查返回值。Open Firmware 也可能完全拒绝将给定值写入属性。在这种情况下，返回 [Er EINVAL]。

**`OFIOCNEXTPROP`** 使用 `struct ofiocdesc`。接受一个节点的包句柄和属性名称。返回该节点下一个属性的名称和长度。如果给定名称引用的属性是该节点的最后一个属性，则返回 [Er ENOENT]。

**`OFIOCFINDDEVICE`** 使用 `struct ofiocdesc`。接受设备节点的名称或别名。返回该节点的包句柄。如果未找到匹配的节点，返回 [Er ENOENT]。

## 文件

**`/dev/openfirm`** Open Firmware 接口节点

## 诊断

以下情况可能导致操作被拒绝：

**[Er EBADF]** 请求的操作需要 Fn open 调用时未指定的权限。

**[Er EINVAL]** 给定的包句柄不为 0 且不对应任何有效节点，或给定的包句柄为 0 但不允许为 0。

**[Er ENAMETOOLONG]** 给定的名称或值分别超过了 `OFIOCMAXNAME` 和 `OFIOCMAXVALUE` 字节的最大允许长度。

## 参见

ioctl(2), ofwdump(8)

> *Core Requirements and Practices"*, ISBN 1-55937-426-8.

## 历史

`openfirm` 接口最早出现于 NetBSD 1.6。第一个包含它的 FreeBSD 版本是 FreeBSD 5.0。

## 作者

`openfirm` 接口由 Thomas Moestl <tmm@FreeBSD.org> 移植到 FreeBSD。本手册页由 Marius Strobl <marius@FreeBSD.org> 基于 OpenBSD 的 openprom(4) 手册页编写。

## 注意事项

由于 Open Firmware 自身的限制，这些函数以提升的优先级运行，可能对系统性能产生不利影响。

至少对于 **/options** 节点，传入 `OFIOCSET` 调用的属性值必须以 null 终止，传入的值长度必须包含终止符 `e0`。但是，与 `OFIOCGET` 调用一样，返回的值长度不包含终止符 `e0`。
