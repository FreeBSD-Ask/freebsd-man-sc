# nvmft.4

`nvmft` — NVM Express over Fabrics CAM 目标层前端

## 名称

`nvmft`

## 概要

`要将此子系统编译进内核，请在内核配置文件中加入以下行：`

> device nvmft
> device ctl

`或者，要在引导时以模块方式加载该子系统，请在 loader.conf(5) 中加入以下行：`

```sh
nvmft_load="YES"
```

## 描述

`nvmft` 驱动提供 NVM Express over Fabrics 控制器的内核组件。NVMeoF 控制器是服务器，将由本地文件和卷支持的命名空间导出给远程主机。`nvmft` 遵循动态控制器模型，为每个关联创建新的动态控制器。

`nvmft` 作为 [ctl(4)](ctl.4.md) 前端实现，将 CAM 目标层 LUN 作为命名空间导出给远程主机。LUN 可通过 ctladm(8) 配置。

本地控制器与远程主机之间的关联通过 nvmfd(8) 守护进程和 ctladm(8) 工具共同管理。nvmfd(8) 守护进程监听新关联，并在将已连接的队列对移交给 `nvmft`（由 `nvmft` 将队列对与合适的控制器实例关联）之前处理传输特定的协商。`nvlist` ctladm(8) 命令列出活动控制器。`nvterminate` 命令终止本地控制器与远程主机之间的一个或多个关联。

关联需要受支持的传输，例如使用 TCP/IP 的关联使用 [nvmf_tcp(4)](nvmf_tcp.4.md)。

## 参见

[ctl(4)](ctl.4.md), [nvmf(4)](nvmf.4.md), [nvmf_tcp(4)](nvmf_tcp.4.md), ctladm(8), nvmfd(8)

## 历史

`nvmft` 模块首次出现于 FreeBSD 15.0。

## 作者

`nvmft` 子系统由 John Baldwin <jhb@FreeBSD.org> 在 Chelsio Communications, Inc. 的赞助下开发。
