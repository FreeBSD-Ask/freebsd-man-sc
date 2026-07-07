# coretemp(4)

`coretemp` — Intel Core 片上数字温度传感器设备驱动

## 名称

`coretemp`

## 概要

要将此驱动编译进内核，请在你的内核配置文件中加入以下行：

> device coretemp

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
coretemp_load="YES"
```

## 描述

`coretemp` 驱动为 Intel Core 及更新 CPU 中存在的片上数字温度传感器提供支持。

`coretemp` 驱动通过相应 CPU 设备 sysctl 树中名为 `dev.cpu.%d.temperature` 的 sysctl 节点报告每个核心的温度。

## 参见

[amdtemp(4)](amdtemp.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`coretemp` 驱动首次出现于 FreeBSD 7.0。

## 作者

`coretemp` 驱动由 Rui Paulo <rpaulo@FreeBSD.org> 作为 Google Summer of Code 项目的一部分编写。本手册页由 Dag-Erling Sm(/orgrav <des@FreeBSD.org> 编写。
