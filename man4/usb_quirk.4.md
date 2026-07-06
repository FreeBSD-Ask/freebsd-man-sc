# usb_quirk.4

`usb_quirk` — USB quirks 模块

## 名称

`usb_quirk`

## 概要

要将此模块编译进内核，请将以下行加入你的内核配置文件：

> device usb

或者，要在引导时以模块方式加载该模块，请将以下行加入 loader.conf(5)：

```sh
usb_quirk_load="YES"
```

## 描述

`usb_quirk` 模块提供对使用 usbconfig(8) 动态添加和删除 USB 设备 quirks 的支持。

## 通用 quirks：

**UQ_AUDIO_SWAP_LR** 交换左右声道

**UQ_AU_INP_ASYNC** 尽管声称是自适应的，输入实际上是异步的

**UQ_AU_NO_FRAC** 不对分数样本进行调整

**UQ_AU_NO_XU** 音频设备的扩展单元损坏

**UQ_AU_VENDOR_CLASS** 音频设备使用厂商类来标识自身

**UQ_AU_SET_SPDIF_CM6206** 音频设备需要特殊编程才能启用 S/PDIF 音频输出

**UQ_BAD_ADC** 错误的音频规范版本号

**UQ_BAD_AUDIO** 设备声称是音频类，但实际不是

**UQ_BROKEN_BIDIR** 打印机的双向模式损坏

**UQ_BUS_POWERED** 设备实际是总线供电的，尽管声称不是

**UQ_HID_IGNORE** 设备应被 hid 类忽略

**UQ_KBD_IGNORE** 设备应被 kbd 类忽略

**UQ_KBD_BOOTPROTO** 设备应设置引导协议

**UQ_UMS_IGNORE** 设备应被 ums 类忽略

**UQ_MS_BAD_CLASS** 标识不正确

**UQ_MS_LEADING_BYTE** 鼠标发送一个未知的前导字节

**UQ_MS_REVZ** 鼠标的 Z 轴反向

**UQ_MS_VENDOR_BTN** 鼠标的按钮在厂商用法页中

**UQ_NO_STRINGS** 字符串描述符损坏

**UQ_POWER_CLAIM** 集线器对电源状态撒谎

**UQ_SPUR_BUT_UP** 虚假的鼠标按钮释放事件

**UQ_SWAP_UNICODE** 某些 Unicode 字符串被交换

**UQ_CFG_INDEX_1** 默认选择配置索引 1

**UQ_CFG_INDEX_2** 默认选择配置索引 2

**UQ_CFG_INDEX_3** 默认选择配置索引 3

**UQ_CFG_INDEX_4** 默认选择配置索引 4

**UQ_CFG_INDEX_0** 默认选择配置索引 0

**UQ_ASSUME_CM_OVER_DATA** 假定 cm over data 特性

**UQ_IGNORE_CDC_CM** 忽略 cm 描述符

**UQ_WMT_IGNORE** 设备应被 wmt 驱动忽略

## USB 大容量存储 quirks：

**UQ_MSC_NO_TEST_UNIT_READY** 发送 start/stop 而非 TUR

**UQ_MSC_NO_RS_CLEAR_UA** 不重置单元注意

**UQ_MSC_NO_START_STOP** 不支持 start/stop

**UQ_MSC_NO_GETMAXLUN** 不支持 get max LUN

**UQ_MSC_NO_INQUIRY** 伪造通用查询响应

**UQ_MSC_NO_INQUIRY_EVPD** 不支持查询 EVPD

**UQ_MSC_NO_SYNC_CACHE** 不支持同步缓存

**UQ_MSC_SHUTTLE_INIT** 需要 Shuttle 初始化序列

**UQ_MSC_ALT_IFACE_1** 切换到备用接口 1

**UQ_MSC_FLOPPY_SPEED** 使用软盘速度（20kb/s）

**UQ_MSC_IGNORE_RESIDUE** 残留值计算错误

**UQ_MSC_WRONG_CSWSIG** 使用错误的 CSW 签名

**UQ_MSC_RBC_PAD_TO_12** 将 RBC 请求填充至 12 字节

**UQ_MSC_READ_CAP_OFFBY1** 报告扇区数，而非最大扇区

**UQ_MSC_FORCE_SHORT_INQ** 不支持完整查询

**UQ_MSC_FORCE_WIRE_BBB** 强制使用 BBB 线协议

**UQ_MSC_FORCE_WIRE_CBI** 强制使用 CBI 线协议

**UQ_MSC_FORCE_WIRE_CBI_I** 强制使用带中断的 CBI 线协议

**UQ_MSC_FORCE_PROTO_SCSI** 强制使用 SCSI 命令协议

**UQ_MSC_FORCE_PROTO_ATAPI** 强制使用 ATAPI 命令协议

**UQ_MSC_FORCE_PROTO_UFI** 强制使用 UFI 命令协议

**UQ_MSC_FORCE_PROTO_RBC** 强制使用 RBC 命令协议

## 3G 数据卡（u3g）quirks：

**UQ_MSC_EJECT_HUAWEI** 在 Huawei USB 命令后弹出

**UQ_MSC_EJECT_SIERRA** 在 Sierra USB 命令后弹出

**UQ_MSC_EJECT_SCSIEJECT** 在 SCSI 弹出命令 `0x1b0000000200` 后弹出

**UQ_MSC_EJECT_REZERO** 在 SCSI rezero 命令 `0x010000000000` 后弹出

**UQ_MSC_EJECT_ZTESTOR** 在 ZTE SCSI 命令 `0x850101011801010101010000` 后弹出

**UQ_MSC_EJECT_CMOTECH** 在 C-motech SCSI 命令 `0xff52444556434847` 后弹出

**UQ_MSC_EJECT_WAIT** 等待设备弹出

**UQ_MSC_EJECT_SAEL_M460** 在 Sael USB 命令后弹出

**UQ_MSC_EJECT_HUAWEISCSI** 在 Huawei SCSI 命令 `0x11060000000000000000000000000000` 后弹出

**UQ_MSC_EJECT_TCT** 在 TCT SCSI 命令 `0x06f504025270` 后弹出

**UQ_MSC_DYMO_EJECT** 在 HID 命令 `0x1b5a01` 后弹出

有关受支持 quirks 的完整列表，请参见 **`/sys/dev/usb/quirk/usb_quirk.h`** 或运行 "usbconfig dump_quirk_names"。

## LOADER 可调参数

以下可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

```sh
“VendorId ProductId LowRevision HighRevision UQ_QUIRK,... ”
```

**`hw.usb.quirk.%d`** 该值为一个字符串，格式为：为所有匹配 `VendorId` 和 `ProductId` 且硬件版本在 `LowRevision` 和 `HighRevision` 之间（含边界）的 USB 设备安装 quirks `UQ_QUIRK,...`。`VendorId`、`ProductId`、`LowRevision` 和 `HighRevision` 均为 16 位数字，可为十进制或十六进制。最多可定义 100 个变量 `hw.usb.quirk.0, .1, ..., .99`。如果在内核内部 quirks 表中找到匹配条目，则替换为新定义。否则，若 quirks 表未满，则创建新条目。内核从 `N = 0` 开始迭代 `hw.usb.quirk.N` 变量，直到 `N = 99` 或第一个不存在的变量为止。

## 实例

在附加了显示为 `ugen0.3` 上 USB 设备的 `u3g` 设备后：

```sh
usbconfig -d ugen0.3 add_quirk UQ_MSC_EJECT_WAIT
```

在 `ugen1.4` 上启用 Holtec/Keep Out F85 游戏键盘：

```sh
usbconfig -d ugen1.4 add_quirk UQ_KBD_BOOTPROTO
```

若要在引导时安装 quirk，请在 loader.conf(5) 中加入一行或多行如下内容：

```sh
hw.usb.quirk.0="0x04d9 0xfa50 0 0xffff UQ_KBD_IGNORE"
```

## 参见

usbconfig(8)

## 历史

`u3g` 模块出现于 FreeBSD 8.0，由 Hans Petter Selasky <hselasky@FreeBSD.org> 编写。本手册页由 Nick Hibma <n_hibma@FreeBSD.org> 编写。
