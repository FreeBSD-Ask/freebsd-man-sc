# elfdump(1)

`elfdump` — 显示 ELF 文件的相关信息

## 名称

`elfdump`

## 概要

`elfdump -a | -E | -cdeGhinprs [-w file] file`

## 描述

`elfdump` 实用程序转储指定 ELF `file` 的各种信息。

选项如下：

**`-a`** 转储所有信息。

**`-c`** 转储节区头。

**`-d`** 转储动态符号。

**`-e`** 转储 ELF 头。

**`-E`** 若 `file` 是 ELF 文件则返回成功，否则返回失败。此选项与其他选项互斥。

**`-G`** 转储 GOT。

**`-h`** 转储哈希值。

**`-i`** 转储动态解释器。

**`-n`** 转储 note 节区。

**`-p`** 转储程序头。

**`-r`** 转储重定位信息。

**`-s`** 转储符号表。

**`-w`** `file` 将输出写入到 `file` 而非标准输出。

## 退出状态

`elfdump` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

以下是 `elfdump` 命令的典型用法示例：

```sh
elfdump -a -w output /bin/ls
```

## 参见

objdump(1), [readelf(1)](readelf.1.md)

> AT&T Unix Systems Labs, "System V Application Binary Interface", <http://www.sco.com/developers/gabi/>.

## 历史

`elfdump` 实用程序首次出现于 FreeBSD 5.0。

## 作者

`elfdump` 实用程序由 Jake Burkholder <jake@FreeBSD.org> 编写。本手册页由 David O'Brien <obrien@FreeBSD.org> 编写。

## 缺陷

未完整实现 ELF gABI。
