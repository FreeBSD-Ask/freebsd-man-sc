  IBV\_ASYNCWATCH(1)  

IBV\_ASYNCWATCH(1)

USER COMMANDS

IBV\_ASYNCWATCH(1)

[名称](#__u540D___u79F0_)
=======================

ibv\_asyncwatch - 显示异步事件

[概要](#__u6982___u8981_)
=======================

**ibv\_asyncwatch** \[-d device\] \[-h\]

[描述](#__u63CF___u8FF0_)
=======================

显示转发到 RDMA 设备的用户空间的异步事件。

[选项](#__u9009___u9879_)
=======================

**\-d**, **\--ib-dev**\=_DEVICE_

使用 IB 设备 _DEVICE_ (默认找到第一个设备)

**\-h**, **\--help**\=_DEVICE_

打印帮助文本并退出。

[作者](#__u4F5C___u8005_)
=======================

Roland Dreier

<_rolandd@cisco.com_\>

Eran Ben Elisha

<_eranbe@mellanox.com_\>

August 30, 2005

libibverbs