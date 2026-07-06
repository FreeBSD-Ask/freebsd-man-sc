# uhid.4

`uhid` — USB 通用 HID 支持

## 名称

`uhid`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device uhid
> device hid
> device usb

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uhid_load="YES"
```

## 描述

`uhid` 驱动为 USB 设备中所有没有专用驱动的人机接口设备（HID）接口提供支持。

该设备处理以下 ioctl(2) 调用：

```sh
struct usb_gen_descriptor {
	void   *ugd_data;
	uint16_t ugd_maxlen;
	uint16_t ugd_actlen;
	uint8_t	ugd_report_type;
	...
};
```

**`USB_GET_REPORT_ID`** (`int`) 获取此 HID 报告使用的报告标识符。

**`USB_GET_REPORT_DESC`** (`struct usb_gen_descriptor`) 获取 HID 报告描述符。将最多 `ugd_maxlen` 字节的报告描述符数据复制到 `ugd_data` 指定的内存中。返回时 `ugd_actlen` 设置为复制的字节数。使用此描述符可找到设备数据的精确布局和含义。报告描述符未经任何处理即交付。

**`USB_SET_IMMED`** (`int`) 将设备设置为一种模式，其中每次 read(2) 都会返回输入报告的当前值。通常 read(2) 仅返回设备在其中断管道上报告的数据。如果设备不支持此功能，此调用可能失败。

**`USB_GET_REPORT`** (`struct usb_gen_descriptor`) 从设备获取报告，无需等待中断管道上的数据。将最多 `ugd_maxlen` 字节的报告数据复制到 `ugd_data` 指定的内存中。返回时 `ugd_actlen` 设置为复制的字节数。`ugd_report_type` 字段指示请求哪个报告。它应为 `UHID_INPUT_REPORT`、`UHID_OUTPUT_REPORT` 或 `UHID_FEATURE_REPORT`。如果设备不支持此功能，此调用可能失败。

**`USB_SET_REPORT`** (`struct usb_gen_descriptor`) 在设备中设置报告。`ugd_report_type` 字段指示要设置哪个报告。它应为 `UHID_INPUT_REPORT`、`UHID_OUTPUT_REPORT` 或 `UHID_FEATURE_REPORT`。报告的值由 `ugd_data` 和 `ugd_maxlen` 字段指定。如果设备不支持此功能，此调用可能失败。

**`USB_GET_DEVICEINFO`** (`struct usb_device_info`) 返回设备信息，例如 USB 厂商 ID 和 USB 产品 ID。此调用不会发出任何 USB 事务。另请参见 [ugen(4)](ugen.4.md)。

使用 read(2) 从设备获取数据。数据应按报告描述符规定的大小分块读取。

使用 write(2) 向设备发送数据。数据应按报告描述符规定的大小分块写入。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.uhid.debug`** 调试输出级别，0 表示禁用调试，更大的值增加调试消息的详细程度。默认为 0。

## 文件

**`/dev/uhid?`**

## 参见

usbhidctl(1), [usb(4)](usb.4.md)

## 历史

`uhid` 驱动出现于 NetBSD 1.4。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 引入。
