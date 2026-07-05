# c.7

`c` — C 编程语言

## 名称

`c`, `c78`, `c89`, `c90`, `c95`, `c99`, `c11`, `c17`, `c23`, `c2y`

## 描述

C 是一种通用编程语言，与 UNIX 操作系统及其衍生系统有着密切联系，因为绝大多数这些系统都是用 C 语言编写的。C 语言包含 BCPL 语言的一些基本思想，这些思想通过 Ken Thompson 于 1970 年为 DEC PDP-7 机器编写的 B 语言传入。UNIX 操作系统的开发始于 PDP-7 机器上的汇编语言，但使得将现有代码移植到其他系统变得非常困难。

1972 年，Dennis M. Ritchie 为 UNIX 操作系统的进一步发展制定了 C 编程语言。其理念是仅在不同平台上实现 C 编译器，并用新编程语言实现操作系统的大部分，以简化不同架构间的可移植性。因此，C 非常适合（但不限于）编写操作系统和底层应用程序。

C 语言长期没有规范或标准化版本。它经历了多年的大量更改和改进。1978 年，Brian W. Kernighan 和 Dennis M. Ritchie 以 "The C Programming Language" 为书名出版了第一本关于 C 的书。我们可以将这本书视为该语言的第一个规范。此版本通常以作者姓名缩写称为 K&R C。有时也称为 C78，以该书第一版的出版年份命名。

重要的是要注意，为简化起见，语言的指令集仅限于最基本的元素。标准 I/O 处理和此类常见函数在随编译器提供的库中实现。由于这些函数也被广泛使用，因此需要在描述中包含库应符合的要求，而不仅仅是语言本身。因此，上述标准也涵盖库元素。此标准库的元素对于更复杂的任务仍然不够。在这种情况下，可使用给定操作系统提供的系统调用。为避免使用这些系统调用而失去可移植性，发展出了 POSIX（可移植操作系统接口）标准。它描述了为保持可移植性应可用的函数。注意，POSIX 不是 C 标准，而是操作系统标准，因此超出了本手册的范围。下面讨论的标准均为 C 标准，仅涵盖 C 编程语言和附带库。各标准版本的所列改进均取自官方标准草案。更多细节，请查阅公开可用的草案或购买已发布的标准——从 ISO 或 IEC 资源。

上述书籍出版后，美国国家标准学会（ANSI）开始致力于语言标准化，于 1989 年发布了 ANSI X3.159-1989。通常称为 ANSI C 或 C89。此标准的主要差异是函数原型，这是一种新的函数声明方式。使用旧式函数声明，编译器无法在函数调用时检查实际参数的合理性。旧语法极易出错，因为不兼容的参数难以在程序代码中检测，问题仅在运行时才显现。

1990 年，国际标准化组织（ISO）于 1990 年采用 ANSI 标准作为 ISO/IEC 9899:1990。这也称为 ISO C 或 C90。它仅对 ANSI C 进行了微不足道的微小修改，因此两个标准通常被认为完全等价。这是 C 语言历史上的重要里程碑，但语言的发展并未停止。

ISO C 标准后来通过修正案扩展为 1995 年的 ISO/IEC 9899/AMD1。其中包含例如

`#include <wchar.h>`

和

`#include <wctype.h>`

中的宽字符支持，以及通过二合字母和

`#include <iso646.h>`

支持的受限字符集。此修正案通常称为 C95。还发布了两份技术勘误：1994 年的技术勘误 1（ISO/IEC 9899/COR1）和 1996 年的技术勘误 2（ISO/IEC 9899/COR2）。持续的发展和增长使得有必要制定新标准，包含新特性并修复语言的已知缺陷和不足。结果，1999 年诞生了 ISO/IEC 9899:1999 作为标准的第二版。与其他标准类似，这以出版年份非正式地命名为 C99。改进包括（但不限于）以下内容：

`#include <iso646.h>`

`#include <wchar.h>`

`#include <wctype.h>`

`#include <complex.h>`

`#include <tgmath.h>`

`#include <stdio.h>`

`#include <wchar.h>`

`#include <stdio.h>`

`#include <stdbool.h>`

`#include <stdarg.h>`

- 二合字母、三合字母以及在中使用非 ISO646 字符的运算符的替代拼写
- 和中扩展的多字节和宽字符库支持
- 变长数组
- 灵活数组成员
- 中的复数（和虚数）算术支持
- 中的类型通用数学宏
- long long int 类型和库函数
- 移除隐式 int 类型
- 通用字符名（eu 和 eU）
- 复合字面量
- 移除隐式函数声明
- BCPL 风格的单行注释
- 允许混合声明和代码
- 和中的 Fn vscanf 函数族
- 允许 enum 声明中的尾随逗号
- 内联函数
- 中的 Fn snprintf 函数族
- 中的布尔类型和宏
- 空宏参数
- _Pragma 预处理运算符
- __func__ 预定义标识符
- 中的 va_copy 宏
- 附加 strftime 转换说明符

后来在 2011 年，标准的第三版 ISO/IEC 1989:2011，通常称为 C11（原 C1x），问世，通过 ISO/IEC 9899:1999/COR1:2001、ISO/IEC 9899:1999/COR2:2004 和 ISO/IEC 9899:1999/COR3:2007 替换了第二版。改进包括（但不限于）以下内容：

`#include <threads.h>`

`#include <stdatomic.h>`

`#include <float.h>`

`#include <stdalign.h>`

`#include <stdlib.h>`

`#include <uchar.h>`

`#include <assert.h>`

`#include <stdio.h>`

`#include <stdlib.h>`

- 和中的多线程执行和原子操作支持
- 中的附加浮点特性宏
- 和中的对象对齐查询和指定
- 中的 Unicode 字符类型和函数
- 类型通用表达式
- 中的静态断言
- 匿名结构和联合
- 从中移除 gets 函数
- 在中添加 aligned_alloc、at_quick_exit 和 quick_exit 函数

C11 后来被 ISO/IEC 9899:2018 取代，也称为 C17，于 2017 年准备，2018 年 6 月作为第四版发布。它纳入了 2012 年发布的技术勘误 1（ISO/IEC 9899:2011/COR1:2012）。它解决了 C11 中的缺陷和不足，未引入新特性，仅作更正和澄清。

C23，正式名称为 ISO/IEC 9899:2024，是当前标准，包含取代 C17（ISO/IEC 9899:2018）的重大更新。标准化工作始于 2016 年，非正式名称为 C2x，2019 年举行首次 WG14 会议，并于 2024 年 10 月 31 日正式发布。C23 原本预计更早发布，但由于 COVID-19 大流行而延长了时间表。在 C23 中，__STDC_VERSION__ 的值从 201710L 更新为 202311L。关键更改包括（但不限于）以下内容：

`#include <string.h>`

`#include <string.h>`

`#include <stdlib.h>`

`#include <string.h>`

`#include <stdbit.h>`

`#include <time.h>`

`#include <stdbool.h>`

`#include <stdnoreturn.h>`

- 添加空指针类型 nullptr_t 和 nullptr 关键字
- 添加 constexpr 关键字作为对象的存储类说明符
- 重新定义 auto 关键字的用法以支持类型推断，同时在与类型一起使用时保留其作为存储类说明符的先前功能
- 向 Fn printf 和 Fn scanf 函数族添加 %b 二进制转换说明符
- 向 Fn strtol 和 Fn wcstol 函数族添加二进制转换支持（0b 和 0B）
- 添加 #embed 指令用于二进制资源包含，以及 __has_embed 用于通过预处理指令检查资源可用性
- 添加 #warning 指令用于诊断
- 添加 #elifdef 和 #elifndef 指令
- 为字符字面量添加 u8 前缀以表示 UTF-8 编码，与 C++17 兼容
- 为 UTF-8 编码数据添加 char8_t 类型，并将 u8 字符常量和字符串字面量的类型更新为 char8_t
- 添加函数 Fn mbrtoc8 和 Fn c8rtomb 在窄多字节字符和 UTF-8 编码之间转换
- 将所有 char16_t 字符串和字面量定义为 UTF-16 编码，char32_t 字符串和字面量定义为 UTF-32 编码，除非另有指定
- 允许在复合字面量中使用存储类说明符
- 支持最新 IEEE 754 标准 ISO/IEC 60559:2020，包括二进制和（可选）十进制浮点算术
- 添加单参数 _Static_assert 以兼容 C++17
- 添加 _Decimal32、_Decimal64、_Decimal128 关键字用于（可选）十进制浮点算术
- 为字面量添加数字分隔符 '（单引号字符）
- 允许指定 enum 的基础类型
- 标准化 Fn typeof 运算符
- 在中添加 Fn memset_explicit 以无论优化如何都安全擦除敏感数据
- 在中添加 Fn memccpy 用于高效字符串连接
- 在中添加 Fn memalignment 用于确定指针对齐
- 在中添加 Fn strdup 和 Fn strndup 用于分配字符串副本
- 在新头文件中引入位工具函数、宏和类型
- 在中添加 Fn timegm 用于将时间结构转换为日历时间值
- 添加 __has_include 用于通过预处理指令检查头文件可用性
- 添加 __has_c_attribute 用于通过预处理指令检查属性可用性
- 添加 _BitInt(N) 和 unsigned _BitInt(N) 用于位精确整数，以及 BITINT_MAXWIDTH 用于最大位宽
- 将 true 和 false 提升为适当的关键字（先前为来自的宏）
- 添加关键字 alignas、alignof、bool、static_assert、thread_local；先前定义的关键字仍可作为替代拼写使用
- 启用 {} 零初始化（包括 VLA 的初始化）
- 引入 C++11 风格的属性 [[]]，添加 [[deprecated]]、[[fallthrough]]、[[maybe_unused]]、[[nodiscard]] 和 [[noreturn]]
- 弃用 _Noreturn、noreturn、C11 中引入的头文件特性
- 移除三合字母支持
- 移除 K&R 函数定义和声明
- 移除有符号整数的非二进制补码表示

C 标准的下一个版本，非正式名称为 C2y，预计在未来六年内发布，最迟目标为 2030 年。C2y 的章程仍在起草和讨论中，2024 年 1 月在法国斯特拉斯堡会议上有几份论文正在辩论，表明此新版本可能解决 C 社区注意到的长期请求和不足，同时保留其核心优势。

ISO/IEC JTC1/SC22/WG14 委员会负责 ISO/IEC 9899，即 C 标准。

## 参见

c89(1), c99(1), [cc(1)](../man1/cc.1.md)

## 标准

> ANSI, "X3.159-1989 (aka C89 or ANSI C)".

> ISO/IEC, "9899:1990 (aka C90)".

> ISO/IEC, "9899:1990/AMD 1:1995, Amendment 1: C Integrity (aka C95)".

> ISO/IEC, "9899:1990/COR 1:1994, Technical Corrigendum 1".

> ISO/IEC, "9899:1990/COR 2:1996, Technical Corrigendum 2".

> ISO/IEC, "9899:1999 (aka C99)".

> ISO/IEC, "9899:1999/COR 1:2001, Technical Corrigendum 1".

> ISO/IEC, "9899:1999/COR 2:2004, Technical Corrigendum 2".

> ISO/IEC, "9899:1999/COR 3:2007, Technical Corrigendum 3".

> ISO/IEC, "TR 24731-1:2007 (aka bounds-checking interfaces)".

> ISO/IEC, "TS 18037:2008 (aka, embedded C)".

> ISO/IEC, "TR 24747:2009 (aka mathematical special functions)".

> ISO/IEC, "TR 24732:2009 (aka decimal floating-point)".

> ISO/IEC, "TR 24731-2:2010 (aka dynamic allocation functions)".

> ISO/IEC, "9899:2011 (aka C11)".

> ISO/IEC, "9899:2011/COR 1:2012, Technical Corrigendum 1".

> ISO/IEC, "TS 17961:2013 (aka C secure coding rules)".

> ISO/IEC, "TS 18861-1:2014 (aka binary floating-point)".

> ISO/IEC, "TS 18861-2:2015 (aka decimal floating-point)".

> ISO/IEC, "TS 18861-3:2015 (aka interchange and extended types)".

> ISO/IEC, "TS 18861-4:2015 (aka supplementary functions)".

> ISO/IEC, "TS 17961:2013/COR 1:2016 (aka C secure coding rules TC1)".

> ISO/IEC, "TS 18861-5:2016 (aka supplementary attributes)".

> ISO/IEC, "9899:2018 (aka C17)".

> ISO/IEC, "9899:2024 (aka C23)".

## 历史

本手册页首次出现于 FreeBSD 9.0。

## 作者

本手册页最初由 Gabor Kovesdan <gabor@FreeBSD.org> 编写。由 Faraz Vahedi <kfv@kfv.io> 更新，添加了关于更近期 C 标准的信息。
