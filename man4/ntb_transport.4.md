# ntb_transport(4)

`ntb_transport` — 面向非透明桥接的包传输

## 名称

`ntb_transport`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ntb
> device ntb_transport

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ntb_transport_load="YES"
```

`以下可调参数可在 loader(8) 中设置：`

`驱动调试级别。默认值为 0，数值越高输出越详细。`

`限制最大内存窗口使用量。分配大型物理连续内存缓冲区可能是个问题，而对于低延迟网络接口来说，过大的缓冲区意义不大。`

`配置一组以逗号分隔的传输消费者。每个消费者可配置为："[<name>][:<queues>]"，其中：name 是要附接的驱动名称（空表示任意），queues 是要分配的队列数量（空表示自动）。默认配置为空字符串，表示单一消费者，每个内存窗口一个队列，允许任意驱动附接。`

`非零值启用紧凑版 scratchpad 协议，使用的寄存器数量减半。如果没有足够的寄存器来协商所有可用内存窗口，则会自动启用。紧凑版不支持 4GB 及以上的内存窗口。`

**hw.ntb_transport.debug_level**

**hw.ntb_transport.max_mw_size**

**hint.ntb_transport.X.config**

**hint.ntb_transport.X.compact**

## 描述

`ntb_transport` 驱动在 `ntb` 驱动之上附接，利用其资源创建一组双向队列，在系统之间传递数据包。此驱动的主要用途是供 `if_ntb` 网络接口使用，但其他消费者也可使用 KPI 开发。

每个 `if_ntb` 需要底层 `ntb` 实例提供：

- 1 个或多个内存窗口；
- 6 个 scratchpad，每增加一个内存窗口再加 2 个，紧凑协议下为 3 个加 1 个；
- 每个内存窗口或配置的队列 1 个 doorbell。

## 参见

[if_ntb(4)](if_ntb.4.md), [ntb(4)](ntb.4.md), [ntb_hw_amd(4)](ntb_hw_amd.4.md), [ntb_hw_intel(4)](ntb_hw_intel.4.md), [ntb_hw_plx(4)](ntb_hw_plx.4.md)

## 作者

`ntb` 驱动由 Intel 开发，最初由 Carl Delsey <carl@FreeBSD.org> 编写。后续改进由 Conrad E. Meyer <cem@FreeBSD.org> 和 Alexander Motin <mav@FreeBSD.org> 完成。
