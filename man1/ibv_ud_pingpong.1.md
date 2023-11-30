  IBV\_UD\_PINGPONG(1)  

IBV\_UD\_PINGPONG(1)

USER COMMANDS

IBV\_UD\_PINGPONG(1)

[名称](#__u540D___u79F0_)
=======================

ibv\_ud\_pingpong - 简单的 InfiniBand UD 传输测试

[概要](#__u6982___u8981_)
=======================

**ibv\_ud\_pingpong** \[-p port\] \[-d device\] \[-i ib port\] \[-s size\] \[-r rx depth\] \[-n iters\] \[-l sl\] \[-e\] \[-g gid index\] **HOSTNAME**

**ibv\_ud\_pingpong** \[-p port\] \[-d device\] \[-i ib port\] \[-s size\] \[-r rx depth\] \[-n iters\] \[-l sl\] \[-e\] \[-g gid index\]

[描述](#__u63CF___u8FF0_)
=======================

通过不可靠数据报 (UD) 传输在 InfiniBand 上运行简单的 ping-pong 测试。

[选项](#__u9009___u9879_)
=======================

**\-p**, **\--port**\=_PORT_

使用 TCP 端口 _PORT_ 进行初始同步（默认 18515）

**\-d**, **\--ib-dev**\=_DEVICE_

使用 IB 设备 _DEVICE_ （默认找到第一个设备）

**\-i**, **\--ib-port**\=_PORT_

使用 IB 端口 _PORT_ （默认端口 1）

**\-s**, **\--size**\=_SIZE_

messages of 大小为 _SIZE_ ping-pong 的消息（默认 2048）

**\-r**, **\--rx-depth**\=_DEPTH_

post _DEPTH_ 一次接收（默认 500）

**\-n**, **\--iters**\=_ITERS_

执行 _ITERS_ 消息交换（默认 1000）

**\-l**, **\--sl**\=_SL_

发送具有服务级别 _SL_ 的消息（默认 0）

**\-e**, **\--events**

在等待工作完成事件时休眠（默认是轮询完成）

**\-g**, **\--gid-idx**\=_GIDINDEX_

本地端口 _GIDINDEX_

[参见](#__u53C2___u89C1_)
=======================

**ibv\_rc\_pingpong**(1), **ibv\_uc\_pingpong**(1), **ibv\_srq\_pingpong**(1), **ibv\_xsrq\_pingpong**(1)

[作者](#__u4F5C___u8005_)
=======================

Roland Dreier

<_rolandd@cisco.com_\>

[缺陷](#__u7F3A___u9677_)
=======================

客户端和服务器实例之间的网络同步很弱，并不能防止在两个实例上使用不兼容的选项。用于检索工作完成的方法并不严格正确，竞争条件可能会导致某些系统出现故障。

August 30, 2005

libibverbs