# look(1)

`look` — 显示以指定字符串开头的行

## 名称

`look`

## 概要

`look [-df] [-t termchar] string [file]`

## 描述

`look` 实用程序显示 `file` 中所有以 `string` 作为前缀的行。由于 `look` 执行二分搜索，`file` 中的行必须已排序。

如果未指定 `file`，则使用文件 **`/usr/share/dict/words`**，仅比较字母数字字符，且忽略字母字符的大小写。

可用选项如下：

**`-d`, `--alphanum`** 字典字符集和顺序，即仅比较字母数字字符。

**`-f`, `--ignore-case`** 忽略字母字符的大小写。

**`-t`, `--terminate`** `termchar` 指定字符串终止字符，即仅比较 `string` 中直到并包括首次出现 `termchar` 之前的字符。

## 环境变量

`LANG`、`LC_ALL` 和 `LC_CTYPE` 环境变量会影响 `look` 实用程序的执行。其影响在 [environ(7)](../man7/environ.7.md) 中描述。

## 文件

**`/usr/share/dict/words`** 字典

## 退出状态

`look` 实用程序找到并显示一行或多行时退出值为 0，未找到行时为 1，发生错误时大于 1。

## 实例

在文件 **`/usr/share/dict/words`** 中查找以 `xylen` 开头的行：

```sh
$ look xylen
xylene
xylenol
xylenyl
```

与上例相同，但不考虑 `string` 中第一个 `e` 之后的任何字符。注意，由于搜索的是默认文件 **`/usr/share/dict/words`**，`-f` 隐式启用：

```sh
$ look -t e xylen
Xyleborus
xylem
xylene
xylenol
xylenyl
xyletic
```

## 兼容性

原始手册页指出，当指定 `-d` 选项时，制表符和空白字符参与比较。这是不正确的，当前手册页与历史实现一致。

`-a` 和 `--alternative` 标志为兼容性而被忽略。

## 参见

[grep(1)](grep.1.md), [sort(1)](sort.1.md)

## 历史

`look` 实用程序首次出现于 Version 7 AT&T UNIX。

## 缺陷

行不会按照当前 locale 的排序顺序进行比较。输入文件必须以 `LC_COLLATE` 设置为 `C` 进行排序。
