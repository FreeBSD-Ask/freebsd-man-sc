# ctl.4

`ctl` — CAM 目标层

## 名称

`ctl`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device ctl

`或者，若要在引导时以模块方式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ctl_load="YES"
```

## 描述

`ctl` 子系统提供 SCSI 目标设备模拟。它支持以下特性：

- 磁盘、CD-ROM 和处理器设备模拟
- 标记队列
- SCSI 任务属性支持（有序、队首、简单标签）
- SCSI 隐式命令排序支持
- 完整的任务管理支持（中止、查询、重置等）
- 支持多个端口、发起方、目标和后端存储
- 支持 VMWare VAAI 和 Microsoft ODX 卸载（COMPARE AND WRITE、XCOPY、POPULATE TOKEN/WRITE USING TOKEN、WRITE SAME 和 UNMAP）
- 持久预留支持
- 丰富的 VPD/模式/日志页支持
- 具备错误报告、错误注入和基本 SMART 支持
- 通过 ALUA 提供高可用性集群支持
- 所有 I/O 均在内核中处理，无用户态上下文切换开销

`ctl` 子系统包含多个前端，可通过不同的传输协议和实现提供访问：

**camsim** 通过虚拟发起方模式的 CAM(4) SIM 为本地系统提供访问。

**camtgt** 通过目标模式的 CAM(4) SIM（如 Fibre Channel [isp(4)](isp.4.md) 和 [mpt(4)](mpt.4.md)）为远程系统提供访问。

**cfumass** 通过 USB 大容量存储类 Bulk Only（BBB）传输为远程系统提供访问。

**ha** 内部前端，用于在高可用性集群中接收来自其他节点端口的请求。

**ioctl** 通过基于 ioctl(2) 的 API 为本地用户级应用程序提供访问。

**iscsi** 使用 [cfiscsi(4)](cfiscsi.4.md) 通过 iSCSI 协议为远程系统提供访问。

**tpc** 内部前端，用于接收来自第三方复制引擎的请求，实现复制卸载操作。

`ctl` 子系统包含两个后端，可使用不同类型的后端存储创建逻辑单元：

**block** 将数据存储于 ZFS ZVOL、文件或裸块设备中。

**ramdisk** 将数据存储于 RAM 中，这使其主要用于性能测试。根据配置的容量，可作为黑洞、精简或厚置备磁盘工作。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数：

**1** 记录出错的命令；

**2** 记录所有命令；

**4** 记录除 READ/WRITE 之外的命令数据。

**0** 活动/备用——主节点拥有后端访问权并处理请求，而备节点只能进行基本的 LUN 发现和预留；

**1** 活动/活动——两个节点均拥有后端访问权并处理请求，备节点与主节点同步处理；

**2** 活动/活动——主节点拥有后端访问权并处理请求，备节点将所有请求和数据转发给主节点；

**0** 未配置；

**1** 已配置但未建立；

**2** 已建立。

**0** 主；

**1** 备。

**`kern.cam.ctl.debug`** 已启用的 CTL 日志级别位掩码：默认为 0。

**`kern.cam.ctl.ha_id`** 指定此节点在高可用性集群中的唯一位置。默认为 0——无 HA，1 和 2——在指定位置启用 HA。

**`kern.cam.ctl.ha_mode`** 指定高可用性集群操作模式：上述所有模式都要求 HA 集群节点之间已建立连接。如果未配置连接，备节点将报告 Unavailable 状态；如果已配置但未建立，则报告 Transitioning 状态。默认为 0。

**`kern.cam.ctl.ha_peer`** 字符串值，指定与对端 HA 节点建立连接的方法。可为 "listen IP:port"、"connect IP:port" 或空值。

**`kern.cam.ctl.ha_link`** 报告 HA 集群节点之间连接的当前状态：

**`kern.cam.ctl.ha_role`** 指定此节点的默认角色：此角色可通过 "ha_role" LUN 选项按 LUN 覆盖，使得对于一个 LUN 某节点为主，而对于另一个 LUN 则为另一节点为主。在 HA 模式 0 和 2 中，从主切换为备会关闭后端，反向切换则打开后端。若无主节点（两个节点均为备，或备节点无法连接到主节点），备节点报告 Transitioning 状态。存在两个主节点的状态是非法的（脑裂条件）。

## 可调变量

以下变量作为 [loader(8)](../man8/loader.8.md) 可调参数提供：

**`kern.cam.ctl.max_luns`** 指定所支持的最大 LUN 数，必须为 2 的幂。默认值为 1024。

**`kern.cam.ctl.max_ports`** 指定所支持的最大端口数，必须为 2 的幂。默认值为 1024。

## 参见

[cfiscsi(4)](cfiscsi.4.md), [cfumass(4)](cfumass.4.md), ctladm(8), ctld(8), ctlstat(8)

## 历史

`ctl` 子系统首次出现于 FreeBSD 9.1。

## 作者

`ctl` 子系统最初由 Kenneth Merry <ken@FreeBSD.org> 编写。后续工作由 Alexander Motin <mav@FreeBSD.org> 完成。
