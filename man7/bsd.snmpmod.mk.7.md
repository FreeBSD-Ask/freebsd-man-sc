# bsd.snmpmod.mk.7

`bsd.snmpmod.mk` — 为 bsnmpd(1) 构建模块

## 名称

`bsd.snmpmod.mk` bsnmpd(1)

## 概要

`Fd .include <bsd.snmpmod.mk>`

## 描述

文件

`#include <bsd.snmpmod.mk>`

简化了 Begemot SNMP 守护进程 bsnmpd(1) 的模块构建。它提供了一些构建模块的通用功能，并依赖于

`#include <bsd.lib.mk>`

该文件由

`#include <bsd.snmpmod.mk>`

包含，用于实际构建共享库。

以下 [make(1)](../man1/make.1.md) 变量控制这些特殊功能：

**`MOD`** 模块的短名称。共享库名称将为 `snmp_${MOD}.so`。必须存在文件 `${MOD}_tree.def` 用于与 gensnmptree(1) 一起编译，该文件包含模块所实现的 MIB 树定义。

**`EXTRAMIBDEFS`** gensnmptree(1) 的额外 MIB 定义文件列表。此项可选。此文件列表会传递给 gensnmptree(1) 的两次调用——一次从 MIB 定义中提取 `XSYM` 中的符号，另一次生成由此模块提供的 OID 表。

**`EXTRAMIBSYMS`** gensnmptree(1) 的额外 MIB 定义文件列表。此项可选。此文件列表仅传递给从 MIB 定义文件中提取符号的 gensnmptree(1) 调用。当存在对其他 MIB 的依赖或需要为枚举常量提取全局定义时很有用。

**`XSYM`** 由 gensnmptree(1) 从 MIB 定义文件中提取的符号列表。此项可选。

**`DEFS`** 要安装的 MIB 定义文件列表。此项可选。

**`BMIBS`** 要安装的文本 MIB 列表。此项可选。

根据 MIB 定义文件和 `XSYM` 变量，自动创建三个文件：

**`${MOD}_tree.c`** 包含模块所实现树结构的表。它会自动包含到 `SRCS` 变量中。

**`${MOD}_tree.h`** 包含模块定义的所有 OID 的预处理器定义，可包含在模块的源代码中。

**`${MOD}_oid.h`** `XSYMS` 中列出的所有符号的 OID 预处理器定义。此文件应包含在模块的源代码中。

## 参见

bsnmpd(1), gensnmptree(1), snmpmod(3)
