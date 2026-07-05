# smb.4

`smb` — 系统管理总线（SMBus）通用 I/O 设备驱动

## 名称

`smb`

## 概要

`device smb`

## 描述

*smb* 字符设备驱动为任意 [smbus(4)](smbus.4.md) 实例提供通用 I/O。要控制 SMB 设备，请使用 **`/dev/smb?`** 配合下述 ioctl。这些 ioctl 命令中的任何一个都接受指向 `struct smbcmd` 的指针作为参数。

```sh
#include <sys/types.h>
struct smbcmd {
	u_char cmd;
	u_char reserved;
	u_short op;
	union {
		char    byte;
		char    buf[2];
		short   word;
	} wdata;
	union {
		char    byte;
		char    buf[2];
		short   word;
	} rdata;
	int  slave;
	char *wbuf;     /* 如果为 NULL 则使用 wdata */
	int  wcount;
	char *rbuf;     /* 如果为 NULL 则使用 rdata */
	int  rcount;
};
```

`slave` 字段始终使用，并提供 SMBus 从设备的地址。从设备地址在最高七位中指定（即"左对齐"）。从设备地址的最低位必须为零。

*QuickWrite* 不传输任何数据。它仅向总线发出带写入意图的设备地址。

*QuickRead* 不传输任何数据。它仅向总线发出带读取意图的设备地址。

*SendByte* 将 `cmd` 中提供的字节发送到设备。

*ReceiveByte* 从设备读取单个字节，返回到 `cmd` 中。

*WriteByte* 首先将 `cmd` 中的字节发送到设备，随后发送 `wdata.byte` 中给出的字节。

*WriteWord* 首先将 `cmd` 中的字节发送到设备，随后发送 `wdata.word` 中给出的字。注意，SMBus 字节序按定义为小端。

*ReadByte* 首先将 `cmd` 中的字节发送到设备，然后从设备读取一字节数据。返回数据存储在 `rdata.byte` 中。

*ReadWord* 首先将 `cmd` 中的字节发送到设备，然后从设备读取一字数据。返回数据存储在 `rdata.word` 中。

*ProcedureCall* 首先将 `cmd` 中的字节发送到设备，随后发送 `wdata.word` 中提供的字。然后从设备读取一字数据并返回到 `rdata.word` 中。

*BlockWrite* 首先将 `cmd` 中的字节发送到设备，然后发送 `wcount` 中的字节，随后是从 `wbuf` 指向的缓冲区取出的 `wcount` 字节数据。SMBus 规范要求单次块读取或写入命令传输的数据不超过 32 字节。此值可从常量 `SMB_MAXBLOCKSIZE` 读取。

*BlockRead* 首先将 `cmd` 中的字节发送到设备，然后读取设备将提供的数据字节计数，再读取那么多字节。计数返回到 `rcount` 中。数据返回到 `rbuf` 指向的缓冲区中。

| *Ioctl* | *Description* |
| ------- | ------------- |
| `SMB_QUICK_WRITE` | |
| `SMB_QUICK_READ` | |
| `SMB_SENDB` | |
| `SMB_RECVB` | |
| `SMB_WRITEB` | |
| `SMB_WRITEW` | |
| `SMB_READB` | |
| `SMB_READW` | |
| `SMB_PCALL` | |
| `SMB_BWRITE` | |
| `SMB_BREAD` | |

read(2) 和 write(2) 系统调用未由此驱动实现。

## 错误

ioctl(2) 命令可能引发以下驱动特定错误：

**[ENXIO]** 设备未响应选择。

**[EBUSY]** 设备仍在使用中。

**[ENODEV]** 设备不支持此操作（不应发生）。

**[EINVAL]** 一般参数错误。

**[EWOULDBLOCK]** SMBus 事务超时。

## 参见

ioctl(2), [smbus(4)](smbus.4.md)

## 历史

`smb` 手册页最早出现于 FreeBSD 3.0。

## 作者

本手册页由 Nicolas Souchu 编写，并由 Michael Gmelin <freebsd@grem.de> 扩展。
