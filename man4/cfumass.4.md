# cfumass(4)

`cfumass` — USB 大容量存储类传输的设备端支持

## 名称

`cfumass`

## 概要

通过将以下行放入内核配置文件中，可将此驱动编译进内核：

> device usb
> device usb_template
> device ctl
> device cfumass

也可以通过在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行来在引导时加载驱动模块：

```sh
cfumass_load="YES"
```

## 描述

`cfumass` 驱动提供设备端支持，用于模拟符合 USB 大容量存储类 Bulk-Only（BBB）传输规范的 USB 大容量存储设备，作为 [ctl(4)](ctl.4.md) 前端驱动实现。

要使用 `cfumass`：

- `cfumass` 必须作为模块加载或编译进内核。
- 必须通过将 `hw.usb.template` sysctl 设置为 0 来选择 USB 大容量存储模板。
- USB OTG 端口必须在 USB 设备端模式下工作。这会在连接到 USB 主机时自动发生。
- 必须为 `cfumass` 端口配置 [ctl(4)](ctl.4.md) LUN。

加载时，驱动创建一个名为 `cfumass` 的 [ctl(4)](ctl.4.md) 端口，向 USB 主机呈现为该端口映射的第一个 LUN（通常为 LUN 0）。有关配置 LUN 的详细信息，请参见 ctl.conf(5) 和 ctld(8)。有关在引导时自动配置的自动化方式，请参见 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cfumass_enable` 和 `cfumass_dir` [rc(8)](../man8/rc.8.md) 变量。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.cfumass.debug`** `cfumass` 驱动日志消息的详细级别。设置为 0 禁用日志记录，设置为 1 警告潜在问题。较大的值启用调试输出。默认为 1。

**`hw.usb.cfumass.ignore_stop`** 忽略 START 和 LOEJ 位清零的 START STOP UNIT SCSI 命令。某些发起方在用户尝试优雅弹出驱动器时发送该命令以停止目标，但在驱动器重新连接时未能启动它。设置为 0 以符合标准的方式处理命令，1 表示忽略它并记录警告，2 表示静默忽略。默认为 1。

**`hw.usb.cfumass.max_lun`** 向发起方（USB 主机）报告的最大 LUN 号。必须在 0 到 15 之间。某些发起方错误处理大于 0 的值。默认为 0。

## 参见

[ctl(4)](ctl.4.md), [umass(4)](umass.4.md), [usb(4)](usb.4.md), [usb_template(4)](usb_template.4.md), ctl.conf(5), ctld(8)

## 历史

`cfumass` 驱动首次出现于 FreeBSD 11.1。

## 作者

`cfumass` 驱动由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。
