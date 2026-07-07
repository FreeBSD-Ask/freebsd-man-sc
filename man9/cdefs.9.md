# cdefs(9)

`cdefs` — 编译器可移植性宏定义

## 名称

`cdefs`

## 描述

`#include <sys/cdefs.h>` 为编译器、C 语言标准可移植性、POSIX 标准合规性和符号可见性定义宏。它为系统头文件定义了编程接口，以适应 FreeBSD 支持编译的多种环境。它为 FreeBSD 源码定义了便利宏，专门满足基本系统的需求。

这些宏大多仅供 FreeBSD 源码内部使用。它们不打算作为通用可移植性层。

## 支持的编译器

在 FreeBSD 上构建程序所支持的编译器：

| **编译器** | **版本** |
| --- | --- |
| gcc | 9, 10, 11, 12, 13, 14 |
| clang | 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| TinyC (tcc) | 0.9 |
| pcc | 1.1 |

由于测试限制，tcc 和 pcc 可能并不总是可用。

构建 FreeBSD 本身所支持的编译器：

| **编译器** | **支持的主要版本** |
| --- | --- |
| gcc | 12, 13, 14 |
| clang | 16, 17, 18 |

请注意：并非这些编译器的每一个次版本都能工作或受支持。

## 编程环境的宏与魔法

`cdefs` 定义（或不定义）若干宏以提高编译程序的可移植性。这些宏允许在头文件中出现更高级的语言特性。头文件假定编译器接受 C 原型函数声明。它们还假定编译器对所有语言方言接受 ANSI C89 关键字。

### 通用宏

促进多种语言环境和语言方言的通用宏。

在 C 环境中，这些定义为空。在 C++ 环境中，它们将函数声明为具有“C”链接。

| **宏** | **描述** |
| --- | --- |
| `__volatile` | 在 C++ 和 C89 及更新环境中展开为 volatile，在支持此扩展的 ANSI 之前的环境中展开为 `__volatile`，否则为空。 |
| `__inline` | 在 C++ 和 C89 及更新环境中展开为 inline，在支持此扩展的 ANSI 之前的环境中展开为 `__inline`，否则为空。 |
| `__restrict` | 在 C99 及更新环境中展开为 restrict，否则为 `__restrict`。 |
| `__CONCAT` | 用于粘贴两个预处理器标记。 |
| `__STRING` | 用于将参数转换为字符串。 |
| `__BEGIN_DECLS` | 开始一组函数。 |
| `__END_DECLS` | 结束一组函数。 |

### 函数、结构和变量修饰符

| **宏** | **描述** |
| --- | --- |
| `__weak_symbol` | 将符号声明为弱符号 |
| `__dead2` | 函数不会返回 |
| `__pure2` | 函数无副作用 |
| `__unused` | 变量可能未使用（通常是参数），因此不发出警告 |
| `__maybe_unused` | 变量可能未使用（通常是参数），因此不发出警告 |
| `__used` | 函数确实被使用，因此即使看起来未使用也发出它 |
| `__deprecated` | 函数接口已弃用，客户端应迁移到新接口。将向此接口的客户端发出警告。 |
| `__deprecated1(msg)` | 函数接口已弃用，客户端应迁移到新接口。字符串 `msg` 将包含在向此接口客户端发出的警告中。 |
| `__packed` | 结构元素之间不留自然对齐空间。用于与外部协议通信。 |
| `__aligned(x)` | 以字节为单位指定给定字段、结构或变量的最小对齐方式 |
| `__section(x)` | 将函数或变量放置在节 `x` 中 |
| `__writeonly` | 提示变量仅被赋值，但不发出警告。适用于宏以及结果最终用途未知的其他位置。 |
| `__alloc_size(x)` | 函数始终返回至少由参数编号 `x` 确定的字节数 |
| `__alloc_size2(x,n)` | 函数始终返回一个数组，其大小至少为由参数编号 `x` 确定的字节数乘以参数编号 `n` 指定的元素数 |
| `__alloc_align(x)` | 函数返回对齐到 `x` 字节的指针或 `NULL`。 |
| `__min_size` | 声明数组具有特定的最小大小 |
| `__malloc_like` | 函数行为类似“malloc”函数族。 |
| `__pure` | 函数无副作用 |
| `__always_inline` | 调用时始终内联此函数 |
| `__fastcall` | 使用“fastcall”ABI 调用并对此函数进行名称改编。 |
| `__result_use_check` | 如果函数调用者未使用其返回值则发出警告。已过时，请改用 `__nodiscard`。 |
| `__nodiscard` | 等同于标准“[[nodiscard]]”属性。如果应用于函数，当函数调用者未使用其返回值时发出警告。可通过强制转换为 `void` 来抑制警告，或在 C++ 中通过赋值给 `std::ignore`。如果应用于结构、C++ 类或枚举，这适用于返回该类型值 的所有函数。如果应用于 C++ 构造函数，这适用于使用该构造函数创建类的实例。注意，`__nodiscard` 必须出现在函数声明之前。 |
| `__returns_twice` | 多次返回，如 [fork(2)](../sys/fork.2.md) |
| `__unreachable` | 此代码在运行时不可达 |
| `__predict_true(x)` | 向编译器提示 `x` 大多数时候为真。仅当频繁调用的代码段性能得到改善时才应使用。 |
| `__predict_false(x)` | 向编译器提示 `x` 大多数时候为假。仅当频繁调用的代码段性能得到改善时才应使用。 |
| `__null_sentinel` | 可变参数函数包含一个为 NULL 哨兵的参数，用于标记参数结束。 |
| `__exported` | |
| `__hidden` | |
| `__printflike(fmtarg,firstvararg)` | 函数类似于 `printf`，通过 `fmtarg` 指定格式参数，由该格式格式化的参数从 `firstvararg` 开始，0 表示使用 `va_arg` 且无法检查。 |
| `__scanflike(fmtarg,firstvararg)` | 函数类似于 `scanf`，通过 `fmtarg` 指定格式参数，由该格式格式化的参数从 `firstvararg` 开始，0 表示使用 `va_arg` 且无法检查。 |
| `__format_arg(f)` | 指定参数 `f` 包含一个字符串，该字符串在以某种方式转换后将传递给类似 `printf` 或 `scanf` 的函数。 |
| `__strfmonlike(fmtarg,firstvararg)` | 函数类似于 `scanf`，通过 `fmtarg` 指定格式参数，由该格式格式化的参数从 `firstvararg` 开始，0 表示使用 `va_arg` 且无法检查。 |
| `__strtimelike(fmtarg,firstvararg)` | 函数类似于 `scanf`，通过 `fmtarg` 指定格式参数，由该格式格式化的参数从 `firstvararg` 开始，0 表示使用 `va_arg` 且无法检查。 |
| `__printf0like(fmtarg,firstvararg)` | 与 `__printflike` 完全相同，只是 `fmtarg` 可以为 `NULL`。 |
| `__strong_reference(sym,aliassym)` | |
| `__weak_reference(sym,alias)` | |
| `__warn_references(sym,msg)` | |
| `__sym_compat(sym,impl,verid)` | |
| `__sym_default(sym,impl,verid)` | |
| `__GLOBAL(sym)` | |
| `__WEAK(sym)` | |
| `__DECONST(type,var)` | |
| `__DEVOLATILE(type,var)` | |
| `__DEQUALIFY(type,var)` | |
| `__RENAME(x)` | |
| `__arg_type_tag` | |
| `__datatype_type_tag` | |
| `__align_up(x,y)` | |
| `__align_down(x,y)` | |
| `__is_aligned(x,y)` | |

### 锁定和调试宏

用于锁注释和调试的宏，以及一些用于地址消毒器的通用调试宏。

| **宏** | |
| --- | --- |
| `__lock_annotate(x)` | |
| `__lockable` | |
| `__locks_exclusive` | |
| `__locks_shared` | |
| `__trylocks_exclusive` | |
| `__trylocks_shared` | |
| `__unlocks` | |
| `__asserts_exclusive` | |
| `__asserts_shared` | |
| `__requires_exclusive` | |
| `__requires_shared` | |
| `__requires_unlocked` | |
| `__no_lock_analysis` | |
| `__nosanitizeaddress` | |
| `__nosanitizememory` | |
| `__nosanitizethread` | |
| `__nostackprotector` | |
| `__guarded_by(x)` | |
| `__pt_guarded_by(x)` | |

### 模拟关键字

随着 C 的演进，我们曾经使用的许多旧宏已被纳入标准语言。发生这种情况时，我们为旧编译环境添加这些关键字作为宏的支持。有时这会导致在旧环境中为空操作。

| **关键字** | **描述** |
| --- | --- |
| `_Alignas(x)` | |
| `_Alignof(x)` | |
| `_Noreturn` | 在 C++11 及更新编译环境中展开为“[[noreturn]]”，否则为 `__dead2`。 |
| `_Static_assert(x, y)` | 编译时断言 `x` 为真，否则发出 `y` 作为错误消息。 |
| `_Thread_local` | 将变量指定为线程局部存储 |
| `__generic` | 实现类似 `_Generic` 的特性，这些特性无法完全模拟 `_Generic` 关键字 |
| `__noexcept` | 模拟 C++11 无参数 noexcept 形式 |
| `__noexcept_if` | 模拟 C++11 条件 noexcept 形式 |
| `_Nonnull` | |
| `_Nullable` | |
| `_Null_unspecified` | |

### 支持宏

以下宏被定义或具有特定值，以表示有关构建环境的某些事项。

| **宏** | **描述** |
| --- | --- |
| `__LONG_LONG_SUPPORTED` | 变量可声明为“long long”。这为 C99 或更新以及 C++ 环境定义。 |
| `__STDC_LIMIT_MACROS` | |
| `__STDC_CONSTANT_MACROS` | |

### 便利宏

这些宏使许多操作更容易，尽管严格来说标准将它们的常规形式放在另一个头文件中。

| **宏** | **描述** |
| --- | --- |
| `__offsetof(type,field)` | |
| `__rangeof(type,start,end)` | |
| `__containerof(x,s,m)` | |

### ID 字符串

本节已弃用，但保留是因为太多 contrib 软件仍在使用这些。

| **宏** | **描述** |
| --- | --- |
| `__IDSTRING(name,string)` | |
| `__FBSDID(s)` | |
| `__RCSID(s)` | |
| `__RCSID_SOURCE(s)` | |
| `__SCCSID(s)` | |
| `__COPYRIGHT(s)` | |

## 支持的 C 环境

FreeBSD 支持多种 C 标准环境。语言方言的选择是编译器相关的命令行选项，通常为 `-std=XX`，其中 XX 是要设置用于编译的标准，例如 c89 或 c23。FreeBSD 提供了多种选择宏来控制符号的可见性。具体信息请参见选择宏章节。

**K&R**：ANSI 之前的 Kernighan 和 Ritchie C。有时称为“knr”或“C78”以区别于较新的标准。对此编译环境的支持取决于支持此配置的编译器。大多数旧的 C 形式在 ISO C-2023 中已弃用或移除。编译器使在此模式下编译变得越来越困难，对其的支持最终可能从源码树中移除。

**ANSI X3.159-1989 ("ANSI C89")**：定义了 `__STDC__`，但未定义 `__STDC_VERSION__`。通过 `_ANSI_SOURCE` 选择严格环境。

**ISO/IEC 9899:1999 ("ISO C99")**：`__STDC_VERSION__ = 199901L`。通过 `_C99_SOURCE` 选择严格环境。

**ISO/IEC 9899:2011 ("ISO C11")**：`__STDC_VERSION__ = 201112L`。通过 `_C11_SOURCE` 选择严格环境。

**ISO/IEC 9899:2018 ("ISO C17")**：`__STDC_VERSION__ = 201710L`。由于没有新的仅 C17 符号或宏，通过 `_C11_SOURCE` 选择严格环境。此版本的标准未引入任何新特性，仅做了少量技术更正。

**ISO C-2023**：`__STDC_VERSION__ = 202311L`。通过 `_C23_SOURCE` 选择严格环境，尽管 ISO C23 支持仅部分实现。

有关 C 标准的更多信息，请参见 [c(7)](../man7/c.7.md)。

### 编程环境选择宏

定义以下宏请求系统头文件仅提供相应标准定义的函数、结构和宏（符号），同时抑制所有扩展。但是，该标准未定义的系统头文件可能定义扩展。对于任何编译单元，只能定义以下之一。

| **宏** | **环境** |
| --- | --- |
| `_POSIX_SOURCE` | -p1003.1-88，包括 -ansiC |
| `_POSIX_C_SOURCE = 1` | -p1003.1-88，包括 -ansiC |
| `_POSIX_C_SOURCE = 2` | -p1003.1-90，包括 -ansiC |
| `_POSIX_C_SOURCE = 199309` | -p1003.1b-93，包括 -ansiC |
| `_POSIX_C_SOURCE = 199506` | -p1003.1c-95，包括 -ansiC |
| `_POSIX_C_SOURCE = 200112` | -p1003.1-2001，包括 -isoC-99 |
| `_POSIX_C_SOURCE = 200809` | -p1003.1-2008，包括 -isoC-99 |
| `_POSIX_C_SOURCE = 202405` | -p1003.1-2024，包括 ISO/IEC 9899:2018 ("ISO C17") |
| `_XOPEN_SOURCE defined` | -p1003.1-90 和 XPG 扩展到 -susv1，包括 -ansiC。但是，FreeBSD 将此实现为 NOP，因为太多软件在正确的严格环境下会出错。 |
| `_XOPEN_SOURCE = 500` | -p1003.1c-95 和 XPG 扩展到 -susv2，包括 -ansiC |
| `_XOPEN_SOURCE = 600` | -p1003.1-2001 和 XPG 扩展到 -susv3，包括 -isoC-99 |
| `_XOPEN_SOURCE = 700` | -p1003.1-2008 和 XPG 扩展到 -susv4，包括 -isoC-99 |
| `_XOPEN_SOURCE = 800` | -p1003.1-2024 和 XPG 扩展到 Version 5 of the Single UNIX Specification ("SUSv5")，包括 ISO/IEC 9899:2018 ("ISO C17") |
| `_ANSI_SOURCE` | -ansiC |
| `_C99_SOURCE` | -isoC-99 |
| `_C11_SOURCE` | -isoC-2011 |
| `_C23_SOURCE` | -isoC-2023 |
| `_BSD_SOURCE` | 一切，包括 FreeBSD 扩展 |

注意：-p1003.1-2024 和 XPG 扩展到 Version 5 of the Single UNIX Specification ("SUSv5") 的支持不完整。

当同时选择 POSIX 和 C 环境时，POSIX 环境选择使用哪个 C 环境。但是，当 C11 方言与 -p1003.1-2008 一起选择时，还包括 -isoC-2011 的定义。同样，当 C23 方言与 -p1003.1-2008 或 -p1003.1-2024 一起选择时，还包括 -isoC-2023 的定义。

### 头文件可见性宏

这些宏由 `cdefs` 设置以控制不同标准的可见性。用户不得定义这些宏，否则会产生未定义结果。此处为开发系统头文件的开发者记录它们。

| **宏** | **描述** |
| --- | --- |
| `__XSI_VISIBLE` | 限制 XOPEN Single Unix Standard 版本的可见性。可能值为 500、600、700 或 800，对应 Single Unix Standard 的 Issue 5、6、7 或 8。这些是常规 POSIX 之外的额外函数。 |
| `__POSIX_VISIBLE` | 使与某些标准版本关联的符号可见。按约定设置为分配给 `_POSIX_C_SOURCE` 的值，-p1003.1-88 为 199009，-p1003.1-90 为 199209。 |
| `__ISO_C_VISIBLE` | 可见的 C 级别。可能值包括 1990、1999、2011、2017 和 2023，分别对应 -isoC-90、-isoC-99、-isoC-2011、ISO/IEC 9899:2018 ("ISO C17") 和 -isoC-2023。 |
| `__BSD_VISIBLE` | 如果 FreeBSD 扩展可见则为 1，否则为 0。 |
| `__EXT1_VISIBLE` | 如果 -isoC-2011 附录 K 3.7.4.1 扩展可见则为 1，否则为 0。 |

## 支持的 C++ 环境

FreeBSD 完全支持 C++11 及更新标准。

**ISO/IEC 14882:1998 ("C++98")** `__cplusplus = 199711`：C++ 的第一个标准化版本。与 C 中的 K&R 支持不同，编译器放弃了对 C++98 之前语言版本的支持。

**ISO/IEC 14882:2003 ("C++03")** `__cplusplus = 199711`：注意，这与 C++98 的值相同。C++03 未为 `__cplusplus` 定义新值。在编译时无法检测差异。该标准解决了若干缺陷报告并略微扩展了值初始化。大多数编译器与 C++98 相同地支持它。

**ISO/IEC 14882:2011 ("C++11")** `__cplusplus = 201103`

**ISO/IEC 14882:2014 ("C++14")** `__cplusplus = 201402`

**ISO/IEC 14882:2017 ("C++17")** `__cplusplus = 201703`

**ISO/IEC 14882:2020 ("C++20")** `__cplusplus = 202002`

**ISO/IEC 14882:2023 ("C++23")** `__cplusplus = 202302`

FreeBSD 使用 llvm 项目的 libc++。但是，他们正在移除对 C++11 之前 C++ 的支持。虽然程序目前仍可在早期环境中构建，但这些更改意味着对于早于 C++11 的标准，无法可靠地启用 `-pedantic-errors`。

## 历史

`#include <sys/cdefs.h>` 首次出现于 4.3BSD NET/2。
