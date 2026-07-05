# ocs_fc.4

`ocs_fc` — Emulex 光纤通道主机适配器驱动

## 名称

`ocs_fc`

## 概要

`device ocs_fc`

`在 device.hints(5) 中：hint.ocs_fc.N.initiator hint.ocs_fc.N.target hint.ocs_fc.N.topology hint.ocs_fc.N.speed`

`在 loader.conf(5) 中：ocs_fc_load="YES"`

`在 loader.conf(5) 或 sysctl.conf(5) 中：dev.ocs_fc.N.port_state dev.ocs_fc.N.wwpn dev.ocs_fc.N.wwnn dev.ocs_fc.N.configured_speed dev.ocs_fc.N.configured_topology dev.ocs_fc.N.current_speed dev.ocs_fc.N.current_topology`

## 描述

`ocs_fc` 驱动提供对光纤通道 SCSI 设备的访问。

`ocs_fc` 驱动支持发起方（initiator）和目标方（target）模式。支持仲裁环路（Arbitrated Loop）、点对点（Point-to-Point）和 Fabric 连接。对于支持 FC-Tape 的磁带驱动器，强烈推荐使用 FC-Tape 连接。FC-Tape 包含 T-10 FCP-4 规范中的四个要素：

- 命令的精确传递（Precise Delivery of Commands）
- FCP I/O 操作的确认完成（Confirmed Completion of FCP I/O Operations）
- 未成功传输 IU 的重传（Retransmission of Unsuccessfully Transmitted IUs）
- 任务重试标识（Task Retry Identification）

这些特性合在一起，允许与磁带设备进行链路级错误恢复。如果没有链路级错误恢复，发起方无法判断某个已超时的磁带写入命令究竟将全部、部分还是完全没有数据写入磁带驱动器。当控制器和目标方都支持 FC-Tape 时，FC-Tape 将自动启用。

## 硬件

`ocs_fc` 驱动支持以下 PCIe 光纤通道适配器：

- LPe3500X FC Host Bus Adapter（Emulex 64/32G FC 第 7 代 HBA）
- LPe3200X FC Host Bus Adapter（Emulex 32/16G FC 第 6 代 HBA）
- LPe3100X FC Host Bus Adapter（Emulex 32/16G FC 第 6 代 HBA）
- LPe160XX FC Host Bus Adapter（Emulex 16/8G FC 第 5 代 HBA）
- LPe15004 FC Host Bus Adapter（Emulex 16/8G FC 第 5 代 HBA）

## 固件升级

适配器固件升级是持久化的。

可以通过以下步骤升级固件：

```sh
KMOD=ocsflash
FIRMWS=imagename.grp:ocsflash
.include <bsd.kmod.mk>
```

- 将以上代码复制到一个 `Makefile` 中：
- 将 `imagename` 替换为 GRP 文件的名称。
- 将 `Makefile` 和 GRP 文件复制到一个本地目录中
- 执行 `make`，并将生成的 `ocsflash.ko` 文件复制到 **/lib/modules**
- `sysctl dev.ocs_fc.<N>.fw_upgrade=ocsflash`
- 检查内核消息以了解操作状态
- 重启机器

## 引导选项

以下引导选项通过在 **/boot/device.hints** 中设置值来控制：

**`hint.ocs_fc.N.initiator`** 启用发起方功能。默认值为 1（启用），设为 0 则禁用。

**`hint.ocs_fc.N.target`** 启用目标方功能。默认值为 1（启用），设为 0 则禁用。

**`hint.ocs_fc.N.topology`** 拓扑：0 表示自动，1 表示仅 NPort，2 表示仅 Loop。

**`hint.ocs_fc.N.speed`** 链路速度，单位为兆比特每秒。可选值包括：0 自动速度协商（默认），4000（4GFC），8000（8GFC），16000（16GFC）。

## SYSCTL 选项

**`dev.ocs_fc.N.port_state`** 端口状态（可读/写）。有效值为 `online` 和 `offline`。

**`dev.ocs_fc.N.wwpn`** World Wide Port Name（可读/写）。

**`dev.ocs_fc.N.wwnn`** World Wide Node Name（可读/写）。

**`dev.ocs_fc.N.fwrev`** 固件版本（只读）。

**`dev.ocs_fc.N.sn`** 适配器序列号（只读）。

**`dev.ocs_fc.N.configured_speed`** 配置的端口速度（可读/写）。有效值为：0 自动速度协商（默认），4000（4GFC），8000（8GFC），16000（16GFC）。

**`dev.ocs_fc.N.configured_topology`** 配置的端口拓扑（可读/写）。有效值为：0 自动；1 NPort；2 Loop。

**`dev.ocs_fc.N.current_speed`** 当前端口速度（只读）。

**`dev.ocs_fc.N.current_topology`** 当前端口拓扑（只读）。

## 支持

如需一般信息和支持，请访问 Broadcom 网站：<http://www.broadcom.com/> 或发送电子邮件至 <ocs-driver-team.pdl@broadcom.com>。

## 参见

[ifconfig(8)](../man8/ifconfig.8.md)

## 作者

`ocs_fc` 驱动由 Broadcom 编写。
