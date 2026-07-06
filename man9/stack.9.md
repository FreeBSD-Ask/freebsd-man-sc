# stack.9

`stack` — 内核线程栈跟踪例程

## 名称

`stack`

## 概要

```c
#include <sys/param.h>
#include <sys/stack.h>

在内核配置文件中：
options DDB
options STACK

struct stack *
stack_create(int flags)

void
stack_destroy(struct stack *st)

int
stack_put(struct stack *st, vm_offset_t pc)

void
stack_copy(const struct stack *src, struct stack *dst)

void
stack_zero(struct stack *st)

void
stack_print(const struct stack *st)

void
stack_print_ddb(const struct stack *st)

void
stack_print_short(const struct stack *st)

void
stack_print_short_ddb(const struct stack *st)

void
stack_sbuf_print(struct sbuf *sb, const struct stack *st)

void
stack_sbuf_print_ddb(struct sbuf *sb, const struct stack *st)

void
stack_save(struct stack *st)

int
stack_save_td(struct stack *st, struct thread *td)
```

## 描述

`stack` KPI 允许查询内核栈跟踪信息，并出于调试和跟踪的目的自动生成内核栈跟踪字符串。要使用该 KPI，内核中必须编译 `options DDB` 或 `options STACK` 中的至少一个。

每个栈跟踪由 `struct stack` 描述。它可以以通常的方式声明，包括在栈上声明，并可选地使用 `stack_zero` 初始化，但在保存跟踪之前这不是必需的。它也可以使用 `stack_create` 动态分配。`flags` 参数传递给 [malloc(9)](malloc.9.md)。此动态分配必须使用 `stack_destroy` 释放。

可以使用 `stack_save` 捕获当前线程内核调用栈的跟踪。`stack_save_td` 可用于捕获调用者指定线程的内核栈。`stack_save_td` 的调用者必须拥有指定线程的线程锁，且线程的栈不能被换出。`stack_save_td` 可以捕获正在运行的线程的内核栈，但注意并非所有平台都实现了此功能。如果线程正在运行，调用者还必须持有目标线程的进程锁。

`stack_print` 和 `stack_print_short` 可用于使用内核 [printf(9)](printf.9.md) 打印栈跟踪，并且由于在查找符号名时获取内核链接器中的 [sx(9)](sx.9.md) 锁而可能睡眠。在对锁敏感的环境中，可以调用未同步的 `stack_print_ddb` 和 `stack_print_short_ddb` 变体。此函数绕过内核链接器锁定，使其可用于 [ddb(4)](../man4/ddb.4.md)，但不能在链接器数据结构可能更改的实时系统中使用。

`stack_sbuf_print` 可用于构造人类可读的字符串，包括（在可能的情况下）从简单的内核指令指针转换为命名符号和偏移量。参数 `sb` 必须是 [sbuf(9)](sbuf.9.md) 中描述的已初始化的 `struct sbuf`。如果使用自动扩展的 `struct sbuf`，或由于内核链接器锁定，此函数可能睡眠。在对锁敏感的环境中（如 [ddb(4)](../man4/ddb.4.md)），可以调用未同步的 `stack_sbuf_print_ddb` 变体以避免内核链接器锁定；它应与固定长度的 sbuf 一起使用。

实用函数 `stack_zero`、`stack_copy` 和 `stack_put` 可用于直接操作栈数据结构。

## 返回值

`stack_put` 成功时返回 0。否则 `struct stack` 没有空间记录额外的帧，返回非零值。

`stack_save_td` 在栈捕获成功时返回 0，否则返回非零错误号。特别是，如果在尝试捕获时线程正在用户模式下运行，则返回 `EBUSY`；如果操作未实现，则返回 `EOPNOTSUPP`。

## 参见

[ddb(4)](../man4/ddb.4.md), [printf(9)](printf.9.md), [sbuf(9)](sbuf.9.md), [sx(9)](sx.9.md)

## 作者

`stack_put` 函数套件由 Antoine Brodin 创建。`stack_put` 由 Robert Watson 扩展，用于 [ddb(4)](../man4/ddb.4.md) 之外的通用用途。
