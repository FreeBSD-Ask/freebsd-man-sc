# getsubopt(3)

`getsubopt` — 从参数中获取子选项

## 名称

`getsubopt`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
extern char *suboptarg;

int
getsubopt(char **optionp, char * const *tokens, char **valuep);
```

## 描述

`getsubopt` 函数解析一个包含由一个或多个制表符、空格或逗号（`,`）分隔的标记的字符串。它用于解析作为实用程序命令行一部分提供的一组选项参数。

参数 `optionp` 是指向字符串指针的指针。参数 `tokens` 是指向以 `NULL` 结尾的字符串指针数组的指针。

`getsubopt` 函数返回 `tokens` 数组中引用与字符串中第一个标记匹配的字符串的指针的从零开始的偏移量；若字符串不含标记或 `tokens` 中不含匹配的字符串，则返回 -1。

若标记的形式为 ``name=value``，`valuep` 所引用的位置将被设置为指向该标记中“value”部分的起始处。

从 `getsubopt` 返回时，`optionp` 将被设置为指向字符串中下一个标记的起始处，若不再有标记则指向字符串末尾的空字符。外部变量 `suboptarg` 将被设置为指向当前标记的起始处，若不存在标记则为 `NULL`。参数 `valuep` 将被设置为指向该标记的“value”部分，若不存在“value”部分则为 `NULL`。

## 实例

```c
char *tokens[] = {
	#define	ONE	0
		"one",
	#define	TWO	1
		"two",
	NULL
};

...

extern char *optarg, *suboptarg;
char *options, *value;

while ((ch = getopt(argc, argv, "ab:")) != -1) {
	switch(ch) {
	case 'a':
		/* 处理 "a" 选项 */
		break;
	case 'b':
		options = optarg;
		while (*options) {
			switch(getsubopt(&options, tokens, &value)) {
			case ONE:
				/* 处理 "one" 子选项 */
				break;
			case TWO:
				/* 处理 "two" 子选项 */
				if (!value)
					error("no value for two");
				i = atoi(value);
				break;
			case -1:
				if (suboptarg)
					error("illegal sub option %s",
					  suboptarg);
				else
					error("missing sub option");
				break;
			}
		}
		break;
	}
}
```

## 参见

[getopt(3)](getopt.3.md), [strsep(3)](../string/strsep.3.md)

## 历史

`getsubopt` 函数首次出现于 4.4BSD。
