# hash(3)

`hash` — 哈希数据库访问方法

## 名称

`hash`

## 概要

`#include <sys/types.h>`

`#include <db.h>`

## 描述

`dbopen` 例程是数据库文件的库接口。其中一种支持的文件格式是 `hash` 文件。数据库访问方法的总体描述参见 [dbopen(3)](dbopen.3.md)，本手册页面仅描述 `hash` 特有的信息。

`hash` 数据结构是一种可扩展的动态哈希方案。

提供给 `dbopen` 的访问方法专有数据结构定义在 `#include <db.h>` 头文件中，如下所示：

```c
typedef struct {
	u_int bsize;
	u_int ffactor;
	u_int nelem;
	u_int cachesize;
	uint32_t (*hash)(const void *, size_t);
	int lorder;
} HASHINFO;
```

该结构的各元素如下：

**`bsize`** `bsize` 元素定义 `hash` 表桶大小，默认为 4096 字节。对于驻留在磁盘上的表和具有大数据项的表，增大页面大小可能更可取。

**`ffactor`** `ffactor` 元素指示 `hash` 表内期望的密度。它是允许在任何单个桶中累积的键数的近似值，用于确定 `hash` 表何时增长或收缩。默认值为 8。

**`nelem`** `nelem` 元素是 `hash` 表最终大小的估计值。如果未设置或设置过低，`hash` 表会在键输入时优雅地扩展，尽管可能会注意到轻微的性能下降。默认值为 1。

**`cachesize`** 建议的内存缓存最大大小（以字节为单位）。此值*仅*是建议性的，访问方法会分配更多内存而不是失败。

**`hash`** `hash` 元素是用户定义的 `hash` 函数。由于没有 `hash` 函数能在所有可能的数据上表现同样好，用户可能发现内置 `hash` 函数在特定数据集上表现不佳。用户指定的 `hash` 函数必须接受两个参数（指向字节串的指针和长度），并返回一个 32 位量用作 `hash` 值。

**`lorder`** 存储数据库元数据中整数的字节顺序。该数字应以整数形式表示顺序；例如，大端序将是数字 4,321。如果 `lorder` 为 0（未指定顺序），则使用当前主机顺序。如果文件已存在，则忽略指定的值，转而使用创建树时指定的值。

如果文件已存在（且未指定 `O_TRUNC` 标志），则为 `bsize`、`ffactor`、`lorder` 和 `nelem` 参数指定的值将被忽略，转而使用创建树时指定的值。

如果指定了 `hash` 函数，`hash_open` 将尝试确定指定的 `hash` 函数是否与创建数据库时使用的相同，如果不同则失败。

提供了与旧版 *dbm* 和 *ndbm* 例程向后兼容的接口，但是这些接口与先前的文件格式不兼容。

## 错误

`hash` 访问方法例程可能失败并为库例程 [dbopen(3)](dbopen.3.md) 所指定的任何错误设置 `errno`。

## 参见

[btree(3)](btree.3.md), [dbopen(3)](dbopen.3.md), [mpool(3)](mpool.3.md), [recno(3)](recno.3.md)

> Per-Ake Larson, "Dynamic Hash Tables", April 1988.

> Margo Seltzer, "A New Hash Package for UNIX", Winter 1991.

## 缺陷

仅支持大端和小端字节顺序。
