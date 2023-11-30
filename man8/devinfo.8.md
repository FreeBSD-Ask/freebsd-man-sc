  DEVINFO(8)  

DEVINFO(8)

FreeBSD System Manager's Manual

DEVINFO(8)

[名称](#__u540D___u79F0_)
=======================

`devinfo` —

打印有关系统设备配置的信息

[概要](#__u6982___u8981_)
=======================

`devinfo` \[`-rv`\] `devinfo` `-u` `devinfo` `-p` dev \[`-v`\]

[描述](#__u63CF___u8FF0_)
=======================

`devinfo` 实用程序不带任何参数，显示系统中可用设备的层次结构，从 “nexus” 设备开始。

接受以下选项。

[`-r`](#r)

导致硬件资源信息（例如 IRQ、I/O 端口、I/O 内存地址）也被列在每个已保留这些资源的设备下。

[`-u`](#u)

显示与 `-r` 相同的信息，但按资源类型而非设备排序，允许按使用情况和可用资源查看系统资源集。 即，它将所有 IRQ 消费者一起列出。

[`-v`](#v)

显示驱动程序树中的所有设备，而不仅仅是那些已连接或忙碌的设备。 如果没有此标志，则仅报告那些已连接的设备。 此标志还显示有关每个设备的详细信息。

[`-p`](#p) dev

将 dev 的路径显示回设备树的根目录。

[参见](#__u53C2___u89C1_)
=======================

systat(1), devinfo(3), iostat(8), pciconf(8), pnpinfo(8), vmstat(8), devclass(9), device(9)

[作者](#__u4F5C___u8005_)
=======================

Mike Smith <[msmith@FreeBSD.org](mailto:msmith@FreeBSD.org)\>

December 21, 2017

FreeBSD 13.1-RELEASE