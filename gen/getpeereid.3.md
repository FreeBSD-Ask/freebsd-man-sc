# getpeereid(3)

`getpeereid` — 获取 UNIX 域对端的有效凭证

## 名称

`getpeereid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
getpeereid(int s, uid_t *euid, gid_t *egid);
```

## 描述

`getpeereid` 函数返回连接到 UNIX 域 socket 的对端的有效用户 ID 和组 ID。参数 `s` 必须是已连接的 UNIX 域 socket（[unix(4)](../man4/unix.4.md)），类型为 `SOCK_STREAM`，且已调用过 [connect(2)](../sys/connect.2.md) 或 [listen(2)](../sys/listen.2.md)。有效用户 ID 放入 `euid`，有效组 ID 放入 `egid`。

返回给 [listen(2)](../sys/listen.2.md) 调用者的凭证是其对端在调用 [connect(2)](../sys/connect.2.md) 时的凭证；返回给 [connect(2)](../sys/connect.2.md) 调用者的凭证是其对端在调用 [listen(2)](../sys/listen.2.md) 时的凭证。此机制是可靠的；任何一方都无法影响返回给其对端的凭证，除非在不同的有效凭证下调用适当的系统调用（即 [connect(2)](../sys/connect.2.md) 或 [listen(2)](../sys/listen.2.md)）。

此例程的一个常见用途是 UNIX 域服务器验证其客户端的凭证。同样，客户端也可以验证服务器的凭证。

## 实现说明

在 FreeBSD 上，`getpeereid` 通过 `LOCAL_PEERCRED` [unix(4)](../man4/unix.4.md) socket 选项实现。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getpeereid` 函数在以下情况下会失败：

**[`EBADF`]** 参数 `s` 不是有效的描述符。

**[`ENOTSOCK`]** 参数 `s` 是文件，不是 socket。

**[`ENOTCONN`]** 参数 `s` 不引用已调用 [connect(2)](../sys/connect.2.md) 或 [listen(2)](../sys/listen.2.md) 的 socket。

**[`EINVAL`]** 参数 `s` 不引用 `SOCK_STREAM` 类型的 socket，或内核返回了无效数据。

## 参见

[connect(2)](../sys/connect.2.md), [getpeername(2)](../sys/getpeername.2.md), [getsockname(2)](../sys/getsockname.2.md), [getsockopt(2)](../sys/getsockopt.2.md), [listen(2)](../sys/listen.2.md), [unix(4)](../man4/unix.4.md)

## 历史

`getpeereid` 函数出现于 FreeBSD 4.6。
