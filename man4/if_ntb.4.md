# if_ntb(4)

`if_ntb` — 用于 Non-Transparent Bridges 的虚拟以太网接口

## 名称

`if_ntb`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device ntb
> device ntb_transport
> device if_ntb

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_ntb_load="YES"
```

`以下可调参数可在 loader(8) 中设置：`

`限制每个接口的最大队列数。默认为无限制。`

**hw.if_ntb.num_queues**

## 描述

`if_ntb` 驱动附着在 [ntb_transport(4)](ntb_transport.4.md) 驱动之上，利用其一个或多个数据包队列在系统之间创建虚拟以太网网络接口。该接口的典型 MTU 约为 64KB，以减少开销。接口的默认 MAC 地址为随机生成。

`if_ntb` 驱动未实现任何真正的硬件卸载，但由于 PCIe 链路由 CRC32 保护，在某些情况下，可通过在链路两端设置 `rxcsum` 和 `txcsum` 接口选项来启用伪校验和卸载，从而节省一些 CPU 周期。

## 参见

[ntb_transport(4)](ntb_transport.4.md)

## 作者

`if_ntb` 驱动由 Intel 开发，最初由 Carl Delsey <carl@FreeBSD.org> 编写。后续改进由 Conrad E. Meyer <cem@FreeBSD.org> 和 Alexander Motin <mav@FreeBSD.org> 完成。

## 缺陷

Linux 每个接口仅支持一个队列，因此可能需要手动配置以保持兼容性。
