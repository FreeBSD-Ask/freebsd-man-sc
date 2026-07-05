# head.1

`head` — 显示文件的开头若干行

## 名称

`head`

## 概要

`head [-qv] [-n count | -c bytes] [file]`

## 描述

该过滤器显示每个指定文件的前 `count` 行或 `bytes` 字节，如果未指定文件则显示标准输入的内容。如果省略 `count`，默认为 10。

选项如下：

**`-c`** `bytes`, `--bytes`=`bytes` 打印每个指定文件的 `bytes` 字节。

**`-n`** `count`, `--lines`=`count` 打印每个指定文件的 `count` 行。`count` 和 `bytes` 均可使用 expand_number(3) 所支持的大小后缀来指定。

**`-q`**, `--quiet`, `--silent` 当检查多个文件时，禁止打印文件头。

**`-v`**, `--verbose` 在每个文件前添加文件头。

如果指定了多个文件，或使用了 `-v` 选项，每个文件前都会有一个由字符串 “==> XXX <==” 组成的文件头，其中 “XXX” 是文件名。`-q` 选项在所有情况下都禁止打印文件头。

## 退出状态

`head` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

显示文件 `foo` 的前 500 行：

```sh
$ head -n 500 foo
```

`head` 可以与 [tail(1)](tail.1.md) 配合使用，例如只显示文件 `foo` 的第 500 行：

```sh
$ head -n 500 foo | tail -n 1
```

## 参见

[tail(1)](tail.1.md), expand_number(3)

## 历史

`head` 命令首次出现于 PWB UNIX。
