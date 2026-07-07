# asmc(4)

`asmc` — Apple 系统管理控制器（SMC）设备驱动

## 名称

`asmc`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device asmc

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
asmc_load="YES"
```

## 描述

`asmc` 驱动控制 Intel Apple 系统上的 Apple 系统管理控制器（简称 SMC）。

已知 SMC 存在于以下系统中：

- MacBook
- MacBook Pro
- Intel MacMini
- Mac Pro
- MacBook Air
- Intel iMac

使用此驱动，你可以配置键盘背光亮度、检查多个传感器的温度、检查内部风扇的转速以及检查突然运动传感器的状态。

与 SMC 控制和检查相关的变量通过 sysctl(3) 在设备树 `dev.asmc` 下导出。

## 键盘背光

在 MacBook Pro 系统上，你可以通过向 `dev.asmc.%d.light.control` sysctl MIB 写入值或使用 backlight(8) 工具来控制键盘亮度。

以下 sysctl MIB 包含左右光传感器返回的原始值：`dev.asmc.%d.light.left` 或 `dev.asmc.%d.light.right`。

## 温度

温度传感器的数量和描述因系统而异。你可以通过遍历 `dev.asmc.temp` sysctl MIB 来检查系统上的温度传感器。

所有值以摄氏度为单位。

## 系统风扇

`dev.asmc.fan.%d` sysctl 树包含叶节点 `speed`、`safespeed`、`minspeed`、`maxspeed` 和 `targetspeed`。这些叶节点分别表示当前风扇转速、最安全最低风扇转速、最低转速和最高转速。

所有值以 RPM 为单位。

## 电源管理

`dev.asmc.%d.auto_poweron` sysctl 控制机器在不正常断电后恢复交流供电时是否自动开机（SMC 键“AUPO”）。值为 1 启用自动开机；0 禁用。

## 原始 SMC 键访问

当内核使用 `ASMC_DEBUG` 选项编译时，在 `dev.asmc.%d.raw` 下提供了一组 sysctl 节点，用于按名称读写任意 SMC 键。

**`dev.asmc.%d.raw.key`** 设置要访问的 4 字符 SMC 键名（例如“AUPO )”。设置此项会自动查询键的长度和类型。

**`dev.asmc.%d.raw.value`** 以十六进制字符串形式读取或写入键的值。

**`dev.asmc.%d.raw.len`** 自动检测的值长度（字节，只读）。

**`dev.asmc.%d.raw.type`** 4 字符 SMC 类型字符串（例如“ui8”、“flt”）（只读）。

使用示例：

```sh
sysctl dev.asmc.0.raw.key=AUPO
sysctl dev.asmc.0.raw.value
sysctl dev.asmc.0.raw.value=01
```

## 突然运动传感器

突然运动传感器（简称 SMS）是一种检测笔记本电脑移动并通过中断通知操作系统的设备。`dev.asmc.sms` 下的 sysctl MIB 全部与 SMS 相关。

此设备最有趣的用途是在笔记本电脑受到剧烈移动时停放磁盘磁头。首先，你需要安装 ataidle(8)（`ports/sysutils/ataidle`），然后按以下方式配置 devd(8)：

```sh
notify 0 {
	match "system"		"ACPI";
	match "subsystem"	"asmc";
	action			"/usr/local/sbin/ataidle -s X Y";
};
```

不要忘记更改上面命令中的 `X` 和 `Y` 值。

此外，请注意停放磁盘磁头次数过多会显著缩短硬盘寿命。不要仅依赖 SMS 来保护硬盘：良好的保养和常识可以延长硬盘寿命。

## 文件

**`/dev/backlight/asmc0`** 键盘 backlight(8) 设备节点。

## 参见

ataidle(8)（`ports/sysutils/ataidle`）, backlight(8), devd(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`asmc` 驱动首次出现于 FreeBSD 8.0。

## 作者

Rui Paulo <rpaulo@FreeBSD.org>（Google Summer of Code 项目）

## 缺陷

对最新型号的支持从未经过测试，很可能无法完全工作。
