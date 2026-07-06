# g_geom.9

`g_new_geomf` — geom 管理

## 名称

`g_new_geomf`, `g_new_geom`, `g_destroy_geom`

## 概要

```c
#include <geom/geom.h>

struct g_geom *
g_new_geomf(struct g_class *mp, const char *fmt, ...)

struct g_geom *
g_new_geom(struct g_class *mp, const char *name)

void
g_destroy_geom(struct g_geom *gp)
```

## 描述

geom（不要将“geom”与“GEOM”混淆）是 GEOM 类的实例。例如：在典型的 i386 FreeBSD 系统上，每个磁盘将有一个 MBR 类的 geom。geom 的名称并不重要，仅用于 XML 转储和调试目的。可以有许多同名的 geom。

`g_new_geomf` 函数创建一个新 geom，它将是类 `mp` 的实例。geom 的名称以类似 printf(3) 的方式从其余参数创建。

`g_new_geom` 函数与 `g_new_geomf` 非常相似，区别在于它接受常规字符串而非类似 printf(3) 的格式字符串作为 geom 的名称。

`g_destroy_geom` 函数立即销毁给定的 geom 并取消所有相关的待处理事件。

`g_geom` 结构包含若干字段，应在 geom 创建后、创建与此 geom 相关的任何提供者或消费者之前由调用者设置（并非全部必填）：

**`g_start_t *`** `start` 指向用于 I/O 处理的函数的指针。

**`g_spoiled_t *`** `spoiled` 指向用于消费者 spoiling 的函数的指针。

**`g_dumpconf_t *`** `dumpconf` 指向用于 XML 格式转储配置的函数的指针。

**`g_access_t *`** `access` 指向用于访问控制的函数的指针。

**`g_orphan_t *`** `orphan` 指向用于通知孤儿消费者的函数的指针。

**`g_ioctl_t *`** `ioctl` 指向用于处理 ioctl 请求的函数的指针。

**`void *`** `softc` 供私有使用的字段。

## 限制/条件

如果打算在此 geom 中使用提供者，必须设置 geom 的 `start` 字段。

如果打算在 geom 中使用消费者，必须为其设置 `orphan` 和 `access` 字段。

`g_new_geomf` 和 `g_new_geom`：

- 类 `mp` 必须有效（已在 GEOM 中注册）。
- 必须持有拓扑锁。

`g_destroy_geom`：

- geom 不能拥有任何提供者。
- geom 不能拥有任何消费者。
- 必须持有拓扑锁。

## 返回值

`g_new_geomf` 函数返回指向新创建的 geom 的指针。

## 实例

创建一个示例 geom。

```c
static void
g_example_start(struct bio *bp)
{
	[...]
}
static void
g_example_orphan(struct g_consumer *cp)
{
	g_topology_assert();
	[...]
}
static void
g_example_spoiled(struct g_consumer *cp)
{
	g_topology_assert();
	[...]
}
static int
g_example_access(struct g_provider *pp, int dr, int dw, int de)
{
	[...]
}
static struct g_geom *
create_example_geom(struct g_class *myclass)
{
	struct g_geom *gp;
	g_topology_lock();
	gp = g_new_geomf(myclass, "example_geom");
	g_topology_unlock();
	gp->start = g_example_start;
	gp->orphan = g_example_orphan;
	gp->spoiled = g_example_spoiled;
	gp->access = g_example_access;
	gp->softc = NULL;
	return (gp);
}
static int
destroy_example_geom(struct g_geom *gp)
{
	g_topology_lock();
	if (!LIST_EMPTY(&gp->provider) ||
	    !LIST_EMPTY(&gp->consumer)) {
		g_topology_unlock();
		return (EBUSY);
	}
	g_destroy_geom(gp);
	g_topology_unlock();
	return (0);
}
```

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
