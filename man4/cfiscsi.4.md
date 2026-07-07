# cfiscsi(4)

`cfiscsi` — CAM 目标层 iSCSI target 前端

## 名称

`cfiscsi`

## 概要

要将此驱动编译进内核，请在你的内核配置文件中加入以下行：

> device cfiscsi
> device ctl
> device iscsi

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
cfiscsi_load="YES"
```

## 描述

`cfiscsi` 子系统提供 iSCSI target 的内核组件。target 即 iSCSI 服务器，向远程发起方提供由本地文件和卷支持的 LUN。用户态组件由 ctld(8) 提供。`cfiscsi` 作为 [ctl(4)](ctl.4.md) 前端实现，并使用 [iscsi(4)](iscsi.4.md) 提供的基础设施。

## sysctl 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`kern.cam.ctl.iscsi.debug`** iSCSI target 内核部分日志消息的详细级别。设为 0 可禁用日志，设为 1 可对潜在问题发出警告。更大的值可启用调试输出。默认值为 1。

**`kern.cam.ctl.iscsi.maxtags`** 向每个 iSCSI 发起方通告的未完成命令数。当前实现不够精确，因此不要将其设置为 2 以下。默认值为 256。

**`kern.cam.ctl.iscsi.ping_timeout`** 等待 iSCSI 发起方响应 NOP-In PDU 的秒数。如果在该时间内没有响应，会话将被强制终止。设为 0 可禁用发送 NOP-In PDU。默认值为 5。

## 参见

[ctl(4)](ctl.4.md), [iscsi(4)](iscsi.4.md), ctl.conf(5), ctld(8)

## 历史

`cfiscsi` 子系统首次出现于 FreeBSD 10.0，作为 [ctl(4)](ctl.4.md) 驱动的一部分。在 FreeBSD 12.0 中从 [ctl(4)](ctl.4.md) 中分离出来。

## 作者

`cfiscsi` 子系统由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。本手册页由 Enji Cooper <ngie@FreeBSD.org> 编写。
