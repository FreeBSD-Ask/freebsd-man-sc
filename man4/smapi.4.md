# smapi(4)

`smapi` — 系统管理应用程序接口驱动

## 名称

`smapi`

## 描述

许多 IBM Thinkpad 笔记本电脑使用一种称为 SMAPI（System Management Application Program Interface）的特殊软件接口。此接口控制系统的各个方面，包括：

- 系统接口（BIOS 可存储系统信息，如系统标识符），
- 系统配置（可配置显示器等设备），
- 电源管理（软件可与 SMAPI BIOS 交互以进行电源管理控制）。

客户端软件必须找到存储在 Thinkpad ROM（只读存储器）中 `F000` 段内的“header image”，它位于 16 字节边界处。这被视为服务的“入口点”。

“header image”存储以下信息：

- 签名，
- SMAPI 版本（主版本和次版本），
- header image 长度，
- 校验和信息（用于验证映像），
- 信息字（用于标识 BIOS 服务级别），
- 实模式入口点（使用实模式/V86 模式的客户端用于 far-call 值），
- 最后是 16 位/32 位保护模式入口点：基本代码地址，指定 BIOS 物理地址。客户端必须为此 BIOS 准备一个 64 千字节的选择子。

要调用 SMAPI BIOS，必须对头文件中指定的入口点使用 far-call。所有其他信息应存储在客户端数据区中。客户端需要在自己的数据区中准备输入和输出参数。可通过在 far-call 之前将这些指针压入栈来“通知”此区域。

SMAPI BIOS 在 BIOS 调用期间使用带选择子的栈和数据区，因此调用方必须定义与 BIOS 相同的特权区域。

参数结构由调用方准备的输入和输出字段构成。输入字段向 BIOS 指定函数请求。BIOS 随后向输出字段中放入返回值。这些字段由三部分组成。第一部分包含参数、函数号和返回代码。下一部分包含十六进制偏移量。最后是长度字段，由字节、字或双字组成。

## 参见

> *IBM Thinkpad 560/560E Technical Reference*, 06J0536 S76H-7587-01。

> *IBM Thinkpad 560Z Technical Reference*, xxxxxxx xxxx-xxxx-xx。

> *IBM Thinkpad 600 Technical Reference*, xxxxxxx xxxx-xxxx-xx。

> *IBM Thinkpad 760XD/760XL/765D/765L Technical Reference*, 06J0537 S30H-2433-02。

> *IBM Thinkpad 770 Technical Reference*, 05L1739 S05L-1739-00。

## 作者

`smapi` 驱动由 Matthew N. Dodd <mdodd@FreeBSD.org> 编写。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 和 Matthew N. Dodd <mdodd@FreeBSD.org> 编写。
