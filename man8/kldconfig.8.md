  KLDCONFIG(8)  

KLDCONFIG(8)

FreeBSD System Manager's Manual

KLDCONFIG(8)

[名称](#__u540D___u79F0_)
=======================

`kldconfig` —

显示或修改内核模块搜索路径

[概要](#__u6982___u8981_)
=======================

`kldconfig` \[`-dfimnUv`\] \[`-S` sysctlname\] \[path ...\] `kldconfig` `-r`

[描述](#__u63CF___u8FF0_)
=======================

当使用 kldload(8) 实用程序或 kldload(2) 系统调用加载模块时， `kldconfig` 实用程序显示或修改内核使用的搜索路径。

可以使用以下选项：

[`-d`](#d)

从模块搜索路径中删除指定的路径。

[`-f`](#f)

如果指定用于添加的路径已存在于搜索路径中，或者指定用于移除的路径不存在于搜索路径中，则不要失败。 这在启动/关闭脚本中可能很有用，用于将路径添加到仍未安装的文件系统，或者在关闭脚本中用于无条件地删除可能在启动期间添加的路径。

[`-i`](#i)

将指定路径添加到搜索路径的开头，而不是结尾。 此选项只能在添加路径时使用。

[`-m`](#m)

不是用指定的路径集替换模块搜索路径，而是在新条目中 “merge” 。

[`-n`](#n)

不要实际更改模块搜索路径。

[`-r`](#r)

显示当前搜索路径。 如果还指定了任何路径，则不能使用此选项。

[`-S`](#S) sysctlname

指定要使用的 sysctl 名称，而不是默认的 kern.module\_path 。

[`-U`](#U)

“Unique-ify” 当前搜索路径 - 如果任何目录重复一次或多次，则只保留第一次出现。 此选项暗示 `-m` 。

[`-v`](#v)

详细输出：显示新模块搜索路径。 如果路径已更改，并且多次指定 `-v` 标志，则旧路径也会显示。

[文件](#__u6587___u4EF6_)
=======================

/boot/kernel, /boot/modules, /modules

内核使用的默认模块搜索路径。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `kldconfig` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示模块搜索路径

$ kldconfig -r /boot/kernel;/boot/modules;/boot/dtb;/boot/dtb/overlays 

尝试从搜索路径中删除 /boot 目录。该命令将失败：

$ kldconfig -d /boot kldconfig: not in module search path: /boot $ echo $? 1 

同上，但强制操作。这次命令将成功：

$ kldconfig -d -f /boot $ echo $? 0 

将 /boot 目录添加到搜索路径的开头并显示额外的详细输出：

$ kldconfig -i -m -vv /boot /boot/kernel;/boot/modules -> /boot;/boot/kernel;/boot/modules 

如果没有 `-m` ， `-i` 标志将覆盖搜索路径列表的内容：

$ kldconfig -i -vv /boot /boot;/boot/kernel;/boot/modules;/boot/dtb;/boot/dtb/overlays -> /boot 

与上面相同，但使用 `-n` 来模拟操作而不实际执行它：

$ kldconfig -i -n -vv /boot /boot;/boot/kernel;/boot/modules;/boot/dtb;/boot/dtb/overlays -> /boot 

将目录添加到搜索路径以删除重复项。 请注意，如果任何目录已经在搜索路径中，则需要 `-f` 来强制执行操作。 /boot/kernel 目录将被添加一次：

$ kldconfig -f -U /boot/kernel /boot/kernel /boot/modules /boot/dtb /boot/dtb/overlays 

[参见](#__u53C2___u89C1_)
=======================

kldload(2), kldload(8), kldxref(8), sysctl(8)

[历史](#__u5386___u53F2_)
=======================

`kldconfig` 实用程序首次出现在 FreeBSD 4.4 中。

[作者](#__u4F5C___u8005_)
=======================

Peter Pentchev <[roam@FreeBSD.org](mailto:roam@FreeBSD.org)\>

September 29, 2020

FreeBSD 13.1-RELEASE