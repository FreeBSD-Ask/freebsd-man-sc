# kldxref(8)

`kldxref` — 为内核加载器生成提示信息

## 名称

`kldxref`

## 概要

`kldxref [-Rdv] [-f hintsfile] path ...`

## 描述

`kldxref` 工具用于生成提示文件，其中列出模块、其版本号以及包含这些模块的文件。内核加载器使用这些提示信息来确定特定 KLD 模块的位置。

为命令行中列出的每个包含模块的目录生成单独的提示文件。如果某个目录未生成任何提示记录，则不会创建提示文件，并会移除该目录中已存在的提示文件（如果有的话）。

`kldxref` 仅处理名称中不含点号的文件（如 `kernel`）或以 “.ko” 结尾的文件（如 `foo.ko`）。

可用选项如下：

**`-R`** 递归进入子目录。

**`-d`** 不生成提示文件，而是将模块元数据打印到标准输出。

**`-f`** `hintsfile` 为提示文件指定不同于 `linker.hints` 的名称。

**`-v`** 以详细模式运行。

## 实例

为标准模块和附加模块构建提示文件：

```sh
# kldxref /boot/kernel /boot/modules
```

为所有已安装的内核构建提示文件：

```sh
# kldxref -R /boot
```

## 参见

[kld(4)](../man4/kld.4.md), [kldconfig(8)](kldconfig.8.md), [kldload(8)](kldload.8.md), [kldstat(8)](kldstat.8.md), [kldunload(8)](kldunload.8.md)

## 历史

`kldxref` 工具首次出现于 FreeBSD 5.0。

## 作者

`kldxref` 工具由 Boris Popov <bp@FreeBSD.org> 实现。本手册页面由 Boris Popov <bp@FreeBSD.org> 和 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
