# ld.lld(1)

`ld.lld` — 来自 LLVM 项目的 ELF 链接器

## 名称

`ld.lld`

## 概要

`ld.lld [options] objfile ...`

## 描述

链接器接收一个或多个目标文件、归档文件和库文件，并将它们合并为一个输出文件（可执行文件、共享库或另一个目标文件）。它对输入文件中的代码和数据进行重定位，并解析它们之间的符号引用。

`ld.lld` 是 GNU BFD 和 gold 链接器的直接替代品。它接受与 GNU 链接器相同的大多数命令行参数和链接器脚本。

`ld.lld` 目前支持 i386、x86-64、ARM、AArch64、LoongArch、PowerPC32、PowerPC64、MIPS32、MIPS64、RISC-V、AMDGPU、Hexagon 和 SPARC V9 目标平台。如果以 `lld-link` 调用，`ld.lld` 将充当 Microsoft link.exe 兼容的链接器；如果以 `ld.ld64` 调用，则充当 macOS 的 ld。无论 `ld.lld` 如何构建，所有这些目标平台始终受支持，因此你始终可以将 `ld.lld` 用作本地链接器或交叉链接器。

## 选项

许多选项同时具有单字母和长格式。使用长格式选项时，除了以字母 `o` 开头的选项外，可以在选项名前使用一个或两个短横线来指定。以 `o` 开头的长选项需要两个短横线，以避免与 `-o` `path` 选项混淆。

**`--allow-multiple-definition`** 如果符号被多次定义，不报错。将使用第一个定义。

**`--allow-shlib-undefined`** 允许共享库中存在未解析的引用。链接共享库时默认启用此选项。

**`--apply-dynamic-relocs`** 对动态重定位应用链接时值。

**`--as-needed`** 仅在使用时才为共享库设置 `DT_NEEDED`。

**`--auxiliary`** =`value` 将 `DT_AUXILIARY` 字段设置为指定名称。

**`--Bdynamic`** , `--dy` 链接共享库。

**`--Bstatic`** , `--static`, `--dn` 不链接共享库。

**`-Bno-symbolic`** 对于 `-shared`，不将默认可见性的已定义符号在本地绑定（默认）。

**`-Bsymbolic`** 对于 `-shared`，将默认可见性的已定义符号在本地绑定。同时设置 `DF_SYMBOLIC` 标志。

**`-Bsymbolic-non-weak`** 对于 `-shared`，将默认可见性的已定义 STB_GLOBAL 符号在本地绑定。

**`-Bsymbolic-functions`** 对于 `-shared`，将默认可见性的已定义函数符号在本地绑定。

**`-Bsymbolic-non-weak-functions`** 对于 `-shared`，将默认可见性的已定义 STB_GLOBAL 函数符号在本地绑定。

**`--be8`** 使用 BE8 格式写入大端序 ELF 文件（仅限 AArch32）。

**`--branch-to-branch`** 启用分支间优化：目标为另一条分支指令的分支将被重写为指向后者的分支目标（仅限 AArch64 和 X86_64）。在 `-O2` 时默认启用。

**`--build-id`** =`value` 生成构建 ID 注记。`value` 可以是 `fast`、`md5`、`sha1`、`tree`、`uuid`、`0x``hex-string` 或 `none` 之一。`tree` 是 `sha1` 的别名。类型为 `fast`、`md5`、`sha1` 和 `tree` 的构建 ID 根据对象内容计算。`fast` 不保证密码学安全性。

**`--build-id`** `--build-id`=`sha1` 的同义词。

**`--call-graph-profile-sort`** =`algorithm` `algorithm` 可以是：

**`none`** 忽略调用图配置文件。

**`hfsort`** 使用 hfsort。

**`cdsort`** 使用 cdsort（默认）。

**`--color-diagnostics`** =`value` 在诊断中使用颜色。`value` 可以是 `always`、`auto` 或 `never` 之一。`auto` 仅在输出到终端时启用颜色。

**`--color-diagnostics`** `--color-diagnostics`=`auto` 的别名。

**`--compress-debug-sections`** =`value` 压缩 DWARF 调试节。如果压缩后的内容更大，则该节保持未压缩。`value` 可以是：

**`none`** 不压缩。

**`zlib`** 默认压缩级别为 1（最快），因为调试信息通常在该级别下压缩效果良好。

**`zstd`** 使用 zstd 的默认压缩级别。

**`--compress-sections`** =`section-glob={none,zlib,zstd}[:level]` 压缩匹配通配符且不具有 SHF_ALLOC 标志的输出节。如果压缩后的内容更大，则匹配的节保持未压缩。压缩级别为 `level`（如果指定）或默认的注重速度的级别。这类似于通用化的 `--compress-debug-sections`。

**`--cref`** 输出交叉引用表。如果指定了 `-Map`，则打印到映射文件中。

**`--debug-names`** 生成合并后的 `.debug_names` 节。

**`--default-script`** =`file`, `-dT` `file` 在未指定 `--script` 时，读取此默认链接器脚本。

**`--defsym`** =`symbol`=`expression` 定义符号别名。`expression` 可以是另一个符号或链接器脚本表达式。例如，`--defsym=foo=bar` 或 `--defsym=foo=bar+0x100`。

**`--demangle`** 还原符号名（demangle）。

**`--disable-new-dtags`** 禁用新的动态标签。

**`--discard-all`** , `-x` 删除所有局部符号。

**`--discard-locals`** , `-X` 删除临时局部符号。

**`--discard-none`** 保留符号表中的所有符号。

**`--dynamic-linker`** =`value` 指定动态链接的可执行文件所使用的动态链接器。此信息记录在类型为 `PT_INTERP` 的 ELF 段中。

**`--dynamic-list`** =`file` 类似于 `--export-dynamic-symbol-list`。创建共享对象时，隐含 `-Bsymbolic`，但不设置 DF_SYMBOLIC。

**`--EB`** 在 OUTPUT_FORMAT 命令中选择大端序格式。

**`--EL`** 在 OUTPUT_FORMAT 命令中选择小端序格式。

**`--eh-frame-hdr`** 请求创建 `.eh_frame_hdr` 节和 `PT_GNU_EH_FRAME` 段头。

**`--emit-relocs`** , `-q` 在输出中生成重定位。

**`--enable-new-dtags`** 启用新的动态标签。

**`--enable-non-contiguous-regions`** 将输入节溢出到后续匹配的输出节，以避免内存区域溢出。

**`--end-lib`** 结束一组应被视为在归档中一起处理的对象。

**`--entry`** =`entry` 入口点符号的名称。

**`--error-limit`** =`value` 停止前最多发出的错误数。值为零表示无限制。

**`--error-unresolved-symbols`** 将未解析的符号报告为错误。

**`--error-handing-script`** =`script_path` 在某些错误时调用脚本 `script_path`，以 `tag` 作为第一个参数，额外参数作为第二个参数。脚本成功时应返回 0。任何其他值被视为一般错误。`tag` 可以是 `missing-lib` 后跟缺失库的名称，或 `undefined-symbol` 后跟未定义符号的名称。

**`--execute-only`** 将可执行节标记为不可读。此选项目前仅在 AArch64 上受支持。

**`--exclude-libs`** =`value` 将静态库从自动导出中排除。

**`--export-dynamic`** , `-E` 将符号放入动态符号表。

**`--export-dynamic-symbol`** =`glob` （可执行文件）将匹配的非局部已定义符号放入动态符号表。（共享对象）对匹配的非局部 STV_DEFAULT 符号的引用不应绑定到共享对象内的定义，即使由于 `-Bsymbolic`、`-Bsymbolic-functions` 或 `--dynamic-list` 本应如此。

**`--export-dynamic-symbol-list`** =`file` 从 `file` 读取动态符号模式列表。对每个模式应用 `--export-dynamic-symbol`。

**`--fatal-warnings`** 将警告视为错误。

**`--filter`** =`value`, `-F` `value` 将 `DT_FILTER` 字段设置为指定值。

**`--fini`** =`symbol` 指定终结器函数。

**`--force-group-allocation`** 仅对 -r 有意义。节组被丢弃。如果两个节组成员被放置到同一输出节，则合并它们的重定位。

**`--format`** =`input-format`, `-b` `input-format` 指定此选项之后输入的格式。`input-format` 可以是 `binary`、`elf` 或 `default` 之一。`default` 是 `elf` 的同义词。

**`--gc-sections`** 启用未使用节的垃圾回收。

**`--gdb-index`** 生成 `.gdb_index` 节。

**`--hash-style`** =`value` 指定哈希风格。`value` 可以是 `sysv`、`gnu` 或 `both` 之一。`both` 是默认值。

**`--help`** 打印帮助信息。

**`--icf`** =`all` 启用相同代码折叠。

**`--icf`** =`safe` 启用安全的相同代码折叠。

**`--icf`** =`none` 禁用相同代码折叠。

**`--ignore-data-address-equality`** 忽略数据的地址唯一性。C/C++ 要求每个数据具有唯一地址。此选项允许 lld 执行破坏此要求的不安全优化：创建只读数据的副本或合并两个或多个恰好具有相同值的只读数据。

**`--ignore-function-address-equality`** 忽略函数的地址唯一性。此选项允许对共享对象中具有非默认可见性的函数进行非 PIC 调用。该函数在可执行文件和共享对象中可能具有不同的地址。

**`--image-base`** =`value` 将基址设置为 `value`。

**`--init`** =`symbol` 指定初始化函数。

**`--keep-unique`** =`symbol` 在 ICF 期间不折叠 `symbol`。

**`-l`** `libName`, `--library`=`libName` 要使用的库的根名称。

**`-L`** `dir`, `--library-path`=`dir` 将目录添加到库搜索路径。

**`--lto-aa-pipeline`** =`value` 在 LTO 期间运行的 AA 管道。与 `--lto-newpm-passes` 配合使用。

**`--lto-newpm-passes`** =`value` 在 LTO 期间运行的 pass。

**`--lto-O`** `opt-level` LTO 的优化级别。

**`--lto-partitions`** =`value` LTO 代码生成分区数。

**`-m`** `value` 设置目标模拟。

**`--Map`** =`file`, `-M` `file` 将链接映射打印到 `file`。

**`--nmagic`** , `-n` 不对节进行页对齐，链接静态库。

**`--no-allow-shlib-undefined`** 不允许共享库中存在未解析的引用。链接可执行文件时默认启用此选项。

**`--no-as-needed`** 始终为共享库设置 `DT_NEEDED`。

**`--no-color-diagnostics`** 在诊断中不使用颜色。

**`--no-demangle`** 不还原符号名。

**`--no-dynamic-linker`** 抑制 `.interp` 节的输出。

**`--no-fortran-common`** 不在归档成员中搜索定义以覆盖 COMMON 符号。

**`--no-gc-sections`** 禁用未使用节的垃圾回收。

**`--no-gnu-unique`** 禁用 STB_GNU_UNIQUE 符号绑定。

**`--no-merge-exidx-entries`** 禁用 .ARM.exidx 条目的合并。

**`--no-nmagic`** 对节进行页对齐。

**`--no-omagic`** 不将文本数据节设置为可写，对节进行页对齐。

**`--no-relax`** 禁用目标特定的松弛优化。对于 x86-64，这会禁用 R_X86_64_GOTPCRELX 和 R_X86_64_REX_GOTPCRELX GOT 优化。

**`--no-rosegment`** 不将只读的非可执行节放入单独的段。

**`--undefined-version`** 不报告引用未定义符号的版本脚本。

**`--no-undefined`** 即使链接器正在创建共享库，也报告未解析的符号。

**`--no-warn-mismatch`** 不拒绝未知的节类型。

**`--no-warn-symbol-ordering`** 不对符号排序文件或调用图配置文件的问题发出警告。

**`--no-warnings`** , `-w` 抑制警告并取消 `--fatal-warnings`。

**`--no-whole-archive`** 恢复加载归档成员的默认行为。

**`--no-pie`** , `--no-pic-executable` 不创建位置无关的可执行文件。

**`--noinhibit-exec`** 只要可执行输出文件仍然可用就保留它。

**`--nostdlib`** 仅搜索命令行上指定的目录。

**`-o`** `path` 将输出可执行文件、库或目标写入 `path`。如果未指定，默认使用 `a.out`。

**`-O`** `value` 优化输出文件。`value` 可以是：

**`0`** 禁用字符串合并。

**`1`** 启用字符串合并。

**`2`** 启用字符串尾部合并和分支间优化。

`-O1` 是默认值。

**`--oformat`** =`format` 指定输出目标文件的格式。唯一支持的 `format` 是 `binary`，它产生没有 ELF 头的输出。

**`--omagic`** , `-N` 将文本和数据节设置为可读和可写，不对节进行页对齐，链接静态库。

**`--opt-remarks-filename`** `file` 以 YAML 格式将优化备注写入 `file`。

**`--opt-remarks-passes`** `pass-regex` 仅允许匹配 `pass-regex` 的 pass 通过，以过滤优化备注。

**`--opt-remarks-with-hotness`** 在优化备注文件中包含热度信息。

**`--orphan-handling`** =`mode` 控制如何处理孤儿节。孤儿节是链接器脚本中未特别提及的节。`mode` 可以是：

**`place`** 将孤儿节放入合适的输出节。

**`warn`** 像 `place` 一样放置孤儿节，并报告警告。

**`error`** 像 `place` 一样放置孤儿节，并报告错误。

`place` 是默认值。

**`--pack-dyn-relocs`** =`format` 以给定格式打包动态重定位。`format` 可以是：

**`none`** 不打包。动态重定位以 SHT_REL(A) 编码。

**`android`** 以 SHT_ANDROID_REL(A) 打包动态重定位。

**`relr`** 以 SHT_RELR 打包相对重定位，其余动态重定位以 SHT_REL(A) 打包。

**`android+relr`** 以 SHT_RELR 打包相对重定位，其余动态重定位以 SHT_ANDROID_REL(A) 打包。

`none` 是默认值。如果指定了 `--use-android-relr-tags`，则使用 SHT_ANDROID_RELR 而非 SHT_RELR。

**`--package-metadata`** 将百分号编码的字符串发送到 `.note.package` 节。例如，%25 解码为单个 %。

**`--pic-veneer`** 始终生成位置无关的 thunk。

**`--pie`** , `--pic-executable` 创建位置无关的可执行文件。

**`--power10-stubs`** =`mode` 是否在 R_PPC64_REL24_NOTOC 和 TOC/NOTOC 互操作的调用桩中使用 Power10 指令。`mode` 可以是：

**`yes`** （默认）使用。

**`auto`** 目前与 yes 相同。

**`no`** 不使用。

**`--print-gc-sections`** 列出已移除的未使用节。

**`--print-icf-sections`** 列出已折叠的相同节。

**`--print-map`** 将链接映射打印到标准输出。

**`--print-archive-stats`** =`file` 将归档使用统计写入指定文件。打印每个归档的成员数和提取的成员数。

**`--push-state`** 保存 `--as-needed`、`--static` 和 `--whole-archive` 的当前状态。

**`--pop-state`** 恢复由 `--push-state` 保存的状态。

**`--randomize-section-padding`** =`seed` 使用给定种子在输入节之间和每个段的开头随机插入填充。填充被插入到名称匹配以下模式的输出节中：`.bss`、`.data`、`.data.rel.ro`、`.lbss`、`.ldata`、`.lrodata`、`.ltext`、`.rodata` 和 `.text*`。

**`--relax-gp`** 为 RISC-V 启用全局指针松弛优化。

**`--relocatable`** , `-r` 创建可重定位目标文件。

**`--remap-inputs`** =`from-glob=to-file` 匹配 `from-glob` 的输入文件映射到 `to-file`。使用 **/dev/null** 忽略输入文件。

**`--remap-inputs-file`** =`file` 基于 `file` 中的模式重映射输入文件。重映射文件中的每行格式为 `from-glob=to-file` 或以 `#` 开头的注释。

**`--reproduce`** =`path` 将 tar 文件写入 `path`，其中包含重现链接所需的所有输入文件、名为 response.txt 的文本文件（包含命令行选项）和名为 version.txt 的文本文件（包含 ld.lld --version 的输出）。解包后的归档可用于以相同的选项和输入文件重新运行链接器。

**`--retain-symbols-file`** =`file` 仅保留文件中列出的符号。

**`--rpath`** =`value`, `-R` `value` 向输出添加 `DT_RUNPATH`。

**`--rsp-quoting`** =`value` 响应文件的引用风格。支持的值为 `windows` 和 `posix`。

**`--script`** =`file`, `-T` `file` 从 `file` 读取链接器脚本。如果给出了多个链接器脚本，它们将按在命令行上出现的顺序拼接处理。

**`--section-start`** =`section`=`address` 设置节的地址。

**`--shared`** , `--Bsharable` 构建共享对象。

**`--shuffle-sections`** =`seed` 在将匹配的节映射到输出节之前，使用给定种子对其进行随机排列。如果为 -1，则反转节顺序。如果为 0，则使用随机种子。

**`--soname`** =`value`, `-h` `value` 将 `DT_SONAME` 设置为 `value`。

**`--sort-common`** 此选项为 GNU 兼容性而被忽略。

**`--sort-section`** =`value` 指定使用链接器脚本时的节排序规则。

**`--start-lib`** 开始一组应被视为在归档中一起处理的对象。

**`--strip-all`** , `-s` 剥离所有符号。隐含 `--strip-debug`。

**`--strip-debug`** , `-S` 剥离调试信息。

**`--symbol-ordering-file`** =`file` 按 `file` 指定的顺序排列节。

**`--sysroot`** =`value` 设置系统根目录。

**`--target1-abs`** 将 `R_ARM_TARGET1` 解释为 `R_ARM_ABS32`。

**`--target1-rel`** 将 `R_ARM_TARGET1` 解释为 `R_ARM_REL32`。

**`--target2`** =`type` 将 `R_ARM_TARGET2` 解释为 `type`，其中 `type` 为 `rel`、`abs` 或 `got-rel` 之一。

**`--Tbss`** =`value` 同 `--section-start`，以 `.bss` 作为节名。

**`--Tdata`** =`value` 同 `--section-start`，以 `.data` 作为节名。

**`--Ttext`** =`value` 同 `--section-start`，以 `.text` 作为节名。

**`--thinlto-cache-dir`** =`value` ThinLTO 缓存目标文件目录的路径。

**`--thinlto-cache-policy`** =`value` ThinLTO 缓存的修剪策略。

**`--thinlto-jobs`** =`value` ThinLTO 作业数。

**`--threads`** =`N` 线程数。`all`（默认）表示支持的所有并发线程。`1` 禁用多线程。

**`--fat-lto-objects`** 在 fat LTO 目标文件中使用包含 LLVM 位码的 .llvm.lto 节来执行 LTO。

**`--no-fat-lto-objects`** 忽略可重定位目标文件中的 .llvm.lto 节（默认）。

**`--time-trace`** 记录时间追踪。

**`--time-trace-file`** =`file` 将时间追踪输出写入 `file`。

**`--time-trace-granularity`** =`value` 时间分析器追踪的最小时间粒度（以微秒为单位）。

**`--trace`** 打印输入文件的名称。

**`--trace-symbol`** =`symbol`, `-y` `symbol` 追踪对 `symbol` 的引用。

**`--undefined`** =`symbol`, `-u` `symbol` 如果 `symbol` 在符号解析后未定义，并且存在包含定义该符号的目标文件的静态库，则加载该成员以将目标文件包含在输出文件中。

**`--undefined-glob`** =`pattern` `--undefined` 的同义词，但接受通配符模式。在通配符模式中，`*` 匹配零个或多个字符，`?` 匹配任意单个字符，`[...]` 匹配括号内的字符。匹配给定模式的所有符号将如同作为 `--undefined` 的参数一样处理。

**`--unique`** 为每个孤儿输入节创建单独的输出节。

**`--unresolved-symbols`** =`value` 确定如何处理未解析的符号。

**`--use-android-relr-tags`** 使用 SHT_ANDROID_RELR / DT_ANDROID_RELR* 标签代替 SHT_RELR / DT_RELR*。

**`-v`** , `-V` 显示版本号，如果指定了目标文件则继续链接。

**`--version`** 显示版本号并退出。

**`--verbose`** 详细模式。

**`--version-script`** =`file` 从 `file` 读取版本脚本。

**`--warn-backrefs`** 对静态归档之间或指向静态归档的反向或循环依赖发出警告。这可用于确保链接器调用与传统 Unix 链接器保持兼容。

**`--warn-backrefs-exclude`** =`glob` 描述应针对 `--warn-backrefs` 忽略的归档（或 --start-lib 中的目标文件）的通配符。

**`--warn-common`** 对重复的公共符号发出警告。

**`--warn-ifunc-textrel`** 对 ifunc 符号与文本重定位一起使用发出警告。旧版 glibc 库（2.28 及更早版本）存在一个 bug，导致包含 ifunc 符号的段在重定位时被标记为不可执行。因此，虽然程序编译和链接成功，但当指令指针到达 ifunc 符号时会产生段错误。如果代码可能包含 ifunc 符号、可能进行文本重定位并与旧版 glibc 链接，请使用 --warn-ifunc-textrel 让 lld 发出警告。否则无需使用，因为默认值不发出警告。此标志于 2018 年末引入，在 ld 和 gold 链接器中没有对应项，将来可能被移除。

**`--warn-unresolved-symbols`** 将未解析的符号报告为警告。

**`--whole-archive`** 强制加载静态库中的所有成员。

**`--why-extract`** =`file` 将提取归档成员的原因打印到文件。

**`--why-live`** =`glob` 为匹配通配符的每个符号报告阻止垃圾回收的引用链。

**`--wrap`** =`symbol` 将对 `symbol` 的引用重定向到 `__wrap_symbol`，将对 `__real_symbol` 的引用重定向到 `symbol`。

**`-z`** `option` 链接器选项扩展。`option` 可以是以下之一：

**`dead-reloc-in-nonalloc`** =`section_glob=value` 将引用已丢弃符号的匹配非 SHF_ALLOC 节中的重定位解析为 `value`。接受通配符，如果某节匹配多个选项，最后一个选项优先。建议按从最不具体到最具体的顺序匹配。

**`execstack`** 使主栈可执行。栈权限记录在 `PT_GNU_STACK` 段中。

**`bti-report`** =`[none|warning|error]` 指定如何报告缺失的 GNU_PROPERTY_AARCH64_FEATURE_1_BTI 属性。`none` 是默认值，链接器不报告缺失的属性，否则将以警告或错误报告。

**`cet-report`** =`[none|warning|error]` 指定如何报告缺失的 GNU_PROPERTY_X86_FEATURE_1_IBT 或 GNU_PROPERTY_X86_FEATURE_1_SHSTK 属性。`none` 是默认值，链接器不报告缺失的属性，否则将以警告或错误报告。

**`dynamic-undefined-weak`** 当存在动态符号表时，如果未定义的弱符号从可重定位目标文件中被引用，且未被符号可见性或版本控制强制为局部，则使其成为动态的。指定 `nodynamic-undefined-weak` 时不使其成为动态的。构建共享对象或存在输入共享对象时，`dynamic-undefined-weak` 是默认值。

**`pauth-report`** =`[none|warning|error]` 指定如何报告缺失的 GNU_PROPERTY_AARCH64_FEATURE_PAUTH 属性。`none` 是默认值，链接器不报告缺失的属性，否则将以警告或错误报告。

**`force-bti`** 强制在 PLT 中启用 AArch64 BTI 指令，如果输入 ELF 文件不具有 GNU_PROPERTY_AARCH64_FEATURE_1_BTI 属性则发出警告。

**`force-ibt`** 强制在 PLT 中启用 Intel 间接分支跟踪，如果输入 ELF 文件不具有 GNU_PROPERTY_X86_FEATURE_1_IBT 属性则发出警告。

**`global`** 在 `DYNAMIC` 节中设置 `DF_1_GLOBAL` 标志。不同的加载器可以自行决定如何处理此标志。

**`ifunc-noplt`** 不为 ifunc 符号发出 PLT 条目。而是发出引用解析器的文本重定位。这是实验性优化，仅适用于文本重定位没有通常缺点的独立环境。此选项必须与 `-z` `notext` 选项组合使用。

**`initfirst`** 设置 `DF_1_INITFIRST` 标志，指示该模块应首先被初始化。

**`interpose`** 设置 `DF_1_INTERPOSE` 标志，向运行时链接器指示该对象是插入器。在符号解析期间，插入器在应用程序之后但在其他依赖项之前被搜索。

**`lrodata-after-bss`** 将 .lrodata 放在 .bss 之后。

**`muldefs`** 如果符号被多次定义，不报错。将使用第一个定义。这是 `--allow-multiple-definition` 的同义词。

**`nocombreloc`** 禁用多个重定位节的合并和排序。

**`nocopyreloc`** 禁用创建复制重定位。

**`nodefaultlib`** 设置 `DF_1_NODEFLIB` 标志，指示应忽略默认库搜索路径。

**`nodelete`** 设置 `DF_1_NODELETE` 标志，指示该对象不能从进程中卸载。

**`nodlopen`** 设置 `DF_1_NOOPEN` 标志，指示该对象不能被 dlopen(3) 打开。

**`nognustack`** 不发出 `PT_GNU_STACK` 段。

**`norelro`** 不指示对象的某些部分在初始重定位处理后被映射为只读。该对象将省略 `PT_GNU_RELRO` 段。

**`nosectionheader`** 不生成节头表。

**`notext`** 允许对只读段进行重定位。在 `DYNAMIC` 节中设置 `DT_TEXTREL` 标志。

**`now`** 设置 `DF_BIND_NOW` 标志，指示运行时加载器应在对象初始化时执行所有重定位处理。默认情况下，重定位可按需执行。

**`origin`** 设置 `DF_ORIGIN` 标志，指示该对象需要 $ORIGIN 处理。

**`pac-plt`** 仅限 AArch64，在 PLT 中使用指针认证。

**`pack-relative-relocs`** 类似于 `-pack-dyn-relocs=relr`，但如果存在 GLIBC_2.* 版本依赖，则合成 GLIBC_ABI_DT_RELR 版本依赖。glibc ld.so 拒绝加载没有 GLIBC_ABI_DT_RELR 版本依赖的动态链接对象。

**`rel`** 对动态重定位使用 REL 格式。

**`rela`** 对动态重定位使用 RELA 格式。

**`retpolineplt`** 发出 retpoline 格式的 PLT 条目，作为 CVE-2017-5715 的缓解措施。

**`rodynamic`** 使 `.dynamic` 节为只读。不发出 `DT_DEBUG` 标签。

**`separate-loadable-segments`**

**`separate-code`**

**`noseparate-code`** 指定两个相邻的 PT_LOAD 段是否允许在页面中重叠。`noseparate-code`（默认）允许重叠。`separate-code` 允许两个可执行段之间或两个非可执行段之间的重叠。`separate-loadable-segments` 不允许重叠。

**`shstk`** 仅限 x86，使用影子栈。

**`stack-size`** =`size` 将主线程的栈大小设置为 `size`。栈大小记录为 `PT_GNU_STACK` 程序段的大小。

**`start-stop-gc`** 不让 __start_/__stop_ 引用保留关联的 C 标识符名节（默认）。

**`nostart-stop-gc`** 让 __start_/__stop_ 引用保留关联的 C 标识符名节。

**`text`** 不允许对只读段进行重定位。这是默认值。

**`nobtcfi`** 创建 `PT_OPENBSD_NOBTCFI` 段。

**`wxneeded`** 创建 `PT_OPENBSD_WXNEEDED` 段。

## 环境变量

**`LLD_REPRODUCE`** 以指定文件名创建重现 tar 包。如果指定了 `--reproduce`，则 `--reproduce` 优先。

**`LLD_VERSION`** ld.lld 创建一个名为 `.comment` 的节，其中包含 LLD 版本字符串。版本字符串可由此环境变量覆盖，这在消除由 LLD 版本号差异导致的二进制文件差异时很有用。

## 实现说明

ld.lld 对归档文件（扩展名为 **.a** 的文件）的处理与 Unix 系统上使用的传统链接器不同。

传统链接器在链接期间维护一组未定义符号。链接器按文件在命令行上出现的顺序处理每个文件，直到未定义符号集为空。目标文件在遇到时被链接到输出对象中，其未定义符号被添加到集合中。遇到归档文件时，传统链接器搜索其中包含的目标，并处理满足未解析集合中符号的那些目标。

使用传统链接器时，处理相互依赖的归档可能比较麻烦。可能需要多次指定归档文件，或者使用特殊的命令行选项 `--start-group` 和 `--end-group` 让链接器在组中的文件上循环，直到没有新符号被添加到集合中。

ld.lld 在遍历命令行参数时记录在目标和归档中找到的所有符号。当 ld.lld 遇到可由先前处理的归档文件中包含的目标文件解析的未定义符号时，它会立即提取并将其链接到输出对象中。

对于某些归档输入，ld.lld 可能产生与传统链接器不同的结果。在实践中，大量第三方软件已使用 ld.lld 链接，没有出现重大问题。

`--warn-backrefs` 选项可用于识别可能与传统 Unix 链接器行为不兼容的链接器调用。
