# acpi_fujitsu(4)

`acpi_fujitsu` — Fujitsu 笔记本附加功能

## 名称

`acpi_fujitsu`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device acpi_fujitsu

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
acpi_fujitsu_load="YES"
```

## 描述

`acpi_fujitsu` 驱动启用 Fujitsu 笔记本上由 ACPI 控制的按钮。按钮事件通过 devd(8) 发送到用户空间，并提供 [sysctl(8)](../man8/sysctl.8.md) 接口来模拟硬件事件。

使用此驱动可以控制显示器亮度、扬声器音量以及内部（指点杆）鼠标指针。

## SYSCTL 变量

当前实现了以下 sysctl：

**`hw.acpi.fujitsu.lcd_brightness`** 使 LCD 背光变亮或变暗。

**`hw.acpi.fujitsu.pointer_enable`** 启用或禁用内部鼠标指针。

**`hw.acpi.fujitsu.volume`** 控制扬声器音量。

**`hw.acpi.fujitsu.mute`** 静音扬声器。

这些 sysctl 的默认值可在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置。

## 实例

可将以下内容加入 devd.conf(5)，以便将按钮事件传递给 **`/usr/local/sbin/acpi_oem_exec.sh`** 脚本：

```sh
notify 10 {
        match "system"		"ACPI";
        match "subsystem"	"FUJITSU";
        action "/usr/local/sbin/acpi_oem_exec.sh $notify fujitsu";
};
```

一个可能的 **`/usr/local/sbin/acpi_oem_exec.sh`** 脚本可能如下所示：

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
MAX_VOLUME=16
OEM=$2
DISPLAY_PIPE=/tmp/acpi_${OEM}_display
case ${NOTIFY} in
        0x00)
                LEVEL=`sysctl -n hw.acpi.${OEM}.mute`
                if [ "$LEVEL" = "1" ]
                then
                        MESSAGE="volume muted"
                else
                        MESSAGE="volume unmuted"
                fi
                ;;
        0x01)
                LEVEL=`sysctl -n hw.acpi.${OEM}.pointer_enable`
                if [ "$LEVEL" = "1" ]
                then
                        MESSAGE="pointer enabled"
                else
                        MESSAGE="pointer disabled"
                fi
                ;;
        0x02)
                LEVEL=`sysctl -n hw.acpi.${OEM}.lcd_brightness`
                PERCENT=`${ECHO} "${BC_PRECOMMANDS} ; \
			 ${LEVEL} / ${MAX_LCD_BRIGHTNESS} * 100" |\
			 ${CALC} | ${CUT} -d . -f 1`
                MESSAGE="brightness level ${PERCENT}%"
                ;;
        0x03)
                LEVEL=`sysctl -n hw.acpi.${OEM}.volume`
                PERCENT=`${ECHO} "${BC_PRECOMMANDS} ; \
			${LEVEL} / ${MAX_VOLUME} * 100" | \
			 ${CALC} | ${CUT} -d . -f 1`
                MESSAGE="volume level ${PERCENT}%"
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

## 参见

[acpi(4)](acpi.4.md), [sysctl.conf(5)](../man5/sysctl.conf.5.md), devd(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_fujitsu` 驱动最早出现在 FreeBSD 5.4 中。

## 作者

`acpi_fujitsu` 驱动由 Sean Bullington <shegget@gmail.com>、Anish Mistry <mistry.7@osu.edu> 和 Marc Santcroos <marks@ripe.net> 编写。

本手册页由 Philip Paeps <philip@FreeBSD.org> 编写。
