# networking.7

`networking` — 连接到网络的快速入门指南

## 名称

`networking`, `wifi`

## 描述

在以下示例中，假设我们通过 [ix(4)](../man4/ix.4.md) 驱动程序找到的第一个接口连接以太网，并通过 [iwlwifi(4)](../man4/iwlwifi.4.md) 驱动程序找到的第一个接口连接 Wi-Fi，不过你的硬件会有所不同。

## 实例

```sh
# dhclient ix0
```

```sh
# dhclient ue0
```

```sh
% sysctl net.wlan.devices
```

```sh
# sysrc wlans_iwlwifi0="wlan0"
```

```sh
# sysrc ifconfig_wlan0="WPA SYNCDHCP"
```

```sh
# cd /etc/
# wpa_passphrase "myssid" "mypassphrase" >> wpa_supplicant.conf
```

```sh
# service netif restart
```

```sh
% ifconfig wlan0 scan
```

```sh
# service netif stop
```

**实例 1：使用 DHCP 连接到以太网** 在第一个 Intel 10Gb 以太网接口上请求 DHCP 租约：

**实例 2：通过 USB tethering 连接到蜂窝网络** 在第一个 USB tethering 接口上请求 DHCP 租约：

**实例 3：连接到 Wi-Fi 网络** 识别你的 Wi-Fi 硬件：使用第一个 Intel Wi-Fi 适配器创建 **wlan0** 接口：将该接口设置为通过 wpa_supplicant(8) 请求 DHCP 租约：输入 Wi-Fi 网络的详细信息：重启网络接口守护进程：

**实例 4：扫描 Wi-Fi 网络**

**实例 5：飞行模式**

## 参见

[bsdconfig(8)](../man8/bsdconfig.8.md), dhclient(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_passphrase(8)

FreeBSD Handbook 的 Advanced Networking 章节。

## 注意事项

`SSID` 或 `passphrase` 中的 shell 特殊字符需要为 wpa_passphrase(8) 进行转义，通常使用 `e`，详情请参阅你所使用 shell 的手册页。

停止网络接口服务也会停止内部网络。
