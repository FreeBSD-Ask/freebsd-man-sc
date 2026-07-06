# g_provider.9

`g_new_providerf` — GEOM 提供者管理

## 名称

`g_new_providerf`, `g_destroy_provider`, `g_error_provider`

## 概要

```c
#include <geom/geom.h>
```

```c
struct g_provider *
g_new_providerf(struct g_geom *gp, const char *fmt, ...)
void
g_destroy_provider(struct g_provider *pp)
void
g_error_provider(struct g_provider *pp, int error)
```

## 描述

GEOM 提供者是 geom 提供服务的前门。提供者是“出现在 `/dev` 中的类磁盘事物”——换句话说，一个逻辑磁盘。所有提供者都有三个主要属性：名称、sectorsize 和大小。

`g_new_providerf` 函数在给定 geom `gp` 上创建新提供者。提供者的名称（将作为设备出现在 [devfs(4)](../man4/devfs.4.md) 中）以 printf(3) 风格从其余参数创建。创建后，调用者必须设置提供者的 `mediasize` 和 `sectorsize` 以及其他所需的初始化，然后调用 `g_error_provider` 重置提供者的错误（最初设置为 `ENXIO`）。

`g_destroy_provider` 函数销毁给定提供者，取消所有相关的挂起事件并移除相应的 devfs 条目。

`g_error_provider` 函数用于设置提供者的错误值。如果设置为非零，所有 I/O 请求将被拒绝，且无法增加其访问计数（将返回错误 `error`）。

## 限制/条件

`g_new_provider`：

- 提供者名称应唯一，但这不由 GEOM 强制执行。如果名称不唯一，最终会出现两个（或更多）同名文件，这是程序员错误。
- geom `gp` 必须定义了 `start` 方法。
- 必须持有拓扑锁。

`g_destroy_provider`：

- 提供者不得已附加消费者。
- 访问计数必须为 0。
- 必须持有拓扑锁。

## 返回值

`g_new_providerf` 函数返回指向新创建提供者的指针。

## 实例

创建示例提供者，设置其参数并使其可用。

```c
struct g_provider *
create_example_provider(struct g_geom *gp)
{
	struct g_provider *pp;
	g_topology_lock();
	pp = g_new_providerf(gp, "example_provider");
	g_topology_unlock();
	pp->mediasize = 65536;
	pp->sectorsize = 512;
	g_error_provider(pp, 0);
	return (pp);
}
```

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
