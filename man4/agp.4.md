# agp.4

`agp` — 加速图形端口（AGP）的通用接口

## 名称

`agp`

## 概要

`device agp`

## 弃用通知

`agp` 驱动计划在 FreeBSD 16.0 中移除。

## 描述

`agp` 驱动提供控制以下设备的统一、抽象方法：

**Ali:** M1541、M1621 和 M1671 host 到 AGP 桥
**AMD:** 751、761 和 762 host 到 AGP 桥
**ATI:** RS100、RS200、RS250 和 RS300 AGP 桥
**Intel:** i820、i840、i845、i850 和 i860 host 到 AGP 桥
**Intel:** i810、i810-DC100、i810E、i815、830M、845G、845M、852GM、852GME、855GM、855GME、865G、915G 和 915GM SVGA 控制器
**Intel:** 82443BX、82443GX、82443LX、82815、82820、82830、82840、82845、82845G、82850、82855、82855GM、82860、82865、82875P、E7205 和 E7505 host 到 AGP 桥
**NVIDIA:** nForce 和 nForce2 AGP 控制器
**SiS:** 530、540、550、620、630、645、645DX、648、650、651、655、661、730、735、740、741、745、746、760 和 5591 host 到 AGP 桥
**VIA:** 3296、82C597、82C598、82C691、82C694X、82C8363、8235、8237、8361、8367、8371、8377、8501、8601、862x、8633、8653、8703、8753、8754、8763、8783、KT880、PM800、PM880、PN800、PN880、PT880、XM266 和 XN266 host 到 PCI 桥

`agp` 最常见的应用是在 Intel i81x 控制器上运行 X(7)（`ports/x11/xorg-docs`）。

## IOCTL

可在 **`/dev/agpgart`** 上执行以下 ioctl(2) 操作，它们定义于

`#include <sys/agpio.h>`

```sh
typedef struct _agp_info {
	agp_version version;  /* 驱动版本        */
	uint32_t bridge_id;   /* 桥厂商/设备         */
	uint32_t agp_mode;    /* 桥模式信息          */
	off_t aper_base;      /* 孔径基址             */
	size_t aper_size;     /* 孔径大小             */
	size_t pg_total;      /* 最大页数（交换 + 系统）    */
	size_t pg_system;     /* 最大页数（系统）           */
	size_t pg_used;       /* 当前已用页数           */
} agp_info;
```

```sh
typedef struct _agp_setup {
	uint32_t agp_mode;    /* 桥模式信息 */
} agp_setup;
```

`#include <sys/agpio.h>`

```sh
typedef struct _agp_allocate {
	int key;              /* 分配标签            */
	size_t pg_count;      /* 页数              */
	uint32_t type;        /* 0 == 普通，其他由设备定义   */
	uint32_t physical;    /* 设备专用（某些设备
			       * 需要 gatt 表背后实际页面的
			       * 物理地址）                       */
} agp_allocate;
```

```sh
typedef struct _agp_bind {
	int key;         /* 分配标签            */
	off_t pg_start;  /* 起始填充页    */
} agp_bind;
```

```sh
typedef struct _agp_unbind {
	int key;                /* 分配标签         */
	uint32_t priority;      /* 换出优先级   */
} agp_unbind;
```

**`AGPIOC_INFO`** 返回 `agp` 系统的状态。结果为指向以下结构的指针：

**`AGPIOC_ACQUIRE`** 为此客户端获取 AGP 芯片组的控制权。如果 AGP 芯片组已被另一客户端获取，返回 Er EBUSY。

**`AGPIOC_RELEASE`** 释放对 AGP 芯片组的控制。这不会取消绑定或释放任何已分配的内存，如有必要由客户端负责处理。

**`AGPIOC_SETUP`** 以相关模式启用 AGP 硬件。此 ioctl(2) 接受以下结构：模式位定义于

**`AGPIOC_ALLOCATE`** 分配适合映射到 AGP 孔径的物理内存。此 ioctl(2) 接受以下结构：返回已分配内存的句柄。

**`AGPIOC_DEALLOCATE`** 释放与传入句柄关联的先前分配的内存。

**`AGPIOC_BIND`** 将已分配内存绑定到 AGP 孔径的给定偏移处。如果内存已绑定或偏移不在 AGP 页边界，返回 Er EINVAL。此 ioctl(2) 接受以下结构：分配标签是 `AGPIOC_ALLOCATE` 返回的句柄。

**`AGPIOC_UNBIND`** 从 AGP 孔径取消绑定内存。如果内存未绑定，返回 Er EINVAL。此 ioctl(2) 接受以下结构：

## 文件

**`/dev/agpgart`** AGP 设备节点。

## 参见

X(7) (`ports/x11/xorg`)

## 历史

`agp` 驱动首次出现于 FreeBSD 4.1。
