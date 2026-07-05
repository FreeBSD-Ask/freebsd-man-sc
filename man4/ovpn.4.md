# ovpn.4

`ovpn` — OpenVPN DCO 驱动

## 名称

`ovpn`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ovpn

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_ovpn_load="YES"
```

## 描述

`ovpn` 设备驱动为 OpenVPN DCO 提供支持。DCO（Data Channel Offload，数据通道卸载）将 OpenVPN 数据路径移入内核，可以提升性能。

`ovpn` 接口由 OpenVPN 守护进程自动创建。除 OpenVPN 所做的配置外，无需其他配置。
