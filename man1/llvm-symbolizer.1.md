# llvm-symbolizer(1)

`llvm-symbolizer` — 将地址转换为源代码位置

## 名称

`llvm-symbolizer`

## 概要

`llvm-symbolizer [options] [addresses...]`

## 描述

`llvm-symbolizer` 从命令行读取输入名称和地址，并将对应的源代码位置打印到标准输出。它还可以通过 `--filter-markup` 对包含 Symbolizer Markup 的日志进行符号化。

如果命令行上未指定地址，则从标准输入读取地址。如果命令行上未指定输入名称但指定了地址，或者在任何时候输入值未被识别，则该输入将直接回显到输出。

输入名称可以与地址一起在标准输入或命令行上作为位置参数指定。默认情况下，输入名称被解释为目标文件路径。但是，在名称前加 `BUILDID:` 表示它是十六进制构建 ID 而非路径。这将查找对应的调试二进制文件。为保持一致性，在名称前加 `FILE:` 显式表示它是目标文件路径（默认行为）。

位置参数或标准输入值可以前缀 "DATA" 或 "CODE"，分别表示地址应被符号化为数据或可执行代码。如果两者均未指定，则假定为 "CODE"。DATA 被符号化为地址和符号大小，而非行号。

`llvm-symbolizer` 在解析命令行选项后，从环境变量 `LLVM_SYMBOLIZER_OPTS` 解析选项。当 `llvm-symbolizer` 被其他程序或运行时调用时，`LLVM_SYMBOLIZER_OPTS` 主要用于补充命令行选项。

## 实例

以下所有示例使用以下两个源文件作为输入。它们混合使用 C 风格和 C++ 风格的链接，以说明这些名称如何以不同方式打印（参见 `--demangle`）。

```c
// test.h
extern "C" inline int foz() { return 1234; }
```

```c
// test.cpp
#include "test.h"
int bar=42;
int foo() { return bar; }
int baz() { volatile int k = 42; return foz() + k; }
int main() { return foo() + baz(); }
```

这些文件按如下方式构建：

```sh
$ clang -g test.cpp -o test.elf
$ clang -g -O2 test.cpp -o inlined.elf
```

示例 1 - 命令行上的地址和目标文件：

```sh
$ llvm-symbolizer --obj=test.elf 0x4004d0 0x400490
foz
/tmp/test.h:1:0
baz()
/tmp/test.cpp:11:0
```

示例 2 - 标准输入上的地址：

```sh
$ cat addr.txt
0x4004a0
0x400490
0x4004d0
$ llvm-symbolizer --obj=test.elf < addr.txt
main
/tmp/test.cpp:15:0
baz()
/tmp/test.cpp:11:0
foz
/tmp/./test.h:1:0
```

示例 3 - 与地址一起指定目标文件：

```sh
$ llvm-symbolizer "test.elf 0x400490" "FILE:inlined.elf 0x400480"
baz()
/tmp/test.cpp:11:0
foo()
/tmp/test.cpp:8:10
$ cat addr2.txt
FILE:test.elf 0x4004a0
inlined.elf 0x400480
$ llvm-symbolizer < addr2.txt
main
/tmp/test.cpp:15:0
foo()
/tmp/test.cpp:8:10
```

示例 4 - BUILDID 和 FILE 前缀：

```sh
$ llvm-symbolizer "FILE:test.elf 0x400490" "DATA BUILDID:123456789abcdef 0x601028"
baz()
/tmp/test.cpp:11:0
bar
6295592
4
$ cat addr3.txt
FILE:test.elf 0x400490
DATA BUILDID:123456789abcdef 0x601028
$ llvm-symbolizer < addr3.txt
baz()
/tmp/test.cpp:11:0
bar
6295592
4
```

示例 5 - CODE 和 DATA 前缀：

```sh
$ llvm-symbolizer --obj=test.elf "CODE 0x400490" "DATA 0x601028"
baz()
/tmp/test.cpp:11:0
bar
6295592
4
$ cat addr4.txt
CODE test.elf 0x4004a0
DATA inlined.elf 0x601028
$ llvm-symbolizer < addr4.txt
main
/tmp/test.cpp:15:0
bar
6295592
4
```

示例 6 - 路径风格选项：

此示例使用与上述相同的源文件，但源文件的完整路径为 **/tmp/foo/test.cpp**，按如下方式编译。第一种情况显示默认的绝对路径，第二种使用 `--basenames`，第三种显示 `--relativenames`。

```sh
$ pwd
/tmp
$ clang -g foo/test.cpp -o test.elf
$ llvm-symbolizer --obj=test.elf 0x4004a0
main
/tmp/foo/test.cpp:15:0
$ llvm-symbolizer --obj=test.elf 0x4004a0 --basenames
main
test.cpp:15:0
$ llvm-symbolizer --obj=test.elf 0x4004a0 --relativenames
main
foo/test.cpp:15:0
```

## 选项

**--adjust-vma <offset>** 执行查找时将指定偏移量添加到目标文件地址。这可用于模拟目标文件被偏移量重定位后的查找。

**--basenames, -s** 仅打印文件名而不包含任何目录，而非绝对路径。

**--build-id** 使用给定的构建 ID 查找目标文件，指定为十六进制字符串。与 `--obj` 互斥。

**--color [=<always|auto|never>]** 指定在 `--filter-markup` 模式下是否使用颜色。默认为 auto，自动检测标准输出是否支持颜色。单独指定 `--color` 等同于 `--color=always`。

**--debug-file-directory <path>** 提供包含 `.build-id` 子目录的路径，用于搜索被剥离二进制文件的调试信息。此参数的多个实例按给定顺序搜索。

**--debuginfod, --no-debuginfod** 是否尝试对调试二进制文件进行 debuginfod 查找。除非另行指定，仅当编译时包含 libcurl（`LLVM_ENABLE_CURL`）且环境变量 `DEBUGINFOD_URLS` 提供了至少一个服务器 URL 时，才启用 debuginfod。

**--demangle, -C** 如果名称已被 mangle，则打印 demangle 后的函数名（例如 mangle 名称 `_Z3bazv` 变为 `baz()`，而未 mangle 的名称 `foz` 按原样打印）。默认为 true。

**--dwp <path>** 对任何具有拆分 DWARF 调试数据的 CU，使用指定路径 <path> 处的 DWP 文件。

**--fallback-debug-path <path>** 当独立文件包含调试数据并由 GNU debug link 节引用时，如果无法相对于目标找到调试数据，则使用指定路径作为定位调试数据的基础。

**--filter-markup** 从标准输入读取，将包含的 Symbolizer Markup 转换为人类可读形式，并将结果打印到标准输出。以下 markup 元素尚不支持：

- `{{{hexdict}}}`
- `{{{dumpfile}}}`

`{{{bt}}}` 回溯元素使用以下语法报告帧：

`#<number>[.<inline>] <address> <function> <file>:<line>:<col> (<module>+<relative address>)`

<inline> 为内联到调用者中的调用提供帧编号，对应于 <number>。内联调用编号从 1 开始，从被调用者到调用者递增。

<address> 是函数调用指令内的地址。该地址可能不是指令的起始位置。<relative address> 是加载到该地址的 <module> 中的对应虚拟偏移量。

**--functions [=<none|short|linkage>], -f** 指定函数名的打印方式（分别为省略函数名、打印短函数名或打印完整链接名）。默认为 linkage。

**--help, -h** 显示此命令的帮助和用法。

**--inlining, --inlines, -i** 如果源代码位置在内联函数中，打印所有内联帧。这是默认行为。

**--no-inlines** 不打印内联帧。

**--no-demangle** 不打印 demangle 后的函数名。

**--obj <path>, --exe, -e** 要符号化的目标文件路径。如果指定为 `-`，则直接从标准输入流读取目标文件。与 `--build-id` 互斥。

**--output-style <LLVM|GNU|JSON>** 指定首选输出风格。默认为 LLVM。当输出风格设置为 GNU 时，工具遵循 GNU addr2line 的风格。与 LLVM 风格的差异如下：

- 不打印源代码位置的列。
- 不在地址报告后添加空行。
- 当未显示内联帧时，不用最顶层调用者的名称替换内联函数的名称。
- 当地址的调试数据判别器非零时打印该判别器。生成判别器的一种方法是使用 clang 的 `-fdebug-info-for-profiling` 编译。

JSON 风格提供 JSON 格式的机器可读输出。如果地址通过 stdin 提供，输出 JSON 将是一系列独立对象。否则，所有结果将包含在单个数组中。

```sh
$ llvm-symbolizer --obj=inlined.elf 0x4004be 0x400486 -p
baz() at /tmp/test.cpp:11:18
(inlined by)
main at /tmp/test.cpp:15:0
foo() at /tmp/test.cpp:6:3
$ llvm-symbolizer --output-style=LLVM --obj=inlined.elf 0x4004be 0x400486 -p --no-inlines
main at /tmp/test.cpp:11:18
foo() at /tmp/test.cpp:6:3
$ llvm-symbolizer --output-style=GNU --obj=inlined.elf 0x4004be 0x400486 -p --no-inlines
baz() at /tmp/test.cpp:11
foo() at /tmp/test.cpp:6
$ clang -g -fdebug-info-for-profiling test.cpp -o profiling.elf
$ llvm-symbolizer --output-style=GNU --obj=profiling.elf 0x401167 -p --no-inlines
main at /tmp/test.cpp:15 (discriminator 2)
$ llvm-symbolizer --output-style=JSON --obj=inlined.elf 0x4004be 0x400486 -p
[
  {
    "Address": "0x4004be",
    "ModuleName": "inlined.elf",
    "Symbol": [
      {
        "Column": 18,
        "Discriminator": 0,
        "FileName": "/tmp/test.cpp",
        "FunctionName": "baz()",
        "Line": 11,
        "StartAddress": "0x4004be",
        "StartFileName": "/tmp/test.cpp",
        "StartLine": 9
      },
      {
        "Column": 0,
        "Discriminator": 0,
        "FileName": "/tmp/test.cpp",
        "FunctionName": "main",
        "Line": 15,
        "StartAddress": "0x4004be",
        "StartFileName": "/tmp/test.cpp",
        "StartLine": 14
      }
    ]
  },
  {
    "Address": "0x400486",
    "ModuleName": "inlined.elf",
    "Symbol": [
      {
        "Column": 3,
        "Discriminator": 0,
        "FileName": "/tmp/test.cpp",
        "FunctionName": "foo()",
        "Line": 6,
        "StartAddress": "0x400486",
        "StartFileName": "/tmp/test.cpp",
        "StartLine": 5
      }
    ]
  }
]
```

**--pretty-print, -p** 打印人类可读的输出。如果指定了 `--inlining`，封闭作用域将以 (inlined by) 为前缀。对于 JSON 输出，此选项会使 JSON 缩进并分行。否则，JSON 输出将以紧凑形式打印。

```sh
$ llvm-symbolizer --obj=inlined.elf 0x4004be --inlining --pretty-print
baz() at /tmp/test.cpp:11:18
(inlined by)
main at /tmp/test.cpp:15:0
```

**--print-address, --addresses, -a** 在源代码位置之前打印地址。默认为 false。

```sh
$ llvm-symbolizer --obj=inlined.elf --print-address 0x4004be
0x4004be
baz()
/tmp/test.cpp:11:18
main
/tmp/test.cpp:15:0
$ llvm-symbolizer --obj=inlined.elf 0x4004be --pretty-print --print-address
0x4004be: baz() at /tmp/test.cpp:11:18
(inlined by)
main at /tmp/test.cpp:15:0
```

**--print-source-context-lines <N>** 为每个符号化地址打印 N 行源代码上下文。

```sh
$ llvm-symbolizer --obj=test.elf 0x400490 --print-source-context-lines=3
baz()
/tmp/test.cpp:11:0
10  : volatile int k = 42;
11 >: return foz() + k;
12  : }
```

**--relativenames** 打印相对于编译目录的文件路径，而非绝对路径。如果编译器的命令行包含完整路径，这与默认行为相同。

**--verbose** 打印详细的地址、行和列信息。

```sh
$ llvm-symbolizer --obj=inlined.elf --verbose 0x4004be
baz()
  Filename: /tmp/test.cpp
  Function start filename: /tmp/test.cpp
  Function start line: 9
  Function start address: 0x4004b6
  Line: 11
  Column: 18
main
  Filename: /tmp/test.cpp
  Function start filename: /tmp/test.cpp
  Function start line: 14
  Function start address: 0x4004b0
  Line: 15
  Column: 18
```

**--version, -v** 打印工具的版本信息。

**@<FILE>** 从响应文件 <FILE> 读取命令行选项。

## Windows/PDB 特定选项

**--dia** 使用 Windows DIA SDK 进行符号化。如果未找到 DIA SDK，`llvm-symbolizer` 将回退到原生实现。

## Mach-O 特定选项

**--default-arch <arch>** 如果二进制文件包含多个架构的目标文件（例如 Mach-O 通用二进制文件），则符号化给定架构的目标文件。也可以通过在输入中写入 binary_name:arch_name 来指定架构（参见下面的示例）。如果未以任一方式指定架构，地址将不被符号化。默认为空字符串。

```sh
$ cat addr.txt
/tmp/mach_universal_binary:i386 0x1f84
/tmp/mach_universal_binary:x86_64 0x100000f24
$ llvm-symbolizer < addr.txt
_main
/tmp/source_i386.cc:8
_main
/tmp/source_x86_64.cc:8
```

**--dsym-hint <path/to/file.dSYM>** 如果二进制文件的调试信息不在默认位置，则通过此选项提供的 .dSYM 路径查找调试信息。此标志可多次使用。

## 退出状态

`llvm-symbolizer` 返回 0。其他退出码意味着内部程序错误。

## 参见

[llvm-addr2line(1)](llvm-addr2line.1.md)

## 作者

由 LLVM Team (<https://llvm.org/>) 维护。

## 版权

2003-2023, LLVM Project
