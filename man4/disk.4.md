# disk(4)

`disk` — 通用磁盘接口

## 名称

`disk`

## 概要

`device cd`

## 描述

通用块设备 IOCTL

系统中所有块设备都应支持此处定义的这些磁盘 ioctl(2) 命令。此类信息中的大部分也可通过 geom(2) 属性获得。

## ioctl

以下 ioctl(2) 调用适用于磁盘驱动器，定义于

`#include <sys/disk.h>`

头文件中。

- 在重新引导之间保留，
- 在提供者分离/附加之间保留，
- 提供者的名称可能更改——ident 不会更改，
- ident 值不应基于磁盘上的元数据；换句话说，将整个数据从一块磁盘复制到另一块磁盘不应使另一块磁盘获得相同的 ident，
- 可能存在多个具有相同 ident 的提供者，但仅当它们指向完全相同的物理存储时才行，例如多路径就是这种情况，
- 对于消耗单个提供者并提供单个提供者的 GEOM 类（如 geli(8)），标识符应通过将该提供者的类名附加到底层提供者的 ident 来形成，
- ident 是以 NUL 终止的 ASCII 字符串（可打印），
- ident 是可选的，应用程序不能依赖其存在。

```sh
struct diocgattr_arg {
	char name[64];
	int len;
	union {
		char str[DISK_IDENT_SIZE];
		off_t off;
		int i;
		uint16_t u16;
	} value;
};
```

```sh
/*
 * kda_index 的哨兵值。
 *
 * 如果 kda_index 为 KDA_REMOVE_ALL，所有转储配置都将清除。
 *
 * 如果 kda_index 为 KDA_REMOVE_DEV，指定设备的所有转储配置都将清除。
 *
 * 如果 kda_index 为 KDA_REMOVE，仅从回退转储配置列表中移除
 * 给定设备的指定转储配置。
 *
 * 如果 kda_index 为 KDA_APPEND，转储配置将添加到所有现有
 * 转储配置之后。
 *
 * 否则，新配置将插入到回退转储列表的索引
 * 'kda_index' 处。
 */
#define	KDA_REMOVE		UINT8_MAX
#define	KDA_REMOVE_ALL		(UINT8_MAX - 1)
#define	KDA_REMOVE_DEV		(UINT8_MAX - 2)
#define	KDA_APPEND		(UINT8_MAX - 3)
struct diocskerneldump_arg {
	uint8_t		 kda_index;
	uint8_t		 kda_compression;
	uint8_t		 kda_encryption;
	uint8_t		 kda_key[KERNELDUMP_KEY_MAX_SIZE];
	uint32_t	 kda_encryptedkeysize;
	uint8_t		*kda_encryptedkey;
	char		 kda_iface[IFNAMSIZ];
	union kd_ip	 kda_server;
	union kd_ip	 kda_client;
	union kd_ip	 kda_gateway;
	uint8_t		 kda_af;
};
```

**`DIOCGSECTORSIZE`** (`u_int`) 获取设备的扇区或块大小，单位为字节。扇区大小是可从此设备传输的最小数据单位。通常是 2 的幂，但也可能不是（例如 CDROM 音频）。对块设备的操作（如 lseek(2)、read(2) 和 write(2)）只能在此大小整数倍的文件偏移处执行。

**`DIOCGMEDIASIZE`** (`off_t`) 获取整个设备的大小，单位为字节。这应是扇区大小的倍数。

**`DIOCGFWSECTORS`** (`u_int`) 返回固件对每磁道扇区数的认识。此值主要用于与各种设计不当的磁盘标签格式兼容。仅在绝对需要时使用此值。其解释和使用很大程度上已过时。

**`DIOCGFWHEADS`** (`u_int`) 返回固件对每柱面磁头数的认识。此值主要用于与各种设计不当的磁盘标签格式兼容。仅在绝对需要时使用此值。其解释和使用很大程度上已过时。

**`DIOCGFLUSH`** 刷新设备的写缓存。

**`DIOCGDELETE`** (`off_t[2]`) 将设备上的数据标记为未使用。第一个元素是开始删除的偏移量。第二个元素是要删除的长度。提供者可使用此信息释放存储或通知存储设备内容可丢弃。

**`DIOCGIDENT`** (`char[DISK_IDENT_SIZE]`) 获取此提供者的 ident。ident 是此提供者的唯一且固定的标识符。ident 的属性如下：

**`DIOCGPROVIDERNAME`** (`char[MAXPATHLEN]`) 将设备的提供者名称存储到缓冲区中。缓冲区必须至少有 MAXPATHLEN 字节长。

**`DIOCGSTRIPESIZE`** (`off_t`) 获取设备最佳访问块的大小，单位为字节。这应是扇区大小的倍数。

**`DIOCGSTRIPEOFFSET`** (`off_t`) 获取第一个设备最佳访问块的偏移量，单位为字节。这应是扇区大小的倍数。

**`DIOCGPHYSPATH`** (`char[MAXPATHLEN]`) 获取定义给定提供者物理路径的字符串。此属性具有与 ident 类似的规则，但其目的是唯一标识设备的物理位置，而非该位置的当前占用者。缓冲区必须至少有 MAXPATHLEN 字节长。

**`DIOCGATTR`** (`struct diocgattr_arg`) 从提供者获取 geom 属性。返回数据的格式特定于属性。

**`DIOCZONECMD`** (`struct disk_zone_arg`) 发送磁盘区域命令。

**`DIOCSKERNELDUMP`** (`struct diocskerneldump_arg`) 为内核核心转储启用/禁用该设备。

**`DIOCGKERNELDUMP`** (`struct diocskerneldump_arg`) 获取给定索引的当前内核网络转储配置详情。

## 历史

本手册页由 M Warner Losh <imp@FreeBSD.org> 编写，内容主要源自

`#include <sys/disk.h>`
