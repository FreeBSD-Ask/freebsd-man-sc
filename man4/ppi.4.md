# ppi(4)

`ppi` — ppbus 并行“极客”端口的用户空间接口

## 名称

`ppi`

## 概要

`device ppi`

`次编号：单元号直接对应于 ppbus 编号。`

`#include <dev/ppbus/ppi.h>`

`#include <dev/ppbus/ppbconf.h>`

## 描述

`ppi` 驱动为用户应用程序提供了操纵并口状态的便捷手段，可轻松进行低速 I/O 操作，而不会带来使用 `/dev/io` 接口固有的安全问题。

## 编程接口

`ppi` 接口上的所有 I/O 都使用 Fn ioctl 调用执行。每个命令接受一个 Ft uint8_t 参数，传输一字节数据。以下命令可用：

**`STROBE`**
**`AUTOFEED`**
**`nINIT`**
**`SELECTIN`**
**`PCD`**

**`PPIGDATA , PPISDATA`** 获取和设置数据寄存器的内容。

**`PPIGSTATUS , PPISSTATUS`** 获取和设置状态寄存器的内容。

**`PPIGCTRL , PPISCTRL`** 获取和设置控制寄存器的内容。以下定义对应于此寄存器中的位。在控制寄存器中设置某位会驱动相应输出为低电平。

**`PPIGEPP , PPISEPP`** 获取和设置 EPP 控制寄存器的内容。

**`PPIGECR , PPISECR`** 获取和设置 ECP 控制寄存器的内容。

**`PPIGFIFO , PPISFIFO`** 读取和写入 ECP FIFO（仅 8 位操作）。

## 实例

要将值 0x5a 呈现到数据端口，驱动 STROBE 为低电平然后再为高电平，可使用以下代码片段：

	int		fd;
	uint8_t		val;
	val = 0x5a;
	ioctl(fd, PPISDATA, &val);
	ioctl(fd, PPIGCTRL, &val);
	val |= STROBE;
	ioctl(fd, PPISCTRL, &val);
	val &= ~STROBE;
	ioctl(fd, PPISCTRL, &val);

## 缺陷

信号的反相意义容易引起混淆。

Fn ioctl 接口较慢，并且（目前）无法将多个操作链接在一起。

用户应用程序所需的头文件未作为标准系统的一部分安装。
