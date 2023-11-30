  RPC.RUSERSD(8)  

RPC.RUSERSD(8)

FreeBSD System Manager's Manual

RPC.RUSERSD(8)

[名称](#__u540D___u79F0_)
=======================

`rpc.rusersd` —

登录用户服务器

[概要](#__u6982___u8981_)
=======================

`/usr/libexec/rpc.rusersd`

[描述](#__u63CF___u8FF0_)
=======================

`rpc.rusersd` 实用程序是一个服务器，它返回有关当前登录到系统的用户的信息。

使用 rusers(1) 命令查询当前登录的用户。 `rpc.rusersd` 守护进程通常由 inetd(8) 调用。

`rpc.rusersd` 实用程序使用 /usr/include/rpcsvc/rnusers.x 中定义的 RPC 协议。

[参见](#__u53C2___u89C1_)
=======================

rusers(1), w(1), who(1), inetd(8)

June 7, 1993

FreeBSD 13.1-RELEASE