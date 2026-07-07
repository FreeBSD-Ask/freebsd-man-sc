# getopt.3

`getopt` — 从命令行参数列表中获取选项字符

## 名称

`getopt`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
extern char *optarg;
extern int optind;
extern int optopt;
extern int opterr;
extern int optreset;

int
getopt(int argc, char * const argv[], const char *optstring);
```

## 描述

`getopt` 函数增量式地解析命令行参数列表 `argv`，并返回下一个*已知*的选项字符。若某个选项字符已在接受的选项字符字符串 `optstring` 中指定，则该选项字符是*已知*的。

选项字符串 `optstring` 可包含以下元素：单个字符，以及后跟冒号（`:`）的字符（表示该选项后需带参数）。若单个字符后跟两个冒号（`::`），则选项参数是可选的；`optarg` 被设置为当前 `argv` 词的其余部分，若当前词中没有更多字符则为 `NULL`。这是 POSIX 未涵盖的扩展。

例如，选项字符串 `"x"` 识别选项“`-x`”。

选项字符串 `"x:"` 识别带参数的选项，包括“`-xarg`”和“`-x` `arg`”两种形式。选项的参数是否为独立的词对 `getopt` 并无影响。

选项字符串 `"x::"` 识别不带参数的选项“`-x`”，以及带参数的选项“`-xarg`”。在后一种情况下，参数必须是同一 `argv` 词的一部分。“`-x`”和“`arg`”在命令行中不能以空白分隔。

从 `getopt` 返回时，若预期有选项参数，`optarg` 指向该参数，变量 `optind` 包含下一次调用 `getopt` 时要处理的下一个 `argv` 参数的索引。变量 `optopt` 保存 `getopt` 返回的最后一个*已知*选项字符。

变量 `opterr` 和 `optind` 均初始化为 1。在一组 `getopt` 调用之前，可将 `optind` 设置为其他值，以跳过更多或更少的 argv 条目。

为了使用 `getopt` 解析多组参数，或对同一组参数多次解析，必须在第二次及后续每组 `getopt` 调用之前将变量 `optreset` 设置为 1，并重新初始化变量 `optind`。

当参数列表耗尽时，`getopt` 函数返回 -1。参数列表中选项的解释可通过选项 `--`（双连字符）取消，该选项使 `getopt` 发出参数处理结束的信号并返回 -1。当所有选项处理完毕后（即到达第一个非选项参数时），`getopt` 返回 -1。

## 返回值

`getopt` 函数返回 `optstring` 中的下一个已知选项字符。若 `getopt` 遇到不在 `optstring` 中的字符，或检测到缺少选项参数，则返回 `?`（问号）。若 `optstring` 以 `:` 开头，则缺少选项参数时返回 `:` 而非 `?`。无论哪种情况，变量 `optopt` 都被设置为导致错误的字符。当参数列表耗尽时，`getopt` 函数返回 -1。

## 实例

```c
#include <unistd.h>
int bflag, ch, fd;

bflag = 0;
while ((ch = getopt(argc, argv, "bf:")) != -1) {
	switch (ch) {
	case 'b':
		bflag = 1;
		break;
	case 'f':
		if ((fd = open(optarg, O_RDONLY, 0)) < 0) {
			(void)fprintf(stderr,
			    "myname: %s: %s\n", optarg, strerror(errno));
			exit(1);
		}
		break;
	case '?':
	default:
		usage();
	}
}
argc -= optind;
argv += optind;
```

## 诊断

若 `getopt` 函数遇到不在字符串 `optstring` 中的字符，或检测到缺少选项参数，它会向 `stderr` 输出错误消息并返回 `?`。将 `opterr` 设置为零可禁用这些错误消息。若 `optstring` 以 `:` 开头，则缺少选项参数时返回 `:` 并抑制所有错误消息。

选项参数允许以“`-`”开头；这是合理的，但减少了可能的错误检查量。

## 参见

getopt(1), [getopt_long(3)](getopt_long.3.md), [getsubopt(3)](getsubopt.3.md)

## 标准

添加 `optreset` 变量是为了能够多次调用 `getopt` 函数。这是对 IEEE Std 1003.2 ("POSIX.2") 规范的扩展。

## 历史

`getopt` 函数出现于 4.3BSD。

## 缺陷

`getopt` 函数曾被规定返回 `EOF` 而非 -1。ISO/IEC 9945-2:1993 ("POSIX.2") 改变了这一点，以将 `getopt` 与 `#include <stdio.h>` 解耦。

单个连字符“`-`”可作为 `optstring` 中的一个字符指定，但它*绝不*应有相关联的参数。这使得 `getopt` 可用于将“`-`”作为选项标志的程序。这种做法是错误的，不应用于任何当前开发中。其存在仅为向后兼容*而保留*。应注意不要将 `-` 作为 `optstring` 的第一个字符，以避免与 GNU `getopt` 的语义冲突，后者对以 `-` 开头的 `optstring` 赋予不同含义。默认情况下，单个连字符使 `getopt` 返回 -1。

也可以将数字作为选项字母处理。这使得 `getopt` 可用于将数字（“`-3`”）作为选项的程序。这种做法是错误的，不应用于任何当前开发中。其存在仅为向后兼容*而保留*。以下代码片段在大多数情况下有效。

```c
int ch;
long length;
char *p, *ep;

while ((ch = getopt(argc, argv, "0123456789")) != -1)
	switch (ch) {
	case '0': case '1': case '2': case '3': case '4':
	case '5': case '6': case '7': case '8': case '9':
		p = argv[optind - 1];
		if (p[0] == '-' && p[1] == ch && !p[2]) {
			length = ch - '0';
			ep = "";
		} else if (argv[optind] && argv[optind][1] == ch) {
			length = strtol((p = argv[optind] + 1),
			    &ep, 10);
			optind++;
			optreset = 1;
		} else
			usage();
		if (*ep != '\0')
			errx(EX_USAGE, "illegal number -- %s", p);
		break;
	}
```
