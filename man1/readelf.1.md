# readelf(1)

`readelf` — 显示 ELF 对象的相关信息

## 名称

`readelf`

## 概要

`readelf [-a | --all] [-c | --archive-index] [-d | --dynamic] [-e | --headers] [-g | --section-groups] [-h | --file-header] [-l | --program-headers] [-n | --notes] [-p section | --string-dump=section] [-r | --relocs] [-t | --section-details] [-u | --unwind] [-v | --version] [-w[afilmoprsFLR] | --debug-dump[=long-option-name,...]] [-x section | --hex-dump=section] [-z | --decompress] [-A | --arch-specific] [-D | --use-dynamic] [-H | --help] [-I | --histogram] [-N | --full-section-name] [-S | --sections | --section-headers] [-V | --version-info] [-W | --wide] file ...`

## 描述

`readelf` 实用程序显示 ELF 对象和 [ar(1)](ar.1.md) 归档的相关信息。

`readelf` 实用程序识别以下选项：

**`-a |`** `--all` 启用以下标志：`-d`、`-h`、`-I`、`-l`、`-n`、`-r`、`-s`、`-u`、`-A`、`-S` 和 `-V`。

**`-c |`** `--archive-index` 打印归档的归档符号表。

**`-d |`** `--dynamic` 打印 ELF 对象中 `SHT_DYNAMIC` 节的内容。

**`-e |`** `--headers` 打印 ELF 对象中的所有程序头、文件头和节头。

**`-g |`** `--section-groups` 打印 ELF 对象中节组的内容。

**`-h |`** `--file-header` 打印 ELF 对象的文件头。

**`-l |`** `--program-headers` 打印对象的程序头表内容。

**`-n |`** `--notes` 打印 ELF 对象中存在的 `PT_NOTE` 段或 `SHT_NOTE` 节的内容。

**`-p`** `section |` `--string-dump`=`section` 以可打印字符串形式打印指定节的内容。参数 `section` 应为节名或数字节索引。

**`-r |`** `--relocs` 打印重定位信息。

**`-s |`** `--syms |` `--symbols` 打印符号表。

**`-t |`** `--section-details` 打印关于节的附加信息，例如节头中的标志字段。隐含 `-S`。

**`-u |`** `--unwind` 尚未实现（选项被接受但被忽略）。

**`-v |`** `--version` 打印 `readelf` 的版本标识并退出。

**`-w`** `[afilmoprsFLR]` `--debug-dump`[=`long-option-name`,...] 显示 DWARF 信息。`-w` 选项与下表中的短选项一起使用；`--debug-dump` 选项与对应长选项名的逗号分隔列表一起使用：

| 短选项 | 长选项 | 描述 |
| --- | --- | --- |
| a | abbrev | 显示缩写信息。 |
| f | frames | 显示帧信息，显示帧指令。 |
| i | info | 显示调试信息条目。 |
| l | rawline | 以原始形式显示行信息。 |
| m | macro | 显示宏信息。 |
| o | loc | 显示位置列表信息。 |
| p | pubnames | 显示全局名称。 |
| r | aranges\|ranges | 显示地址范围信息。 |
| s | str | 显示调试字符串表。 |
| F | frames-interp | 显示帧信息，显示寄存器规则。 |
| L | decodedline | 以解码形式显示行信息。 |
| R | Ranges | 显示范围列表。 |

如果未指定子选项，默认显示与 `a`、`f`、`i`、`l`、`o`、`p`、`r`、`s` 和 `R` 短选项对应的信息。

**`-x`** `section |` `--hex-dump`=`section` 以十六进制形式显示指定节的内容。参数 `section` 应为节名或数字节索引。

**`-z |`** `--decompress` 在显示前解压缩由 `-x` 或 `-p` 指定的节的内容。如果指定节未压缩，则按原样显示。

**`-A |`** `--arch-specific` 该选项被接受但目前未实现。

**`-D |`** `--use-dynamic` 打印由“`.dynamic`”节中 `DT_SYMTAB` 条目指定的符号表。

**`-H |`** `--help` 打印帮助信息。

**`-I |`** `--histogram` 为 `SHT_HASH` 和 `SHT_GNU_HASH` 类型的节打印桶列表长度信息。

**`-N |`** `--full-section-name` 该选项被接受但目前未实现。

**`-S |`** `--sections |` `--section-headers` 打印每个 ELF 对象的节头信息。

**`-V |`** `--version-info` 打印符号版本信息。

**`-W |`** `--wide` 每个结构使用一行长行打印 ELF 结构信息。如果未指定此选项，`readelf` 将在 64 位 ELF 对象的头中以两行分别列出信息。

## 退出状态

`readelf` 实用程序成功时退出码为 0，发生错误时大于 0。

## 参见

nm(1), [addr2line(1)](llvm-addr2line.1.md), elfcopy(1),

## 作者

`readelf` 实用程序由 Kai Wang <kaiwang27@users.sourceforge.net> 编写。
