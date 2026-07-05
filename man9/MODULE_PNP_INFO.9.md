# MODULE\_PNP\_INFO.9

`MODULE_PNP_INFO` — 注册用于设备匹配的即插即用信息

## 名称

`MODULE_PNP_INFO`

## 概要

```c
#include <sys/module.h>

MODULE_PNP_INFO(const char *descriptor_string, bus, module, void *table,
    size_t num_entries)
```

## 描述

`MODULE_PNP_INFO` 宏注册一个包含设备识别数据的 `table`，供 [devmatch(8)](../man8/devmatch.8.md) 使用。由于它基于模块标记宏构建，因此必须放在 [DRIVER_MODULE(9)](DRIVER_MODULE.9.md) 行之后。

该宏接受一个 `descriptor_string` 来描述表项的内存布局。该字符串是由分号分隔的一系列成员组成的。成员由类型和名称标识。在描述符字符串中，通过将类型与冒号连接，后跟名称来编码它们。（特殊类型 `W32` 表示两个成员。第一个名称的编码方式与任何其他类型相同。第二个名称通过在第一个名称后追加正斜杠和第二个名称来编码。）

类型为以下之一：

**“`U8`”** `uint8_t` 元素。

**“`V8`”** 与 `U8` 相同，但哨兵值 0xFF 匹配任意值。

**“`G16`”** `uint16_t` 元素；大于或等于该值的任何值都匹配。

**“`L16`”** `uint16_t` 元素；小于或等于该值的任何值都匹配。

**“`M16`”** `uint16_t` 元素；用于指示以下哪些字段要使用的掩码。

**“`U16`”** `uint16_t` 元素。

**“`V16`”** 与 `U16` 相同，但哨兵值 0xFFFF 匹配任意值。

**“`U32`”** `uint32_t` 元素。

**“`V32`”** 与 `U32` 相同，但哨兵值 0xFFFFFFFF 匹配任意值。

**“`W32`”** 两个 `uint16_t` 值；第一个命名的成员在最低有效字中，第二个命名的成员在最高有效字中。

**“`Z`”** 指向需精确匹配的字符串的指针。

**“`D`”** 指向设备的人类可读描述的指针。

**“`P`”** 应被忽略的指针。

**“`E`”** EISA PNP 标识符。

**“`T`”** 对整个表都成立的 PNP 信息。驱动程序代码在使用此表匹配设备之前会实用地检查这些条件。此项必须放在列表的最后。

伪名称“#”保留给应被忽略的字段。任何与父设备的 pnpinfo 输出不匹配的成员都必须被忽略。

`bus` 参数是一个不带引号的词，命名驱动的父总线。例如“pci”。

`module` 参数也是一个不带引号的词。它对驱动必须唯一。通常使用驱动名称。

`table` 参数指向设备匹配数据，其条目与 `descriptor_string` 匹配。

`num_entries` 参数是表中的条目数，即 `nitems(table)`。注意只应包含有效的条目。如果表末尾包含尾随的零或无效值，则不应将它们包含在 `num_entries` 中。

## 实例

```c
#include <sys/param.h>
#include <sys/module.h>
static struct my_pciids {
	uint32_t devid;
	const char *desc;
} my_ids[] = {
	{ 0x12345678, "Foo bar" },
	{ 0x9abcdef0, "Baz fizz" },
};
MODULE_PNP_INFO("W32:vendor/device;D:#", pci, my_driver, my_ids,
    nitems(my_ids));
```

```c
#include <sys/param.h>
#include <sys/module.h>
static struct my_pciids {
	uint16_t device;
	const char *desc;
} my_ids[] = {
	{ 0x9abc, "Foo bar" },
	{ 0xdef0, "Baz fizz" },
};
MODULE_PNP_INFO("U16:device;D:#;T:vendor=0x1234", pci, my_driver,
    my_ids, nitems(my_ids));
```

**实例 1：为厂商/设备对使用 W32** 以下示例展示了当厂商/设备值组合为单个 `uint32_t` 值时 `W32` 类型的用法：

**实例 2：为公共厂商值使用 T** 以下示例展示了当表中所有条目具有相同厂商值时 `T` 类型的用法：

## 缺陷

由于 `linker.hints` 文件格式的限制，`MODULE_PNP_INFO` 宏必须放在 `DRIVER_MODULE` 调用之后。

## 参见

[devmatch(8)](../man8/devmatch.8.md), [DRIVER_MODULE(9)](DRIVER_MODULE.9.md), [module(9)](module.9.md)

## 历史

`MODULE_PNP_INFO` 宏首次出现于 FreeBSD 11.0。

## 作者

PNP 框架和 [devmatch(8)](../man8/devmatch.8.md) 实用程序由 Warner Losh <imp@FreeBSD.org> 编写。
