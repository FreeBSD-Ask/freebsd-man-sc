# uftdi(4)

`uftdi` — Future Technology Devices International USB 串口 UART 驱动

## 名称

`uftdi`

## 概要

`device usb device ucom device uftdi`

在 rc.conf(5) 中：`kld_list="uftdi"`

在 sysctl.conf(5) 中：`hw.usb.uftdi.debug=1 hw.usb.uftdi.skip_jtag_interfaces=0`

## 描述

`uftdi` 驱动支持 FTDI USB 串口 UART 设备。若检测到相应硬件，该驱动会由 [devmatch(8)](../man8/devmatch.8.md) 自动加载。若要手动加载该驱动，请将其加入 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `kld_list`，或在运行时使用 [kldload(8)](../man8/kldload.8.md)。该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

通过此接口可使用 cu(1) 或 tip(1) 等应用程序进行呼出。

## 硬件

`uftdi` 驱动支持以下 USB 串口 UART 控制器：

- FTDI FT4232H
- FTDI FT232R
- FTDI FT230X
- FTDI FT2232H
- FTDI FT2232D
- FTDI FT2232C
- FTDI FT8U232BM
- FTDI FT8U232AM
- FTDI FT8U100AX

## SYSCTL 变量

以下设置可在 [loader(8)](../man8/loader.8.md) 提示符下输入，在 loader.conf(5)、[sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，或在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 更改：

**`hw.usb.uftdi.debug`** 启用调试消息，默认 `0`

**`hw.usb.uftdi.skip_jtag_interfaces`** 忽略 JTAG 接口，默认 `1`

## IOCTLS

许多受支持的芯片提供附加功能，例如位操作模式和用于串行总线仿真的 MPSSE 引擎。`uftdi` 驱动通过以下 ioctl(2) 调用提供对这些功能的访问，这些调用定义于

`#include <dev/usb/uftdiio.h>`

```sh
enum uftdi_bitmodes
{
	UFTDI_BITMODE_ASYNC = 0,
	UFTDI_BITMODE_MPSSE = 1,
	UFTDI_BITMODE_SYNC = 2,
	UFTDI_BITMODE_CPU_EMUL = 3,
	UFTDI_BITMODE_FAST_SERIAL = 4,
	UFTDI_BITMODE_CBUS = 5,
	UFTDI_BITMODE_NONE = 0xff,
};
struct uftdi_bitmode
{
	uint8_t mode;
	uint8_t iomask;
};
```

```sh
struct uftdi_eeio
{
	uint16_t offset;
	uint16_t length;
	uint16_t data[64];
};
```

**`UFTDIIOC_RESET_IO`** (`int`) 将通道重置为默认配置，清空 RX 和 TX FIFO。

**`UFTDIIOC_RESET_RX`** (`int`) 清空 RX FIFO。

**`UFTDIIOC_RESET_TX`** (`int`) 清空 TX FIFO。

**`UFTDIIOC_SET_BITMODE`** (`struct uftdi_bitmode`) 将通道置入 `mode` 指定的操作模式，并将 `iomask` 中为 1 的位对应的引脚设置为输出模式。`mode` 必须为 `uftdi_bitmodes` 值之一。将 `mode` 设置为 `UFTDI_BITMODE_NONE` 可使通道返回标准 UART 模式。FTDI 发布的手册和应用说明详细描述了这些模式。要使用大多数模式，首先将通道置入所需模式，然后通过 read(2) 和 write(2) 读写数据，依据模式不同，数据会反映引脚状态或被解释为 MPSSE 命令和参数。

**`UFTDIIOC_GET_BITMODE`** (`struct uftdi_bitmode`) 在 `mode` 成员中返回当前位操作模式，并在 `iomask` 成员中返回调用时 DBUS0..DBUS7 引脚的状态。无论芯片处于何种模式（包括 `UFTDI_BITMODE_NONE`（UART）模式），均可读取引脚状态。

**`UFTDIIOC_SET_ERROR_CHAR`** (`int`) 设置插入缓冲区以标记错误（如 FIFO 溢出）位置的字符。

**`UFTDIIOC_SET_EVENT_CHAR`** (`int`) 设置一个字符，使得即使 FIFO 未满，部分填满数据的 FIFO 也会立即返回。

**`UFTDIIOC_SET_LATENCY`** (`int`) 设置等待满 FIFO 的时间（单位为毫秒）。若超过此时间未收到新字符，则返回 FIFO 中的所有字符。

**`UFTDIIOC_GET_LATENCY`** (`int`) 获取延迟计时器的当前值。

**`UFTDIIOC_GET_HWREV`** (`int`) 获取硬件版本号。即 `usb_device_descriptor` 中的 `bcdDevice` 值。

**`UFTDIIOC_READ_EEPROM`** (`struct uftdi_eeio`) 从配置 eeprom 读取一个或多个字。FTDI 芯片以 16 位字为单位执行 eeprom I/O。调用前将 `offset` 和 `length` 设置为可被 2 整除的值，调用后 `data` 数组将包含从 eeprom 请求的值。FT232R 芯片具有内部 eeprom。其他 FTDI 芯片可选择外部串行 eeprom。eeprom 可包含 64、128 或 256 个字，具体取决于所用型号。读取或写入较大容量时可能需要多次调用。当不存在 eeprom 时，返回数据中的所有字均为 0xffff。擦除后的 eeprom 读取结果也为全 0xffff。

**`UFTDIIOC_WRITE_EEPROM`** (`struct uftdi_eeio`) 向配置 eeprom 写入一个或多个字。`uftdi_eeio` 值的说明与 `UFTDIIOC_READ_EEPROM` 相同。FTDI 芯片对 eeprom 执行盲写，即使不存在 eeprom 也会显示成功。为确保写入成功，必须回读并验证数据。写入前*无需*擦除。eeprom 中的任何位置均可在任何时候覆写。

**`UFTDIIOC_ERASE_EEPROM`** (`int`) 擦除整个 eeprom。这主要用于测试和调试，因为写入前无需擦除。为防止因调用错误的 ioctl 导致意外擦除，必须向此 ioctl 传递特殊值 `UFTDI_CONFIRM_ERASE` 作为参数。

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 对应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 对应的呼出初始状态和锁定状态设备

## 参见

cu(1), [tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`uftdi` 驱动出现于 FreeBSD 4.8，源自 NetBSD 1.5。
