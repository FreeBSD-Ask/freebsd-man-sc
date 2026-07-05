# sbuf.9

`sbuf` — 安全字符串组合

## 名称

`sbuf`, `sbuf_new`, `sbuf_new_auto`, `sbuf_new_for_sysctl`, `sbuf_clear`, `sbuf_get_flags`, `sbuf_set_flags`, `sbuf_clear_flags`, `sbuf_setpos`, `sbuf_bcat`, `sbuf_bcopyin`, `sbuf_bcpy`, `sbuf_cat`, `sbuf_copyin`, `sbuf_cpy`, `sbuf_nl_terminate`, `sbuf_printf`, `sbuf_vprintf`, `sbuf_putc`, `sbuf_set_drain`, `sbuf_trim`, `sbuf_error`, `sbuf_finish`, `sbuf_data`, `sbuf_len`, `sbuf_done`, `sbuf_delete`, `sbuf_start_section`, `sbuf_end_section`, `sbuf_hexdump`, `sbuf_printf_drain`, `sbuf_putbuf`

## 库

libsbuf

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/sbuf.h>
```

```c
typedef int (sbuf_drain_func)(void *arg, const char *data, int len)
```

```c
struct sbuf *
sbuf_new(struct sbuf *s, char *buf, int length, int flags)

struct sbuf *
sbuf_new_auto(void)

void
sbuf_clear(struct sbuf *s)

int
sbuf_get_flags(struct sbuf *s)

void
sbuf_set_flags(struct sbuf *s, int flags)

void
sbuf_clear_flags(struct sbuf *s, int flags)

int
sbuf_setpos(struct sbuf *s, int pos)

int
sbuf_bcat(struct sbuf *s, const void *buf, size_t len)

int
sbuf_bcpy(struct sbuf *s, const void *buf, size_t len)

int
sbuf_cat(struct sbuf *s, const char *str)

int
sbuf_cpy(struct sbuf *s, const char *str)

int
sbuf_nl_terminate(struct sbuf *)

int
sbuf_printf(struct sbuf *s, const char *fmt, ...)

int
sbuf_vprintf(struct sbuf *s, const char *fmt, va_list ap)

int
sbuf_putc(struct sbuf *s, int c)

void
sbuf_set_drain(struct sbuf *s, sbuf_drain_func *func, void *arg)

int
sbuf_trim(struct sbuf *s)

int
sbuf_error(struct sbuf *s)

int
sbuf_finish(struct sbuf *s)

char *
sbuf_data(struct sbuf *s)

ssize_t
sbuf_len(struct sbuf *s)

int
sbuf_done(struct sbuf *s)

void
sbuf_delete(struct sbuf *s)

void
sbuf_start_section(struct sbuf *s, ssize_t *old_lenp)

ssize_t
sbuf_end_section(struct sbuf *s, ssize_t old_len, size_t pad, int c)

void
sbuf_hexdump(struct sbuf *sb, void *ptr, int length, const char *hdr, int flags)

int
sbuf_printf_drain(void *arg, const char *data, int len)

void
sbuf_putbuf(struct sbuf *s)
```

```c
#ifdef _KERNEL
```

```c
#include <sys/types.h>
```

```c
#include <sys/sbuf.h>
```

```c
int
sbuf_bcopyin(struct sbuf *s, const void *uaddr, size_t len)

int
sbuf_copyin(struct sbuf *s, const void *uaddr, size_t len)
```

```c
#include <sys/sysctl.h>
```

```c
struct sbuf *
sbuf_new_for_sysctl(struct sbuf *s, char *buf, int length, struct sysctl_req *req)
```

```c
#endif /* _KERNEL */
```

## 描述

`sbuf` 函数族允许在内核空间或用户空间中安全地分配、组合和释放字符串。

这些函数不是操作字符数组，而是操作称为 `sbufs` 的结构，该结构定义在

```c
#include <sys/sbuf.h>
```

中。

在字符串分配或组合过程中遇到的任何错误都会被锁存在数据结构中，使得在组合结束时进行单次错误测试即可确定整个过程的成功或失败。

`sbuf_new` 函数初始化由其第一个参数所指向的 `sbuf`。如果该指针为 `NULL`，`sbuf_new` 会使用 [malloc(9)](malloc.9.md) 分配一个 `struct sbuf`。`buf` 参数是指向用于存储实际字符串的缓冲区的指针；如果为 `NULL`，`sbuf_new` 将使用 [malloc(9)](malloc.9.md) 分配一个。`length` 是存储缓冲区的初始大小。第四个参数 `flags` 可由以下标志组成：

**`SBUF_FIXEDLEN`** 存储缓冲区固定为其初始大小。尝试将 sbuf 扩展到此大小之外会导致溢出条件。

**`SBUF_AUTOEXTEND`** 这表示存储缓冲区可以在资源允许的情况下根据需要扩展，以容纳额外数据。

**`SBUF_INCLUDENUL`** 这使得最后的 nulterm 字节被计入数据长度中。

**`SBUF_DRAINTOEOR`** 将由 `sbuf_start_section` 启动的顶层节视为记录边界标记，该标记将在 drain 操作期间使用，以避免记录被分割。如果记录增长到足够大以至于填满了 `sbuf`，因此无法在不被分割的情况下排空，将设置 `EDEADLK` 错误。

**`SBUF_NOWAIT`** 表示在低内存条件下扩展存储缓冲区的尝试应该失败，类似于 [malloc(9)](malloc.9.md) 的 `M_NOWAIT`。

注意，如果 `buf` 不为 `NULL`，它必须指向一个至少有 `length` 个字符的数组。在 sbuf 使用该数组期间直接访问它的结果是未定义的。

`sbuf_new_auto` 函数是创建完全动态 `sbuf` 的快捷方式。它等价于以 `NULL`、`NULL`、`0` 和 `SBUF_AUTOEXTEND` 为值调用 `sbuf_new`。

`sbuf_new_for_sysctl` 函数将设置一个带有 drain 函数的 sbuf，以便在内部缓冲区填满时使用 `SYSCTL_OUT`。注意，如果在持有非可睡眠锁时使用追加到 sbuf 的各种函数，应使用 `sysctl_wire_old_buffer` 锁定用户缓冲区。

`sbuf_delete` 函数清除 `sbuf` 并释放为其分配的任何内存。每次调用 `sbuf_new` 都必须对应一次 `sbuf_delete` 调用。在 sbuf 被删除后，任何访问它的尝试都将失败。

`sbuf_clear` 函数使 `sbuf` 的内容无效，并将其位置重置为零。

`sbuf_get_flags` 函数返回当前用户标志。`sbuf_set_flags` 和 `sbuf_clear_flags` 函数分别设置或清除一个或多个用户标志。用户标志在 `sbuf_new` 函数下描述。

`sbuf_setpos` 函数将 `sbuf` 的结束位置设置为 `pos`，该值介于零和缓冲区中的当前位置之间。它只能将 sbuf 截断到新位置。

`sbuf_bcat` 函数将缓冲区 `buf` 的前 `len` 字节追加到 `sbuf`。

`sbuf_bcopyin` 函数将 `len` 字节从指定的用户空间地址复制到 `sbuf` 中。

`sbuf_bcpy` 函数用缓冲区 `buf` 的前 `len` 字节替换 `sbuf` 的内容。

`sbuf_cat` 函数将 NUL 结尾的字符串 `str` 追加到 `sbuf` 的当前位置。

`sbuf_set_drain` 函数为 `sbuf` 设置 drain 函数 `func`，并记录一个指针 `arg` 以便在回调时传递给 drain。当 `sbuf_len` 非零时，不能更改 drain 函数。

注册的 drain 函数 `sbuf_drain_func` 将被调用，参数包括传递给 `sbuf_set_drain` 的参数 `arg`、指向作为 sbuf 内容的字节字符串的指针 `data`，以及数据的长度 `len`。如果 drain 函数存在，它将在 sbuf 内部缓冲区满时或代表 `sbuf_finish` 被调用。drain 函数可以排空部分或全部数据，但必须至少排空 1 字节。drain 函数的返回值如果为正，表示已排空的字节数。如果为负，返回值表示负的错误代码，该代码将从此次或后续的 `sbuf_finish` 调用中返回。如果返回的排空长度为 0，将设置 `EDEADLK` 错误。要进行无缓冲排空，请使用两字节的缓冲区初始化 sbuf。每向 sbuf 添加一个字节都会调用 drain。`sbuf_bcopyin`、`sbuf_bcpy`、`sbuf_clear`、`sbuf_copyin`、`sbuf_cpy`、`sbuf_trim`、`sbuf_data` 和 `sbuf_len` 函数不能用于带有 drain 的 sbuf。

`sbuf_copyin` 函数将 NUL 结尾的字符串从指定的用户空间地址复制到 `sbuf` 中。如果 `len` 参数非零，复制的字符数（不包括结尾的 NUL）不超过 `len` 个；否则复制整个字符串，或尽可能多地复制能放入 `sbuf` 的部分。

`sbuf_cpy` 函数用 NUL 结尾的字符串 `str` 的内容替换 `sbuf` 的内容。这等价于在一个新的 `sbuf` 或位置已通过 `sbuf_clear` 或 `sbuf_setpos` 重置为零的 `sbuf` 上调用 `sbuf_cat`。

`sbuf_nl_terminate` 函数在当前行非空且尚未以换行符结尾时，追加一个尾随换行符。

`sbuf_printf` 函数根据 `fmt` 所指向的格式字符串格式化其参数，并将结果字符串追加到 `sbuf` 的当前位置。

`sbuf_vprintf` 函数的行为与 `sbuf_printf` 相同，只是参数来自可变长度参数列表 `ap`。

`sbuf_putc` 函数将字符 `c` 追加到 `sbuf` 的当前位置。

`sbuf_trim` 函数从 `sbuf` 中移除尾随空白字符。

`sbuf_error` 函数返回 `sbuf` 可能累积的任何错误值，无论是来自 drain 函数，还是 `ENOMEM`（如果 `sbuf` 溢出）。通常不需要此函数，而是使用 `sbuf_finish` 的错误代码来发现 sbuf 是否有错误。

`sbuf_finish` 函数将在存在已附加的 drain 函数时调用它，直到 `sbuf` 中的所有数据都被刷新。如果没有附加的 drain，`sbuf_finish` 将对 `sbuf` 进行 NUL 终止。无论哪种情况，它都会将 `sbuf` 标记为已完成，这意味着在调用 `sbuf_clear` 重置 sbuf 之前，不能再使用 `sbuf_setpos`、`sbuf_cat`、`sbuf_cpy`、`sbuf_printf` 或 `sbuf_putc` 修改它。

`sbuf_data` 函数返回实际的字符串；`sbuf_data` 仅对已完成的 `sbuf` 有效。`sbuf_len` 函数返回字符串的长度。对于带有附加 drain 的 `sbuf`，`sbuf_len` 返回未排空数据的长度。如果 `sbuf` 已完成，`sbuf_done` 返回非零值。

`sbuf_start_section` 和 `sbuf_end_section` 函数可用于自动节对齐。参数 `pad` 和 `c` 指定填充大小和用于填充的字符。参数 `old_lenp` 和 `old_len` 用于在使用嵌套节时保存和恢复当前节长度。对于顶层节，可以分别为 `old_lenp` 和 `old_len` 指定 `NULL` 和 -1。

`sbuf_hexdump` 函数将字节数组打印到提供的 sbuf，如果可能，还包括字节的 ASCII 表示。有关接口的更多详情，请参见 hexdump(3) 手册页面。

`sbuf_printf_drain` 函数是一个 drain 函数，它将调用 printf，或记录到控制台。参数 `arg` 必须是 `NULL`，或是指向 `size_t` 的有效指针。如果 `arg` 不为 `NULL`，已排空的总字节数将加到 `arg` 所指向的值上。

`sbuf_putbuf` 函数如果在用户空间则将 sbuf printf 到 stdout，如果在内核中则输出到控制台和日志。在调用 `sbuf_putbuf` 之前，`sbuf` 必须已完成。它不会排空缓冲区或更新任何指针。

## 注释

如果某个操作导致 `sbuf` 溢出，则在其上执行的大多数后续操作都将失败，直到使用 `sbuf_finish` 完成 `sbuf` 或使用 `sbuf_clear` 重置，或使用 `sbuf_setpos` 将其位置重置为介于 0 和其存储缓冲区大小减一之间的值，或使用 `sbuf_cpy` 将其重新初始化为足够短的字符串。

用户空间中的 drain 并不总是如所述那样工作。虽然 drain 函数会在 `sbuf_putc`、`sbuf_bcat`、`sbuf_cat` 函数溢出时立即被调用，但 `sbuf_printf` 和 `sbuf_vprintf` 目前无法在溢出发生之前确定是否会发生溢出，并且无法对格式字符串进行部分展开。因此，使用 libsbuf 时，即使附加了 drain，缓冲区也可能被扩展以允许完成单次 printf 调用。

## 返回值

`sbuf_new` 函数如果未能分配存储缓冲区则返回 `NULL`，否则返回指向新 `sbuf` 的指针。

`sbuf_setpos` 函数如果 `pos` 无效则返回 -1，否则返回零。

`sbuf_bcat`、`sbuf_cat`、`sbuf_cpy`、`sbuf_printf`、`sbuf_putc` 和 `sbuf_trim` 函数在缓冲区溢出时都返回 -1，否则返回零。

`sbuf_error` 函数如果缓冲区有溢出或 drain 错误则返回非零值，否则返回零。

`sbuf_len` 函数在缓冲区溢出时返回 -1。

`sbuf_copyin` 函数如果从用户空间复制字符串失败则返回 -1，否则返回复制的字节数。

`sbuf_end_section` 函数返回节长度，如果缓冲区有错误则返回 -1。

`sbuf_finish` 9 函数（内核版本）如果 sbuf 在完成之前溢出则返回 `ENOMEM`，或如果附加了 drain 则返回来自 drain 的错误代码。

`sbuf_finish` 3 函数（用户空间版本）成功时返回零，出错时返回 -1 并设置 errno。

## 实例

```c
#include <sys/types.h>
#include <sys/sbuf.h>
struct sbuf *sb;
sb = sbuf_new_auto();
sbuf_cat(sb, "Customers found:\n");
TAILQ_FOREACH(foo, &foolist, list) {
	sbuf_printf(sb, "   %4d %s\n", foo->index, foo->name);
	sbuf_printf(sb, "      Address: %s\n", foo->address);
	sbuf_printf(sb, "      Zip: %s\n", foo->zipcode);
}
if (sbuf_finish(sb) != 0) /* 检查任何和所有错误 */
	err(1, "Could not generate message");
transmit_msg(sbuf_data(sb), sbuf_len(sb));
sbuf_delete(sb);
```

## 参见

hexdump(3), printf(3), strcat(3), strcpy(3), copyin(9), copyinstr(9), [printf(9)](printf.9.md)

## 历史

`sbuf` 函数族首次出现在 FreeBSD 4.4 中。

## 作者

`sbuf` 函数族由 Poul-Henning Kamp <phk@FreeBSD.org> 设计，由 Dag-Erling Smørgrav <des@FreeBSD.org> 实现。Justin T. Gibbs <gibbs@FreeBSD.org> 提出了额外的改进建议。Kelly Yancey <kbyanc@FreeBSD.org> 添加了自动扩展支持。Matthew Fleming <mdf@FreeBSD.org> 添加了 drain 功能。

本手册页面由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
