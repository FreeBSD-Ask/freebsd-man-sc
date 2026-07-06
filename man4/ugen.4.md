# ugen.4

`ugen` — USB 通用设备支持

## 名称

`ugen`

## 概要

`ugen 集成于 usb(4) 内核模块中。`

## 描述

`ugen` 驱动为所有没有专用驱动的 USB 设备提供支持。它支持访问设备的所有部分，但不如专用驱动方便。

USB 总线上最多可连接 127 个 USB 设备。每个 USB 设备最多可有 16 个端点。每个端点以四种不同模式之一通信：控制、同步、批量或中断。每个端点都有不同的设备节点。次设备号的最低 4 位决定设备访问哪个端点，其余位决定哪个 USB 设备。

如果某个端点地址同时用于输入和输出，则该设备可同时以读或写方式打开。

要查看存在哪些端点，可对控制端点执行一系列 ioctl(2) 操作，这些操作返回设备、配置、接口和端点的 USB 描述符。

控制传输模式只能在控制端点（始终为端点 0）上进行。控制端点接受请求，并可能响应该请求。控制请求通过 ioctl(2) 调用发出。

批量传输模式依据端点可为输入或输出。要在批量端点上执行 I/O，应使用 read(2) 和 write(2)。批量端点上的所有 I/O 操作均无缓冲。

中断传输模式依据端点可为输入或输出。要在中断端点上执行 I/O，应使用 read(2) 和 write(2)。驱动会进行适度的缓冲。

所有端点均处理以下 ioctl(2) 调用：

**`USB_SET_SHORT_XFER`** (`int`) 允许短读取传输。通常，来自设备的传输如果短于指定的请求长度，会报告为错误。

**`USB_SET_TIMEOUT`** (`int`) 设置设备操作的超时时间，时间以毫秒为单位指定。值 0 表示无超时。

控制端点（端点 0）处理以下 ioctl(2) 调用：

```sh
struct usb_alt_interface {
	int	uai_config_index;
	int	uai_interface_index;
	int	uai_alt_no;
};
```

```sh
struct usb_config_desc {
	int	ucd_config_index;
	usb_config_descriptor_t ucd_desc;
};
```

```sh
struct usb_interface_desc {
	int	uid_config_index;
	int	uid_interface_index;
	int	uid_alt_index;
	usb_interface_descriptor_t uid_desc;
};
```

```sh
struct usb_endpoint_desc {
	int	ued_config_index;
	int	ued_interface_index;
	int	ued_alt_index;
	int	ued_endpoint_index;
	usb_endpoint_descriptor_t ued_desc;
};
```

```sh
struct usb_full_desc {
	int	ufd_config_index;
	u_int	ufd_size;
	u_char	*ufd_data;
};
```

```sh
struct usb_string_desc {
	int	usd_string_index;
	int	usd_language_id;
	usb_string_descriptor_t usd_desc;
};
```

```sh
struct usb_ctl_request {
	int	ucr_addr;
	usb_device_request_t ucr_request;
	void	*ucr_data;
	int	ucr_flags;
#define USBD_SHORT_XFER_OK	0x04	/* 允许短读取 */
	int	ucr_actlen;		/* 实际传输长度 */
};
```

**`USB_GET_CONFIG`** (`int`) 获取设备配置号。

**`USB_SET_CONFIG`** (`int`) 将设备设置为给定配置号。此操作仅在控制端点是唯一打开的端点时才能执行。

**`USB_GET_ALTINTERFACE`** (`struct usb_alt_interface`) 获取具有给定索引的接口的备用设置号。此调用中 `uai_config_index` 被忽略。

**`USB_SET_ALTINTERFACE`** (`struct usb_alt_interface`) 将具有给定索引的接口的备用设置设置为给定号。此调用中 `uai_config_index` 被忽略。此操作仅在该接口没有任何端点打开时才能执行。

**`USB_GET_NO_ALT`** (`struct usb_alt_interface`) 在 `uai_alt_no` 字段中返回不同备用设置的数量。

**`USB_GET_DEVICE_DESC`** (`usb_device_descriptor_t`) 返回设备描述符。

**`USB_GET_CONFIG_DESC`** (`struct usb_config_desc`) 返回具有给定索引的配置的描述符。为方便起见，当前配置可通过 `USB_CURRENT_CONFIG_INDEX` 指定。

**`USB_GET_INTERFACE_DESC`** (`struct usb_interface_desc`) 返回由其配置索引、接口索引和备用索引指定的接口的接口描述符。为方便起见，当前备用设置可通过 `USB_CURRENT_ALT_INDEX` 指定。

**`USB_GET_ENDPOINT_DESC`** (`struct usb_endpoint_desc`) 返回由其配置索引、接口索引、备用索引和端点索引指定的端点的端点描述符。

**`USB_GET_FULL_DESC`** (`struct usb_full_desc`) 返回给定配置的所有描述符。`ufd_data` 字段应指向大小由 `ufd_size` 字段给定的内存区域。正确的大小可通过先发出 `USB_GET_CONFIG_DESC` 并检查 `wTotalLength` 字段来确定。

**`USB_GET_STRING_DESC`** (`struct usb_string_desc`) 获取给定语言 ID 和字符串索引的字符串描述符。

**`USB_DO_REQUEST`** (`struct usb_ctl_request`) 在控制端点上向设备发送 USB 请求。发送到设备或从设备接收的任何数据位于 `ucr_data`。传输数据的大小由 `ucr_request` 确定。此调用中 `ucr_addr` 字段被忽略。`ucr_flags` 字段可用于标记请求允许短于请求的大小，完成后 `ucr_actlen` 将包含实际大小。此操作具有危险性，因为它可在设备上执行任意操作。一些最危险的操作（例如更改设备地址）不被允许。

**`USB_GET_DEVICEINFO`** (`struct usb_device_info`) 获取设备的信息摘要。此调用不会发出任何 USB 事务。

注意，寻址配置、接口、备用设置和端点有两种方式：按索引或按编号。索引是设备呈现的描述符的序号（从 0 开始）。编号是在其描述符中找到的实体的相应编号。描述符枚举使用索引，获取和设置通常使用编号。

示例：要查找当前配置的所有端点（控制端点除外），可将 `interface_index` 从 0 迭代到 `config_desc->bNumInterface`-1，并对每个接口将 `endpoint_index` 从 0 迭代到 `interface_desc->bNumEndpoints`。`config_index` 应设置为 `USB_CURRENT_CONFIG_INDEX`，`alt_index` 应设置为 `USB_CURRENT_ALT_INDEX`。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.ugen.debug`** 调试输出级别，0 表示禁用调试，更大的值增加调试消息的详细程度。默认为 0。

## 文件

**`/dev/usb/B.D.E`** 总线 **文件** 上设备 `D` 的端点 `E`。
**`/dev/ugenB.D`** 总线 **文件** 上设备 `D` 的控制端点 0。

## 参见

[usb(4)](usb.4.md)

## 历史

`ugen` 驱动出现于 NetBSD 1.4。
