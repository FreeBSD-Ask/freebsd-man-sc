# kqueue(2)

`kqueue`, `kevent` — 内核事件通知机制

## 名称

`kqueue`, `kevent`

## 库

Lb libc

## 概要

`#include <sys/event.h>`

```c
int
kqueue(void);

int
kqueuex(u_int flags);

int
kqueue1(int flags);

int
kevent(int kq, const struct kevent *changelist,
    int nchanges, struct kevent *eventlist, int nevents,
    const struct timespec *timeout);

EV_SET(kev, ident, filter, flags, fflags, data, udata);
```

## 描述

`kqueue()` 系统调用提供了一种通用方法，用于在事件发生或条件成立时通知用户，其依据是被称为过滤器的小段内核代码的执行结果。kevent 由 (ident, filter) 对标识；每个 kqueue 中每个 kevent 只能有一个唯一实例。

过滤器在 kevent 初始注册时执行，以检测是否存在预先存在的条件，并且每当有事件传递给过滤器进行评估时也会执行。如果过滤器确定应报告该条件，则将 kevent 放置在 kqueue 上供用户检索。

当用户尝试从 kqueue 检索 kevent 时，过滤器也会运行。如果过滤器指示触发事件的条件不再成立，则该 kevent 将从 kqueue 中移除并不予返回。

触发过滤器的多个事件不会导致多个 kevent 被放置在 kqueue 上；相反，过滤器会将这些事件聚合为单个 struct kevent。对文件描述符调用 `close()` 将移除任何引用该描述符的 kevent。

`kqueue()` 系统调用创建一个新的内核事件队列并返回一个描述符。该队列不会由通过 [fork(2)](fork.2.md) 创建的子进程继承。然而，如果调用 [rfork(2)](rfork.2.md) 时未指定 `RFFDG` 标志，则描述符表将被共享，这将允许两个进程之间共享 kqueue。

`kqueuex()` 系统调用也创建一个新的内核事件队列，并额外接受一个 `flags` 参数，该参数是以下标志的按位或：

**`KQUEUE_CLOEXEC`** 返回的文件描述符在 [execve(2)](execve.2.md) 时自动关闭。

**`KQUEUE_CPONFORK`** 设置此标志时，创建的 kqueue 在 [fork(2)](fork.2.md) 调用时会复制到子进程中。新 kqueue 的 kqueue 描述符索引将被子进程继承，即描述符的数值保持不变。

复制是深层的，即原始 kqueue 中的每个已注册事件都被复制（而非共享）到新 kqueue 中。这与 [fork(2)](fork.2.md) 时处理其他描述符类型的方式相反，后者中复制的文件描述符引用与源描述符相同的文件对象（浅拷贝）。

默认情况下，换言之，当未设置该标志时，父进程的 kqueue 不会在 fork 时复制到子进程。相应的文件描述符索引在子进程中未使用。

引用未在 fork 时复制的文件描述符的已注册事件，不会被复制到新 kqueue 中。例如，如果事件引用以 `O_CLOEXEC` 标志打开的文件描述符，则不会复制。类似地，如果事件引用未设置 `KQUEUE_CPONFORK` 标志打开的 kqueue，则该事件不会复制。

`kqueue()` 系统调用等效于以 `flags` 设置为 0 调用 `kqueuex()`。

`kqueue1()` 函数存在是为了与 NetBSD 兼容。`flags` 参数接受以下零个或多个值：

**`O_CLOEXEC`** 返回的文件描述符在 [execve(2)](execve.2.md) 时自动关闭。

`kevent()` 系统调用用于向队列注册事件，并将任何待处理事件返回给用户。`changelist` 参数是指向 `kevent` 结构体数组的指针，如 `#include <sys/event.h>` 中所定义。`changelist` 中包含的所有更改都在从队列读取任何待处理事件之前应用。`nchanges` 参数给出 `changelist` 的大小。`eventlist` 参数是指向 kevent 结构体数组的指针。`nevents` 参数确定 `eventlist` 的大小。当 `nevents` 为零时，即使指定了 `timeout`，`kevent()` 也会立即返回，这与 [select(2)](select.2.md) 不同。如果 `timeout` 为非 NULL 指针，它指定等待事件的最大间隔，将被解释为 struct timespec。如果 `timeout` 为 NULL 指针，`kevent()` 将无限期等待。要进行轮询，`timeout` 参数应为非 NULL，指向一个零值的 `timespec` 结构体。`changelist` 和 `eventlist` 可以使用同一数组。

`EV_SET` 宏用于方便地初始化 kevent 结构体。

`kevent` 结构体定义为：

```c
struct kevent {
        uintptr_t  ident;       /* 此事件的标识符 */
        short     filter;       /* 事件过滤器 */
        u_short   flags;        /* kqueue 的动作标志 */
        u_int     fflags;       /* 过滤器标志值 */
        int64_t   data;         /* 过滤器数据值 */
        void      *udata;       /* 不透明的用户数据标识符 */
        uint64_t  ext[4];       /* 扩展 */
};
```

`struct kevent` 的字段为：

**`ident`** 用于标识此事件的值。确切含义由所附的过滤器决定，但通常是文件描述符。

**`filter`** 标识用于处理此事件的内核过滤器。预定义的系统过滤器如下所述。

**`flags`** 对事件执行的动作。

**`fflags`** 过滤器特定的标志。

**`data`** 过滤器特定的数据值。

**`udata`** 不透明的用户定义值，通过内核原样传递。

**`ext`** 与内核之间传递的扩展数据。`ext[0]` 和 `ext[1]` 成员的含义由过滤器定义。如果过滤器不使用它们，这些成员通过内核原样传递。`ext[2]` 和 `ext[3]` 成员始终通过内核原样传递，提供额外的用户定义值。

`flags` 字段可以包含以下值：

**`EV_ADD`** 将事件添加到 kqueue。重新添加现有事件将修改原始事件的参数，不会产生重复条目。添加事件时会自动启用它，除非被 `EV_DISABLE` 标志覆盖。

**`EV_ENABLE`** 允许 `kevent()` 在事件触发时返回该事件。

**`EV_DISABLE`** 禁用事件，使 `kevent()` 不会返回它。过滤器本身未被禁用。

**`EV_DISPATCH`** 在交付事件后立即禁用事件源。参见上文 `EV_DISABLE`。

**`EV_DELETE`** 从 kqueue 中移除事件。附加到文件描述符的事件会在该描述符最后一次关闭时自动删除。

**`EV_RECEIPT`** 此标志用于在不排空任何待处理事件的情况下对 kqueue 进行批量更改。作为输入传递时，它强制始终返回 `EV_ERROR`。当过滤器成功添加时，`data` 字段将为零。注意，如果遇到此标志且 `eventlist` 中没有剩余空间来容纳 `EV_ERROR` 事件，则后续的更改将不会被处理。

**`EV_ONESHOT`** 仅返回过滤器触发的第一次出现。用户从 kqueue 检索事件后，该事件将被删除。

**`EV_CLEAR`** 在用户检索事件后重置事件状态。这对于报告状态转换而非当前状态的过滤器很有用。注意，某些过滤器可能在内部自动设置此标志。

**`EV_EOF`** 过滤器可设置此标志以指示特定于过滤器的 EOF 条件。

**`EV_ERROR`** 参见下文返回值。

**`EV_KEEPUDATA`** 保留与现有事件关联的 `udata`。这允许修改事件的其他方面，而无需调用者知道先前向事件注册的 `udata` 值。这在 `NOTE_TRIGGER` 或 `EV_ENABLE` 时特别有用。此标志不能与 `EV_ADD` 一起使用。

预定义的系统过滤器如下所列。参数可以通过 kevent 结构体中的 `fflags` 和 `data` 字段传递给过滤器或从过滤器传出。

**套接字** 先前传递给 [listen(2)](listen.2.md) 的套接字在有传入连接待处理时返回。`data` 包含 listen backlog 的大小。其他套接字描述符在有数据可读时返回，受套接字缓冲区的 `SO_RCVLOWAT` 值约束。这可以在添加过滤器时通过在 `fflags` 中设置 `NOTE_LOWAT` 标志并在 `data` 中指定新的低水位标记来按过滤器覆盖。返回时，`data` 包含可读的协议数据字节数。如果套接字的读方向已关闭，则过滤器还会在 `flags` 中设置 `EV_EOF`，并在 `fflags` 中返回套接字错误（如果有）。在套接字缓冲区中仍有数据待处理时也可能返回 EOF（表示连接已断开）。

**Vnode** 当文件指针不在文件末尾时返回。`data` 包含从当前位置到文件末尾的偏移量，可能为负。此行为与 [poll(2)](poll.2.md) 不同，后者对普通文件无条件触发读事件。可以通过在 `fflags` 中设置 `NOTE_FILE_POLL` 标志来无条件触发此事件。

**Fifo、管道** 当有数据可读时返回；`data` 包含可用字节数。当最后一个写者断开时，过滤器将在 `flags` 中设置 `EV_EOF`。当新的写者连接时，过滤器将清除该标志，此时过滤器将恢复等待数据可用后再返回。

**BPF 设备** 当 BPF 缓冲区满、BPF 超时已过期，或 BPF 启用了 "immediate mode" 且有数据可读时返回；`data` 包含可用字节数。

**Eventfd** 当计数器大于 0 时返回；`data` 包含计数器值，必须转换为 `uint64_t`。

**Kqueue** 当队列上有待处理事件时返回；`data` 包含可用事件数。

**`NOTE_ATTRIB`** 描述符引用的文件的属性已更改。

**`NOTE_CLOSE`** 引用受监视文件的文件描述符已关闭。被关闭的文件描述符没有写权限。

**`NOTE_CLOSE_WRITE`** 引用受监视文件的文件描述符已关闭。被关闭的文件描述符具有写权限。此 note 以及 `NOTE_CLOSE` 在文件被 [unmount(2)](unmount.2.md) 或 [revoke(2)](revoke.2.md) 强制关闭时不会激活。对于此类事件，会发送 `NOTE_REVOKE`。

**`NOTE_DELETE`** 对描述符引用的文件调用了 `unlink()` 系统调用。

**`NOTE_EXTEND`** 对于普通文件，描述符引用的文件被扩展。对于目录，报告由于重命名操作而添加或删除了目录项。当目录内的名称更改时不报告 `NOTE_EXTEND` 事件。

**`NOTE_LINK`** 文件的链接计数已更改。特别是，如果在描述符引用的目录内创建或删除了子目录，则报告 `NOTE_LINK` 事件。

**`NOTE_OPEN`** 描述符引用的文件被打开。

**`NOTE_READ`** 对描述符引用的文件发生了读取操作。

**`NOTE_RENAME`** 描述符引用的文件被重命名。

**`NOTE_REVOKE`** 对文件的访问通过 [revoke(2)](revoke.2.md) 被撤销，或底层文件系统被卸载。

**`NOTE_WRITE`** 对描述符引用的文件发生了写入操作。

**`NOTE_EXIT`** 进程已退出。退出状态将以与 [wait(2)](wait.2.md) 返回的状态相同的格式存储在 `data` 中。

**`NOTE_FORK`** 进程已调用 `fork()`。

**`NOTE_EXEC`** 进程通过 [execve(2)](execve.2.md) 或类似调用执行了新进程。

**`NOTE_TRACK`** 跨 `fork()` 调用跟踪进程。父进程使用与原始事件相同的 `fflags` 注册一个新的 kevent 来监视子进程。子进程将发出一个在 `fflags` 中设置 `NOTE_CHILD` 且在 `data` 中包含父 PID 的事件。如果父进程未能注册新的 kevent（通常由于资源限制），它将发出一个在 `fflags` 中设置 `NOTE_TRACKERR` 的事件，而子进程不会发出 `NOTE_CHILD` 事件。

**`NOTE_EXIT`** 进程已退出。退出状态将存储在 `data` 中。

**`NOTE_JAIL_SET`** Jail 已通过 [jail_set(2)](jail_set.2.md) 更改。

**`NOTE_JAIL_ATTACH`** 进程已通过 [jail_attach(2)](jail_attach.2.md) 或类似调用附加到 jail。进程 ID 将存储在 `data` 中。如果自上次调用 `kevent()` 以来有多个进程附加，`data` 将为零。

**`NOTE_JAIL_REMOVE`** Jail 已被移除。

**`NOTE_JAIL_CHILD`** 受监视 jail 的子 jail 已创建。其 jail ID 将存储在 `data` 中。如果自上次调用 `kevent()` 以来创建了多个 jail，`data` 将为零。

**`NOTE_SECONDS`** `data` 以秒为单位。

**`NOTE_MSECONDS`** `data` 以毫秒为单位。

**`NOTE_USECONDS`** `data` 以微秒为单位。

**`NOTE_NSECONDS`** `data` 以纳秒为单位。

**`NOTE_ABSTIME`** 指定的过期时间为绝对对时间。

**`NOTE_FFNOP`** 忽略输入的 `fflags`。

**`NOTE_FFAND`** 对 `fflags` 进行按位与。

**`NOTE_FFOR`** 对 `fflags` 进行按位或。

**`NOTE_FFCOPY`** 复制 `fflags`。

**`NOTE_FFCTRLMASK`** `fflags` 的控制掩码。

**`NOTE_FFLAGSMASK`** `fflags` 的用户定义标志掩码。

**`NOTE_TRIGGER`** 使事件被触发。

**`EVFILT_READ`** 以描述符作为标识符，每当有数据可读时返回。过滤器的行为根据描述符类型略有不同。

**`EVFILT_WRITE`** 以描述符作为标识符，每当可以向描述符写入时返回。对于套接字、管道和 fifo，`data` 将包含写缓冲区中剩余的空间量。当读者断开时，过滤器将设置 `EV_EOF`，对于 fifo 的情况，当新的读者连接时该标志将被清除。注意，vnode 不支持此过滤器。对于套接字，低水位标记和套接字错误处理与 `EVFILT_READ` 情况相同。对于 eventfd，`data` 将包含可添加到计数器而不阻塞的最大值。对于 BPF 设备，当描述符附加到接口时，过滤器始终指示可以写入，且 `data` 将包含底层接口的 MTU 大小。

**`EVFILT_EMPTY`** 以描述符作为标识符，每当写缓冲区中没有剩余数据时返回。

**`EVFILT_AIO`** 此过滤器的事件不直接通过 `kevent()` 注册，而是在异步 I/O 请求通过 `aio_read()` 等异步 I/O 系统调用调度时，通过异步 I/O 请求的 `aio_sigevent` 成员注册。过滤器在与 `aio_error()` 相同的条件下返回。有关此过滤器的更多详细信息，请参见 [sigevent(3)](../man3/sigevent.3.md) 和 [aio(4)](../man4/aio.4.md)。

**`EVFILT_VNODE`** 以文件描述符作为标识符，在 `fflags` 中指定要监视的事件，当描述符上发生一个或多个请求的事件时返回。要监视的事件为：返回时，`fflags` 包含触发过滤器的事件。

**`EVFILT_PROC`** 以要监视的进程 ID 作为标识符，在 `fflags` 中指定要监视的事件，当进程执行一个或多个请求的事件时返回。如果进程通常可以看到另一个进程，则可以向其附加事件。要监视的事件为：返回时，`fflags` 包含触发过滤器的事件。

**`EVFILT_PROCDESC`** 以 [pdfork(2)](pdfork.2.md) 创建的进程描述符作为标识符进行监视，在 `fflags` 中指定要监视的事件，当关联的进程执行一个或多个请求的事件时返回。要监视的事件为：返回时，`fflags` 包含触发过滤器的事件。

**`EVFILT_SIGNAL`** 以要监视的信号编号作为标识符，当给定信号被传递到进程时返回。这与 `signal()` 和 `sigaction()` 设施共存，并具有较低的优先级。过滤器将记录所有向进程传递信号的尝试，即使信号已被标记为 `SIG_IGN`，但 `SIGCHLD` 信号除外——如果被忽略，则不会被过滤器记录。事件通知在正常信号传递处理之前发生。`data` 返回自上次调用 `kevent()` 以来信号发生的次数。此过滤器在内部自动设置 `EV_CLEAR` 标志。

**`EVFILT_JAIL`** 以要监视的 jail ID 作为标识符，在 `fflags` 中指定要监视的事件，当 jail 执行一个或多个请求的事件时返回。如果进程通常可以看到 jail，则可以向其附加事件。标识符为零时将监视进程自身的 jail。要监视的事件为：返回时，`fflags` 包含触发过滤器的事件。如果自上次调用 `kevent()` 以来收到多个 `NOTE_JAIL_ATTACH` 或 `NOTE_JAIL_CHILD` 事件，它还将包含 `NOTE_JAIL_MULTI`。

**`EVFILT_JAILDESC`** 以 [jail_set(2)](jail_set.2.md) 或 [jail_get(2)](jail_get.2.md) 返回的 jail 描述符作为标识符，在 `fflags` 中指定要监视的事件，当 jail 执行一个或多个请求的事件时返回。要监视的事件及产生的 `fflags` 与上文 `EVFILT_JAIL` 中列出的相同。

**`EVFILT_TIMER`** 建立一个由 `ident` 标识的任意定时器。添加定时器时，`data` 指定触发定时器的时刻（用于 `NOTE_ABSTIME`）或超时周期。除非指定 `EV_ONESHOT` 或 `NOTE_ABSTIME`，否则定时器将是周期性的。返回时，`data` 包含自上次调用 `kevent()` 以来超时已过期的次数。对于非单调定时器，此过滤器在内部自动设置 `EV_CLEAR` 标志。过滤器在 `fflags` 参数中接受以下标志：如果未设置 `fflags`，则默认为毫秒。返回时，`fflags` 包含触发过滤器的事件。指定超时为 0 的周期性定时器将被静默调整为在 `fflags` 中请求的精度指定的时间单位后超时 1 次。如果指定的绝对时间已经过去，则将其视为指定了当前时间，事件将尽快触发。如果重新添加现有定时器，现有定时器将被有效取消（丢弃任何未交付的先前定时器过期记录），并使用 `data` 和 `fflags` 中包含的新参数重新启动。系统范围内定时器数量有限制，由 `kern.kq_calloutmax` sysctl 控制。

**`EVFILT_USER`** 建立一个由 `ident` 标识的用户事件，该事件不与任何内核机制关联，而是由用户级代码触发。`fflags` 的低 24 位可用于用户定义的标志，并可使用以下方式操作：用户事件通过以下方式触发以输出：返回时，`fflags` 在低 24 位中包含用户定义的标志。

## 取消行为

如果 `nevents` 非零，即函数可能阻塞，则该调用是一个取消点。否则，即如果 `nevents` 为零，则该调用不可取消。取消只能在对 kqueue 进行任何更改之前发生，或当调用被阻塞且未请求对队列进行更改时发生。

## 返回值

`kqueue()` 系统调用创建一个新的内核事件队列并返回一个文件描述符。如果创建内核事件队列时出错，返回值 -1 并设置 errno。

`kevent()` 系统调用返回放置在 `eventlist` 中的事件数，最多为 `nevents` 给定的值。如果在处理 `changelist` 的某个元素时发生错误，且 `eventlist` 中有足够的空间，则该事件将被放置在 `eventlist` 中，并在 `flags` 中设置 `EV_ERROR`，在 `data` 中设置系统错误。否则，返回 `-1`，并设置 `errno` 以指示错误条件。如果时间限制到期，`kevent()` 返回 0。

## 实例

```c
#include <sys/event.h>
#include <err.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main(int argc, char **argv)
{
    struct kevent event;    /* 我们要监视的事件 */
    struct kevent tevent;   /* 触发的事件 */
    int kq, fd, ret;

    if (argc != 2)
        err(EXIT_FAILURE, "Usage: %s path\n", argv[0]);
    fd = open(argv[1], O_RDONLY);
    if (fd == -1)
        err(EXIT_FAILURE, "Failed to open '%s'", argv[1]);

    /* 创建 kqueue。 */
    kq = kqueue();
    if (kq == -1)
        err(EXIT_FAILURE, "kqueue() failed");

    /* 初始化 kevent 结构体。 */
    EV_SET(&event, fd, EVFILT_VNODE, EV_ADD | EV_CLEAR, NOTE_WRITE,
        0, NULL);
    /* 将事件附加到 kqueue。 */
    ret = kevent(kq, &event, 1, NULL, 0, NULL);
    if (ret == -1)
        err(EXIT_FAILURE, "kevent register");

    for (;;) {
        /* 休眠直到有事件发生。 */
        ret = kevent(kq, NULL, 0, &tevent, 1, NULL);
        if (ret == -1) {
            err(EXIT_FAILURE, "kevent wait");
        } else if (ret > 0) {
            if (tevent.flags & EV_ERROR)
                errx(EXIT_FAILURE, "Event error: %s", strerror(event.data));
            else
                printf("Something was written in '%s'\n", argv[1]);
        }
    }

    /* kqueue 在 close() 时销毁 */
    (void)close(kq);
    (void)close(fd);
}
```

## 错误

`kqueue()` 系统调用在以下情况下会失败：

**[`ENOMEM`]** 内核未能为内核队列分配足够的内存。

**[`ENOMEM`]** 将超出当前用户的 `RLIMIT_KQUEUES` rlimit（参见 [getrlimit(2)](getrlimit.2.md)）。

**[`EMFILE`]** 每进程描述符表已满。

**[`ENFILE`]** 系统文件表已满。

`kevent()` 系统调用在以下情况下会失败：

**[`EACCES`]** 进程没有权限注册过滤器。

**[`EFAULT`]** 读取或写入 `kevent` 结构体时发生错误。

**[`EBADF`]** 指定的描述符无效。

**[`EINTR`]** 在超时过期之前以及在有任何事件放置到 kqueue 上待返回之前，传递了信号。

**[`EINTR`]** 向线程传递了取消请求，但尚未处理。

**[`EINVAL`]** 指定的时间限制或过滤器无效。

**[`EINVAL`]** 指定的事件或更改列表长度为负。

**[`ENOENT`]** 找不到要修改或删除的事件。

**[`ENOMEM`]** 没有可用内存来注册事件，或者在定时器的特殊情况下，已超出最大定时器数。此最大值可通过 `kern.kq_calloutmax` sysctl 配置。

**[`ESRCH`]** 指定要附加的进程不存在。

当 `kevent()` 调用因 `EINTR` 错误失败时，`changelist` 中的所有更改都已被应用。

## 参见

[aio_error(2)](aio_error.2.md), [aio_read(2)](aio_read.2.md), [aio_return(2)](aio_return.2.md), [poll(2)](poll.2.md), [read(2)](read.2.md), [select(2)](select.2.md), [sigaction(2)](sigaction.2.md), [write(2)](write.2.md), [pthread_setcancelstate(3)](../man3/pthread_setcancelstate.3.md), [signal(3)](../man3/signal.3.md)

> Jonathan Lemon, "Kqueue: A Generic and Scalable Event Notification Facility", *Proceedings of the FREENIX Track: 2001 USENIX Annual Technical Conference*, USENIX Association, June 25-30, 2001.

## 历史

`kqueue()` 和 `kevent()` 系统调用首次出现于 FreeBSD 4.1。`kqueuex()` 系统调用和 `kqueue1()` 函数首次出现于 FreeBSD 14.0。

## 作者

*kqueue* 子系统及本手册页由 Jonathan Lemon <jlemon@FreeBSD.org> 编写。

## 缺陷

在 FreeBSD 12.0 之前的版本中，

`#include <sys/event.h>`

未手动包含

`#include <sys/types.h>`

时无法解析。
