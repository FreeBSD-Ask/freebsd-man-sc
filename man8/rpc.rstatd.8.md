# rpc.rstatd(8)

`rpc.rstatd` — 内核统计服务器

## 名称

`rpc.rstatd`

## 概要

`/usr/libexec/rpc.rstatd`

## 描述

**`/usr/libexec/rpc.rstatd`** 工具是一个服务器，返回从内核获取的性能统计信息。这些统计信息使用 rup(1) 命令读取。`rpc.rstatd` 守护进程通常由 [inetd(8)](inetd.8.md) 调用。

`rpc.rstatd` 工具使用 **`/usr/include/rpcsvc/rstat.x`** 中定义的 RPC 协议。

## 参见

rup(1), [inetd(8)](inetd.8.md)
