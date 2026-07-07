# getcap(3)

`cgetent` — capability 数据库访问例程

## 名称

`cgetent`, `cgetset`, `cgetmatch`, `cgetcap`, `cgetnum`, `cgetstr`, `cgetustr`, `cgetfirst`, `cgetnext`, `cgetclose`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
cgetent(char **buf, char **db_array, const char *name);

int
cgetset(const char *ent);

int
cgetmatch(const char *buf, const char *name);

char *
cgetcap(char *buf, const char *cap, int type);

int
cgetnum(char *buf, const char *cap, long *num);

int
cgetstr(char *buf, const char *cap, char **str);

int
cgetustr(char *buf, const char *cap, char **str);

int
cgetfirst(char **buf, char **db_array);

int
cgetnext(char **buf, char **db_array);

int
cgetclose(void);
```

## 描述

`cgetent` 函数从由 `NULL` 终止的文件数组 `db_array` 指定的数据库中提取能力 `name`，并在 `buf` 中返回指向其 malloc(3) 分配副本的指针。`cgetent` 函数会先查找以 `.db` 结尾的文件（参见 cap_mkdb(1)），然后再访问 ASCII 文件。`buf` 参数必须在后续对 `cgetmatch`、`cgetcap`、`cgetnum`、`cgetstr` 和 `cgetustr` 的所有调用中保留，但之后可以 free(3) 释放。成功时返回 0，如果返回的记录包含未解析的 `tc` 扩展则返回 1，如果找不到请求的记录则返回 -1，如果遇到系统错误（无法打开/读取文件等）则返回 -2 并设置 `errno`，如果检测到潜在的引用循环（参见下文 `tc=` 注释）则返回 -3。

`cgetset` 函数允许向能力数据库添加一个包含单条能力记录条目的字符缓冲区。从概念上讲，该条目作为数据库中的第一个"文件"添加，因此在调用 `cgetent` 时会首先搜索它。条目通过 `ent` 传递。如果 `ent` 为 `NULL`，则从数据库中移除当前条目。调用 `cgetset` 必须在数据库遍历之前进行。它必须在 `cgetent` 调用之前调用。如果正在执行顺序访问（参见下文），它必须在第一次顺序访问调用（`cgetfirst` 或 `cgetnext`）之前调用，或者直接在 `cgetclose` 调用之后进行。成功时返回 0，失败时返回 -1。

`cgetmatch` 函数在 `name` 是能力记录 `buf` 的名称之一时返回 0，否则返回 -1。

`cgetcap` 函数在能力记录 `buf` 中搜索类型为 `type` 的能力 `cap`。`type` 使用任意单个字符指定。如果使用冒号（`:`），则搜索无类型能力（类型的说明参见下文）。成功时返回指向 `buf` 中 `cap` 值的指针，如果找不到请求的能力则返回 `NULL`。能力值的末尾由 `:` 或 ASCII `NUL` 标记（能力数据库语法参见下文）。

`cgetnum` 函数从 `buf` 指向的能力记录中获取数值能力 `cap` 的值。数值在 `num` 指向的 `long` 中返回。成功时返回 0，如果找不到请求的数值能力则返回 -1。

`cgetstr` 函数从 `buf` 指向的能力记录中获取字符串能力 `cap` 的值。在 `str` 指向的 `char *` 中返回指向解码后的、以 `NUL` 终止的 malloc(3) 分配副本的指针。成功时返回解码字符串中的字符数（不包括末尾的 `NUL`），如果找不到请求的字符串能力则返回 -1，如果遇到系统错误（存储分配失败）则返回 -2。

`cgetustr` 函数与 `cgetstr` 相同，只是它不展开特殊字符，而是按原样返回能力字符串中的每个字符。

`cgetfirst` 和 `cgetnext` 函数组成一个函数组，提供对以 `NULL` 指针终止的文件名数组 `db_array` 的顺序访问。`cgetfirst` 函数返回数据库中的第一条记录并重置访问到第一条记录。`cgetnext` 函数返回数据库中相对于前一次 `cgetfirst` 或 `cgetnext` 调用返回记录的下一条记录。如果之前没有这样的调用，则返回数据库中的第一条记录。每条记录在 `buf` 指向的 malloc(3) 分配副本中返回。`tc` 扩展会执行（参见下文 `tc=` 注释）。数据库遍历完成时返回 0，成功返回记录且可能还有更多记录（尚未到达数据库末尾）时返回 1，如果记录包含未解析的 `tc` 扩展则返回 2，如果发生系统错误则返回 -1，如果检测到潜在的引用循环（参见下文 `tc=` 注释）则返回 -2。数据库遍历完成（返回 0）时，数据库会被关闭。

`cgetclose` 函数关闭顺序访问并释放使用的所有内存和文件描述符。注意，它不会清除由 `cgetset` 调用压入的缓冲区。

## 能力数据库语法

能力数据库通常为 ASCII 格式，可使用标准文本编辑器编辑。空行和以 `#` 开头的行是注释，会被忽略。以 `\` 结尾的行表示下一行是当前行的续行；`\` 和随后的换行符会被忽略。长行通常通过在除最后一行外的每行末尾加 `\` 来延续到多个物理行上。

能力数据库由一系列记录组成，每个逻辑行一条记录。每条记录包含数量可变的以 `:` 分隔的字段（能力）。完全由空白字符（空格和制表符）组成的空字段会被忽略。

每条记录的第一个能力指定其名称，名称之间用 `|` 字符分隔。这些名称用于引用数据库中的记录。按照惯例，最后一个名称通常是注释，不作为查找标签。例如，termcap(5) 数据库中的 *vt100* 记录开头为：

```sh
d0|vt100|vt100-am|vt100am|dec vt100:
```

给出了四个可用于访问该记录的名称。

其余非空能力描述了一组（名称，值）绑定，由名称后可选地跟一个有类型的值组成：

- **name** — 无类型 [布尔] 能力 *name* 存在 [为真]
- **name** *T* *value* — 能力（*name*, *T*）的值为 *value*
- **name@** — 不存在能力 *name*
- **name** *T* @ — 不存在能力（*name*, *T*）

名称由一个或多个字符组成。名称可以包含除 `:` 外的任何字符，但通常最好将其限制为可打印字符，避免使用 `#`、`=`、`%`、`@` 等图形字符。类型是用于分隔能力名称及其关联的类型值的单个字符。类型可以是除 `:` 外的任何字符。通常使用 `#`、`=`、`%` 等图形字符。值可以是任意数量的字符，可以包含除 `:` 外的任何字符。

## 能力数据库语义

能力记录描述了一组（名称，值）绑定。名称可以绑定多个值。名称的不同值通过其 `类型` 区分。`cgetcap` 函数在给定能力名称和值类型时返回指向该名称值的指针。

类型 `#` 和 `=` 按惯例用于表示数值和字符串类型的值，但不强制限制这些类型。`cgetnum` 和 `cgetstr` 函数可用于实现 `#` 和 `=` 的传统语法和语义。无类型能力通常用于表示布尔对象，存在表示为真，不存在表示为假。这种解释可方便地表示为：

```c
(getcap(buf, name, ':') != NULL)
```

一种特殊能力 `tc=name` 用于指示由 `name` 指定的记录应替换 `tc` 能力。`tc` 能力可以插入同样包含 `tc` 能力的记录，一条记录中可以使用多个 `tc` 能力。`tc` 扩展范围（即搜索参数的位置）包含声明 `tc` 的文件以及文件数组中的所有后续文件。

在数据库中搜索能力记录时，返回搜索中第一条匹配的记录。在扫描记录的能力时，返回第一条匹配的能力；能力 `:nameT@:` 会隐藏 `name` 类型为 *T* 的任何后续值定义；能力 `:name@:` 会阻止 `name` 的任何后续值被看到。

这些功能与 `tc` 能力结合，可以通过添加新能力、用新定义覆盖现有定义，或通过 `@` 能力隐藏后续定义来生成其他数据库和记录的变体。

## 实例

```sh
example|an example of binding multiple values to names:\
	:foo%bar:foo^blah:foo@:\
	:abc%xyz:abc^frap:abc$@:\
	:tc=more:
```

能力 foo 绑定了两个值（类型为 `%` 的 bar 和类型为 `^` 的 blah），其他值绑定被隐藏。能力 abc 也绑定了两个值，但只有类型为 `$` 的值被阻止在能力记录 more 中定义。

```sh
file1:
 	new|new_record|a modification of "old":\
		:fript=bar:who-cares@:tc=old:blah:tc=extensions:
file2:
	old|old_record|an old database record:\
		:fript=foo:who-cares:glork#200:
```

记录通过调用 `cgetent` 提取，file1 在 file2 之前。在 file1 的能力记录 new 中，fript=bar 覆盖了从 file2 的能力记录 old 中插入的 fript=foo 定义，who-cares@ 阻止 old 中的任何 who-cares 定义被看到，glork#200 继承自 old，blah 和记录 extensions 定义的任何内容都被添加到 old 的定义中。注意，fript=bar 和 who-cares@ 定义在 tc=old 之前的位置在此很重要。如果它们在之后，old 中的定义将优先。

## cgetnum 与 cgetstr 的语法和语义

`cgetnum` 和 `cgetstr` 预定义了两种类型：

- ***name*#*number*** — 数值能力 *name* 的值为 *number*
- ***name*=*string*** — 字符串能力 *name* 的值为 *string*
- ***name*#@** — 数值能力 *name* 不存在
- ***name*=@** — 字符串能力 *name* 不存在

数值能力的值可以用三种进制之一给出。如果数字以 `0x` 或 `0X` 开头，则解释为十六进制数（大小写 a-f 均可用于表示扩展的十六进制数字）。否则，如果数字以 `0` 开头，则解释为八进制数。否则，数字解释为十进制数。

字符串能力的值可以包含任何字符。不可打印的 `ASCII` 码、换行符和冒号可以使用转义序列方便地表示：

- `^X`（'X' & 037）— control-X
- `\b`、`\B`（ASCII 010）— 退格
- `\t`、`\T`（ASCII 011）— 制表符
- `\n`、`\N`（ASCII 012）— 换行
- `\f`、`\F`（ASCII 014）— 换页
- `\r`、`\R`（ASCII 015）— 回车
- `\e`、`\E`（ASCII 027）— 转义
- `\c`、`\C`（:）— 冒号
- `\\`（\）— 反斜杠
- `\^`（^）— 脱字符
- `\nnn`（ASCII 八进制 nnn）— 对应字符

`\` 后可跟最多三个八进制数字，直接指定字符的数字代码。使用 ASCII `NUL` 虽然容易编码，但会导致各种问题，必须谨慎使用，因为 `NUL` 通常用于表示字符串的结束；许多应用程序使用 `\200` 来表示 `NUL`。

## 诊断

`cgetent`、`cgetset`、`cgetmatch`、`cgetnum`、`cgetstr`、`cgetustr`、`cgetfirst` 和 `cgetnext` 函数成功时返回大于或等于 0 的值，失败时返回小于 0 的值。`cgetcap` 函数成功时返回字符指针，失败时返回 `NULL`。

`cgetent` 和 `cgetset` 函数可能失败并为以下库函数指定的任何错误设置 `errno`：[fopen(3)](../stdio/fopen.3.md)、[fclose(3)](../stdio/fclose.3.md)、[open(2)](../sys/open.2.md) 和 [close(2)](../sys/close.2.md)。

`cgetent`、`cgetset`、`cgetstr` 和 `cgetustr` 函数可能失败并如下设置 `errno`：

**`ENOMEM`** 无可用内存。

## 参见

cap_mkdb(1), malloc(3)

## 缺陷

冒号（`:`）不能用于名称、类型或值中。

`cgetent` 不检查 `tc=name` 循环。

由 `cgetset` 调用添加到数据库的缓冲区并非该数据库独有，而是添加到使用的任何数据库前。
