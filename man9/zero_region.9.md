# zero\_region.9

`zero_region` — 预填充为零的只读区域

## 名称

`zero_region` — 预填充为零的只读区域

## 概要

```c
#include <sys/param.h>
#include <sys/systm.h>
#include <vm/vm_param.h>

extern const void *zero_region;
```

## 描述

全局变量 `zero_region` 指向一个预填充为零的只读区域。该区域的大小由 `ZERO_REGION_SIZE` 宏指定。

## 实现说明

`zero_region` 所指向的区域被多次映射到同一个页面。

## 实例

```c
/*
 * 该函数将零写入 vnode 的偏移 0 处，
 * 长度为 ZERO_REGION_SIZE。
 */
static int
write_example(struct vnode *vp)
{
	struct thread *td;
	struct iovec aiov;
	struct uio auio;
	int error;

	td = curthread;

	aiov.iov_base = __DECONST(void *, zero_region);
	aiov.iov_len = ZERO_REGION_SIZE;
	auio.uio_iov = &aiov;
	auio.uio_iovcnt = 1;
	auio.uio_offset = 0;
	auio.uio_resid = ZERO_REGION_SIZE;
	auio.uio_segflg = UIO_SYSSPACE;
	auio.uio_rw = UIO_WRITE;
	auio.uio_td = td;

	error = VOP_WRITE(vp, &auio, 0, td->td_ucred);
	return (error);
}
```

## 参见

[pmap(9)](pmap.9.md), [vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Ka Ho Ng <khng@FreeBSDFoundation.org> 在 FreeBSD 基金会赞助下编写。
