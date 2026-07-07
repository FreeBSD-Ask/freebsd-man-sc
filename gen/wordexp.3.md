# wordexp(3)

`wordexp` — 执行 shell 风格的单词扩展

## 名称

`wordexp`

## 库

Lb libc

## 概要

`#include <wordexp.h>`

```c
int
wordexp(const char * restrict words, wordexp_t * restrict we,
    int flags);

void
wordfree(wordexp_t *we);
```

## 描述

`wordexp` 函数对 `words` 执行 shell 风格的单词扩展，并将单词列表放入 `we` 的 `we_wordv` 成员中，将单词数量放入 `we_wordc`。

`flags` 参数是以下任意常量的按位或：

**`WRDE_APPEND`** 将单词追加到先前调用 `wordexp` 所生成的单词中。

**`WRDE_DOOFFS`** 在 `we_wordv` 的前面添加由 `we` 的 `we_offs` 成员所指定数量的 `NULL` 指针。

**`WRDE_NOCMD`** 禁止在 `words` 中进行命令替换。使用前请参见 [缺陷](#缺陷) 中的说明。

**`WRDE_REUSE`** `we` 参数已传递给先前成功的 `wordexp` 调用，但尚未传递给 `wordfree`。实现可以重用分配给它的空间。

**`WRDE_SHOWERR`** 不将 shell 错误消息重定向到 **/dev/null**。

**`WRDE_UNDEF`** 在尝试扩展未定义的 shell 变量时报告错误。

`wordexp_t` 结构定义于 `#include <wordexp.h>` 中，如下：

```c
typedef struct {
	size_t	we_wordc;	/* 匹配的单词计数 */
	char	**we_wordv;	/* 指向单词列表的指针 */
	size_t	we_offs;	/* 在 we_wordv 中保留的槽位数 */
} wordexp_t;
```

`wordfree` 函数释放由 `wordexp` 分配的内存。

## 实现说明

`wordexp` 函数使用未公开的 `freebsd_wordexp` shell 内建命令实现。

## 返回值

`wordexp` 函数成功时返回零，否则返回以下错误代码之一：

**`WRDE_BADCHAR`** `words` 参数包含以下未加引号的字符之一：换行符、`|`、`&`、`;`、`<`、`>`、`(`、`)`、`{`、`}`。

**`WRDE_BADVAL`** 成功解析后发生的错误，例如在 `flags` 中设置了 `WRDE_UNDEF` 时尝试扩展未定义的 shell 变量。

**`WRDE_CMDSUB`** 尝试使用命令替换且 `flags` 中设置了 `WRDE_NOCMD`。

**`WRDE_NOSPACE`** 没有足够的内存来存储结果，或在 [fork(2)](../sys/fork.2.md) 期间发生错误。

**`WRDE_SYNTAX`** `words` 中存在 shell 语法错误。

`wordfree` 函数没有返回值。

## 环境变量

**`IFS`** 字段分隔符。

## 实例

对当前目录下的所有 `.c` 文件和 **/etc/motd** 调用编辑器（省略了错误检查）：

```c
wordexp_t we;

wordexp("${EDITOR:-vi} *.c /etc/motd", &we, 0);
execvp(we.we_wordv[0], we.we_wordv);
```

## 诊断

如果在 `flags` 中设置了 `WRDE_SHOWERR`，则来自 shell 的诊断消息将写入标准错误输出。

## 参见

[sh(1)](../man1/sh.1.md), [fnmatch(3)](fnmatch.3.md), [glob(3)](glob.3.md), [popen(3)](popen.3.md), [system(3)](../man3/system.3.md)

## 标准

`wordexp` 和 `wordfree` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 缺陷

当前的 `wordexp` 实现不识别 UTF-8 以外的多字节字符，因为 shell（它调用 shell 来执行扩展）也不识别。

## 安全注意事项

路径名生成可能产生比输入大小呈指数级增大的输出。

尽管此实现能可靠地检测 `WRDE_NOCMD` 的命令替换，但攻击面仍然相当大。此外，某些其他实现（如此实现的较旧版本）即使在设置了 `WRDE_NOCMD` 的情况下也可能执行命令替换。
