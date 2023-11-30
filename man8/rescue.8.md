  RESCUE(8)  

RESCUE(8)

FreeBSD System Manager's Manual

RESCUE(8)

[名称](#__u540D___u79F0_)
=======================

`rescue` —

/rescue 中的救援工具

[描述](#__u63CF___u8FF0_)
=======================

/rescue 目录包含一组用于恢复严重损坏的系统的常用实用程序。 随着从 FreeBSD 5.2 开始过渡到动态链接的根目录， /bin 和 /sbin 中的标准工具很有可能由于升级失败或磁盘错误而无法使用。 /rescue 中的工具是静态链接的，因此应该更能抵抗损坏。 但是，由于是静态链接的， /rescue 中的工具的功能也不如标准实用程序。 特别是，它们没有充分利用 locale、 pam(3), 和 nsswitch 库。

如果您的系统无法启动，并且会显示类似于以下内容的提示：

`Enter full pathname of shell or RETURN for /bin/sh:`

尝试运行的第一件事是标准 shell， /bin/sh 。 如果失败，请尝试运行 /rescue/sh ，它是 `rescue` shell 。 要修复系统，必须首先以读写方式重新挂载根分区。 这可以通过以下 mount(8) 命令完成：

`/rescue/mount -uw /`

下一步是仔细检查 /bin, /sbin 和 /usr/lib 的内容，可能会安装 FreeBSD 救援或 “实时文件系统” CD-ROM（例如，正式发布的 FreeBSD ISO 映像的 `disc2` ）和从那里复制文件。 一旦可以成功运行 /bin/sh, /bin/ls 和其他标准实用程序，请尝试重新启动回到标准系统。

/rescue 工具是使用 crunchgen(1) 编译的，这使得它们比标准实用程序更紧凑。 要构建一个对空间至关重要的 FreeBSD 系统，可以使用 /rescue 替代标准的 /bin 和 /sbin 目录；只需将 /bin 和 /sbin 更改为指向 /rescue 的符号链接。 由于 /rescue 是静态链接的，因此在这样的环境中也应该可以省去很多 /usr/lib 。

与其前身 /stand 不同, /rescue 在正常的 FreeBSD 源代码和二进制升级期间更新。

[文件](#__u6587___u4EF6_)
=======================

/rescue

`rescue` 层次结构的根。

[参见](#__u53C2___u89C1_)
=======================

crunchgen(1), crash(8)

[历史](#__u5386___u53F2_)
=======================

`rescue` 工具最早出现在 FreeBSD 5.2 中。

[作者](#__u4F5C___u8005_)
=======================

`rescue` 系统由 Tim Kientzle <[kientzle@FreeBSD.org](mailto:kientzle@FreeBSD.org)\> 根据 NetBSD 的想法编写。 本手册页由 Simon L. Nielsen <[simon@FreeBSD.org](mailto:simon@FreeBSD.org)\> 根据 Tim Kientzle <[kientzle@FreeBSD.org](mailto:kientzle@FreeBSD.org)\> 的文字编写。

[缺陷](#__u7F3A___u9677_)
=======================

大多数 `rescue` 工具即使在相当残缺的系统中也能工作。 最令人震惊的例外是 vi(1) 的 `rescue` 版本，它当前需要挂载 /usr-
以便它可以访问 termcap(5) 文件。 希望故障安全 termcap(3) 条目最终会被添加到 ncurses(3) 库中，这样 /rescue/vi 即使在 /usr 不能立即挂载的系统中也可以使用。 同时，如果您需要编辑文件，可以从 /rescue/ed 使用 ed(1) 编辑器的 `rescue` 版本，但不能挂载 /usr 。

July 23, 2003

FreeBSD 13.1-RELEASE