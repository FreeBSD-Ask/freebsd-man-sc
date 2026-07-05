# devcfg.4.arm

`devcfg` — Zynq PL 设备配置接口

## 名称

`devcfg`

## 概要

`device devcfg`

## 描述

特殊文件 **/dev/devcfg** 可用于配置 Xilinx Zynq-7000 的 PL（FPGA）部分。

在文件偏移 0 处首次写入字符设备时，`devcfg` 驱动会置位顶层 PL 复位信号，禁用 PS-PL 电平转换器，并清除 PL 配置。写入数据被发送到 PCAP（处理器配置访问端口）。当 PL 置位 DONE 信号时，devcfg 驱动将启用电平转换器并释放顶层 PL 复位信号。

可通过将比特流写入字符设备来配置 PL（FPGA），如下所示：

```sh
cat design.bit.bin > /dev/devcfg
```

不应将此文件与 FPGA 设计工具输出的 .bit 文件混淆。它是配置比特流的二进制形式。Xilinx `promgen` 工具可进行转换：

```sh
promgen -b -w -p bin -data_width 32 -u 0 design.bit -o design.bit.bin
```

## sysctl 变量

`devcfg` 驱动提供以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`hw.fpga.pl_done`** 此变量始终反映 PL 的 DONE 信号状态。1 表示 PL 部分已被正确编程。

**`hw.fpga.en_level_shifters`** 此变量控制 PL 部分重新配置后是否启用 PS-PL 电平转换器。此变量默认为 1，但设为 0 时允许 PL 部分以不与器件 PS 部分接口的配置进行编程。在下次设备重新配置之前，更改此值对电平转换器没有影响。

## 文件

**`/dev/devcfg`** `devcfg` 驱动的字符设备。

## 参见

Zynq-7000 SoC Technical Reference Manual (Xilinx doc UG585)

## 作者

Thomas Skibo
