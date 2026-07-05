# clang.1

`clang` — Clang C、C++ 和 Objective-C 编译器

## 名称

`clang`

## 概要

`clang [options] filename ...`

## 描述

`clang` 是一个 C、C++ 和 Objective-C 编译器，涵盖预处理、解析、优化、代码生成、汇编和链接。根据传递的高级模式设置不同，Clang 会在执行完整链接之前停止。虽然 Clang 高度集成，但了解编译的各个阶段对正确调用它非常重要。这些阶段包括：

**Driver（驱动器）**

`clang` 可执行文件实际上是一个小型驱动器，控制其他工具（如编译器、汇编器和链接器）的整体执行。通常你不需要直接与驱动器交互，但会透明地使用它来运行其他工具。

**Preprocessing（预处理）**

此阶段处理输入源文件的词法分析、宏展开、`#include` 展开以及其他预处理指令的处理。此阶段的输出通常称为 “`.i`”（C）、“`.ii`”（C++）、“`.mi`”（Objective-C）或 “`.mii`”（Objective-C++）文件。

**Parsing and Semantic Analysis（解析与语义分析）**

此阶段解析输入文件，将预处理词法单元转换为解析树。一旦形成解析树，它会进行语义分析以计算表达式的类型，并确定代码是否格式良好。此阶段负责生成大多数编译器警告和解析错误。此阶段的输出是 “Abstract Syntax Tree”（抽象语法树，AST）。

**Code Generation and Optimization（代码生成与优化）**

此阶段将 AST 转换为低级中间代码（称为 “LLVM IR”），最终转换为机器码。此阶段负责优化生成的代码并处理目标特定的代码生成。此阶段的输出通常称为 “`.s`” 文件或 “assembly”（汇编）文件。

Clang 还支持使用集成汇编器，由代码生成器直接生成目标文件。这避免了生成 “`.s`” 文件和调用目标汇编器的开销。

**Assembler（汇编器）**

此阶段运行目标汇编器，将编译器的输出转换为目标目标文件。此阶段的输出通常称为 “`.o`” 文件或 “object”（目标）文件。

**Linker（链接器）**

此阶段运行目标链接器，将多个目标文件合并为可执行文件或动态库。此阶段的输出通常称为 “`a.out`”、“`.dylib`” 或 “`.so`” 文件。

Clang Static Analyzer

Clang Static Analyzer 是一个通过代码分析扫描源代码以发现 bug 的工具。该工具使用了 Clang 的许多部分，并内置在同一驱动器中。有关如何使用静态分析器的更多详细信息，请参见 <https://clang-analyzer.llvm.org>。

## 选项

### 阶段选择选项

**`-E`** 运行预处理阶段。

**`-fsyntax-only`** 运行预处理、解析和语义分析阶段。

**`-S`** 运行上述阶段以及 LLVM 生成和优化阶段及目标特定的代码生成，生成汇编文件。

**`-c`** 运行上述所有阶段，加上汇编器，生成目标 “`.o`” 目标文件。

**无阶段选择选项** 如果未指定阶段选择选项，则运行上述所有阶段，并运行链接器将结果合并为可执行文件或共享库。

### 语言选择与模式选项

**`-x <language>`** 将后续输入文件视为具有 `language` 类型。

**`-std=<standard>`** 指定要编译的语言标准。

C 语言支持的值为：

- `c89`、`c90`、`iso9899:1990` — ISO C 1990
- `iso9899:199409` — ISO C 1990 with amendment 1
- `gnu89`、`gnu90` — ISO C 1990 with GNU extensions
- `c99`、`iso9899:1999` — ISO C 1999
- `gnu99` — ISO C 1999 with GNU extensions
- `c11`、`iso9899:2011` — ISO C 2011
- `gnu11` — ISO C 2011 with GNU extensions
- `c17`、`iso9899:2017` — ISO C 2017
- `gnu17` — ISO C 2017 with GNU extensions

默认 C 语言标准为 `gnu17`，但在 PS4 上为 `gnu99`。

C++ 语言支持的值为：

- `c++98`、`c++03` — ISO C++ 1998 with amendments
- `gnu++98`、`gnu++03` — ISO C++ 1998 with amendments and GNU extensions
- `c++11` — ISO C++ 2011 with amendments
- `gnu++11` — ISO C++ 2011 with amendments and GNU extensions
- `c++14` — ISO C++ 2014 with amendments
- `gnu++14` — ISO C++ 2014 with amendments and GNU extensions
- `c++17` — ISO C++ 2017 with amendments
- `gnu++17` — ISO C++ 2017 with amendments and GNU extensions
- `c++20` — ISO C++ 2020 with amendments
- `gnu++20` — ISO C++ 2020 with amendments and GNU extensions
- `c++2b` — Working draft for ISO C++ 2023
- `gnu++2b` — Working draft for ISO C++ 2023 with GNU extensions

默认 C++ 语言标准为 `gnu++17`。

OpenCL 语言支持的值为：

- `cl1.0` — OpenCL 1.0
- `cl1.1` — OpenCL 1.1
- `cl1.2` — OpenCL 1.2
- `cl2.0` — OpenCL 2.0

默认 OpenCL 语言标准为 `cl1.0`。

CUDA 语言支持的值为：

- `cuda` — NVIDIA CUDA(tm)

**`-stdlib=<library>`** 指定要使用的 C++ 标准库；支持的选项为 `libstdc++` 和 `libc++`。如果未指定，将使用平台默认值。

**`-rtlib=<library>`** 指定要使用的编译器运行时库；支持的选项为 `libgcc` 和 `compiler-rt`。如果未指定，将使用平台默认值。

**`-ansi`** 与 `-std=c89` 相同。

**`-ObjC`**, **`-ObjC++`** 分别将源输入文件视为 Objective-C 和 Objective-C++ 输入。

**`-trigraphs`** 启用 trigraph。

**`-ffreestanding`** 表示文件应针对独立环境而非宿主环境进行编译。注意，假定独立环境还将提供 `memcpy`、`memmove`、`memset` 和 `memcmp` 实现，因为许多程序的高效代码生成需要这些函数。

**`-fno-builtin`** 禁用对已知库函数（如 `strlen()` 和 `malloc()`）的特殊处理和优化。

**`-fno-builtin-<function>`** 禁用对特定库函数的特殊处理和优化。例如，`-fno-builtin-strlen` 移除对 `strlen()` 库函数的任何特殊处理。

**`-fno-builtin-std-<function>`** 禁用对命名空间 `std` 中特定 C++ 标准库函数的特殊处理和优化。例如，`-fno-builtin-std-move_if_noexcept` 移除对 `std::move_if_noexcept()` 库函数的任何特殊处理。

对于 C++ 标准库在命名空间 `std` 中也提供的 C 标准库函数，请改用 `-fno-builtin-<function>`。

**`-fmath-errno`** 表示数学函数应被视为会更新 `errno`。

**`-fpascal-strings`** 启用对 Pascal 风格字符串的支持，使用 “`\pfoo`”。

**`-fms-extensions`** 启用对 Microsoft 扩展的支持。

**`-fmsc-version=`** 设置 `_MSC_VER`。在 Windows 上默认为 1300。其他情况下不设置。

**`-fborland-extensions`** 启用对 Borland 扩展的支持。

**`-fwritable-strings`** 使所有字符串字面量默认可写。这会禁用字符串的唯一化和其他优化。

**`-flax-vector-conversions`**, **`-flax-vector-conversions=<kind>`**, **`-fno-lax-vector-conversions`** 允许对隐式向量转换使用宽松的类型检查规则。`<kind>` 的可能值：

- `none`：不允许向量之间的任何隐式转换
- `integer`：允许相同总位宽的整数向量之间的隐式位转换
- `all`：允许相同总位宽的任何向量之间的隐式位转换

如果未指定，`<kind>` 默认为 `integer`。

**`-fblocks`** 启用 “Blocks” 语言特性。

**`-fobjc-abi-version=version`** 选择要使用的 Objective-C ABI 版本。可用版本为 1（传统 “fragile” ABI）、2（non-fragile ABI 1）和 3（non-fragile ABI 2）。

**`-fobjc-nonfragile-abi-version=<version>`** 选择默认使用的 Objective-C non-fragile ABI 版本。这仅在启用 non-fragile ABI 时（通过 `-fobjc-nonfragile-abi` 或因为它是平台默认值）用作 Objective-C ABI。

**`-fobjc-nonfragile-abi`**, **`-fno-objc-nonfragile-abi`** 启用 Objective-C non-fragile ABI 的使用。在将其作为默认 ABI 的平台上，可以通过 `-fno-objc-nonfragile-abi` 禁用。

### 目标选择选项

Clang 在设计上完全支持交叉编译。根据你的 Clang 版本配置方式，它可能支持多个交叉编译器，或仅支持本机目标。

**`-arch <architecture>`** 指定要构建的目标架构（Mac OS X 特定）。

**`-target <architecture>`** 指定要构建的目标架构（所有平台）。

**`-mmacosx-version-min=<version>`** 为 macOS 构建时，指定应用程序支持的最低版本。

**`-miphoneos-version-min`** 为 iPhone OS 构建时，指定应用程序支持的最低版本。

**`--print-supported-cpus`** 打印给定目标（通过 `--target=<architecture>` 或 `-arch <architecture>` 指定）支持的处理器列表。如果未指定目标，将使用系统默认目标。

**`-mcpu=?`**, **`-mtune=?`** 作为 `--print-supported-cpus` 的别名。

**`-march=<cpu>`** 指定 Clang 应为特定处理器系列成员及更高版本生成代码。例如，如果指定 `-march=i486`，编译器可以生成在 i486 及更高版本处理器上有效的指令，但这些指令可能在早期处理器上不存在。

### 代码生成选项

**`-O0`**, **`-O1`**, **`-O2`**, **`-O3`**, **`-Ofast`**, **`-Os`**, **`-Oz`**, **`-Og`**, **`-O`**, **`-O4`** 指定要使用的优化级别：

- `-O0` 表示 “无优化”：此级别编译最快，生成的代码最易于调试。
- `-O1` 介于 `-O0` 和 `-O2` 之间。
- `-O2` 中等优化级别，启用大多数优化。
- `-O3` 类似于 `-O2`，但启用的优化耗时更长或可能生成更大的代码（试图让程序运行得更快）。
- `-Ofast` 启用 `-O3` 的所有优化以及其他可能违反严格遵循语言标准的激进优化。
- `-Os` 类似于 `-O2`，但增加减少代码大小的额外优化。
- `-Oz` 类似于 `-Os`（因此也是 `-O2`），但进一步减少代码大小。
- `-Og` 类似于 `-O1`。在将来版本中，此选项可能禁用不同的优化以改善可调试性。
- `-O` 等同于 `-O1`。
- `-O4` 及更高 目前等同于 `-O3`。

**`-g`**, **`-gline-tables-only`**, **`-gmodules`** 控制调试信息输出。注意，Clang 调试信息在 `-O0` 时效果最佳。指定多个以 `-g` 开头的选项时，最后一个生效：

- `-g` 生成调试信息。
- `-gline-tables-only` 仅生成行表调试信息。这允许带有内联信息的符号化回溯，但不包含任何关于变量、其位置或类型的信息。
- `-gmodules` 生成调试信息，其中包含对 Clang 模块或预编译头中定义的类型的外部引用，而不是将冗余的调试类型信息输出到每个目标文件中。此选项透明地将 Clang 模块格式切换为包含 Clang 模块和调试信息的目标文件容器。编译使用 Clang 模块或预编译头的程序时，此选项生成完整的调试信息，编译时间更快，目标文件更小。

此选项不应用于构建要分发给其他机器的静态库，因为调试信息将包含对库中目标文件构建所在机器上模块缓存的引用。

**`-fstandalone-debug`** **`-fno-standalone-debug`** Clang 支持多种优化以减少二进制文件中调试信息的大小。这些优化基于调试类型信息可以分布在多个编译单元中的假设。例如，Clang 不会为模块不需要的类型发出类型定义，可以替换为前向声明。此外，Clang 仅在包含类 vtable 的模块中为动态 C++ 类发出类型信息。

`-fstandalone-debug` 选项关闭这些优化。这在处理不附带调试信息的第三方库时非常有用。这是 Darwin 上的默认选项。注意，Clang 永远不会为程序根本未引用的类型发出类型信息。

**`-feliminate-unused-debug-types`** 默认情况下，Clang 不会为已定义但未在程序中使用的类型发出类型信息。要保留这些未使用类型的调试信息，可以使用反向选项 `-fno-eliminate-unused-debug-types`。

**`-fexceptions`** 启用 unwind 信息生成。这允许异常通过 Clang 编译的栈帧抛出。在 x86-64 上默认启用。

**`-ftrapv`** 生成捕获整数溢出错误的代码。有符号整数溢出在 C 中是未定义行为。使用此标志，会生成额外代码来检测并在发生时中止。

**`-fvisibility`** 此标志设置默认可见性级别。

**`-fcommon`**, **`-fno-common`** 此标志指定没有初始值设定项的变量获得公共链接。可以通过 `-fno-common` 禁用。

**`-ftls-model=<model>`** 设置线程局部变量使用的默认线程局部存储（TLS）模型。有效值为：“global-dynamic”、“local-dynamic”、“initial-exec” 和 “local-exec”。默认值为 “global-dynamic”。默认模型可以通过 `tls_model` 属性覆盖。编译器会在可能的情况下尝试选择更高效的模型。

**`-flto`**, **`-flto=full`**, **`-flto=thin`**, **`-emit-llvm`** 以 LLVM 格式生成输出文件，适用于链接时优化。与 `-S` 一起使用时，生成 LLVM 中间语言汇编文件；否则生成 LLVM bitcode 格式的目标文件（根据阶段选择选项，可能会传递给链接器）。

`-flto` 的默认值为 “full”，其中 LLVM bitcode 适用于整体链接时优化（LTO），链接器将所有此类模块合并为单个组合模块进行优化。使用 “thin” 时，调用 ThinLTO 编译。

注意：在 Darwin 上，将 `-flto` 与 `-g` 一起使用并分步编译和链接时，还需要在链接步骤中传递 `-Wl,-object_path_lto,<lto-filename>.o` 以指示 `ld64` 链接器不要删除链接时优化期间生成的临时目标文件（如果编译和链接在单步中完成，此标志会自动传递给链接器）。这允许调试可执行文件以及使用 dsymutil(1) 生成 `.dSYM` 包。

### 驱动器选项

**`-###`** 打印（但不运行）此编译要运行的命令。

**`--help`** 显示可用选项。

**`-Qunused-arguments`** 不为未使用的驱动器参数发出任何警告。

**`-Wa,<args>`** 将 `args` 中以逗号分隔的参数传递给汇编器。

**`-Wl,<args>`** 将 `args` 中以逗号分隔的参数传递给链接器。

**`-Wp,<args>`** 将 `args` 中以逗号分隔的参数传递给预处理器。

**`-Xanalyzer <arg>`** 将 `arg` 传递给静态分析器。

**`-Xassembler <arg>`** 将 `arg` 传递给汇编器。

**`-Xlinker <arg>`** 将 `arg` 传递给链接器。

**`-Xpreprocessor <arg>`** 将 `arg` 传递给预处理器。

**`-o <file>`** 将输出写入 `file`。

**`-print-file-name=<file>`** 打印 `file` 的完整库路径。

**`-print-libgcc-file-name`** 打印当前使用的编译器运行时库的库路径（“`libgcc.a`” 或 “`libclang_rt.builtins.*.a`”）。

**`-print-prog-name=<name>`** 打印 `name` 的完整程序路径。

**`-print-search-dirs`** 打印用于查找库和程序的路径。

**`-save-temps`** 保存中间编译结果。

**`-save-stats`**, **`-save-stats=cwd`**, **`-save-stats=obj`** 将内部代码生成（LLVM）统计信息保存到当前目录（`-save-stats`/“`-save-stats=cwd`”）或输出文件目录（“`-save-stats=obj`”）中的文件。

**`-integrated-as`**, **`-no-integrated-as`** 分别用于启用和禁用集成汇编器的使用。集成汇编器默认是否启用取决于目标。

**`-time`** 为单个命令计时。

**`-ftime-report`** 打印编译每个阶段的计时摘要。

**`-v`** 显示要运行的命令并使用详细输出。

### 诊断选项

**`-fshow-column`**, **`-fshow-source-location`**, **`-fcaret-diagnostics`**, **`-fdiagnostics-fixit-info`**, **`-fdiagnostics-parseable-fixits`**, **`-fdiagnostics-print-source-range-info`**, **`-fprint-source-range-info`**, **`-fdiagnostics-show-option`**, **`-fmessage-length`** 这些选项控制 Clang 如何打印诊断信息（错误和警告）的详细信息。更多信息请参见 Clang 用户手册。

### 预处理器选项

**`-D<macroname>=<value>`** 向预定义缓冲区添加隐式 `#define`，该缓冲区在源文件预处理之前读取。

**`-U<macroname>`** 向预定义缓冲区添加隐式 `#undef`，该缓冲区在源文件预处理之前读取。

**`-include <filename>`** 向预定义缓冲区添加隐式 `#include`，该缓冲区在源文件预处理之前读取。

**`-I<directory>`** 将指定目录添加到 include 文件的搜索路径中。

**`-F<directory>`** 将指定目录添加到框架 include 文件的搜索路径中。

**`-nostdinc`** 不搜索标准系统目录或编译器内置目录以查找 include 文件。

**`-nostdlibinc`** 不搜索标准系统目录以查找 include 文件，但搜索编译器内置 include 目录。

**`-nobuiltininc`** 不搜索 clang 的内置目录以查找 include 文件。

## 环境变量

**`TMPDIR`**, **`TEMP`**, **`TMP`** 按顺序检查这些环境变量，以确定编译过程中使用的临时文件写入位置。

**`CPATH`** 如果存在此环境变量，它将被视为要添加到默认系统 include 路径列表中的分隔路径列表。分隔符是平台相关的分隔符，与 `PATH` 环境变量中使用的一样。

环境变量中的空组件将被忽略。

**`C_INCLUDE_PATH`**, **`OBJC_INCLUDE_PATH`**, **`CPLUS_INCLUDE_PATH`**, **`OBJCPLUS_INCLUDE_PATH`** 这些环境变量指定附加路径，如同 `CPATH`，但仅在处理相应语言时使用。

**`MACOSX_DEPLOYMENT_TARGET`** 如果未指定 `-mmacosx-version-min`，则从此环境变量读取默认部署目标。此选项仅影响 Darwin 目标。

## 缺陷

要报告 bug，请访问 <https://github.com/llvm/llvm-project/issues/>。大多数 bug 报告应包括预处理源文件（使用 `-E` 选项）和编译器的完整输出，以及重现信息。

## 参见

as(1), ld(1)

## 作者

由 Clang / LLVM 团队维护（<http://clang.llvm.org>）

## 版权

2007-2023, The Clang Team
