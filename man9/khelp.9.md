# khelp.9

`khelp` — 内核助手框架

## 名称

`khelp`, `khelp_init_osd`, `khelp_destroy_osd`, `khelp_get_id`, `khelp_get_osd`, `khelp_add_hhook`, `khelp_remove_hhook`, `KHELP_DECLARE_MOD`, `KHELP_DECLARE_MOD_UMA`

## 概要

```c
#include <sys/khelp.h>
#include <sys/module_khelp.h>
```

```c
int
khelp_init_osd(uint32_t classes, struct osd *hosd)

int
khelp_destroy_osd(struct osd *hosd)

int32_t
khelp_get_id(char *hname)

void *
khelp_get_osd(struct osd *hosd, int32_t id)

int
khelp_add_hhook(const struct hookinfo *hki, uint32_t flags)

int
khelp_remove_hhook(const struct hookinfo *hki)

KHELP_DECLARE_MOD(hname, hdata, hhooks, version)
KHELP_DECLARE_MOD_UMA(hname, hdata, hhooks, version, ctor, dtor)
```

## 描述

`khelp` 提供了一个框架，用于管理 `KHELP_DECLARE_MOD_UMA` 模块，这些模块间接使用 [hhook(9)](hhook.9.md) KPI 将其钩子函数注册到内核内感兴趣的钩子点。Khelp 模块旨在提供一种结构化的方式，以保持 ABI 的方式在运行时动态扩展内核。根据提供钩子点的子系统，`KHELP_DECLARE_MOD_UMA` 模块可能能够关联每对象数据，以在钩子调用之间维护相关状态。[hhook(9)](hhook.9.md) 和 `KHELP_DECLARE_MOD_UMA` 框架紧密集成，任何对 `KHELP_DECLARE_MOD_UMA` 感兴趣的人都应仔细阅读 [hhook(9)](hhook.9.md) 手册页。

### Khelp 模块实现者信息

`KHELP_DECLARE_MOD_UMA` 模块在 `KHELP_DECLARE_MOD_UMA` 框架内由 `struct helper` 表示，其具有以下成员：

```c
struct helper {
	int (*mod_init) (void);
	int (*mod_destroy) (void);
#define	HELPER_NAME_MAXLEN 16
	char			h_name[HELPER_NAME_MAXLEN];
	uma_zone_t		h_zone;
	struct hookinfo		*h_hooks;
	uint32_t		h_nhooks;
	uint32_t		h_classes;
	int32_t			h_id;
	volatile uint32_t	h_refcount;
	uint16_t		h_flags;
	TAILQ_ENTRY(helper)	h_next;
};
```

模块必须实例化一个 `struct helper`，但只需要设置 `h_classes` 字段，并可在需要时可选地设置 `h_flags`、`mod_init` 和 `mod_destroy` 字段。框架负责所有其他字段，模块应避免操作它们。鼓励使用 C99 指定初始化器特性来设置字段。

如果指定，`mod_init` 函数将在 `KHELP_DECLARE_MOD_UMA` 框架完成注册过程之前运行。从 `mod_init` 函数返回非零值将中止注册过程并导致模块加载失败。如果指定，`mod_destroy` 函数将在注销过程中由 `KHELP_DECLARE_MOD_UMA` 框架运行，此时模块已被 `KHELP_DECLARE_MOD_UMA` 框架注销。返回值当前被忽略。有效的 `KHELP_DECLARE_MOD_UMA` 类定义在

```c
#include <sys/khelp.h>
```

有效的标志定义在

```c
#include <sys/module_khelp.h>
```

如果 `KHELP_DECLARE_MOD_UMA` 模块需要持久的每对象数据存储，应在 `h_flags` 字段中设置 HELPER_NEEDS_OSD 标志。目前没有编程方式来检查 `KHELP_DECLARE_MOD_UMA` 类是否为 `KHELP_DECLARE_MOD_UMA` 模块提供关联持久每对象数据的能力，因此需要手动检查。

`KHELP_DECLARE_MOD` 和 `KHELP_DECLARE_MOD_UMA` 宏提供了 [DECLARE_MODULE(9)](declare_module.9.md) 宏的便捷包装，用于向 `KHELP_DECLARE_MOD_UMA` 框架注册 `KHELP_DECLARE_MOD_UMA` 模块。`KHELP_DECLARE_MOD_UMA` 只应由需要使用持久每对象存储的模块使用，即在其 `struct helper` 的 `h_flags` 字段中设置 HELPER_NEEDS_OSD 标志的模块。

两个宏共有的前四个参数如下。`hname` 参数指定 `KHELP_DECLARE_MOD_UMA` 模块的唯一 [ascii(7)](../man7/ascii.7.md) 名称。其长度不应超过 HELPER_NAME_MAXLEN-1 个字符。`hdata` 参数是指向模块 `struct helper` 的指针。`hhooks` 参数指向 `struct hookinfo` 结构的静态数组。该数组应为模块希望挂钩的每个 [hhook(9)](hhook.9.md) 点包含一个 `struct hookinfo`，即使对不同的 [hhook(9)](hhook.9.md) 点多次使用相同的钩子函数。`version` 参数指定模块的版本号，将传递给 [MODULE_VERSION(9)](module_version.9.md)。`KHELP_DECLARE_MOD_UMA` 宏接受额外的 `ctor` 和 `dtor` 参数，指定可选的 uma(9) 构造函数和析构函数。在不需要该功能的地方应传递 NULL。

`khelp_get_id` 函数返回名为 `hname` 的 `KHELP_DECLARE_MOD_UMA` 模块的数字标识符。

`khelp_get_osd` 函数用于获取指定 `KHELP_DECLARE_MOD_UMA` 模块的每对象数据指针。`hosd` 参数是指向底层子系统对象的 `struct osd` 的指针。这由 [hhook(9)](hhook.9.md) 框架在调用 `KHELP_DECLARE_MOD_UMA` 模块的钩子函数时提供。`id` 参数指定要从 `hosd` 中提取数据指针的 `KHELP_DECLARE_MOD_UMA` 模块的数字标识符。`id` 使用 `khelp_get_id` 函数获取。

`khelp_add_hhook` 和 `khelp_remove_hhook` 函数允许 `KHELP_DECLARE_MOD_UMA` 模块在运行时动态挂钩/摘钩 [hhook(9)](hhook.9.md) 点。`hki` 参数指定指向 `struct hookinfo` 的指针，该结构封装了有关正在操作的 [hhook(9)](hhook.9.md) 点和钩子函数的所需信息。如果允许 [malloc(9)](malloc.9.md) 休眠等待内存可用，可以通过 `khelp_add_hhook` 的 `flags` 参数传递 HHOOK_WAITOK 标志。

### 将 Khelp 集成到内核子系统

允许 `KHELP_DECLARE_MOD_UMA` 模块做有用事情所需的大部分工作涉及为 `KHELP_DECLARE_MOD_UMA` 模块定义和实例化合适的 [hhook(9)](hhook.9.md) 点以供挂钩。子系统需要做出的唯一额外决定是是否要允许 `KHELP_DECLARE_MOD_UMA` 模块关联持久的每对象数据。提供对持久数据存储的支持可以允许 `KHELP_DECLARE_MOD_UMA` 模块执行可能更复杂的功能。希望允许 Khelp 模块将持久每对象数据与子系统数据结构之一关联的子系统需要进行以下两个关键更改：

- 在对象的结构定义中嵌入一个 `struct osd` 指针。
- 在分别负责初始化和销毁对象的子系统代码路径中添加对 `khelp_init_osd` 和 `khelp_destroy_osd` 的调用。

`khelp_init_osd` 函数为所有当前已加载且在其 `h_flags` 字段中设置了 HELPER_NEEDS_OSD 标志的适当类的 `KHELP_DECLARE_MOD_UMA` 模块初始化每对象数据存储。`classes` 参数指定此子系统关联的 `KHELP_DECLARE_MOD_UMA` 类的位掩码。如果 `KHELP_DECLARE_MOD_UMA` 模块匹配位掩码中的任何类，该模块将与对象关联。`hosd` 参数指定指向对象 `struct osd` 的指针，将用于提供 `KHELP_DECLARE_MOD_UMA` 模块使用的持久存储。

`khelp_destroy_osd` 函数释放之前通过调用 `khelp_init_osd` 与对象 `struct osd` 关联的所有内存。`hosd` 参数指定指向对象 `struct osd` 的指针，该结构将被清除以准备销毁。

## 实现说明

`KHELP_DECLARE_MOD_UMA` 模块通过引用计数防止被过早卸载。每次子系统调用 `khelp_init_osd` 为模块分配持久存储时，计数递增，每次相应的 `khelp_destroy_osd` 调用递减。只有当模块的引用计数降为零时，才能卸载该模块。

## 返回值

`khelp_init_osd` 函数如果未发生错误则返回零。如果需要每对象存储的 `KHELP_DECLARE_MOD_UMA` 模块未能分配所需内存，则返回 ENOMEM。

`khelp_destroy_osd` 函数仅返回零以指示未发生错误。

`khelp_get_id` 函数返回名为 `hname` 的已注册 `KHELP_DECLARE_MOD_UMA` 模块的唯一数字标识符。如果当前没有注册具有指定名称的模块，则返回 -1。

`khelp_get_osd` 函数返回指向 `KHELP_DECLARE_MOD_UMA` 模块持久对象存储内存的指针。如果由 `id` 标识的模块未在对象的 `hosd` `struct osd` 中注册持久对象存储，则返回 NULL。

`khelp_add_hhook` 函数如果未发生错误则返回零。如果找不到请求的 [hhook(9)](hhook.9.md) 点则返回 ENOENT。如果 [malloc(9)](malloc.9.md) 未能分配内存则返回 ENOMEM。如果尝试为同一 [hhook(9)](hhook.9.md) 点多次注册同一钩子函数则返回 EEXIST。

`khelp_remove_hhook` 函数如果未发生错误则返回零。如果找不到请求的 [hhook(9)](hhook.9.md) 点则返回 ENOENT。

## 实例

一个注释良好的 Khelp 模块示例可在以下位置找到：**`/usr/share/examples/kld/khelp/h_example.c`**

增强往返时间 (ERTT) [h_ertt(4)](../man4/h_ertt.4.md) `KHELP_DECLARE_MOD_UMA` 模块提供了一个更复杂的示例，展示了可能实现的功能。

## 参见

[h_ertt(4)](../man4/h_ertt.4.md), [hhook(9)](hhook.9.md), [osd(9)](osd.9.md)

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Cisco 大学研究计划基金（由硅谷社区基金会管理）的资助。

## 历史

`KHELP_DECLARE_MOD_UMA` 内核助手框架首次出现在 FreeBSD 9.0 中。

`KHELP_DECLARE_MOD_UMA` 框架由 Lawrence Stewart 于 2010 年在澳大利亚墨尔本斯威本科技大学高级互联网架构中心学习期间首次发布。更多详情请参见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`KHELP_DECLARE_MOD_UMA` 框架由 Lawrence Stewart <lstewart@FreeBSD.org> 编写。

本手册页由 David Hayes <david.hayes@ieee.org> 和 Lawrence Stewart <lstewart@FreeBSD.org> 编写。
