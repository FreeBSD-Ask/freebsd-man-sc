# microseq.9

`microseq` — ppbus 微序列器开发者指南

## 名称

`microseq`

## 概要

```c
#include <sys/types.h>
```

```c
#include <dev/ppbus/ppbconf.h>
```

```c
#include <dev/ppbus/ppb_msq.h>
```

## 描述

ppbus 的描述及微序列器的总体信息参见 [ppbus(4)](../man4/ppbus.4.md)。

本文档的目的是鼓励开发者使用微序列器机制，以获得：

- 统一的编程模型
- 高效的代码

在使用微序列之前，建议查看 [ppc(4)](../man4/ppc.4.md) 的微序列器实现以及 [ppi(4)](../man4/ppi.4.md) 中如何使用它的示例。

## PPBUS 寄存器模型

### 背景

为 ppbus 选择的并行端口模型是 PC 并行端口模型。因此，后文所述的任何寄存器与其在 PC 并行端口中的对应物具有相同语义。有关 ISA/ECP 编程的更多信息，可获取名为 "Extended Capabilities Port Protocol and ISA interface Standard" 的 Microsoft 标准。后文所述寄存器为标准并行端口寄存器。

标准 ppbus 包含文件中为并行端口寄存器的每个有效位定义了掩码宏。

### 数据寄存器

在兼容模式或半字节模式下，写入此寄存器将数据驱动到并行端口数据线上。在任何其他模式下，可通过在控制寄存器中设置方向位（PCD）将驱动器置为三态。读取此寄存器返回数据线上的值。

### 设备状态寄存器

此只读寄存器反映并行端口接口上的输入。

| *位* | *名称* | *描述* |
| ---- | ------ | ------ |
| 7 | nBUSY | 并行端口 Busy 信号的反相版本 |
| 6 | nACK | 并行端口 nAck 信号的版本 |
| 5 | PERROR | 并行端口 PERROR 信号的版本 |
| 4 | SELECT | 并行端口 Select 信号的版本 |
| 3 | nFAULT | 并行端口 nFault 信号的版本 |

其他位保留，读取时返回未定义结果。

### 设备控制寄存器

此寄存器直接控制若干输出信号并启用某些功能。

| *位* | *名称* | *描述* |
| ---- | ------ | ------ |
| 5 | PCD | 扩展模式下的方向位 |
| 4 | IRQENABLE | 1 在 nAck 上升沿启用中断 |
| 3 | SELECTIN | 反相并驱动为并行端口 nSelectin 信号 |
| 2 | nINIT | 驱动为并行端口 nInit 信号 |
| 1 | AUTOFEED | 反相并驱动为并行端口 nAutoFd 信号 |
| 0 | STROBE | 反相并驱动为并行端口 nStrobe 信号 |

## 微指令

### 描述

*微指令*可以是并行端口访问、程序迭代、子微序列或 C 调用。并行端口应被视为 [ppbus(4)](../man4/ppbus.4.md) 中描述的逻辑模型。

可用的微指令包括：

```c
#define MS_OP_GET       0	/* get <ptr>, <len>			*/
#define MS_OP_PUT       1	/* put <ptr>, <len>			*/
#define MS_OP_RFETCH	2	/* rfetch <reg>, <mask>, <ptr>		*/
#define MS_OP_RSET	3	/* rset <reg>, <mask>, <mask>		*/
#define MS_OP_RASSERT	4	/* rassert <reg>, <mask>		*/
#define MS_OP_DELAY     5	/* delay <val>				*/
#define MS_OP_SET       6	/* set <val>				*/
#define MS_OP_DBRA      7	/* dbra <offset>			*/
#define MS_OP_BRSET     8	/* brset <mask>, <offset>		*/
#define MS_OP_BRCLEAR   9	/* brclear <mask>, <offset>		*/
#define MS_OP_RET       10	/* ret <retcode>			*/
#define MS_OP_C_CALL	11	/* c_call <function>, <parameter>	*/
#define MS_OP_PTR	12	/* ptr <pointer>			*/
#define MS_OP_ADELAY	13	/* adelay <val>				*/
#define MS_OP_BRSTAT	14	/* brstat <mask>, <mask>, <offset>	*/
#define MS_OP_SUBRET	15	/* subret <code>			*/
#define MS_OP_CALL	16	/* call <microsequence>			*/
#define MS_OP_RASSERT_P	17	/* rassert_p <iter>, <reg>		*/
#define MS_OP_RFETCH_P	18	/* rfetch_p <iter>, <reg>, <mask>	*/
#define MS_OP_TRIG	19	/* trigger <reg>, <len>, <array>	*/
```

### 执行上下文

微指令的*执行上下文*包括：

- *程序计数器*，指向主微序列或子调用中下一个要执行的微指令
- *ptr* 的当前值，指向下一个要发送/接收的字符
- 内部*分支寄存器*的当前值

此数据被部分微指令修改，并非全部。

### MS_OP_GET 和 MS_OP_PUT

是用于执行预定义标准 IEEE1284-1994 传输或编程非标准 I/O 的微指令。

### MS_OP_RFETCH - 寄存器读取（Register FETCH）

用于获取并行端口寄存器的当前值，应用掩码并将其保存到缓冲区。

参数：

- 寄存器
- 字符掩码
- 指向缓冲区的指针

预定义宏：MS_RFETCH(reg,mask,ptr)

### MS_OP_RSET - 寄存器设置（Register SET）

用于断言/清除特定并行端口寄存器的某些位，应用两个掩码。

参数：

- 寄存器
- 要断言的位掩码
- 要清除的位掩码

预定义宏：MS_RSET(reg,assert,clear)

### MS_OP_RASSERT - 寄存器断言（Register ASSERT）

用于断言特定并行端口寄存器的所有位。

参数：

- 寄存器
- 要断言的字节

预定义宏：MS_RASSERT(reg,byte)

### MS_OP_DELAY - 微秒延迟（microsecond DELAY）

用于延迟微序列的执行。

参数：

- 微秒为单位的延迟

预定义宏：MS_DELAY(delay)

### MS_OP_SET - 设置内部分支寄存器（SET internal branch register）

用于设置内部分支寄存器的值。

参数：

- 整数值

预定义宏：MS_SET(accum)

### MS_OP_DBRA - 执行分支（Do BRAnch）

如果内部分支寄存器减一后的结果为正，则分支。

参数：

- 当前执行的（子）微序列中的整数偏移量。偏移量加到下一个要执行的微指令的索引上。

预定义宏：MS_DBRA(offset)

### MS_OP_BRSET - 设置时分支（BRanch on SET）

如果并行端口状态寄存器的某些位被设置，则分支。

参数：

- 状态寄存器的位
- 当前执行的（子）微序列中的整数偏移量。偏移量加到下一个要执行的微指令的索引上。

预定义宏：MS_BRSET(mask,offset)

### MS_OP_BRCLEAR - 清除时分支（BRanch on CLEAR）

如果并行端口状态寄存器的某些位被清除，则分支。

参数：

- 状态寄存器的位
- 当前执行的（子）微序列中的整数偏移量。偏移量加到下一个要执行的微指令的索引上。

预定义宏：MS_BRCLEAR(mask,offset)

### MS_OP_RET - 返回（RETurn）

用于从微序列返回。此指令是必需的。这是微序列器检测微序列结束的唯一方式。返回码在 ppb_MS_microseq() 的 (int *) 参数所指向的整数中返回。

参数：

- 整数返回码

预定义宏：MS_RET(code)

### MS_OP_C_CALL - C 函数调用（C function CALL）

用于从微序列执行中调用 C 函数。当执行非标准 I/O 以从并行端口获取数据字符时，这可能很有用。

参数：

- 要调用的 C 函数
- 要传递给函数调用的参数

C 函数应声明为 `int(*)(void *p, char *ptr)`。`ptr` 参数是当前扫描缓冲区中的当前位置。

预定义宏：MS_C_CALL(func,param)

### MS_OP_PTR - 初始化内部 PTR（initialize internal PTR）

用于将内部指针初始化为当前扫描的缓冲区。此指针传递给任何 C 调用（见上文）。

参数：

- 指向应由 xxx_P() 微序列调用访问的缓冲区的指针。注意，此指针在 xxx_P() 调用期间自动递增。

预定义宏：MS_PTR(ptr)

### MS_OP_ADELAY - 执行异步延迟（Asynchronous DELAY）

用于在微序列执行期间执行 tsleep()。tsleep 在 PPBPRI 级别执行。

参数：

- 毫秒为单位的延迟

预定义宏：MS_ADELAY(delay)

### MS_OP_BRSTAT - 状态分支（BRanch on STATe）

用于根据状态寄存器状态条件分支。

参数：

- 断言位掩码。状态寄存器中应被断言的位在掩码中设置
- 清除位掩码。状态寄存器中应被清除的位在掩码中设置
- 当前执行的（子）微序列中的整数偏移量。偏移量加到下一个要执行的微指令的索引上。

预定义宏：MS_BRSTAT(asserted_bits,clear_bits,offset)

### MS_OP_SUBRET - 子微序列返回（SUBmicrosequence RETurn）

用于从子微序列调用返回。此操作在 RET 调用之前是必需的。某些微指令（PUT、GET）可能无法在子微序列中调用。

无参数。

预定义宏：MS_SUBRET()

### MS_OP_CALL - 子微序列调用（submicrosequence CALL）

用于调用子微序列。子微序列是带有 SUBRET 调用的微序列。参数：

- 要执行的子微序列

预定义宏：MS_CALL(microseq)

### MS_OP_RASSERT_P - 从内部 PTR 断言寄存器（Register ASSERT from internal PTR）

用于用内部 PTR 指针当前指向的数据断言寄存器。参数：

- 要写入寄存器的数据量
- 寄存器

预定义宏：MS_RASSERT_P(iter,reg)

### MS_OP_RFETCH_P - 取数据到内部 PTR 的寄存器读取（Register FETCH to internal PTR）

用于从寄存器获取数据。数据存储在内部 PTR 指针当前指向的缓冲区。参数：

- 要从寄存器读取的数据量
- 寄存器
- 应用于所取数据的掩码

预定义宏：MS_RFETCH_P(iter,reg,mask)

### MS_OP_TRIG - 触发寄存器（TRIG register）

用于触发并行端口。此微指令旨在提供对并行端口的非常高效控制。触发寄存器即写入数据、等待片刻、写入数据、等待片刻……这允许向端口写入魔序列。参数：

- 要从寄存器读取的数据量
- 寄存器
- 数组大小
- 无符号字符数组。每对 u_chars 定义要写入寄存器的数据和以 us 为单位的等待延迟。延迟限制为 255 us，以简化并减小数组大小。

预定义宏：MS_TRIG(reg,len,array)

## 微序列

### C 结构

```c
union ppb_insarg {
     int     i;
     char    c;
     void    *p;
     int     (* f)(void *, char *);
};
struct ppb_microseq {
     int                     opcode;         /* 微指令操作码 */
     union ppb_insarg        arg[PPB_MS_MAXARGS];    /* 参数 */
};
```

### 使用微序列

要实例化一个微序列，只需声明一个 ppb_microseq 结构数组并按需初始化。可使用预定义宏，也可根据 ppb_microseq 定义直接编码微指令。例如，

```c
     struct ppb_microseq select_microseq[] = {
	     /* 参数列表
	      */
	     #define SELECT_TARGET    MS_PARAM(0, 1, MS_TYP_INT)
	     #define SELECT_INITIATOR MS_PARAM(3, 1, MS_TYP_INT)
	     /* 向驱动器发送 select 命令 */
	     MS_DASS(MS_UNKNOWN),
	     MS_CASS(H_nAUTO | H_nSELIN |  H_INIT | H_STROBE),
	     MS_CASS( H_AUTO | H_nSELIN |  H_INIT | H_STROBE),
	     MS_DASS(MS_UNKNOWN),
	     MS_CASS( H_AUTO | H_nSELIN | H_nINIT | H_STROBE),
	     /* 现在，等待驱动器就绪 */
	     MS_SET(VP0_SELTMO),
/* loop: */     MS_BRSET(H_ACK, 2 /* ready */),
	     MS_DBRA(-2 /* loop */),
/* error: */    MS_RET(1),
/* ready: */    MS_RET(0)
     };
```

此处部分参数未定义，必须在执行微序列之前填充。为初始化每个微序列，应使用 ppb_MS_init_msq() 函数，如下所示：

```c
     ppb_MS_init_msq(select_microseq, 2,
		     SELECT_TARGET, 1 << target,
		     SELECT_INITIATOR, 1 << initiator);
```

然后执行微序列。

### 微序列器

微序列器在 ppbus 或适配器级别执行（有关 ppbus 系统层的信息，参见 [ppbus(4)](../man4/ppbus.4.md)）。大部分微序列器在 ppc 级别执行，以避免 ppbus 到适配器函数调用的开销。但某些操作（如判断传输是否符合 IEEE1284-1994）在 ppbus 层执行。

## 参见

[ppbus(4)](../man4/ppbus.4.md), [ppc(4)](../man4/ppc.4.md), [ppi(4)](../man4/ppi.4.md)

## 历史

`microseq` 手册页首次出现于 FreeBSD 3.0。

## 作者

本手册页由 Nicolas Souchu 编写。

## 缺陷

仅允许一级子微序列。

触发端口时，允许的最大延迟为 255 us。
