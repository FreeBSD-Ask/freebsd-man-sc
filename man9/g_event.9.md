# g_event.9

`g_post_event` — GEOM 事件管理

## 名称

`g_post_event`, `g_waitfor_event`, `g_cancel_event`

## 概要

```c
#include <geom/geom.h>

int
g_post_event(g_event_t *func, void *arg, int flag, ...)

int
g_waitfor_event(g_event_t *func, void *arg, int flag, ...)

void
g_cancel_event(void *ref)

struct g_event *
g_alloc_event(int flag)

void
g_post_event_ep(g_event_t *func, void *arg, struct g_event *ep, ...)
```

## 描述

GEOM 框架有自己的事件队列，用于向类通知重要事件。事件队列也可由 GEOM 类自身使用，例如用于绕过 I/O 路径中的某些限制，在 I/O 路径中不允许休眠、重量级任务等。

`g_post_event` 函数通知 GEOM 框架从事件队列中调用函数 `func`，参数为 `arg`。`flag` 参数传递给 [malloc(9)](malloc.9.md) 用于 `g_post_event` 内部的内存分配。仅允许的标志为 `M_WAITOK` 和 `M_NOWAIT`。其余参数用作标识事件的引用。可通过使用任一给定引用作为 `g_cancel_event` 的参数来取消事件。引用列表必须以 `NULL` 值结束。

`g_waitfor_event` 函数是 `g_post_event` 函数的阻塞版本。它等待事件完成或取消后返回。

`g_post_event_ep` 函数使用预分配的 `struct g_event` 发布事件。可通过 `g_alloc_event` 预分配事件。

`g_cancel_event` 函数取消由 `ref` 标识的所有事件。取消等价于以请求的参数和设置为 `EV_CANCEL` 的参数 `flag` 调用所请求的函数。

## 限制/条件

`g_post_event`：

- 参数 `flag` 必须为 `M_WAITOK` 或 `M_NOWAIT`。
- 引用列表必须以 `NULL` 值结束。

`g_waitfor_event`：

- 参数 `flag` 必须为 `M_WAITOK` 或 `M_NOWAIT`。
- 引用列表必须以 `NULL` 值结束。
- `g_waitfor_event` 函数不能从事件中调用，因为这样做会导致死锁。

`g_alloc_event`：

- 参数 `flag` 必须为 `M_WAITOK` 或 `M_NOWAIT`。
- 如果未调用 `g_post_event_ep`，则返回的 `struct g_event *` 必须用 `g_free` 释放。

## 返回值

`g_post_event` 和 `g_waitfor_event` 函数成功时返回 0；否则返回错误码。

## 实例

从事件队列调用的函数示例。

```c
void
example_event(void *arg, int flag)
{
	if (flag == EV_CANCEL) {
		printf("Event with argument %p canceled.n", arg);
		return;
	}
	printf("Event with argument %p called.n", arg);
}
```

## 错误

`g_post_event` 函数可能的错误：

**[`ENOMEM`]** `flag` 参数设置为 `M_NOWAIT` 且内存不足。

`g_waitfor_event` 函数可能的错误：

**[`EAGAIN`]** 事件已取消。

**[`ENOMEM`]** `flag` 参数设置为 `M_NOWAIT` 且内存不足。

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
