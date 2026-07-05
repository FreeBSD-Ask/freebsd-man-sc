# ida.4

`ida` — Compaq Intelligent Drive Array 控制器

## 名称

`ida`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device scbus
> device ida

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ida_load="YES"
```

## 描述

Compaq Intelligent Drive Array (IDA) 技术用于将数据分布到一组硬盘上。它将这些硬盘组合为一个或多个高性能逻辑驱动器。驱动器阵列由阵列控制器管理。

这些控制器能够为所连接的驱动器提供容错能力，并可选择为逻辑驱动器提供写缓存。应用程序也可以通过 pass-through 接口直接访问 SCSI 总线子系统。

## 硬件

`ida` 驱动支持以下控制器：

- Compaq SMART Array 221
- Compaq Integrated SMART Array Controller
- Compaq SMART Array 4200
- Compaq SMART Array 4250ES
- Compaq SMART 3200 Controller
- Compaq SMART 3100ES Controller
- Compaq SMART-2/DH Controller
- Compaq SMART-2/SL Controller
- Compaq SMART-2/P Controller

## 实现说明

使用 pass-through 接口时应格外谨慎。如果对活动设备使用 pass-through，可能会干扰正常的系统 I/O 并导致挂起。pass-through 仅应用于处于静止状态的设备。

## 参见

cam(4), [pass(4)](pass.4.md), [xpt(4)](xpt.4.md), [camcontrol(8)](../man8/camcontrol.8.md)

## 作者

`ida` 驱动由 Jonathan Lemon <jlemon@FreeBSD.org> 和 Matthew N. Dodd <mdodd@FreeBSD.org> 编写。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 编写。
