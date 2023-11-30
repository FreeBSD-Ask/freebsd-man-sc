  KLDSTAT(8)  

KLDSTAT(8)

FreeBSD System Manager's Manual

KLDSTAT(8)

[名称](#__u540D___u79F0_)
=======================

`kldstat` —

显示动态内核链接器的状态

[概要](#__u6982___u8981_)
=======================

`kldstat` \[`-h`\] \[`-q`\] \[`-v`\] \[`-d`\] \[`-i` id\] \[`-n` filename\] `kldstat` \[`-q`\] \[`-d`\] \[`-m` modname\]

[描述](#__u63CF___u8FF0_)
=======================

`kldstat` 实用程序显示动态链接到内核的任何文件的状态。

可以使用以下选项：

[`-h`](#h)

以人类可读的形式显示尺寸字段，使用单位后缀而不是十六进制值。

[`-v`](#v)

更冗长。

[`-d`](#d)

显示模块特定数据（如 int、unsigned int 和 unsigned long）

[`-i`](#i) id

仅显示具有此 ID 的文件的状态。

[`-n`](#n) filename

仅显示具有此文件名的文件的状态。

[`-q`](#q)

仅检查文件是否已加载或编译到内核中。

[`-m`](#m) modname

仅显示具有此 modname 的模块的状态。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `kldstat` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示动态链接到内核的文件。 请注意，内核本身显示在列表中。 _Refs_ 显示了每个文件引用的模块数量：

$ kldstat Id Refs Address Size Name 1 38 0xffffffff80200000 2448f20 kernel 2 3 0xffffffff82649000 b7bd8 linux.ko 3 5 0xffffffff82701000 9698 linux\_common.ko 4 1 0xffffffff82b11000 1eae linsysfs.ko 5 1 0xffffffff82b13000 f2af8 nvidia-modeset.ko 6 1 0xffffffff82c06000 122b020 nvidia.ko 7 1 0xffffffff83e32000 2668 intpm.ko 8 1 0xffffffff83e35000 b50 smbus.ko 9 1 0xffffffff83e36000 18a0 uhid.ko 10 1 0xffffffff83e38000 2928 ums.ko 11 1 0xffffffff83e3b000 1aa0 wmt.ko 12 1 0xffffffff83e3d000 cd70 snd\_uaudio.ko 

显示 _linux_ 文件的详细状态并以人类可读的方式显示大小：

$ kldstat -h -v -n linux Id Refs Address Size Name 2 3 0xffffffff82649000 735K linux.ko (/boot/kernel/linux.ko) Contains modules: Id Name 2 linuxelf 

与上面使用文件的 _id_ 相同：

$ kldstat -h -i 2 -v Id Refs Address Size Name 2 3 0xffffffff82649000 735K linux.ko (/boot/kernel/linux.ko) Contains modules: Id Name 2 linuxelf 

显示从上例中获取的 _linuxelf_ 模块的状态：

$ kldstat -v -m linuxelf Id Refs Name 2 1 linuxelf 

显示 _g\_raid_ 模块的模块特定数据：

$ kldstat -d -m g\_raid Id Refs Name data..(int, uint, ulong) 366 1 g\_raid (0, 0, 0x0) 

检查模块 _fakefile_ 是否已链接。如果是则返回 0，否则返回 1：

$ kldstat -q -n fakefile || echo file not linked file not linked 

[参见](#__u53C2___u89C1_)
=======================

kldstat(2), kldload(8), kldunload(8)

[历史](#__u5386___u53F2_)
=======================

`kldstat` 实用程序首次出现在 FreeBSD 3.0 中，取代了 `lkm`-
接口。

[作者](#__u4F5C___u8005_)
=======================

Doug Rabson <[dfr@FreeBSD.org](mailto:dfr@FreeBSD.org)\>

January 19, 2016

FreeBSD 13.1-RELEASE