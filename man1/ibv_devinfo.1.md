  IBV\_DEVINFO(1)  

IBV\_DEVINFO(1)

USER COMMANDS

IBV\_DEVINFO(1)

[名称](#__u540D___u79F0_)
=======================

ibv\_devinfo - 查询 RDMA 设备

[概要](#__u6982___u8981_)
=======================

**ibv\_devinfo** \[-d device\] \[-i port\] \[-l\] \[-v\]

[描述](#__u63CF___u8FF0_)
=======================

打印有关可从用户空间使用的 RDMA 设备的信息。

[选项](#__u9009___u9879_)
=======================

**\-d**, **\--ib-dev**\=_DEVICE_

使用 IB 设备 _DEVICE_ (默认找到第一个设备)

**\-i**, **\--ib-port**\=_PORT_ 查询端口 _PORT_ (默认所有端口)

**\-l**, **\--list** 仅列出 RDMA 设备的名称

**\-v**, **\--verbose** 打印有关 RDMA 设备的所有可用信息

[参见](#__u53C2___u89C1_)
=======================

**ibv\_devices**(1)

[作者](#__u4F5C___u8005_)
=======================

Dotan Barak

<_dotanba@gmail.com_\>

Roland Dreier

<_rolandd@cisco.com_\>

August 30, 2005

libibverbs