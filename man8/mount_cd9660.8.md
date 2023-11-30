  MOUNT\_CD9660(8)  

MOUNT\_CD9660(8)

FreeBSD System Manager's Manual

MOUNT\_CD9660(8)

[名称](#__u540D___u79F0_)
=======================

`mount_cd9660` —

挂载 ISO-9660 文件系统

[概要](#__u6982___u8981_)
=======================

`mount_cd9660` \[`-begjrv`\] \[`-C` charset\] \[`-o` options\] \[`-s` startsector\] special node

[描述](#__u63CF___u8FF0_)
=======================

`mount_cd9660` 实用程序将驻留在设备上的ISO-9660文件系统附加到 node 指定位置的全局文件系统名称空间。 该命令通常由 mount(8) 在引导时执行。

选项如下：

[`-b`](#b)

放松检查 Supplementary Volume Descriptor Flags 字段，该字段在某些 Joliet 格式化磁盘上设置为错误值。

[`-e`](#e)

启用扩展属性。

[`-g`](#g)

不要去除文件上的版本号。 （默认情况下，如果磁盘上有不同版本号的文件，只会列出最后一个。） 在任何一种情况下，文件都可以在没有明确说明版本号的情况下打开。

[`-j`](#j)

不要使用文件系统中包含的任何 Joliet 扩展。

[`-o`](#o)

选项使用 `-o` 标志指定，后跟以逗号分隔的选项字符串。 有关可能的选项及其含义，请参见 mount(8) 手册页。 以下 cd9660 特定选项可用：

[`extatt`](#extatt)

与 `-e` 相同。

[`gens`](#gens)

与 `-g` 相同。

[`nojoliet`](#nojoliet)

与 `-j` 相同。

[`norrip`](#norrip)

与 `-r` 相同。

[`brokenjoliet`](#brokenjoliet)

与 `-b` 相同。

[`-r`](#r)

不要使用文件系统中包含的任何 Rockridge 扩展。

[`-s`](#s) startsector

在 startsector 启动文件系统。 通常，如果底层设备是 CD-ROM 驱动器， `mount_cd9660` 将尝试找出包含数据的 CD-ROM 中的最后一个轨道，并在那里启动文件系统。 如果设备不是 CD-ROM，或者无法检查目录，则文件系统将在扇区 0 处启动。 此选项可用于覆盖该行为。 请注意， startsector 以 CD-ROM 块为单位，每个块有 2048 个字节。 这与例如 cdcontrol(1) 的 `info` 命令正在打印相同。 通过在此处指定正确的 startsector 扇区，可以安装多会话 CD 的任意会话。

[`-C`](#C) charset

指定本地 charset 以在使用 Joliet 扩展时转换 Unicode 文件名。

[`-v`](#v)

详细说明所做出的起始扇区决策。

[实例](#__u5B9E___u4F8B_)
=======================

以下命令可用于安装 Kodak Photo-CD：

`mount_cd9660 -o rw -v -s 0 /dev/cd0 /cdrom`

[参见](#__u53C2___u89C1_)
=======================

cdcontrol(1), mount(2), unmount(2), cd9660(5), fstab(5), mdconfig(8), mount(8)

[历史](#__u5386___u53F2_)
=======================

`mount_cd9660` 实用程序首次出现在 4.4BSD 中。

Unicode 转换例程由 Ryuichiro Imura <[imura@ryu16.org](mailto:imura@ryu16.org)\> 在 2003 年添加。

[缺陷](#__u7F3A___u9677_)
=======================

目前不支持POSIX设备节点映射。

如果使用Rockridge扩展，则不会删除版本号。

在这种情况下，访问没有Rockridge名称而没有版本号的文件将获得版本号最低的文件，而不是版本号最高的文件。

没有 ECMA 支持。

August 11, 2018

FreeBSD 13.1-RELEASE