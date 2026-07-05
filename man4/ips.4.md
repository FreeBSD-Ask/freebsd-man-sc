# ips.4

`ips` — IBM/Adaptec ServeRAID 控制器驱动

## 名称

`ips`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device pci
> device scbus
> device ips

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ips_load="YES"
```

## 描述

`ips` 驱动声称支持 IBM（现为 Adaptec）ServeRAID 系列 SCSI 控制器卡。

这些卡附带存储在固件中的内置配置实用程序，称为 ISPR。在卡初始 POST 期间使用 <*Ctrl+I*> 组合键访问此实用程序。

强烈建议在尝试诊断以下错误消息之前使用此实用程序配置卡。

在某些情况下，`ips` 驱动在系统初始化期间可能难以附加。为避免这些困难，将 `hw.ips.0.disable` 可调参数设为 1。它将阻止驱动附加。

## 硬件

`ips` 驱动支持的控制器包括：

- IBM ServeRAID 3H
- ServeRAID 4L/4M/4H
- ServeRAID Series 5
- ServeRAID 6i/6M
- ServeRAID 7t/7k/7M

较新的 ServeRAID 控制器由 [aac(4)](aac.4.md) 或 [mfi(4)](mfi.4.md) 驱动支持。

## 诊断

当卡初始化 IBM ISPR 实用程序时，可能会显示若干错误代码，这些代码与 FreeBSD 无关。

- ips%d: failed to get adapter configuration data from device
- ips%d: failed to get drive configuration data from device 无法获取适配器或驱动器配置。
- ips%d iobuf error 发生缓冲区输入/输出错误。[ENXIO]

### 一般适配器错误：

- Attaching bus failed 此消息未文档化。
- WARNING: command timeout. Adapter is in toaster mode, resetting 命令超时导致适配器被重置。
- AIEE! adapter reset failed, giving up and going home! Have a nice day 尝试重置适配器时发生错误。
- unable to get adapter configuration
- unable to get drive configuration 尝试获取配置信息时出错。
- Adapter error during initialization.
- adapter initialization failed 尝试初始化适配器时出错。
- adapter failed config check
- adapter clear failed 检查适配器时出错。
- device is disabled 适配器已禁用。
- resource allocation failed
- irq allocation failed
- irq setup failed 驱动无法为设备分配资源。

### DMA 相关错误消息：

- can't alloc command dma tag
- can't alloc SG dma tag
- can't alloc dma tag for statue queue
- dmamap failed 无法映射或分配 DMA 资源。

### 缓存、缓冲区和命令错误：

- failed to initialize command buffers
- no mem for command slots! 在这种情况下，`ips` 驱动将返回 [ENOMEM]。
- ERROR: unable to get a command! can't flush cache!
- ERROR: cache flush command failed!
- ERROR: unable to get a command! can't update nvram
- ERROR: nvram update command failed!
- ERROR: unable to get a command! can't sync cache!
- ERROR: cache sync command failed!
- ERROR: unable to get a command! can't sync cache!
- ERROR: etable command failed!

## 兼容性

与 FreeBSD 中的许多其他 SCSI 设备不同，`ips` 驱动不使用 cam(4) SCSI 子系统。

## 参见

[aac(4)](aac.4.md), [ch(4)](ch.4.md), [da(4)](da.4.md), [mfi(4)](mfi.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 作者

`ips` 驱动由 David Jefferys 和 Scott Long <scottl@FreeBSD.org> 编写。

本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 编写。
