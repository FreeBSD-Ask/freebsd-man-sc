# ti_adc(4)

`ti_adc` — TI AM3XXX 模数转换器驱动程序

## 名称

`ti_adc`

## 概要

`device ti_adc`

## 描述

`ti_adc` 驱动提供对 am3xxx SoC 上 AIN（模拟输入）的访问。

它为每个模拟输入提供转换值的原始读数。

通过 [sysctl(8)](../man8/sysctl.8.md) 接口访问 `ti_adc` 数据：

```sh
dev.ti_adc.0.%desc: TI ADC controller
dev.ti_adc.0.%driver: ti_adc
dev.ti_adc.0.%pnpinfo: name=adc@44E0D000 compat=ti,adc
dev.ti_adc.0.%parent: simplebus0
dev.ti_adc.0.clockdiv: 2400
dev.ti_adc.0.ain.0.enable: 0
dev.ti_adc.0.ain.0.open_delay: 0
dev.ti_adc.0.ain.0.samples_avg: 0
dev.ti_adc.0.ain.0.input: 0
dev.ti_adc.0.ain.1.enable: 0
dev.ti_adc.0.ain.1.open_delay: 0
dev.ti_adc.0.ain.1.samples_avg: 0
dev.ti_adc.0.ain.1.input: 0
dev.ti_adc.0.ain.2.enable: 0
dev.ti_adc.0.ain.2.open_delay: 0
dev.ti_adc.0.ain.2.samples_avg: 0
dev.ti_adc.0.ain.2.input: 0
dev.ti_adc.0.ain.3.enable: 0
dev.ti_adc.0.ain.3.open_delay: 0
dev.ti_adc.0.ain.3.samples_avg: 0
dev.ti_adc.0.ain.3.input: 0
dev.ti_adc.0.ain.4.enable: 0
dev.ti_adc.0.ain.4.open_delay: 0
dev.ti_adc.0.ain.4.samples_avg: 0
dev.ti_adc.0.ain.4.input: 0
dev.ti_adc.0.ain.5.enable: 0
dev.ti_adc.0.ain.5.open_delay: 0
dev.ti_adc.0.ain.5.samples_avg: 0
dev.ti_adc.0.ain.5.input: 0
dev.ti_adc.0.ain.6.enable: 1
dev.ti_adc.0.ain.6.open_delay: 0
dev.ti_adc.0.ain.6.samples_avg: 4
dev.ti_adc.0.ain.6.input: 2308
dev.ti_adc.0.ain.7.enable: 1
dev.ti_adc.0.ain.7.open_delay: 0
dev.ti_adc.0.ain.7.samples_avg: 0
dev.ti_adc.0.ain.7.input: 3812
```

在 Beaglebone-black 上，模拟输入 7 通过电压分压器（2:1）连接到 3V3B 电源轨。3V3B 电压轨来自 TL5209 LDO 稳压器，最大限制为 500mA。

全局设置：

**`dev.ti_adc.0.clockdiv`** 设置 ADC 时钟预分频器。最小值为 10，最大值为 65535。ADC 时钟基于 CLK_M_OSC（24Mhz）/ clockdiv。这为 ADC 时钟提供了最大约 2.4Mhz，默认设置（clockdiv = 2400）约为 10Khz。

每个输入的设置：

**`dev.ti_adc.0.ain.%d.enable`** 启用该输入的转换。每个输入必须单独启用才能使用。当所有输入都被禁用时，ADC 被关闭。

**`dev.ti_adc.0.ain.%d.open_delay`** 设置应用输入配置后、开始 ADC 转换之前要等待的 ADC 时钟周期数。

**`dev.ti_adc.0.ain.%d.samples_avg`** 设置每个输入上使用的样本平均数，可设为 0（无样本平均）、2、4、8 或 16。

**`dev.ti_adc.0.ain.%d.input`** 是模拟输入上施加电压的转换原始值。它由 12 位值（0 ~ 4095）组成。

## 参见

[sysctl(8)](../man8/sysctl.8.md)

## 历史

`ti_adc` 驱动首次出现于 FreeBSD 10.1。

## 作者

该驱动和本手册页由 Luiz Otavio O Souza <loos@FreeBSD.org> 编写。
