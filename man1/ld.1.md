  LD.LLD(1)  

LD.LLD(1)

FreeBSD General Commands Manual

LD.LLD(1)

[名称](#__u540D___u79F0_)
=======================

`ld.lld` —

来自 LLVM 项目的 ELF 链接器

[概要](#__u6982___u8981_)
=======================

`ld.lld` \[options\] objfile ...

[描述](#__u63CF___u8FF0_)
=======================

链接器获取一个或多个对象、存档和库文件，并将它们组合成一个输出文件（可执行文件、共享库或另一个对象文件）。 它从输入文件中重新定位代码和数据并解析它们之间的符号引用。

`ld.lld` 是 GNU BFD 和黄金链接器的直接替代品。 它接受大多数与 GNU 链接器相同的命令行参数和链接器脚本。

`ld.lld` 目前支持 i386、x86-64、ARM、AArch64、PowerPC32、PowerPC64、MIPS32、MIPS64、RISC-V、AMDGPU、Hexagon 和 SPARC V9 目标。 如果作为 `lld-link` 调用， `ld.lld` 充当 Microsoft link.exe 兼容的链接器；如果作为 ld.ld64 调用，则充当 macOS 的 `ld.lld` 。 无论 `ld.lld` 是构建的，但始终支持所有这些目标，因此您始终可以将 `ld.lld` 用作本机链接器和交叉链接器。

[选项](#__u9009___u9879_)
=======================

许多选项都有单字母和长格式。 当使用以字母 `o` 开头的选项以外的长格式选项时，可以在选项名称前使用一或两个破折号来指定。 以 `o` 开头的长选项需要两个破折号以避免与 `-o` path 选项混淆。

[`--allow-multiple-definition`](#-allow-multiple-definition)

如果一个符号被多次定义，不要出错。 将使用第一个定义。

[`--allow-shlib-undefined`](#-allow-shlib-undefined)

允许共享库中未解析的引用。 链接共享库时默认启用此选项。

[`--apply-dynamic-relocs`](#-apply-dynamic-relocs)

为动态重定位应用链接时间值。

[`--as-needed`](#-as-needed)

如果使用，仅为共享库设置 `DT_NEEDED` 。

[`--auxiliary`](#-auxiliary)\=value

将 `DT_AUXILIARY` 字段设置为指定的名称。

[`--Bdynamic`](#-Bdynamic), `--dy`

链接到共享库。

[`--Bstatic`](#-Bstatic), `--static`, `--dn`

不要链接到共享库。

[`--Bsymbolic`](#-Bsymbolic)

在本地绑定定义的符号。

[`--Bsymbolic-functions`](#-Bsymbolic-functions)

在本地绑定定义的函数符号。

[`--build-id`](#-build-id)\=value

生成构建 ID 注释。 value 可以是 `fast`, `md5`, `sha1`, `tree`, `uuid`, `0x`hex-string 和 `none` 之一。 `tree` 是 `sha1` 的别名。 `fast`, `md5`, `sha1` 和 `tree` 类型的 Build-ID 是根据对象内容计算得出的。 `fast` 并不是为了加密安全。

[`--build-id`](#-build-id_2)

[`--build-id`](#-build-id_3)\=`fast` 的同义词。

[`--color-diagnostics`](#-color-diagnostics)\=value

在诊断中使用颜色。 value 可以是 `always`, `auto` 和 `never` 之一。 当且仅当输出到终端时， `auto` 启用颜色。

[`--color-diagnostics`](#-color-diagnostics_2)

[`--color-diagnostics`](#-color-diagnostics_3)\=`auto` 的别名。

[`--compress-debug-sections`](#-compress-debug-sections)\=value

压缩 DWARF 调试部分。 value 可以是 `none` 和 `zlib` 。 默认压缩级别为 1（最快），因为调试信息通常在该级别压缩得很好，但如果您想进一步压缩，可以指定 `-O2` 将压缩级别设置为 6。

[`--cref`](#-cref)

输出交叉引用表。

[`--define-common`](#-define-common), `-d`

为常用符号分配空间。

[`--defsym`](#-defsym)\=symbol\=expression

定义符号别名。 expression 可以是另一个符号或链接描述文件表达式。 例如， ‘`--defsym=foo=bar`’ or ‘`--defsym=foo=bar+0x100`’.

[`--demangle`](#-demangle)

去除符号名称。

[`--disable-new-dtags`](#-disable-new-dtags)

禁用新的动态标签。

[`--discard-all`](#-discard-all), `-x`

删除所有本地符号。

[`--discard-locals`](#-discard-locals), `-X`

删除临时本地符号。

[`--discard-none`](#-discard-none)

将所有符号保留在符号表中。

[`--dynamic-linker`](#-dynamic-linker)\=value

指定用于动态链接的可执行文件的动态链接器。 这记录在 `PT_INTERP` 类型的 ELF 段中。

[`--dynamic-list`](#-dynamic-list)\=file

从 file 中读取动态符号列表。 （可执行）将匹配的非本地定义符号放入动态符号表。 （共享对象）对匹配的非本地 STV\_DEFAULT 符号的引用不应绑定到共享对象中的定义。 暗示 `-Bsymbolic` 但不设置 DF\_SYMBOLIC

[`--eh-frame-hdr`](#-eh-frame-hdr)

请求创建 `.eh_frame_hdr` 部分和 `PT_GNU_EH_FRAME` 段头。

[`--emit-relocs`](#-emit-relocs), `-q`

在输出中生成重定位。

[`--enable-new-dtags`](#-enable-new-dtags)

启用新的动态标签。

[`--end-lib`](#-end-lib)

结束一组对象，这些对象应该被视为一起在一个档案中。

[`--entry`](#-entry)\=entry

入口点符号的名称。

[`--error-limit`](#-error-limit)\=value

停止前发出的最大错误数。 零值表示没有限制。

[`--error-unresolved-symbols`](#-error-unresolved-symbols)

将未解析的符号报告为错误。

[`--execute-only`](#-execute-only)

将可执行部分标记为不可读。 此选项目前仅在 AArch64 上受支持。

[`--exclude-libs`](#-exclude-libs)\=value

从自动导出中排除静态库。

[`--export-dynamic`](#-export-dynamic), `-E`

将符号放入动态符号表中。

[`--export-dynamic-symbol`](#-export-dynamic-symbol)\=glob

（可执行）将匹配的非本地定义符号放入动态符号表。 （共享对象）对匹配的非本地 STV\_DEFAULT 符号的引用不应绑定到共享对象中的定义，即使它们可能是由于 `-Bsymbolic` 、 `-Bsymbolic-functions` 或 `--dynamic-list`

[`--fatal-warnings`](#-fatal-warnings)

将警告视为错误。

[`--filter`](#-filter)\=value, `-F` value

将 `DT_FILTER` 字段设置为指定值。

[`--fini`](#-fini)\=symbol

指定终结器函数。

[`--format`](#-format)\=input-format, `-b` input-format

指定此选项后的输入格式。 input-format 可以是 `binary`, `elf` 和 `default` 之一。 `default` 是 `elf` 的同义词。

[`--gc-sections`](#-gc-sections)

启用未使用部分的垃圾收集。

[`--gdb-index`](#-gdb-index)

生成 `.gdb_index` 部分。

[`--hash-style`](#-hash-style)\=value

指定哈希样式。 value 可以是 `sysv 、` `gnu` 或 `both` 。 `both` 都是默认值。

[`--help`](#-help)

打印帮助信息。

[`--icf`](#-icf)\=`all`

启用相同的代码折叠。

[`--icf`](#-icf_2)\=`safe`

启用安全的相同代码折叠。

[`--icf`](#-icf_3)\=`none`

禁用相同的代码折叠。

[`--ignore-data-address-equality`](#-ignore-data-address-equality)

忽略数据的地址相等性。 C/C++ 要求每个数据有一个唯一的地址。 此选项允许 lld 进行不安全的优化，从而打破要求：创建只读数据的副本或合并两个或多个恰好具有相同值的只读数据。

[`--ignore-function-address-equality`](#-ignore-function-address-equality)

忽略函数的地址相等。 此选项允许对共享对象中具有非默认可见性的函数进行非 PIC 调用。 该函数在可执行文件和共享对象中可能有不同的地址。

[`--image-base`](#-image-base)\=value

将基地址设置为 value 。

[`--init`](#-init)\=symbol

指定初始化函数。

[`--keep-unique`](#-keep-unique)\=symbol

在 ICF 期间不要折叠 symbol 。

[`-l`](#l) libName, `--library`\=libName

要使用的库的根名称。

[`-L`](#L) dir, `--library-path`\=dir

将目录添加到库搜索路径。

[`--lto-aa-pipeline`](#-lto-aa-pipeline)\=value

在 LTO 期间运行的 AA 管道。与 `--lto-newpm-passes` 结合使用。

[`--lto-newpm-passes`](#-lto-newpm-passes)\=value

在 LTO 期间通过运行。

[`--lto-O`](#-lto-O)opt-level

LTO 的优化级别。

[`--lto-partitions`](#-lto-partitions)\=value

LTO 代码生成分区的数量。

[`-m`](#m) value

设置目标仿真。

[`--Map`](#-Map)\=file, `-M` file

将链接映射打印到 file 。

[`--nmagic`](#-nmagic), `-n`

不要页面对齐部分，链接到静态库。

[`--no-allow-shlib-undefined`](#-no-allow-shlib-undefined)

不允许共享库中未解析的引用。 链接可执行文件时默认启用此选项。

[`--no-as-needed`](#-no-as-needed)

始终为共享库设置 `DT_NEEDED` 。

[`--no-color-diagnostics`](#-no-color-diagnostics)

不要在诊断中使用颜色。

[`--no-define-common`](#-no-define-common)

不要为常用符号分配空格。

[`--no-demangle`](#-no-demangle)

不要对符号名称进行拆解。

[`--no-dynamic-linker`](#-no-dynamic-linker)

禁止 `.interp` 部分的输出。

[`--no-gc-sections`](#-no-gc-sections)

禁用未使用部分的垃圾收集。

[`--no-gnu-unique`](#-no-gnu-unique)

禁用 STB\_GNU\_UNIQUE 符号绑定。

[`--no-merge-exidx-entries`](#-no-merge-exidx-entries)

禁用合并 .ARM.exidx 条目。

[`--no-nmagic`](#-no-nmagic)

页面对齐部分

[`--no-omagic`](#-no-omagic)

不要将文本数据部分设置为可写、页面对齐部分。

[`--no-relax`](#-no-relax)

禁用特定于目标的放松。 目前这是一个空操作。

[`--no-rosegment`](#-no-rosegment)

不要将只读不可执行的部分放在它们自己的段中。

[`--no-undefined-version`](#-no-undefined-version)

报告引用未定义符号的版本脚本。

[`--no-undefined`](#-no-undefined)

即使链接器正在创建共享库，也要报告未解析的符号。

[`--no-warn-symbol-ordering`](#-no-warn-symbol-ordering)

不要警告符号排序文件或调用图配置文件的问题。

[`--no-whole-archive`](#-no-whole-archive)

恢复加载存档成员的默认行为。

[`--no-pie`](#-no-pie), `--no-pic-executable`

不要创建与位置无关的可执行文件。

[`--noinhibit-exec`](#-noinhibit-exec)

只要可执行输出文件仍然可用，就保留它。

[`--nostdlib`](#-nostdlib)

仅搜索命令行上指定的目录。

[`-o`](#o) path

将输出的可执行文件、库或对象写入 path 。 如果未指定，则使用 `a.out` 作为默认值。

[`-O`](#O)value

优化输出文件大小。 value 可能是：

[`0`](#0)

禁用字符串合并。

[`1`](#1)

启用字符串合并。

[`2`](#2)

启用字符串尾部合并。 如果给出 `--compress-debug-sections` ，则以压缩级别 6 而非 1 压缩调试部分。

`-O``1` 是默认值。

[`--oformat`](#-oformat)\=format

指定输出对象文件的格式。 唯一支持的 format 是 `binary` ，它产生没有 ELF 标头的输出。

[`--omagic`](#-omagic), `-N`

将文本和数据部分设置为可读可写，不要页面对齐部分，链接到静态库。

[`--opt-remarks-filename`](#-opt-remarks-filename) file

将 YAML 格式的优化备注写入 file 。

[`--opt-remarks-passes`](#-opt-remarks-passes) pass-regex

通过仅允许匹配 pass-regex 的通行证来过滤优化备注。

[`--opt-remarks-with-hotness`](#-opt-remarks-with-hotness)

在优化备注文件中包含热度信息。

[`--orphan-handling`](#-orphan-handling)\=mode

控制如何处理孤立部分。 孤立部分是链接描述文件中未特别提及的部分。 mode 可能是：

[`place`](#place)

将孤立部分放在合适的输出部分中。

[`warn`](#warn)

放置孤儿部分作为 `place` ，也报告一个警告。

[`error`](#error)

放置孤儿部分作为 `place` ，也报告错误。

`place` 是默认值。

[`--pack-dyn-relocs`](#-pack-dyn-relocs)\=format

以给定格式打包动态重定位。 format 可能是：

[`none`](#none)

不要打包。 动态重定位在 SHT\_REL(A) 中编码。

[`android`](#android)

在 SHT\_ANDROID\_REL(A) 中打包动态重定位。

[`relr`](#relr)

在 SHT\_RELR 中打包相对重定位，在 SHT\_REL(A) 中打包其余动态重定位。

[`android+relr`](#android+relr)

在 SHT\_RELR 中打包相对重定位，在 SHT\_ANDROID\_REL(A) 中打包其余动态重定位。

`none` 是默认值。 如果指定了 `--use-android-relr-tags` ，则使用 SHT\_ANDROID\_RELR 而不是 SHT\_RELR。

[`--pic-veneer`](#-pic-veneer)

始终生成与位置无关的 thunk。

[`--pie`](#-pie), `--pic-executable`

创建与位置无关的可执行文件。

[`--print-gc-sections`](#-print-gc-sections)

列出已删除的未使用部分。

[`--print-icf-sections`](#-print-icf-sections)

列出相同的折叠部分。

[`--print-map`](#-print-map)

将链接映射打印到标准输出。

[`--print-archive-stats`](#-print-archive-stats)\=file

将归档使用统计信息写入指定文件。 打印每个档案的成员数和获取的成员数。

[`--push-state`](#-push-state)

保存 `--as-needed` `-、` `--static` 和 `--whole-archive` 的当前状态。

[`--pop-state`](#-pop-state)

取消 `--push-state` 的效果。

[`--relocatable`](#-relocatable), `-r`

创建可重定位目标文件。

[`--reproduce`](#-reproduce)\=path

将一个 tar 文件写入 path ，其中包含重现链接所需的所有输入文件、一个名为 response.txt 的文本文件（包含命令行选项）和一个名为 version.txt 的文本文件，其中包含 ld.lld --version 的输出。 解压后的存档可用于使用相同的选项和输入文件重新运行链接器。

[`--retain-symbols-file`](#-retain-symbols-file)\=file

仅保留文件中列出的符号。

[`--rpath`](#-rpath)\=value, `-R` value

将 `DT_RUNPATH` 添加到输出。

[`--rsp-quoting`](#-rsp-quoting)\=value

响应文件的引用样式。 支持的值为 `windows` 和 `posix` 。

[`--script`](#-script)\=file, `-T` file

从 file 中读取链接描述文件。 如果给出了多个链接描述文件，它们的处理方式就好像它们是按照它们在命令行中出现的顺序连接起来的一样。

[`--section-start`](#-section-start)\=section\=address

设置段地址。

[`--shared`](#-shared), `--Bsharable`

构建共享对象。

[`--shuffle-sections`](#-shuffle-sections)\=seed

使用给定的种子随机播放输入部分。 如果为 0，则使用随机种子。

[`--soname`](#-soname)\=value, `-h` value

将 `DT_SONAME` 设置为 value 。

[`--sort-common`](#-sort-common)

为了 GNU 兼容性，忽略此选项。

[`--sort-section`](#-sort-section)\=value

使用链接描述文件时指定节排序规则。

[`--start-lib`](#-start-lib)

开始一组对象，这些对象应该被视为一起在一个档案中。

[`--strip-all`](#-strip-all), `-s`

剥离所有符号。

[`--strip-debug`](#-strip-debug), `-S`

剥离调试信息。

[`--symbol-ordering-file`](#-symbol-ordering-file)\=file

按 file 指定的顺序布置部分。

[`--sysroot`](#-sysroot)\=value

设置系统根目录。

[`--target1-abs`](#-target1-abs)

将 `R_ARM_TARGET1` 解释为 `R_ARM_ABS32` 。

[`--target1-rel`](#-target1-rel)

将 `R_ARM_TARGET1` 解释为 `R_ARM_REL32` 。

[`--target2`](#-target2)\=type

将 `R_ARM_TARGET2` 解释为 type, 其中 type 是 `rel 、` `abs` 或 `got-rel` 之一。

[`--Tbss`](#-Tbss)\=value

与 `--section-start` 相同，以 `.bss` 作为部分名称。

[`--Tdata`](#-Tdata)\=value

与 `--section-start` 相同，以 `.data` 作为部分名称。

[`--Ttext`](#-Ttext)\=value

与 `--section-start` 相同，以 `.text` 作为部分名称。

[`--thinlto-cache-dir`](#-thinlto-cache-dir)\=value

ThinLTO 缓存对象文件目录的路径。

[`--thinlto-cache-policy`](#-thinlto-cache-policy)\=value

ThinLTO 缓存的修剪策略。

[`--thinlto-jobs`](#-thinlto-jobs)\=value

ThinLTO 作业的数量。

[`--threads`](#-threads)\=N

线程数。 `all` （默认）表示支持的所有并发线程。 `1` 禁用多线程。

[`--time-trace`](#-time-trace)

记录时间轨迹。

[`--time-trace-file`](#-time-trace-file)\=file

将时间跟踪输出写入 file 。

[`--time-trace-granularity`](#-time-trace-granularity)\=value

时间分析器跟踪的最小时间粒度（以微秒为单位）。

[`--trace`](#-trace)

打印输入文件的名称。

[`--trace-symbol`](#-trace-symbol)\=symbol, `-y` symbol

跟踪对 symbol 的引用。

[`--undefined`](#-undefined)\=symbol, `-u` symbol

如果 symbol 解析后未定义符号，并且存在包含定义符号的目标文件的静态库，则加载成员以将目标文件包含在输出文件中。

[`--undefined-glob`](#-undefined-glob)\=pattern

[`--undefined`](#-undefined_2) 的同义词，除了它采用 glob 模式。 在 glob 模式中， `*` 匹配零个或多个字符， ? 匹配任何单个字符，并且 `[...]` 匹配括号内的字符。 与给定模式匹配的所有符号都被视为作为 `--undefined` 的参数给出。

[`--unique`](#-unique)

为每个孤立输入部分创建一个单独的输出部分。

[`--unresolved-symbols`](#-unresolved-symbols)\=value

确定如何处理未解析的符号。

[`--use-android-relr-tags`](#-use-android-relr-tags)

使用 SHT\_ANDROID\_RELR / DT\_ANDROID\_RELR\* 标签代替 SHT\_RELR / DT\_RELR\*。

[`-v`](#v)

如果指定了目标文件，则显示版本号并继续链接。

[`-V`](#V), `--version`

显示版本号并退出。

[`--verbose`](#-verbose)

详细模式。

[`--version-script`](#-version-script)\=file

从 file 中读取版本脚本。

[`--warn-backrefs`](#-warn-backrefs)

警告静态存档之间或之间的反向或循环依赖关系。 这可用于确保链接器调用与传统的类 Unix 链接器保持兼容。

[`--warn-backrefs-exclude`](#-warn-backrefs-exclude)\=glob

描述存档（或 --start-lib 中的目标文件）的 Glob，对于 `--warn-backrefs` 应该忽略它

[`--warn-common`](#-warn-common)

警告重复的常用符号。

[`--warn-ifunc-textrel`](#-warn-ifunc-textrel)

警告将 ifunc 符号与文本重定位结合使用。 旧版本的 glibc 库（2.28 和更早版本）有一个错误，该错误会导致包含 ifunc 符号的段在重定位时被标记为不可执行。 结果，尽管程序编译和链接成功，但当指令指针到达 ifunc 符号时，它给出了分段错误。 使用 -warn-ifunc-textrel 让 lld 发出警告，如果代码可能包含 ifunc 符号，可能会进行文本重定位并与较旧的 glibc 版本链接。 否则，没有必要使用它，因为默认值不会给出警告。 此标志已于 2018 年底引入，在 ld 和 gold 链接器中没有对应部分，将来可能会被删除。

[`--warn-unresolved-symbols`](#-warn-unresolved-symbols)

将未解析的符号报告为警告。

[`--whole-archive`](#-whole-archive)

强制加载静态库中的所有成员。

[`--wrap`](#-wrap)\=symbol

对符号使用包装函数。

[`-z`](#z) option

链接器选项扩展。

[`dead-reloc-in-nonalloc`](#dead-reloc-in-nonalloc)\=section\_glob=value

解析匹配的非 SHF\_ALLOC 部分中的重定位，将丢弃的符号引用到 value 接受 glob，如果部分匹配多个选项，则最后一个选项优先。 建议使用从最不具体到最具体匹配的顺序。

[`execstack`](#execstack)

使主堆栈可执行。 堆栈权限记录在 `PT_GNU_STACK` 段中。

[`force-bti`](#force-bti)

在 PLT 中强制启用 AArch64 BTI 指令，如果输入 ELF 文件没有 GNU\_PROPERTY\_AARCH64\_FEATURE\_1\_BTI 属性，则会发出警告。

[`force-ibt`](#force-ibt)

在 PLT 中强制启用英特尔间接分支跟踪，如果输入 ELF 文件没有 GNU\_PROPERTY\_X86\_FEATURE\_1\_IBT 属性，则会发出警告。

[`global`](#global)

在 `DYNAMIC` 部分设置 `DF_1_GLOBAL flag in the` 标志。 不同的加载器可以自行决定如何处理这个标志。

[`ifunc-noplt`](#ifunc-noplt)

不要为 ifunc 符号发出 PLT 条目。相反，发出引用解析器的文本重定位。 这是一个实验性优化，仅适用于文本重定位没有通常缺点的独立环境。 此选项必须与 `-z` `notext` 选项结合使用。

[`initfirst`](#initfirst)

设置 `DF_1_INITFIRST` 标志以指示应首先初始化模块。

[`interpose`](#interpose)

设置 `DF_1_INTERPOSE` 标志以向运行时链接器指示对象是插入器。 在符号解析期间，在应用程序之后但在其他依赖项之前搜索插入器。

[`muldefs`](#muldefs)

如果一个符号被多次定义，不要出错。 将使用第一个定义。 这是 `--allow-multiple-definition` 的同义词。

[`nocombreloc`](#nocombreloc)

禁用组合和排序多个重定位部分。

[`nocopyreloc`](#nocopyreloc)

禁用复制重定位的创建。

[`nodefaultlib`](#nodefaultlib)

设置 `DF_1_NODEFLIB` 标志以指示应忽略默认库搜索路径。

[`nodelete`](#nodelete)

设置 `DF_1_NODELETE` 标志以指示无法从进程中卸载对象。

[`nodlopen`](#nodlopen)

设置 `DF_1_NOOPEN` 标志以指示对象可能不会被 dlopen(3) 打开。

[`nognustack`](#nognustack)

不要发出 `PT_GNU_STACK` 段。

[`norelro`](#norelro)

不要指出对象的某些部分应该在初始重定位处理之后以只读方式映射。 该对象将省略 `PT_GNU_RELRO` 段。

[`notext`](#notext)

允许对只读段进行重定位。 在 `DYNAMIC` 部分中设置 `DT_TEXTREL` 标志。

[`now`](#now)

设置 `DF_BIND_NOW` 标志以指示运行时加载程序应执行所有重定位处理作为对象初始化的一部分。 默认情况下，可以按需执行重定位。

[`origin`](#origin)

设置 `DF_ORIGIN` 标志以指示对象需要 $ORIGIN 处理。

[`pac-plt`](#pac-plt)

仅限 AArch64，在 PLT 中使用指针认证。

[`rel`](#rel)

使用 REL 格式进行动态重定位。

[`rela`](#rela)

使用 RELA 格式进行动态重定位。

[`retpolineplt`](#retpolineplt)

发出 retpoline 格式的 PLT 条目作为 CVE-2017-5715 的缓解措施。

[`rodynamic`](#rodynamic)

将 `.dynamic` 部分设为只读。不会发出 `DT_DEBUG` 标记。

[`separate-loadable-segments`](#separate-loadable-segments)

[`separate-code`](#separate-code)

[`noseparate-code`](#noseparate-code)

指定是否允许两个相邻的 PT\_LOAD 段在页面中重叠。 `noseparate-code` （默认）允许重叠。 `separate-code` 允许两个可执行段或两个不可执行段之间的重叠。 `separate-loadable-segments` 不允许重叠。

[`shstk`](#shstk)

仅限 x86，使用影子堆栈。

[`stack-size`](#stack-size)\=size

将主线程的堆栈大小设置为 size 。 堆栈大小记录为大小的 size 。 `PT_GNU_STACK` 程序段。

[`text`](#text)

不允许对只读段进行重定位。 这是默认设置。

[`wxneeded`](#wxneeded)

创建一个 `PT_OPENBSD_WXNEEDED` 段。

[实现说明](#__u5B9E___u73B0___u8BF4___u660E_)
=========================================

`ld.lld` 对归档文件（具有 .a 文件扩展名的文件）的处理与在类 Unix 系统上使用的传统链接器不同。

传统的链接器在链接期间维护一组未定义的符号。 链接器按照文件在命令行中出现的顺序处理每个文件，直到未定义符号集变为空。 遇到对象文件时，它会链接到输出对象，并将其未定义的符号添加到集合中。 在遇到档案文件时，传统的链接器会搜索其中包含的对象，并处理那些满足未解析集中符号的对象

使用传统链接器时，处理相互依赖的档案可能会很尴尬。 存档文件可能必须多次指定，或者可以使用特殊的命令行选项 `--start-group` 和 `--end-group` 让链接器循环遍历组中的文件，直到没有新符号添加到集合中.

`ld.lld` 在遍历命令行参数时记录在对象和档案中发现的所有符号。 当 `ld.lld` 遇到可以由包含在先前处理的存档文件中的对象文件解析的未定义符号时，它会立即将其提取并链接到输出对象中。

与传统链接器相比，使用某些存档输入 `ld.lld` 可能会产生不同的结果。 在实践中，大量第三方软件已与 `ld.lld` 链接，没有重大问题。

The `--warn-backrefs` 选项可用于标识可能与传统的类 Unix 链接器行为不兼容的链接器调用。

May 12, 2019

FreeBSD 13.1-RELEASE