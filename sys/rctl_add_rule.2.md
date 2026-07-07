# rctl_add_rule(2)

`rctl_add_rule` — 操作和查询资源限制数据库

## 名称

`rctl_add_rule`, `rctl_get_limits`, `rctl_get_racct`, `rctl_get_rules`, `rctl_remove_rule`

## 库

Lb libc

## 概要

`#include <sys/rctl.h>`

```c
int
rctl_add_rule(const char *inbufp, size_t inbuflen,
    char *outbufp, size_t outbuflen);

int
rctl_get_limits(const char *inbufp, size_t inbuflen,
    char *outbufp, size_t outbuflen);

int
rctl_get_racct(const char *inbufp, size_t inbuflen,
    char *outbufp, size_t outbuflen);

int
rctl_get_rules(const char *inbufp, size_t inbuflen,
    char *outbufp, size_t outbuflen);

int
rctl_remove_rule(const char *inbufp, size_t inbuflen,
    char *outbufp, size_t outbuflen);
```

## 描述

这些系统调用用于操作和查询资源限制数据库。对于所有函数，`inbuflen` 指的是 `inbufp` 指向的缓冲区的长度，`outbuflen` 指的是 `outbufp` 指向的缓冲区的长度。

`rctl_add_rule()` 函数将 `inbufp` 指向的规则添加到资源限制数据库中。`outbufp` 和 `outbuflen` 参数未使用。规则格式如 rctl(8) 中所述，例外情况见“规则和过滤器”章节。

`rctl_get_limits()` 函数在 `outbufp` 中返回一个逗号分隔的规则列表，这些规则适用于与 `inbufp` 中指定的过滤器匹配的进程。这包括以该进程本身为主体的规则，以及以不同主体（如 user 或 loginclass）但适用于该进程的规则。

`rctl_get_racct()` 函数返回给定主体的资源使用信息。主体通过在 `inbufp` 中传递过滤器来指定。过滤器语法如 rctl(8) 中所述，例外情况见“规则和过滤器”章节。`outbufp` 中返回一个逗号分隔的资源列表以及指定主体使用的每种资源的数量。资源和数量格式为"resource=amount"。

`rctl_get_rules()` 函数在 `outbufp` 中返回资源限制数据库中与 `inbufp` 传递的过滤器匹配的规则列表（逗号分隔）。过滤器语法如 rctl(8) 中所述，例外情况见“规则和过滤器”章节。可以传递 `::` 过滤器以返回所有规则。

`rctl_remove_rule()` 函数从资源限制数据库中删除所有与 `inbufp` 传递的过滤器匹配的规则。过滤器语法如 rctl(8) 中所述，例外情况见“规则和过滤器”章节。`outbufp` 和 `outbuflen` 未使用。

## 规则和过滤器

本节解释 rctl(8) 中描述的规则和过滤器格式与传递给系统调用本身的格式有何不同。rctl 工具提供了系统调用所不具备的一些便利。使用系统调用时：

- 主体必须完整指定。例如，将 `user` 缩写为 `u` 是不可接受的。
- 用户和组 ID 必须是数字。例如，`root` 必须表示为 `0`。
- 资源数量不允许使用单位。例如，1024 字节的数量必须表示为 `1024` 而非 `1k`。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

rctl 系统调用在以下情况下可能失败：

**[`ENOSYS`]** 内核中不存在 RACCT/RCTL 支持，或 `kern.racct.enable` sysctl 为 0。

**[`EINVAL`]** `inbufp` 传递的规则或过滤器无效。

**[`EPERM`]** 用户没有执行所请求操作的足够权限。

**[`E2BIG`]** `inbufp` 或 `outbufp` 过大。

**[`ESRCH`]** 没有进程与提供的规则或过滤器匹配。

**[`ENAMETOOLONG`]** 指定的 loginclass 或 jail 名称过长。

**[`ERANGE`]** 规则数量超出允许范围或 `outbufp` 过小。

**[`EOPNOTSUPP`]** 请求的操作不支持给定的规则或过滤器。

**[`EFAULT`]** `inbufp` 或 `outbufp` 引用了无效地址。

## 参见

[rctl(8)](../man8/rctl.8.md)

## 历史

rctl 系列系统调用出现于 FreeBSD 9.0。

## 作者

rctl 系统调用由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD Foundation 赞助下开发。本手册页由 Eric Badger <badger@FreeBSD.org> 编写。