# me.4

`me` — 封装网络设备

## 名称

`me`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device me

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_me_load="YES"
```

## 描述

`me` 网络接口是一种点对点伪设备，将数据报封装到 IP 中。这些封装的数据报被路由到目标主机，在那里被解封装并进一步路由到最终目的地。

`me` 接口通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `create` 和 `destroy` 子命令动态创建和销毁。

此驱动对应 RFC 2004。数据报以更短的封装形式封装到 IP 中。原始 IP 头被修改，修改内容被插入到如此修改后的头和原始有效载荷之间。外部头使用协议号 55。

## 注释

为正确运行，`me` 设备需要一条不经过隧道的到解封装主机的路由，否则会形成环路。

## 参见

[gif(4)](gif.4.md), [gre(4)](gre.4.md), [inet(4)](inet.4.md), [ip(4)](ip.4.md), [netintro(4)](netintro.4.md), [protocols(5)](../man5/protocols.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 作者

Andrey V. Elsukov <ae@FreeBSD.org>
