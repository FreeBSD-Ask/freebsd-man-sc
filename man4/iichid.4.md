# iichid.4

`iichid` — I2C HID 传输驱动

## 名称

`iichid`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device iichid

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
iichid_load="YES"
```

## 描述

`iichid` 驱动为 I2C 人机接口设备（HID）提供接口。

## SYSCTL 变量

以下参数可作为 [sysctl(8)](../man8/sysctl.8.md) 变量使用。Debug 参数也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用。

**`dev.iichid.*.sampling_rate_fast`** 活动采样速率，单位为次/秒（用于采样模式）。

**`dev.iichid.*.sampling_rate_slow`** 空闲采样速率，单位为次/秒（用于采样模式）。

**`dev.iichid.*.sampling_hysteresis`** 启用慢速模式前缺失的样本数（用于采样模式）。

**`hw.iichid.debug`** 调试输出级别，0 为禁用调试，更大的值增加调试消息的详细程度。默认为 0。

## 参见

[ig4(4)](ig4.4.md)

## 缺陷

`iichid` 尚不支持 GPIO 中断。在这种情况下，`iichid` 通过驱动手段定期轮询硬件启用采样模式。参见 dev.iichid.*.sampling_* [sysctl(8)](../man8/sysctl.8.md) 变量以调整采样参数。

## 历史

`iichid` 驱动最早出现于 FreeBSD 13.0。

## 作者

`iichid` 驱动由 Marc Priggemeyer <marc.priggemeyer@gmail.com> 和 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。

本手册页由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
