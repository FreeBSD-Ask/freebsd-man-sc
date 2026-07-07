# glob(3)

`glob` — 生成与模式匹配的路径名

## 名称

`glob`, `glob_b`, `globfree`

## 库

Lb libc

## 概要

`#include <glob.h>`

```c
int
glob(const char * restrict pattern, int flags,
    int (*errfunc)(const char *epath, int errno),
    glob_t * restrict pglob);

int
glob_b(const char * restrict pattern, int flags,
    int (^errblk)(const char *epath, int errno),
    glob_t * restrict pglob);

void
globfree(glob_t *pglob);
```

## 描述

`glob` 函数是一个路径名生成器，实现了 shell 所使用的文件名模式匹配规则。

头文件

`#include <glob.h>`

定义了结构类型 `glob_t`，该结构至少包含以下字段：

```c
typedef struct {
	size_t gl_pathc;	/* 到目前为止的路径总数 */
	size_t gl_matchc;	/* 与模式匹配的路径数 */
	size_t gl_offs;		/* 在 gl_pathv 开头保留的数量 */
	int gl_flags;		/* 返回的标志 */
	char **gl_pathv;	/* 与模式匹配的路径列表 */
} glob_t;
```

参数 `pattern` 是指向待展开路径名模式的指针。`glob` 函数将所有可访问的路径名与模式进行匹配，并创建匹配的路径名列表。为获得对路径名的访问权限，`glob` 要求对路径中除最后一个组件外的每个组件具有搜索权限，并对 `pattern` 中包含特殊字符 `*`、`?` 或 `[` 的任何文件名组件的每个目录具有读权限。

`glob` 函数将匹配的路径名数量存入 `gl_pathc` 字段，将指向路径名指针列表的指针存入 `gl_pathv` 字段。最后一个路径名之后的第一个指针为 `NULL`。如果模式不匹配任何路径名，返回的匹配路径数设置为零。

创建 `pglob` 所指向的结构是调用者的责任。`glob` 函数根据需要分配其他空间，包括 `gl_pathv` 所指向的内存。

`flags` 参数用于修改 `glob` 的行为。`flags` 的值是以下在

`#include <glob.h>`

中定义的值的按位或（包含 OR）：

**`GLOB_APPEND`** 将生成的路径名追加到先前一次或多次调用 `glob` 所生成的路径名之后。`gl_pathc` 的值将是此次调用和先前调用找到的匹配总数。路径名是追加到先前调用返回的路径名之后，而非合并。在调用之间，调用者不得更改 `GLOB_DOOFFS` 标志的设置，也不得在设置了 `GLOB_DOOFFS` 时更改 `gl_offs` 的值，也不得（显然）对 `pglob` 调用 `globfree`。

**`GLOB_DOOFFS`** 使用 `gl_offs` 字段。如果设置了此标志，`gl_offs` 用于指定在 `gl_pathv` 字段开头前缀多少个 `NULL` 指针。换言之，`gl_pathv` 将指向 `gl_offs` 个 `NULL` 指针，其后是 `gl_pathc` 个路径名指针，最后是一个 `NULL` 指针。

**`GLOB_ERR`** 使 `glob` 在遇到无法打开或读取的目录时返回。通常，`glob` 会继续查找匹配项。

**`GLOB_MARK`** 每个匹配 `pattern` 且为目录的路径名都追加一个斜杠。

**`GLOB_NOCHECK`** 如果 `pattern` 不匹配任何路径名，则 `glob` 返回仅由 `pattern` 组成的列表，总路径名数设置为 1，匹配路径名数设置为 0。返回的模式中保留了反斜杠转义的效果。

**`GLOB_NOESCAPE`** 默认情况下，反斜杠（`\`）字符用于转义模式中的下一个字符，避免对该字符进行任何特殊解释。如果设置了 `GLOB_NOESCAPE`，则禁用反斜杠转义。

**`GLOB_NOSORT`** 默认情况下，路径名按升序排序；此标志阻止该排序（从而加快 `glob` 的速度）。

以下值也可包含在 `flags` 中，但它们是 IEEE Std 1003.2（"POSIX.2"）的非标准扩展：

```c
void *(*gl_opendir)(const char * name);
struct dirent *(*gl_readdir)(void *);
void (*gl_closedir)(void *);
int (*gl_lstat)(const char *name, struct stat *st);
int (*gl_stat)(const char *name, struct stat *st);
```

**`GLOB_ALTDIRFUNC`** pglob 结构中的以下附加字段已初始化为备用函数，供 glob 用于打开、读取和关闭目录，以及获取在这些目录中找到的名称的 stat 信息。提供此扩展是为了允许诸如 restore(8) 之类的程序从存储在磁带上的目录提供 globbing。

**`GLOB_BRACE`** 预处理模式字符串以展开 `{pat,pat,...}` 字符串，类似于 [csh(1)](../man1/csh.1.md)。由于历史原因，模式 `{}` 保持不展开（[csh(1)](../man1/csh.1.md) 也这样做，以便于输入 [find(1)](../man1/find.1.md) 模式）。

**`GLOB_MAGCHAR`** 如果模式包含 globbing 字符，则由 `glob` 函数设置。有关更多详细信息，请参阅 `gl_matchc` 结构成员的使用说明。

**`GLOB_NOMAGIC`** 与 `GLOB_NOCHECK` 相同，但仅在 `pattern` 不包含任何特殊字符 `*`、`?` 或 `[` 时才追加 `pattern`。提供 `GLOB_NOMAGIC` 是为了简化实现历史 [csh(1)](../man1/csh.1.md) globbing 行为，可能不应用于其他地方。

**`GLOB_TILDE`** 将以 `~` 开头的模式展开为用户名主目录。

**`GLOB_LIMIT`** 将返回的路径名总数限制为 `gl_matchc` 中提供的值（默认为 `ARG_MAX`）。对于可通过展开为大量匹配项的模式（如长字符串 `*/../*/..`）被胁迫进行拒绝服务攻击的程序，应设置此选项。

如果在搜索期间遇到无法打开或读取的目录，且 `errfunc` 为非 `NULL`，`glob` 会调用 `(*errfunc)`(`path`, `errno`)。这可能不太直观：类似 `*/Makefile` 的模式会尝试对 `foo/Makefile` 进行 [stat(2)](../sys/stat.2.md)，即使 `foo` 不是目录，从而导致调用 `errfunc`。错误例程可以通过测试 `ENOENT` 和 `ENOTDIR` 来抑制此操作；但是，当发生这种情况时，`GLOB_ERR` 标志仍会导致立即返回。

如果 `errfunc` 返回非零值，`glob` 在设置 `gl_pathc` 和 `gl_pathv` 以反映已匹配的路径后停止扫描并返回 `GLOB_ABORTED`。如果遇到错误且 `flags` 中设置了 `GLOB_ERR`，也会发生这种情况，无论 `errfunc` 的返回值如何（如果被调用）。如果未设置 `GLOB_ERR` 且 `errfunc` 为 `NULL` 或 `errfunc` 返回零，则忽略错误。

`glob_b` 函数与 `glob` 类似，不同之处在于错误回调是块指针而非函数指针。

`globfree` 函数释放与先前一次或多次调用 `glob` 或 `glob_b` 相关联的 `pglob` 的所有空间。

## 返回值

成功完成时，`glob` 和 `glob_b` 返回零。此外，`pglob` 的字段包含以下描述的值：

**`gl_pathc`** 包含到目前为止匹配的路径名总数。如果指定了 `GLOB_APPEND`，这包括先前调用 `glob` 或 `glob_b` 的其他匹配项。

**`gl_matchc`** 包含当前调用 `glob` 或 `glob_b` 时匹配的路径名数量。

**`gl_flags`** 包含 `flags` 参数的副本，如果 `pattern` 包含任何特殊字符 `*`、`?` 或 `[`，则设置 `GLOB_MAGCHAR` 位，否则清除。

**`gl_pathv`** 包含指向以 `NULL` 结尾的匹配路径名列表的指针。但是，如果 `gl_pathc` 为零，则 `gl_pathv` 的内容未定义。

如果 `glob` 或 `glob_b` 因错误而终止，它会设置 errno 并返回以下非零常量之一，这些常量定义在头文件

`#include <glob.h>`

中：

**`GLOB_NOSPACE`** 尝试分配内存失败，或者如果 `errno` 为 E2BIG，且 `flags` 中指定了 `GLOB_LIMIT`，并且匹配了 `pglob->gl_matchc` 个或更多模式。

**`GLOB_ABORTED`** 扫描因遇到错误而停止，且要么设置了 `GLOB_ERR`，要么 `(*errfunc)()` 返回非零值。

**`GLOB_NOMATCH`** 模式不匹配任何路径名且未设置 `GLOB_NOCHECK`。

参数 `pglob->gl_pathc` 和 `pglob->gl_pathv` 仍按上述设置。

## 实例

使用以下代码可以获得 `ls -l *.c *.h` 的粗略等效效果：

```c
glob_t g;

g.gl_offs = 2;
glob("*.c", GLOB_DOOFFS, NULL, &g);
glob("*.h", GLOB_DOOFFS | GLOB_APPEND, NULL, &g);
g.gl_pathv[0] = "ls";
g.gl_pathv[1] = "-l";
execvp("ls", g.gl_pathv);
```

## 注意事项

`glob` 和 `glob_b` 函数不会匹配以句点开头的文件名，除非明确要求（例如，通过 ".*"）。

## 参见

[sh(1)](../man1/sh.1.md), [fnmatch(3)](fnmatch.3.md), [regex(3)](../man3/regex.3.md)

## 标准

`glob` 函数的当前实现*不*遵循 IEEE Std 1003.2（"POSIX.2"）。不支持排序符号表达式、等价类表达式和字符类表达式。

标志 `GLOB_ALTDIRFUNC`、`GLOB_BRACE`、`GLOB_LIMIT`、`GLOB_MAGCHAR`、`GLOB_NOMAGIC` 和 `GLOB_TILDE`，以及字段 `gl_matchc` 和 `gl_flags` 是 POSIX 标准的扩展，不应被追求严格一致性的应用程序使用。

## 历史

`glob` 和 `globfree` 函数首次出现于 4.4BSD。`glob_b` 函数首次出现于 FreeBSD 15.0。

## 缺陷

超过 `MAXPATHLEN` 长度的模式可能导致未检查的错误。

`glob` 和 `glob_b` 函数可能失败并设置 errno 为库函数 [stat(2)](../sys/stat.2.md)、closedir(3)、opendir(3)、readdir(3)、malloc(3) 和 free(3) 所指定的任何错误。