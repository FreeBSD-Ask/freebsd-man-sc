# rtsx(4)

`rtsx` — Realtek SD 卡读卡器

## 名称

`rtsx`

## 概要

`要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device mmc
> device mmcsd
> device rtsx

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
mmc_load="YES"
mmcsd_load="YES"
rtsx_load="YES"
```

## 描述

`rtsx` 驱动为 Realtek SD 卡读卡器提供支持。驱动在卡插入时附加 mmc 总线，在卡移除时分离 mmc 总线。

## 硬件

`rtsx` 驱动支持以下 Realtek SD 卡读卡器：

- RTS5209
- RTS5227
- RTS5229
- RTS522A
- RTS525A
- RTS5260
- RTL8411B
- RTS5249（未验证）
- RTL8402（未验证）
- RTL8411（未验证）

## 参见

[mmc(4)](mmc.4.md), [mmcsd(4)](mmcsd.4.md)

> "SanDisk Secure Digital Card"。

## 历史

`rtsx` 驱动出现在 FreeBSD 13.0 中，从 OpenBSD 移植而来，并融合了 Linux 和 NetBSD 中的修改。

## 作者

Henri Hennebert <hlh@restart.be> Gary Jennejohn <gj@freebsd.org> Jesper Schmitz Mouridsen <jsm@FreeBSD.org>

## 贡献者

Lutz Bichler <Lutz.Bichler@gmail.com>

## 调试信息

*dev.rtsx.0.debug_mask* 可设置为以下掩码：

- 0x01 - 显示驱动的基本流程，
- 0x02 - 跟踪 SD 命令，
- 0x04 - 跟踪调优阶段。

## 缺陷

> `dev.rtsx.0.inversion=1`

> `dev.rtsx.0.inversion=0`

- 在 Lenovo T470p 上的 RTS522A，卡检测和只读开关是反的。此问题可通过在 *loader.conf(5)* 中添加解决：驱动会尝试自动处理这些异常。如果此自动化处理有误，可通过在 *loader.conf(5)* 中添加来规避：
- 在写保护的卡上以写访问方式挂载文件系统可能导致内核崩溃。
- 挂起/恢复在 MMCCAM 下不工作。
- 对于某些芯片（如 RTS5260），在 `devctl disable/enable` 或 `kldunload/kldload` 之后，驱动无法正确检测卡。
