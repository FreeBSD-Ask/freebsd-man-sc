# cdce.4

`cdce` — USB 通信设备类以太网（ECM/NCM）驱动

## 名称

`cdce`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device cdce

移动设备（例如华为 E3372、E5573 等）可能还需要 u3g 命令端口：

> device ucom
> device u3g

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_cdce_load="YES"
```

## 描述

`cdce` 驱动为基于 USB 通信设备类以太网控制模型（CDC ECM）和网络控制模型（CDC NCM）规范的 USB 主机到主机（又名 USB 到 USB）和 USB 到以太网桥接器提供支持。它还提供设备端 CDC ECM 支持。

USB 桥接器在两侧都呈现为常规网络接口，传输以太网帧。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

USB 1.x 桥接器支持高达 12Mbps 的速度，USB 2.0 高达 480Mbps。

数据包通过独立的 USB 批量传输端点接收和发送。

`cdce` 驱动不支持不同的媒体类型或选项。

## 硬件

`cdce` 驱动支持实现 USB 通信设备类以太网控制模型（CDC ECM）或网络控制模型（CDC NCM）协议的 USB 以太网接口，例如：

- Android USB 网络共享
- iPhone USB 网络共享
- Realtek RTL8153 USB 3.0 千兆以太网控制器
- Prolific PL-2501 主机到主机桥接控制器
- Sharp Zaurus PDA
- Terayon TJ-715 DOCSIS 电缆调制解调器
- 华为 3G/4G LTE（例如 E3372、E5573）和其他移动网络设备

## 实例

移动 `cdce` 网络设备在激活 NCM/ECM/ACM 网络接口之前，可能需要通过 [u3g(4)](u3g.4.md) 串行命令端口发送连接命令序列。例如：

```sh
echo 'AT^NDISUP=1,1,"internet"' > /dev/cuaU[0].0
```

其中“internet”是你的运营商 apn 名称。

## 诊断

- cdce%d: no union descriptor：驱动无法从 USB 设备获取接口描述符。对于手动添加的 USB 厂商/产品，可以尝试使用 CDCE_NO_UNION 标志来解决缺少描述符的问题。
- cdce%d: no data interface
- cdce%d: could not read endpoint descriptor
- cdce%d: unexpected endpoint
- cdce%d: could not find data bulk in/out：对于手动添加的 USB 厂商/产品，这些错误表明桥接器与驱动不兼容。
- cdce%d: watchdog timeout：数据包已排队等待传输且已发出传输命令，但设备在超时过期之前未能确认传输。
- cdce%d: no memory for rx list -- packet dropped!：通过 MGETHDR 或 MCLGET 进行的内存分配失败，系统 mbuf 不足。
- cdce%d: abort/close rx/tx pipe failed
- cdce%d: rx/tx list init failed
- cdce%d: open rx/tx pipe failed
- cdce%d: usb error on rx/tx

## 参见

arp(4), [cdceem(4)](cdceem.4.md), [intro(4)](intro.4.md), [ipheth(4)](ipheth.4.md), [netintro(4)](netintro.4.md), [u3g(4)](u3g.4.md), [ucom(4)](ucom.4.md), [urndis(4)](urndis.4.md), [usb(4)](usb.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "Universal Serial Bus Class Definitions for Communication Devices"。

> "Data sheet Prolific PL-2501 Host-to-Host Bridge/Network Controller"。

## 历史

`cdce` 设备驱动首次出现于 OpenBSD 3.6、NetBSD 3.0 和 FreeBSD 6.0。

## 作者

`cdce` 驱动由 Craig Boston <craig@tobuj.gank.org> 基于 Bill Paul <wpaul@windriver.com> 编写的 [aue(4)](aue.4.md) 驱动编写，并由 Daniel Hartmeier <dhartmei@openbsd.org> 移植到 OpenBSD。

## 注意事项

许多 USB 设备臭名昭著地无法正确报告其类和接口。手动将其厂商和产品 ID 添加到驱动后，未检测到的产品可能会完美工作。
