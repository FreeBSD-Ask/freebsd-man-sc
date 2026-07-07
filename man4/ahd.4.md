# ahd(4)

`ahd` — Adaptec PCI/PCI-X Ultra320 SCSI 主机适配器驱动

## 名称

`ahd`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device pci
> device scbus
> device ahd
> 要编译调试代码：
> options AHD_DEBUG
> options AHD_DEBUG_OPTS=<选项的位掩码>
> options AHD_REG_PRETTY_PRINT

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ahd_load="YES"
```

## 描述

此驱动提供对连接到 Adaptec AIC79xx 主机适配器芯片的 SCSI 总线的访问。

驱动特性包括支持 narrow 和 wide 总线、fast、ultra、ultra2、ultra160 和 ultra320 同步传输、分组化传输、标记队列、512 个 SCB 以及目标模式。

`AHD_DEBUG_OPTS` 选项用于控制启用 `AHD_DEBUG` 时打印到控制台的诊断消息。将以下比特按逻辑 OR 组合：

*值	功能* 0x0001	显示杂项信息 0x0002	显示 sense 数据 0x0004	显示串行 EEPROM 内容 0x0008	显示总线终端设置 0x0010	显示主机内存使用情况 0x0020	显示 SCSI 协议消息 0x0040	显示芯片寄存器窗口的模式指针 0x0080	显示选择超时 0x0100	显示 FIFO 使用消息 0x0200	显示 Queue Full 状态 0x0400	显示 SCB 队列状态 0x0800	显示入站分组信息 0x1000	显示 S/G 列表信息 0x2000	在固件中启用额外诊断代码

`AHD_REG_PRETTY_PRINT` 选项编译进对调试代码打印的每个寄存器的人类可读位定义支持。但是，它也会使驱动编译后的大小增加约 215KB。

在引导时可访问的 SCSI-Select 菜单中执行的每目标配置由此驱动遵循。这包括同步/异步传输、最大同步协商速率、wide 传输、断开连接以及主机适配器的 SCSI ID。

## 配置选项

要将一个或多个控制器静态配置为承担目标角色：

`options AHD_TMODE_ENABLE <unit 的位掩码>`

> 分配给此选项的值应为需要目标模式的所有 unit 的位图。例如，
> 值 0x25 将在 unit 0、2 和 5 上启用目标模式。值 0x8a 为 unit 1、3 和 7 启用。
> 请注意，控制器可通过下文所述的 device hint 动态配置。

## 引导选项

以下选项可通过在 **`/boot/device.hints`** 中设置值来切换。

它们是：

**`hint.ahd.`** `N``.tmode_enable` 用于定义是否启用 SCSI 目标模式的 hint（0 -- 禁用，1 -- 启用）。

## 硬件

`ahd` 驱动支持以下 PCI/PCI-X 并行 SCSI 控制器：

- Adaptec AIC7901 host adapter chip
- Adaptec AIC7901A host adapter chip
- Adaptec AIC7902 host adapter chip
- Adaptec 29320 host adapter
- Adaptec 39320 host adapter
- 许多带板载 SCSI 支持的主板

## 参见

[ahc(4)](ahc.4.md), [cd(4)](cd.4.md), [da(4)](da.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md)

## 历史

`ahd` 驱动首次出现于 FreeBSD 4.7。

## 作者

`ahd` 驱动、AIC7xxx sequencer 代码汇编器以及运行在 aic79xx 芯片上的固件由 Justin T. Gibbs 编写。本手册页基于 [ahc(4)](ahc.4.md) 手册页编写。

## 缺陷

当前这一代 79xx 芯片在 Ultra320 模式下不支持目标模式。目标模式在此驱动中总体上未经充分测试。
