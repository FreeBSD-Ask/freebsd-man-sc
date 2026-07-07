# fsck_msdosfs(8)

`fsck_msdosfs` — DOS/Windows (FAT) 文件系统一致性检查器

## 名称

`fsck_msdosfs`

## 概要

`fsck_msdosfs -p [-BCf] filesystem ...`

`fsck_msdosfs [-BCMny] filesystem ...`

## 描述

`fsck_msdosfs` 工具用于校验和修复 FAT 文件系统（通常称为 DOS 文件系统）。

`fsck_msdosfs` 的第一种形式用于预检（preen）指定的文件系统。它通常在自动重启期间，当检测到 FAT 文件系统时，由从 **/etc/rc** 启动的 [fsck(8)](fsck.8.md) 调用。在预检文件系统时，`fsck_msdosfs` 会以非交互方式修复常见的不一致问题。如果发现更严重的问题，`fsck_msdosfs` 不会尝试修复，而是指出操作未成功并退出。

`fsck_msdosfs` 的第二种形式会检查指定的文件系统，并尝试修复所有检测到的不一致问题，在进行任何更改前会请求确认。

选项如下：

**`-B`** 为兼容 [fsck(8)](fsck.8.md) 而忽略。

**`-C`** 为兼容 [fsck(8)](fsck.8.md) 而忽略。

**`-F`** 为兼容封装程序 [fsck(8)](fsck.8.md) 而设，该程序试图确定文件系统是否需要立即在前台清理，或者其清理可以推迟到后台进行。FAT (MS-DOS) 文件系统必须始终在前台清理。使用此选项时始终返回非零退出码。

**`-M`** 使 `fsck_msdosfs` 在检查 FAT32 文件系统时不使用 [mmap(2)](../man2/mmap.2.md)。此选项主要用于调试目的，通常不需要。当 `fsck_msdosfs` 执行 [mmap(2)](../man2/mmap.2.md) 失败，或指定了 `-M` 时，会自动回退到使用 4 MiB 的简单 LRU 缓存。

**`-f`** 强制 `fsck_msdosfs` 在预检时检查“干净”的文件系统。

**`-n`** 使 `fsck_msdosfs` 对操作员的所有问题都假设回答“`no`”，但“`CONTINUE?`”除外。

**`-p`** 预检指定的文件系统。

**`-y`** 使 `fsck_msdosfs` 对操作员的所有问题都假设回答“`yes`”。

## 参见

[msdosfs(4)](../man4/msdosfs.4.md), [fsck(8)](fsck.8.md)

## 历史

`fsck_msdosfs` 工具首次出现在 NetBSD 1.2 中。`fsck_msdosfs` 首次出现在 FreeBSD 4.4 中。

## 缺陷

`fsck_msdosfs` 工具未编写文档。
