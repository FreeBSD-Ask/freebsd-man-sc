# mktemp(3)

`mktemp` — 创建临时文件名（唯一）

## 名称

`mktemp`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`Ft char * Fn mktemp char *template Ft int Fn mkstemp char *template Ft int Fn mkostemp char *template int oflags Ft int Fn mkostemps char *template int suffixlen int oflags Ft int Fn mkostempsat int dfd char *template int suffixlen int oflags Ft char * Fn mkdtemp char *template`

`#include <unistd.h>`

`Ft int Fn mkstemps char *template int suffixlen`

## 描述

`mktemp` 函数接受给定的文件名模板，覆盖其中一部分以创建文件名。该文件名在函数调用时保证不存在，适合应用程序使用。模板可以是任何文件名，并在末尾附加若干 `X` 字符，例如 **/tmp/temp.XXXXXXXXXX**。末尾的 `X` 字符被替换为唯一的字母数字组合。`mktemp` 能返回的唯一文件名数量取决于提供的 `X` 字符数；六个 `X` 字符将使 `mktemp` 从 56800235584（`62 ** 6`）个可能的临时文件名中选择一个。

`mkstemp` 函数对模板进行相同的替换，并创建模板文件，模式为 0600，返回一个打开用于读写的文件描述符。这避免了测试文件存在性与打开文件使用之间的竞争。

`mkostemp` 函数类似于 `mkstemp`，但允许指定额外的 [open(2)](../sys/open.2.md) 标志（定义于

`#include <fcntl.h>`

允许的标志为 `O_APPEND`、`O_DIRECT`、`O_SHLOCK`、`O_EXLOCK`、`O_SYNC`、`O_CLOEXEC` 和 `O_CLOFORK`。

`mkstemps` 和 `mkostemps` 函数分别与 `mkstemp` 和 `mkostemp` 行为相同，区别在于它们允许模板中存在后缀。模板应采用 **/tmp/tmpXXXXXXXXXXsuffix** 形式。`mkstemps` 和 `mkostemps` 函数需告知后缀字符串的长度。

`mkostempsat` 函数行为与 `mkostemps` 相同，但额外接受一个目录描述符作为参数。临时文件相对于相应目录创建，若指定特殊值 `AT_FDCWD` 则相对于当前工作目录创建。若模板路径为绝对路径，`dfd` 参数被忽略，行为与 `mkostemps` 相同。

`mkdtemp` 函数对模板进行与 `mktemp` 相同的替换，并创建模板目录，模式为 0700。

## 返回值

`mktemp` 和 `mkdtemp` 函数成功时返回指向模板的指针，失败时返回 `NULL`。`mkstemp`、`mkostemp`、`mkstemps` 和 `mkostemps` 函数若无法创建合适的文件则返回 -1。若任一调用失败，错误码存入全局变量 `errno`。

## 错误

`mkstemp`、`mkostemp`、`mkstemps`、`mkostemps` 和 `mkdtemp` 函数可能将 `errno` 设置为以下值之一：

[`ENOTDIR`] 模板的路径部分不是现有目录。

`mkostemp` 和 `mkostemps` 函数还可能将 `errno` 设置为以下值：

[`EINVAL`] `oflags` 参数无效。

`mkstemp`、`mkostemp`、`mkstemps`、`mkostemps` 和 `mkdtemp` 函数还可能将 `errno` 设置为 [stat(2)](../sys/stat.2.md) 函数指定的任何值。

`mkstemp`、`mkostemp`、`mkstemps` 和 `mkostemps` 函数还可能将 `errno` 设置为 [open(2)](../sys/open.2.md) 函数指定的任何值。

`mkdtemp` 函数还可能将 `errno` 设置为 [mkdir(2)](../sys/mkdir.2.md) 函数指定的任何值。

## 注释

导致核心转储的一个常见问题是程序员将只读字符串传递给 `mktemp`、`mkstemp`、`mkstemps` 或 `mkdtemp`。这在 ISO/IEC 9899:1990 ("ISO C89") 编译器普及之前开发的程序中很常见。例如，以 **/tmp/tempfile.XXXXXXXXXX** 为参数调用 `mkstemp` 会导致核心转储，因为 `mkstemp` 试图修改给定的字符串常量。

`mkdtemp`、`mkstemp` 和 `mktemp` 函数原型也可从

`#include <unistd.h>`

获取。

## 参见

[chmod(2)](../sys/chmod.2.md), [getpid(2)](../sys/getpid.2.md), [mkdir(2)](../sys/mkdir.2.md), [open(2)](../sys/open.2.md), [stat(2)](../sys/stat.2.md)

## 标准

`mkstemp` 和 `mkdtemp` 函数预期遵循 IEEE Std 1003.1-2008 ("POSIX.1")。`mktemp` 函数预期遵循 IEEE Std 1003.1-2001 ("POSIX.1")，但未被 IEEE Std 1003.1-2008 ("POSIX.1") 指定。`mkostemp` 函数遵循 -p1003.1-2024。`mkstemps`、`mkostemps` 和 `mkostempsat` 函数不遵循任何标准。

## 历史

`mktemp` 函数出现于 Version 7 AT&T UNIX。`mkstemp` 函数出现于 4.4BSD。`mkdtemp` 函数首次出现于 OpenBSD 2.2，后出现于 FreeBSD 3.2。`mkstemps` 函数首次出现于 OpenBSD 2.4，后出现于 FreeBSD 3.4。`mkostemp` 和 `mkostemps` 函数出现于 FreeBSD 10.0。`mkostempsat` 函数出现于 FreeBSD 13.0。

## 缺陷

此函数族生成的文件名可被猜测，但使用大量 `X` 字符增加可能的临时文件名数量时风险降低。这使得 `mktemp` 中测试文件存在性（在 `mktemp` 函数调用中）与打开文件使用（稍后在用户应用程序中）之间的竞争从安全角度特别危险。只要可能，应改用 `mkstemp`、`mkostemp` 或 `mkostempsat`，因为它们不存在竞争条件。若无法使用 `mkstemp`，`mktemp` 创建的文件名应使用 [open(2)](../sys/open.2.md) 的 `O_EXCL` 标志创建，并测试调用的返回状态以判断失败。这可确保程序在攻击者已创建该文件意图操纵或读取其内容时不会盲目继续。
