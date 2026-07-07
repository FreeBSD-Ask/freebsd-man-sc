# g_attach(9)

`g_attach` — 将 GEOM 消费者附加到/从提供者分离

## 名称

`g_attach`, `g_detach`

## 概要

```c
#include <geom/geom.h>

int
g_attach(struct g_consumer *cp, struct g_provider *pp)

void
g_detach(struct g_consumer *cp)
```

## 描述

`g_attach` 函数将给定消费者 `cp` 附加到给定提供者 `pp`，从而在消费者和提供者之间建立通信通道，允许更改访问计数并执行 I/O 操作。

`g_detach` 函数将给定消费者 `cp` 从其对应的提供者分离，拆除它们之间的通信通道。

## 限制/条件

`g_attach`：

- 消费者不得已附加到提供者。
- 操作不得创建拓扑环。
- 必须持有拓扑锁。

`g_detach`：

- 消费者必须已附加。
- 访问计数必须为 0。
- 不能有活动请求。
- 必须持有拓扑锁。

## 返回值

`g_attach` 函数成功时返回 0；否则返回错误码。

## 实例

创建一个消费者，将其附加到给定提供者，获取读取访问权限并清理。

```c
void
some_function(struct g_geom *mygeom, struct g_provider *pp)
{
	struct g_consumer *cp;
	g_topology_assert();
	/* 在“mygeom”geom 上创建新消费者。 */
	cp = g_new_consumer(mygeom);
	/* 将新创建的消费者附加到给定提供者。 */
	if (g_attach(cp, pp) != 0) {
		g_destroy_consumer(cp);
		return;
	}
	/* 通过我们的消费者以读取方式打开提供者。 */
	if (g_access(cp, 1, 0, 0) != 0) {
		g_detach(cp);
		g_destroy_consumer(cp);
		return;
	}
	g_topology_unlock();
	/*
	 * 从提供者读取数据。
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

**[`ELOOP`]** 操作创建了拓扑环。

**[`ENXIO`]** 提供者已成孤儿。

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_access(9)](g_access.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
