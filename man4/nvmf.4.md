# nvmf(4)

`nvmf` — NVM Express over Fabrics 主机驱动

## 名称

`nvmf`

## 概要

`要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device nvmf

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nvmf_load="YES"
```

## 描述

`nvmf` 驱动提供 NVM Express over Fabrics 主机的内核组件。NVMeoF 主机是客户端，提供对远程控制器导出的命名空间的本地访问。

本地主机与远程控制器之间的关联通过 nvmecontrol(8) 管理。新关联通过 `connect` 命令创建，通过 `disconnect` 命令销毁。如果关联的连接中断，`reconnect` 命令会创建新关联以替换中断的关联。

与 [nvme(4)](nvme.4.md) 类似，`nvmf` 使用 `/dev/nvmeX` 格式创建控制器设备节点，使用 `/dev/nvmeXnsY` 格式创建命名空间设备节点。`nvmf` 还通过 CAM [nda(4)](nda.4.md) 外设驱动导出远程命名空间。与 [nvme(4)](nvme.4.md) 不同，`nvmf` 不支持 [nvd(4)](nvd.4.md) 磁盘驱动。

关联需要受支持的传输，例如使用 TCP/IP 的关联使用 [nvmf_tcp(4)](nvmf_tcp.4.md)。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`kern.nvmf.fail_on_disconnection`** 确定关联连接中断时的行为。默认情况下，主机断开连接时输入/输出操作会被挂起。这包括关联连接中断时挂起的操作以及主机断开连接时新提交的请求。建立新关联后，挂起的 I/O 请求会重试。设置为 1 时，主机断开连接时输入/输出操作会以 `EIO` 失败，[nda(4)](nda.4.md) 外设会在第一次 I/O 请求失败后销毁。注意，任何已销毁的 [nda(4)](nda.4.md) 外设会在建立新关联后重新创建。

## 参见

[nda(4)](nda.4.md), [nvme(4)](nvme.4.md), [nvmf_tcp(4)](nvmf_tcp.4.md), [nvmft(4)](nvmft.4.md), nvmecontrol(8)

## 历史

`nvmf` 模块首次出现于 FreeBSD 15.0。

## 作者

`nvmf` 驱动由 John Baldwin <jhb@FreeBSD.org> 在 Chelsio Communications, Inc. 的赞助下开发。
