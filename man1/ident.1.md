# ident.1

`ident` — 识别文件中的 RCS 关键字字符串

## 名称

`ident`

## 概要

`ident [-q] [-V] [file]`

## 描述

`ident` 实用程序在 `files` 中搜索所有匹配模式 `$keyword: text$` 的实例。

如果未传递参数，则 `ident` 解析标准输入。

*keyword* 必须仅由 C 语言环境中的字母数字值组成，后跟 `:` 和一个空格。

支持的选项：

**`-q`**, `--quiet` 静默模式：如果未找到模式，则抑制警告。

**`-V`**, `--version` 不执行任何操作，为兼容 GNU ident 而添加。

## 退出状态

`ident` 实用程序成功时退出值为 0，发生错误时大于 0。

## 作者

此版本的 `ident` 实用程序由 Baptiste Daroussin <bapt@FreeBSD.org> 和 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
