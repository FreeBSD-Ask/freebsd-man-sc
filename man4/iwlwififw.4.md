# iwlwififw.4

`iwlwififw` — Intel iwlwifi 无线网络驱动的固件

## 名称

`iwlwififw`

## 概要

`iwlwifi(4) 驱动应自动加载所需的任何固件。不建议从 loader(8) 手动加载驱动或固件。`

## 描述

[iwlwifi(4)](iwlwifi.4.md) 驱动支持的各种芯片组型号的固件文件可从 [ports(7)](../man7/ports.7.md) 获取。现代芯片组通常需要一个 `.ucode` 文件和配套的 `.pnvm` 文件。

可以使用 fwget(8) 安装正确的固件包。

下表作为参考，列出了在可确定范围内特定卡所需的文件前缀以及 port flavor。

| `Name` |
| --- |
| `Vendor` |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 3160 |
| 0x8086 |
|  |
| Intel(R) Wireless N 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 3160 |
| 0x8086 |
|  |
| Intel(R) Wireless N 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3160 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3168 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3168 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3168 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3168 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 3168 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 7265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless N 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 4165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 4165 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8260 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8275 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8275 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8275 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8275 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| Intel(R) Dual Band Wireless AC 8265 |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| (unknown) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550s Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550s Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550s Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550s Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer(R) Wireless-AC 1550s Wireless Network Adapter (9560D2W) 160MHz |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer(R) Wireless-AC 1550s Wireless Network Adapter (9560D2W) 160MHz |
| 0x8086 |
|  |
| Killer(R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690s 160MHz Wireless Network Adapter (411D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690i 160MHz Wireless Network Adapter (411NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690i 160MHz Wireless Network Adapter (411NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690s 160MHz Wireless Network Adapter (411D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690i 160MHz Wireless Network Adapter (411NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690s 160MHz Wireless Network Adapter (411D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690i 160MHz Wireless Network Adapter (411NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690s 160MHz Wireless Network Adapter (411D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690i 160MHz Wireless Network Adapter (411NGW) |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9260-1 |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690s 160MHz Wireless Network Adapter (411D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1690i 160MHz Wireless Network Adapter (411NGW) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX200 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650w 160MHz Wireless Network Adapter (200D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650x 160MHz Wireless Network Adapter (200NGW) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201D2W) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201D2W) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201D2W) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201D2W) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX210 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675w 160MHz Wireless Network Adapter (210D2W) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675x 160MHz Wireless Network Adapter (210NGW) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX411 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX411 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Killer(R) Wireless-AC 1550s Wireless Network Adapter (9560D2W) 160MHz |
| 0x8086 |
|  |
| Killer(R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) 160MHz |
| 0x8086 |
|  |
| Killer(R) Wireless-AC 1550s Wireless Network Adapter (9560D2W) 160MHz |
| 0x8086 |
|  |
| Killer(R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) 160MHz |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW) |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9270 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9270 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9162 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9162 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9260 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9260 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550s Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550s Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550s Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Killer (R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX101 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX203 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX101 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX203 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX101 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX203 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX231 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX203 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX101 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6 AX201 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX211 160MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 6E AX411 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9560 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 160MHz |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9461 |
| 0x8086 |
|  |
| Intel(R) Wireless-AC 9462 |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 7 BE201 320MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 7 BE200 320MHz |
| 0x8086 |
|  |
| Intel(R) Wi-Fi 7 BE202 160MHz |
| 0x8086 |
|  |
| Intel(R) TBD ’ |
| 0x8086 |
|  |
| Intel(R) TBD Sc2 device |
| 0x8086 |
|  |
| Intel(R) TBD Sc2f device |
| 0x8086 |

*注意：* 某些设备只能在运行时根据硬件寄存器（或上表中未复制的一些其他特殊魔法）正确确定。

## 文件

[iwlwifi(4)](iwlwifi.4.md) 固件许可的副本随 `wifi-firmware-iwlwifi-kmod` 包或 `ports/net/wifi-firmware-iwlwifi-kmod` port（或其各 flavor）一起安装。

## 参见

[iwlwifi(4)](iwlwifi.4.md), fwget(8), [firmware(9)](../man9/firmware.9.md)

## 历史

`iwlwififw` 固件模块最早出现于 FreeBSD 13.1，在 FreeBSD 14.3 之前被移除并由基于 [ports(7)](../man7/ports.7.md) 的固件包替代。
