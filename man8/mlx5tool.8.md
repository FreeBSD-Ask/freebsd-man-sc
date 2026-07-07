# mlx5tool(8)

`mlx5tool` — 管理 Connect-X 4/5/6 Mellanox 网络适配器的工具

## 名称

`mlx5tool`

## 概要

`mlx5tool -d domain:bus:slot:func -E`

`mlx5tool -d domain:bus:slot:func -e`

`mlx5tool -d domain:bus:slot:func -f file.mfa2`

`mlx5tool -d domain:bus:slot:func -o file -w`

`mlx5tool -d domain:bus:slot:func -r`

`mlx5tool -d domain:bus:slot:func -z`

## 描述

`mlx5tool` 工具用于管理 Connect-X4、5 和 6 网络适配器，涵盖通用 [ifconfig(8)](ifconfig.8.md) 命令未涉及的方面，主要与 PCIe 附件和卡内部工作相关。该工具在特定适配器上执行命令，适配器使用 PCIe 总线的 *device:bus:slot:function* 约定寻址。你可以使用 pciconf(8) 工具匹配适配器的以太网名称和地址。地址作为 `-d` 选项的参数传递，每次调用都必须指定。

当驱动程序检测到硬件故障，或应用户请求，可以创建*固件转储（firmware dump）*，其中包含有关设备内部状态的调试信息，供 Mellanox 支持团队分析故障。

目前已实现以下命令：

**`-E`** 打印 EEPROM 信息

**`-e`** 对固件寄存器状态进行快照并存储到内核缓冲区。缓冲区必须为空，换言之，此前不应已写入任何转储，或已使用 `-r` 命令清除现有转储。

**`-f`** 将固件镜像 `file.mfa2` 刷写到指定适配器。镜像必须为 MFA2 打包格式，并包含适用于适配器硬件的组件。通常需要 PCIe 链路级复位来激活新刷写的镜像，可通过系统重启或使用 `-z` 选项对指定设备执行。

**`-r`** 清除已存储的固件转储，为下一次转储准备内核缓冲区。

**`-w`** 获取已存储的固件转储并将其写入由 `-o` 选项参数指定的文件。

**`-z`** 对指定设备执行 PCIe 链路级复位。

## 文件

**/dev/mlx5ctl** [devfs(4)](../man4/devfs.4.md) 节点用于向驱动程序传递命令。

## 参见

[mlx5en(4)](../man4/mlx5en.4.md), [mlx5ib(4)](../man4/mlx5ib.4.md), [mlx5io(4)](../man4/mlx5io.4.md), [ifconfig(8)](ifconfig.8.md) 和 pciconf(8)。
