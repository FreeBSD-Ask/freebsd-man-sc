# nvmf_che.4

`nvmf_che` — Chelsio NIC 上 NVM Express over Fabrics 的 TCP 传输

## 名称

`nvmf_che`

## 概要

`在 loader.conf(5) 中：`

```sh
nvmf_che_load="YES"
```

## 描述

`nvmf_che` 模块使用 Chelsio T7 适配器上的 PDU 卸载实现 NVM Express over Fabrics 的 TCP/IP 传输。它可由内核内 NVMeoF 主机驱动或控制器使用。要使用 PDU 卸载，初始套接字连接必须在受支持的网络接口上使用 TCP 卸载引擎（TOE）。此外，控制器连接必须协商合适的 `MAXH2CDATA` 限制，以确保接收到的 PDU 不超过适配器支持的最大大小。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`kern.nvmf.che.max_transmit_pdu`** 传输的 PDU 的最大大小，包括所有头部、负载和校验和。这是创建队列时强制执行的上限。各个适配器可能会施加更小的限制。默认大小为 32 千字节。

**`kern.nvmf.che.max_receive_pdu`** 同上，但用于接收的 PDU。

**`kern.nvmf.che.use_dsgl`** 在为 DDP 写入控制结构时启用 S/G 列表将大型写入写入适配器内存（不用于 PDU 负载数据）。S/G 列表默认启用。

**`kern.nvmf.che.inline_threshold`** 将控制结构写入适配器内存时使用 S/G 列表而非工作请求中放置的立即数据。默认阈值为 256 字节。

**`kern.nvmf.che.ddp_tags_per_qp`** 为每个队列对的 DDP 缓冲区保留的 STAG 数量。在队列上发送的每个请求远程对端数据的命令都可使用 DDP 将接收到的数据直接放入关联的数据缓冲区。每个缓冲区都需要一个 STAG 才能启用 DDP。如果发送请求远程数据的命令时没有可用的 STAG，数据将接收到空闲列表缓冲区中并由驱动复制到数据缓冲区。默认大小为 256 千字节。

## 参见

[cxgbe(4)](cxgbe.4.md), [nvmf(4)](nvmf.4.md), [nvmf_tcp(4)](nvmf_tcp.4.md), [nvmft(4)](nvmft.4.md)

## 历史

`nvmf_che` 模块首次出现于 FreeBSD 16.0。

## 作者

`nvmf_che` 模块由 John Baldwin <jhb@FreeBSD.org> 在 Chelsio Communications, Inc. 的赞助下开发。
