# iscsi.4

`iscsi` — iSCSI 发起端

## 名称

`iscsi`

## 概要

`要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device iscsi

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
iscsi_load="YES"
```

## 描述

`iscsi` 子系统提供 iSCSI 发起端的内核组件，负责实现 iSCSI 协议的 Full Feature Phase。发起端是 iSCSI 客户端，连接到 iSCSI 目标，提供对远程块设备的本地访问。用户态组件由 iscsid(8) 提供，内核和用户态均使用 iscsictl(8) 配置。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`kern.iscsi.debug`** `iscsi` 驱动日志消息的详细级别。设置为 0 可禁用日志，设置为 1 可对潜在问题发出警告。更大的值启用调试输出。默认为 1。

**`kern.iscsi.ping_timeout`** 等待目标响应 NOP-Out PDU 的秒数。如果在此时间内没有响应，会话将被强制重启。设置为 0 可禁用发送 NOP-Out PDU。默认为 5。

**`kern.iscsi.iscsid_timeout`** 等待 iscsid(8) 建立会话的秒数。超过此时间后 `iscsi` 将中止并重试。默认为 60。

**`kern.iscsi.login_timeout`** 等待登录尝试成功的秒数。超过此时间后 `iscsi` 将中止并重试。默认为 60。

**`kern.iscsi.maxtags`** 未完成 IO 请求的最大数量。默认为 255。

**`kern.iscsi.fail_on_disconnection`** 控制因网络问题导致 iSCSI 连接断开后的行为。设置为 1 时，连接断开会导致 iSCSI 设备节点被销毁。重新连接后将再次创建。默认情况下，设备节点保持不变。连接断开期间，所有输入/输出操作都将挂起，待连接重新建立后重试。

## 参见

[iser(4)](iser.4.md), iscsi.conf(5), iscsictl(8), iscsid(8)

## 历史

`iscsi` 子系统最早出现于 FreeBSD 10.0。

## 作者

`iscsi` 子系统由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。
