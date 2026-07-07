# hidraw(4)

`hidraw` — HID 设备的原始访问

## 名称

`hidraw`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device hidraw
> device hid
> device hidbus

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
hidraw_load="YES"
```

## 描述

`hidraw` 驱动提供对人机接口设备 (Human Interface Devices, HID) 的原始接口。报告会原封不动地发送到设备或从设备接收。

该设备处理 2 组 ioctl(2) 调用：

FreeBSD [uhid(4)](uhid.4.md) 兼容调用：

```sh
struct hidraw_gen_descriptor {
	void   *hgd_data;
	uint16_t hgd_maxlen;
	uint16_t hgd_actlen;
	uint8_t	hgd_report_type;
	...
};
```

**`HIDRAW_GET_REPORT_ID`** (`int`) 获取此 HID 报告使用的报告标识符。

**`HIDRAW_GET_REPORT_DESC`** (`struct hidraw_gen_descriptor`) 获取 HID 报告描述符。将最多 `hgd_maxlen` 字节的报告描述符数据复制到 `hgd_data` 指定的内存中。返回时 `hgd_actlen` 设置为实际复制的字节数。使用此描述符可找出从设备读取或写入设备的数据的确切布局和含义。报告描述符在交付时不做任何处理。

**`HIDRAW_SET_IMMED`** (`int`) 将设备设置为一种模式，每次 read(2) 都会返回输入报告的当前值。通常 read(2) 只返回设备在中断管道上报告的数据。如果设备不支持此特性，此调用可能失败。

**`HIDRAW_GET_REPORT`** (`struct hidraw_gen_descriptor`) 不等待中断管道上的数据，直接从设备获取报告。将最多 `hgd_maxlen` 字节的报告数据复制到 `hgd_data` 指定的内存中。返回时 `hgd_actlen` 设置为实际复制的字节数。`hgd_report_type` 字段指示请求哪种报告。它应为 `HID_INPUT_REPORT`、`HID_OUTPUT_REPORT` 或 `HID_FEATURE_REPORT`。在使用编号报告的设备上，返回数据的第一字节为报告编号。报告数据从第二字节开始。对于不使用编号报告的设备，报告数据从第一字节开始。如果设备不支持此特性，此调用可能失败。

**`HIDRAW_SET_REPORT`** (`struct hidraw_gen_descriptor`) 在设备中设置报告。`hgd_report_type` 字段指示要设置哪种报告。它应为 `HID_INPUT_REPORT`、`HID_OUTPUT_REPORT` 或 `HID_FEATURE_REPORT`。报告的值由 `hgd_data` 和 `hgd_maxlen` 字段指定。在使用编号报告的设备上，要发送的数据第一字节为报告编号。报告数据从第二字节开始。对于不使用编号报告的设备，报告数据从第一字节开始。如果设备不支持此特性，此调用可能失败。

**`HIDRAW_GET_DEVICEINFO`** (`struct hidraw_device_info`) 返回设备的信息，如厂商 ID 和产品 ID。此调用不会发起任何硬件传输。

Linux `hidraw` 兼容调用：

```sh
struct hidraw_report_descriptor {
	uint32_t	size;
	uint8_t		value[HID_MAX_DESCRIPTOR_SIZE];
};
```

```sh
struct hidraw_devinfo {
	uint32_t	bustype;
	int16_t		vendor;
	int16_t		product;
};
```

**`HIDIOCGRDESCSIZE`** (`int`) 获取 HID 报告描述符大小。返回设备报告描述符的大小，用于 `HIDIOCGRDESC` ioctl(2)。

**`HIDIOCGRDESC`** (`struct hidraw_report_descriptor`) 获取 HID 报告描述符。将最多 `size` 字节的报告描述符数据复制到 `value` 指定的内存中。

**`HIDIOCGRAWINFO`** (`struct hidraw_devinfo`) 获取包含设备的总线类型、厂商 ID (VID) 和产品 ID (PID) 的结构。总线类型可为以下之一：`BUS_USB` 或 `BUS_I2C`，定义在 dev/evdev/input.h 中。

**`HIDIOCGRAWNAME(len)`** (`char[] buf`) 获取设备描述。将之前由 [device_set_desc(9)](../man9/device_set_desc.9.md) 过程设置的设备描述最多 `len` 字节复制到 `buf` 指定的内存中。

**`HIDIOCGRAWPHYS(len)`** (`char[] buf`) 获取设备的 newbus 路径。将 newbus 设备路径最多 `len` 字节复制到 `buf` 指定的内存中。

**`HIDIOCGFEATURE(len)`** (`void[] buf`)

**`HIDIOCGINPUT(len)`** (`void[] buf`)

**`HIDIOCGOUTPUT(len)`** (`void[] buf`) 分别从设备获取 feature、input 或 output 报告。将最多 `len` 字节的报告数据复制到 `buf` 指定的内存中。所提供缓冲区的第一字节应设置为所请求报告的报告编号。对于不使用编号报告的设备，将第一字节设置为 0。报告将从缓冲区的第一字节开始返回（即：不返回报告编号）。如果设备不支持此特性，此调用可能失败。

**`HIDIOCSFEATURE(len)`** (`void[] buf`)

**`HIDIOCSINPUT(len)`** (`void[] buf`)

**`HIDIOCSOUTPUT(len)`** (`void[] buf`) 分别在设备中设置 feature、input 或 output 报告。报告的值由 `buf` 和 `len` 参数指定。将所提供缓冲区的第一字节设置为报告编号。对于不使用编号报告的设备，将第一字节设置为 0。报告数据从第二字节开始。务必相应地设置 len，比报告长度大 1（以容纳报告编号）。如果设备不支持此特性，此调用可能失败。

使用 read(2) 从设备获取数据。数据应按报告描述符规定的大小分块读取。在使用编号报告的设备上，返回数据的第一字节为报告编号。报告数据从第二字节开始。对于不使用编号报告的设备，报告数据从第一字节开始。

使用 write(2) 向设备发送数据。数据应按报告描述符规定的大小分块写入。传递给 write(2) 的缓冲区第一字节应设置为报告编号。如果设备不使用编号报告，则有 2 种操作模式：`hidraw` 模式和 [uhid(4)](uhid.4.md) 模式。在 `hidraw` 模式下，第一字节应设置为 0，报告数据本身应从第二字节开始。在 [uhid(4)](uhid.4.md) 模式下，报告数据应从第一字节开始。可分别通过发出 `HIDIOCGRDESC` 或 `HID_GET_REPORT_DESC` ioctl(2) 来切换模式。默认模式为 `hidraw`。

## SYSCTL 变量

以下变量既是 [sysctl(8)](../man8/sysctl.8.md) 变量，也是 [loader(8)](../man8/loader.8.md) 可调参数：

**`hw.hid.hidraw.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

## 文件

**`/dev/hidraw?`**

## 参见

usbhidctl(1), hid(4), [hidbus(4)](hidbus.4.md), [uhid(4)](uhid.4.md)

## 历史

[uhid(4)](uhid.4.md) 驱动出现于 NetBSD 1.4。`hidraw` 协议支持由 Vladimir Kondratyev <wulf@FreeBSD.org> 在 FreeBSD 13 中添加。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 移植。
