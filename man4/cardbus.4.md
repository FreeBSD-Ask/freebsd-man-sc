# cardbus(4)

`cardbus` — CardBus 总线驱动

## 名称

`cardbus`

## 概要

`device cardbus`

## 描述

`cardbus` 驱动实现了 CardBus 总线。`cardbus` 驱动支持系统中的所有 CardBus 桥。

## 可调参数

该驱动支持以下可调参数，可添加到 **/boot/loader.conf** 或通过 [sysctl(8)](../man8/sysctl.8.md) 命令设置：

**`hw.cardbus.debug`** 非零值会在插入或移除 32 位 CardBus 卡时打印更详细的信息。

**`hw.cardbus.cis_debug`** 非零值会使 32 位 CardBus 卡的 CIS 解析输出更加详细，并包含完整的 CIS 转储。

## 参见

[pccbb(4)](pccbb.4.md)
