# aacraid(4)

`aacraid` — Adaptec Series 6/7/8 6G 和 12G SAS+SATA RAID 控制器驱动

## 名称

`aacraid`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device pci
> device aacraid
> 要编译调试代码：
> options AACRAID_DEBUG=N

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
aacraid_load="YES"
```

## 描述

`aacraid` 驱动提供对 Adaptec by PMC RAID 控制器的支持，包括 Series 6/7/8 及后续系列。

RAID 容器通过 `aacraidp0` 总线处理。物理总线由 `aacraidp?` 设备表示（从 aacraidp1 开始）。这些设备启用 SCSI 直通接口，允许通过 CAM [scsi(4)](scsi.4.md) 子系统使用连接到卡上的设备（如 CD-ROM）。请注意，并非所有卡都允许启用此接口。

**`/dev/aacraid?`** 设备节点提供对控制器管理接口的访问。每块已安装的卡对应一个节点。如果加载了 `aacraid_linux.ko` 和 `linux.ko` 模块，将启用管理设备的 Linux 兼容 ioctl(2) 接口，并允许基于 Linux 的管理应用程序控制该卡。

## 硬件

`aacraidp?` 驱动支持以下 Adaptec 6G 和 12G SAS/SATA RAID 控制器：

- Adaptec ASR-6405(T|E)
- Adaptec ASR-6445
- Adaptec ASR-6805(T|E|Q|TQ)
- Adaptec ASR-7085
- Adaptec ASR-7805(Q)
- Adaptec ASR-70165
- Adaptec ASR-71605(E|Q)
- Adaptec ASR-71685
- Adaptec ASR-72405
- Adaptec Series 8 cards

## 文件

**`/dev/aacraid?`** aacraid 管理接口

## 诊断

在编译时将 `AACRAID_DEBUG` 设置为 0 到 3 之间的数字将启用逐步详细的调试消息。

适配器可异步向驱动发送状态和告警消息。这些消息会打印在系统控制台上，并排队等待管理应用程序检索。

## 参见

[kld(4)](kld.4.md), [linux(4)](linux.4.md), [scsi(4)](scsi.4.md), [kldload(8)](../man8/kldload.8.md)

## 作者

Achim Leubner <achim@FreeBSD.org> Ed Maste <emaste@FreeBSD.org> Scott Long <scottl@FreeBSD.org>

## 缺陷

在挂起/恢复时，控制器实际上并未暂停。
