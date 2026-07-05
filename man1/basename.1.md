# basename.1

`basename` — 返回路径名中的文件名或目录部分

## 名称

`basename`, `dirname`

## 概要

`basename string [suffix] basename [-a] [-s suffix] string [...] dirname string [...]`

## 描述

`basename` 实用程序删除 `string` 中（在先去除尾部斜杠后）以最后一个斜杠 `/` 字符结尾的任何前缀，以及 `suffix`（如果给定）。如果 `suffix` 与 `string` 中剩余字符完全相同，则不去除 `suffix`。结果文件名写入标准输出。不存在的后缀被忽略。如果指定了 `-a`，则每个参数都被视为一个 `string`，如同 `basename` 仅以一个参数调用。如果指定了 `-s`，则将 `suffix` 作为其参数，所有其他参数被视为 `string`。

`dirname` 实用程序删除从 `string` 中（在先去除尾部斜杠后）最后一个斜杠 `/` 字符开始到末尾的文件名部分，并将结果写入标准输出。

## 退出状态

`basename` 实用程序在成功时退出 0，发生错误时退出 >0。

## 实例

以下行将 shell 变量 `FOO` 设置为 **`/usr/bin`**。

```sh
FOO=`dirname /usr/bin/trail`
```

## 参见

[csh(1)](csh.1.md), [sh(1)](sh.1.md), basename(3), dirname(3)

## 标准

`basename` 和 `dirname` 实用程序预期兼容 IEEE Std 1003.2 ("POSIX.2") 标准。

## 历史

`basename` 实用程序首次出现在 Version 7 AT&T UNIX。`dirname` 实用程序首次出现在 AT&T System III UNIX。
