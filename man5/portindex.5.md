# portindex(5)

`portindex` — 包含 Ports 树状态信息的文件

## 名称

`portindex`

## 描述

`/usr/ports` 中的 port 索引文件包含有关 Ports 树的各种信息。FreeBSD 的每个主分支都有一个独立的索引文件，命名为 “INDEX-`N`”，其中 `N` 是 FreeBSD 分支的主版本号，例如：`INDEX-7` 或 `INDEX-8`。

**`name`** 软件包名称。

**`path`** port 目录的路径。

**`install prefix`** 默认安装前缀。

**`short description`** 简短描述。

**`full description`** 完整描述的路径。

**`maintainer email`** 维护者的电子邮件地址。

**`index`** 该 port 所属的分类。

**`build dependencies`** 在构建该 port 之前需要先安装的 Ports。

**`run dependencies`** 该 port 运行所需安装的 Ports。

**`website`** 该 port 的项目网站。

**`e-deps`** 解压该 port 可能需要的 Ports。

**`p-deps`** 为该 port 打补丁可能需要的 Ports。

**`f-deps`** 抓取该 port 可能需要的 Ports。

## 文件

**/usr/ports/INDEX-**`N`，其中 `N` 是 FreeBSD 分支的主版本号。

## 实例

```sh
vim-6.3.15|/usr/ports/editors/vim|/usr/local|Vi "workalike", with many additional features|/usr/ports/editors/vim/pkg-descr|obrien@FreeBSD.org|editors|libiconv-1.9.2_1|libiconv-1.9.2_1|http://www.vim.org/|||
```

## 参见

[build(7)](../man7/build.7.md), [ports(7)](../man7/ports.7.md)

## 作者

本手册页由 Paul Armstrong 和 Thomas Abthorpe <tabthorpe@FreeBSD.org> 编写。
