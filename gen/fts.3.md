# fts(3)

`fts` — 遍历文件层次结构

## 名称

`fts` — 遍历文件层次结构

## 库

Lb libc

## 概要

```c
#include <fts.h>

FTS *
fts_open(char * const *path_argv, int options,
    int (*compar)(const FTSENT * const *, const FTSENT * const *));

FTS *
fts_open_b(char * const *path_argv, int options,
    int (^compar)(const FTSENT * const *, const FTSENT * const *));

FTSENT *
fts_read(FTS *ftsp);

FTSENT *
fts_children(FTS *ftsp, int options);

int
fts_set(FTS *ftsp, FTSENT *f, int instr);

void
fts_set_clientptr(FTS *ftsp, void *clientdata);

void *
fts_get_clientptr(FTS *ftsp);

FTS *
fts_get_stream(FTSENT *f);

int
fts_close(FTS *ftsp);
```

## 描述

`fts` 函数用于遍历 UNIX 文件层次结构。简要概述：`fts_open` 和 `fts_open_b` 函数返回文件层次结构的“句柄”，然后将其传递给其他 `fts` 函数。`fts_read` 函数返回指向描述文件层次结构中某个文件的结构的指针。`fts_children` 函数返回指向结构链表的指针，每个结构描述层次结构中某个目录中包含的一个文件。通常，目录会被访问两次可区分的时间：先序（在访问其任何后代之前）和后序（在访问其所有后代之后）。文件只被访问一次。可以“逻辑地”（忽略符号链接）或物理地（访问符号链接）遍历层次结构，可以排序遍历或修剪和/或重新访问层次结构的部分。

两个结构在包含文件中定义（并 typedef）：

```c
#include <fts.h>
```

第一个是 `FTS`，表示文件层次结构本身的结构。第二个是 `FTSENT`，表示文件层次结构中文件的结构。通常，文件层次结构中的每个文件都会返回一个 `FTSENT` 结构。在本手册页中，“文件”和“`FTSENT` 结构”通常可互换使用。

`FTS` 结构包含一个单个指针的空间，可用于存储应用程序数据或每个层次结构的状态。`fts_set_clientptr` 和 `fts_get_clientptr` 函数可用于设置和检索此指针。这仅在从排序比较函数访问时才可能有用，该函数可以使用 `fts_get_stream` 函数确定其参数的原始 `FTS` 流。这两个 `get` 函数也可作为同名宏使用。

`FTSENT` 结构至少包含以下字段，下文将更详细地描述：

```c
typedef struct _ftsent {
	int fts_info;			/* FTSENT 结构的状态 */
	char *fts_accpath;		/* 访问路径 */
	char *fts_path;			/* 根路径 */
	size_t fts_pathlen;		/* strlen(fts_path) */
	char *fts_name;			/* 文件名 */
	size_t fts_namelen;		/* strlen(fts_name) */
	long fts_level;			/* 深度 (-1 到 N) */
	int fts_errno;			/* 文件 errno */
	long long fts_number;		/* 本地数值 */
	void *fts_pointer;		/* 本地地址值 */
	struct ftsent *fts_parent;	/* 父目录 */
	struct ftsent *fts_link;	/* 下一个文件结构 */
	struct ftsent *fts_cycle;	/* 循环结构 */
	struct stat *fts_statp;		/* stat(2) 信息 */
} FTSENT;
```

这些字段定义如下：

**`FTS_D`** 正在先序访问的目录。

**`FTS_DC`** 在树中导致循环的目录。（`FTSENT` 结构的 `fts_cycle` 字段也将被填充。）

**`FTS_DEFAULT`** 任何表示未被其他 `fts_info` 值之一明确描述的文件类型的 `FTSENT` 结构。

**`FTS_DNR`** 无法读取的目录。当目录无法进入或可进入但无法读取时，此值紧跟 `FTS_D` 出现，代替 `FTS_DP`。这是错误返回，`fts_errno` 字段将设置为指示导致错误的原因。

**`FTS_DOT`** 名为 `.` 或 `..` 的文件，未指定为 `fts_open` 或 `fts_open_b` 的文件名（参见 `FTS_SEEDOT`）。

**`FTS_DP`** 正在后序访问的目录。`FTSENT` 结构的内容与先序访问目录时相同，除了 `fts_info` 字段。

**`FTS_ERR`** 这是错误返回，`fts_errno` 字段将设置为指示导致错误的原因。

**`FTS_F`** 常规文件。

**`FTS_NS`** 没有 [stat(2)](../sys/stat.2.md) 信息的文件。`fts_statp` 字段的内容未定义。这是错误返回，`fts_errno` 字段将设置为指示导致错误的原因。

**`FTS_NSOK`** 未请求 [stat(2)](../sys/stat.2.md) 信息的文件。`fts_statp` 字段的内容未定义。

**`FTS_SL`** 符号链接。

**`FTS_SLNONE`** 目标不存在的符号链接。`fts_statp` 字段的内容引用符号链接本身的文件特征信息。

**`fts_info`** 以下值之一，描述返回的 `FTSENT` 结构及其表示的文件。除无错误的目录（`FTS_D`）外，所有这些条目都是终止的，即它们不会被重新访问，其后代也不会被访问。

**`fts_accpath`** 从当前目录访问文件的路径。

**`fts_path`** 文件相对于遍历根的路径。此路径包含指定给 `fts_open` 或 `fts_open_b` 的路径作为前缀。

**`fts_pathlen`** `fts_path` 引用的字符串长度。

**`fts_name`** 文件名。

**`fts_namelen`** `fts_name` 引用的字符串长度。

**`fts_level`** 遍历深度，从 -1 到 N 编号，表示找到此文件的位置。表示遍历起点（或根）父级的 `FTSENT` 结构编号为 `FTS_ROOTPARENTLEVEL` (-1)，根本身的 `FTSENT` 结构编号为 `FTS_ROOTLEVEL` (0)。

**`fts_errno`** 当 `fts_children` 或 `fts_read` 函数返回 `FTSENT` 结构且其 `fts_info` 字段设置为 `FTS_DNR`、`FTS_ERR` 或 `FTS_NS` 时，`fts_errno` 字段包含指定错误原因的外部变量 `errno` 的值。否则，`fts_errno` 字段的内容未定义。

**`fts_number`** 此字段供应用程序使用，不被 `fts` 函数修改。初始化为 0。

**`fts_pointer`** 此字段供应用程序使用，不被 `fts` 函数修改。初始化为 `NULL`。

**`fts_parent`** 指向引用层次结构中当前文件正上方文件的 `FTSENT` 结构的指针，即此文件所属的目录。还提供了初始入口点的父结构，但仅保证 `fts_level`、`fts_number` 和 `fts_pointer` 字段已初始化。

**`fts_link`** 从 `fts_children` 函数返回后，`fts_link` 字段指向目录成员的以 NULL 结尾的链表中的下一个结构。否则，`fts_link` 字段的内容未定义。

**`fts_cycle`** 如果目录在层次结构中导致循环（参见 `FTS_DC`），无论是因为两个目录之间的硬链接还是指向目录的符号链接，该结构的 `fts_cycle` 字段将指向层次结构中引用与当前 `FTSENT` 结构相同文件的 `FTSENT` 结构。否则，`fts_cycle` 字段的内容未定义。

**`fts_statp`** 指向文件 [stat(2)](../sys/stat.2.md) 信息的指针。

所有文件层次结构中所有文件的路径使用单个缓冲区。因此，`fts_path` 和 `fts_accpath` 字段仅保证对 `fts_read` 最近返回的文件以 `NUL` 结尾。使用这些字段引用由其他 `FTSENT` 结构表示的任何文件，需要使用该 `FTSENT` 结构的 `fts_pathlen` 字段中包含的信息修改路径缓冲区。在进一步调用 `fts_read` 之前应撤销任何此类修改。`fts_name` 字段始终以 `NUL` 结尾。

### 线程安全

`fts` 函数可以安全地用于多线程程序，前提是没有两个线程同时访问相同的 `FTS` 或 `FTSENT` 结构。但是，除非将 `FTS_NOCHDIR` 标志传递给 `fts_open` 或 `fts_open_b`，否则调用 `fts_read` 和 `fts_children` 可能会更改当前工作目录，这将影响所有线程。反之，在 `fts_read` 或 `fts_children` 调用期间或之间更改当前工作目录（即使在单线程程序中）可能导致 `fts` 故障，除非将 `FTS_NOCHDIR` 标志传递给 `fts_open` 或 `fts_open_b` 且 `path_argv` 中的所有路径都是绝对路径。

### fts_open

`fts_open` 函数接受指向字符指针数组的指针，该数组命名构成要遍历的逻辑文件层次结构的一个或多个路径。该数组必须以 `NULL` 指针终止。

有许多选项，至少必须指定其中一个（`FTS_LOGICAL` 或 `FTS_PHYSICAL`）。通过以下值的按位或选择选项：

**`FTS_COMFOLLOW`** 此选项使指定为根路径的任何符号链接立即被跟随，无论是否还指定了 `FTS_LOGICAL`。

**`FTS_COMFOLLOWDIR`** 此选项类似于 `FTS_COMFOLLOW`，但仅跟随指向目录的符号链接。

**`FTS_LOGICAL`** 此选项使 `fts` 例程返回符号链接目标的 `FTSENT` 结构，而非符号链接本身。如果设置此选项，向应用程序返回 `FTSENT` 结构的符号链接仅限于引用不存在文件的符号链接。必须向 `fts_open` 函数提供 `FTS_LOGICAL` 或 `FTS_PHYSICAL` 之一。

**`FTS_NOCHDIR`** 为允许下降到任意深度（独立于 `PATH_MAX`）并提高性能，`fts` 函数在遍历文件层次结构时更改目录。这带来副作用，应用程序不能依赖遍历期间处于任何特定目录。`FTS_NOCHDIR` 选项关闭此功能，`fts` 函数将不更改当前目录。注意，应用程序自身不应更改当前目录并尝试访问文件，除非指定了 `FTS_NOCHDIR` 且向 `fts_open` 提供了绝对路径名。

**`FTS_NOSTAT`** 默认情况下，返回的 `FTSENT` 结构引用每个访问文件的特征信息（`statp` 字段）。此选项作为性能优化放宽该要求，允许 `fts` 函数将 `fts_info` 字段设置为 `FTS_NSOK` 并使 `statp` 字段内容未定义。根目录和遍历期间遇到的任何目录（`FTS_D`、`FTS_DC`、`FTS_DP`）仍然完全填充。

**`FTS_NOSTAT_TYPE`** 此选项类似于 `FTS_NOSTAT`，但尝试基于 `struct dirent` 的 `d_type` 字段信息填充 `fts_info`。

**`FTS_PHYSICAL`** 此选项使 `fts` 例程返回符号链接本身的 `FTSENT` 结构，而非其指向的目标文件。如果设置此选项，层次结构中所有符号链接的 `FTSENT` 结构都返回给应用程序。必须向 `fts_open` 函数提供 `FTS_LOGICAL` 或 `FTS_PHYSICAL` 之一。

**`FTS_SEEDOT`** 默认情况下，除非指定为 `fts_open` 的路径参数，文件层次结构中遇到的任何名为 `.` 或 `..` 的文件都被忽略。此选项使 `fts` 例程为它们返回 `FTSENT` 结构。

**`FTS_XDEV`** 此选项阻止 `fts` 下降到与开始下降的文件具有不同设备号的目录。

`compar` 参数指向用户定义的函数，可用于排序层次结构的遍历。它接受两个指向 `FTSENT` 结构指针的指针作为参数，应返回负值、零或正值，以指示其第一个参数引用的文件在顺序上位于、以任何顺序相对于、或在其第二个参数引用的文件之后。`FTSENT` 结构的 `fts_accpath`、`fts_path` 和 `fts_pathlen` 字段在此比较中*绝不能*使用。如果 `fts_info` 字段设置为 `FTS_NS` 或 `FTS_NSOK`，`fts_statp` 字段也不能使用。如果 `compar` 参数为 `NULL`，根路径的目录遍历顺序为 `path_argv` 中列出的顺序，其他所有内容为目录中列出的顺序。

### fts_open_b

`fts_open_b` 函数与 `fts_open` 相同，不同之处在于它接受块指针而非函数指针。块在 `fts_open_b` 返回前被复制，因此原始块可以安全地超出作用域或被释放。

### fts_read

`fts_read` 函数返回指向描述层次结构中文件的 `FTSENT` 结构的指针。目录（可读且不导致循环的）至少被访问两次，一次先序一次后序。所有其他文件至少被访问一次。（目录之间不导致循环的硬链接或指向符号链接的符号链接可能导致文件被访问多次，或目录被访问两次以上。）

如果层次结构的所有成员都已返回，`fts_read` 返回 `NULL` 并将外部变量 `errno` 设置为 0。如果发生与层次结构中文件无关的错误，`fts_read` 返回 `NULL` 并适当设置 `errno`。如果发生与返回文件相关的错误，返回指向 `FTSENT` 结构的指针，`errno` 可能设置也可能未设置（参见 `fts_info`）。注意，在设置 `FTS_STOP` 标志或到达流末尾后，如果使用相同的 `ftsp` 参数再次调用 `fts_read`，不会将 `errno` 设置为 0。

`fts_read` 返回的 `FTSENT` 结构在对同一文件层次结构流调用 `fts_close` 后可能被覆盖，或者在对同一文件层次结构流调用 `fts_read` 后可能被覆盖，除非它们表示目录类型的文件，在这种情况下，它们在 `fts_read` 函数以后序返回 `FTSENT` 结构后再次调用 `fts_read` 之前不会被覆盖。

### fts_children

`fts_children` 函数返回指向 `FTSENT` 结构的指针，该结构描述 `fts_read` 最近返回的 `FTSENT` 结构所表示目录中文件的以 NULL 结尾的链表中的第一个条目。该链表通过 `FTSENT` 结构的 `fts_link` 字段链接，并按用户指定的比较函数（如果有）排序。重复调用 `fts_children` 将重新创建此链表。

作为特殊情况，如果尚未对层次结构调用 `fts_read`，`fts_children` 将返回指向指定给 `fts_open` 或 `fts_open_b` 的逻辑目录中文件的指针，即指定给 `fts_open` 或 `fts_open_b` 的参数。否则，如果 `fts_read` 最近返回的 `FTSENT` 结构不是先序访问的目录，或目录不包含任何文件，`fts_children` 返回 `NULL` 并将 `errno` 设置为零。如果发生错误，`fts_children` 返回 `NULL` 并适当设置 `errno`。

`fts_children` 返回的 `FTSENT` 结构在对同一文件层次结构流调用 `fts_children`、`fts_close` 或 `fts_read` 后可能被覆盖。

*Option* 可设置为以下值：

**`FTS_NAMEONLY`** 仅需要文件名。返回的结构链表中所有字段的内容均未定义，`fts_name` 和 `fts_namelen` 字段除外。

### fts_set

`fts_set` 函数允许用户应用程序确定流 `ftsp` 中文件 `f` 的进一步处理。`fts_set` 函数成功时返回 0，发生错误时返回 -1。其 `instr` 参数必须为以下值之一：

**`FTS_AGAIN`** 重新访问该文件；任何文件类型都可重新访问。下一次调用 `fts_read` 将返回引用的文件。该结构的 `fts_stat` 和 `fts_info` 字段将在那时重新初始化，但其他字段不会被更改。此选项仅对 `fts_read` 最近返回的文件有意义。正常用于后序目录访问，它使目录（以先序和后序）及其所有后代重新被访问。

**`FTS_FOLLOW`** 引用的文件必须是符号链接。如果引用的文件是 `fts_read` 最近返回的文件，下一次调用 `fts_read` 返回该文件，`fts_info` 和 `fts_statp` 字段重新初始化以反映符号链接的目标而非符号链接本身。如果该文件是 `fts_children` 最近返回的文件之一，该结构在由 `fts_read` 返回时，`fts_info` 和 `fts_statp` 字段将反映符号链接的目标而非符号链接本身。在任一情况下，如果符号链接的目标不存在，返回结构的字段将不变，`fts_info` 字段设置为 `FTS_SLNONE`。如果链接的目标是目录，则进行先序返回，随后返回其所有后代，最后进行后序返回。

**`FTS_SKIP`** 不访问此文件的后代。该文件可以是 `fts_children` 或 `fts_read` 最近返回的文件之一。

### fts_set_clientptr, fts_get_clientptr

`fts_set_clientptr` 函数将流 `ftsp` 的客户端数据指针设置为 `clientdata`。`fts_get_clientptr` 函数返回与 `ftsp` 关联的客户端数据指针。这可用于将每流数据传递给比较函数。

出于性能原因，`fts_get_clientptr` 可能被预处理器宏遮蔽。

### fts_get_stream

`fts_get_stream` 函数返回与文件条目 `f` 关联的 `fts` 流。典型用途是比较函数首先对其参数之一调用 `fts_get_stream`，然后调用 `fts_get_clientptr` 获取客户端数据指针，该指针又指向正确排序两个条目所需的信息。

出于性能原因，`fts_get_stream` 可能被预处理器宏遮蔽。

### fts_close

`fts_close` 函数关闭文件层次结构流 `ftsp` 并将当前目录恢复为调用 `fts_open` 或 `fts_open_b` 打开 `ftsp` 时所在的目录。

## 返回值

`fts_open` 和 `fts_open_b` 函数成功时返回指向新 `fts` 流的指针，失败时返回 `NULL`。

`fts_read` 函数成功时或发生特定于该文件条目的错误时返回指向下一个文件条目的指针。到达文件层次结构末尾时，返回 `NULL` 并将外部变量 `errno` 设置为 0。失败时返回 `NULL` 并将 `errno` 设置为适当的非零值。在设置 `FTS_STOP` 标志或到达流末尾后再次调用时，`fts_read` 返回 `NULL` 且不修改 `errno`。

`fts_children` 函数成功时返回指向文件条目链表的指针。到达文件层次结构末尾时，返回 `NULL` 并将外部变量 `errno` 设置为 0。失败时返回 `NULL` 并将 `errno` 设置为适当的非零值。

`fts_set` 函数成功时返回 0，如果 `instr` 参数无效则返回 -1。

`fts_get_clientptr` 函数返回与其参数关联的客户端数据指针，如果未设置则返回 `NULL`。

`fts_get_stream` 函数返回与其参数关联的 `fts` 流指针。

`fts_close` 函数成功时返回 0，发生错误时返回 -1。

## 错误

`fts_open` 和 `fts_open_b` 函数可能失败并为库函数 [open(2)](../sys/open.2.md) 和 malloc(3) 指定的任何错误设置 `errno`。如果缺少 blocks 运行时，`fts_open_b` 函数还可能失败并将 `errno` 设置为 `ENOSYS`。

`fts_close` 函数可能失败并为库函数 [chdir(2)](../sys/chdir.2.md) 和 [close(2)](../sys/close.2.md) 指定的任何错误设置 `errno`。

`fts_read` 和 `fts_children` 函数可能失败并为库函数 [chdir(2)](../sys/chdir.2.md)、malloc(3)、opendir(3)、readdir(3) 和 [stat(2)](../sys/stat.2.md) 指定的任何错误设置 `errno`。

此外，`fts_children`、`fts_open` 和 `fts_set` 函数可能失败并按如下方式设置 `errno`：

**[`EINVAL`]** 选项无效，或列表为空。

## 参见

[find(1)](../man1/find.1.md), [chdir(2)](../sys/chdir.2.md), [stat(2)](../sys/stat.2.md), [ftw(3)](ftw.3.md), [qsort(3)](../stdlib/qsort.3.md)

## 历史

`fts` 接口首次引入于 4.4BSD。`fts_get_clientptr`、`fts_get_stream` 和 `fts_set_clientptr` 函数引入于 FreeBSD 5.0，主要用于提供使用不同数据结构的 `fts` 功能替代接口。Blocks 支持以及 `FTS_COMFOLLOWDIR` 和 `FTS_NOSTAT` 选项在 FreeBSD 15.0 中添加，基于 macOS 中的类似功能。

## 缺陷

如果提供了 `FTS_LOGICAL` 选项，或无法 [open(2)](../sys/open.2.md) 当前目录，`fts_open` 函数将自动设置 `FTS_NOCHDIR` 选项。

