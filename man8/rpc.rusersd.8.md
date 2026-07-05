# rpc.rusersd.8

`rpc.rusersd` — 已登录用户服务器

## 名称

`rpc.rusersd`

## 概要

**/usr/libexec/rpc.rusersd**

## 描述

**/usr/libexec/rpc.rusersd** 工具是一个服务器，返回有关当前登录到系统的用户的信息。

当前登录的用户通过 rusers(1) 命令查询。**/usr/libexec/rpc.rusersd** 守护进程通常由 [inetd(8)](inetd.8.md) 调用。

**/usr/libexec/rpc.rusersd** 工具使用 **/usr/include/rpcsvc/rnusers.x** 中定义的 RPC 协议。

## 参见

rusers(1), [w(1)](../man1/w.1.md), [who(1)](../man1/who.1.md), [inetd(8)](inetd.8.md)
