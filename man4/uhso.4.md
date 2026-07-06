# uhso.4

`uhso` — 支持 Option N.V. 的若干 HSxPA 设备

## 名称

`uhso`

## 概要

`通过在 loader.conf(5) 中加入以下行，可在引导时加载此模块：`

```sh
uhso_load="YES"
```

## 描述

`uhso` 驱动为 Option N.V. 基于其分组接口的若干 HSxPA 设备提供支持。每个设备都有一组串口和一个原始 IP 分组接口。设备的串口通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md) 设备。分组接口以网络接口形式呈现。

在分组接口上建立连接是通过在任一可用串口上使用专有 AT 命令“`AT_OWANCALL`”和“`AT_OWANDATA`”来实现的。

必须使用从这些调用获取的数据手动配置网络接口。

每个设备通常至少有两个或更多串口，其各自用途可通过 [sysctl(8)](../man8/sysctl.8.md) 标识。标识为“Modem”的端口具有正常的调制解调器接口，可与 PPP 一起使用。标识为“Diagnostic”的端口使用专有二进制接口，用于固件升级，此端口没有 AT 命令接口，无法用于控制设备。其他端口具有 AT 命令接口，可用于正常设备控制。

## 硬件

`uhso` 驱动应能与 Option 的大多数设备配合工作。以下设备已经过验证可正常工作：

- Option GlobeSurfer iCON 7.2（新固件）
- Option GlobeTrotter Max 7.2（新固件）
- Option iCON 225
- Option iCON 452
- Option iCON 505

该设备具有一个称为“Zero-CD”的大容量存储设备，其中包含 Microsoft Windows 的驱动程序；这是设备的默认模式。`uhso` 驱动会自动将设备从“Zero-CD”模式切换到调制解调器模式。可通过 [sysctl(8)](../man8/sysctl.8.md) 将 `hw.usb.uhso.auto_switch` 设置为 0 来禁用此行为。

## 文件

**`/dev/cuaU?.?`**

## 实例

使用某个串口上可用的 AT 命令接口建立分组接口连接：

```sh
AT+CGDCONT=1,,"apn.provider"
AT_OWANCALL=1,1,1
OK
_OWANCALL=1,1
AT_OWANDATA=1
_OWANDATA: 1, 10.11.12.13, 0.0.0.0, 10.2.3.4, 10.2.3.5, e
	0.0.0.0, 0.0.0.0, 72000
```

配置接口：

```sh
ifconfig uhso0 10.11.12.13 up
route add default -interface uhso0
echo "nameserver 10.2.3.4" > /etc/resolv.conf
echo "nameserver 10.2.3.5" >> /etc/resolv.conf
```

可通过以下命令终止连接：

```sh
AT_OWANCALL=1,0,1
```

## 参见

uhsoctl(1), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 作者

`uhso` 驱动由 Fredrik Lindberg <fli@shapeshifter.se> 编写。
