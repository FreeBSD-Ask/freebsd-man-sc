# bcm283x\_pwm.4

`bcm283x_pwm` — Raspberry Pi 2/3 PWM 驱动

## 名称

`bcm283x_pwm`

## 概要

`kldload bcm283x_clkman kldload bcm283x_pwm`

## 描述

`bcm283x_pwm` 驱动提供对 Raspberry Pi 2 和 3 硬件上 GPIO12 的 PWM 引擎的访问。

PWM 硬件通过 [sysctl(8)](../man8/sysctl.8.md) 接口控制：

```sh
dev.pwm.0.mode: 1
dev.pwm.0.mode2: 1
dev.pwm.0.freq: 125000000
dev.pwm.0.ratio: 2500
dev.pwm.0.ratio2: 2500
dev.pwm.0.period: 10000
dev.pwm.0.period2: 10000
dev.pwm.0.pwm_freq: 12500
dev.pwm.0.pwm_freq2: 12500
```

**`dev.pwm.0.mode , dev.pwm.0.mode2`** 通道 1 和 2 的 PWM 模式。存在三种模式：0=关闭，1=PWM，2=N/M。N/M 模式是一阶 delta-sigma 模式，配合简单的 RC 低通滤波器即可成为非常方便的 DAC 输出。

**`dev.pwm.0.freq`** PWM 硬件的输入频率（单位为 Hz）。同时适用于通道 1 和 2。最低频率为 123 kHz，最高频率为 125 MHz。

**`dev.pwm.0.period , dev.pwm.0.period2`** 周期长度（单位为周期数）。在 PWM 模式下，输出频率为（`dev.pwm.0.freq` / `dev.pwm.period`）和（`dev.pwm.0.freq2` / `dev.pwm.0.period2`）。在 N/M 模式下，此值为 'M'。

**`dev.pwm.0.ratio , dev.pwm.0.ratio2`** PWM 通道 1 和 2 的“开启”周期（单位为周期数）。在 PWM 模式下，要获得 25% 的占空比，请将此值设置为 `dev.pwm.0.period` 或 `dev.pwm.0.period2` 的 25%（视情况而定）。在 N/M 模式下，此值为 'N'。

**`dev.pwm.0.pwm_freq , dev.pwm.0.pwm_freq2`** PWM 模式下通道 1 和 2 计算得出的 PWM 输出频率。

## 注释

目前 `bcm283x_pwm` 驱动会忽略 DTB 中的 'status="disabled"' 标志，假定如果加载了驱动，就希望它工作。

## 参见

[sysctl(8)](../man8/sysctl.8.md)

## 历史

`bcm283x_pwm` 驱动首次出现于 FreeBSD 12.0。

## 作者

`bcm283x_pwm` 驱动及本手册页由 Poul-Henning Kamp <phk@FreeBSD.org> 编写。
