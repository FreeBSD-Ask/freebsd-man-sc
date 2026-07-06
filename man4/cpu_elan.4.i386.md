# CPU_ELAN.4.i386

`CPU_ELAN` — AMD Elan 520 CPU 支持

## 名称

`CPU_ELAN`

## 概要

`options CPU_ELAN options CPU_ELAN_PPS options CPU_ELAN_XTAL`

`machdep.elan_gpio_config`

`machdep.elan_freq`

`options CPU_SOEKRIS`

## 描述

`options CPU_ELAN` 启用对 AMD Elan 520 CPU 的支持。

设备 **`/dev/elan-mmcr`** 通过 mmap(2) 将 MMCR 寄存器组导出到用户态。

i8254 定时器将被调整为 Elan 所采用的略不寻常的频率 1189161 Hz（32768 *45* 25 / 31）。

名为“`ELAN`”的 timecounter 使用通用定时器 2 实现，但除非 HZ 配置为 150 或更高，否则它将不可用。该 timecounter 远优于“`i8254`”timecounter，应始终使用。

`machdep.elan_gpio_config` [sysctl(8)](../man8/sysctl.8.md) 变量允许配置 CPU 的 GPIO 引脚。该字符串长度必须恰好为 32 个字符。`-` 表示该 GPIO 不可用。`l`（小写字母 L）配置一个 [led(4)](led.4.md) 设备（低电平有效）。`L` 配置一个 [led(4)](led.4.md) 设备（高电平有效）。`.` 表示不对该 GPIO 进行配置。这些 [led(4)](led.4.md) 设备将被命名为 **`/dev/led/gpio%d`**。关于 `P`、`e` 和 `E` 的含义，参见下文 `options CPU_ELAN_PPS` 部分。

`options CPU_ELAN_XTAL` 和 `machdep.elan_freq` [sysctl(8)](../man8/sysctl.8.md) 变量可用于设置 CPU 时钟晶振频率（单位为 Hz）。默认值为 33333333 Hz。

`options CPU_ELAN_PPS` 启用通过 **`/dev/elan-mmcr`** 设备使用 RFC2783 PPS-API 进行精确时间戳标记。分辨率约为 125 nsec，精度为 ±125 nsec。（对于 125 nsec，即“4 / CPU 时钟晶振频率”。）

输入信号必须连接到 TMR1IN 引脚和一个 GPIO 引脚。该 GPIO 引脚必须在 `machdep.elan_gpio_config` 中以 `P` 配置。

此外，可以用 `e`（低电平有效）或 `E`（高电平有效）配置一个 GPIO 引脚，使其成为输入信号的“回显”输出。请注意，该信号不适合用于校准。

如果指定了 `options CPU_SOEKRIS`，该支持还将针对 Soekris Engineering 45xx 系列嵌入式计算机进行定制。“error”指示灯将被配置（作为 **`/dev/led/error`**），并且不可用的 GPIO 引脚将被禁用。

## 参见

[led(4)](led.4.md), [timecounters(4)](timecounters.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`CPU_ELAN` 代码首次出现于 FreeBSD 4.7。

## 作者

Poul-Henning Kamp <phk@FreeBSD.org>
