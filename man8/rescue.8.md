# rescue(8)

`rescue` — **/rescue** 中的救援工具

## 名称

`rescue`

## 描述

**/rescue** 目录包含一组常用工具，用于恢复严重损坏的系统。随着 FreeBSD 5.2 开始向动态链接的根文件系统过渡，**/bin** 和 **/sbin** 中的标准工具可能因升级失败或磁盘错误而无法使用。**/rescue** 中的工具是静态链接的，因此应该更能抵抗损坏。然而，由于是静态链接，**/rescue** 中的工具功能也不如标准工具完整。特别是，它们无法完整使用 locale、pam(3) 和 nsswitch 库。

如果系统无法引导，并显示类似以下的提示：

```sh
Enter full pathname of shell or RETURN for /bin/sh:
```

首先应尝试运行标准 shell **/bin/sh**。如果失败，再尝试运行 **/rescue/sh**，即 `rescue` shell。要修复系统，必须先以读写模式重新挂载根分区。可使用以下 [mount(8)](mount.8.md) 命令完成：

```sh
/rescue/mount -uw /
```

下一步是仔细检查 **/bin**、**/sbin** 和 **/usr/lib** 的内容，可能需要挂载 FreeBSD 救援 CD-ROM 或“活动文件系统”CD-ROM 并从中复制文件。一旦能够成功运行 **/bin/sh**、**/bin/ls** 和其他标准工具，就可以尝试重新引导回标准系统。

**/rescue** 工具使用 crunchgen(1) 编译，这使得它们比标准工具紧凑得多。在空间极为关键的 FreeBSD 系统中，**/rescue** 可以替代标准的 **/bin** 和 **/sbin** 目录；只需将 **/bin** 和 **/sbin** 改为指向 **/rescue** 的符号链接即可。由于 **/rescue** 是静态链接的，在这种环境中还应该可以省去 **/usr/lib** 的大部分内容。

与其前身 **/stand** 不同，**/rescue** 会在正常的 FreeBSD 源码和二进制升级过程中更新。

## 文件

**/rescue** `rescue` 层次结构的根目录。

## 参见

crunchgen(1), [crash(8)](crash.8.md)

## 历史

`rescue` 工具首次出现于 FreeBSD 5.2。

## 作者

`rescue` 系统由 Tim Kientzle <kientzle@FreeBSD.org> 编写，基于来自 NetBSD 的想法。本手册页由 Simon L. Nielsen <simon@FreeBSD.org> 编写，基于 Tim Kientzle <kientzle@FreeBSD.org> 的文字。

## 缺陷

大多数 `rescue` 工具即使在相当残缺的系统中也能工作。最严重的例外是 `rescue` 版本的 vi(1)，它目前要求挂载 **/usr** 以便访问 termcap(5) 文件。希望最终能在 ncurses(3) 库中加入一个故障安全的 termcap(3) 条目，使得 **/rescue/vi** 即使在无法立即挂载 **/usr** 的系统中也能使用。在此之前，如果你需要编辑文件但无法挂载 **/usr**，可以使用 **/rescue/ed** 中的 `rescue` 版 ed(1) 编辑器。
