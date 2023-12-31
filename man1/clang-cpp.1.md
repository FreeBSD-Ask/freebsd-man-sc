  CLANG(1)  

CLANG(1)

Clang

CLANG(1)

[名称](#__u540D___u79F0_)
=======================

clang - Clang C、C++ 和 Objective-C 编译器

[概要](#__u6982___u8981_)
=======================

**clang** \[_options_\] _filename ..._

[描述](#__u63CF___u8FF0_)
=======================

**clang** 是一个 C、C++ 和 Objective-C 编译器，它包含预处理、解析、优化、代码生成、汇编和链接。 根据传递的高级模式设置，Clang 将在执行完整链接之前停止。 虽然 Clang 是高度集成的，但了解编译的各个阶段以及如何调用它很重要。这些阶段是：

**驱动**

clang 可执行文件实际上是一个小型驱动程序，它控制其他工具（例如编译器、汇编器和链接器）的整体执行。 通常您不需要与驱动程序交互，但您可以透明地使用它来运行其他工具。

**预处理**

此阶段处理输入源文件的标记化、宏扩展、#include 扩展和其他预处理器指令的处理。 此阶段的输出通常称为 ".i" (用于 C)、 ".ii" (用于 C++)、 ".mi" (用于 Objective-C) 或 ".mii" (用于 Objective-C++) 文件。

**解析和语义分析**

此阶段解析输入文件，将预处理器标记转换为解析树。 一旦以解析树的形式出现，它还会应用语义分析来计算表达式的类型，并确定代码是否格式正确。 此阶段负责生成大部分编译器警告以及解析错误。 这个阶段的输出是一个 an "抽象语法树" (AST).

**代码生成和优化**

此阶段将 AST 转换为低级中间代码（称为 "LLVM IR") 并最终转换为机器代码。 此阶段负责优化生成的代码并处理特定于目标的代码生成。 此阶段的输出通常称为 ".s" 文件或"assembly" 文件。

Clang 还支持使用集成汇编器，其中代码生成器直接生成目标文件。 这避免了生成 ".s" 文件和调用目标汇编程序的开销。

**汇编器**

此阶段运行目标汇编器以将编译器的输出转换为目标目标文件。 此阶段的输出通常称为 ".o" 文件或 "object" 文件。

**链接器**

此阶段运行目标链接器以将多个目标文件合并到一个可执行文件或动态库中。 此阶段的输出通常称为 "a.out"、 ".dylib" 或 ".so" 文件。

-

**Clang 静态分析器**

静态分析器是一种扫描源代码以尝试通过代码分析发现错误的工具。 该工具使用了 Clang 的许多部分，并内置在同一个驱动程序中。 有关如何使用静态分析器的更多详细信息，请参阅 <_https://clang-analyzer.llvm.org_\> 。

[选项](#__u9009___u9879_)
=======================

[阶段 选择选项](#__u9636___u6BB5____u9009___u62E9___u9009___u9879_)
-------------------------------------------------------------

**\-E**

运行预处理器阶段。

-

**\-fsyntax-only**

运行预处理器、解析器和类型检查阶段。

-

**\-S**

运行前面的阶段以及 LLVM 生成和优化阶段以及特定于目标的代码生成，生成汇编文件。

-

**\-c**

运行上述所有程序，加上汇编程序，生成目标 ".o" 目标文件。

-

**no stage selection option**

如果未指定阶段选择选项，则运行上述所有阶段，并运行链接器以将结果组合到可执行文件或共享库中。

-

[语言选择和模式选项](#__u8BED___u8A00___u9009___u62E9___u548C___u6A21___u5F0F___u9009___u9879_)
--------------------------------------------------------------------------------------

**\-x <language>**

将后续输入文件视为具有类型语言。

-

**\-std=<standard>**

指定要编译的语言标准。

C 语言支持的值为：

**c89** **c90** **iso9899:1990** 

ISO C 1990

-

-

**iso9899:199409** 

ISO C 1990 修订版 1

-

-

**gnu89** **gnu90** 

带有 GNU 扩展的 ISO C 1990

-

-

**c99** **iso9899:1999** 

ISO C 1999

-

-

**gnu99** 

具有 GNU 扩展的 ISO C 1999

-

-

**c11** **iso9899:2011** 

ISO C 2011

-

-

**gnu11** 

带有 GNU 扩展的 ISO C 2011

-

-

**c17** **iso9899:2017** 

ISO C 2017

-

-

**gnu17** 

具有 GNU 扩展的 ISO C 2017

-

-

-

-

默认的 C 语言标准是 **gnu11**, 但在 PS4 上是 **gnu99** 。

C++ 语言支持的值为：

**c++98** **c++03** 

ISO C++ 1998 及修正

-

-

**gnu++98** **gnu++03** 

ISO C++ 1998 与修正和 GNU 扩展

-

-

**c++11** 

ISO C++ 2011 修订版

-

-

**gnu++11** 

带有修正和 GNU 扩展的 ISO C++ 2011

-

-

**c++14** 

ISO C++ 2014 修订版

-

-

**gnu++14** 

带有修正和 GNU 扩展的 ISO C++ 2014

-

-

**c++17** 

ISO C++ 2017 修订版

-

-

**gnu++17** 

带有修正和 GNU 扩展的 ISO C++ 2017

-

-

**c++2a** 

ISO C++ 2020 工作草案

-

-

**gnu++2a** 

具有 GNU 扩展的 ISO C++ 2020 工作草案

-

-

-

-

默认的 C++ 语言标准是 **gnu++14**.

OpenCL 语言支持的值为：

**cl1.0** 

OpenCL 1.0

-

-

**cl1.1** 

OpenCL 1.1

-

-

**cl1.2** 

OpenCL 1.2

-

-

**cl2.0** 

OpenCL 2.0

-

-

-

-

默认的 OpenCL 语言标准是 **cl1.0** 。

CUDA 语言支持的值为：

**cuda** 

NVIDIA CUDA(tm)

-

-

-

-

-

**\-stdlib=<library>**

指定要使用的 C++ 标准库；支持的选项是 libstdc++ 和 libc++。 如果未指定，将使用平台默认值。

-

**\-rtlib=<library>**

指定要使用的编译器运行时库；支持的选项是 libgcc 和 compiler-rt。 如果未指定，将使用平台默认值。

-

**\-ansi**

与 -std=c89 相同

-

**\-ObjC, -ObjC++**

将源输入文件分别视为 Objective-C 和 Object-C++ 输入。

-

**\-trigraphs**

启用三元组。

-

**\-ffreestanding**

指示该文件应针对独立环境而非托管环境进行编译。

-

**\-fno-builtin**

禁用 **strlen()** 和 **malloc()** 等内置函数的特殊处理和优化。

-

**\-fmath-errno**

表示数学函数应被视为更新 **errno** 。

-

**\-fpascal-strings**

使用 "\\pfoo" 启用对 Pascal 样式字符串的支持。

-

**\-fms-extensions**

启用对 Microsoft 扩展的支持。

-

**\-fmsc-version=**

设置\_MSC\_VER。 在 Windows 上默认为 1300。 否则不设置。

-

**\-fborland-extensions**

启用对 Borland 扩展的支持。

-

**\-fwritable-strings**

使所有字符串文字默认为可写。 这会禁用字符串的唯一性和其他优化。

-

**\-flax-vector-conversions, -flax-vector-conversions=<kind>, -fno-lax-vector-conversions**

允许隐式向量转换的松散类型检查规则。 <种类> 的可能值：

*   **none**: 不允许向量之间的隐式转换
*   **integer**: 允许在具有相同整体位宽的整数向量之间进行隐式位广播
*   **all**: 允许在具有相同整体位宽的任何向量之间进行隐式位广播

-

<kind> 如果未指定，则默认为 **integer** 。

-

**\-fblocks**

启用 "Blocks" 语言功能。

-

**\-fobjc-abi-version=version**

选择要使用的 Objective-C ABI ABI 版本。 可用版本为 1（传统 "fragile" ABI)、2（非脆弱 ABI 1）和 3（非脆弱 ABI 2）。

-

**\-fobjc-nonfragile-abi-version=<version>**

选择默认使用的 Objective-C 非脆弱 ABI 版本。 仅当启用非易碎 ABI 时（通过 _\-fobjc-nonfragile-abi_ 或因为它是平台默认设置），它才会用作 Objective-C ABI 。

-

**\-fobjc-nonfragile-abi, -fno-objc-nonfragile-abi**

启用 Objective-C 非脆弱 ABI。 在这是默认 ABI 的平台上，可以使用 _\-fno-objc-nonfragile-abi_ 禁用它。

-

[目标选择选项](#__u76EE___u6807___u9009___u62E9___u9009___u9879_)
-----------------------------------------------------------

Clang 完全支持交叉编译作为其设计的固有部分。 根据您的 Clang 版本的配置方式，它可能支持许多交叉编译器，或者可能只支持本机目标。

**\-arch <architecture>**

指定要构建的架构。

-

**\-mmacosx-version-min=<version>**

为 macOS 构建时，请指定应用程序支持的最低版本。

-

**\-miphoneos-version-min**

为 iPhone OS 构建时，请指定应用程序支持的最低版本。

-

**\--print-supported-cpus**

打印给定目标的支持处理器列表（通过 --target=<architecture> 或 -arch <architecture> 指定）。 如果未指定目标，将使用系统默认目标。

-

**\-mcpu=?, -mtune=?**

\--print-supported-cpus 的别名

-

**\-march=<cpu>**

指定 Clang 应为特定处理器系列成员及更高版本生成代码。 例如，如果您指定 -march=i486，则允许编译器生成在 i486 和更高版本处理器上有效但在更早版本处理器上可能不存在的指令。

-

[代码生成选项](#__u4EE3___u7801___u751F___u6210___u9009___u9879_)
-----------------------------------------------------------

**\-O0, -O1, -O2, -O3, -Ofast, -Os, -Oz, -Og, -O, -O4**

指定要使用的优化级别：

_\-O0_ 表示 "no optimization": 此级别编译速度最快并生成最可调试的代码。

_\-O1_ 介于 _\-O0_ 和 _\-O2_ 之间。

_\-O2_ 中等优化级别，可实现大多数优化。

_\-O3_ 与 _\-O2_ 类似，不同之处在于它启用了需要更长时间执行或可能生成更大代码的优化（以试图使程序运行得更快）

_\-Ofast_ 启用 _\-O3_ 的所有优化以及其他可能违反严格遵守语言标准的积极优化。

_\-Os_ 与 _\-O2_ 类似，具有额外的优化以减少代码大小。

_\-Oz_ 与 _\-Os_ 类似（因此也与 _\-O2_ 类似），但进一步减小了代码大小。

_\-Og_ 与 _\-O1_ 类似。在未来的版本中，此选项可能会禁用不同的优化以提高可调试性。

_\-O_ 相当于 _\-O2_ 。

_\-O4_ 及以上

目前相当于 _\-O3_

-

-

-

-

-

**\-g, -gline-tables-only, -gmodules**

控制调试信息输出。 请注意，Clang 调试信息在 _\-O0_ 时效果最好。 当指定了多个以 _\-g_ 开头的选项时，最后一个获胜：

**\-g** 生成调试信息。

**\-gline-tables-only** 仅生成行表调试信息。 这允许带有内联信息的符号化回溯，但不包括有关变量、它们的位置或类型的任何信息。

_\-gmodules_ 生成包含对 Clang 模块或预编译头文件中定义的类型的外部引用的调试信息，而不是将冗余的调试类型信息发送到每个目标文件中。 此选项透明地将 Clang 模块格式切换到将 Clang 模块与调试信息一起保存的目标文件容器。 编译使用 Clang 模块或预编译头文件的程序时，此选项会生成完整的调试信息，编译时间更快，目标文件更小。

在构建静态库以分发到其他机器时不应使用此选项，因为调试信息将包含对构建库中的目标文件的机器上的模块缓存的引用。

-

-

-

**\-fstandalone-debug -fno-standalone-debug**

Clang 支持许多优化以减少二进制文件中调试信息的大小。 它们的工作基于调试类型信息可以分布在多个编译单元上的假设。 例如，Clang 不会为模块不需要的类型发出类型定义，并且可以用前向声明替换。 此外，Clang 只会为包含类的 vtable 的模块中的动态 C++ 类发出类型信息。

**\-fstandalone-debug** 选项关闭这些优化。 这在使用不附带调试信息的 3rd 方库时很有用。 这是达尔文的默认设置。 请注意，Clang 永远不会为程序根本没有引用的类型发出类型信息。

-

**\-fexceptions**

启用展开信息的生成。 这允许通过 Clang 编译的堆栈帧抛出异常。 这是在 x86-64 中默认开启的。

-

**\-ftrapv**

生成代码以捕获整数溢出错误。 有符号整数溢出在 C 中未定义。 使用这个标志，会生成额外的代码来检测它并在它发生时中止。

-

**\-fvisibility**

此标志设置默认可见性级别。

-

**\-fcommon, -fno-common**

此标志指定没有初始化程序的变量获得公共链接。 可以使用 _\-fno-common_ 禁用它。

-

**\-ftls-model=<model>**

设置用于线程局部变量的默认线程局部存储 (TLS) 模型。 有效值为： "global-dynamic"、 "local-dynamic"、 "initial-exec" 和 "local-exec" 。 默认值为 "global-dynamic" 。 可以使用 tls\_model 属性覆盖默认模型。 如果可能，编译器将尝试选择更有效的模型。

-

**\-flto, -flto=full, -flto=thin, -emit-llvm**

生成 LLVM 格式的输出文件，适用于链接时间优化。 当与 _\-S_ 一起使用时，这会生成 LLVM 中间语言汇编文件，否则会生成 LLVM 位码格式的目标文件（可能会根据阶段选择选项传递给链接器）。

_\-flto_ 的默认值为 "full" ，其中 LLVM 位码适用于单片链接时间优化 (LTO)，其中链接器将所有此类模块合并为单个组合模块以进行优化。 使用 "thin" 时，会改为调用 ThinLTO 编译。

-

[驱动程序选项](#__u9A71___u52A8___u7A0B___u5E8F___u9009___u9879_)
-----------------------------------------------------------

**\-###**

打印（但不运行）为此编译运行的命令。

-

**\--help**

显示可用选项。

-

**\-Qunused-arguments**

不要为未使用的驱动程序参数发出任何警告。

-

**\-Wa,<args>**

将 args 中逗号分隔的参数传递给汇编器。

-

**\-Wl,<args>**

将 args 中逗号分隔的参数传递给链接器。

-

**\-Wp,<args>**

将 args 中逗号分隔的参数传递给预处理器。

-

**\-Xanalyzer <arg>**

将 arg 传递给静态分析器。

-

**\-Xassembler <arg>**

将 arg 传递给汇编程序。

-

**\-Xlinker <arg>**

将 arg 传递给链接器。

-

**\-Xpreprocessor <arg>**

将 arg 传递给预处理器。

-

**\-o <file>**

将输出写入文件。

-

**\-print-file-name=<file>**

打印文件的完整库路径。

-

**\-print-libgcc-file-name**

打印当前使用的编译器运行时库的库路径 ("libgcc.a" 或 "libclang\_rt.builtins.\*.a")。

-

**\-print-prog-name=<name>**

打印名称的完整程序路径。

-

**\-print-search-dirs**

打印用于查找库和程序的路径。

-

**\-save-temps**

保存中间编译结果。

-

**\-save-stats, -save-stats=cwd, -save-stats=obj**

将内部代码生成 (LLVM) 统计信息保存到当前目录 (_\-save-stats_/"-save-stats=cwd") 或输出文件目录 ("-save-state=obj") 中的文件。

-

**\-integrated-as, -no-integrated-as**

用于分别启用和禁用集成汇编程序的使用。 默认情况下是否打开集成汇编器取决于目标。

-

**\-time**

计时单个命令。

-

**\-ftime-report**

打印每个编译阶段的时序摘要。

-

**\-v**

显示命令以运行和使用详细输出。

-

[诊断选项](#__u8BCA___u65AD___u9009___u9879_)
-----------------------------------------

**\-fshow-column, -fshow-source-location, -fcaret-diagnostics, -fdiagnostics-fixit-info, -fdiagnostics-parseable-fixits, -fdiagnostics-print-source-range-info, -fprint-source-range-info, -fdiagnostics-show-option, -fmessage-length**

这些选项控制 Clang 如何打印有关诊断（错误和警告）的信息。 请参阅 Clang 用户手册了解更多信息。

-

[预处理器选项](#__u9884___u5904___u7406___u5668___u9009___u9879_)
-----------------------------------------------------------

**\-D<macroname>=<value>**

将隐式 #define 添加到预定义缓冲区中，在预处理源文件之前读取该缓冲区。

-

**\-U<macroname>**

将隐式 #undef 添加到预定义缓冲区中，在预处理源文件之前读取该缓冲区。

-

**\-include <filename>**

将隐式 #include 添加到预定义缓冲区中，在预处理源文件之前读取该缓冲区。

-

**\-I<directory>**

将指定目录添加到包含文件的搜索路径。

-

**\-F<directory>**

将指定目录添加到框架包含文件的搜索路径。

-

**\-nostdinc**

不要在标准系统目录或编译器内置目录中搜索包含文件。

-

**\-nostdlibinc**

不要在标准系统目录中搜索包含文件，但要搜索编译器内置的包含目录。

-

**\-nobuiltininc**

不要在 clang 的内置目录中搜索包含文件。

-

[环境](#__u73AF___u5883_)
=======================

**TMPDIR, TEMP, TMP**

依次检查这些环境变量，以确定在编译过程中写入临时文件的位置。

-

**CPATH**

如果存在此环境变量，则将其视为要添加到默认系统包含路径列表的分隔路径列表。 分隔符是与平台相关的分隔符，在 PATH 环境变量中使用。

环境变量中的空组件将被忽略。

-

**C\_INCLUDE\_PATH, OBJC\_INCLUDE\_PATH, CPLUS\_INCLUDE\_PATH, OBJCPLUS\_INCLUDE\_PATH**

这些环境变量指定了额外的路径，就像 _CPATH_ 一样，它们只在处理适当的语言时使用。

-

**MACOSX\_DEPLOYMENT\_TARGET**

如果未指定 _\-mmacosx-version-min_ ，则从此环境变量中读取默认部署目标。 此选项仅影响达尔文目标。

-

[缺陷](#__u7F3A___u9677_)
=======================

要报告错误，请访问 <_https://bugs.llvm.org/_\> 。 大多数错误报告应包括预处理的源文件（使用 _\-E_ 选项）和编译器的完整输出，以及要重现的信息。

[参见](#__u53C2___u89C1_)
=======================

**as(1)**, **ld(1)**

[作者](#__u4F5C___u8005_)
=======================

由 Clang / LLVM 团队维护 (<http://clang.llvm.org>)

[版权](#__u7248___u6743_)
=======================

2007-2020, Clang 团队

2020-06-26

10