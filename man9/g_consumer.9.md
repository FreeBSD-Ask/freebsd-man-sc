# g_consumer.9

`g_new_consumer` — GEOM 消费者管理

## 名称

`g_new_consumer`, `g_destroy_consumer`

## 概要

```c
#include <geom/geom.h>

struct g_consumer *
g_new_consumer(struct g_geom *gp)

void
g_destroy_consumer(struct g_consumer *cp)
```

## 描述

GEOM 消费者是 geom 连接到另一个 GEOM 提供者并发送 I/O 请求的后门。

`g_new_consumer` 函数在 geom `gp` 上创建一个新消费者。在使用新消费者之前，必须通过 [g_attach(9)](g_attach.9.md) 将其附加到提供者，并通过 [g_access(9)](g_access.9.md) 打开。

`g_destroy_consumer` 函数销毁给定消费者并取消所有相关的待处理事件。此函数是杀掉不需要的消费者的最后阶段。

## 限制/条件

`g_new_consumer`：

- geom `gp` 必须定义了 `orphan` 方法。
- 必须持有拓扑锁。

`g_destroy_consumer`：

- 消费者不得已附加到提供者。
- 访问计数必须为 0。
- 必须持有拓扑锁。

## 返回值

`g_new_consumer` 函数返回指向新创建的消费者的指针。

## 实例

创建消费者，将其附加到给定提供者，获取读取访问权限并清理。

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

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](DECLARE_GEOM_CLASS.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
