# oce.4

`oce` — Emulex OneConnect 10Gb 网络适配器设备驱动

## 名称

`oce`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device pci
> device oce

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_oce_load="YES"
```

## 描述

Emulex OneConnect 适配器有各种型号，具有不同的 NIC、FCoE 和 iSCSI 功能组合。`oce` 驱动声明所有这些适配器中的 NIC 功能。

`oce` 驱动支持 VLAN 硬件卸载、TCP 校验和卸载、TCP 分段卸载（TSO）、大接收卸载（LRO）、Bonding、巨帧（从 1500 到 9000）、多 TX 队列、接收端缩放（RSS）和 MSI-X 中断。

## 硬件

`oce` 驱动支持以下网络适配器：

- Emulex BladeEngine 2
- Emulex BladeEngine 3
- Emulex Lancer

## 固件更新

适配器固件更新是持久性的。

可按以下步骤更新固件：

```sh
KMOD=elxflash
FIRMWS=imagename.ufi:elxflash
.include <bsd.kmod.mk>
```

- 将以下代码复制到 Makefile：
- 将上面的 imagename 替换为 UFI 文件名
- 将 Makefile 和 UFI 文件复制到某个目录
- 执行 make 并将生成的 elxflash.ko 复制到 `/lib/modules`
- sysctl dev.oce.<if_id>.fw_upgrade=elxflash
- 重启机器

如果提供的 UFI 有问题，刷写会失败并出现以下错误之一。

- "Invalid BE3 firmware image"
- "Invalid Cookie. Firmware image corrupted ?"
- "cmd to write to flash rom failed."

## 支持

有关一般信息和支持，请访问 Emulex 网站：`http://www.Emulex.com/` 或发送电子邮件至 `freebsd-drivers@emulex.com`。

## 参见

[ifconfig(8)](../man8/ifconfig.8.md)

## 作者

`oce` 驱动由 <freebsd-drivers@emulex.com> 编写。
