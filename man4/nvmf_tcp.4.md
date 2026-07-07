# nvmf_tcp(4)

`nvmf_tcp` — NVM Express over Fabrics 的 TCP 传输

## 名称

`nvmf_tcp`

## 概要

`要将此模块编译进内核，请在内核配置文件中加入以下行：`

> device nvmf_tcp

`或者，要在引导时以模块方式加载，请在 loader.conf(5) 中加入以下行：`

```sh
nvmf_tcp_load="YES"
```

## 描述

`nvmf_tcp` 模块实现 NVM Express over Fabrics 的软件 TCP/IP 传输。它可由内核内 NVMeoF 主机驱动或控制器使用。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`kern.nvmf.tcp.max_transmit_data`** `C2H_DATA` 和 `H2C_DATA` PDU 的最大数据负载大小。远程控制器可通过 `MAXH2CDATA` 参数对 `H2C_DATA` PDU 的大小强制执行更低的限制。默认大小为 256 千字节。

## 参见

[nvmf(4)](nvmf.4.md), [nvmft(4)](nvmft.4.md)

## 历史

`nvmf_tcp` 模块首次出现于 FreeBSD 15.0。

## 作者

`nvmf_tcp` 模块由 John Baldwin <jhb@FreeBSD.org> 在 Chelsio Communications, Inc. 的赞助下开发。
