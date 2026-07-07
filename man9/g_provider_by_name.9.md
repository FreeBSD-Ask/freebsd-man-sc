# g_provider_by_name(9)

`g_provider_by_name` — 查找具有给定名称的 GEOM 提供者

## 名称

`g_provider_by_name`

## 概要

```c
#include <geom/geom.h>
```

```c
struct g_provider *
g_provider_by_name(const char *name)
```

## 描述

`g_provider_by_name` 函数搜索名为 `name` 的提供者，并返回绑定到它的 `g_provider` 结构。参数 `name` 可以是名称或完整路径（即“`da0`”或“`/dev/da0`”）。

## 限制/条件

必须持有拓扑锁。

## 返回值

`g_provider_by_name` 函数返回指向名为 `name` 的提供者的指针，如果没有这样的提供者则返回 `NULL`。

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
