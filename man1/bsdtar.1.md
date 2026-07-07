# bsdtar(1)

`tar` — 操作磁带归档

## 名称

`tar`

## 概要

`tar [bundled-flags <args>] [<file> | <pattern> ...]`
`tar {-c} [options] [files | directories]`
`tar {-r | -u} -f archive-file [options] [files | directories]`
`tar {-t | -x} [options] [patterns]`

## 描述

`tar` 用于创建和操作流式归档文件。本实现可从 tar、pax、cpio、zip、jar、ar、xar、rar、rpm、7-zip 和 ISO 9660 cdrom 镜像中提取，并能创建 tar、pax、cpio、ar、zip、7-zip 和 shar 归档。

第一种概要形式展示了一个“bundled”（捆绑式）选项字。提供此用法是为了与历史实现兼容。详情参见下文 COMPATIBILITY 章节。

其他概要形式展示了推荐的用法。`tar` 的第一个选项是以下列表中的模式指示符：

**`-c`** 创建包含指定项的新归档。长选项形式为 `--create`。

**`-r`** 类似于 `-c`，但新条目会被追加到归档中。注意，这仅适用于存储在常规文件中的未压缩归档。必须使用 `-f` 选项。长选项形式为 `--append`。

**`-t`** 将归档内容列表输出到 stdout。长选项形式为 `--list`。

**`-u`** 类似于 `-r`，但仅在条目的修改日期比归档中对应条目更新时才添加。注意，这仅适用于存储在常规文件中的未压缩归档。必须使用 `-f` 选项。长选项形式为 `--update`。

**`-x`** 从归档中提取到磁盘。如果归档中多次出现同名文件，每个副本都会被提取，后提取的副本会覆盖（替换）先前的副本。长选项形式为 `--extract`。

在 `-c`、`-r` 或 `-u` 模式下，每个指定的文件或目录按命令行中的顺序添加到归档中。默认情况下，每个目录的内容也会被归档。

在提取或列表模式下，整个命令行会在归档打开前被读取和解析。命令行上的路径名或模式指示应处理归档中的哪些项。模式是 shell 风格的 glob 匹配模式，参见 [tcsh(1)](csh.1.md)。

## 选项

除非另有说明，选项适用于所有操作模式。

```sh
tar -cf - newfile @original.tar
```

```sh
tar -cf - newfile original.tar
```

```sh
tar -czf - --format pax @-
```

```sh
tar -acf archive.tgz source.c source.h
```

```sh
tar -af archive.tar.bz2.uu source.c source.h
```

```sh
tar -af archive.zip source.c source.h
```

```sh
tar -ajcf archive.tgz source.c source.h
```

```sh
tar -ajcf archive.xxx source.c source.h
```

```sh
tar -cf new.tar --include='*foo*' @old.tgz
```

**`key=value`** 在每个支持该 key 的模块中将 key 设置为指定值。不支持此 key 的模块将忽略它。

**`key`** 在每个支持该 key 的模块中启用该 key。等效于 `key=1`。

**`!key`** 在每个支持该 key 的模块中禁用该 key。

**`module:key=value`**、**`module:key`**、**`module:!key`** 同上，但相应的 key 和 value 仅提供给名称与 `module` 匹配的模块。

**`iso9660:joliet`** 支持 Joliet 扩展。默认启用，使用 `!joliet` 或 `iso9660:!joliet` 禁用。

**`iso9660:rockridge`** 支持 Rock Ridge 扩展。默认启用，使用 `!rockridge` 或 `iso9660:!rockridge` 禁用。

**`gzip:compression-level`** 1 到 9 的十进制整数，指定 gzip 压缩级别。

**`gzip:timestamp`** 存储时间戳。默认启用，使用 `!timestamp` 或 `gzip:!timestamp` 禁用。

**`lrzip:compression`**=`type` 使用 `type` 作为压缩方法。支持的值有 bzip2、gzip、lzo（极快）和 zpaq（最佳，但极慢）。

**`lrzip:compression-level`** 1 到 9 的十进制整数，指定 lrzip 压缩级别。

**`lz4:compression-level`** 1 到 9 的十进制整数，指定 lzop 压缩级别。

**`lz4:stream-checksum`** 启用流校验和。默认启用，使用 `lz4:!stream-checksum` 禁用。

**`lz4:block-checksum`** 启用块校验和（默认禁用）。

**`lz4:block-size`** 4 到 7 的十进制整数，指定 lz4 压缩块大小（默认为 7）。

**`lz4:block-dependence`** 使用正在压缩的块的前一个块作为压缩字典，以提高压缩率。

**`zstd:compression-level`**=`N` 十进制整数，指定 zstd 压缩级别。支持的值取决于库版本，常见值为 1 到 22。

**`zstd:threads`**=`N` 指定要使用的工作线程数，或设为 0 以使用与系统 CPU 核心数相同的线程数。

**`zstd:frame-per-file`** 在归档中每个文件开头启动新的压缩帧。

**`zstd:min-frame-in`**=`N` 与 `zstd:frame-per-file` 配合使用，仅当当前帧的未压缩大小至少为 `N` 字节时才启动新的压缩帧。数字后可跟 `k`/`kB`、`M`/`MB` 或 `G`/`GB` 分别表示千字节、兆字节或吉字节。

**`zstd:min-frame-out`**=`N`、**`zstd:min-frame-size`**=`N` 与 `zstd:frame-per-file` 配合使用，仅当当前帧的压缩大小至少为 `N` 字节时才启动新的压缩帧。数字后可跟 `k`/`kB`、`M`/`MB` 或 `G`/`GB` 分别表示千字节、兆字节或吉字节。

**`zstd:max-frame-in`**=`N`、**`zstd:max-frame-size`**=`N` 在当前帧的未压缩大小超过 `N` 字节后尽快启动新的压缩帧。数字后可跟 `k`/`kB`、`M`/`MB` 或 `G`/`GB` 分别表示千字节、兆字节或吉字节。小于 1024 的值将被拒绝。

**`zstd:max-frame-out`**=`N` 在当前帧的压缩大小超过 `N` 字节后尽快启动新的压缩帧。数字后可跟 `k`/`kB`、`M`/`MB` 或 `G`/`GB` 分别表示千字节、兆字节或吉字节。小于 1024 的值将被拒绝。

**`lzop:compression-level`** 1 到 9 的十进制整数，指定 lzop 压缩级别。

**`xz:compression-level`** 0 到 9 的十进制整数，指定 xz 压缩级别。

**`xz:threads`** 指定要使用的工作线程数。将 threads 设为特殊值 0 时，[xz(1)](xz.1.md) 会使用与系统 CPU 核心数相同的线程数。

**`mtree:`**`keyword` mtree 写入器模块允许指定输出中包含哪些 mtree 关键字。支持的关键字包括：`cksum`、`device`、`flags`、`gid`、`gname`、`indent`、`link`、`md5`、`mode`、`nlink`、`rmd160`、`sha1`、`sha256`、`sha384`、`sha512`、`size`、`time`、`uid`、`uname`。默认等效于：“device, flags, gid, gname, link, mode, nlink, size, time, type, uid, uname”。

**`mtree:all`** 启用上述所有关键字。也可使用 `mtree:!all` 禁用所有关键字。

**`mtree:use-set`** 在输出中启用 `/set` 行的生成。

**`mtree:indent`** 通过缩进选项并将行拆分以适应 80 列来生成易读输出。

**`zip:compression`**=`type` 使用 `type` 作为压缩方法。支持的值有 store（未压缩）和 deflate（gzip 算法）。

**`zip:encryption`** 使用传统 zip 加密启用加密。

**`zip:encryption`**=`type` 使用 `type` 作为加密类型。支持的值有 zipcrypt（传统 zip 加密）、aes128（WinZip AES-128 加密）和 aes256（WinZip AES-256 加密）。

**`read_concatenated_archives`** 忽略归档中的零块，这种情况出现在多个 tar 归档被连接在一起时。不使用此选项时，仅会读取第一个连接归档的内容。此选项类似于 GNU tar 的 `-i`、`--ignore-zeros` 选项。

**`@`** `archive`（仅 c 和 r 模式）打开指定归档，其中的条目将被追加到当前归档。例如，`tar -cf - newfile @original.tar` 将一个新归档写入标准输出，其中包含文件 `newfile` 和 `original.tar` 中的所有条目。相比之下，`tar -cf - newfile original.tar` 创建一个仅包含两个条目的新归档。类似地，`tar -czf - --format pax @-` 从标准输入读取归档（格式自动确定），并将其转换为 gzip 压缩的 pax 格式归档输出到 stdout。通过这种方式，`tar` 可用于在不同格式之间转换归档。

**`-a`**、**`--auto-compress`**（仅 c 模式）根据归档后缀决定格式和压缩方式。例如，`tar -acf archive.tgz source.c source.h` 创建一个使用受限 pax 格式和 gzip 压缩的新归档；`tar -af archive.tar.bz2.uu source.c source.h` 创建一个使用受限 pax 格式和 bzip2 压缩及 uuencode 压缩的新归档；`tar -af archive.zip source.c source.h` 创建一个 zip 格式的新归档；`tar -ajcf archive.tgz source.c source.h` 忽略 “-j” 选项，创建一个使用受限 pax 格式和 gzip 压缩的新归档；`tar -ajcf archive.xxx source.c source.h` 当后缀未知或无后缀时，创建一个使用受限 pax 格式和 bzip2 压缩的新归档。

**`--acls`**（仅 c、r、u、x 模式）归档或提取 POSIX.1e 或 NFSv4 ACL。这是 `-no-acls` 的反向选项，也是 c、r 和 u 模式下（Mac OS X 除外）或 `tar` 以 root 身份在 x 模式下运行时的默认行为。在 Mac OS X 上，此选项将扩展 ACL 转换为 NFSv4 ACL。要存储扩展 ACL，推荐使用 `--mac-metadata` 选项。

**`-B`**、**`--read-full-blocks`** 为兼容其他 [tar(1)](bsdtar.1.md) 实现而忽略。

**`-b`** `blocksize`、**`--block-size`** `blocksize` 指定磁带驱动器 I/O 的块大小（以 512 字节记录为单位）。通常，此参数仅在从磁带驱动器读取或写入时才需要，且通常即使那时也不需要，因为默认块大小为 20 条记录（10240 字节）非常常见。

**`-C`** `directory`、**`--cd`** `directory`、**`--directory`** `directory` 在 c 和 r 模式下，添加后续文件前更改目录。在 x 模式下，打开归档后、提取条目前更改目录。

**`--chroot`**（仅 x 模式）在处理任何 `-C` 选项后、提取任何文件前，chroot() 到当前目录。

**`--clamp-mtime`**（与 `--mtime` 配合使用）仅当文件比 `--mtime` 中指定的日期更新时才设置修改时间。

**`--clear-nochange-fflags`**（仅 x 模式）在删除文件系统对象以替换它们之前，清除可能阻止删除的特定平台文件属性或文件标志。

**`--exclude`** `pattern` 不处理与指定模式匹配的文件或目录。注意，排除优先于命令行上指定的模式或文件名。

**`--exclude-vcs`** 不处理版本控制系统 ‘Arch’、‘Bazaar’、‘CVS’、‘Darcs’、‘Mercurial’、‘RCS’、‘SCCS’、‘SVN’ 和 ‘git’ 内部使用的文件或目录。

**`--fflags`**（仅 c、r、u、x 模式）归档或提取特定平台的文件属性或文件标志。这是 `--no-fflags` 的反向选项，也是 c、r 和 u 模式下或 `tar` 以 root 身份在 x 模式下运行时的默认行为。

**`--format`** `format`（仅 c、r、u 模式）为创建的归档使用指定格式。支持的格式包括 “cpio”、“pax”、“shar” 和 “ustar”。可能还支持其他格式；参见 libarchive-formats(5) 了解当前支持的格式。在 r 和 u 模式下扩展现有归档时，此处指定的格式必须与磁盘上现有归档的格式兼容。

**`-f`** `file`、**`--file`** `file` 从指定文件读取归档或将归档写入指定文件。文件名可以是 `-` 表示标准输入或标准输出。默认值因系统而异；在 FreeBSD 上默认为 **/dev/sa0**，在 Linux 上默认为 **/dev/st0**。

**`--gid`** `id` 使用提供的组 ID 号。提取时，这会覆盖归档中的组 ID；归档中的组名将被忽略。创建时，这会覆盖从磁盘读取的组 ID；如果未同时指定 `--gname`，组名将被设置为与组 ID 匹配。

**`--gname`** `name` 使用提供的组名。提取时，这会覆盖归档中的组名；如果系统上不存在提供的组名，则使用组 ID（来自归档或 `--gid` 选项）。创建时，这会设置存储在归档中的组名；该名称不会与系统组数据库进行验证。

**`--group`** `name`[:`gid`] 使用提供的组，如果未提供 `gid`，`name` 可以是组名或数字 ID。参见 `--gname` 选项的详细说明。

**`-H`**（仅 c 和 r 模式）命令行上指定的符号链接将被跟随；归档的是链接目标，而非链接本身。

**`-h`**（仅 c 和 r 模式）`-L` 的同义词。

**`-I`** `-T` 的同义词。

**`--help`** 显示用法。

**`--hfsCompression`**（仅 x 模式）Mac OS X 特有（v10.6 或更高版本）。使用 HFS+ 压缩压缩提取的常规文件。

**`--ignore-zeros`** 为兼容 GNU tar，`--options read_concatenated_archives` 的别名。

**`--include`** `pattern` 仅处理与指定模式匹配的文件或目录。注意，`--exclude` 指定的排除优先于包含。如果未显式指定包含，默认处理所有条目。`--include` 选项在过滤归档时特别有用。例如，命令 `tar -cf new.tar --include='*foo*' @old.tgz` 创建一个新归档 `new.tar`，其中仅包含 `old.tgz` 中包含字符串 ‘foo’ 的条目。

**`-J`**、**`--xz`**（仅 c 模式）使用 [xz(1)](xz.1.md) 压缩生成的归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 XZ 压缩。

**`-j`**、**`--bzip`**、**`--bzip2`**、**`--bunzip2`**（仅 c 模式）使用 bzip2(1) 压缩生成的归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 bzip2 压缩。

**`-k`**、**`--keep-old-files`**（仅 x 模式）不覆盖现有文件。特别是，如果归档中多次出现同一文件，后提取的副本不会覆盖先前的副本。

**`--keep-newer-files`**（仅 x 模式）不覆盖比正在提取的归档中版本更新的现有文件。

**`-L`**、**`--dereference`**（仅 c 和 r 模式）所有符号链接都将被跟随。通常，符号链接原样归档。使用此选项时，将归档链接目标。

**`-l`**、**`--check-links`**（仅 c 和 r 模式）除非每个文件的所有链接都已归档，否则发出警告消息。

**`--lrzip`**（仅 c 模式）使用 lrzip(1) 压缩生成的归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 lrzip 压缩。

**`--lz4`**（仅 c 模式）在写入前使用 lz4 兼容的压缩方式压缩归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 lz4 压缩。

**`--zstd`**（仅 c 模式）在写入前使用 zstd 兼容的压缩方式压缩归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 zstd 压缩。

**`--lzma`**（仅 c 模式）使用原始 LZMA 算法压缩生成的归档。在提取或列表模式下，此选项被忽略。不鼓励使用此选项，新归档应使用 `--xz` 创建。注意，此 `tar` 实现在读取归档时会自动识别 LZMA 压缩。

**`--lzop`**（仅 c 模式）使用 lzop(1) 压缩生成的归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 LZO 压缩。

**`-m`**、**`--modification-time`**（仅 x 模式）不提取修改时间。默认情况下，修改时间设置为归档中存储的时间。

**`--mac-metadata`**（仅 c、r、u 和 x 模式）Mac OS X 特有。使用 copyfile(3) 以 AppleDouble 格式归档或提取扩展 ACL 和扩展文件属性。这是 `--no-mac-metadata` 的反向选项，也是 c、r 和 u 模式下或 `tar` 以 root 身份在 x 模式下运行时的默认行为。目前仅支持 pax 格式（包括 pax restricted，即 `bsdtar` 的默认 tar 格式）。

**`--mtime`** `date`（仅 c、r、u 模式）将添加文件的修改时间设置为指定日期。

**`-n`**、**`--norecurse`**、**`--no-recursion`** 不对目录内容递归操作。

**`--newer`** `date`（仅 c、r、u 模式）仅包含比指定日期更新的文件和目录。比较 ctime 条目。

**`--newer-mtime`** `date`（仅 c、r、u 模式）类似于 `--newer`，但比较 mtime 条目而非 ctime 条目。

**`--newer-than`** `file`（仅 c、r、u 模式）仅包含比指定文件更新的文件和目录。比较 ctime 条目。

**`--newer-mtime-than`** `file`（仅 c、r、u 模式）类似于 `--newer-than`，但比较 mtime 条目而非 ctime 条目。

**`--nodump`**（仅 c 和 r 模式）通过跳过此文件来遵守 nodump 文件标志。

**`--nopreserveHFSCompression`**（仅 x 模式）Mac OS X 特有（v10.6 或更高版本）。不压缩那些在归档前已使用 HFS+ 压缩压缩过的提取常规文件。默认情况下，再次使用 HFS+ 压缩压缩常规文件。

**`--null`**（与 `-I` 或 `-T` 配合使用）文件名或模式以 null 字符分隔，而非以换行符分隔。这通常用于读取 [find(1)](find.1.md) 的 `-print0` 选项输出的文件名。

**`--no-acls`**（仅 c、r、u、x 模式）不归档或提取 POSIX.1e 或 NFSv4 ACL。这是 `--acls` 的反向选项，也是 `bsdtar` 在 x 模式下以非 root 身份运行时的默认行为（在 Mac OS X 上为 c、r、u 和 x 模式下任意用户）。

**`--no-fflags`**（仅 c、r、u、x 模式）不归档或提取文件属性或文件标志。这是 `--fflags` 的反向选项，也是 `bsdtar` 在 x 模式下以非 root 身份运行时的默认行为。

**`--no-mac-metadata`**（仅 c、r、u 和 x 模式）Mac OS X 特有。不使用 copyfile(3) 以 AppleDouble 格式归档或提取 ACL 和扩展文件属性。这是 `--mac-metadata` 的反向选项，也是 `bsdtar` 在 x 模式下以非 root 身份运行时的默认行为。

**`--no-read-sparse`**（仅 c、r、u 模式）不从磁盘读取稀疏文件信息。这是 `--read-sparse` 的反向选项。

**`--no-safe-writes`**（仅 x 模式）不创建临时文件并使用 rename(2) 替换原始文件。这是 `--safe-writes` 的反向选项。

**`--no-same-owner`**（仅 x 模式）不提取所有者和组 ID。这是 `--same-owner` 的反向选项，也是 `bsdtar` 以非 root 身份运行时的默认行为。

**`--no-same-permissions`**（仅 x 模式）不提取完整权限（SGID、SUID、粘滞位、文件属性或文件标志、扩展文件属性和 ACL）。这是 `-p` 的反向选项，也是 `bsdtar` 以非 root 身份运行时的默认行为。

**`--no-xattrs`**（仅 c、r、u、x 模式）不归档或提取扩展文件属性。这是 `--xattrs` 的反向选项，也是 `bsdtar` 在 x 模式下以非 root 身份运行时的默认行为。

**`--numeric-owner`** 等效于 `--uname` "" `--gname` ""。提取时，它使归档中的用户和组名被忽略，使用数字用户和组 ID。创建时，它使用户和组名不存储在归档中。

**`-O`**、**`--to-stdout`**（仅 x、t 模式）在提取（-x）模式下，文件将写入标准输出而非提取到磁盘。在列表（-t）模式下，文件列表将写入 stderr 而非通常的 stdout。

**`-o`**（x 模式）使用运行该程序的用户的用户和组，而非归档中指定的。注意，除非指定了 `-p` 且程序由 root 用户运行，否则此选项无意义。在这种情况下，归档中的文件模式和标志将被恢复，但归档中的 ACL 或所有者信息将被丢弃。

**`-o`**（c、r、u 模式）`--format ustar` 的同义词。

**`--older`** `date`（仅 c、r、u 模式）仅包含比指定日期更早的文件和目录。比较 ctime 条目。

**`--older-mtime`** `date`（仅 c、r、u 模式）类似于 `--older`，但比较 mtime 条目而非 ctime 条目。

**`--older-than`** `file`（仅 c、r、u 模式）仅包含比指定文件更早的文件和目录。比较 ctime 条目。

**`--older-mtime-than`** `file`（仅 c、r、u 模式）类似于 `--older-than`，但比较 mtime 条目而非 ctime 条目。

**`--one-file-system`**（仅 c、r 和 u 模式）不跨越挂载点。

**`--options`** `options` 为特定模块选择可选行为。参数是包含逗号分隔关键字和值的文本字符串。这些内容传递给处理特定格式的模块以控制这些格式的行为。每个选项采用以下形式之一：创建和追加模式支持的模块和 key 的完整列表参见 archive_write_set_options(3)，提取和列表模式参见 archive_read_set_options(3)。支持选项的示例：如果提供的选项未被任何模块支持，则为致命错误。

**`-P`**、**`--absolute-paths`** 保留路径名。默认情况下，创建归档和从归档提取时，绝对路径名（以 / 字符开头的）会去除前导斜杠。此外，`bsdtar` 会拒绝提取路径名包含 `..` 或其目标目录会被符号链接更改的归档条目。此选项抑制这些行为。

**`-p`**、**`--insecure`**、**`--preserve-permissions`**（仅 x 模式）保留文件权限。尝试为从归档提取的每个项恢复完整权限，包括文件模式、文件属性或文件标志、扩展文件属性和 ACL（如果可用）。这是 `--no-same-permissions` 的反向选项，也是 `bsdtar` 以 root 身份运行时的默认行为。可以通过同时指定 `--no-acls`、`--no-fflags`、`--no-mac-metadata` 或 `--no-xattrs` 部分覆盖。

**`--passphrase`** `passphrase` `passphrase` 用于提取或创建加密归档。目前，zip 是唯一支持加密的格式。除非你了解使用此选项的不安全性，否则不应使用此选项。

**`--posix`**（仅 c、r、u 模式）`--format pax` 的同义词。

**`-q`**、**`--fast-read`**（仅 x 和 t 模式）仅提取或列出每个模式或文件名操作数匹配的第一个归档条目。每个指定模式或文件名匹配后即退出。默认情况下，归档始终读取到末尾，因为可能存在多个同名条目，且按约定后出现的条目覆盖先前的条目。此选项作为性能优化提供。

**`--read-sparse`**（仅 c、r、u 模式）从磁盘读取稀疏文件信息。这是 `--no-read-sparse` 的反向选项，也是默认行为。

**`-S`**（仅 x 模式）将文件提取为稀疏文件。对于磁盘上的每个块，首先检查它是否仅包含 NULL 字节，如果是则跳过。这与 dd 的 conv=sparse 选项类似。

**`-s`** `pattern` 根据 `pattern` 修改文件或归档成员名称。模式格式为 `/old/new/`[bghHprRsS]，其中 `old` 是基本正则表达式，`new` 是匹配部分的替换字符串，可选的尾部字母修改替换处理方式。如果 `old` 不匹配，则跳过该模式。在 `new` 中，~ 被替换为匹配内容，e1 到 e9 被替换为相应捕获组的内容。可选的尾部 g 指定匹配应在匹配部分后继续，并在第一个不匹配的模式处停止。可选的尾部 s 指定模式应用于符号链接的值。可选的尾部 p 指定成功替换后应将原始路径名和新路径名打印到标准错误。可选的尾部 b 指定替换应从字符串开头匹配，而非从前一个匹配替换结束位置之后开始。可选的尾部 H、R 或 S 字符分别抑制对硬链接目标、常规文件名或符号链接目标的替换。可选的尾部 h、r 或 s 字符分别启用对硬链接目标、常规文件名或符号链接目标的替换。默认为 `hrs`，即对所有名称应用替换。特别是，无需指定 h、r 或 s。

**`--safe-writes`**（仅 x 模式）以原子方式提取文件。默认情况下，`bsdtar` 会删除与提取文件同名的原始文件（如果存在），然后立即以同名创建并写入。在短时间内，尝试访问该文件的应用程序可能找不到它，或看到不完整的结果。如果启用 `--safe-writes`，`bsdtar` 首先创建一个唯一的临时文件，然后将新内容写入临时文件，最后使用 rename(2) 原子地将临时文件重命名为最终名称。这确保访问文件的应用程序在任何时候都能看到旧内容或新内容。

**`--same-owner`**（仅 x 模式）提取所有者和组 ID。这是 `--no-same-owner` 的反向选项，也是 `bsdtar` 以 root 身份运行时的默认行为。

**`--strip-components`** `count` 移除指定数量的前导路径元素。路径元素较少的路径名将被静默跳过。注意，路径名在检查包含/排除模式后、安全检查前被编辑。

**`-T`** `filename`、**`--files-from`** `filename` 在 x 或 t 模式下，`bsdtar` 将从 `filename` 读取要提取的名称列表。在 c 模式下，`bsdtar` 将从 `filename` 读取要归档的名称。单独一行上的特殊名称 “-C” 会将当前目录更改为下一行指定的目录。除非指定 `--null`，否则名称以换行符分隔。注意，`--null` 还会禁用对包含 “-C” 的行的特殊处理。注意：如果使用 [find(1)](find.1.md) 生成文件列表，你可能也需要使用 `-n`。

**`--totals`**（仅 c、r、u 模式）归档所有文件后，将摘要打印到 stderr。

**`-U`**、**`--unlink`**、**`--unlink-first`**（仅 x 模式）创建文件前先删除。如果大多数文件已存在，这可以作为小的性能优化，但如果大多数文件不存在，可能会使速度变慢。此标志还导致 `bsdtar` 删除中间的目录符号链接，而非报告错误。详情参见下文 SECURITY 章节。

**`--uid`** `id` 使用提供的用户 ID 号并忽略归档中的用户名。创建时，如果未同时指定 `--uname`，用户名将被设置为与用户 ID 匹配。

**`--uname`** `name` 使用提供的用户名。提取时，这会覆盖归档中的用户名；如果系统上不存在提供的用户名，则忽略它并使用用户 ID（来自归档或 `--uid` 选项）。创建时，这会设置存储在归档中的用户名；该名称不会与系统用户数据库进行验证。

**`--use-compress-program`** `program` 通过 `program` 管道传输输入（x 或 t 模式）或输出（c 模式），而非使用内建的压缩支持。

**`--owner`** `name`[:`uid`] 使用提供的用户，如果未提供 `uid`，`name` 可以是用户名或数字 ID。参见 `--uname` 选项的详细说明。

**`-v`**、**`--verbose`** 生成详细输出。在创建和提取模式下，`bsdtar` 会列出每个从归档读取或写入归档的文件名。在列表模式下，`bsdtar` 会生成类似于 [ls(1)](ls.1.md) 的输出。额外的 `-v` 选项还将在创建和提取模式下提供类似 ls 的详细信息。

**`--version`** 打印 `bsdtar` 和 `libarchive` 的版本并退出。

**`-w`**、**`--confirmation`**、**`--interactive`** 对每个操作请求确认。

**`-X`** `filename`、**`--exclude-from`** `filename` 从指定文件读取排除模式列表。参见 `--exclude` 了解排除处理的更多信息。

**`--xattrs`**（仅 c、r、u、x 模式）归档或提取扩展文件属性。这是 `--no-xattrs` 的反向选项，也是 c、r 和 u 模式下或 `libarchive` 在 x 模式下以 root 身份运行时的默认行为。

**`-y`**（仅 c 模式）使用 bzip2(1) 压缩生成的归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 bzip2 压缩。

**`-Z`**、**`--compress`**、**`--uncompress`**（仅 c 模式）使用 compress(1) 压缩生成的归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 compress 压缩。

**`-z`**、**`--gunzip`**、**`--gzip`**（仅 c 模式）使用 [gzip(1)](gzip.1.md) 压缩生成的归档。在提取或列表模式下，此选项被忽略。注意，此 `tar` 实现在读取归档时会自动识别 gzip 压缩。

## 环境变量

以下环境变量影响 `tar` 的执行：

**`TAR_READER_OPTIONS`** 格式读取器和压缩读取器的默认选项。`--options` 选项会覆盖此值。

**`TAR_WRITER_OPTIONS`** 格式写入器和压缩写入器的默认选项。`--options` 选项会覆盖此值。

**`LANG`** 使用的区域设置。参见 [environ(7)](../man7/environ.7.md) 了解更多信息。

**`TAPE`** 默认设备。`-f` 选项会覆盖此值。请参见上文对 `-f` 选项的描述以了解更多详情。

**`TZ`** 显示日期时使用的时区。参见 [environ(7)](../man7/environ.7.md) 了解更多信息。

## 退出状态

`tar` 实用程序成功时退出值为 0，发生错误时退出值大于 0。

## 实例

以下命令创建一个名为 `file.tar.gz` 的新归档，其中包含两个文件 `source.c` 和 `source.h`：

```sh
tar -czf file.tar.gz source.c source.h
```

查看此归档的详细目录：

```sh
tar -tvf file.tar.gz
```

从默认磁带驱动器上的归档中提取所有条目：

```sh
tar -x
```

查看 ISO 9660 cdrom 镜像的内容：

```sh
tar -tf image.iso
```

移动文件层次结构，按如下方式调用 `tar`：

```sh
tar -cf - -C srcdir . | tar -xpf - -C destdir
```

或更传统的方式：

```sh
cd srcdir ; tar -cf - . | ( cd destdir ; tar -xpf - )
```

在创建模式下，要归档的文件和目录列表还可包含 `-C foo/baz` 形式的目录切换指令和 `@archive-file` 形式的归档包含。例如，命令行：

```sh
tar -cf new.tar foo1 @old.tgz -C /tmp foo2
```

将创建一个新归档 `new.tar`。`tar` 会从当前目录读取文件 `foo1` 并将其添加到输出归档。然后它会从 `old.tgz` 读取每个条目并将这些条目添加到输出归档。最后，它会切换到 **/tmp** 目录并将 `foo2` 添加到输出归档。

mtree(5) 格式的输入文件可用于创建具有任意所有权、权限或名称的输出归档，这些与磁盘上的现有数据不同：

```sh
$ cat input.mtree
#mtree
usr/bin uid=0 gid=0 mode=0755 type=dir
usr/bin/ls uid=0 gid=0 mode=0755 type=file content=myls
$ tar -cvf output.tar @input.mtree
```

`--newer` 和 `--newer-mtime` 开关接受各种常见的日期和时间规范，包括 “12 Mar 2005 7:14:29pm”、“2005-03-12 19:14”、“5 minutes ago” 和 “19:14 PST May 1”。

`--options` 参数可用于控制归档生成或读取的各种细节。例如，你可以生成仅包含 `type`、`time` 和 `uid` 关键字的 mtree 输出：

```sh
tar -cf file.tar --format=mtree --options='!all,type,time,uid' dir
```

或设置 gzip 或 xz 压缩使用的压缩级别：

```sh
tar -czf file.tar --options='compression-level=9'.
```

更多详情，参见 archive_read(3) 和 archive_write(3) 中描述的 archive_read_set_options() 和 archive_write_set_options() API 调用的说明。

## COMPATIBILITY

支持捆绑参数格式是为了与历史实现兼容。它由一个初始字（无前导 - 字符）组成，每个字符指示一个选项。参数作为单独的字跟随。参数的顺序必须与捆绑命令字中相应字符的顺序匹配。例如，

```sh
tar tbf 32 file.tar
```

指定三个标志 `t`、`b` 和 `f`。`b` 和 `f` 标志都需要参数，因此命令行上必须有两个附加项。`32` 是 `b` 标志的参数，`file.tar` 是 `f` 标志的参数。

模式选项 c、r、t、u 和 x 以及选项 b、f、l、m、o、v 和 w 符合 SUSv2。

为了最大可移植性，调用 `tar` 的脚本应使用上述捆绑参数格式，应限于 `c`、`t` 和 `x` 模式，以及 `b`、`f`、`m`、`v` 和 `w` 选项。

提供额外的长选项以改善与其他 tar 实现的兼容性。

## SECURITY

某些安全问题在许多归档程序中都很常见，包括 `tar`。特别是，精心制作的归档可以请求 `tar` 将文件提取到目标目录之外的位置。这可能被用于导致不知情的用户覆盖他们无意覆盖的文件。如果归档由超级用户提取，系统上的任何文件都可能被覆盖。这有三种发生方式。尽管 `tar` 有针对每种情况的保护机制，但明智的用户应意识到这些影响：

- 归档条目可以具有绝对路径名。默认情况下，`tar` 在恢复文件名前会去除前导 `/` 字符以防范此问题。
- 归档条目可以包含 `..` 组件的路径名。默认情况下，`tar` 不会提取路径名中包含 `..` 组件的文件。
- 归档条目可以利用符号链接将文件恢复到其他目录。归档可以将符号链接恢复到另一个目录，然后使用该链接将文件恢复到该目录。为防范此问题，`tar` 检查每个提取路径的符号链接。如果最终路径元素是符号链接，它将被删除并替换为归档条目。如果指定了 `-U`，任何中间符号链接也将被无条件删除。如果既未指定 `-U` 也未指定 `-P`，`tar` 将拒绝提取该条目。

为保护自己，你应警惕任何来自不可信来源的归档。你应在提取前使用以下命令检查归档内容：

```sh
tar -tf filename
```

应使用 `-k` 选项确保 `tar` 不会覆盖任何现有文件，或使用 `-U` 选项删除任何预先存在的文件。通常不应在具有超级用户权限时提取归档。注意，`tar` 的 `-P` 选项会禁用上述安全检查，并允许你在保留任何绝对路径名、`..` 组件或指向其他目录的符号链接的情况下提取归档。

## 参见

bzip2(1), compress(1), cpio(1), [gzip(1)](gzip.1.md), mt(1), [pax(1)](pax.1.md), shar(1), [xz(1)](xz.1.md), libarchive(3), libarchive-formats(5), tar(5)

## 标准

目前没有针对 tar 命令的 POSIX 标准；它曾出现在 ISO/IEC 9945-1:1996（“POSIX.1”）中，但在 IEEE Std 1003.1-2001（“POSIX.1”）中被删除。此实现支持的选项是通过对多个现有 tar 实现、旧的 tar POSIX 规范和当前的 pax POSIX 规范进行调查而开发的。

ustar 和 pax 交换文件格式由 IEEE Std 1003.1-2001（“POSIX.1”）为 pax 命令定义。

## 历史

`tar` 命令首次出现于 Seventh Edition Unix，于 1979 年 1 月发布。此后有许多其他实现，其中许多扩展了文件格式。John Gilmore 的 **pdtar** 公共领域实现（约 1987 年 11 月）颇具影响力，构成了 GNU tar 的基础。从 FreeBSD 1.0 开始，GNU tar 作为标准系统 tar 包含在 FreeBSD 中。

这是一个基于 libarchive(3) 库的完整重新实现。它首次随 FreeBSD 5.4 于 2005 年 5 月发布。

## 缺陷

本程序遵循 ISO/IEC 9945-1:1996（“POSIX.1”）对 `-l` 选项的定义。注意，1.15 版本之前的 GNU tar 将 `-l` 视为 `--one-file-system` 选项的同义词。

`-C` `dir` 选项可能与历史实现不同。

所有归档输出都以正确大小的块写入，即使输出正在被压缩。最后一个输出块是否填充到完整块大小因格式和输出设备而异。对于 tar 和 cpio 格式，如果输出正在写入标准输出或字符/块设备（如磁带驱动器），最后一个输出块会填充到完整块大小。如果输出正在写入常规文件，最后一个块不会被填充。许多压缩器，包括 [gzip(1)](gzip.1.md) 和 bzip2(1)，在解压 `tar` 创建的归档时会抱怨空填充，尽管它们仍能正确提取。

压缩和解压缩在内部实现，因此以下命令生成的压缩输出：

```sh
tar -czf - file
```

与以下命令生成的可能存在微小差异：

```sh
tar -cf - file | gzip
```

默认应该是向标准 I/O 路径读取和写入归档，但传统（和 POSIX）另有规定。

`r` 和 `u` 模式要求归档未压缩且位于磁盘上的常规文件中。其他归档可以使用 `c` 模式配合 `@archive-file` 扩展进行修改。

要归档名为 `@foo` 或 `-foo` 的文件，必须分别指定为 `./@foo` 或 `./-foo`。

在创建模式下，前导 `./` 总是被移除。除非指定 `-P` 选项，否则前导 `/` 会被去除。

在创建和提取时需要更好地支持文件选择。

目前尚不支持多卷归档。

使用 `@-` 约定在不同归档格式（如 tar 和 cpio）之间转换可能导致硬链接信息丢失。这是不同归档格式存储硬链接信息的方式不兼容的后果。
