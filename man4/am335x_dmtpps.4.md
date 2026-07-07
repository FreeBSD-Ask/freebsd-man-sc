# am335x_dmtpps(4)

`am335x_dmtpps` — AM335x 系统的 RFC 2783 每秒脉冲 API 驱动

## 名称

`am335x_dmtpps`

## 概要

`device am335x_dmtpps`

`可选地在 /boot/loader.conf 中设置：hw.am335x_dmtpps.input="引脚名称"`

## 描述

`am335x_dmtpps` 设备驱动提供一个系统时间计数器，能够精确捕获由 GPS 接收器及其他定时设备发出的每秒脉冲（PPS）信号。`am335x_dmtpps` 驱动可编译进内核，或以模块形式加载。

AM335x 定时器硬件会在 PPS 脉冲的上升沿捕获系统时间计数器的值。由于捕获由硬件完成，测量中不存在中断延迟。时间计数器以 24MHz 运行，提供 42 纳秒的测量分辨率。

要将此驱动提供的 PPS 定时信息用于 ntpd(8)，请将 `/dev/dmtpps` 设备符号链接到 `/dev/pps0`，并在 ntp.conf(5) 中配置 server `127.127.22.0`，以配置类型 22（ATOM）参考时钟。

## 驱动配置

AM335x 硬件提供四个带捕获输入引脚的定时器设备，即 DMTimer4 到 DMTimer7。由于它还提供活动系统时间计数器，因此同一时间只能有一个 `am335x_dmtpps` 驱动实例处于活动状态。该驱动使用系统引脚配置来确定使用哪个硬件定时器设备。在系统的 FDT 数据中配置定时器输入引脚，或通过 loader.conf(5) 中的可调变量提供引脚名称。

要使用标准内核和 FDT 数据，请使用 loader.conf(5) 加载 `am335x_dmtpps` 模块，并将 `hw.am335x_dmtpps.input` 可调变量设置为输入引脚的名称，可选值如下：

***名称*** *硬件*

**P8-7** DMTimer4；Beaglebone P8 排针第 7 脚。

**P8-8** DMTimer7；Beaglebone P8 排针第 8 脚。

**P8-9** DMTimer5；Beaglebone P8 排针第 9 脚。

**P8-10** DMTimer6；Beaglebone P8 排针第 10 脚。

**GPMC_ADVn_ALE** DMTimer4。

**GPMC_BEn0_CLE** DMTimer5。

**GPMC_WEn** DMTimer6。

**GPMC_OEn_REn** DMTimer7。

要使用 FDT 数据配置 `am335x_dmtpps` 驱动，请在你的 dts 文件中引用标准 `am33xx_pinmux` 驱动节点（定义于 am33xx.dtsi）来创建一个新的 pinctrl 节点。例如：

```sh
   &am33xx_pinmux {
      timer4_pins: timer4_pins {
         pinctrl-single,pins = <0x90 (PIN_INPUT | MUX_MODE2)>;
      };
   };
```

在你的 dts 文件中按如下方式引用 `timer4_pins`，将引用 `timer4_pins` 的 pinctrl 属性添加到标准 `timer4` 设备节点（同样定义于 am33xx.dtsi）：

```sh
   &timer4 {
      pinctrl-names = "default";
      pinctrl-0 = <&timer4_pins>;
   };
```

## 文件

**`/dev/dmtpps`** 提供 RFC 2783 API 的 ioctl(2) 访问设备。

## 参见

[timecounters(4)](timecounters.4.md), loader.conf(5), ntp.conf(5), ntpd(8)

## 历史

`am335x_dmtpps` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`am335x_dmtpps` 设备驱动及本手册页由 Ian Lepore <ian@FreeBSD.org> 编写。
