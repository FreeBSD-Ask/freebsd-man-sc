  TAR(1)  

TAR(1)

FreeBSD General Commands Manual

TAR(1)

[名称](#__u540D___u79F0_)
=======================

`tar` —

操作磁带档案

[概要](#__u6982___u8981_)
=======================

`tar` \[bundled-flags ⟨args⟩\] \[⟨file⟩ | ⟨pattern⟩ ...\] `tar` {`-c`} \[options\] \[files | directories\] `tar` {`-r` | `-u`} `-f` archive-file \[options\] \[files | directories\] `tar` {`-t` | `-x`} \[options\] \[patterns\]

[描述](#__u63CF___u8FF0_)
=======================

`tar` 创建和操作流归档文件。 此实现可以从 tar, pax, cpio, zip, jar, ar, xar, rpm, 7-zip 和 ISO 9660 cdrom i映像中提取，并且可以创建 tar, pax, cpio, ar, zip, 7-zip 和 shar 档案.

第一个概要表格显示了一个 “bundled” 选项词。 提供此用法是为了与历史实现兼容。 有关详细信息，请参阅下面的兼容性。

其他概要形式显示了首选用法。 `tar` 的第一个选项是以下列表中的模式指示符：

[`-c`](#c)

创建包含指定项目的新存档。 长选项形式是 `-``-create` 。

[`-r`](#r)

与 `-c` 类似，但新条目会附加到存档中。 请注意，这仅适用于存储在常规文件中的未压缩存档。 `-f` 选项是必需的。 长选项形式是 `-``-append` 。

[`-t`](#t)

将存档内容列出到标准输出。 长选项形式是 `-``-list` 。

[`-u`](#u)

与 `-r` 类似，但仅当新条目的修改日期比存档中的相应条目新时才会添加新条目。 请注意，这仅适用于存储在常规文件中的未压缩存档。 `-f` 选项是必需的。 长格式是 `-``-update` 。

[`-x`](#x)

从存档中提取到磁盘。 如果同名文件在存档中多次出现，则将提取每个副本，之后的副本会覆盖（替换）之前的副本。 长选项形式是 `-``-extract` 。

在 `-c` `-、` `-r` 或 `-u` 模式下，每个指定的文件或目录都按命令行上指定的顺序添加到存档中。 默认情况下，每个目录的内容也会被归档。

在提取或列表模式下，在打开存档之前读取和解析整个命令行。 命令行上的路径名或模式指示应处理存档中的哪些项目。 模式是 tcsh(1) 中记录的 shell 样式的通配模式。

[选项](#__u9009___u9879_)
=======================

除非另有特别说明，否则选项适用于所有操作模式。

[`@`](#@)archive

（仅限 c 和 r 模式）打开指定的存档，其中的条目将附加到当前存档。 举个简单的例子，

````````` `tar` `-c` `-f` - newfile `@`original.tar`````````

将新存档写入标准输出，其中包含文件 newfile 和 original.tar 中的所有条目。 相比之下，

``````` `tar` `-c` `-f` - newfile original.tar```````

创建一个只有两个条目的新存档。相似地，

````````````` `tar` `-czf` - `-` `-format` `pax` `@`-`````````````

从标准输入读取存档（其格式将自动确定）并将其转换为标准输出上 gzip 压缩的 pax 格式存档。 这样， `tar` 可用于将档案从一种格式转换为另一种格式。

[`-a`](#a), `-``-auto-compress`

（仅限 c 模式）使用存档后缀来决定一组格式和压缩。举个简单的例子，

``````` `tar` `-a` `-cf` archive.tgz source.c source.h```````

创建一个具有受限 pax 格式和 gzip 压缩的新存档，

``````` `tar` `-a` `-cf` archive.tar.bz2.uu source.c source.h```````

创建一个具有受限 pax 格式和 bzip2 压缩和 uuencode 压缩的新存档，

``````` `tar` `-a` `-cf` archive.zip source.c source.h```````

创建一个 zip 格式的新存档，

``````` `tar` `-a` `-jcf` archive.tgz source.c source.h```````

忽略 “-j” 选项，并创建一个具有受限 pax 格式和 gzip 压缩的新存档，

``````` `tar` `-a` `-jcf` archive.xxx source.c source.h```````

如果它是未知后缀或没有后缀，则创建一个具有受限 pax 格式和 bzip2 压缩的新存档。

`-``-acls`

（仅限 c、r、u、x 模式）存档或提取 POSIX.1e 或 NFSv4 ACL。 这与 `-``-no-acls` 和 c、r 和 u 模式（Mac OS X 除外）或 `tar`-
以 root 身份在 x 模式下运行时的默认行为相反。 在 Mac OS X 上，此选项将扩展 ACL 转换为 NFSv4 ACL。 要存储扩展 ACL，首选 `-``-mac-metadata` 选项。

[`-B`](#B), `-``-read-full-blocks`

忽略与其他 tar(1) 实现的兼容性。

[`-b`](#b) blocksize, `-``-block-size` blocksize

指定磁带驱动器 I/O 的块大小（以 512 字节记录为单位）。 通常，只有在读取或写入磁带驱动器时才需要此参数，并且通常不需要，因为 20 条记录（10240 字节）的默认块大小非常常见。

[`-C`](#C) directory, `-``-cd` directory, `-``-directory` directory

在 c 和 r 模式下，这会在添加以下文件之前更改目录。 在 x 模式下，在打开存档之后但在从存档中提取条目之前更改目录。

`-``-chroot`

（仅限 x 模式）在处理任何 `-C` 选项之后和提取任何文件之前， `chroot`() 到当前目录。

`-``-clear-nochange-fflags`

（仅限 x 模式）在删除文件系统对象以替换它们之前，清除可能阻止删除的特定于平台的文件属性或文件标志。

`-``-exclude` pattern

不要处理与指定模式匹配的文件或目录。 请注意，排除优先于命令行上指定的模式或文件名。

`-``-exclude-vcs`

不要处理版本控制系统 ‘Arch’, ‘Bazaar’, ‘CVS’, ‘Darcs’, ‘Mercurial’, ‘RCS’, ‘SCCS’, ‘SVN’ 和 ‘git’ 内部使用的文件或目录。

`-``-fflags`

（仅限 c、r、u、x 模式）存档或提取特定于平台的文件属性或文件标志。 这与 `-``-no-fflags` 和 c、r 和 u 模式下的默认行为相反，或者如果 `tar` 以 root 身份在 x 模式下运行。

`-``-format` format

（仅限 c、r、u 模式）对创建的存档使用指定的格式。 支持的格式包括 “cpio”, “pax”, “shar” 和 “ustar” 。 也可能支持其他格式；有关当前支持的格式的更多信息，请参阅 libarchive-formats(5) 在 r 和 u 模式下，扩展现有存档时，此处指定的格式必须与磁盘上现有存档的格式兼容。

[`-f`](#f) file, `-``-file` file

从指定文件读取存档或将存档写入指定文件。文件名可以是 \- 用于标准输入或标准输出。 默认值因系统而异；在 FreeBSD 上，默认为 /dev/sa0; 在 Linux 上，默认值为 /dev/st0 。

`-``-gid` id

使用提供的组 ID 号。 提取时，这会覆盖存档中的组 ID；存档中的组名将被忽略。 创建时，这会覆盖从磁盘读取的组 ID；如果 `-``-gname` 也没有指定，组名将被设置为匹配组 id。

`-``-gname` name

使用提供的组名。 提取时，这会覆盖存档中的组名；如果系统上不存在提供的组名，则将使用组 ID（来自存档或 `-` `-gid` 选项）。 创建时，这将设置将存储在存档中的组名；该名称将不会根据系统组数据库进行验证。

[`-H`](#H)

（仅限 c 和 r 模式）将遵循命令行中命名的符号链接；链接的目标将被归档，而不是链接本身。

[`-h`](#h)

（仅限 c 和 r 模式） `-L` 的同义词。

[`-I`](#I)

[`-T`](#T) 的同义词。

`-``-help`

显示用法。

`-``-hfsCompression`

（仅限 x 模式）Mac OS X 特定（v10.6 或更高版本）。使用 HFS+ 压缩压缩提取的常规文件。

`-``-ignore-zeros`

`-``-options` `read_concatenated_archives` 的别名，用于与 GNU tar 兼容。

`-``-include` pattern

仅处理与指定模式匹配的文件或目录。 请注意，使用 `-``-exclude` 指定的排除优先于包含。 如果没有明确指定包含，则默认处理所有条目。 `-``-include` 选项在过滤档案时特别有用。 例如，命令

``````````` `tar` `-c` `-f` new.tar `-``-include='*foo*'` `@`old.tgz```````````

创建一个新存档 new.tar ，其中仅包含 old.tgz 中包含字符串 ‘foo’ 的条目。

[`-J`](#J), `-``-xz`

（仅限 c 模式）使用 xz(1) 压缩生成的存档。在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 XZ 压缩。

[`-j`](#j), `-``-bzip`, `-` `-bzip2`, `-` `-bunzip2`

（仅限 c 模式）使用 bzip2(1) 压缩生成的存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 bzip2 压缩。

[`-k`](#k), `-``-keep-old-files`

（仅限 x 模式）不要覆盖现有文件。 特别是，如果一个文件在档案中出现多次，以后的副本不会覆盖以前的副本。

`-``-keep-newer-files`

（仅限 x 模式）不要覆盖比正在提取的存档中出现的版本新的现有文件。

[`-L`](#L), `-``-dereference`

（仅限 c 和 r 模式）将遵循所有符号链接。 通常，符号链接是这样存档的。 使用此选项，链接的目标将被存档。

[`-l`](#l), `-``-check-links`

（仅限 c 和 r 模式）除非每个文件的所有链接都已归档，否则会发出警告消息。

`-``-lrzip`

（仅限 c 模式）使用 lrzip(1) 压缩生成的存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 lrzip 压缩。

`-``-lz4`

（仅限 c 模式）在写入之前使用与 lz4 兼容的压缩来压缩存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 lz4 压缩。

`-``-zstd`

（仅限 c 模式）在写入之前使用与 zstd 兼容的压缩来压缩存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 zstd 压缩。

`-``-lzma`

（仅限 c 模式）使用原始 LZMA 算法压缩生成的存档。 在提取或列表模式下，此选项将被忽略。 不鼓励使用此选项，而应使用 `-``-xz` 创建新档案。 请注意，此 `tar` 实现在读取档案时会自动识别 LZMA 压缩。

`-``-lzop`

（仅限 c 模式）使用 lzop(1) 压缩生成的存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 LZO 压缩。

[`-m`](#m), `-``-modification-time`

（仅限 x 模式）不要提取修改时间。 默认情况下，修改时间设置为存档中存储的时间。

`-``-mac-metadata`

（仅限 c、r、u 和 x 模式）特定于 Mac OS X。使用 AppleDouble 格式的 copyfile(3) 归档或提取扩展 ACL 和扩展文件属性。 这与 `-``-no-mac-metadata` 正好相反。 以及 c、r 和 u 模式下的默认行为，或者如果 `tar` 以 root 身份在 x 模式下运行。

[`-n`](#n), `-``-norecurse`, `-``-no-recursion`

不要对目录的内容进行递归操作。

`-``-newer` date

（仅限 c、r、u 模式）仅包括比指定日期新的文件和目录。 这将比较 ctime 条目。

`-``-newer-mtime` date

（仅限 c、r、u 模式）与 `-``-newer` 类似，但它比较 mtime 条目而不是 ctime 条目。

`-``-newer-than` file

（仅限 c、r、u 模式）仅包含比指定文件新的文件和目录。 这将比较 ctime 条目。

`-``-newer-mtime-than` file

（仅限 c、r、u 模式）与 `-``-newer-than` 类似，只是它比较 mtime 条目而不是 ctime 条目。

`-``-nodump`

（仅限 c 和 r 模式）通过跳过此文件来尊重 nodump 文件标志。

`-``-nopreserveHFSCompression`

（仅限 x 模式）Mac OS X 特定（v10.6 或更高版本）。 不要压缩在归档之前使用 HFS+ 压缩压缩的提取的常规文件。 默认情况下，使用 HFS+ 压缩再次压缩常规文件。

`-``-null`

（与 `-I` 或 `-T` 一起使用）文件名或模式由空字符分隔，而不是由换行符分隔。 这通常用于读取 find(1) 的 `-print0` 选项输出的文件名。

`-``-no-acls`

（仅限 c、r、u、x 模式）不要归档或提取 POSIX.1e 或 NFSv4 ACL。 如果 `tar` 在 x 模式下以非 root 用户身份运行（在 Mac OS X 上作为 c、r、u 和 x 模式下的任何用户），这与 `-``-acls` 和默认行为相反。

`-``-no-fflags`

（仅限 c、r、u、x 模式）不要归档或提取文件属性或文件标志。 如果 `tar` 在 x 模式下以非 root 身份运行，这与 `-``-fflags` 和默认行为相反。

`-``-no-mac-metadata`

（仅限 x 模式）特定于 Mac OS X。 不要使用 AppleDouble 格式的 copyfile(3) 归档或提取 ACL 和扩展文件属性。 这与 `-``-mac-metadata` 正好相反。 如果 `tar` 在 x 模式下以非 root 身份运行，则默认行为。

`-``-no-safe-writes`

（仅限 x 模式）不要创建临时文件并使用 rename(2) 替换原始文件。 这与 `-``-safe-writes` 正好相反。

`-``-no-same-owner`

如果 `tar` 以非 root 身份运行，这与 `-``-same-owner` 和默认行为相反。

`-``-no-same-permissions`

（仅限 x 模式）不要提取完整权限（SGID、SUID、粘滞位、文件属性或文件标志、扩展文件属性和 ACL）。 如果 `tar` 以非 root 身份运行，这与 `-p` 和默认行为相反。

`-``-no-xattrs`

（仅限 c、r、u、x 模式）不要归档或提取扩展文件属性。 如果 `tar` 在 x 模式下以非 root 身份运行，这与 `-``-xattrs` 和默认行为相反。

`-``-numeric-owner`

这相当于 `-``-uname` “” `-``-gname` “。” 提取时，它会导致存档中的用户和组名被忽略，而使用数字用户和组 ID。 创建时，它会导致用户名和组名不存储在存档中。

[`-O`](#O), `-``-to-stdout`

（仅限 x、t 模式）在提取 (-x) 模式下，文件将被写入标准输出，而不是被提取到磁盘。 在列表 (-t) 模式下，文件列表将被写入标准错误，而不是通常的标准输出。

[`-o`](#o)

(x 模式) 使用运行程序的用户和用户组，而不是存档中指定的用户和组。 请注意，除非指定了 `-p` 并且程序正在由 root 用户运行，否则这没有任何意义。 在这种情况下，存档中的文件模式和标志将被恢复，但存档中的 ACL 或所有者信息将被丢弃。

[`-o`](#o_2)

(c, r, u 模式) `-``-format` ustar 的同义词

`-``-older` date

（仅限 c、r、u 模式）仅包括早于指定日期的文件和目录。 这将比较 ctime 条目。

`-``-older-mtime` date

（仅限 c、r、u 模式）与 `-``-older` 类似，不同之处在于它比较 mtime 条目而不是 ctime 条目。

`-``-older-than` file

（仅限 c、r、u 模式）仅包含比指定文件更早的文件和目录。 这将比较 ctime 条目。

`-``-older-mtime-than` file

（仅限 c、r、u 模式）与 `-``-older-than` 类似，不同之处在于它比较 mtime 条目而不是 ctime 条目。

`-``-one-file-system`

（c、r 和 u 模式）不要交叉安装点。

`-``-options` options

为特定模块选择可选行为。 参数是包含逗号分隔的关键字和值的文本字符串。 这些被传递给处理特定格式的模块以控制这些格式的行为方式。 每个选项具有以下形式之一：

key=value

该键将在每个支持它的模块中设置为指定的值。 不支持此键的模块将忽略它。

key

该密钥将在支持它的每个模块中启用。 这相当于 key`=1` 。

!key

该密钥将在支持它的每个模块中被禁用。

module:key=value, module:key, module:!key

和上面一样，但是对应的键和值将只提供给名称与 module 匹配的模块。

创建和追加模式支持的模块和键的完整列表在 archive\_write\_set\_options(3)-
中，对于提取和列表模式在 archive\_read\_set\_options(3) 中。

支持的选项示例：

[`iso9660:joliet`](#iso9660:joliet)

支持 Joliet 扩展。 这是默认启用的，使用 `!joliet` 或 `iso9660:!joliet` 禁用。

[`iso9660:rockridge`](#iso9660:rockridge)

支持 Rock Ridge 扩展。 这是默认启用的，使用 `!rockridge` 或 `iso9660:!rockridge` 禁用。

[`gzip:compression-level`](#gzip:compression-level)

一个从 1 到 9 的十进制整数，指定 gzip 压缩级别。

[`gzip:timestamp`](#gzip:timestamp)

存储时间戳。 这是默认启用的，使用 `!timestamp` 或 `gzip:!timestamp` 禁用。

[`lrzip:compression`](#lrzip:compression)\=type

使用 type 作为压缩方法。 支持的值为 bzip2、gzip、lzo（超快）和 zpaq（最佳，极慢）。

[`lrzip:compression-level`](#lrzip:compression-level)

一个从 1 到 9 的十进制整数，指定 lrzip 压缩级别。

[`lz4:compression-level`](#lz4:compression-level)

一个从 1 到 9 的十进制整数，指定 lzop 压缩级别。

[`lz4:stream-checksum`](#lz4:stream-checksum)

启用流校验和。这是默认情况下，使用 `lz4:!stream-checksum` 禁用。

[`lz4:block-checksum`](#lz4:block-checksum)

启用块校验和（默认禁用）。

[`lz4:block-size`](#lz4:block-size)

一个从 4 到 7 的十进制整数，指定 lz4 压缩块大小（默认设置为 7）。

[`lz4:block-dependence`](#lz4:block-dependence)

使用被压缩块的前一个块作为压缩字典来提高压缩率。

[`zstd:compression-level`](#zstd:compression-level)

指定 zstd 压缩级别的十进制整数。 支持的值取决于库版本，常用值从 1 到 22。

[`lzop:compression-level`](#lzop:compression-level)

一个从 1 到 9 的十进制整数，指定 lzop 压缩级别。

[`xz:compression-level`](#xz:compression-level)

一个从 0 到 9 的十进制整数，指定 xz 压缩级别。

[`mtree:`](#mtree:)keyword

mtree writer 模块允许您指定将在输出中包含哪些 mtree 关键字。 支持的关键字包括： `cksum`, `device`, `flags`, `gid`, `gname`, `indent`, `link`, `md5`, `mode`, `nlink`, `rmd160`, `sha1`, `sha256`, `sha384`, `sha512`, `size`, `time`, `uid`, `uname 。` 默认等价于： “device, flags, gid, gname, link, mode, nlink, size, time, type, uid, uname 。”

[`mtree:all`](#mtree:all)

启用所有上述关键字。 您还可以使用 `mtree:!all` 禁用所有关键字。

[`mtree:use-set`](#mtree:use-set)

在输出中启用 `/set` 行的生成。

[`mtree:indent`](#mtree:indent)

通过缩进选项和拆分行以适应 80 列来生成人类可读的输出。

[`zip:compression`](#zip:compression)\=type

使用 type 作为压缩方法。 支持的值是 store（未压缩）和 deflate（gzip 算法）。

[`zip:encryption`](#zip:encryption)

使用传统的 zip 加密启用加密。

[`zip:encryption`](#zip:encryption_2)\=type

使用 type 作为加密类型。 支持的值为 zipcrypt（传统 zip 加密）、aes128（WinZip AES-128 加密）和 aes256（WinZip AES-256 加密）。

[`read_concatenated_archives`](#read_concatenated_archives)

忽略存档中的零块，当多个 tar 存档连接在一起时会发生这种情况。 如果没有此选项，则只会读取第一个串联存档的内容。 此选项与 GNU tar 的 `-i` `-、` `-``-ignore-zeros` 选项相当。

如果任何模块都不支持提供的选项，则这是一个致命错误。

[`-P`](#P), `-``-absolute-paths`

默认情况下，绝对路径名（以 / 字符开头的路径名）在创建档案和从中提取档案时都会删除前导斜杠。 此外， `tar` 将拒绝提取路径名包含 .. 或其目标目录将被符号链接更改的归档条目。 此选项会抑制这些行为。

[`-p`](#p), `-``-insecure`, `-``-preserve-permissions`

（仅限 x 模式）保留文件权限。 尝试恢复从存档中提取的每个项目的完整权限，包括文件模式、文件属性或文件标志、扩展文件属性和 ACL（如果可用）。 这与 `-``-no-same-permissions` 相反，如果 `tar` 以 root 身份运行，则为默认值。 还可以通过指定 `-``-no-acls`, `-``-no-fflags`, `-``-no-mac-metadata` 或 `-``-no-xattrs` 来部分覆盖它。

`-``-passphrase` passphrase

passphrase 用于提取或创建加密存档。 目前，zip 是唯一支持加密的支持格式。 除非您意识到使用此选项有多么不安全，否则不应使用此选项。

`-``-posix`

（仅限 c、r、u 模式） `-``-format` pax 的同义词

[`-q`](#q), `-``-fast-read`

（仅限 x 和 t 模式）仅提取或列出与每个模式或文件名操作数匹配的第一个存档条目。 匹配每个指定的模式或文件名后立即退出。 默认情况下，存档总是被读取到最后，因为可以有多个具有相同名称的条目，并且按照惯例，后面的条目会覆盖前面的条目。 此选项作为性能优化提供。

[`-S`](#S)

（仅限 x 模式）将文件提取为稀疏文件。 对于磁盘上的每个块，首先检查它是否只包含 NULL 字节，否则寻找它。 这类似于 dd 的 conv=sparse 选项。

[`-s`](#s) pattern

根据 pattern 修改文件或存档成员名称。 该模式的格式为 /old/new/\[ghHprRsS\] 其中 old 是基本正则表达式， new 是匹配部分的替换字符串，可选的尾随字母修改处理替换的方式。 如果 old 不匹配，则跳过该模式。 在 new 中，~ 被替换为匹配，\\1 到 \\9 与相应捕获组的内容。 可选的尾随 g 指定匹配应该在匹配的部分之后继续，并在第一个不匹配的模式处停止。 可选的尾随 s 指定该模式适用于符号链接的值。 可选的尾随 p 指定在成功替换后原始路径名和新路径名应打印到标准错误。 可选的尾随 H、R 或 S 字符分别抑制硬链接目标、常规文件名或符号链接目标的替换。 可选的尾随 h、r 或 s 字符分别启用硬链接目标、常规文件名或符号链接目标的替换。默认值为 hrs ，它将替换应用于所有名称。 特别是，从来没有必要指定 h、r 或 s。

`-``-safe-writes`

（仅限 x 模式）以原子方式提取文件。 默认情况下， `tar` 取消与提取文件同名的原始文件（如果存在）的链接，然后立即以相同的名称创建它并写入它。 在短时间内，尝试访问该文件的应用程序可能找不到它，或者看到不完整的结果。 如果启用了 `-``-safe-writes` ， `tar` 首先创建一个唯一的临时文件，然后将新内容写入临时文件，最后使用 rename(2) 以原子方式将临时文件重命名为其最终名称。 这保证了访问文件的应用程序将始终看到旧内容或新内容。

`-``-same-owner`

（仅限 x 模式）提取所有者和组 ID。 这与 `-``-no-same-owner` 和 `tar` 以 root 身份运行时的默认行为相反。

`-``-strip-components` count

删除指定数量的前导路径元素。 元素较少的路径名将被静默跳过。 请注意，在检查包含/排除模式之后但在安全检查之前编辑路径名。

[`-T`](#T_2) filename, `-``-files-from` filename

在 x 或 t 模式下， `tar` 将读取要从 filename 中提取的名称列表。 在 c 模式下， `tar` 将从 filename 中读取要归档的名称。 单独一行上的特殊名称 “-C” 将导致当前目录更改为下一行指定的目录。 除非指定了 `-``-null` ，否则名称由换行符终止。 请注意， `-``-null` 还会禁用对包含 “-C” 的行的特殊处理。 注意：如果您使用 find(1) 生成文件列表，您可能还想使用 `-n` 。

`-``-totals`

（仅限 c、r、u 模式）归档所有文件后，将摘要打印到 stderr。

[`-U`](#U), `-``-unlink`, `-` `-unlink-first`

（仅限 x 模式）在创建文件之前取消链接文件。 如果大多数文件已经存在，这可能是一个较小的性能优化，但如果大多数文件不存在，则可能会使事情变慢。 此标志还会导致 `tar`-
删除干预目录符号链接，而不是报告错误。 有关更多详细信息，请参阅下面的安全部分。

`-``-uid` id

使用提供的用户 ID 号并忽略存档中的用户名。 在创建时，如果没有同时指定 `-``-uname` ，则用户名将设置为与用户 ID 匹配。

`-``-uname` name

使用提供的用户名。 提取时，这会覆盖存档中的用户名；如果系统上不存在提供的用户名，它将被忽略，而使用用户 ID（来自存档或 `-` `-uid` 选项）。 创建时，这将设置将存储在存档中的用户名；该名称未针对系统用户数据库进行验证。

`-``-use-compress-program` program

通过 program 管道输入（在 x 或 t 模式下）或输出（在 c 模式下），而不是使用内置的压缩支持。

[`-v`](#v), `-``-verbose`

产生详细的输出。 在创建和提取模式下， `tar` 将列出从存档读取或写入存档的每个文件名。 在列表模式下， `tar` 将产生类似于 ls(1) 的输出。 额外的 `-v` 选项还将在创建和提取模式下提供类似 ls 的详细信息。

`-``-version`

打印 `tar` 和 `libarchive`, 的版本，然后退出。

[`-w`](#w), `-``-confirmation`, `-``-interactive`

要求对每项操作进行确认。

[`-X`](#X) filename, `-``-exclude-from` filename

从指定文件中读取排除模式列表。 有关排除处理的更多信息，请参见 `-``-exclude` 。

`-``-xattrs`

（仅限 c、r、u、x 模式）存档或提取扩展文件属性。 这与 `-``-no-xattrs` 和 c、r 和 u 模式下的默认行为相反，或者如果 `tar` 以 root 身份在 x 模式下运行。

[`-y`](#y)

（仅限 c 模式）使用 bzip2(1) 压缩生成的存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 bzip2 压缩。

[`-Z`](#Z), `-``-compress`, `-``-uncompress`

（仅限 c 模式）使用 compress(1) 压缩生成的存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别压缩压缩。

[`-z`](#z), `-``-gunzip`, `-` `-gzip`

（仅限 c 模式）使用 gzip(1) 压缩生成的存档。 在提取或列表模式下，此选项将被忽略。 请注意，此 `tar` 实现在读取档案时会自动识别 gzip 压缩。

[环境](#__u73AF___u5883_)
=======================

以下环境变量会影响 `tar` 的执行：

[`TAR_READER_OPTIONS`](#TAR_READER_OPTIONS)

格式阅读器和压缩阅读器的默认选项。 `-``-options` 选项会覆盖此选项。

[`TAR_WRITER_OPTIONS`](#TAR_WRITER_OPTIONS)

格式编写器和压缩编写器的默认选项。 `-``-options` 选项会覆盖此选项。

[`LANG`](#LANG)

要使用的语言环境。 有关详细信息，请参阅 environ(7) 。

[`TAPE`](#TAPE)

默认设备。 `-f` 选项会覆盖它。 有关详细信息，请参阅上面的 `-f` 选项的说明。

[`TZ`](#TZ)

显示日期时使用的时区。 有关详细信息，请参阅 environ(7) 。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `tar` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

下面创建一个名为 file.tar.gz 的新存档，其中包含两个文件 source.c 和 source.h:

````` `tar` `-czf` file.tar.gz source.c source.h`````

要查看此存档的详细目录：

````` `tar` `-tvf` file.tar.gz`````

要从默认磁带驱动器上的存档中提取所有条目：

````` `tar` `-x` `````

要检查 ISO 9660 cdrom 映像的内容：

````` `tar` `-tf` image.iso`````

要移动文件层次结构，请调用 `tar` 作为

````````````` `tar` `-cf` - `-C` srcdir . | `tar` `-xpf` - `-C` destdir`````````````

或更传统的

`````````cd srcdir ; `tar` `-cf` - . | (cd destdir ; `tar` `-xpf` -)`````````

在创建模式下，要归档的文件和目录的列表还可以包括 `-C`foo/baz 形式的目录更改指令和 `@`archive-file 形式的归档包含。例如，命令行

``````````` `tar` `-c` `-f` new.tar foo1 `@`old.tgz `-C`/tmp foo2```````````

将创建一个新的存档 new.tar 。 `tar` 将从当前目录读取文件 foo1 并将其添加到输出存档中。 然后它将从 old.tgz 中读取每个条目并将这些条目添加到输出存档中。 最后，它将切换到 /tmp 目录并将 foo2-
添加到输出存档中。

mtree(5) 格式的输入文件可用于创建具有与磁盘上现有数据不同的任意所有权、权限或名称的输出存档：

$ cat input.mtree #mtree usr/bin uid=0 gid=0 mode=0755 type=dir usr/bin/ls uid=0 gid=0 mode=0755 type=file content=myls $ tar -cvf output.tar @input.mtree 

`-``-newer` 和 `-``-newer-mtime` 开关接受各种常见的日期和时间规范，包括 “12 Mar 2005 7:14:29pm”, “2005-03-12 19:14”, “5 minutes ago” 和 “19:14 PST May 1” 。

`-``-options` 参数可用于控制归档生成或读取的各种细节。 例如，您可以生成仅包含 `type`, `time` 和 `uid` 关键字的 mtree 输出：

````````` `tar` `-cf` file.tar `-``-format=mtree` `-``-options='!all,type,time,uid'` dir`````````

或者您可以设置 gzip 或 xz 压缩使用的压缩级别：

``````` `tar` `-czf` file.tar `-``-options='compression-level=9'`.```````

有关更多详细信息，请参阅 archive\_read(3) 和 archive\_write(3) 中描述的 `archive_read_set_options`() 和 `archive_write_set_options`() API 调用的说明。

[兼容性](#__u517C___u5BB9___u6027_)
================================

支持捆绑参数格式以与历史实现兼容。 它由一个初始单词（没有前导 - 字符）组成，其中每个字符表示一个选项。 参数作为单独的词跟随。 参数的顺序必须与捆绑命令字中相应字符的顺序相匹配。例如，

````` `tar` `tbf 32` file.tar`````

指定三个标志 `t 、` `b` 和 `f` 。 `b` 和 `f` 标志都需要参数，因此命令行上必须有两个附加项。 32 是 `b` 标志的参数， file.tar 是 `f` 标志的参数。

模式选项 c、r、t、u 和 x 以及选项 b、f、l、m、o、v 和 w 符合 SUSv2。

为了获得最大的可移植性，调用 `tar` 的脚本应使用上述捆绑参数格式，应将自身限制为 `c 、` `t` 和 `x` 模式以及 `b 、` `f 、` `m 、` `v` 和 `w` 选项。

提供了额外的长选项以提高与其他 tar 实现的兼容性。

[安全](#__u5B89___u5168_)
=======================

某些安全问题对于许多归档程序都很常见，包括 `tar` 。 特别是，精心制作的存档可以请求将文件 `tar` 解压缩到目标目录之外的位置。 这可能会导致不知情的用户覆盖他们不打算覆盖的文件。 如果超级用户正在提取存档，则系统上的任何文件都可能被覆盖。 这可以通过三种方式发生。 尽管 `tar` 具有针对每一个的保护机制，但精明的用户应该意识到其中的含义：

*   存档条目可以有绝对路径名。 默认情况下， `tar` 在恢复文件名之前会从文件名中删除前导 / 字符以防止出现此问题。
*   存档条目可以具有包含 .. 组件的路径名。 默认情况下， `tar` 不会提取路径名中包含 .. 组件的文件。 存档条目可以利用符号链接将文件恢复到其他目录。
*   存档可以将符号链接恢复到另一个目录，然后使用该链接将文件恢复到该目录。 为了防止这种情况， `tar` 检查每个提取的路径中的符号链接。 如果最终路径元素是符号链接，它将被删除并替换为存档条目。 如果指定了 `-U` ，任何中间符号链接也将被无条件删除。 如果既没有指定 `-U` 也没有指定 `-P` ， `tar` 将拒绝提取条目。

为了保护自己，您应该警惕来自不受信任来源的任何档案。 您应该检查存档的内容

````` `tar` `-tf` filename`````

提取前。 您应该使用 `-k` 选项来确保 `tar` 不会覆盖任何现有文件或使用 `-U` 选项来删除任何预先存在的文件。 在以超级用户权限运行时，您通常不应提取档案。 请注意， `tar` 的 `-P` 选项会禁用上述安全检查，并允许您在提取存档的同时保留任何绝对路径名、 .. 组件或指向其他目录的符号链接。

[参见](#__u53C2___u89C1_)
=======================

bzip2(1), compress(1), cpio(1), gzip(1), mt(1), pax(1), shar(1), xz(1), libarchive(3), libarchive-formats(5), tar(5)

[标准](#__u6807___u51C6_)
=======================

tar 命令没有当前的 POSIX 标准；它出现在 ISO/IEC 9945-1:1996 (“POSIX.1”) 中，但从 IEEE Std 1003.1-2001 (“POSIX.1”) 中删除。 此实现支持的选项是通过调查许多现有的 tar 实现以及 tar 的旧 POSIX 规范和 pax 的当前 POSIX 规范来开发的。

IEEE Std 1003.1-2001 (“POSIX.1”) 为 pax 命令定义了ustar 和 pax 交换文件格式。

[历史](#__u5386___u53F2_)
=======================

`tar` 命令出现在 1979 年 1 月发布的第七版 Unix 中。 还有许多其他实现，其中许多扩展了文件格式。 John Gilmore 的 `pdtar` 公共域实现（大约在 1987 年 11 月）非常有影响力，并形成了 GNU tar 的基础。 从 FreeBSD 1.0 开始，GNU tar 作为标准系统 tar 包含在 FreeBSD 中。

这是基于 libarchive(3) 库的完整重新实现。 它于 2005 年 5 月首次与 FreeBSD 5.4 一起发布。

[缺陷](#__u7F3A___u9677_)
=======================

该程序遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 对 `-l` 选项的定义。 请注意，1.15 版之前的 GNU tar 将 `-l` 视为 `-``-one-file-system` 选项的同义词。

`-C` dir 选项可能与历史实现不同。

所有存档输出都写入大小正确的块中，即使输出正在被压缩。 最后一个输出块是否填充到完整的块大小取决于格式和输出设备。 对于 tar 和 cpio 格式，如果输出正在写入标准输出或字符或块设备（如磁带驱动器），则将最后一个输出块填充到完整的块大小。 如果将输出写入常规文件，则不会填充最后一个块。 许多压缩器，包括 gzip(1) 和 bzip2(1) ，在解压缩由 `tar` 创建的档案时会抱怨空填充，尽管它们仍然可以正确解压。

压缩和解压是在内部实现的，所以生成的压缩输出之间可能存在微不足道的差异

````` `tar` `-czf` - file`````

以及由

``````` `tar` `-cf` - file | `gzip` ```````

默认应该是读取和写入归档到标准 I/O 路径，但传统（和 POSIX）另有规定。

`r` 和 `u` 模式要求存档未压缩并位于磁盘上的常规文件中。 可以使用带有 @archive-file 扩展名的 `c` 模式修改其他存档。

要归档名为 @foo 或 \-foo 的文件，您必须分别将其指定为 ./@foo 或 ./-foo 。

在创建模式下，前导 ./ 总是被删除。 除非指定了 `-P` 选项，否则会去除前导 / 。

在创建和提取时需要更好地支持文件选择。

尚不支持多卷存档。

使用 `@`\- 约定在不同的存档格式（例如 tar 和 cpio）之间进行转换可能会导致硬链接信息丢失。 （这是不同归档格式存储硬链接信息的方式不兼容的结果。）

January 31, 2020

FreeBSD 13.1-RELEASE