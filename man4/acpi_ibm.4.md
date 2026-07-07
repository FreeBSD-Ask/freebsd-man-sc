# acpi_ibm(4)

`acpi_ibm` — ThinkPad ACPI 附加功能驱动

## 名称

`acpi_ibm`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device acpi_ibm

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
acpi_ibm_load="YES"
```

## 描述

`acpi_ibm` 驱动提供对 ThinkPad 笔记本热键及其他组件的支持。此驱动的主要目的是提供一个可通过 [sysctl(8)](../man8/sysctl.8.md) 和 devd(8) 访问的接口，应用程序可通过该接口确定各笔记本组件的状态。

[sysctl(8)](../man8/sysctl.8.md) 接口在加载驱动后自动启用，而 devd(8) 接口必须显式启用，因为它可能改变某些按键的默认行为。这通过设置下文所述的 `events` sysctl 来完成。通过设置一个位掩码来指定哪些按键应生成事件，其中每个比特代表一个按键或按键组合。此位掩码可通过 `eventmask` sysctl 访问，默认设置为 `availmask`，该值代表特定 ThinkPad 型号上所有可能的按键事件。

### devd(8) 事件

devd(8) 收到的热键事件提供以下信息：

**system** “`ACPI`”

**subsystem** “`IBM`”

**type** 事件在 ACPI 命名空间中的来源。该值取决于型号。

**notify** 事件代码（见下文）。

根据 ThinkPad 型号的不同，事件代码可能有所差异。在 ThinkPad T41p 上如下：

**`0x01`** Fn + F1
**`0x02`** Fn + F2
**`0x03`** Fn + F3（LCD 背光）
**`0x04`** Fn + F4（挂起到内存）
**`0x05`** Fn + F5（蓝牙）
**`0x06`** Fn + F6
**`0x07`** Fn + F7（屏幕扩展）
**`0x08`** Fn + F8
**`0x09`** Fn + F9
**`0x0a`** Fn + F10
**`0x0b`** Fn + F11
**`0x0c`** Fn + F12（挂起到磁盘）
**`0x0d`** Fn + Backspace
**`0x0e`** Fn + Insert
**`0x0f`** Fn + Delete
**`0x10`** Fn + Home（提高亮度）
**`0x11`** Fn + End（降低亮度）
**`0x12`** Fn + PageUp（ThinkLight）
**`0x13`** Fn + PageDown
**`0x14`** Fn + Space（缩放）
**`0x15`** 音量增大
**`0x16`** 音量减小
**`0x17`** 静音
**`0x18`** Access IBM 按钮
**`0x1b`** 麦克风静音按钮

### led(4) 接口

`acpi_ibm` 驱动为 ThinkLight 提供了 [led(4)](led.4.md) 接口。通过向 **`/dev/led/thinklight`** 设备写入 ASCII 字符串可使 ThinkLight 闪烁。

## SYSCTL 变量

目前实现了以下 sysctl：

**`1`** Fn + F1
**`2`** Fn + F2
**`4`** Fn + F3（LCD 背光）
**`8`** Fn + F4（挂起到内存）
**`16`** Fn + F5（蓝牙）
**`32`** Fn + F6
**`64`** Fn + F7（屏幕扩展）
**`128`** Fn + F8
**`256`** Fn + F9
**`512`** Fn + F10
**`1024`** Fn + F11
**`2048`** Fn + F12（挂起到磁盘）
**`4096`** Fn + Backspace
**`8192`** Fn + Insert
**`16384`** Fn + Delete
**`32768`** Fn + Home（提高亮度）
**`65536`** Fn + End（降低亮度）
**`131072`** Fn + PageUp（ThinkLight）
**`262144`** Fn + PageDown
**`524288`** Fn + Space（缩放）
**`1048576`** 音量增大
**`2097152`** 音量减小
**`4194304`** 静音
**`8388608`** Access IBM 按钮
**`67108864`** 麦克风静音

**`1`** Home 按钮
**`2`** Search 按钮
**`4`** Mail 按钮
**`8`** Access IBM 按钮
**`16`** 缩放
**`32`** 无线网络按钮
**`64`** 视频按钮
**`128`** 休眠按钮
**`256`** ThinkLight 按钮
**`512`** 屏幕扩展
**`1024`** 亮度增减按钮
**`2048`** 音量增减/静音按钮

**`0`** 关闭
**`1, 2`** 约 3000 RPM
**`3, 4, 5`** 约 3600 RPM
**`6, 7`** 约 4300 RPM
**`8`** 约 6400 RPM（全速，不限流）

- CPU
- Mini PCI 模块
- HDD
- GPU
- 内置电池
- UltraBay 电池
- 内置电池
- UltraBay 电池

**`dev.acpi_ibm.0.initialmask`** （只读）加载 `acpi_ibm` 驱动之前的 ACPI 事件位掩码。

**`dev.acpi_ibm.0.availmask`** （只读）所有受支持的 ACPI 事件的位掩码。

**`dev.acpi_ibm.0.events`** 启用 ACPI 事件并将 `eventmask` 设置为 `availmask`。未加载 `acpi_ibm` 驱动时，仅 Fn+F4 按钮生成 ACPI 事件。

**`dev.acpi_ibm.0.eventmask`** 设置报告给 devd(8) 的 ACPI 事件。Fn+F3、Fn+F4 和 Fn+F12 始终生成 ACPI 事件，无论 `eventmask` 为何值。根据 ThinkPad 型号的不同，`eventmask` 中各比特的含义可能有所差异。在 ThinkPad T41p 上，这是以下值的按位 OR：

**`dev.acpi_ibm.0.hotkey`** （只读）若干按钮的状态。每次按下按钮时，相应比特会翻转。它是以下值的按位 OR：

**`dev.acpi_ibm.0.lcd_brightness`** 显示当前的亮度级别。

**`dev.acpi_ibm.0.volume`** 扬声器音量。

**`dev.acpi_ibm.0.mute`** 指示扬声器是否静音。

**`dev.acpi_ibm.0.mic_led`** 指示麦克风静音指示灯（某些型号具备）是否点亮。请注意，这并不意味着麦克风输入已静音。

**`dev.acpi_ibm.0.thinklight`** 指示 ThinkLight 键盘灯是否已激活。

**`dev.acpi_ibm.0.bluetooth`** 切换蓝牙芯片活动状态。

**`dev.acpi_ibm.0.wlan`** （只读）指示 WLAN 芯片是否处于活动状态。

**`dev.acpi_ibm.0.fan`** 指示风扇处于自动（1）还是手动（0）模式。默认为自动模式。使用此 sysctl 应格外谨慎，因为禁用自动风扇控制可能导致 ThinkPad 过热，若未相应设置 `fan_level`，可能导致永久性损坏。

**`dev.acpi_ibm.0.fan_level`** 指示在手动模式下风扇应以何种速度运行。有效值范围为 0（关闭）到 7（最大）以及 8。驱动使用级别 8 将风扇设置为不限流模式。在此模式下，风扇自由旋转并会迅速达到很高的速度。仅在绝对必要时使用此模式，例如系统已达到临界温度且即将关机时。由此产生的速度因型号而异。在 T41p 上如下：

**`dev.acpi_ibm.0.fan_speed`** （只读）风扇转速（每分钟转数）。少数较旧的 ThinkPad 以 0（关闭）到 7（最大）的级别报告风扇转速。

**`dev.acpi_ibm.0.thermal`** （只读）显示最多八个不同温度传感器的读数。大多数 ThinkPad 包含六个或更多温度传感器，但仅通过 [acpi_thermal(4)](acpi_thermal.4.md) 公开 CPU 温度。某些 ThinkPad 具有以下传感器布局，该布局可能因具体型号而异：

**`dev.acpi_ibm.0.handlerevents`** 当 `events` 设置为 1 时由 `acpi_ibm` 处理的 devd(8) 事件。事件以空白分隔的十六进制或十进制形式事件代码列表指定。请注意，如果 ACPI BIOS 已处理该事件，则事件可能被处理两次（例如亮度增减）。

这些 sysctl 的默认值可在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置。

## 文件

**`/dev/led/thinklight`** ThinkLight [led(4)](led.4.md) 设备节点

## 实例

可将以下内容添加到 devd.conf(5) 中，以将按钮事件传递给 **`/usr/local/sbin/acpi_oem_exec.sh`** 脚本：

```sh
notify 10 {
        match "system"          "ACPI";
        match "subsystem"       "IBM";
        action "/usr/local/sbin/acpi_oem_exec.sh $notify ibm";
};
```

一个可能的 **`/usr/local/sbin/acpi_oem_exec.sh`** 脚本如下：

```sh
#!/bin/sh
#
if [ "$1" = "" -o "$2" = "" ]
then
        echo "usage: $0 notify oem_name"
        exit 1
fi
NOTIFY=`echo $1`
LOGGER="logger"
CALC="bc"
BC_PRECOMMANDS="scale=2"
ECHO="echo"
CUT="cut"
MAX_LCD_BRIGHTNESS=7
MAX_VOLUME=14
OEM=$2
DISPLAY_PIPE=/tmp/acpi_${OEM}_display
case ${NOTIFY} in
        0x05)
                LEVEL=`sysctl -n dev.acpi_${OEM}.0.bluetooth`
                if [ "$LEVEL" = "1" ]
                then
                        sysctl dev.acpi_${OEM}.0.bluetooth=0
                        MESSAGE="bluetooth disabled"
                else
                        sysctl dev.acpi_${OEM}.0.bluetooth=1
                        MESSAGE="bluetooth enabled"
                fi
                ;;
        0x10|0x11)
                LEVEL=`sysctl -n dev.acpi_${OEM}.0.lcd_brightness`
                PERCENT=`${ECHO} "${BC_PRECOMMANDS} ; \
                         ${LEVEL} / ${MAX_LCD_BRIGHTNESS} * 100" |\
                         ${CALC} | ${CUT} -d . -f 1`
                MESSAGE="brightness level ${PERCENT}%"
                ;;
        0x12)
                LEVEL=`sysctl -n dev.acpi_${OEM}.0.thinklight`
                if [ "$LEVEL" = "1" ]
                then
                        MESSAGE="thinklight enabled"
                else
                        MESSAGE="thinklight disabled"
                fi
                ;;
        0x15|0x16)
                LEVEL=`sysctl -n dev.acpi_${OEM}.0.volume`
                PERCENT=`${ECHO} "${BC_PRECOMMANDS} ; \
                        ${LEVEL} / ${MAX_VOLUME} * 100" | \
                         ${CALC} | ${CUT} -d . -f 1`
                MESSAGE="volume level ${PERCENT}%"
                ;;
        0x17)
                LEVEL=`sysctl -n dev.acpi_${OEM}.0.mute`
                if [ "$LEVEL" = "1" ]
                then
                        MESSAGE="volume muted"
                else
                        MESSAGE="volume unmuted"
                fi
                ;;
	0x1b)
		LEVEL=`sysctl -n dev.acpi_ibm.0.mic_led`
		if [ $LEVEL -eq 0 ]; then
			sysctl dev.acpi_ibm.0.mic_led=1
			mixer rec.volume=0
		fi
		if [ $LEVEL -eq 1 ]; then
			sysctl dev.acpi_ibm.0.mic_led=0
			mixer rec.volume=30%
		fi
		;;
        *)
                ;;
esac
${LOGGER} ${MESSAGE}
if [ -p ${DISPLAY_PIPE} ]
then
        ${ECHO} ${MESSAGE} >> ${DISPLAY_PIPE} &
fi
exit 0
```

以下示例指定事件代码 0x04（挂起到内存）、0x10（提高亮度）和 0x11（降低亮度）由 `acpi_ibm` 处理。

```sh
sysctl dev.acpi_ibm.0.handlerevents='0x04 0x10 0x11'
```

在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中：

```sh
dev.acpi_ibm.0.handlerevents=0x04 0x10 0x11
```

## 参见

[acpi(4)](acpi.4.md), [led(4)](led.4.md), [sysctl.conf(5)](../man5/sysctl.conf.5.md), devd(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_ibm` 设备驱动首次出现于 FreeBSD 6.0。

## 作者

`acpi_ibm` 驱动由 Takanori Watanabe <takawata@FreeBSD.org> 编写，后由 Markus Brueffer <markus@FreeBSD.org> 大部分重写。本手册页由 Christian Brueffer <brueffer@FreeBSD.org> 和 Markus Brueffer <markus@FreeBSD.org> 编写。
