# iser(4)

`iser` — iSCSI Extensions for RDMA (iSER) 驱动

## 名称

`iser`

## 概要

`要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device iser

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
iser_load="YES"
```

## 描述

`iser`（iSCSI Extensions for RDMA）发起端驱动将 iSCSI 协议扩展到 RDMA。它允许数据直接传输到和从 SCSI 缓冲区，无需中间数据复制。iSER 使用 RDMA 协议套件为块存储传输提供更高带宽（零复制行为）。因此，它消除了 TCP/IP 处理开销，同时保持与 iSCSI 协议的兼容性。发起端是 iSCSI/iSER 客户端，连接到 iSCSI/iSER 目标，提供对远程块设备的本地访问。用户态组件由 iscsid(8) 提供，内核和用户态均使用 iscsictl(8) 配置。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`kern.iser.debug`** `iser` 驱动日志消息的详细级别。设置为 0 可禁用日志，设置为 1 可对潜在问题发出警告。更大的值启用信息和调试输出。默认为 0。

## 参见

[iscsi(4)](iscsi.4.md), iscsi.conf(5), iscsictl(8), iscsid(8)

## 历史

`iser` 子系统最早出现于 FreeBSD 11.0。

## 作者

`iser` 子系统由 Max Gurtovoy <maxg@mellanox.com> 和 Sagi Grimberg <sagig@mellanox.com> 在 Mellanox Technologies 赞助下开发。
