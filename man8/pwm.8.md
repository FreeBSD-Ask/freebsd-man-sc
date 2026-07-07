# pwm(8)

`pwm` — 配置 PWM（脉宽调制）硬件

## 名称

`pwm`

## 概要

`pwm [-f device] -C`
`pwm [-f device] [-D | -E] [-I] [-p period] [-d duty]`

## 描述

`pwm` 工具可用于配置 PWM 硬件。`pwm` 使用 [pwmc(4)](../man4/pwmc.4.md) 设备与硬件通信。某些 PWM 硬件在单个控制器块内支持多个输出通道；每个 [pwmc(4)](../man4/pwmc.4.md) 实例控制单个 PWM 通道。

[pwmc(4)](../man4/pwmc.4.md) 设备命名为 **/dev/pwm/pwmcX.Y**，其中 `X` 是控制器单元号，`Y` 是该单元内的通道号。

选项如下：

**`-f`** `device` 要操作的设备。未指定时使用 **/dev/pwm/pwmc0.0**。如果提供的是未限定的名称，则自动前缀 **/dev/pwm**。

**`-C`** 显示 PWM 通道的配置。

**`-D`** 禁用 PWM 通道。

**`-d`** `duty` 配置 PWM 通道的占空比（以纳秒或百分比为单位）。占空比是 `period` 期间信号有效的部分。

**`-E`** 启用 PWM 通道。

**`-p`** `period` 配置 PWM 通道的周期（以纳秒为单位）。

**`-I`** 反转 PWM 信号极性。

## 实例

- 显示 PWM 通道的配置：

```sh
pwm -f /dev/pwm/pwmc0.1 -C
```

- 配置 50000 纳秒的周期和 25000 纳秒的占空比，并启用该通道：

```sh
pwm -f pwmc1.1 -E -p 50000 -d 25000
```

- 在 [pwmc(4)](../man4/pwmc.4.md) 中配置为标签 `backlight` 的设备和通道上配置 50% 的占空比：

```sh
pwm -f backlight -d 50%
```

## 参见

pwm(9), [pwmbus(9)](../man9/pwmbus.9.md)

## 历史

`pwm` 工具出现于 FreeBSD 13.0。

## 作者

`pwm` 工具及本手册页由 Emmanuel Vadot <manu@FreeBSD.org> 编写。
