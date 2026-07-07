# acpi_hp(4)

`acpi_hp` — HP 笔记本的 ACPI 附加功能驱动

## 名称

`acpi_hp`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device acpi_hp

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
acpi_hp_load="YES"
```

## 描述

`acpi_hp` 驱动为使用启用 WMI 的 BIOS 的 HP 笔记本（例如 HP Compaq 8510p 和 6510p）上由 ACPI 控制的功能提供支持。

此驱动的主要目的是提供一个可通过 [sysctl(8)](../man8/sysctl.8.md)、devd(8) 和 devfs(8) 访问的接口，应用程序可通过该接口确定和更改各种笔记本组件及 BIOS 设置的状态。

### devd(8) 事件

devd(8) 收到的事件提供以下信息：

**system** `ACPI`
**subsystem** `HP`
**type** ACPI 命名空间中的事件来源。该值取决于具体型号。
**notify** 事件代码（见下文）。

事件代码：

**`0xc0`** WLAN on air 状态更改为 0（不在工作中）
**`0xc1`** WLAN on air 状态更改为 1（工作中）
**`0xd0`** Bluetooth on air 状态更改为 0（不在工作中）
**`0xd1`** Bluetooth on air 状态更改为 1（工作中）
**`0xe0`** WWAN on air 状态更改为 0（不在工作中）
**`0xe1`** WWAN on air 状态更改为 1（工作中）

### devfs(8) 设备

你可以读取 /dev/hpcmi 来查看当前 BIOS 设置。可以通过设置下文所述的 sysctl `cmi_detail` 来调整详细程度。

## SYSCTL 变量

当前实现了以下 sysctl：

### WLAN：

**`dev.acpi_hp.0.wlan_enabled`** 切换 WLAN 芯片活动状态。

**`dev.acpi_hp.0.wlan_radio`** （只读）WLAN 无线电状态（由硬件开关控制）

**`dev.acpi_hp.0.wlan_on_air`** （只读）WLAN 在工作中（芯片已启用、硬件开关已启用 + 在 BIOS 中已启用）

**`dev.acpi_hp.0.wlan_enabled_if_radio_on`** 若设为 1，则当无线电开启时将启用 WLAN 芯片

**`dev.acpi_hp.0.wlan_disable_if_radio_off`** 若设为 1，则当无线电关闭时将禁用 WLAN 芯片

### Bluetooth：

**`dev.acpi_hp.0.bt_enabled`** 切换 Bluetooth 芯片活动状态。

**`dev.acpi_hp.0.bt_radio`** （只读）Bluetooth 无线电状态（由硬件开关控制）

**`dev.acpi_hp.0.bt_on_air`** （只读）Bluetooth 在工作中（芯片已启用、硬件开关已启用 + 在 BIOS 中已启用）

**`dev.acpi_hp.0.bt_enabled_if_radio_on`** 若设为 1，则当无线电开启时将启用 Bluetooth 芯片

**`dev.acpi_hp.0.bt_disable_if_radio_off`** 若设为 1，则当无线电关闭时将禁用 Bluetooth 芯片

### WWAN：

**`dev.acpi_hp.0.wwan_enabled`** 切换 WWAN 芯片活动状态。

**`dev.acpi_hp.0.wwan_radio`** （只读）WWAN 无线电状态（由硬件开关控制）

**`dev.acpi_hp.0.wwan_on_air`** （只读）WWAN 在工作中（芯片已启用、硬件开关已启用 + 在 BIOS 中已启用）

**`dev.acpi_hp.0.wwan_enabled_if_radio_on`** 若设为 1，则当无线电开启时将启用 WWAN 芯片

**`dev.acpi_hp.0.wwan_disable_if_radio_off`** 若设为 1，则当无线电关闭时将禁用 WWAN 芯片

### 杂项：

**`0x01`** 显示 BIOS 设置的路径组件
**`0x02`** 显示 BIOS 设置的有效选项列表
**`0x04`** 显示 BIOS 设置的附加标志（ReadOnly 等）
**`0x08`** 查询最高 BIOS 条目实例。这在许多 HP 型号上有问题，因此默认禁用。

**`dev.acpi_hp.0.als_enabled`** 切换环境光传感器（ALS）

**`dev.acpi_hp.0.display`** （只读）显示状态（位掩码）

**`dev.acpi_hp.0.hdd_temperature`** （只读）硬盘温度

**`dev.acpi_hp.0.is_docked`** （只读）扩展坞状态（1 表示已插接）

**`dev.acpi_hp.0.cmi_detail`** 控制 /dev/hpcmi 输出详细程度的位掩码（值可按位 OR）。

**`dev.acpi_hp.0.verbose`** （只读）设置详细级别

这些 sysctl 的默认值可在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置。

## 硬件

据报告 `acpi_hp` 驱动支持以下硬件：

- HP Compaq 8510p
- HP Compaq nx7300

它应能在大多数启用 WMI BIOS 的 HP 笔记本上工作。

## 文件

**`/dev/hpcmi`** 用于读取 BIOS 设置的接口

## 实例

可将以下内容加入 devd.conf(5)，以便在 WLAN 工作时禁用 LAN 接口，并在其不工作时重新启用：

```sh
notify 0 {
	match "system"          "ACPI";
	match "subsystem"       "HP";
	match "notify"          "0xc0";
	action                  "ifconfig em0 up";
};
notify 0 {
	match "system"          "ACPI";
	match "subsystem"       "HP";
	match "notify"          "0xc1";
	action                  "ifconfig em0 down";
};
```

启用环境光传感器：

```sh
sysctl dev.acpi_hp.0.als_enabled=1
```

启用 Bluetooth：

```sh
sysctl dev.acpi_hp.0.bt_enabled=1
```

获取 BIOS 设置：

```sh
cat /dev/hpcmi
Serial Port                                Disable
Infrared Port                              Enable
Parallel Port                              Disable
Flash Media Reader                         Disable
USB Ports including Express Card slot      Enable
1394 Port                                  Enable
Cardbus Slot                               Disable
Express Card Slot                          Disable
(...)
```

为 /dev/hpcmi 输出设置最高详细级别：

```sh
sysctl dev.acpi_hp.0.cmi_detail=7
```

## 参见

[acpi(4)](acpi.4.md), [acpi_wmi(4)](acpi_wmi.4.md), [sysctl.conf(5)](../man5/sysctl.conf.5.md), devd(8), devfs(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_hp` 设备驱动最早出现在 FreeBSD 8.0 中。

## 作者

`acpi_hp` 驱动由 Michael Gmelin <freebsd@grem.de> 编写。

其灵感来自 hp-wmi 驱动，后者在 Linux 上实现了这些功能的一个子集（热键）。

**HP** CMI 白皮书：<https://h20331.www2.hp.com/Hpsub/downloads/cmi_whitepaper.pdf>

**wmi-hp** for Linux：<https://www.kernel.org>

**WMI** and ACPI：<http://www.microsoft.com/whdc/system/pnppwr/wmi/wmi-acpi.mspx>

本手册页由 Michael Gmelin <freebsd@grem.de> 编写。

## 缺陷

此驱动为实验性，仅在 i386 上一台具备所有受支持无线设备（WWAN/BT/WLAN）的 HP Compaq 8510p 上测试过。在不同硬件上运行可能产生未定义的结果。

加载此驱动较慢。从 **`/dev/hpcmi`** 读取更慢。

不支持 HP 专用传感器读数或写入 BIOS 设置等附加功能。
