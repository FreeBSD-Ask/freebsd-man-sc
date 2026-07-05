# qat.4

`qat` — Intel QuickAssist Technology 压缩与加密驱动程序

## 名称

`qat`

## 概要

若要加载驱动程序，调用：

`kldload qat`

-

若要在引导时加载驱动程序，将以下行加入 loader.conf(5)：

`qat_200xx_fw_load="YES"`

`qat_c3xxx_fw_load="YES"`

`qat_c4xxx_fw_load="YES"`

`qat_c62x_fw_load="YES"`

`qat_dh895xcc_fw_load="YES"`

`qat_4xxx_fw_load="YES"`

`qat_load="YES"`

-
-
-
-
-
-
-

## 描述

`qat` 驱动程序支持 Intel (R) QuickAssist Technology (QAT) 设备的加密和压缩加速。

内核中暴露了用于卸载这些操作的完整 API，任何其他实体都可以直接使用。除了暴露用于卸载加密和压缩操作的完整内核 API 外，`qat` 驱动程序还与 [crypto(4)](crypto.4.md) 集成，允许将受支持的操作卸载到 Intel QuickAssist Technology 设备。

## 硬件

`qat` 驱动程序支持以下 Intel QuickAssist Technology 引擎：

- Intel (R) C62x 芯片组
- Intel (R) Atom C3000 处理器产品家族
- Intel (R) QuickAssist Adapter 8960/Intel (R) QuickAssist Adapter 8970（前称“Lewis Hill”）
- Intel (R) Communications Chipset 8925 至 8955 系列
- Intel (R) Atom P5300 处理器产品家族
- Intel (R) QAT 4xxx 系列

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用于重新配置 `qat` 设备。为了保持配置持久化，这些变量可在加载驱动程序之前设置，可通过 [kenv(1)](../man1/kenv.1.md) 或 loader.conf(5)。

更改配置前，特定设备必须处于“down”状态。

**`dev.qat.X.state`** 显示或设置设备的当前状态。可能取值：“down”、“up”。注意：如果设备使用了对称服务，则在重新配置设备之前需要禁用 **qat_ocf** 驱动程序。

**`dev.qat_ocf.0.enable`** 启用/禁用 QAT 加密框架连接。默认启用。

**`dev.qat.X.cfg_services`** 覆盖启用的设备服务，可为以下之一：symmetric、asymmetric、data compression。可能取值：“sym”、“asym”、“dc”、“sym;dc”、“asym;dc”、“sym;asym”。默认配置的服务对于偶数设备为“sym;asym”，对于奇数设备为 “dc”。

**`dev.qat.X.cfg_mode`** 覆盖内核空间和用户空间实例的设备模式配置。可能取值：“ks”、“us”、“ks;us”。默认值为“ks;us”。

**`dev.qat.X.num_user_processes`** 覆盖可连接到 QAT 设备的 uio 用户空间进程数。默认：2

**`dev.qat.X.disable_safe_dc_mode`** 覆盖历史缓冲区缓解。默认禁用。启用后解压吞吐量会增加，但若 `dev.qat.X.num_user_processes` 大于 1 可能导致数据泄漏。仅当你的系统不易发生用户数据泄漏时才启用此选项。

以下 [sysctl(8)](../man8/sysctl.8.md) 变量为只读：

**`dev.qat.X.frequency`** QAT 设备频率值。

**`dev.qat.X.mmp_version`** QAT MMP 库修订号。

**`dev.qat.X.hw_version`** QAT 硬件修订号。

**`dev.qat.X.fw_version`** QAT 固件修订号。

**`dev.qat.X.dev_cfg`** 设备特定配置摘要。

**`dev.qat.X.heartbeat`** QAT 设备心跳状态。值‘1’表示设备运行正常。值‘0’ 表示设备无响应。设备需要重启。

**`dev.qat.X.heartbeat_failed`** 收到的 QAT 心跳失败次数。

**`dev.qat.X.heartbeat_sent`** 发送的 QAT 心跳请求数。

## 参见

[crypto(4)](crypto.4.md), [ipsec(4)](ipsec.4.md), [pci(4)](pci.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

有关用法及受支持的操作和算法的详细信息，请参阅 Intel 下载中心 Lk <https://downloadcenter.intel.com> 提供的以下文档：

> Intel (R), "QuickAssist Technology API Programmer's Guide".

> Intel (R), "QuickAssist Technology Cryptographic API Reference Manual".

> Intel (R), "QuickAssist Technology Data Compression API Reference Manual".

> Intel (R), "QuickAssist Technology Performance Optimization Guide".

-
-
-
-

## 历史

`qat` 驱动程序出现于 FreeBSD 13.0。在 FreeBSD 14.0 中被上游驱动程序取代。

## 作者

`qat` 驱动程序由 Intel (R) Corporation 编写。
