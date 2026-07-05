# iic.4

`iic` — I2C 通用 I/O 设备驱动

## 名称

`iic`

## 概要

`device iic`

`#include <dev/iicbus/iic.h>`

## 描述

`iic` 设备驱动为任何 [iicbus(4)](iicbus.4.md) 实例提供通用 I/O。要控制 I2C 设备，可使用 `/dev/iic?` 配合以下 ioctl：

**`I2CSTART`** (`struct iiccmd`) 向总线上的 `slave` 元素指定的从设备发送起始条件。`slave` 元素由 7 位地址和读/写位组成（即 7 位地址 << 1 | r/w）。当读/写位置位时启动读操作，清零时启动写操作。所有其他元素被忽略。如果成功，文件描述符将获得底层 iicbus 实例的独占所有权。

**`I2CRPTSTART`** (`struct iiccmd`) 向总线上 `slave` 元素指定的从设备发送重复起始条件。从设备地址应与 `I2CSTART` 中一样指定。所有其他元素被忽略。在同一文件描述符上必须先前已发出 `I2CSTART`。

**`I2CSTOP`** 不传参数。向总线发送停止条件。如果先前在文件描述符上发出过 `I2CSTART`，则终止当前事务并释放底层 iicbus 实例的独占所有权。否则，不执行任何操作。

**`I2CRSTCARD`** (`struct iiccmd`) 复位总线。参数被完全忽略。此命令不要求在同一文件描述符上先前发出过 `I2CSTART`。如果先前已发出，则释放底层 iicbus 实例的独占所有权。

**`I2CWRITE`** (`struct iiccmd`) 向 [iicbus(4)](iicbus.4.md) 写入数据。总线必须已通过同一文件描述符上的先前 `I2CSTART` 启动。`slave` 元素被忽略。`count` 元素为要写入的字节数。`last` 元素是布尔标志。如果后续还有读命令，则必须为零；如果是最后一条命令，则为非零。`buf` 元素是指向要写入总线的数据的指针。

**`I2CREAD`** (`struct iiccmd`) 从 [iicbus(4)](iicbus.4.md) 读取数据。总线必须已通过同一文件描述符上的先前 `I2CSTART` 启动。`slave` 元素被忽略。`count` 元素为要读取的字节数。`last` 元素是布尔标志。如果后续还有读命令，则必须为零；如果是最后一条命令，则为非零。`buf` 元素是指向存储从总线读取数据的指针。总线上的短读取会产生未定义的结果。

**`I2CRDWR`** (`struct iic_rdwr_data`) 通用读/写接口。允许向总线上的任意数量设备发送任意数量的命令。在同一文件描述符上发出 `I2CRDWR` 之前，必须通过 `I2CSTOP` 或 `I2CRSTCARD` 终止先前由 `I2CSTART` 启动的任何事务。如果在 `flags` 中设置了 `IIC_M_RD`，则指定为读传输。否则为写传输。`slave` 元素指定传输的带读/写位的 7 位地址。读/写位将由 iicbus 栈根据指定的传输操作处理。`len` 元素是 (`struct iic_rdwr_data`) 中编码的 (`struct iic_msg`) 消息数量。`buf` 元素是该数据的缓冲区。此 ioctl 旨在与 Linux 兼容。

**`I2CSADDR`** (`uint8_t`) 将指定地址与文件描述符关联，供后续 read(2) 或 write(2) 调用使用。参数为 8 位地址（即 7 位地址 << 1）。最低位的读/写位被忽略。任何后续的读或写操作都会根据需要置位或清零该位。

以下数据结构定义于

`#include <dev/iicbus/iic.h>`

并已在上面引用：

```sh
struct iiccmd {
	u_char slave;
	int count;
	int last;
	char *buf;
};
/* Designed to be compatible with linux's struct i2c_msg */
struct iic_msg
{
	uint16_t	slave;
	uint16_t	flags;
#define	IIC_M_WR	0	/* Fake flag for write */
#define	IIC_M_RD	0x0001	/* read vs write */
#define	IIC_M_NOSTOP	0x0002	/* do not send a I2C stop after message */
#define	IIC_M_NOSTART	0x0004	/* do not send a I2C start before message */
	uint16_t	len;	/* msg length */
	uint8_t *	buf;
};
struct iic_rdwr_data {
	struct iic_msg *msgs;
	uint32_t nmsgs;
};
```

也可以使用 read(2) 或 write(2)，此时 I2C 起始/停止握手由 [iicbus(4)](iicbus.4.md) 管理。用于读/写操作的地址是传递给打开的 `/dev/iic?` 文件描述符上最近一次 `I2CSTART` ioctl(2) 或 `I2CSADDR` ioctl(2) 的地址。关闭文件描述符会清除先前 `I2CSTART` 或 `I2CSADDR` 建立的任何寻址状态，停止由尚未终止的 `I2CSTART` 建立的任何事务，并释放 iicbus 所有权。由于寻址状态以每个文件描述符为基础存储，因此允许在同一 `/dev/iic?` 设备上同时打开多个文件描述符。这些描述符上的并发事务通过向底层 iicbus 实例发出的独占所有权请求进行同步。

## 参见

ioctl(2), read(2), write(2), [iicbus(4)](iicbus.4.md)

## 历史

`iic` 手册页最早出现于 FreeBSD 3.0。

## 作者

本手册页由 Nicolas Souchu 和 M. Warner Losh 编写。
