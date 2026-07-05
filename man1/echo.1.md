# echo.1

`echo` — 将参数写入标准输出

## 名称

`echo`

## 概要

`echo [-n] [string ...]`

## 描述

`echo` 实用程序将任何指定的操作数写入标准输出，操作数之间以单个空白（“` `”）字符分隔，并以换行（`\n`）字符结尾。

以下选项可用：

**`-n`** 不打印尾随换行字符。

结束选项标记 `--` 不被识别，按字面输出。

也可以通过在字符串末尾追加 `\c` 来抑制换行，这与 iBCS2 兼容系统的做法一致。注意，`-n` 选项以及 `\c` 的效果在 IEEE Std 1003.1-2001 ("POSIX.1") 经 Cor. 1-2002 修订中是实现定义的。为了可移植性，仅当第一个参数不以连字符（“`-`”）开头且不包含任何反斜杠（“`\`”）时才应使用 `echo`。如果这不够，应使用 printf(1)。

大多数 shell 提供内建的 `echo` 命令，往往在此实用程序对选项和反斜杠的处理上有所不同。请参阅 [builtin(1)](builtin.1.md) 手册页。

## 退出状态

`echo` 实用程序成功时退出 0，发生错误时退出 >0。

## 实例

选项和反斜杠的特殊处理：

```sh
$ /bin/echo "-hello\tworld"
-hello\tworld
```

避免换行字符：

```sh
$ /bin/echo -n hello;/bin/echo world
helloworld
```

或达到相同结果：

```sh
$ /bin/echo "hello\c";/bin/echo world
helloworld
```

## 参见

[builtin(1)](builtin.1.md), [csh(1)](csh.1.md), printf(1), [sh(1)](sh.1.md)

## 标准

`echo` 实用程序符合 IEEE Std 1003.1-2001 ("POSIX.1") 经 Cor. 1-2002 修订。

## 历史

`echo` 命令首次出现于 Version 2 AT&T UNIX。

## 注意事项

`echo` 命令在许多方面（包括转义字符处理）与内建的 `echo` shell 命令行为不同。它在不同系统之间的行为也有所不同，因此使编写可移植脚本变得复杂。建议使用 printf(1) 命令来避免这些缺陷。
