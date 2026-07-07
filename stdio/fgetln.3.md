# fgetln(3)

`fgetln` — 从流中获取一行

## 名称

`fgetln`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft char * Fn fgetln FILE *stream size_t *len`

## 描述

`fgetln` 函数返回指向 `stream` 所引用流的下一行的指针。该行 **并非** C 字符串，因为它不以终止 `NUL` 字符结尾。行的长度（包括最后的换行符）存储在 `len` 所指向的内存位置。（但注意，如果该行是文件中不以换行符结尾的最后一行，返回的文本将不包含换行符。）

## 返回值

成功完成时返回一个指针；该指针在 `stream` 上的下一次 I/O 操作（无论是否成功）后或流关闭后即变为无效。否则返回 `NULL`。`fgetln` 函数不区分文件末尾和错误；必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来确定发生的是哪种情况。发生错误时，全局变量 `errno` 被设置以指示错误。文件末尾条件会被记住，即使在终端上也是如此，所有后续的读取尝试都将返回 `NULL`，直到用 clearerr(3) 清除该条件。

返回指针所指向的文本可以被修改，前提是不超过返回的大小进行更改。一旦指针变为无效，这些更改即丢失。

## 错误

**`EBADF`** 参数 `stream` 不是为读取而打开的流。

**`ENOMEM`** 由于可用内存不足，或因为需要扩展的大小超过 INT_MAX，内部行缓冲区无法扩展。

`fgetln` 函数也可能失败并为 [fflush(3)](fflush.3.md)、malloc(3)、[read(2)](../sys/read.2.md)、[stat(2)](../sys/stat.2.md) 或 realloc(3) 所指定的任何错误设置 `errno`。

## 参见

[ferror(3)](ferror.3.md), [fgets(3)](fgets.3.md), [fgetwln(3)](fgetwln.3.md), [fopen(3)](fopen.3.md), [getline(3)](getline.3.md), [putc(3)](putc.3.md)

## 历史

`fgetln` 函数首次出现于 4.4BSD。

## 注意事项

由于返回的缓冲区不是 C 字符串（不以 NUL 结尾），常见做法是将换行符替换为 `'\0'`。但是，如果文件中最后一行不包含换行符，返回的文本也不会包含换行符。以下代码演示了如何通过分配临时缓冲区来处理此问题：

```c
	char *buf, *lbuf;
	size_t len;
	lbuf = NULL;
	while ((buf = fgetln(fp, &len)) != NULL) {
		if (buf[len - 1] == '\n')
			buf[len - 1] = '\0';
		else {
			/* 文件末尾无换行符，复制并添加 NUL */
			if ((lbuf = malloc(len + 1)) == NULL)
				err(1, NULL);
			memcpy(lbuf, buf, len);
			lbuf[len] = '\0';
			buf = lbuf;
		}
		printf("%s\n", buf);
	}
	free(lbuf);
	if (ferror(fp))
		err(1, "fgetln");
```
