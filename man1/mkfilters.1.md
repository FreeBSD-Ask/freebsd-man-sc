  MKFILTERS(1)  

MKFILTERS(1)

FreeBSD General Commands Manual

MKFILTERS(1)

[名称](#__u540D___u79F0_)
=======================

mkfilters - 为 ipfilter 生成最小的防火墙规则集

[概要](#__u6982___u8981_)
=======================

**mkfilters**

[文件](#__u6587___u4EF6_)
=======================

/usr/share/examples/ipfilter/mkfilters

[描述](#__u63CF___u8FF0_)
=======================

**mkfilters** 是一个 perl 脚本，它通过解析 **ifconfig** 的输出来生成与 **ipfilter** 一起使用的最小过滤器规则集。

[参见](#__u53C2___u89C1_)
=======================

ipf(8), ipf(5), ipfilter(5), ifconfig(8)