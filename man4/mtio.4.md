# mtio(4)

`mtio` — FreeBSD 磁带接口

## 名称

`mtio`

## 描述

名为 **`/dev/[en]sa*`** 的特殊文件指向可连接到系统的 SCSI 磁带驱动器。**`/dev/sa*.ctl`** 是控制设备，可用于向 SCSI 磁带驱动程序发出 ioctl，以设置需要在磁带卸载之后仍然保留的参数。

回绕设备在最后一次请求的读、写或寻道完成，或到达磁带末尾时，会自动回绕。不回绕设备的名称前会加上字母 `n`。弹出设备的名称前会加上字母 `e`。

磁带可以用固定长度记录或可变长度记录写入。更多信息请参见 [sa(4)](sa.4.md)。两个文件标记表示磁带结束，一个文件标记表示磁带文件结束。如果磁带不回绕，磁头将停在两个磁带标记之间，下一次写入将覆盖第二个文件结束标记。

所有磁带设备都可以使用 mt(1) 命令进行操作。

原始磁带上提供了若干 ioctl(2) 操作。以下定义来自

`#include <sys/mtio.h>`

```sh
#ifndef	_SYS_MTIO_H_
#define	_SYS_MTIO_H_
#ifndef _KERNEL
#include <sys/types.h>
#endif
#include <sys/ioccom.h>
/*
 * 磁带 io 控制命令的结构和定义
 */
/* MTIOCTOP 的结构 - 磁带操作命令 */
struct mtop {
	short	mt_op;		/* 操作定义如下 */
	int32_t	mt_count;	/* 操作的次数 */
};
/* 操作 */
#define MTWEOF		0	/* 写入文件结束记录 */
#define MTFSF		1	/* 向前跳过文件 */
#define MTBSF		2	/* 向后跳过文件 */
#define MTFSR		3	/* 向前跳过记录 */
#define MTBSR		4	/* 向后跳过记录 */
#define MTREW		5	/* 回绕 */
#define MTOFFL		6	/* 回绕并使驱动器脱机 */
#define MTNOP		7	/* 无操作，仅设置状态 */
#define MTCACHE		8	/* 启用控制器缓存 */
#define MTNOCACHE	9	/* 禁用控制器缓存 */
#if defined(__FreeBSD__)
/* 设置设备的块大小。如果设备是可变大小设备		*/
/* 非零参数会将设备更改为固定块大小设备，	*/
/* 块大小设置为传入的参数值。	*/
/* 将块大小重置为 0 会将设备恢复为可变块大小设备。 */
#define MTSETBSIZ	10
/* 设置设备的密度值。仅对打开的模式设置值。 */
#define MTSETDNSTY	11
#define MTERASE		12	/* 擦除至 EOM */
#define MTEOD		13	/* 跳至 EOM */
#define MTCOMP		14	/* 选择压缩模式 0=关，1=默认 */
#define MTRETENS	15	/* 重新张紧磁带 */
#define MTWSS		16	/* 写入 setmark */
#define MTFSS		17	/* 向前跳过 setmark */
#define MTBSS		18	/* 向后跳过 setmark */
#define MTLOAD		19	/* 在驱动器中加载磁带 */
#define MTWEOFI		20	/* 写入文件结束记录但不等待 */
#define MT_COMP_ENABLE		0xffffffff
#define MT_COMP_DISABLED	0xfffffffe
#define MT_COMP_UNSUPP		0xfffffffd
/*
 * mt_dsreg 中表示设备状态的值
 */
#define	MTIO_DSREG_NIL	0	/* 未知 */
#define	MTIO_DSREG_REST	1	/* 空闲 */
#define	MTIO_DSREG_RBSY	2	/* 与磁带通信（但无运动） */
#define	MTIO_DSREG_WR	20	/* 写入中 */
#define	MTIO_DSREG_FMK	21	/* 写入文件标记中 */
#define	MTIO_DSREG_ZER	22	/* 擦除中 */
#define	MTIO_DSREG_RD	30	/* 读取中 */
#define	MTIO_DSREG_FWD	40	/* 向前定位 */
#define	MTIO_DSREG_REV	41	/* 向后定位 */
#define	MTIO_DSREG_POS	42	/* 硬件定位（方向未知） */
#define	MTIO_DSREG_REW	43	/* 回绕中 */
#define	MTIO_DSREG_TEN	44	/* 重新张紧中 */
#define	MTIO_DSREG_UNL	45	/* 卸载中 */
#define	MTIO_DSREG_LD	46	/* 加载中 */
#endif	/* __FreeBSD__ */
/* MTIOCGET 的结构 - 磁带获取状态命令 */
struct mtget {
	short	mt_type;	/* 磁带设备类型 */
/* 以下两个寄存器严重依赖于设备 */
	short	mt_dsreg;	/* “驱动器状态”寄存器 */
	short	mt_erreg;	/* “错误”寄存器 */
/* 设备相关寄存器结束 */
	/*
	 * 注意，残留计数虽然会维护，但可能
	 * 毫无意义，因为残留大小可能（极大地）
	 * 超过 32K 字节。使用 MTIOCERRSTAT ioctl 获取
	 * 更准确的计数。
	 */
	short	mt_resid;	/* 残留计数 */
#if defined (__FreeBSD__)
	int32_t mt_blksiz;	/* 当前操作的块大小 */
	int32_t mt_density;	/* 当前操作的密度 */
	uint32_t mt_comp;	/* 当前操作的压缩 */
	int32_t mt_blksiz0;	/* 模式 0 的块大小 */
	int32_t mt_blksiz1;	/* 模式 1 的块大小 */
	int32_t mt_blksiz2;	/* 模式 2 的块大小 */
	int32_t mt_blksiz3;	/* 模式 3 的块大小 */
	int32_t mt_density0;	/* 模式 0 的密度 */
	int32_t mt_density1;	/* 模式 1 的密度 */
	int32_t mt_density2;	/* 模式 2 的密度 */
	int32_t mt_density3;	/* 模式 3 的密度 */
/* 以下尚未实现 */
	uint32_t mt_comp0;	/* 模式 0 的压缩类型 */
	uint32_t mt_comp1;	/* 模式 1 的压缩类型 */
	uint32_t mt_comp2;	/* 模式 2 的压缩类型 */
	uint32_t mt_comp3;	/* 模式 3 的压缩类型 */
/* 尚未实现结束 */
#endif
	int32_t	mt_fileno;	/* 当前位置的相对文件号 */
	int32_t	mt_blkno;	/* 当前位置的相对块号 */
};
/* MTIOCERRSTAT 的结构 - 磁带获取错误状态命令 */
/* 目前仅支持 SCSI 磁带 */
struct scsi_tape_errors {
	/*
	 * 这些是这些操作中注意到 SCSI Check Condition 的
	 * 最后一个命令所锁定的值。发出
	 * MTIOCERRSTAT 的行为会解除锁定并清除它们。
	 */
	uint8_t io_sense[32];	/* 最后一次数据 I/O 的检测数据 */
	int32_t io_resid;	/* 最后一次数据 I/O 的残留计数 */
	uint8_t io_cdb[16];	/* 引起最后一次数据检测的命令 */
	uint8_t ctl_sense[32];	/* 最后一次控制 I/O 的检测数据 */
	int32_t ctl_resid;	/* 最后一次控制 I/O 的残留计数 */
	uint8_t ctl_cdb[16];	/* 引起最后一次控制检测的命令 */
	/*
	 * 这些是读写累积错误计数器。
	 * （如何重置累积错误计数器尚未定义。）
	 * （尚未实现，但为它们预留了空间）
	 */
	struct {
		uint32_t retries;	/* 执行的总重试次数 */
		uint32_t corrected;	/* 执行的总纠正次数 */
		uint32_t processed;	/* 成功的总纠正次数 */
		uint32_t failures;	/* 失败的总纠正/重试次数 */
		uint64_t nbytes;	/* 处理的总字节数 */
	} wterr, rderr;
};
union mterrstat {
	struct scsi_tape_errors scsi_errstat;
	char _reserved_padding[256];
};
struct mtrblim {
	uint32_t granularity;
	uint32_t min_block_length;
	uint32_t max_block_length;
};
typedef enum {
	MT_LOCATE_DEST_OBJECT	= 0x00,
	MT_LOCATE_DEST_FILE	= 0x01,
	MT_LOCATE_DEST_SET	= 0x02,
	MT_LOCATE_DEST_EOD	= 0x03
} mt_locate_dest_type;
typedef enum {
	MT_LOCATE_BAM_IMPLICIT	= 0x00,
	MT_LOCATE_BAM_EXPLICIT	= 0x01
} mt_locate_bam;
typedef enum {
	MT_LOCATE_FLAG_IMMED		= 0x01,
	MT_LOCATE_FLAG_CHANGE_PART	= 0x02
} mt_locate_flags;
struct mtlocate {
	mt_locate_flags		flags;
	mt_locate_dest_type 	dest_type;
	mt_locate_bam		block_address_mode;
	int64_t			partition;
	uint64_t		logical_id;
	uint8_t			reserved[64];
};
typedef enum {
	MT_EXT_GET_NONE,
	MT_EXT_GET_OK,
	MT_EXT_GET_NEED_MORE_SPACE,
	MT_EXT_GET_ERROR
} mt_ext_get_status;
struct mtextget {
	uint32_t		alloc_len;
	char			*status_xml;
	uint32_t		fill_len;
	mt_ext_get_status	status;
	char			error_str[128];
	uint8_t			reserved[64];
};
#define	MT_EXT_GET_ROOT_NAME		"mtextget"
#define	MT_DENSITY_ROOT_NAME		"mtdensity"
#define	MT_MEDIA_DENSITY_NAME		"media_density"
#define	MT_DENSITY_REPORT_NAME		"density_report"
#define	MT_MEDIUM_TYPE_REPORT_NAME	"medium_type_report"
#define	MT_MEDIA_REPORT_NAME		"media_report"
#define	MT_DENSITY_ENTRY_NAME		"density_entry"
#define	MT_DENS_WRITE_OK		0x80
#define	MT_DENS_DUP			0x40
#define	MT_DENS_DEFLT			0x20
#define	MT_PARAM_FIXED_STR_LEN	32
union mt_param_value {
	int64_t		value_signed;
	uint64_t	value_unsigned;
	char		*value_var_str;
	char		value_fixed_str[MT_PARAM_FIXED_STR_LEN];
	uint8_t		reserved[64];
};
typedef enum {
	MT_PARAM_SET_NONE,
	MT_PARAM_SET_SIGNED,
	MT_PARAM_SET_UNSIGNED,
	MT_PARAM_SET_VAR_STR,
	MT_PARAM_SET_FIXED_STR
} mt_param_set_type;
typedef enum {
	MT_PARAM_STATUS_NONE,
	MT_PARAM_STATUS_OK,
	MT_PARAM_STATUS_ERROR
} mt_param_set_status;
#define	MT_PARAM_VALUE_NAME_LEN	64
struct mtparamset {
	char			value_name[MT_PARAM_VALUE_NAME_LEN];
	mt_param_set_type	value_type;
	int			value_len;
	union mt_param_value	value;
	mt_param_set_status	status;
	char			error_str[128];
};
#define	MT_PARAM_ROOT_NAME	"mtparamget"
#define	MT_PROTECTION_NAME	"protection"
/*
 * 设置参数列表。
 */
struct mtsetlist {
	int num_params;
	int param_len;
	struct mtparamset *params;
};
/*
 * mt_type 字节的常量。对于与所列类型兼容的
 * 控制器，这些常量是相同的。
 */
#define	MT_ISTS		0x01		/* TS-11 */
#define	MT_ISHT		0x02		/* TM03 Massbus: TE16, TU45, TU77 */
#define	MT_ISTM		0x03		/* TM11/TE10 Unibus */
#define	MT_ISMT		0x04		/* TM78/TU78 Massbus */
#define	MT_ISUT		0x05		/* SI TU-45 emulation on Unibus */
#define	MT_ISCPC	0x06		/* SUN */
#define	MT_ISAR		0x07		/* SUN */
#define	MT_ISTMSCP	0x08		/* DEC TMSCP 协议 (TU81, TK50) */
#define MT_ISCY		0x09		/* CCI Cipher */
#define MT_ISCT		0x0a		/* HP 1/4 磁带 */
#define MT_ISFHP	0x0b		/* HP 7980 1/2 磁带 */
#define MT_ISEXABYTE	0x0c		/* Exabyte */
#define MT_ISEXA8200	0x0c		/* Exabyte EXB-8200 */
#define MT_ISEXA8500	0x0d		/* Exabyte EXB-8500 */
#define MT_ISVIPER1	0x0e		/* Archive Viper-150 */
#define MT_ISPYTHON	0x0f		/* Archive Python (DAT) */
#define MT_ISHPDAT	0x10		/* HP 35450A DAT 驱动器 */
#define MT_ISMFOUR	0x11		/* M4 Data 1/2 9 磁道驱动器 */
#define MT_ISTK50	0x12		/* DEC SCSI TK50 */
#define MT_ISMT02	0x13		/* Emulex MT02 SCSI 磁带控制器 */
/* 磁带 io 控制命令 */
#define	MTIOCTOP	_IOW('m', 1, struct mtop)	/* 执行磁带操作 */
#define	MTIOCGET	_IOR('m', 2, struct mtget)	/* 获取磁带状态 */
/* 这两个似乎在任何地方都未使用 */
#define MTIOCIEOT	_IO('m', 3)			/* 忽略 EOT 错误 */
#define MTIOCEEOT	_IO('m', 4)			/* 启用 EOT 错误 */
/*
 * 当更多支持完整 32 字节 type 2 结构的 SCSI-3 SSC（流设备）
 * 设备出现时，我们将不得不重新考虑这些 ioctl，
 * 以支持它们引入的所有实体（64 位块、逻辑文件记录号等）。
 */
#define	MTIOCRDSPOS	_IOR('m', 5, uint32_t)	/* 获取逻辑块地址 */
#define	MTIOCRDHPOS	_IOR('m', 6, uint32_t)	/* 获取硬件块地址 */
#define	MTIOCSLOCATE	_IOW('m', 5, uint32_t)	/* 寻道至逻辑块地址 */
#define	MTIOCHLOCATE	_IOW('m', 6, uint32_t)	/* 寻道至硬件块地址 */
#define	MTIOCERRSTAT	_IOR('m', 7, union mterrstat)	/* 获取磁带错误 */
/*
 * 设置 EOT 模型 - 参数是用于结束磁带的文件标记数。
 * 注意，并非所有可能的值都会被接受。
 */
#define	MTIOCSETEOTMODEL	_IOW('m', 8, uint32_t)
/* 获取当前 EOT 模型 */
#define	MTIOCGETEOTMODEL	_IOR('m', 8, uint32_t)
#define	MTIOCRBLIM	_IOR('m', 9, struct mtrblim)    /* 获取块限制 */
#define	MTIOCEXTLOCATE	_IOW('m', 10, struct mtlocate)  /* 定位 */
#define	MTIOCEXTGET	_IOWR('m', 11, struct mtextget) /* 获取磁带状态 */
#define	MTIOCPARAMGET	_IOWR('m', 12, struct mtextget) /* 获取磁带参数 */
#define	MTIOCPARAMSET	_IOWR('m', 13, struct mtparamset) /* 设置磁带参数 */
#define	MTIOCSETLIST	_IOWR('m', 14, struct mtsetlist) /* 设置 N 个参数 */
#ifndef _KERNEL
#define	DEFTAPE	"/dev/nsa0"
#endif
#endif /* !_SYS_MTIO_H_ */
```

## 文件

**`/dev/[en]sa*`**

## 参见

mt(1), [tar(1)](../man1/tar.1.md), [sa(4)](sa.4.md)

## 历史

`mtio` 手册页出现于 4.2BSD。一个 i386 版本首次出现于 FreeBSD 2.2。
