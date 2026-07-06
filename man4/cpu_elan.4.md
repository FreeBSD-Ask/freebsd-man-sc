# CPU\_ELAN.4

`CPU_ELAN` — AMD Elan 520 CPU 支持

## 名称

`CPU_ELAN`

## 概要

`options CPU_ELAN`

`options CPU_ELAN_PPS`

`options CPU_ELAN_XTAL`

- `machdep.elan_gpio_config`
- `machdep.elan_freq`

`options CPU_SOEKRIS`

## 描述

`options CPU_ELAN` 启用对 AMD Elan 520 CPU 的支持。

设备 **/dev/elan-mmcr** 使用 mmap(2) 将 MMCR 寄存器组导出到用户空间。

`i8254` 定时器将被调整到 Elan 采用的略非标准的频率 1189161 Hz（`32768 * 45 * 25 / 31`）。

名为 `ELAN` 的时间计数器使用通用定时器 2 实现，但除非 `HZ` 配置为 150 或更高，否则它将不可用。此时间计数器远优于 `i8254` 时间计数器，应始终使用。

`machdep.elan_gpio_config` [sysctl(8)](../man8/sysctl.8.md) 变量允许配置 CPU 的 GPIO 引脚。该字符串必须正好 32 个字符长。`-` 表示 GPIO 不可用。`l`（小写字母 l）配置一个 [led(4)](led.4.md) 设备（低电平有效）。`L` 配置一个 [led(4)](led.4.md) 设备（高电平有效）。`.` 表示此 GPIO 无配置。这些 [led(4)](led.4.md) 设备将被命名为 **/dev/led/gpio%d**。关于 `P`、`e` 和 `E` 的含义，参见下文 `options CPU_ELAN_PPS` 部分。

`options CPU_ELAN_XTAL` 和 `machdep.elan_freq` [sysctl(8)](../man8/sysctl.8.md) 变量可用于设置 CPU 时钟晶振频率，单位为 Hz。默认值为 33333333 Hz。

`options CPU_ELAN_PPS` 启用精确时间戳功能，通过 **/dev/elan-mmcr** 设备使用 RFC2783 PPS-API 实现。分辨率约为 125 纳秒，精度 ± 125 纳秒。（125 纳秒即"4 / CPU 时钟晶振频率"。）

输入信号必须连接到 TMR1IN 引脚和一个 GPIO 引脚。该 GPIO 引脚必须在 `machdep.elan_gpio_config` 中配置为 `P`。

此外，一个 GPIO 引脚可以配置为 `e`（低电平有效）或 `E`（高电平有效），成为输入信号的"回显"输出。请注意此信号不适合用于校准。

如果指定了 `options CPU_SOEKRIS`，支持还将针对 Soekris Engineering 45xx 系列嵌入式计算机进行定制。"error"指示灯将被配置（作为 **/dev/led/error**），不可用的 GPIO 引脚将被禁用。

## 参见

[led(4)](led.4.md), [timecounters(4)](timecounters.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`CPU_ELAN` 代码首次出现于 FreeBSD 4.7。

## 作者

Poul-Henning Kamp <phk@FreeBSD.org>
