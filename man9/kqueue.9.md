# kqueue(9)

`kqueue_add_filteropts` — 事件传递子系统

## 名称

`kqueue_add_filteropts`, `kqfd_register`, `knote_fdclose`, `knlist_init`, `knlist_add`, `knlist_clear`, `KNOTE_LOCKED`

## 概要

```c
#include <sys/event.h>
```

```c
int
kqueue_add_filteropts(int filt, struct filterops *filtops)

int
kqueue_del_filteropts(int filt)

int
kqfd_register(int fd, struct kevent *kev, struct thread *td, int waitok)

void
knote_fdclose(struct thread *td, int fd)

void
knlist_init(struct knlist *knl, void *lock,
    void *kl_lock(void *), void *kl_unlock(void *),
    int *kl_locked(void *))

void
knlist_init_mtx(struct knlist *knl, struct mtx *lock)

void
knlist_add(struct knlist *knl, struct knote *kn, int islocked)

void
knlist_remove(struct knlist *knl, struct knote *kn, int islocked)

int
knlist_empty(struct knlist *knl)

void
knlist_clear(struct knlist *knl, int islocked)

void
knlist_delete(struct knlist *knl, struct thread *td, int islocked)

void
knlist_destroy(struct knlist *knl)

void
KNOTE_LOCKED(struct knlist *knl, long hint)

void
KNOTE_UNLOCKED(struct knlist *knl, long hint)
```

## 描述

`kqueue_add_filteropts` 和 `kqueue_del_filteropts` 函数允许添加和删除过滤器类型。过滤器由 `EVFILT_*` 宏静态定义。`kqueue_add_filteropts` 函数将使 `filt` 可用。`struct filterops` 具有以下成员：

**`f_isfd`** 如果设置了 `f_isfd`，则 `struct kevent` 中的 `ident` 被视为文件描述符。在这种情况下，传递给 `f_attach` 的 `knote` 将把 `kn_fp` 成员初始化为表示该文件描述符的 `struct file *`。

**`f_attach`** 当将 `knote` 附加到对象时将调用 `f_attach` 函数。该方法应调用 `knlist_add` 将 `knote` 添加到使用 `knlist_init` 初始化的列表中。只有在对象可以关联多个 `knotes` 时才需要调用 `knlist_add`。如果没有 `knlist` 可调用 `knlist_add`，函数 `f_attach` 必须清除 `knote` 中 `kn_status` 的 `KN_DETACHED` 位。函数成功时返回 0，失败时返回适当的错误，例如对象正在被销毁或不存在时。在 `f_attach` 期间，可以将 `kn_fop` 指针更改为不同的指针。这将更改处理 `knote` 时调用的 `f_event` 和 `f_detach` 函数。

**`f_detach`** 如果 `knote` 尚未通过调用 `knlist_remove` 或 `knlist_delete` 摘除，则将调用 `f_detach` 函数来摘除 `knote`。调用此函数时不持有列表 `lock`。

**`f_event`** 将调用 `f_event` 函数来更新 `knote` 的状态。如果函数返回 0，将假定对象未准备好（或不再准备好）被唤醒。当扫描 `knotes` 以查看哪些被触发时，`hint` 参数将为 0。否则，`hint` 参数将是传递给 `KNOTE_LOCKED` 或 `KNOTE_UNLOCKED` 的值。`kn_data` 值应按需更新以反映当前值，例如可供读取的字节数或可供写入的缓冲区空间。在 `f_event` 中*不得*获取锁。如果 `f_event` 中需要锁，则必须在 `knote` 添加到的 `knlist` 的 `kl_lock` 函数中获取。

**`f_copy`** 当进程分叉时调用 `f_copy` 函数来复制 note。当为 `NULL` 时，当前节点不会复制到子进程。除了 knote 本身的浅拷贝之外不需要额外处理时，过滤器可以将 `f_copy` 设置为 `knote_triv_copy`。

`kqfd_register` 函数将在 kqueue 文件描述符 `fd` 上注册 `kevent`。如果可以安全休眠，应设置 `waitok`。

`knote_fdclose` 函数用于删除与 `fd` 关联的所有 `knotes`。返回后，将不再有任何 `knotes` 与 `fd` 关联。移除的 `knotes` 永远不会从 kevent(2) 调用返回，因此如果用户态使用 `knote` 跟踪资源，这些资源将会泄漏。在调用 `knote_fdclose` 期间必须持有 `FILEDESC_LOCK` 锁，以防止文件描述符被添加或删除。

`knlist_*` 函数系列用于管理与对象关联的 `knotes`。`knlist` 不是必需的，但很常用。如果使用，`knlist` 必须使用 `knlist_init` 或 `knlist_init_mtx` 初始化。`knlist` 结构可以嵌入到对象结构中。在 `f_event` 调用期间将持有 `lock`。

对于 `knlist_init` 函数，如果 `lock` 为 `NULL`，将使用共享全局锁，其余参数必须为 `NULL`。函数指针 `kl_lock`、`kl_unlock` 和 `kl_locked` 将用于操作参数 `lock`。如果任何函数指针为 `NULL`，将使用操作 `MTX_DEF` 风格 [mutex(9)](mutex.9.md) 锁的函数。

`knlist_init_mtx` 函数可用于在 `lock` 为 `MTX_DEF` 风格 [mutex(9)](mutex.9.md) 锁时初始化 `knlist`。

`knlist_empty` 函数在列表中没有 `knotes` 时返回 true。该函数要求在调用时持有 `lock`。

`knlist_clear` 函数从列表中移除所有 `knotes`。`islocked` 参数声明是否已获取 `lock`。所有 `knotes` 将设置 `EV_ONESHOT`，以便在下次扫描期间返回并移除 `knote`。当 `knote` 在下次扫描期间被删除时将调用 `f_detach` 函数。

`knlist_delete` 函数移除并删除列表上的所有 `knotes`。不会调用 `f_detach` 函数，`knote` 也不会在下次扫描时返回。如果进程使用 `knote` 跟踪资源，使用此函数可能会泄漏用户态资源。

`knlist_clear` 和 `knlist_delete` 函数都可能会休眠。它们也可能释放 `lock` 以等待其他 `knotes` 排空。

`knlist_destroy` 函数用于销毁 `knlist`。必须没有 `knotes` 与 `knlist` 关联（`knlist_empty` 返回 true），并且不能再有 `knotes` 附加到该对象。可以通过调用 `knlist_clear` 或 `knlist_delete` 来清空 `knlist`。

`KNOTE_LOCKED` 和 `KNOTE_UNLOCKED` 宏用于通知 `knotes` 与对象相关的事件。它将遍历列表上的所有 `knotes`，调用与 `knote` 关联的 `f_event` 函数。如果持有与 `knl` 关联的锁，必须使用 `KNOTE_LOCKED` 宏。`KNOTE_UNLOCKED` 函数将在遍历 `knotes` 列表之前获取锁。

## 返回值

`kqueue_add_filteropts` 函数成功时返回零，`filt` 无效时返回 EINVAL，如果过滤器已安装则返回 EEXIST。

`kqueue_del_filteropts` 函数成功时返回零，`filt` 无效时返回 EINVAL，如果过滤器仍在使用则返回 EBUSY。

`kqfd_register` 函数成功时返回零，如果文件描述符不是 kqueue 则返回 EBADF，或返回 kevent(2) 可能返回的任何值。

## 参见

kevent(2), kqueue(2)

## 作者

本手册页由 John-Mark Gurney <jmg@FreeBSD.org> 编写。
