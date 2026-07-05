# acpi_panasonic.4

`acpi_panasonic` — Panasonic 笔记本的 ACPI 热键驱动

## 名称

`acpi_panasonic`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device acpi_panasonic

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
acpi_panasonic_load="YES"
```

## 描述

`acpi_panasonic` 驱动启用各种 Panasonic 笔记本上的热键功能，如更改 LCD 亮度、控制混音器音量、进入睡眠或挂起状态等。据报告在以下型号上可正常工作：Let's note（在日本以外地区称为 Toughbook）CF-R1N、CF-R2A 和 CF-R3。也可能在其他型号上工作。

此驱动由三项功能组成。第一是检测热键事件并采取相应动作，包括更改 LCD 亮度和扬声器静音状态。第二是通过 [devctl(4)](devctl.4.md) 通知事件发生，并最终传递给 devd(8)。第三是提供通过 [sysctl(8)](../man8/sysctl.8.md) 调节 LCD 亮度和声音静音状态的方式。

### 热键

受支持的硬件上有 9 个热键：

****Fn+F1**** 使 LCD 背光变暗。
****Fn+F2**** 使 LCD 背光变亮。
****Fn+F3**** 在 LCD 和 CRT 之间切换视频输出。`acpi_panasonic` 驱动不支持。
****Fn+F4**** 切换扬声器静音状态。
****Fn+F5**** 调低混音器音量。
****Fn+F6**** 调高混音器音量。
****Fn+F7**** 进入挂起到内存状态。
****Fn+F9**** 显示电池状态。
****Fn+F10**** 进入挂起到磁盘状态。

对于 **Fn+F1、Fn+F2** 和 **Fn+F4**，驱动会自动采取相应动作。对于混音器控制和显示电池状态等其他事件，应由 devd(8) 按下文所述处理。

### devd(8) 事件

通知 devd(8) 时，热键事件提供以下信息：

**system** `ACPI`
**subsystem** `Panasonic`
**type** ACPI 命名空间中的事件来源。该值取决于具体型号，但通常为 `e_SB_.HKEY`。
**notify** 事件代码（见下文）。

生成的事件代码分配如下：

**0x81-0x86，** 0x89 **Fn+F<n>** 按下。0x81 对应 **Fn+F1，** 0x82 对应 **Fn+F2，** 依此类推。

**0x01-0x07，** 0x09, 0x1a **Fn+F<n>** 释放。0x01 对应 **Fn+F1，** 0x02 对应 **Fn+F2，** 依此类推。

## SYSCTL 变量

可用以下 MIB：

**`hw.acpi.panasonic.lcd_brightness_max`** 最大亮度级别。此只读值根据硬件型号自动设置。

**`hw.acpi.panasonic.lcd_brightness_min`** 最小亮度级别。此只读值根据硬件型号自动设置。

**`hw.acpi.panasonic.lcd_brightness`** LCD 当前亮度级别（可读写）。值范围从 `hw.acpi.panasonic.lcd_brightness_min` 到 `hw.acpi.panasonic.lcd_brightness_max`。

**`hw.acpi.panasonic.sound_mute`** 控制是否静音扬声器的可读写布尔标志。值为 1 表示静音，0 表示不静音。

## 参见

[acpi(4)](acpi.4.md), devd.conf(5), devd(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_panasonic` 驱动最早出现在 FreeBSD 5.3 中。

## 作者

`acpi_panasonic` 驱动及本手册页由 OGAWA Takaya <t-ogawa@triaez.kaisei.org> 和 TAKAHASHI Yoshihiro <nyan@FreeBSD.org> 编写。
