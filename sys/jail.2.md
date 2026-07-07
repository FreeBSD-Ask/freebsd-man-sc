# jail(2)

`jail` — 创建和管理系统 Jail

## 名称

`jail`, `jail_get`, `jail_set`, `jail_remove`, `jail_attach`, `jail_remove_jd`, `jail_attach_jd`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/jail.h>`

```c
int
jail(struct jail *jail);

int
jail_attach(int jid);

int
jail_remove(int jid);

int
jail_attach_jd(int fd);

int
jail_remove_jd(int fd);
```

`#include <sys/uio.h>`

```c
int
jail_get(struct iovec *iov, u_int niov, int flags);

int
jail_set(struct iovec *iov, u_int niov, int flags);
```

## 描述

`jail()` 系统调用建立一个 Jail 并将当前进程锁定在其中。

参数是指向描述该 prison 的结构的指针：

```c
struct jail {
	uint32_t	version;
	char		*path;
	char		*hostname;
	char		*jailname;
	unsigned int	ip4s;
	unsigned int	ip6s;
	struct in_addr	*ip4;
	struct in6_addr	*ip6;
};
```

“`version`” 定义所使用的 API 版本。为当前版本定义了 `JAIL_API_VERSION`。

“`path`” 指针应设置为将成为该 prison 根目录的目录。

“`hostname`” 指针可设置为该 prison 的主机名。这可以从 prison 内部更改。

“`jailname`” 指针是可选的名称，可分配给该 Jail，例如用于管理目的。

“`ip4s`” 和 “`ip6s`” 给出将通过各自指针传递的 IPv4 和 IPv6 地址数量。

“`ip4`” 和 “`ip6`” 指针可设置为分配给该 prison 的 IPv4 和 IPv6 地址数组，如无则为 NULL。IPv4 地址必须为网络字节序。

这等同于 `jail_set()` 系统调用（参见下文），并由其取代，参数为 `path`、`host.hostname`、`name`、`ip4.addr` 和 `ip6.addr`，并带有 `JAIL_ATTACH` 标志。

`jail_set()` 系统调用创建新 Jail 或修改现有 Jail，并可选地将当前进程锁定在其中。Jail 参数以名值对数组的形式在 `iov` 数组中传递，包含 `niov` 个元素。参数名为以 null 结尾的字符串，值可以是字符串、整数或其他任意数据。某些参数为布尔型，没有值（其长度为零），仅通过名称带或不带 “no” 前缀来设置，例如 `persist` 或 `nopersist`。任何未设置的参数将给予默认值，通常基于当前环境。

Jail 具有一组核心参数，模块可以添加自己的 Jail 参数。当前可用参数集及其格式可通过 `security.jail.param` sysctl MIB 条目检索。值得注意的参数包括上面 `jail()` 描述中提到的那些，以及 `jid` 和 `name`（用于标识正在创建或修改的 Jail）。有关核心 Jail 参数的更多信息，请参见 [jail(8)](../man8/jail.8.md)。

`flags` 参数由以下一个或多个标志组成：

**`JAIL_CREATE`** 创建新 Jail。如果存在 `jid` 或 `name` 参数，它们不能引用现有 Jail。

**`JAIL_UPDATE`** 修改现有 Jail。必须存在 `jid` 或 `name` 参数之一，且必须引用现有 Jail。如果同时设置 `JAIL_CREATE` 和 `JAIL_UPDATE`，则在不存在时创建 Jail，在存在时修改 Jail。

**`JAIL_ATTACH`** 除创建或修改 Jail 外，将当前进程附加到其中，如同调用 `jail_attach()` 系统调用。

**`JAIL_DYING`** 这在 `jail_set()` 中弃用，无效果。

**`JAIL_USE_DESC`** 通过 `desc` 参数中的描述符标识 Jail。

**`JAIL_AT_DESC`** 在 `desc` 参数描述的 Jail 上下文中操作，而非当前 Jail。`JAIL_USE_DESC` 或 `JAIL_AT_DESC` 只能指定其一。

**`JAIL_GET_DESC`** 为 `desc` 参数中的 Jail 返回新的 Jail 描述符。

**`JAIL_OWN_DESC`** 在 `desc` 参数中返回 “拥有” 的 Jail 描述符。

`jail_get()` 系统调用检索 Jail 参数，使用与 `jail_set()` 中 `iov` 和 `niov` 参数相同的名值列表。要读取的 Jail 可通过在列表中包含 `jid` 或 `name` 参数来指定。如果包含但不打算作为搜索键，应清除它们（分别为零和空字符串）。

特殊参数 `lastjid` 可用于检索所有 Jail 的列表。它将获取 jid 大于且最接近所传递值的 Jail。通过传递 `lastjid` 为零可以找到第一个 Jail（通常但不总是 jid 1）。

`flags` 参数由以下一个或多个标志组成：

**`JAIL_DYING`** 允许获取正在被移除的 Jail。

**`JAIL_USE_DESC`**, `JAIL_AT_DESC`, `JAIL_GET_DESC`, `JAIL_OWN_DESC` 这些与在 `jail_set()` 中的含义相同。

`jail_attach()` 系统调用将当前进程附加到由 `jid` 标识的现有 Jail。它将进程的根目录和当前目录更改为该 Jail 的 `path` 目录。

`jail_remove()` 系统调用移除由 `jid` 标识的 Jail。它将杀死属于该 Jail 的所有进程，并移除该 Jail 的任何子 Jail。

`jail_attach_jd()` 和 `jail_remove_jd()` 系统调用的作用与 `jail_attach()` 和 `jail_remove()` 相同，只是它们对由 Jail 描述符 `fd` 标识的 Jail 进行操作。

### Jail 描述符

除 Jail ID 外，还可以使用 Jail 描述符引用 Jail，这是一种绑定到特定 Jail 的文件描述符。通过调用 `jail_set()` 或 `jail_get()` 并指定特殊参数 `desc` 以及 `JAIL_GET_DESC` 或 `JAIL_OWN_DESC` 标志来创建 Jail 描述符。两个标志的区别在于，使用 `JAIL_OWN_DESC` 创建的描述符（称为 “拥有” 描述符）在描述符关闭时会自动移除该 Jail。

Jail 描述符可通过 `desc` 参数传回 `jail_set()` 或 `jail_get()`，并设置 `JAIL_USE_DESC` 或 `JAIL_AT_DESC` 标志。使用 `JAIL_USE_DESC` 时，描述符标识要操作的 Jail，而非 `jid` 或 `name` 参数。使用 `JAIL_AT_DESC` 时，描述符用于代替当前 Jail，允许访问或创建作为描述符 Jail 子级的 Jail。

`jail_attach_jd()` 和 `jail_remove_jd()` 系统调用的作用与 `jail_attach()` 和 `jail_remove()` 相同，只是它们对所传递描述符引用的 Jail 进行操作。

## 返回值

如果成功，`jail()`、`jail_set()` 和 `jail_get()` 返回一个非负整数，称为 Jail 标识符（JID）。失败时返回 -1，并设置 `errno` 以指示错误。

`jail_attach()`、`jail_remove()`、`jail_attach_jd()`、`jail_remove_jd()` 成功时返回 0；失败时返回 -1，并设置 `errno` 以指示错误。

## 错误

`jail()` 系统调用将在以下情况下失败：

**[`EPERM`]** 此进程不被允许创建 Jail，原因在于它不是超级用户，或会超过 Jail 的 `children.max` 限制。

**[`EFAULT`]** `jail` 指向进程分配地址空间之外的地址。

**[`EINVAL`]** 参数的版本号不正确。

**[`EAGAIN`]** 找不到空闲的 JID。

`jail_set()` 系统调用将在以下情况下失败：

**[`EPERM`]** 此进程不被允许创建 Jail，原因在于它不是超级用户，或会超过 Jail 的 `children.max` 限制。

**[`EPERM`]** `desc` 参数中的 Jail 描述符由超级用户以外的用户创建，且设置了 `JAIL_USE_DESC` 标志。

**[`EPERM`]** 某个 Jail 参数被设置为比当前环境限制更宽松的值。

**[`EFAULT`]** `iov` 或其中包含的某个地址指向进程分配地址空间之外的地址。

**[`ENOENT`]** 由 `jid` 或 `name` 参数引用的 Jail 不存在，且未设置 `JAIL_CREATE` 标志。

**[`ENOENT`]** 由 `jid` 参数引用的 Jail 不被进程可访问，因为进程位于不同的 Jail 中。

**[`ENOENT`]** 由 `desc` 参数引用的 Jail 被移除。

**[`EEXIST`]** 由 `jid` 或 `name` 参数引用的 Jail 存在，且未设置 `JAIL_UPDATE` 标志。

**[`EINVAL`]** 所提供的参数大小错误。

**[`EINVAL`]** 所提供的参数超出范围。

**[`EINVAL`]** 所提供的字符串参数不以 null 结尾。

**[`EINVAL`]** 所提供的参数名不匹配任何已知参数。

**[`EINVAL`]** 未设置 `JAIL_CREATE` 或 `JAIL_UPDATE` 标志之一。

**[`ENAMETOOLONG`]** 所提供的字符串参数超过允许长度。

**[`EAGAIN`]** 没有剩余的 Jail ID。

**[`EMFILE`]** 无法为带有 `JAIL_GET_DESC` 或 `JAIL_OWN_DESC` 标志的 `desc` 参数创建 Jail 描述符，因为进程达到其打开文件描述符的限制。

**[`ENFILE`]** 无法为带有 `JAIL_GET_DESC` 或 `JAIL_OWN_DESC` 标志的 `desc` 参数创建 Jail 描述符，因为系统文件表已满。

`jail_get()` 系统调用将在以下情况下失败：

**[`ENOENT`]** 由 `jid` 或 `name` 参数引用的 Jail 不存在。

**[`ENOENT`]** 由 `jid` 引用的 Jail 不被进程可访问，因为进程位于不同的 Jail 中。

**[`ENOENT`]** `lastjid` 参数大于当前最高 Jail ID。

**[`ENOENT`]** 由 `desc` 参数引用的 Jail 被移除（即使设置了 `JAIL_CREATE` 标志）。

**[`EINVAL`]** 所提供的参数大小错误。

**[`EINVAL`]** 所提供的参数超出范围。

**[`EINVAL`]** 所提供的字符串参数不以 null 结尾。

**[`EINVAL`]** 所提供的参数名不匹配任何已知参数。

**[`EMFILE`]** 无法为带有 `JAIL_GET_DESC` 或 `JAIL_OWN_DESC` 标志的 `desc` 参数创建 Jail 描述符，因为进程达到其打开文件描述符的限制。

**[`ENFILE`]** 无法为带有 `JAIL_GET_DESC` 或 `JAIL_OWN_DESC` 标志的 `desc` 参数创建 Jail 描述符，因为系统文件表已满。

`jail_attach()` 和 `jail_remove()` 系统调用将在以下情况下失败：

**[`EPERM`]** 超级用户以外的用户尝试附加到或移除 Jail。

**[`EINVAL`]** 由 `jid` 指定的 Jail 不存在。

`jail_attach_jd()` 和 `jail_remove_jd()` 系统调用将在以下情况下失败：

**[`EINVAL`]** `fd` 参数不是有效的 Jail 描述符。

**[`EPERM`]** 该 Jail 描述符由超级用户以外的用户创建。

**[`EINVAL`]** 由 `jid` 指定的 Jail 被移除。

此外，`jail()`、`jail_set()`、`jail_attach()` 和 `jail_attach_jd()` 调用内部会调用 [chroot(2)](chroot.2.md)，因此可能因相同的原因失败。特别是，当加入 Jail 的进程有打开的目录时，它们返回 `EPERM` 错误。详情请参阅 [chroot(2)](chroot.2.md) 手册页。

## 参见

[chdir(2)](chdir.2.md), [chroot(2)](chroot.2.md), [jail(8)](../man8/jail.8.md)

## 历史

`jail()` 系统调用出现于 FreeBSD 4.0。`jail_attach()` 系统调用出现于 FreeBSD 5.1。`jail_set()`、`jail_get()` 和 `jail_remove()` 系统调用出现于 FreeBSD 8.0。

## 作者

Jail 功能由 Poul-Henning Kamp 为 R&D Associates 编写，并贡献给 FreeBSD。James Gritton 添加了可扩展的 Jail 参数和分层 Jail。
