# stab(5)

`stab` — 符号表类型

## 名称

`stab`

## 概要

`#include <stab.h>`

## 描述

文件

`#include <stab.h>`

为 a.out 文件定义了一些符号表 `n_type` 字段值。这些是旧调试器 *sdb* 和 Berkeley Pascal 编译器 pc(1) 所使用的永久符号（即不是局部标号等）的类型。符号表条目可以由 `.stabs` 汇编指令产生。这允许指定一个用双引号定界的名称、一个符号类型、一个字符和一个短整数的信息，以及一个无符号长整数（通常是地址）。为了避免必须为地址字段显式产生一个标号，可以使用 `.stabd` 指令隐式地寻址当前位置。如果不需要名称，可以使用 `.stabn` 指令生成符号表条目。链接器承诺保留由 `.stab` 指令产生的符号表条目的顺序。如 [a.out(5)](a.out.5.md) 中所述，符号表的一个元素由以下结构组成：

```sh
/*
* 符号表条目的格式。
*/
struct nlist {
	union {
		const char *n_name;	/* 用于在内存中时 */
		long	n_strx;		/* 文件字符串表的索引 */
	} n_un;
	unsigned char	n_type;		/* 类型标志 */
	char		n_other;	/* 未使用 */
	short		n_desc;		/* 见下文的 desc 结构 */
	unsigned	n_value;	/* 地址或偏移量或行号 */
};
```

`n_type` 字段的低位用于根据以下掩码将符号放入至多一个段中，这些掩码定义于

`#include <a.out.h>`

如果这些段位均未设置，则符号可以不属于任何段。

```sh
/*
* n_type 的简单值。
*/
#define	N_UNDF	0x0	/* 未定义 */
#define	N_ABS	0x2	/* 绝对 */
#define	N_TEXT	0x4	/* 文本 */
#define	N_DATA	0x6	/* 数据 */
#define	N_BSS	0x8	/* bss */
#define	N_EXT	01	/* 外部位，或入 */
```

符号的 `n_value` 字段由链接器 [ld(1)](../man1/ld.1.md) 作为相应段内的地址进行重定位。不属于任何段的符号的 `N_value` 字段不会被链接器更改。此外，除非 `n_type` 字段设置了以下位之一，链接器将根据自身规则丢弃某些符号：

```sh
/*
* 其他永久符号表条目设置了某些 N_STAB 位。
* 这些在 <stab.h> 中给出
*/
#define	N_STAB	0xe0	/* 如果设置了这些位中的任何一个，不要丢弃 */
```

这允许至多 112（7 × 16）种符号类型，分布在各个段之间。其中一些已被使用。旧的符号调试器 *sdb* 使用以下 n_type 值：

```sh
#define	N_GSYM	0x20	/* 全局符号：name,,0,type,0 */
#define	N_FNAME	0x22	/* 过程名（f77 权宜之计）：name,,0 */
#define	N_FUN	0x24	/* 过程：name,,0,linenumber,address */
#define	N_STSYM	0x26	/* 静态符号：name,,0,type,address */
#define	N_LCSYM	0x28	/* .lcomm 符号：name,,0,type,address */
#define	N_RSYM	0x40	/* 寄存器符号：name,,0,type,register */
#define	N_SLINE	0x44	/* 源码行：0,,0,linenumber,address */
#define	N_SSYM	0x60	/* 结构元素：name,,0,type,struct_offset */
#define	N_SO	0x64	/* 源文件名：name,,0,0,address */
#define	N_LSYM	0x80	/* 局部符号：name,,0,type,offset */
#define	N_SOL	0x84	/* #included 文件名：name,,0,0,address */
#define	N_PSYM	0xa0	/* 参数：name,,0,type,offset */
#define	N_ENTRY	0xa4	/* 备用入口：name,linenumber,address */
#define	N_LBRAC	0xc0	/* 左括号：0,,0,nesting level,address */
#define	N_RBRAC	0xe0	/* 右括号：0,,0,nesting level,address */
#define	N_BCOMM	0xe2	/* common 开始：name,, */
#define	N_ECOMM	0xe4	/* common 结束：name,, */
#define	N_ECOML	0xe8	/* common 结束（本地名）：,,address */
#define	N_LENG	0xfe	/* 带有长度信息的第二个 stab 条目 */
```

其中注释给出了 *sdb* 对 `.stab` `s` 以及给定 `n_type` 的 `n_name`、`n_other`、`n_desc` 和 `n_value` 字段的约定用法。*Sdb* 使用 `n_desc` 字段保存 Portable C Compiler [cc(1)](../man1/cc.1.md) 所使用的形式中的类型说明符；有关这些类型值格式的详细信息，请参见头文件 `pcc.h`。

Berkeley Pascal 编译器 pc(1) 使用以下 `n_type` 值：

```sh
#define	N_PC	0x30	/* 全局 pascal 符号：name,,0,subtype,line */
```

并使用以下子类型在单独编译的文件之间进行类型检查：

```sh
1	源文件名
2	包含文件名
3	全局标号
4	全局常量
5	全局类型
6	全局变量
7	全局函数
8	全局过程
9	外部函数
10	外部过程
11	库变量
12	库例程
```

## 参见

as(1), [ld(1)](../man1/ld.1.md), [a.out(5)](a.out.5.md)

## 历史

`stab` 文件出现于 4.0BSD。

## 缺陷

需要更多基本类型。
