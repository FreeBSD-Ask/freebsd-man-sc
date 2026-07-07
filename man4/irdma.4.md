# irdma(4)

`irdma` — Intel(R) Ethernet Controller E810 的 RDMA FreeBSD 驱动

## 名称

`irdma`

## 概要

`此模块依赖 ice(4)`

`options OFED options OFED_DEBUG_INIT options COMPAT_LINUXKPI options SDP options IPOIB_CM`

以下内核选项应包含在配置中：

## 描述

### 特性

`irdma` 驱动在由 [ice(4)](ice.4.md) 支持的、支持 RDMA 的 Intel Ethernet 800 系列网卡上提供 RDMA 协议支持。

该驱动同时支持 iWARP 和 RoCEv2 协议。

## 配置

### 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`dev.irdma<interface_number>.roce_enable`** 在 <interface_number> 接口上启用 RoCEv2 协议。默认使用 RoCEv2 协议。

**`dev.irdma<interface_number>.dcqcn_cc_cfg_valid`** 表示所有 DCQCN 参数有效，应在寄存器或 QP 上下文中更新。将此参数设置为 1 表示 *dcqcn_min_dec_factor , dcqcn_min_rate_MBps , dcqcn_F , dcqcn_T, dcqcn_B, dcqcn_rai_factor, dcqcn_hai_factor, dcqcn_rreduce_mperiod* 中的设置将被采用。否则使用默认值。注意：此可调参数生效时还必须设置 "roce_enable"。

**`dev.irdma<interface_number>.dcqcn_min_dec_factor`** 处理 CNP 时当前发送速率可改变的最小因子。值以百分比（1-100）给出。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

**`dev.irdma<interface_number>.dcqcn_min_rate_MBps`** 速率限制的最小值，单位为 Mbits/s。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

**`dev.irdma<interface_number>.dcqcn_F`** 在带宽恢复的每个阶段中保持的次数。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

**`dev.irdma<interface_number>.dcqcn_T`** 在 DCQCN 模式下增加 CWND 前应经过的微秒数。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

**`dev.irdma<interface_number>.dcqcn_B`** 在 DCQCN 模式下更新 CWND 前要发送的字节数。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

**`dev.irdma<interface_number>.dcqcn_rai_factor`** 在加性增加模式下加到拥塞窗口的 MSS 数量。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

**`dev.irdma<interface_number>.dcqcn_hai_factor`** 在超活跃增加模式下加到拥塞窗口的 MSS 数量。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

**`dev.irdma<interface_number>.dcqcn_rreduce_mperiod`** 单个流连续两次速率降低之间的最短时间。仅在相关时间间隔内收到 CNP 时才会发生速率降低。注意：此可调参数生效时还必须设置 "roce_enable" 和 "dcqcn_cc_cfg_valid"。

### SYSCTL 过程

运行时调整可使用 sysctl 控制。

**`dev.irdma<interface_number>.debug`** 定义调试消息级别。典型值：1 表示仅错误，0x7fffffff 表示完整调试。

**`dev.irdma<interface_number>.dcqcn_enable`** 为 RoCEv2 启用 DCQCN 算法。注意：此 sysctl 生效时还必须设置 "roce_enable"。注意：可随时更改此设置，但仅应用于新创建的 QP。

### 测试

```sh
kldload irdma
```

```sh
hw.ice.irdma=1
```

```sh
sysctl -a | grep infiniband
```

```sh
dev.irdma<interface_number>.roce_enable=1
```

**dev.irdma0.roce_enable=0**

**dev.irdma1.roce_enable=1**

```sh
sysctl dev.irdma<interface_number>.roce_enable
```

```sh
sysctl dev.irdma2.roce_enable
```

```sh
sysctl dev.ice.<interface_number>.fc=3
```

make clean

make

make install

kldload krping

```sh
echo size=64,count=1,port=6601,addr=100.0.0.189,server > /dev/krping
```

```sh
echo size=64,count=1,port=6601,addr=100.0.0.189,client > /dev/krping
```

- 要加载 irdma 驱动，运行：如果 if_ice 尚未加载，系统会自动加载。如果 irdma 驱动未加载，请检查 sysctl `hw.ice.irdma` 的值是否为 1。要更改值，在 **/boot/loader.conf** 中写入：并重启。
- 要检查驱动是否已加载，运行：通常，如果一切顺利，每个 PF 将出现约 190 个条目。
- 网卡的每个接口可在 iWARP 或 RoCEv2 模式下工作。要启用 RoCEv2 兼容性，添加：其中 <interface_number> 是需要启用 RoCEv2 协议的所需 ice 接口编号，写入：**/boot/loader.conf**，例如：将在 ice0 上保持 iWARP 模式并在接口 ice1 上启用 RoCEv2 模式。RoCEv2 模式为默认。要检查 irdma roce_enable 状态，运行：例如：返回值为 '0' 表示 iWARP 模式，值为 '1' 表示 RoCEv2 模式。注意：以一种模式配置的接口将无法连接到以另一种模式配置的节点。注意：RoCEv2 当前支持有限，仅用于功能测试。当前不支持 DCB 和优先级流控制（PFC），可能导致显著的性能损失或连接问题。
- 在 ice 驱动中启用流控制：在系统所连接的交换机上启用流控制。详细信息请参见交换机文档。
- krping 软件的源代码随内核提供，位于 **/usr/src/sys/contrib/rdma/krping/**。要编译该软件，切换到 **/usr/src/sys/modules/rdma/krping/** 并执行以下命令：
- 在一台机器上启动 krping 服务器：
- 从另一台机器连接客户端：

## 支持

如需一般信息和支持，请访问 Intel 支持网站：<Lk <http://support.intel.com/>。>

如果使用受支持的适配器发现此驱动的问题，请将与问题相关的所有具体信息发送邮件至 <freebsd@intel.com>。

## 参见

[ice(4)](ice.4.md)

## 作者

`irdma` 驱动由 Bartosz Sobczak <bartosz.sobczak@intel.com> 编写。
