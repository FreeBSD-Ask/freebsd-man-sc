# hhook.9

`hhook` — 辅助钩子框架

## 名称

`hhook`, `hhook_head_register`, `hhook_head_deregister`, `hhook_head_deregister_lookup`, `hhook_run_hooks`, `HHOOKS_RUN_IF`, `HHOOKS_RUN_LOOKUP_IF`

## 概要

```c
#include <sys/hhook.h>
```

```c
typedef int *(*hhook_func_t)(int32_t hhook_type, int32_t hhook_id,
    void *udata, void *ctx_data, void *hdata, struct osd *hosd)
int
hhook_head_register(int32_t hhook_type, int32_t hhook_id,
    struct hhook_head **hhh, uint32_t flags)
int
hhook_head_deregister(struct hhook_head *hhh)
int
hhook_head_deregister_lookup(int32_t hhook_type, int32_t hhook_id)
void
hhook_run_hooks(struct hhook_head *hhh, void *ctx_data, struct osd *hosd)
HHOOKS_RUN_IF(hhh, ctx_data, hosd)
HHOOKS_RUN_LOOKUP_IF(hhook_type, hhook_id, ctx_data, hosd)
```

## 描述

`HHOOKS_RUN_LOOKUP_IF` 提供了一个框架，用于在内核中定义的钩子点管理和运行任意钩子函数。该 KPI 受 [pfil(9)](pfil.9.md) 启发，在许多方面可视为 pfil 的更通用超集。

[khelp(9)](khelp.9.md) 和 `HHOOKS_RUN_LOOKUP_IF` 框架紧密集成。Khelp 负责向 `HHOOKS_RUN_LOOKUP_IF` 点注册和注销 Khelp 模块钩子函数。Khelp 用于执行此操作的 KPI 函数未在此处记录，因为它们与希望实例化钩子点的消费者无关。

### Khelp 模块实现者信息

Khelp 模块通过为插入钩子点定义适当的钩子函数来间接与 `HHOOKS_RUN_LOOKUP_IF` 交互。钩子函数必须符合概要中概述的 `hhook_func_t` 函数指针声明。

`hhook_type` 和 `hhook_id` 参数标识调用钩子函数的钩子点。当单个钩子函数注册到多个钩子点并想知道是哪个钩子点调用了它时，这很有用。

```c
#include <sys/hhook.h>
```

列出了可用的 `hhook_type` 定义，导出钩子点的子系统负责在适当的头文件中定义 `hhook_id` 值。

如果在钩子注册时在 `struct hookinfo` 中指定了 `udata` 参数，它将传递给钩子函数。

`ctx_data` 参数包含来自钩子点调用位置的上下文特定数据。传递的数据类型取决于子系统。

`hdata` 参数是指向为模块分配的持久每对象存储的指针（如果需要）。仅当模块未请求每对象存储时，该指针才会为 NULL。

`hosd` 参数可与 [khelp(9)](khelp.9.md) 框架的 `khelp_get_osd` 函数一起使用，以访问属于不同 Khelp 模块的数据。

Khelp 模块通过为每个钩子点创建 `struct hookinfo` 来指示 Khelp 框架将其钩子函数注册到 `HHOOKS_RUN_LOOKUP_IF` 点，该结构包含以下成员：

```c
struct hookinfo {
	hhook_func_t	hook_func;
	struct helper	*hook_helper;
	void		*hook_udata;
	int32_t		hook_id;
	int32_t		hook_type;
};
```

Khelp 模块负责设置结构中除 `hook_helper` 之外的所有成员，后者由 Khelp 框架处理。

### 创建和管理钩子点

希望提供 `HHOOKS_RUN_LOOKUP_IF` 点的内核子系统通常需要对其实现进行四项可能五项关键更改：

- 在适当的子系统头文件中定义 `hhook_id` 映射列表。
- 在子系统初始化期间使用 `hhook_head_register` 函数注册每个钩子点。
- 选择或创建要作为上下文数据传递给钩子函数的标准化数据类型。
- 在子系统代码中应执行钩子点的位置添加对 `HHOOKS_RUN_IF` 或 `HHOOKS_RUN_IF_LOOKUP` 的调用。
- 如果子系统可在运行时动态添加/移除，则在子系统初始化时使用 `hhook_head_register` 函数注册的每个钩子点需要在子系统移除前取消初始化时使用 `hhook_head_deregister` 或 `hhook_head_deregister_lookup` 函数注销。

`hhook_head_register` 函数向 `HHOOKS_RUN_LOOKUP_IF` 框架注册钩子点。`hook_type` 参数定义钩子点的高级类型。有效类型定义于：

```c
#include <sys/hhook.h>
```

应根据需要添加新类型。`hook_id` 参数指定钩子点的唯一子系统特定标识符。`hhh` 参数（如果不为 NULL）将用于存储对作为注册过程一部分创建的 `struct hhook_head` 的引用。子系统通常希望存储 `struct hhook_head` 的本地副本，以便它们可以使用 `HHOOKS_RUN_IF` 宏来实例化钩子点。如果允许 [malloc(9)](malloc.9.md) 休眠等待内存可用，则可通过 `flags` 参数传入 HHOOK_WAITOK 标志。如果钩子点位于虚拟化子系统中（例如网络栈），则应通过 `flags` 参数传入 HHOOK_HEADISINVNET 标志，以便在注册过程中创建的 `struct hhook_head` 将添加到虚拟化列表。

`hhook_head_deregister` 函数从 `HHOOKS_RUN_LOOKUP_IF` 框架注销先前注册的钩子点。`hhh` 参数是注册钩子点时由 `hhook_head_register` 返回的指向 `struct hhook_head` 的指针。

`hhook_head_deregister_lookup` 函数可在调用者没有 `struct hhook_head` 缓存副本并希望使用适当的 `hook_type` 和 `hook_id` 标识符注销钩子点的情况下替代 `hhook_head_deregister` 使用。

`hhook_run_hooks` 函数通常不应直接调用，而应通过 `HHOOKS_RUN_IF` 宏间接调用。然而，可能存在直接调用函数更可取的情况，因此此处为完整性起见对其进行了记录。`hhh` 参数引用要为其调用所有已注册钩子函数的 `HHOOKS_RUN_LOOKUP_IF` 点。`ctx_data` 参数指定指向要传递给钩子函数的上下文钩子点数据的指针。`hosd` 参数应为指向适当对象 `struct osd` 的指针（如果子系统为 Khelp 模块提供关联每对象数据的能力）。不提供的子系统应传递 NULL。

`HHOOKS_RUN_IF` 宏是实现钩子点的首选方式。仅当至少一个钩子函数注册到钩子点时，它才调用 `hhook_run_hooks` 函数。通过检查已注册的钩子函数，该宏在未注册钩子函数的常见情况下将向频繁使用的代码路径添加钩子点的成本降低为简单的 if 测试，从而最小化成本。参数如 `hhook_run_hooks` 函数所述。

`HHOOKS_RUN_IF_LOOKUP` 宏执行与 `HHOOKS_RUN_IF` 宏相同的功能，但执行额外步骤来查找指定 `hook_type` 和 `hook_id` 标识符的 `struct hhook_head`。由于查找关联的引用计数开销，它不应在频繁执行的代码路径中使用。

## 实现说明

每个 `struct hhook_head` 用 [rmlock(9)](rmlock.9.md) 保护其内部钩子函数列表。因此，每当直接或通过 `HHOOKS_RUN_IF` 或 `HHOOKS_RUN_IF_LOOKUP` 宏间接调用 `hhook_run_hooks` 时，都会获取并持有不可休眠的读锁，跨越对所有已注册钩子函数的调用。

## 返回值

`hhook_head_register` 无错误时返回 0。如果具有相同 `hook_type` 和 `hook_id` 的钩子点已注册，则返回 EEXIST。如果 `flags` 中未设置 HHOOK_HEADISINVNET 标志（因为实现尚不支持非虚拟化子系统中的钩子点），则返回 EINVAL（详见缺陷部分）。如果 [malloc(9)](malloc.9.md) 未能为新 `struct hhook_head` 分配内存，则返回 ENOMEM。

`hhook_head_deregister` 和 `hhook_head_deregister_lookup` 无错误时返回 0。如果 `hhh` 为 NULL 则返回 ENOENT。如果 `hhh` 的引用计数大于一则返回 EBUSY。

## 实例

可在以下位置找到注释完善的示例 Khelp 模块：`/usr/share/examples/kld/khelp/h_example.c`

[tcp(4)](../man4/tcp.4.md) 实现提供了两个 `HHOOKS_RUN_LOOKUP_IF` 点，当连接处于建立阶段时为发送/接收的数据包调用。在以下文件中搜索 HHOOK：`sys/netinet/tcp_var.h`、`sys/netinet/tcp_input.c`、`sys/netinet/tcp_output.c` 和 `sys/netinet/tcp_subr.c`。

## 参见

[khelp(9)](khelp.9.md)

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Cisco 大学研究计划基金（在硅谷社区基金会）的资助。

## 历史

`HHOOKS_RUN_LOOKUP_IF` 框架首次出现于 FreeBSD 9.0。

`HHOOKS_RUN_LOOKUP_IF` 框架由 Lawrence Stewart 于 2010 年在澳大利亚墨尔本斯威本科技大学高级互联网架构中心学习期间首次发布。更多详情请见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`HHOOKS_RUN_LOOKUP_IF` 框架由 Lawrence Stewart <lstewart@FreeBSD.org> 编写。

本手册页由 David Hayes <david.hayes@ieee.org> 和 Lawrence Stewart <lstewart@FreeBSD.org> 编写。
