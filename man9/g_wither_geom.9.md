# g_wither_geom.9

`g_wither_geom` — 在有机会时销毁 geom 及相关提供者和消费者

## 名称

`g_wither_geom`

## 概要

```c
#include <geom/geom.h>
```

```c
void
g_wither_geom(struct g_geom *gp, int error)
```

## 描述

`g_wither_geom` 函数通知 GEOM geom `gp` 将被销毁。GEOM 在给定 geom 的每个提供者上设置错误（在孤立过程中），并等待机会销毁 geom。如果任何拥有的消费者的访问计数变为 0，该消费者将被自动分离并销毁。如果附加到任何拥有的提供者的最后一个消费者被分离，该提供者将被销毁。如果没有更多的提供者或消费者，geom 将被销毁。

这是一种自动的“垃圾回收”，以避免在所有类中重复代码。在调用之前，应处理 `softc` 字段并将其设置为 `NULL`。注意，`g_wither_geom` 函数不保证 geom 会立即被销毁，主要是因为 geom 的消费者和提供者的访问计数可能不为 0。这就是为什么对于给定类中的每个 geom 调用此函数不足以确保该类可以卸载。

## 限制/条件

参数 `error` 必须非零。

必须持有拓扑锁。

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](DECLARE_GEOM_CLASS.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
