# nmdm(4)

`nmdm` — nullmodem 终端驱动

## 名称

`nmdm`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device nmdm

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nmdm_load="YES"
```

## 描述

`nmdm` 驱动提供两个由虚拟“空调制解调器（null modem）”线缆连接的 [tty(4)](tty.4.md) 设备。

如果两个 tty 设备中任一在其线路规程中设置了 `CDSR_OFLOW` 位（“`stty dsrflow`”），`nmdm` 设备将仿真 [termios(4)](termios.4.md) 设置中配置的速度。速度仿真在两个方向上独立工作，由较慢一端的 termios 设置控制（`c_ispeed`、`c_ospeed`、`CS5 ... CS8`、`CSTOPB` 和 `PARENB`）。

## 文件

**`/dev/nmdm`** `N`[`AB`] nullmodem 设备节点。其中 `A` 节点有对应的 `B` 节点。

`nmdm` 驱动实现“按需创建设备”，因此只需访问 `/dev` 中的给定实例即可创建它。

## 诊断

无。

## 参见

stty(1), [termios(4)](termios.4.md), [tty(4)](tty.4.md), ttys(5)

## 历史

`nmdm` 驱动首次出现于 FreeBSD 4.4。
