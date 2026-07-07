# g_bio(9)

`g_new_bio` — GEOM bio 控制函数

## 名称

`g_new_bio`, `g_clone_bio`, `g_destroy_bio`, `g_format_bio`, `g_print_bio`, `g_reset_bio`

## 概要

```c
#include <sys/bio.h>

#include <geom/geom.h>

struct bio *
g_new_bio(void)

struct bio *
g_alloc_bio(void)

struct bio *
g_clone_bio(struct bio *bp)

struct bio *
g_duplicate_bio(struct bio *bp)

void
g_destroy_bio(struct bio *bp)

void
g_format_bio(struct sbuf *sb, const struct bio *bp)

void
g_print_bio(struct sbuf *sb, const char *prefix, const struct bio *bp,
    const char *fmtsuffix, ...)

void
g_reset_bio(struct bio *bp)
```

## 描述

GEOM 使用 `struct bio` 描述 I/O 请求，其最重要的字段描述如下：

**`BIO_READ`** 读取请求。

**`BIO_WRITE`** 写入请求。

**`BIO_DELETE`** 指示某段数据范围不再使用，可按底层技术支持的方式擦除或释放。闪存适配层等技术可在相关块被重新分配之前安排擦除，加密设备可能希望在范围内填充随机位以减少可供攻击的数据量。

**`BIO_GETATTR`** 检查和操作特定提供者或路径上的带外属性。属性由 ASCII 字符串命名，存储在 `bio_attribute` 字段中。

**`BIO_FLUSH`** 通知底层提供者刷新其写缓存。

**`BIO_ERROR`** 请求失败（错误值存储在 `bio_error` 字段中）。

**`BIO_DONE`** 请求完成。

**`bio_cmd`** I/O 请求命令。GEOM 中有五种 I/O 请求可用：

**`bio_flags`** 可用标志：

**`bio_cflags`** 供消费者私有使用。

**`bio_pflags`** 供提供者私有使用。

**`bio_offset`** 提供者内的偏移量。

**`bio_data`** 指向数据缓冲区的指针。

**`bio_error`** 设置 `BIO_ERROR` 时的错误值。

**`bio_done`** 指向请求完成时调用的函数的指针。

**`bio_driver1`** 供提供者私有使用。

**`bio_driver2`** 供提供者私有使用。

**`bio_caller1`** 供消费者私有使用。

**`bio_caller2`** 供消费者私有使用。

**`bio_attribute`** `BIO_GETATTR` 请求的属性字符串。

**`bio_from`** 用于请求的消费者（附加到存储在 `bio_to` 字段中的提供者）（通常对类只读）。

**`bio_to`** 目标提供者（通常对类只读）。

**`bio_length`** 请求长度（字节）。

**`bio_completed`** 已完成的字节数，但可能不是从请求的开头完成的。

**`bio_children`** `bio` 克隆数（通常对类只读）。

**`bio_inbed`** 已完成的 `bio` 克隆数。

**`bio_parent`** 指向父 `bio` 的指针。

`g_new_bio` 函数分配一个新的空 `bio` 结构。

`g_alloc_bio` — 与 `g_new_bio` 相同，但始终成功（使用 `M_WAITOK` malloc 标志分配 bio）。

`g_clone_bio` 函数分配一个新的 `bio` 结构，并从作为参数传递给克隆的 `bio` 中复制以下字段：`bio_cmd`、`bio_length`、`bio_offset`、`bio_data`、`bio_attribute`。克隆中的 `bio_parent` 字段指向传递的 `bio`，传递的 `bio` 中的 `bio_children` 字段递增。

此函数应用于每个通过特定 geom 的提供者进入并需要向下调度的请求。正确顺序为：

- 克隆接收到的 `struct bio`。
- 修改克隆。
- 在自己的消费者上调度克隆。

`g_duplicate_bio` — 与 `g_clone_bio` 相同，但始终成功（使用 `M_WAITOK` malloc 标志分配 bio）。

`g_destroy_bio` 函数释放并销毁给定的 `bio` 结构。

`g_format_bio` 函数将给定 `bio` 结构的信息打印到提供的 `sbuf` 中。

`g_print_bio` 函数是 `g_format_bio` 的便捷包装，可用于调试目的。它打印提供的 `prefix` 字符串，后跟格式化的 `bio`，再后跟 [printf(9)](printf.9.md) 风格的 `fmtsuffix`。prefix 或 suffix 字符串可为空字符串。`g_print_bio` 始终在行尾打印换行符。

`g_reset_bio` 函数将给定的 `bio` 结构重置回初始状态。`g_reset_bio` 保留内部数据结构，同时将所有用户可见字段设置为其初始值。当重用从 `g_new_bio`、`g_alloc_bio`、`g_clone_bio` 或 `g_duplicate_bio` 获取的 `bio` 进行多次事务时，必须在事务之间调用 `g_reset_bio` 以替代 `bzero`。虽然对于通过其他方式创建的 `bio` 结构并非严格要求，但应使用 `g_reset_bio` 来初始化它及在事务之间使用。

## 返回值

`g_new_bio` 和 `g_clone_bio` 函数返回指向分配的 `bio` 的指针，发生错误时返回 `NULL`。

## 实例

实现 “`NULL` 转换”，即 I/O 请求被克隆并向下调度而无需任何修改。假设 `example_softc` 结构中的 `ex_consumer` 字段包含一个附加到我们要操作的提供者的消费者。

```c
void
example_start(struct bio *bp)
{
	struct example_softc *sc;
	struct bio *cbp;
	g_print_bio("Request received: ", bp, "");
	sc = bp->bio_to->geom->softc;
	if (sc == NULL) {
		g_io_deliver(bp, ENXIO);
		return;
	}
	/* 让我们克隆 bio 请求。 */
	cbp = g_clone_bio(bp);
	if (cbp == NULL) {
		g_io_deliver(bp, ENOMEM);
		return;
	}
	cbp->bio_done = g_std_done;	/* 标准“完成”函数。 */
	/* 好，向下调度它。 */
	/*
	 * 消费者也可以从
	 * LIST_FIRST(&bp->bio_to->geom->consumer) 获取，
	 * 如果我们的 geom 中只有一个的话。
	 */
	g_io_request(cbp, sc->ex_consumer);
}
```

## 参见

[dtrace_io(4)](../man4/dtrace_io.4.md), [geom(4)](../man4/geom.4.md), [DECLARE_GEOM_CLASS(9)](declare_geom_class.9.md), [g_access(9)](g_access.9.md), [g_attach(9)](g_attach.9.md), [g_consumer(9)](g_consumer.9.md), [g_data(9)](g_data.9.md), [g_event(9)](g_event.9.md), [g_geom(9)](g_geom.9.md), [g_provider(9)](g_provider.9.md), [g_provider_by_name(9)](g_provider_by_name.9.md), [g_wither_geom(9)](g_wither_geom.9.md)

## 作者

本手册页由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 编写。
