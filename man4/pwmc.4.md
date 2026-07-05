# pwmc.4

`pwmc` — PWM（脉宽调制）控制设备驱动程序

## 名称

`pwmc`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device pwmbus
> device pwmc

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
pwmc_load="YES"
```

## 描述

`pwmc` 驱动程序为 PWM 硬件的一个通道提供设备控制访问。每个 `pwmc` 设备实例都与单个 PWM 输出通道关联。

某些 PWM 硬件以多通道共享公共时钟或其他资源的方式组织。在这种情况下，每个通道会存在一个独立的 `pwmc` 实例，但更改任一通道的周期或占空比可能会影响共享相同资源的硬件中的其他通道。有关共享资源的通道的详细信息，请参阅底层 PWM 硬件设备驱动程序的文档。

`pwmc` 的一个实例会创建一个名为 **`/dev/pwm/pwmcX.Y`** 的字符设备，其中 `X` 是系统发现每个 PWM 硬件控制器时分配的顺序号，`Y` 是该硬件控制器内的通道号。可以将驱动程序配置为创建指向 `pwmcX.Y` 条目的别名，从而创建命名通道。

`pwmc` 驱动程序通过以下 ioctl(2) 调用和数据结构提供对 PWM 通道的控制，定义于：

`#include <dev/pwm/pwmc.h>`

**`PWMGETSTATE`** (`struct pwm_state`) 检索通道的当前状态。

**`PWMSETSTATE`** (`struct pwm_state`) 设置通道的当前状态。每次调用都会更新所有参数。若仅更改其中某个值，可使用 `PWMGETSTATE` 获取当前状态，然后仅修改相应值后重新提交。

`pwm_state` 结构定义如下：

```sh
struct pwm_state {
	u_int		period;
	u_int		duty;
	uint32_t	flags;
	bool		enable;
};
```

**`PWM_POLARITY_INVERTED`** 反转信号极性。

**`period`** 一个完整开关周期的持续时间，以纳秒为单位。

**`duty`** 一个周期中开通部分的持续时间，以纳秒为单位。

**`flags`** 影响输出信号的标志可按位或组合。当前定义了以下标志：

**`enable`** 为 false 时禁用输出信号，为 true 时启用。

## HINTS 配置

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统（例如 `MIPS`）上，可以为 `pwmc` 配置以下值：

**`hint.pwmc.%d.at`** `pwmc` 实例所附加到的 pwmbus 实例。

**`hint.pwmc.%d.channel`** 实例所附加到的硬件通道号。通道号从零开始计数。

**`hint.pwmc.%d.label`** 若设置了此可选 hint，驱动程序将在 **`/dev/pwm`** 中以给定名创建指向该实例的别名。

## FDT 配置

在基于 [fdt(4)](fdt.4.md) 的系统上，`pwmc` 设备通过 pwm 硬件控制器节点的一个子节点描述。当硬件在控制器内支持多个通道时，无需为硬件支持的每个通道都包含一个 `pwmc` 子节点。仅定义你需要控制的通道。

`pwmc` 设备节点需要以下属性：

**`compatible`** 必须为字符串 "freebsd,pwmc"。

**`reg`** 硬件通道号。

`pwmc` 设备节点的以下属性是可选的：

**`label`** 仅包含文件名合法字符的字符串。驱动程序在 **`/dev/pwm`** 中以给定名创建一个别名，指向该实例的 **`/dev/pwm/pwmcX.Y`** 设备条目。

包含一个 `pwmc` 子节点的 PWM 硬件节点示例：

```sh
&ehrpwm0 {
    status = "okay";
    pinctrl-names = "default";
    pinctrl-0 = <&ehrpwm0_AB_pins>;
    pwmcontrol@0 {
        compatible = "freebsd,pwmc";
        reg = <0>;
        label = "backlight";
    };
};
```

## 文件

**`/dev/pwm/pwmc*`**

## 参见

[fdt(4)](fdt.4.md), [device.hints(5)](../man5/device.hints.5.md), [pwm(8)](../man8/pwm.8.md), pwm(9)

## 历史

`pwmc` 驱动程序出现于 FreeBSD 13.0。
