# coredumper_register(9)

`coredumper_register` — 可加载的用户核心转储器支持

## 名称

`coredumper_register`, `coredumper_unregister`

## 概要

```c
#include <sys/ucoredump.h>

void
coredumper_register(struct coredumper *cd)

void
coredumper_unregister(struct coredumper *cd)

int
coredumper_probe_fn(struct thread *td)

int
coredumper_handle_fn(struct thread *td, off_t limit)

/* 不完整，但此处描绘了有用的成员。 */
struct coredumper {
	const char		*cd_name;
	coredumper_probe_fn	*cd_probe;
	coredumper_handle_fn	*cd_handle;
};

int
coredump_init_fn(const struct coredump_writer *,
    const struct coredump_params *)

int
coredump_write_fn(const struct coredump_writer *, const void *, size_t,
    off_t, enum uio_seg, struct ucred *, size_t *, struct thread *)

int
coredump_extend_fn(const struct coredump_writer *, off_t,
    struct ucred *)

struct coredump_writer {
	void			*ctx;
	coredump_init_fn	*init_fn;
	coredump_write_fn	*write_fn;
	coredump_extend_fn	*extend_fn;
};
```

## 描述

`coredumper_register` 机制为内核模块提供注册新用户进程核心转储器的途径。`coredumper_register` 的预期用法是模块定义上述 struct coredumper 的字段，然后在 `MOD_LOAD` 时调用 `coredumper_register`。应在 `MOD_UNLOAD` 时调用相应的 `coredumper_unregister`。注意，`coredumper_unregister` 将阻塞，直到指定的核心转储器不再处理核心转储。

当用户进程准备开始转储核心时，内核将为当前注册的每个核心转储器执行 `cd_probe` 函数。`cd_probe` 函数应返回 -1（如果拒绝转储该进程）或大于 0 的优先级。具有最高优先级的 coredumper 将处理核心转储。定义了以下默认优先级：

**`COREDUMPER_NOMATCH`** 此转储器拒绝转储该进程。

**`COREDUMPER_GENERIC`** 此转储器将以最低优先级转储进程。不推荐使用此优先级，因为默认的 vnode 转储器也会以 `COREDUMPER_GENERIC` 竞标。

**`COREDUMPER_SPECIAL`** 此转储器提供特殊行为，将以较高优先级转储进程。

**`COREDUMPER_HIGHPRIORITY`** 此转储器希望处理此核心转储。例如，可由希望抢占其他机制的自定义或厂商特定核心转储机制使用。

注意，此系统的设计使得 `cd_probe` 函数可以检查所讨论的进程并做出明智的决策。同一 coredumper 中被转储的不同进程可以以不同优先级探测。

一旦选择了最高优先级的 coredumper，将调用 `cd_handle` 函数。`cd_handle` 将接收线程和 `RLIMIT_CORE` [setrlimit(2)](../sys/getrlimit.2.md) `limit`。进入时持有 proc 锁，应在处理程序返回之前解锁。`limit` 通常传递给属于进程 `p_sysent` 的 `sv_coredump`。

`cd_handle` 函数应在转储成功时返回 0，否则返回适当的 [errno(2)](../sys/intro.2.md)。

### 自定义核心转储写入器

自定义 coredumper 可以定义自己的 `coredump_writer` 以传递给 `sv_coredump`。

`ctx` 成员是不透明的，仅供 coredumper 自身使用。

`init_fn` 函数（如果提供）将在写入任何数据之前由 `sv_coredump` 实现调用。这允许写入器实现记录可能需要捕获的任何核心转储参数，或设置要写入的对象。

`write_fn` 函数将由 `sv_coredump` 实现调用以写出数据。`extend_fn` 函数将被调用以扩大核心转储，即在当前大小和新大小之间的任何差异中创建空洞。为方便起见，vnode coredumper 使用的 `core_vn_write` 和 `core_vn_extend` 函数在 `#include <sys/ucordumper.h>` 中公开，并且在那里定义的 `coredump_vnode_ctx` 应填充要写入的 vnode。

## 参见

[setrlimit(2)](../sys/getrlimit.2.md), [core(5)](../man5/core.5.md)

## 作者

本手册页由 Kyle Evans <kevans@FreeBSD.org> 编写。
