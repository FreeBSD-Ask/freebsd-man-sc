# getopt_long(3)

`getopt_long` — 从命令行参数列表中获取长选项

## 名称

`getopt_long`, `getopt_long_only`

## 库

Lb libc

## 概要

`#include <getopt.h>`

```c
extern char *optarg;
extern int optind;
extern int optopt;
extern int opterr;
extern int optreset;

int
getopt_long(int argc, char * const *argv, const char *optstring,
    const struct option *longopts, int *longindex);

int
getopt_long_only(int argc, char * const *argv, const char *optstring,
    const struct option *longopts, int *longindex);
```

## 描述

`getopt_long` 函数类似于 [getopt(3)](getopt.3.md)，但它接受两种形式的选项：单词和字符。`getopt_long` 函数提供了 [getopt(3)](getopt.3.md) 功能的超集。`getopt_long` 函数可以两种方式使用。第一种方式中，程序识别的每个长选项都有对应的短选项，option 结构仅用于将长选项转换为短选项。以这种方式使用时，`getopt_long` 的行为与 [getopt(3)](getopt.3.md) 完全相同。这是以最少的重写为现有程序添加长选项处理的好方法。

第二种机制中，长选项在传入的 `option` 结构中设置一个标志，或者对于带参数的选项，将指向命令行参数的指针存储在传入的 `option` 结构中。此外，长选项的参数可以指定为带等号的单一参数，例如：

```sh
myprogram --myoption=somevalue
```

当处理长选项时，对 `getopt_long` 的调用将返回 0。因此，不带快捷方式的长选项处理与 [getopt(3)](getopt.3.md) 不向后兼容。

可以组合这些方法，为某些选项提供带短选项等价物的长选项处理。较少使用的选项仅作为长选项处理。

`getopt_long` 调用需要初始化一个描述长选项的结构。该结构为：

```c
struct option {
	char *name;
	int has_arg;
	int *flag;
	int val;
};
```

`name` 字段应包含不带前导双连字符的选项名。

`has_arg` 字段应为以下值之一：

**`no_argument`** 选项不接受参数
**`required_argument`** 选项需要参数
**`optional_argument`** 选项可接受参数

若 `flag` 不是 `NULL`，则其指向的整数将被设置为 `val` 字段中的值。若 `flag` 字段为 `NULL`，则返回 `val` 字段的值。将 `flag` 设为 `NULL` 并将 `val` 设为对应的短选项，可使此函数的行为与 [getopt(3)](getopt.3.md) 相同。

若 `longindex` 字段不是 `NULL`，则其指向的整数将被设置为该长选项相对于 `longopts` 的索引。

`longopts` 数组的最后一个元素必须填充为零。

`getopt_long_only` 函数的行为与 `getopt_long` 相同，区别在于长选项可以以 `-` 开头而不仅是 `--`。若以 `-` 开头的选项不匹配长选项但匹配单字符选项，则返回该单字符选项。

## 返回值

若 `struct option` 中的 `flag` 字段为 `NULL`，`getopt_long` 和 `getopt_long_only` 返回 `val` 字段中指定的值，通常就是对应的短选项。若 `flag` 不是 `NULL`，这些函数返回 0 并将 `val` 存储在 `flag` 所指向的位置。

这些函数在缺少选项参数且错误消息被抑制时返回 `:`，在用户指定了未知或歧义选项时返回 `?`，在参数列表耗尽时返回 -1。遇到缺少选项参数时的默认行为是输出错误并返回 `?`。在 `optstring` 中指定 `:` 将抑制错误消息并改为返回 `:`。

除 `:` 外，`optstring` 中的前导 `+` 或 `-` 也具有特殊含义。若指定了其中任何一个，必须出现在 `:` 之前。

前导 `+` 表示处理应在第一个非选项参数处停止，与 [getopt(3)](getopt.3.md) 的默认行为一致。不带 `+` 时的默认行为是将非选项参数重排到 `argv` 末尾。

前导 `-` 表示所有非选项参数都应被视为字面 `1` 标志的参数（即函数调用将返回值 1，而非字符字面量 '1'）。

## 环境变量

**`POSIXLY_CORRECT`** 若设置了此变量，则在找到第一个非选项时停止选项处理，且忽略 `optstring` 中的前导 `-` 或 `+`。

## 实例

```c
int bflag, ch, fd;
int daggerset;
/* 选项描述符 */
static struct option longopts[] = {
	{ "buffy",	no_argument,		NULL, 		'b' },
	{ "fluoride",	required_argument,	NULL, 	       	'f' },
	{ "daggerset",	no_argument,		&daggerset,	1 },
	{ NULL,		0,			NULL, 		0 }
};

bflag = 0;
while ((ch = getopt_long(argc, argv, "bf:", longopts, NULL)) != -1) {
	switch (ch) {
	case 'b':
		bflag = 1;
		break;
	case 'f':
		if ((fd = open(optarg, O_RDONLY, 0)) == -1)
			err(1, "unable to open %s", optarg);
		break;
	case 0:
		if (daggerset) {
			fprintf(stderr,"Buffy will use her dagger to "
			    "apply fluoride to dracula's teeth\n");
		}
		break;
	default:
		usage();
	}
}
argc -= optind;
argv += optind;
```

## 实现差异

本节描述与 glibc-2.1.3 中的 GNU 实现之间的差异：

- 对于 `flag` != `NULL` 的长选项，`optopt` 的设置：
  - **GNU** 将 `optopt` 设置为 `val`。
  - **BSD** 将 `optopt` 设置为 0（因为 `val` 永远不会被返回）。

- 对于通过 `-W` 调用且不带参数的长选项（选项字符串中的 `W;`），`optarg` 的设置：
  - **GNU** 将 `optarg` 设置为选项名（即 `-W` 的参数）。
  - **BSD** 将 `optarg` 设置为 `NULL`（即长选项的参数）。

- 对于 `-W` 带有不是已知长选项（或其前缀）的参数时（选项字符串中的 `W;`）的处理：
  - **GNU** 返回 `-W`，并将 `optarg` 设置为该未知选项。
  - **BSD** 将此视为错误（未知选项），返回 `?`，并将 `optopt` 设置为 0、`optarg` 设置为 `NULL`（如 GNU 的 man 页面所记载）。

- **BSD** 不会在与 **GNU** 相同的调用序列位置重排参数向量。不过，调用者通常使用的方面（返回 -1 后的顺序、`optind` 相对于当前位置的值）是相同的。（我们做了更少的变量交换。）

## 参见

[getopt(3)](getopt.3.md)

## 历史

`getopt_long` 和 `getopt_long_only` 函数首次出现于 GNU libiberty 库。`getopt_long` 的首个 BSD 实现出现于 NetBSD 1.5，`getopt_long_only` 的首个 BSD 实现出现于 OpenBSD 3.3。FreeBSD 首次在 FreeBSD 5.0 中引入 `getopt_long`，在 FreeBSD 5.2 中引入 `getopt_long_only`。

## 缺陷

`argv` 参数并非真正的 `const`，因为其元素可能被重排（除非设置了 `POSIXLY_CORRECT`）。

该实现可以完全替代 [getopt(3)](getopt.3.md)，但目前使用的是独立的代码。

`getopt_long_only` 假定第一个参数应当总是被跳过，因为它通常是程序名。因此，将 `optind` 设置为 0 表示 `getopt_long_only` 应当重置，在此过程中 `optind` 将被设置为 1。此行为与 [getopt(3)](getopt.3.md) 不同，后者会按预期处理 `optind` 值 0 并处理第一个元素。
