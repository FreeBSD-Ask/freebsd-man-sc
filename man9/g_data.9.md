# g_data(9)

`g_read_data` — 从 GEOM 消费者读取/向其写入数据

## 名称

`g_read_data`, `g_write_data`

## 概要

```c
#include <geom/geom.h>

void *
g_read_data(struct g_consumer *cp, off_t offset, off_t length, int *error)

int
g_write_data(struct g_consumer *cp, off_t offset, void *ptr, off_t length)
```

## 描述

`g_read_data` 函数从附加到消费者 `cp` 的提供者中，起始偏移 `offset` 处读取 `length` 字节的数据。`g_read_data` 返回的缓冲区使用 `g_malloc` 分配，因此使用后应由调用者用 `g_free` 释放。如果操作失败，当 `error` 参数不为 `NULL` 时，错误值将存储在该参数中。

`g_write_data` 函数将 `ptr` 所指向缓冲区中的 `length` 字节数据写入附加到消费者 `cp` 的提供者，起始偏移为 `offset`。

## 限制/条件

`length` 参数应为提供者扇区大小的倍数，且小于或等于 `DFLTPHYS`（`DFLTPHYS` 定义于以下文件中：

```c
#include <sys/param.h>
```

不得持有拓扑锁。

## 返回值

`g_read_data` 函数返回指向数据缓冲区的指针，发生错误时返回 `NULL`。此时，当 `error` 参数不为 `NULL` 时，错误值存储在该参数中。

`g_write_data` 函数成功时返回 0；否则返回错误码。

## 错误

可能的错误：

**[`EIO`]** 从消费者读取或向其写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从消费者读取时检测到数据损坏。

## 参见

[geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_bio(9)](g_bio.9.md), [g_consumer(9)](g_consumer.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
