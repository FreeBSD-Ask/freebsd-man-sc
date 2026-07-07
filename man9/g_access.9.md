# g_access(9)

`g_access` — 控制对 GEOM 消费者及其提供者的访问

## 名称

`g_access`

## 概要

```c
#include <geom/geom.h>

int
g_access(struct g_consumer *cp, int dcr, int dcw, int dce)
```

## 描述

`g_access` 函数允许打开、关闭以及一般性地更改附加到给定消费者 `cp` 的提供者的访问。参数 `dcr`、`dcw` 和 `dce` 表示相对的读取、写入和独占访问计数变化。读取和写入访问计数不言自明，独占访问计数则拒绝其他相关方的写入访问。提供者的访问计数是所有附加消费者的访问计数之和。

在使用 [g_attach(9)](g_attach.9.md) 将消费者附加到提供者之后，必须在该消费者上调用 `g_access` 函数才能开始 I/O 请求。

## 限制/条件

消费者必须已附加到提供者。

预期的更改不得导致访问计数为负。

不允许无操作（`dcr` = `dcw` = `dce` = `0`）。

提供者的 geom 必须定义了访问方法（例如 `gp->access`）。

必须持有拓扑锁。

## 返回值

`g_access` 函数成功时返回 0；否则返回错误码。注意，当参数 `dcr`、`dcw` 和 `dce` 小于或等于 0 时，`g_access` 不会失败。

## 实例

创建一个消费者，将其附加到给定提供者，获取读取访问权限并读取第一个扇区。

```c
void
some_function(struct g_geom *mygeom, struct g_provider *pp)
{
	struct g_consumer *cp;
	void *ptr;
	int error;
	g_topology_assert();
	/* 在“mygeom”geom 上创建新消费者。 */
	cp = g_new_consumer(mygeom);
	/* 将新创建的消费者附加到给定提供者。 */
	if (g_attach(cp, pp) != 0) {
		g_destroy_consumer(cp);
		return;
	}
	/* 通过我们的消费者以读取方式打开提供者。 */
	error = g_access(cp, 1, 0, 0);
	if (error != 0) {
		printf("Cannot access provider: %sn", error);
		g_detach(cp);
		g_destroy_consumer(cp);
		return;
	}
	/*
	 * 读取时不要持有拓扑锁。
	 */
	g_topology_unlock();
	ptr = g_read_data(cp, 0, pp->sectorsize, &error);
	if (ptr == NULL)
		printf("Error while reading: %dn", error);
	/*
	 * 对数据做些有用的操作。
	 */
	g_topology_lock();
	/* 断开与提供者的连接（释放访问计数）。 */
	g_access(cp, -1, 0, 0);
	/* 从提供者分离。 */
	g_detach(cp);
	/* 销毁消费者。 */
	g_destroy_consumer(cp);
}
```

## 错误

可能的错误：

**[`EPERM`]** 函数试图以独占访问计数打开提供者，但该提供者已为写入而打开。

**[`EPERM`]** 函数试图以写入方式打开提供者，但该提供者已以独占方式打开。

提供者的访问方法可能返回的任何其他错误。

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
