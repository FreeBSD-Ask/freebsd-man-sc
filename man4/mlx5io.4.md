# mlx5io.4

`mlx5io` — 管理 Connect-X 4/5/6 Mellanox 网络适配器的 IOCTL 接口

## 名称

`mlx5io`

## 概要

`#include <dev/mlx5/mlx5io.h>`

## 描述

`mlx5io` 接口用于管理 Connect-X 4、5 和 6 网络适配器，覆盖通用网络配置之外的方面，主要与 PCIe 附件和卡内工作相关。该接口由若干命令组成，通过在从 `/dev/mlx5ctl` 设备节点打开的文件描述符上调用 ioctl(2) 来传递。

已实现以下命令：

```sh
struct mlx5_tool_addr {
	uint32_t domain;
	uint8_t bus;
	uint8_t slot;
	uint8_t func;
};
```

```sh
struct mlx5_fwdump_get {
	struct mlx5_tool_addr devaddr;
	struct mlx5_fwdump_reg *buf;
	size_t reg_cnt;
	size_t reg_filled; /* 输出 */
};
```

```sh
struct mlx5_fwdump_reg {
	uint32_t addr;
	uint32_t val;
};
```

```sh
struct mlx5_fw_update {
	struct mlx5_tool_addr devaddr;
	void *img_fw_data;
	size_t img_fw_data_len;
};
```

```sh
struct mlx5_eeprom_get {
        struct mlx5_tool_addr devaddr;
        size_t eeprom_info_page_valid;
        uint32_t *eeprom_info_buf;
        size_t eeprom_info_out_len;
};
```

**`MLX5_FWDUMP_FORCE`** 对固件寄存器状态进行快照并存储到内核缓冲区。该缓冲区必须为空，换句话说，此前不应已写入任何转储，或已对指定设备使用 `MLX5_FWDUMP_RESET` 命令清除现有转储。该命令的参数应指向一个 `struct mlx5_tool_addr` 结构，包含设备的 PCIe 总线地址。

**`MLX5_FWDUMP_RESET`** 清除已存储的固件转储，为下一次转储准备内核缓冲区。该命令的参数应指向一个 `struct mlx5_tool_addr` 结构，包含设备的 PCIe 总线地址。

**`MLX5_FWDUMP_GET`** 将已存储的固件转储提取到用户内存中。该命令的参数应指向输入/输出 `struct mlx5_fwdump_get` 结构。其 `devaddr` 字段指定设备地址，`buf` 字段指向由 `struct mlx5_fwdump_reg` 组成的数组，用于记录寄存器值，数组大小由 `reg_cnt` 字段指定。成功返回时，`reg_filled` 字段报告 `buf` 数组中实际填充了寄存器值的元素数量。若 `buf` 包含 `NULL` 指针，则不会填充任何寄存器，但 `reg_filled` 仍会包含为完整转储所需传递的寄存器数量。`struct mlx5_fwdump_reg` 元素在 `addr` 字段中包含寄存器地址，在 `val` 字段中包含其值。

**`MLX5_FW_UPDATE`** 请求对由 `devaddr` 指定的适配器使用 `MFA2` 格式的固件镜像进行固件更新（刷写）。该 ioctl 命令的参数为 `struct mlx5_fw_update`，定义如下。镜像在内存中的地址通过 `img_fw_data` 传递，镜像长度由 `img_fw_data_len` 字段指定。

**`MLX5_FW_RESET`** 请求对该设备执行 PCIe 链路级重置。设备地址由 `struct mlx5_tool_addr` 结构指定，应作为参数传递。

**`MLX5_EEPROM_GET`** 提取 EEPROM 信息。该命令的参数应指向输入/输出 `struct mlx5_eeprom_get` 结构，其中 `devaddr` 字段指定设备地址。成功返回时，`eeprom_info_out_len` 字段报告 EEPROM 信息的长度。`eeprom_info_buf` 字段包含实际的 EEPROM 信息。`eeprom_info_page_valid` 字段报告第三页的有效性。

## 文件

`/dev/mlx5ctl` [devfs(4)](devfs.4.md) 节点用于向驱动传递命令。

## 返回值

成功时，IOCTL 返回零。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 参见

[errno(2)](../man2/errno.2.md), [ioctl(2)](../man2/ioctl.2.md), [mlx5en(4)](mlx5en.4.md), [mlx5ib(4)](mlx5ib.4.md), [mlx5tool(8)](../man8/mlx5tool.8.md) 和 [pci(9)](../man9/pci.9.md)
