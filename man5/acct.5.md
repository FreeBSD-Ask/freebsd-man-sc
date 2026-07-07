# acct(5)

`acct` — 执行记账文件

## 名称

`acct`

## 概要

`#include <sys/types.h>`

`#include <sys/acct.h>`

## 描述

内核为所有进程维护以下 `acct` 信息结构。如果一个进程终止，且记账功能已启用，内核会调用 acct(2) 函数准备记录并将其追加到记账文件中。

```sh
#define AC_COMM_LEN 16
/*
 * 记账结构版本 3（当前版本）。
 * 第一个字节始终为零。
 * 时间单位为微秒。
 */
struct acctv3 {
	uint8_t  ac_zero;		/* 零标识新版本 */
	uint8_t  ac_version;		/* 记录版本号 */
	uint16_t ac_len;		/* 记录长度 */
	char	  ac_comm[AC_COMM_LEN];	/* 命令名 */
	float	  ac_utime;		/* 用户时间 */
	float	  ac_stime;		/* 系统时间 */
	float	  ac_etime;		/* 经过时间 */
	time_t	  ac_btime;		/* 开始时间 */
	uid_t	  ac_uid;		/* 用户 ID */
	gid_t	  ac_gid;		/* 组 ID */
	float	  ac_mem;		/* 平均内存使用量 */
	float	  ac_io;		/* IO 块计数 */
	__dev_t   ac_tty;		/* 控制终端 */
	uint16_t ac_len2;		/* 记录长度 */
	union {
		uint32_t  ac_align;	/* 强制与 v1 兼容的对齐 */
#define	AFORK	0x01			/* 已 fork 但未 exec */
/* ASU 不再受支持 */
#define	ASU	0x02			/* 使用了超级用户权限 */
#define	ACOMPAT	0x04			/* 使用了兼容模式 */
#define	ACORE	0x08			/* 转储了 core */
#define	AXSIG	0x10			/* 被信号杀死 */
#define ANVER	0x20			/* 新记录版本 */
		uint8_t  ac_flag;	/* 记账标志 */
	} ac_trailer;
#define ac_flagx ac_trailer.ac_flag
};
```

如果已终止的进程是由 execve(2) 创建的，已执行文件的名称（最多十个字符）保存在 `ac_comm` 字段中，其状态通过在 `ac_flag` 中设置以下一个或多个标志来保存：`AFORK`、`ACOMPAT`、`ACORE` 和 `AXSIG`。`ASU` 不再受支持。在上述结构中 `ANVER` 始终被设置。

## 参见

[lastcomm(1)](../man1/lastcomm.1.md), acct(2), execve(2), sa(8)

## 历史

`acct` 文件格式出现于 Version 7 AT&T UNIX。当前的记录格式于 2007 年 5 月引入。它与以前的格式向后兼容，以前的格式仍记录在

`#include <sys/acct.h>`

中，并由 [lastcomm(1)](../man1/lastcomm.1.md) 和 sa(8) 支持。
