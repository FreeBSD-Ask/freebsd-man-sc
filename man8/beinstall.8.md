# beinstall.8

`beinstall.sh` — 使用当前 FreeBSD 源码树安装引导环境

## 名称

`beinstall.sh`

## 概要

`beinstall.sh [options ...]`

## 描述

`beinstall.sh` 使用当前 FreeBSD 源码树安装引导环境。`beinstall.sh` 还会在新引导环境的沙箱中自动执行 **/etc** 更新（使用 etcupdate(8)）和软件包更新（使用 pkg-upgrade(8)）。

成功完成后，系统将准备好引导进入新引导环境。失败时，目标引导环境将被销毁。无论何种情况，正在运行的系统保持不变，不会发生引导进入部分更新系统的情况（由于安装或硬件故障）。此外，整个安装过程只需要一次重启，因为是在新引导环境中执行的。

`beinstall.sh` 需要完全构建好的 world 和 kernel。它还需要 [pkg(8)](pkg.8.md)，该工具不在基本系统中，必须手动安装。

传递给 `beinstall.sh` 的 `options` 是 world 和 kernel 标志，例如 [build(7)](../man7/build.7.md) 中描述的 `KERNCONF`。

## 环境变量

用户可修改的变量。如有需要，可在环境中设置：

**`BE_UTILITY`**（默认：“`bectl`”）管理 ZFS 引导环境的工具。可以是基本系统中的 bectl(8)，或来自 ports（sysutils/beadm）的 beadm(1)。

**`CONFIG_UPDATER`**（默认：“`etcupdate`”）配置更新器：支持 etcupdate(8)。设置为空字符串可跳过。

**`ETCUPDATE_FLAGS`**（默认：“`-F`”）使用 etcupdate(8) 时的标志。

**`NO_PKG_UPGRADE`**（默认：“”）如果非空，将跳过 “`pkg upgrade`”。

## 文件

**src/tools/build/beinstall.sh** `beinstall.sh` 在源码树中的位置。

## 参见

[build(7)](../man7/build.7.md), [development(7)](../man7/development.7.md), bectl(8), etcupdate(8), [pkg(8)](pkg.8.md)

## 历史

`beinstall.sh` 受 Solaris/illumos 风格升级启发，功能与之类似。

`beinstall.sh` 手册页首次出现于 FreeBSD 12.0。

## 作者

`beinstall.sh` 脚本由 Will Andrews <will@FreeBSD.org> 实现。本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
