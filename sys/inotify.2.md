# inotify(2)

`inotify_init` — 监视文件系统事件

## 名称

`inotify_init`, `inotify_init1`, `inotify_add_watch`, `inotify_add_watch_at`, `inotify_rm_watch`

## 库

Lb libc

## 概要

`#include <sys/inotify.h>`

```c
int
inotify_init(void);

int
inotify_init1(int flags);

int
inotify_add_watch(int fd, const char *pathname, uint32_t mask);

int
inotify_add_watch_at(int fd, int dfd, const char *pathname, uint32_t mask);

int
inotify_rm_watch(int fd, uint32_t wd);
```

```c
struct inotify_event {
        int wd;                 /* 监视描述符 */
        uint32_t mask;          /* 事件和标志 */
        uint32_t cookie;        /* 链接重命名事件的唯一 ID */
        uint32_t len;           /* name 字段大小，包括 nul 字节 */
        char name[0];           /* 文件名（以 nul 结尾） */
};
```

## 描述

inotify 系统调用提供了监视文件系统事件的接口。它们旨在与 Linux inotify 接口兼容。提供的功能类似于 [kevent(2)](kevent.2.md) 系统调用的 `EVFILT_VNODE` 过滤器，但进一步允许监视目录而无需打开该目录中的每个对象。这避免了竞态条件，并减少了监视大型文件层次结构所需的文件描述符数量。

inotify 允许监视一个或多个文件系统对象（通常是文件或目录）的事件，如文件打开或关闭。被监视的对象与由 `inotify_init()` 或 `inotify_init1()` 返回的文件描述符关联。当事件发生时，描述该事件的记录可从 inotify 文件描述符中读取。因此，每个 inotify 描述符都引用一个等待读取的事件队列。inotify 描述符在 [fork(2)](fork.2.md) 调用中继承，并可通过 [unix(4)](../man4/unix.4.md) 套接字传递给其他进程。

`inotify_init1()` 系统调用接受两个标志。`IN_NONBLOCK` 标志使 inotify 描述符以非阻塞模式打开，使得如果没有记录可消费，[read(2)](read.2.md) 调用不会阻塞，而是返回 `EWOULDBLOCK`。`IN_CLOEXEC` 标志使 inotify 描述符在调用 [execve(2)](execve.2.md) 时自动关闭。

要监视文件或目录，必须使用 `inotify_add_watch()` 或 `inotify_add_watch_at()` 系统调用。它们接受一个路径和要监视的事件掩码，返回一个“监视描述符”，一个非负整数，在 inotify 描述符中唯一标识被监视的对象。

`inotify_rm_watch()` 系统调用从 inotify 描述符中移除一个监视。

监视目录时，目录中的对象以及目录本身都会被监视事件。描述 inotify 事件的记录由“struct inotify_event”后跟被监视目录中对象的名称组成。如果被监视对象本身生成事件，则不出现名称。文件名后可能有额外的 nul 字节，以便为后续记录提供对齐。

定义以下事件：

**`IN_ACCESS`** 文件内容被访问，如通过 [read(2)](read.2.md)、[copy_file_range(2)](copy_file_range.2.md)、[sendfile(2)](sendfile.2.md) 或 [getdirentries(2)](getdirentries.2.md)。

**`IN_ATTRIB`** 文件元数据被更改，如通过 [chmod(2)](chmod.2.md) 或 [unlink(2)](unlink.2.md)。

**`IN_CLOSE_WRITE`** 先前为写入而打开的文件被关闭。

**`IN_CLOSE_NOWRITE`** 先前以只读方式打开的文件被关闭。

**`IN_CREATE`** 被监视目录中的文件被创建，如通过 [open(2)](open.2.md)、[mkdir(2)](mkdir.2.md)、[symlink(2)](symlink.2.md)、[mknod(2)](mknod.2.md) 或 [bind(2)](bind.2.md)。

**`IN_DELETE`** 被监视目录中的文件或目录被移除。

**`IN_DELETE_SELF`** 被监视的文件或目录本身被删除。此事件仅在文件的链接计数降为零时生成。

**`IN_MODIFY`** 文件内容被修改，如通过 [write(2)](write.2.md) 或 [copy_file_range(2)](copy_file_range.2.md)。

**`IN_MOVE_SELF`** 被监视的文件或目录本身被重命名。

**`IN_MOVED_FROM`** 文件或目录被移出被监视目录。

**`IN_MOVED_TO`** 文件或目录被移入被监视目录。因此 [rename(2)](rename.2.md) 调用可能生成两个事件，一个对应旧名称，一个对应新名称。它们通过 inotify 记录中的 `cookie` 字段链接，可以进行比较以将两条记录关联到同一事件。

**`IN_OPEN`** 文件被打开。

inotify 事件记录中还可设置一些附加标志：

**`IN_IGNORED`** 当监视从文件中移除时（例如因为使用 `IN_ONESHOT` 标志创建、文件被删除或通过 inotify_rm_watch(2) 显式移除），会生成具有此掩码的事件以指示该监视将不再生成任何事件。生成此事件后，监视会自动移除，特别是不应使用 inotify_rm_watch(2) 手动移除。

**`IN_ISDIR`** 当事件的主题是目录时，此标志在 `mask` 中设置。

**`IN_Q_OVERFLOW`** 一个或多个事件被丢弃，例如因为内核内存分配失败或事件队列大小达到限制。

**`IN_UNMOUNT`** 包含被监视对象的文件系统被卸载。

在传给 `inotify_add_watch()` 和 `inotify_add_watch_at()` 的 `mask` 中还可以指定若干标志：

**`IN_DONT_FOLLOW`** 如果 `pathname` 是符号链接，不跟随它。

**`IN_EXCL_UNLINK`** 目前无效果，参见缺陷部分。

**`IN_MASK_ADD`** 当向一个对象添加监视，且该对象已经被同一个 inotify 描述符监视时，默认情况下会覆盖现有监视的掩码。当指定了 `IN_MASK_ADD` 时，现有监视的掩码会与新掩码进行逻辑或运算。

**`IN_MASK_CREATE`** 当使用 `inotify_add_watch()` 向一个对象添加监视时指定了 `IN_MASK_CREATE`，且该对象已经被同一个 inotify 描述符监视，则返回错误而不是更新现有监视。

**`IN_ONESHOT`** 监视对象直到发生单个事件，之后监视会自动移除。作为移除的一部分，会生成一个 `IN_IGNORED` 事件。

**`IN_ONLYDIR`** 创建监视时，如果路径不指向目录，则以 `ENOTDIR` 失败。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`vfs.inotify.max_events`** 可为单个 inotify 描述符排队的 inotify 记录最大数量。超过此限制的记录将被丢弃，队列中将存在一个掩码等于 `IN_Q_OVERFLOW` 的单个事件。

**`vfs.inotify.max_user_instances`** 单个用户可创建的 inotify 描述符最大数量。

**`vfs.inotify.max_user_watches`** 每个用户的 inotify 监视最大数量。

## 实例

参见 **/usr/share/examples/inotify/inotify.c** 中的示例程序。

## 错误

`inotify_init()` 和 `inotify_init1()` 函数在以下情况下会失败：

**[`ENFILE`]** 已达到系统打开文件总数的限制。

**[`EMFILE`]** 已达到每进程打开文件数的限制。

**[`EMFILE`]** 已达到 inotify 描述符数量的系统限制。

**[`EINVAL`]** 向 `inotify_init1()` 传递了无法识别的标志。

`inotify_add_watch()` 和 `inotify_add_watch_at()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`EINVAL`]** `fd` 参数不是 inotify 描述符。

**[`EINVAL`]** `mask` 参数未指定事件，或同时设置了 `IN_MASK_CREATE` 和 `IN_MASK_ADD` 标志，或传递了无法识别的标志。

**[`ENOTDIR`]** `pathname` 参数引用的不是目录的文件，且指定了 `IN_ONLYDIR` 标志。

**[`ENOSPC`]** 已达到每个用户 inotify 监视总数的限制。

**[`ECAPMODE`]** 进程处于能力模式且调用了 `inotify_add_watch()`，或调用 `inotify_add_watch_at()` 时以 `AT_FDCWD` 作为目录文件描述符 `dfd`。

**[`ENOTCAPABLE`]** 进程处于能力模式且 `pathname` 包含“..”分量，指向 `dfd` 指定的目录层次结构之外的目录。

`inotify_rm_watch()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`EINVAL`]** `fd` 参数不是 inotify 描述符。

**[`EINVAL`]** `wd` 参数不是有效的监视描述符。

## 参见

[kevent(2)](kevent.2.md), [capsicum(4)](../man4/capsicum.4.md)

## 标准

`inotify_rm_watch` 接口源自 Linux，是非标准的。此实现旨在与 Linux 的实现兼容，并基于 `https://man7.org/linux/man-pages/man7/inotify.7.html` 上可用的文档。

## 历史

inotify 系统调用首次出现于 FreeBSD 15.0。

## 缺陷

如果被监视目录中的文件有多个硬链接，通过该文件的任何硬链接的访问都会生成事件，即使被访问的链接属于未被监视的目录。Linux 实现并非如此，只有通过被监视目录中的硬链接的访问才会生成事件。

如果被监视目录包含某个文件的多个硬链接，其中一个硬链接上的事件会为目录中的每个链接生成一条 inotify 记录。

当文件被取消链接时，即使该文件继续被访问，也不会再为其生成事件。默认情况下，Linux 实现在这种情况下会继续生成事件。因此，FreeBSD 实现的行为就好像始终设置了 `IN_EXCL_UNLINK` 一样。
