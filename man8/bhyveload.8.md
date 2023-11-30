  BHYVELOAD(8)  

BHYVELOAD(8)

FreeBSD System Manager's Manual

BHYVELOAD(8)

[名称](#__u540D___u79F0_)
=======================

`bhyveload` —

在 bhyve 虚拟机中加载 FreeBSD 来宾

[概要](#__u6982___u8981_)
=======================

`bhyveload` \[`-C`\] \[`-S`\] \[`-c` cons-dev\] \[`-d` disk-path\] \[`-e` name=value\] \[`-h` host-path\] \[`-l` os-loader\] \[`-m` memsize\[K|k|M|m|G|g|T|t\]\] vmname

[描述](#__u63CF___u8FF0_)
=======================

`bhyveload` 用于 在 bhyve(4) 虚拟机中加载 FreeBSD 来宾。

`bhyveload` 它基于 loader(8) 并将在用户终端上显示与 FreeBSD 加载程序相同的界面。可以通过指定不同的 OS 加载程序来更改此行为。

虚拟机被标识为 vmname ，如果它不存在，将被创建。

[选项](#__u9009___u9879_)
=======================

可以使用以下选项：

[`-c`](#c) cons-dev

cons-dev 是一个用于 `bhyveload` 终端I/O的 tty(4) 设备。

文本字符串 "stdio" 也被接受并选择使用无缓冲的标准 I/O。这是默认值。

[`-d`](#d) disk-path

disk-path 是来宾引导磁盘映像的路径名。

[`-e`](#e) name=value

将 FreeBSD 加载程序环境变量 name 设置为 value 。

该选项可以多次使用以设置多个环境变量。

[`-h`](#h) host-path

host-path 是来宾引导文件系统顶部的目录。

[`-l`](#l) os-loader

指定不同的操作系统加载程序。默认情况下 `bhyveload` 将使用 /boot/userboot.so ，它提供了一个标准的 FreeBSD 加载器。

[`-m`](#m) memsize\[K|k|M|m|G|g|T|t\]

memsize 是分配给来宾的内存量。

memsize 参数可以以 `K`, `M`, `G` 或 `T` (大写或小写)中的一个作为后缀，分别表示 Kilobytes、Megabytes、Gigabytes 或 Terabytes 的倍数。

memsize 默认为 256M。

[`-C`](#C)

`bhyveload` 转储核心时，在核心文件中包含来宾内存 。这用于调试 OS 加载程序，因为它允许检查来宾内存。

[`-S`](#S)

连接访客内存。

[实例](#__u5B9E___u4F8B_)
=======================

要创建一个名为 freebsd-vm 的虚拟机，它会从 ISO 映像 /freebsd/release.iso 启动并分配 1GB 内存：

`bhyveload -m 1G -d /freebsd/release.iso freebsd-vm`

要创建一个名为 test-vm 的虚拟机 ，分配 256MB 内存，主机目录 /user/images/test 下的来宾根文件系统和终端 I/O 发送到 nmdm(4) 设备 /dev/nmdm1B

`bhyveload -m 256MB -h /usr/images/test -c /dev/nmdm1B test-vm`

[参见](#__u53C2___u89C1_)
=======================

bhyve(4), nmdm(4), vmm(4), bhyve(8), loader(8)

[历史](#__u5386___u53F2_)
=======================

`bhyveload` 首次出现在 FreeBSD 10.0 中。

[作者](#__u4F5C___u8005_)
=======================

`bhyveload` 是由NetApp公司的 Neel Natu <[neel@FreeBSD.org](mailto:neel@FreeBSD.org)\> 在 Doug Rabson <[dfr@FreeBSD.org](mailto:dfr@FreeBSD.org)\> 的帮助下开发的。

[缺陷](#__u7F3A___u9677_)
=======================

`bhyveload` 只能以访客身份加载 FreeBSD 。

June 24, 2016

FreeBSD 13.1-RELEASE