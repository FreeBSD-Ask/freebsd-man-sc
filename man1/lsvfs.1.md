  LSVFS(1)  

LSVFS(1)

FreeBSD General Commands Manual

LSVFS(1)

[名称](#__u540D___u79F0_)
=======================

`lsvfs` —

列出已安装的虚拟文件系统

[概要](#__u6982___u8981_)
=======================

`lsvfs` \[vfsname ...\]

[描述](#__u63CF___u8FF0_)
=======================

`lsvfs` 命令列出有关当前加载的虚拟文件系统模块的信息。当给出 vfsname 参数时， `lsvfs` 列出有关指定 VFS 模块的信息。 否则， `lsvfs` 会列出所有当前加载的模块。信息如下：

Filesystem

文件系统的名称，用于 mount(2) 的 type 参数和 mount(8) 的 `-t` 选项

Num

文件系统类型号。

Refs

引用此 VFS 的次数；即，当前挂载的此类文件系统的数量

Flags

标志位。

[实例](#__u5B9E___u4F8B_)
=======================

显示有关 ‘`ufs`’ 和 devfs(5) 文件系统的信息并检查前者的挂载数量：

$ lsvfs ufs devfs 文件系统 编号 参考 标志 -------------------------------- ---------- ----- --------------- ufs 0x00000035 2 devfs 0x00000071 1 synthetic, jail $ mount -t ufs | wc -l 2 

[参见](#__u53C2___u89C1_)
=======================

mount(2), getvfsbyname(3), mount(8)

[历史](#__u5386___u53F2_)
=======================

一个 `lsvfs` 命令出现在 FreeBSD 2.0 中。

December 28, 2020

FreeBSD 13.1-RELEASE