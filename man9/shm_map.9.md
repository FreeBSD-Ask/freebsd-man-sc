# shm_map(9)

`shm_map` — 将共享内存对象映射到内核地址空间

## 名称

`shm_map`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/mman.h>
```

```c
int
shm_map(struct file *fp, size_t size, off_t offset, void **memp)

int
shm_unmap(struct file *fp, void *mem, size_t size)
```

## 描述

`shm_map` 和 `shm_unmap` 函数提供了将共享内存对象映射到内核的 API。共享内存对象由 shm_open(2) 创建。然后这些对象可以通过文件描述符传递到内核中。

共享内存对象在映射到内核时不能被缩小。这是为了避免使可能锁定到内核地址空间中的任何页面无效。共享内存对象在映射到内核时仍然可以被增长。

为简化执行上述要求所需的记账，此 API 的调用者在调用 `shm_unmap` 时需要取消映射由 `shm_map` 映射的整个区域。不允许仅取消映射区域的一部分。

`shm_map` 函数定位与打开文件 `fp` 关联的共享内存对象。它将该对象中由 `offset` 和 `size` 描述的区域映射到内核地址空间。如果成功，`*memp` 将设置为映射的起始位置。成功返回时，该范围的所有页面将被锁定到内存中。

`shm_unmap` 函数取消先前由 `shm_map` 映射的区域。`mem` 参数应与先前在 `*memp` 中返回的值匹配，`size` 参数应与传递给 `shm_map` 的值匹配。

注意，`shm_map` 不会在映射的生命周期内对打开文件 `fp` 持有额外引用。相反，如果调用代码希望将来在该区域上使用 `shm_unmap`，则需要自行执行此操作。

## 返回值

`shm_map` 和 `shm_unmap` 函数成功时返回零，失败时返回错误。

## 实例

以下函数接受共享内存对象的文件描述符。它将对象的前 16 KB 映射到内核，对该地址执行一些操作，然后在返回之前取消映射该地址。

```c
int
shm_example(int fd)
{
	struct file *fp;
	void *mem;
	int error;
	error = fget(curthread, fd, CAP_MMAP, &fp);
	if (error)
		return (error);
	error = shm_map(fp, 16384, 0, &mem);
	if (error) {
		fdrop(fp, curthread);
		return (error);
	}
	/* 对 'mem' 做一些操作。 */
	error = shm_unmap(fp, mem, 16384);
	fdrop(fp, curthread);
	return (error);
}
```

## 错误

`shm_map` 函数失败时返回以下错误：

**[`EINVAL`]** 打开文件 `fp` 不是共享内存对象。

**[`EINVAL`]** 由 `offset` 和 `size` 描述的请求区域超出了共享内存对象的末尾。

**[`ENOMEM`]** 可用地址空间不足。

**[`EACCES`]** 由于保护错误，无法映射共享内存对象。

**[`EINVAL`]** 由于其他 VM 错误，无法映射共享内存对象。

`shm_unmap` 函数失败时返回以下错误：

**[`EINVAL`]** 打开文件 `fp` 不是共享内存对象。

**[`EINVAL`]** 由 `mem` 和 `size` 描述的地址范围不是有效的地址范围。

**[`EINVAL`]** 由 `mem` 和 `size` 描述的地址范围不由与打开文件 `fp` 关联的共享内存对象支持，或该地址范围不覆盖该对象的整个映射。

## 参见

[shm_open(2)](../sys/shm_open.2.md)

## 历史

此 API 首次在 FreeBSD 10.0 中引入。
