# DECLARE_GEOM_CLASS.9

`DECLARE_GEOM_CLASS` — GEOM 类声明宏

## 名称

`DECLARE_GEOM_CLASS`

## 概要

```c
#include <geom/geom.h>
```

```c
DECLARE_GEOM_CLASS(class, mod_name);
```

## 描述

`DECLARE_GEOM_CLASS` 宏在 GEOM 中注册一个 GEOM 类。GEOM 类本身实现一种特定类型的转换。典型的例子包括：MBR 磁盘分区、BSD disklabel 和 RAID5 类。`DECLARE_GEOM_CLASS` 可用于编译内建的 GEOM 类和作为 [kld(4)](../man4/kld.4.md) 模块加载的 GEOM 类，它是类注册的唯一官方方式。

`DECLARE_GEOM_CLASS` 的参数如下：

**`class`** 描述 GEOM 类的 `g_class` 结构。

**`mod_name`** 内核模块名（不是类名！）。

`g_class` 结构包含描述类的数据。它们是：

- 在类激活时，所有现有的 provider 都会被提供以供 taste。
- 当新 provider 创建时，它会被提供以供 taste。
- 在对 provider 的最后一次写访问关闭后，它会被提供以供重新 taste（在第一次写打开事件时会发送“spoil”）。

**`const char *`** `name` 类名。

**`g_taste_t *`** `taste` 指向用于处理 taste 事件的函数的指针。如果非 `NULL`，则在以下三种情况下被调用：

**`g_config_t *`** `config` 此字段不再使用，其功能已被 `ctlreq` 字段取代。

**`g_ctl_req_t *`** `ctlreq` 指向用于处理来自用户空间应用程序事件的函数的指针。

**`g_init_t *`** `init` 指向在类注册后立即调用的函数的指针。

**`g_fini_t *`** `fini` 指向在类注销前调用的函数的指针。

**`g_ctl_destroy_geom_t *`** `destroy_geom` 指向在类卸载时为每个 geom 调用的函数的指针。如果未设置此字段，则该类无法卸载。

只有 `name` 字段是必需的；其余均为可选。

## 限制与条件

`g_class` 的字段应始终使用 C99 风格的字段命名进行初始化（参见下面 `example_class` 的初始化方式）。

## 实例

类声明示例。

```c
static struct g_geom *
g_example_taste(struct g_class *mp, struct g_provider *pp,
    int flags __unused)
{
	g_topology_assert();
	[...]
}
static void
g_example_ctlreq(struct gctl_req *req, struct g_class *cp,
    char const *verb)
{
	[...]
}
static int
g_example_destroy_geom(struct gctl_req *req, struct g_class *cp,
    struct g_geom *gp)
{
	g_topology_assert();
	[...]
}
static void
g_example_init(struct g_class *mp)
{
	[...]
}
static void
g_example_fini(struct g_class *mp)
{
	[...]
}
struct g_class example_class = {
	.name = "EXAMPLE",
	.taste = g_example_taste,
	.ctlreq = g_example_ctlreq,
	.init = g_example_init,
	.fini = g_example_fini,
	.destroy_geom = g_example_destroy_geom
};
DECLARE_GEOM_CLASS(example_class, g_example);
```

## 参见

[geom(4)](../man4/geom.4.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
