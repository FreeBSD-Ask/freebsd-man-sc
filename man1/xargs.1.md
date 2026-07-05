# xargs.1

`xargs` — 构造参数列表并执行实用程序

## 名称

`xargs`

## 概要

`xargs [-0oprt] [-E eofstr] [[-I replstr] [-R replacements] [-S replsize]] [-J replstr] [-L number] [[-n number] [-x]] [-P maxprocs] [-s size] [utility [argument ...]]`

## 描述

`xargs` 实用程序从标准输入读取以空格、制表符、换行符和文件结束符分隔的字符串，并以这些字符串作为参数执行 `utility`。

在命令行上指定的任何参数都会在每次调用时传递给 `utility`，其后是从 `xargs` 标准输入读取的若干参数。重复此过程，直到标准输入耗尽。

可以使用单引号（' '）、双引号（""）或反斜杠（\）在参数中嵌入空格、制表符和换行符。单引号会转义除换行符以外的所有非单引号字符，直到匹配的右单引号。双引号会转义除换行符以外的所有非双引号字符，直到匹配的右双引号。任何单个字符（包括换行符）都可以用反斜杠转义。

选项如下：

**`-0`**, `--null` 改变 `xargs`，使其期望 NUL（'\0'）字符作为分隔符，而非空格和换行符。这预期与 [find(1)](find.1.md) 中的 `-print0` 功能配合使用。

**`-E`** `eofstr` 使用 `eofstr` 作为逻辑 EOF 标记。

**`-I`** `replstr` 对每个输入行执行 `utility`，将 `utility` 的最多 `replacements`（若未指定 `-R` 标志则为 5）个参数中 `replstr` 的一次或多次出现替换为整行输入。替换后，生成的参数不允许超过 `replsize`（若未指定 `-S` 标志则为 255）字节；这是通过将包含 `replstr` 的参数尽可能多地拼接到 `utility` 的构造参数中来实现的，最多 `replsize` 字节。此大小限制不适用于 `utility` 中不包含 `replstr` 的参数，且不会对 `utility` 本身进行替换。隐含 `-x`。

**`-J`** `replstr` 如果指定了此选项，`xargs` 将使用从标准输入读取的数据替换 `replstr` 的第一次出现，而非将该数据附加到所有其他参数之后。此选项不会影响从输入读取的参数数量（`-n`）或 `xargs` 生成的命令大小（`-s`）。该选项只是移动这些参数在执行的命令中的位置。`replstr` 必须作为 `xargs` 的独立 `argument` 出现。例如，如果它在引号字符串中间，则不会被识别。此外，只有 `replstr` 的第一次出现会被替换。例如，以下命令会将当前目录中以大写字母开头的文件和目录列表复制到 `destdir`：

```sh
/bin/ls -1d [A-Z]* | xargs -J % cp -Rp % destdir
```

**`-L`** `number` 每读取 `number` 行调用一次 `utility`。如果到达 EOF 且读取的行数少于 `number`，则用可用行调用 `utility`。

**`-n`** `number`, `--max-args=number` 为每次调用 `utility` 设置从标准输入获取的最大参数数量。如果累积的字节数（参见 `-s` 选项）超过指定的 `size`，或者最后一次调用 `utility` 时剩余参数少于 `number`，则 `utility` 的调用将使用少于 `number` 个标准输入参数。`number` 的当前默认值为 5000。

**`-o`** 在执行命令之前，在子进程中将 stdin 重新打开为 **/dev/tty**。如果希望 `xargs` 运行交互式应用程序，这很有用。

**`-P`** `maxprocs`, `--max-procs=maxprocs` 并行模式：同时运行最多 `maxprocs` 个 `utility` 调用。如果 `maxprocs` 设为 0，`xargs` 将运行尽可能多的进程。

**`-p`**, `--interactive` 回显要执行的每个命令，并询问用户是否应执行。肯定回答（POSIX 语言环境下的 `y`）使命令执行，任何其他回答导致其被跳过。如果进程未连接到终端，则不执行任何命令。

**`-r`**, `--no-run-if-empty` 与 GNU `xargs` 兼容。GNU 版本的 `xargs` 至少运行一次 `utility` 参数，即使 `xargs` 输入为空，且支持 `-r` 选项来抑制此行为。FreeBSD 版本的 `xargs` 在输入为空时不运行 `utility` 参数，但支持 `-r` 选项以保持与 GNU `xargs` 的命令行兼容性，但 `-r` 选项在 FreeBSD 版本的 `xargs` 中不起作用。

**`-R`** `replacements` 指定 `-I` 将进行替换的最大参数数量。如果 `replacements` 为负，则替换的参数数量不受限制。

**`-S`** `replsize` 指定 `-I` 可用于替换的空间量（以字节为单位）。`replsize` 的默认值为 255。

**`-s`** `size`, `--max-chars=size` 设置提供给 `utility` 的命令行长度最大字节数。实用程序名称长度、传递给 `utility` 的参数（包括 `NULL` 终止符）和当前环境的总和将小于或等于此数字。`size` 的当前默认值为 `ARG_MAX` - 4096。

**`-t`**, `--verbose` 在执行命令之前，立即将要执行的命令回显到标准错误。

**`-x`**, `--exit` 如果包含 `number` 个参数的命令行不适合指定的（或默认的）命令行长度，则强制 `xargs` 立即终止。

如果省略 `utility`，则使用 echo(1)。

如果 `utility` 从标准输入读取，可能发生未定义行为。

如果无法组装命令行，或无法调用，或 `utility` 的调用被信号终止，或 `utility` 的调用以值 255 退出，`xargs` 实用程序将停止处理输入，并在所有 `utility` 调用完成处理后退出。

## 退出状态

`xargs` 实用程序若无错误发生，退出值为 0。如果找不到 `utility`，`xargs` 退出值为 127；否则如果无法执行 `utility`，`xargs` 退出值为 126。如果发生任何其他错误，`xargs` 退出值为 1。

## 实例

使用 1 到 9 的数字创建 3x3 矩阵。每个 echo(1) 实例接收三行作为参数：

```sh
$ seq 1 9 | xargs -L3 echo
1 2 3
4 5 6
7 8 9
```

复制标准输入的每一行：

```sh
$ echo -e "one\ntwo\nthree" | xargs -I % echo % %
one one
two two
three three
```

最多并发执行 2 个 [find(1)](find.1.md) 实例，每个使用标准输入中的一个目录：

```sh
echo -e "/usr/ports\n/etc\n/usr/local" | xargs -J % -P2 -n1 find % -name file
```

## 参见

echo(1), [find(1)](find.1.md), execvp(3)

## 标准

`xargs` 实用程序预期符合 IEEE Std 1003.2 ("POSIX.2")。`-J`、`-o`、`-P`、`-R` 和 `-S` 选项是非标准 FreeBSD 扩展，在其他操作系统上可能不可用。

## 历史

`xargs` 实用程序出现于 PWB UNIX。

## 缺陷

如果 `utility` 尝试调用另一个命令，导致参数数量或环境大小增加，则 execvp(3) 可能因 E2BIG 而失败。

`xargs` 实用程序在对 `-I` 和 `-J` 选项进行字符串比较时不考虑多字节字符，在某些语言环境下可能导致错误结果。
