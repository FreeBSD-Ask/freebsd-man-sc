# fs(5)

`fs` — 文件系统卷格式

## 名称

`fs`, `inode`

## 概要

`#include <sys/param.h>`

`#include <ufs/ffs/fs.h>`

`#include <sys/types.h>`

`#include <sys/lock.h>`

`#include <sys/extattr.h>`

`#include <sys/acl.h>`

`#include <ufs/ufs/quota.h>`

`#include <ufs/ufs/dinode.h>`

`#include <ufs/ufs/extattr.h>`

## 描述

文件

`#include <fs.h>`

和

`#include <inode.h>`

声明了若干结构、已定义的变量和宏，用于在随机访问设备（磁盘）上创建和管理文件系统对象的底层格式。

块大小和构成文件系统的块数是文件系统的参数。从 `BBLOCK` 开始、持续 `BBSIZE` 的扇区用于 disklabel 以及某些硬件的主引导和次引导程序。

实际文件系统从 `SBLOCK` 扇区开始，包含大小为 `SBLOCKSIZE` 的 *超级块*。以下结构描述了超级块，来自文件

`#include <ufs/ffs/fs.h>`

```sh
/*
 * FFS 文件系统的超级块。
 */
struct fs {
	int32_t	 fs_firstfield;	   /* 历史文件系统链表， */
	int32_t	 fs_unused_1;      /*     用于内存中的超级块 */
	int32_t	 fs_sblkno;        /* 超级块在文件系统中的偏移 */
	int32_t	 fs_cblkno;        /* 柱面块在文件系统中的偏移 */
	int32_t	 fs_iblkno;        /* inode 块在文件系统中的偏移 */
	int32_t	 fs_dblkno;        /* cg 之后首个数据块的偏移 */
	int32_t	 fs_old_cgoffset;  /* 柱面组在柱面中的偏移 */
	int32_t	 fs_old_cgmask;    /* 用于计算 mod fs_ntrak */
	int32_t  fs_old_time;      /* 最后写入时间 */
	int32_t	 fs_old_size;      /* 文件系统中的块数 */
	int32_t	 fs_old_dsize;     /* 文件系统中的数据块数 */
	int32_t	 fs_ncg;           /* 柱面组数量 */
	int32_t	 fs_bsize;         /* 文件系统中基本块的大小 */
	int32_t	 fs_fsize;         /* 文件系统中片段块的大小 */
	int32_t	 fs_frag;          /* 文件系统中一块的片段数 */
/* 这些是配置参数 */
	int32_t	 fs_minfree;       /* 最小空闲块百分比 */
	int32_t	 fs_old_rotdelay;  /* 最佳下一块的毫秒数 */
	int32_t	 fs_old_rps;       /* 每秒磁盘转速 */
/* 这些字段可从其他字段计算得出 */
	int32_t	 fs_bmask;         /* 块偏移的 ``blkoff'' 计算 */
	int32_t	 fs_fmask;         /* 片段偏移的 ``fragoff'' 计算 */
	int32_t	 fs_bshift;        /* 逻辑块号的 ``lblkno'' 计算 */
	int32_t	 fs_fshift;        /* 片段数的 ``numfrags'' 计算 */
/* 这些是配置参数 */
	int32_t	 fs_maxcontig;     /* 最大连续块数 */
	int32_t	 fs_maxbpg;        /* 每个柱面组的最大块数 */
/* 这些字段可从其他字段计算得出 */
	int32_t	 fs_fragshift;     /* 块到片段的位移 */
	int32_t	 fs_fsbtodb;       /* fsbtodb 和 dbtofsb 的位移常量 */
	int32_t	 fs_sbsize;        /* 超块的实际大小 */
	int32_t	 fs_spare1[2];     /* 旧的 fs_csmask */
	                           /* 旧的 fs_csshift */
	int32_t	 fs_nindir;        /* NINDIR 的值 */
	int32_t	 fs_inopb;         /* INOPB 的值 */
	int32_t	 fs_old_nspf;      /* NSPF 的值 */
/* 又一个配置参数 */
	int32_t	 fs_optim;         /* 优化偏好，见下文 */
	int32_t	 fs_old_npsect;    /* 每磁道扇区数（含备用） */
	int32_t	 fs_old_interleave; /* 硬件扇区交错 */
	int32_t	 fs_old_trackskew; /* 每磁道扇区 0 的偏斜 */
	int32_t	 fs_id[2];         /* 唯一的文件系统 ID */
/* 大小由柱面组数量及其大小决定 */
	int32_t	 fs_old_csaddr;	   /* 柱面组汇总区的块地址 */
	int32_t	 fs_cssize;        /* 柱面组汇总区的大小 */
	int32_t	 fs_cgsize;        /* 柱面组大小 */
	int32_t	 fs_spare2;        /* 旧的 fs_ntrak */
	int32_t	 fs_old_nsect;     /* 每磁道扇区数 */
	int32_t  fs_old_spc;       /* 每柱面扇区数 */
	int32_t	 fs_old_ncyl;      /* 文件系统中的柱面数 */
	int32_t	 fs_old_cpg;       /* 每组柱面数 */
	int32_t	 fs_ipg;           /* 每组 inode 数 */
	int32_t	 fs_fpg;           /* 每组块数 * fs_frag */
/* 此数据在崩溃后必须重新计算 */
	struct	csum fs_old_cstotal; /* 柱面汇总信息 */
/* 这些字段在挂载时清零 */
	int8_t   fs_fmod;          /* 超级块修改标志 */
	int8_t   fs_clean;         /* 文件系统干净标志 */
	int8_t 	 fs_ronly;         /* 只读挂载标志 */
	int8_t   fs_old_flags;     /* 旧的 FS_ 标志 */
	u_char	 fs_fsmnt[MAXMNTLEN]; /* 挂载点名称 */
	u_char	 fs_volname[MAXVOLLEN]; /* 卷名 */
	uint64_t fs_swuid;         /* 系统级 uid */
	int32_t  fs_pad;           /* 由于 fs_swuid 的对齐 */
/* 这些字段保留当前块分配信息 */
	int32_t	 fs_cgrotor;       /* 上次搜索的 cg */
	void 	*fs_ocsp[NOCSPTRS]; /* 填充；曾是 fs_cs 缓冲区列表 */
	uint8_t *fs_contigdirs;    /* 连续分配的目录数 */
	struct	csum *fs_csp;      /* fs_cs 的 cg 汇总信息缓冲区 */
	int32_t	*fs_maxcluster;    /* 每个柱面组的最大簇 */
	u_int	*fs_active;        /* 快照用于跟踪文件系统 */
	int32_t	 fs_old_cpc;       /* postbl 中每循环柱面数 */
	int32_t	 fs_maxbsize;      /* 允许的最大块因子 */
	int64_t	 fs_unrefs;        /* 未引用的 inode 数 */
	int64_t	 fs_sparecon64[16]; /* 旧的旋转块列表头 */
	int64_t	 fs_sblockloc;     /* 标准超级块的字节偏移 */
	struct	csum_total fs_cstotal;  /* 柱面汇总信息 */
	ufs_time_t fs_time;        /* 最后写入时间 */
	int64_t	 fs_size;          /* 文件系统中的块数 */
	int64_t	 fs_dsize;         /* 文件系统中的数据块数 */
	ufs2_daddr_t fs_csaddr;    /* 柱面组汇总区的块地址 */
	int64_t	 fs_pendingblocks; /* 正在释放的块数 */
	int32_t	 fs_pendinginodes; /* 正在释放的 inode 数 */
	int32_t	 fs_snapinum[FSMAXSNAP]; /* 快照 inode 号列表 */
	int32_t	 fs_avgfilesize;   /* 预期平均文件大小 */
	int32_t	 fs_avgfpdir;      /* 预期每目录文件数 */
	int32_t	 fs_save_cgsize;   /* 保存真实 cg 大小以使用 fs_bsize */
	int32_t	 fs_sparecon32[26]; /* 保留用于未来常量 */
	int32_t  fs_flags;         /* 见下文 FS_ 标志 */
	int32_t	 fs_contigsumsize; /* 簇汇总数组大小 */
	int32_t	 fs_maxsymlinklen; /* 内部符号链接的最大长度 */
	int32_t	 fs_old_inodefmt;  /* 磁盘上 inode 的格式 */
	uint64_t fs_maxfilesize;   /* 最大可表示的文件大小 */
	int64_t	 fs_qbmask;        /* 用于 64 位大小的 ~fs_bmask */
	int64_t	 fs_qfmask;        /* 用于 64 位大小的 ~fs_fmask */
	int32_t	 fs_state;         /* 验证 fs_clean 字段 */
	int32_t	 fs_old_postblformat; /* 位置布局表的格式 */
	int32_t	 fs_old_nrpos;     /* 旋转位置数 */
	int32_t	 fs_spare5[2];     /* 旧的 fs_postbloff */
	                           /* 旧的 fs_rotbloff */
	int32_t	 fs_magic;         /* 魔数 */
};
/*
 * 文件系统标识
 */
#define	FS_UFS1_MAGIC	0x011954    /* UFS1 快速文件系统魔数 */
#define	FS_UFS2_MAGIC	0x19540119  /* UFS2 快速文件系统魔数 */
#define	FS_OKAY		0x7c269d38  /* 超级块校验和 */
#define FS_42INODEFMT	-1      /* 4.2BSD inode 格式 */
#define FS_44INODEFMT	2       /* 4.4BSD inode 格式 */
/*
 * 优化偏好。
 */
#define FS_OPTTIME	0	/* 最小化分配时间 */
#define FS_OPTSPACE	1	/* 最小化磁盘碎片 */
```

每个磁盘驱动器包含若干文件系统。一个文件系统由若干柱面组组成。每个柱面组包含 inode 和数据。

文件系统由其超级块描述，超级块又描述了柱面组。超级块是关键数据，在每个柱面组中都有副本，以防灾难性损失。这是在文件系统创建时完成的，关键的超级块数据不会改变，因此除非发生灾难，否则无需进一步引用这些副本。

存储在 inode 中的地址能够寻址 “块” 的片段。最多 `MAXBSIZE` 大小的文件系统块可以选择性地分为 2、4 或 8 片，每片都可寻址；这些片段可以是 `DEV_BSIZE`，或 `DEV_BSIZE` 单位的某个倍数。

大文件完全由大数据块组成。为避免过度浪费磁盘空间，小文件的最后一个数据块仅按需要分配一个大块的若干片段。文件系统格式仅保留指向此类片段的单个指针，该片段是被分割的某个大块的一部分。此类片段的大小可从 inode 中的信息通过 Fn blksize fs ip lbn 宏确定。

文件系统在片段级别记录空间可用性；要确定块可用性，需检查对齐的片段。

根 inode 是文件系统的根。inode 0 不能用于正常用途，历史上坏块链接到 inode 1，因此根 inode 是 2（inode 1 不再用于此目的，但许多 dump 磁带做了这种假设，因此我们只能维持现状）。

`fs_minfree` 元素给出可接受的最低空闲文件系统块百分比。如果空闲列表低于此水平，只有超级用户才能继续分配块。如果认为不需要保留空闲块，`fs_minfree` 元素可设为 0，但如果文件系统运行超过 90% 满，将观察到严重的性能下降；因此 `fs_minfree` 的默认值为 8%。

根据经验，在 90% 负载下，块碎片和整体磁盘利用率之间的最佳折衷是碎片化为 8，因此默认片段大小为块大小的八分之一。

`fs_optim` 元素指定文件系统应尝试最小化分配块所花费的时间，还是应尝试最小化磁盘上的空间碎片。如果 fs_minfree 的值（见上文）小于 8%，则文件系统默认优化空间，以避免耗尽完整大小的块。如果 minfree 的值大于或等于 8%，碎片化不太可能成为问题，文件系统默认优化时间。

*柱面组相关限制：* 每个柱面跟踪不同旋转位置上块的可用性，以便以最小的旋转延迟布局连续块。在默认的 8 个区分旋转位置下，对于典型的 3600 rpm 驱动器，汇总信息的分辨率为 2ms。

`fs_old_rotdelay` 元素给出在同一柱面上启动另一次磁盘传输所需的最小毫秒数。它用于确定文件内磁盘块的旋转最佳布局；`fs_old_rotdelay` 的默认值为 2ms。

每个文件系统有静态分配的 inode 数。每 `NBPI` 字节的磁盘空间分配一个 inode。inode 分配策略极其保守。

`MINBSIZE` 是允许的最小块大小。在 `MINBSIZE` 为 4096 时，仅用两级间接即可创建大小为 2^32 的文件。`MINBSIZE` 必须足够大以容纳柱面组块，因此对（`struct cg`）的修改必须使其大小保持在 `MINBSIZE` 之内。注意，超级块的大小从不超过 `SBLOCKSIZE`。

文件系统挂载的路径名保存在 `fs_fsmnt` 中。`MAXMNTLEN` 定义了超级块中为此名称分配的空间量。每个文件系统的汇总信息量限制由 `MAXCSBUFS` 定义。对于 4096 字节的块大小，目前参数化为最多两百万个柱面。

每个柱面组的信息汇总在从第一个柱面组数据块分配的块中。除了超级块外，这些块还从 `fs_csaddr`（大小 `fs_cssize`）读入。

**注意：** Fn sizeof struct csum 必须是 2 的幂，Fn fs_cs 宏才能工作。

*文件系统的超级块：* 旋转布局表的大小受超级块大小为 `SBLOCKSIZE` 这一事实限制。这些表的大小与文件系统的块大小成 *反比*。当扇区大小不是 2 的幂时，表的大小会增加，因为这会增加旋转模式重复前所包含的柱面数（`fs_cpc`）。旋转布局表的大小由（`struct fs`）中剩余字节数推导得出。

每个柱面组的数据块数受限，因为柱面组最多为一个块。inode 和空闲块表在扣除柱面组结构（`struct cg`）的空间后必须能放入单个块中。

*inode：* inode 是 UNIX 文件系统中所有文件活动的焦点。每个活动文件、每个当前目录、每个被挂载的文件、文本文件和根目录都分配有唯一的 inode。inode 通过其设备/i-编号对“命名”。更多信息，参见包含文件

`#include <ufs/ufs/inode.h>`

外部属性的格式由 extattr 结构定义：

```sh
struct extattr {
	uint32_t ea_length;	    /* 此属性的长度 */
	uint8_t	ea_namespace;	    /* 此属性的命名空间 */
	uint8_t	ea_contentpadlen;   /* 属性末尾的填充字节数 */
	uint8_t	ea_namelength;	    /* 属性名的长度 */
	char	ea_name[1];	    /* 属性名（非 nul 结尾） */
	/* 如有填充，将属性内容对齐到 8 字节边界 */
	/* 扩展属性内容紧随其后 */
};
```

定义了若干宏来操作这些结构。每个宏接受一个指向 extattr 结构的指针。

**`EXTATTR_NEXT(eap)`** 返回指向 `eap` 之后下一个扩展属性的指针。

**`EXTATTR_CONTENT(eap)`** 返回指向 `eap` 所引用的扩展属性内容的指针。

**`EXTATTR_CONTENT_SIZE(eap)`** 返回 `eap` 所引用的扩展属性内容的大小。

以下代码标识一个 ACL：

```sh
	if (eap->ea_namespace == EXTATTR_NAMESPACE_SYSTEM &&
            eap->ea_namelength == sizeof(POSIX1E_ACL_ACCESS_EXTATTR_NAME) - 1 &&
	    strncmp(eap->ea_name, POSIX1E_ACL_ACCESS_EXTATTR_NAME,
             sizeof(POSIX1E_ACL_ACCESS_EXTATTR_NAME) - 1) == 0) {
		aclp = EXTATTR_CONTENT(eap);
		acllen = EXTATTR_CONTENT_SIZE(eap);
		...
	}
```

## 历史

名为 filsys 的超级块结构出现于 Version 6 AT&T UNIX。本手册所述的文件系统出现于 4.2BSD。
