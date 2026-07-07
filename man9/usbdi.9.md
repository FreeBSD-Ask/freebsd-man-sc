# usbdi(9)

`usb_fifo_alloc_buffer` — 通用串行总线驱动程序编程接口

## 名称

`usb_fifo_alloc_buffer`, `usb_fifo_attach`, `usb_fifo_detach`, `usb_fifo_free_buffer`, `usb_fifo_get_data`, `usb_fifo_get_data_buffer`, `usb_fifo_get_data_error`, `usb_fifo_get_data_linear`, `usb_fifo_put_bytes_max`, `usb_fifo_put_data`, `usb_fifo_put_data_buffer`, `usb_fifo_put_data_error`, `usb_fifo_put_data_linear`, `usb_fifo_reset`, `usb_fifo_softc`, `usb_fifo_wakeup`, `usbd_do_request`, `usbd_do_request_flags`, `usbd_errstr`, `usbd_lookup_id_by_info`, `usbd_lookup_id_by_uaa`, `usbd_transfer_clear_stall`, `usbd_transfer_drain`, `usbd_transfer_pending`, `usbd_transfer_poll`, `usbd_transfer_setup`, `usbd_transfer_start`, `usbd_transfer_stop`, `usbd_transfer_submit`, `usbd_transfer_unsetup`, `usbd_xfer_clr_flag`, `usbd_xfer_frame_data`, `usbd_xfer_frame_len`, `usbd_xfer_get_frame`, `usbd_xfer_get_priv`, `usbd_xfer_is_stalled`, `usbd_xfer_max_framelen`, `usbd_xfer_max_frames`, `usbd_xfer_max_len`, `usbd_xfer_set_flag`, `usbd_xfer_set_frame_data`, `usbd_xfer_set_frame_len`, `usbd_xfer_set_frame_offset`, `usbd_xfer_set_frames`, `usbd_xfer_set_interval`, `usbd_xfer_set_priv`, `usbd_xfer_set_stall`, `usbd_xfer_set_timeout`, `usbd_xfer_softc`, `usbd_xfer_state`, `usbd_xfer_status`

## 概要

`#include <dev/usb/usb.h>`

`#include <dev/usb/usbdi.h>`

`#include <dev/usb/usbdi_util.h>`

`usb_error_t usbd_transfer_setup(struct usb_device *udev, const uint8_t *ifaces, struct usb_xfer **pxfer, const struct usb_config *setup_start, uint16_t n_setup, void *priv_sc, struct mtx *priv_mtx)`

`void usbd_transfer_unsetup(struct usb_xfer **pxfer, uint16_t n_setup)`

`void usbd_transfer_start(struct usb_xfer *xfer)`

`void usbd_transfer_stop(struct usb_xfer *xfer)`

`void usbd_transfer_drain(struct usb_xfer *xfer)`

## 描述

通用串行总线（USB）驱动程序编程接口为 USB 外设驱动程序提供与主机控制器无关的 API，用于控制和与 USB 外设通信。`usb` 模块同时支持 USB 主机和 USB 设备侧模式。

## USB 传输管理函数

USB 标准定义了四种类型的 USB 传输：控制传输、批量传输、中断传输和等时传输。所有传输类型都使用以下五个函数进行管理：

`usbd_transfer_setup()` 此函数将为 USB 传输数组及所有所需的 DMA 内存分配内存并初始化。此函数可能睡眠或阻塞等待资源可用。`udev` 是指向 `struct usb_device` 的指针。`ifaces` 是要使用的接口索引号数组。参见 `if_index`。`pxfer` 是指向 USB 传输指针数组的指针，这些指针初始化为 NULL，然后指向已分配的 USB 传输。`setup_start` 是指向 USB 配置结构数组的指针。`n_setup` 是告知 USB 系统应设置多少个 USB 传输的数字。`priv_sc` 是私有 softc 指针，用于初始化 `xfer->priv_sc`。`priv_mtx` 是保护传输结构和 softc 的私有互斥锁。此指针用于初始化 `xfer->priv_mtx`。此函数成功时返回零。非零返回值表示失败。

`usbd_transfer_unsetup()` 此函数将释放给定的 USB 传输及与这些 USB 传输关联的所有已分配资源。`pxfer` 是指向 USB 传输指针数组的指针，可以为 NULL，应由 USB 系统释放。`n_setup` 是告知 USB 系统应取消设置多少个 USB 传输的数字。此函数可能睡眠等待 USB 传输完成。此函数对 USB 传输结构指针是 NULL 安全的。不允许从 USB 传输回调中调用此函数。

`usbd_transfer_start()` 此函数将启动 `xfer` 所指向的 USB 传输（如果尚未启动）。此函数始终非阻塞，必须在所谓的私有 USB 互斥锁锁定时调用。此函数对 USB 传输结构指针是 NULL 安全的。

`usbd_transfer_stop()` 此函数将停止 `xfer` 所指向的 USB 传输（如果尚未停止）。此函数始终非阻塞，必须在所谓的私有 USB 互斥锁锁定时调用。此函数可在 USB 回调被调用之前返回。此函数对 USB 传输结构指针是 NULL 安全的。如果传输正在进行中，回调将以 `USB_ST_ERROR` 和 `error = USB_ERR_CANCELLED` 被调用。

`usbd_transfer_drain()` 此函数将停止 USB 传输（如果尚未停止），并等待任何额外的 USB 硬件操作完成。在使用 `usbd_xfer_set_frame_data()` 加载到 DMA 中的缓冲区在此函数返回后可以安全释放。此函数可能阻塞调用者，在 USB 回调被调用之前不会返回。此函数对 USB 传输结构指针是 NULL 安全的。

## USB 传输回调

USB 回调有三种状态：USB_ST_SETUP、USB_ST_TRANSFERRED 和 USB_ST_ERROR。USB_ST_SETUP 是初始状态。回调以此状态被调用后，将在稍后阶段以其他两种状态之一被回调。如果错误原因是 USB_ERR_CANCELLED，USB 回调不应重启 USB 传输。USB 回调受递归保护。这意味着可以从另一个传输的回调中启动和停止任何所需的传输，也包括当前正在回调的传输。递归的处理方式是，当希望递归的回调返回时，它将被再调用一次。

`usbd_transfer_submit()` 此函数仅应从 USB 回调内部调用，用于启动 USB 硬件。一个 USB 传输可以具有由一个或多个 USB 数据包组成的多帧，为所有 USB 传输类型构成 I/O 向量。

```c
void
usb_default_callback(struct usb_xfer *xfer, usb_error_t error)
{
	int actlen;
	usbd_xfer_status(xfer, &actlen, NULL, NULL, NULL);
	switch (USB_GET_STATE(xfer)) {
	case USB_ST_SETUP:
		/*
		 * 设置 xfer 帧长度/计数和数据
		 */
		usbd_transfer_submit(xfer);
		break;
	case USB_ST_TRANSFERRED:
		/*
		 * 读取 usb 帧数据（如果有）。
		 * "actlen" 是所有帧传输的总长度。
		 */
		break;
	default: /* 错误 */
		/*
		 * 例如，打印错误消息并清除停滞。
		 */
		break;
	}
	/*
	 * 此处在不持有私有 USB 互斥锁的情况下
	 * 执行操作是安全的。
	 */
	return;
}
```

## USB 控制传输

USB 控制传输有三部分。首先是 SETUP 数据包，然后是 DATA 数据包，最后是 STATUS 数据包。SETUP 数据包始终由帧 0 指向，其长度由 `usbd_xfer_frame_len()` 设置，即使不应发送任何 SETUP 数据包也是如此！如果 USB 控制传输没有 DATA 阶段，则帧数应设为 1。否则默认帧数为 2。

```sh
示例 1：SETUP + STATUS
 usbd_xfer_set_frames(xfer, 1);
 usbd_xfer_set_frame_len(xfer, 0, 8);
 usbd_transfer_submit(xfer);
示例 2：SETUP + DATA + STATUS
 usbd_xfer_set_frames(xfer, 2);
 usbd_xfer_set_frame_len(xfer, 0, 8);
 usbd_xfer_set_frame_len(xfer, 1, 1);
 usbd_transfer_submit(xfer);
示例 3：SETUP + DATA + STATUS - 拆分
第 1 次回调：
 usbd_xfer_set_frames(xfer, 1);
 usbd_xfer_set_frame_len(xfer, 0, 8);
 usbd_transfer_submit(xfer);
第 2 次回调：
 /* 重要：frbuffers[0] 必须仍然指向 setup 数据包！ */
 usbd_xfer_set_frames(xfer, 2);
 usbd_xfer_set_frame_len(xfer, 0, 0);
 usbd_xfer_set_frame_len(xfer, 1, 1);
 usbd_transfer_submit(xfer);
示例 4：SETUP + STATUS - 拆分
第 1 次回调：
 usbd_xfer_set_frames(xfer, 1);
 usbd_xfer_set_frame_len(xfer, 0, 8);
 usbd_xfer_set_flag(xfer, USB_MANUAL_STATUS);
 usbd_transfer_submit(xfer);
第 2 次回调：
 usbd_xfer_set_frames(xfer, 1);
 usbd_xfer_set_frame_len(xfer, 0, 0);
 usbd_xfer_clr_flag(xfer, USB_MANUAL_STATUS);
 usbd_transfer_submit(xfer);
```

## USB 传输配置

为简化端点搜索，`usb` 模块定义了一个 USB 配置结构，可在其中指定所需端点的特性。

```c
struct usb_config {
	bufsize,
	callback
	direction,
	endpoint,
	frames,
	index flags,
	interval,
	timeout,
	type,
};
```

`type` 字段选择 USB 管道类型。有效值为：UE_INTERRUPT、UE_CONTROL、UE_BULK、UE_ISOCHRONOUS。特殊值 UE_BULK_INTR 将选择 BULK 和 INTERRUPT 管道。此字段为必填。

`endpoint` 字段选择 USB 端点号。值 0xFF、`-1` 或 `UE_ADDR_ANY` 将选择第一个匹配的端点。此字段为必填。

`direction` 字段选择 USB 端点方向。值 `UE_DIR_ANY` 将选择第一个匹配的端点。其他有效值为 `UE_DIR_IN` 和 `UE_DIR_OUT`。`UE_DIR_IN` 和 `UE_DIR_OUT` 可以通过 `UE_DIR_SID` 进行二进制或运算，这意味着在 USB_MODE_DEVICE 情况下方向将被交换。注意，`UE_DIR_IN` 指的是 `IN` 令牌的数据传输方向，`UE_DIR_OUT` 指的是 `OUT` 令牌的数据传输方向。此字段为必填。

`interval` 字段选择中断间隔。此字段的值以毫秒为单位，与设备速度无关。根据端点类型，此字段具有不同含义：

**UE_INTERRUPT** `0` 使用基于端点描述符的默认中断间隔。其他值使用给定值作为轮询率。

**UE_ISOCHRONOUS** `0` 使用默认值。其他值被忽略。

**UE_BULK**

**UE_CONTROL** `0` 无传输预延迟。其他值在调用 `usbd_transfer_submit()` 启动硬件之前插入由此字段以毫秒为单位给定的延迟。注意：传输超时（如果有）在预延迟过后才启动！

`timeout` 字段（如果非零）将以毫秒为单位设置传输超时。如果 `timeout` 字段为零且传输类型为 ISOCHRONOUS，则使用 250ms 的超时。

`frames` 字段设置最大帧数。如果指定为零，将产生以下结果：

**UE_BULK** xfer->nframes = 1;

**UE_INTERRUPT** xfer->nframes = 1;

**UE_CONTROL** xfer->nframes = 2;

**UE_ISOCHRONOUS** 不允许。将导致错误。

`ep_index` 字段允许在多个端点匹配描述时提供一个数字，用于选择应使用哪个匹配的 `ep_index`。

`if_index` 字段允许选择传递给 `usbd_transfer_setup` 的 `ifaces` 数组参数中的哪个接口号用于设置给定的 USB 传输。

`flags` 字段类型为 `struct usb_xfer_flags`，允许设置 USB 传输的初始标志。有效标志有：

**1** 失败的 USB 传输使用 `usbd_transfer_stop()` 停止。

**2** 失败的 USB 传输执行成功传输。

**设备**侧模式 设置此标志将导致在传输开始之前向属于此传输的端点发送 STALL pid。传输在主机对 STALL 端点发出清除停滞命令时开始。此标志可在操作期间更改。

**主机**侧模式 设置此标志将导致在 USB 传输开始之前对端点执行清除停滞控制请求。

**force_short_xfer** 此标志强制最后传输的 USB 数据包为短包。短包的长度小于 `xfer->max_packet_size`，该值源自 `wMaxPacketSize`。此标志可在操作期间更改。

**short_xfer_ok** 此标志允许在传输完成时接收到的传输长度 `xfer->actlen` 小于 `xfer->sumlen`。此标志可在操作期间更改。

**short_frames_ok** 此标志允许接收多个短 USB 帧。此标志仅对 BULK 和 INTERRUPT 端点且接收到的帧数大于 1 时有效。此标志可在操作期间更改。

**pipe_bof** 此标志使失败的 USB 传输保持在 PIPE 队列首位，除非 `xfer->error` 等于 `USB_ERR_CANCELLED`。受影响的 PIPE 队列中的其他 USB 传输将不会启动，直到：此标志的目的是避免当多个传输排队在 USB 端点上执行且第一个执行的传输失败（例如需要清除停滞）时出现竞态。在此情况下，此标志用于防止后续 USB 传输在 USB 控制端点上执行清除停滞命令的同时被执行。此标志可在操作期间更改。"BOF" 是 "Block On Failure" 的缩写。注意：此标志应设置在所有使用可在用户态和内核之间共享的端点的 BULK 和 INTERRUPT USB 传输上。

**proxy_buffer** 设置此标志将使总缓冲区大小向上舍入到最近的原子硬件传输大小。任何 USB 传输的最大数据长度始终存储在 `xfer->max_data_length` 中。对于控制传输，USB 内核将为 8 字节的 SETUP 头分配额外空间。这 8 字节不计入 `xfer->max_data_length` 变量。此标志不能在操作期间更改。

**ext_buffer** 设置此标志将导致不分配数据缓冲区。相反，USB 客户端必须提供数据缓冲区。此标志不能在操作期间更改。

**manual_status** 设置此标志可防止 USB STATUS 阶段附加到 USB 控制传输的末尾。如果未传输控制数据，则必须清除此标志。否则将向 USB 回调返回错误。此标志对 USB 设备侧最有用。此标志可在操作期间更改。

**no_pipe_ok** 设置此标志将忽略 USB_ERR_NO_PIPE 错误。此标志不能在操作期间更改。

**stall_pipe** 如果在 USB 回调函数之外更改此标志，则必须使用 `usbd_xfer_set_stall()` 和 `usbd_transfer_clear_stall()` 函数！此标志在执行停滞或清除停滞后自动清除。

**pre_scale_frames** 如果设置此标志，则指定的帧数假定以毫秒而非帧为单位给出缓冲时间。在传输设置期间，frames 字段将使用端点的相应值进行预缩放，并舍入到大于零的最近帧数。此选项仅对 ISOCHRONOUS 传输有效。

`bufsize` 字段以字节为单位设置总缓冲区大小。如果此字段为零，将使用 `wMaxPacketSize`，如果传输类型为 ISOCHRONOUS 则乘以 `frames` 字段。这对于设置中断管道很有用。此字段为必填。

注意：对于控制传输，`bufsize` 包括请求结构的长度。

`callback` 指针设置 USB 回调。此字段为必填。

## USB LINUX 兼容层

`usb` 模块支持 Linux USB API。

## 参见

libusb(3), [usb(4)](../man4/usb.4.md), usbconfig(8)

## 标准

`usb` 模块符合 USB 2.0 标准。

## 历史

`usb` 模块受 Lennart Augustsson 最初编写的 NetBSD USB 栈启发。`usb` 模块由 Hans Petter Selasky <hselasky@FreeBSD.org> 编写。
