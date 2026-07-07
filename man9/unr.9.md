# unr(9)

`new_unrhdr` — 内核单元号分配器

## 名称

`new_unrhdr`, `clean_unrhdr`, `clear_unrhdr`, `delete_unrhdr`, `alloc_unr`, `alloc_unr_specific`, `free_unr`, `create_iter_unr`, `next_iter_unr`, `free_iter_unr`

## 概要

`#include <sys/systm.h>`

`struct unrhdr * new_unrhdr(int low, int high, struct mtx *mutex)`

`void clean_unrhdr(struct unrhdr *uh)`

`void clean_unrhdrl(struct unrhdr *uh)`

`void clear_unrhdr(struct unrhdr *uh)`

`void delete_unrhdr(struct unrhdr *uh)`

`int alloc_unr(struct unrhdr *uh)`

`int alloc_unrl(struct unrhdr *uh)`

`int alloc_unr_specific(struct unrhdr *uh, u_int item)`

`void free_unr(struct unrhdr *uh, u_int item)`

`void * create_iter_unr(struct unrhdr *uh)`

`int next_iter_unr(void *handle)`

`void free_iter_unr(void *handle)`

## 描述

内核单元号分配器是一个通用设施，允许在指定范围内分配单元号。

**`new_unrhdr(low, high, mutex)`** 初始化一个新的单元号分配器实体。`low` 和 `high` 参数指定单元号的最小和最大值。单元号的范围不产生任何开销，因此除非资源确实有限，否则可使用 `INT_MAX`。如果 `mutex` 不为 `NULL`，则在分配和释放单元时用于加锁。如果传递的值为令牌 `UNR_NO_MTX`，则内部不应用任何锁定。否则，使用内部互斥锁。

**`clear_unrhdr(uh)`** 从指定的单元号分配器实体中清除所有单元。此函数重置实体，使其就像刚刚通过 `new_unrhdr()` 初始化一样。

**`delete_unrhdr(uh)`** 删除指定的单元号分配器实体。此函数释放与该实体关联的内存，不释放任何单元。要释放所有单元，请使用 `clear_unrhdr()`。

**`clean_unrhdr(uh)`** 释放单元号可能会导致一些内部内存变得不再使用。有些单元分配器使用者无法容忍在持有其单元互斥锁的情况下获取 [malloc(9)](malloc.9.md) 锁来释放内存。因此，删除后未使用内存的释放被推迟到使用者可以调用 [malloc(9)](malloc.9.md) 子系统时进行。调用 `clean_unrhdr(uh)` 来执行清理。特别是，如果可能执行过单元删除，则在释放 unr 之前需要执行此操作。

**`clean_unrhdrl`** 与 `clean_unrhdr()` 相同，但假定 unr 互斥锁（如果有）已被持有。

**`alloc_unr(uh)`** 返回一个新的单元号。始终分配最低的空闲编号。此函数不分配内存且从不睡眠，但可能在互斥锁上阻塞。如果没有剩余的空闲单元号，则返回 `-1`。

**`alloc_unrl(uh)`** 与 `alloc_unr()` 相同，但假定互斥锁已被锁定，因此不使用它。

**`alloc_unr_specific(uh, item)`** 分配特定的单元号。此函数分配内存，因此可能睡眠。成功时返回分配的单元号。如果指定的编号已分配或超出范围，则返回 `-1`。

**`free_unr(uh, item)`** 释放先前分配的单元号。此函数可能需要分配内存，因此可能睡眠。没有预锁定变体。

## 迭代器接口

`unr` 设施提供了一个接口，用于迭代给定 `unrhdr` 的所有已分配单元。迭代器由不透明的句柄标识。可以同时运行多个迭代器；迭代器位置数据仅记录在迭代器句柄中。

使用者必须确保在对迭代器函数的调用之间不修改单元分配器。特别是，内部分配器互斥锁无法提供一致性，因为它在 `next_iter_unr()` 函数内部被获取和释放。如果分配器已被修改，仍然可以使用 `free_iter_unr()` 方法安全地释放迭代器。

**`create_iter_unr(uh)`** 创建一个迭代器。返回应传递给其他迭代器函数的句柄。

**`next_iter_unr(handle)`** 返回下一个单元的值。单元按升序返回。返回值 `-1` 表示迭代结束，在此情况下，所有后续调用都将返回 `-1`。

**`free_iter_unr(handle)`** 释放迭代器，句柄不再有效。

## 代码参考

上述函数实现于 `sys/kern/subr_unit.c`。

## 历史

内核单元号分配器首次出现在 FreeBSD 6.0 中。

## 作者

内核单元号分配器由 Poul-Henning Kamp 编写。本手册页由 Gleb Smirnoff 编写。
