# getnetpath(3)

`getnetpath` — 获取与 `NETPATH` 组件对应的 **/etc/netconfig** 条目

## 名称

`getnetpath`, `setnetpath`, `endnetpath`

## 库

Lb libc

## 概要

`#include <netconfig.h>`

```c
struct netconfig *
getnetpath(void *handlep);

void *
setnetpath(void);

int
endnetpath(void *handlep);
```

## 描述

本页所述的例程使应用程序能够访问系统网络配置数据库 **/etc/netconfig**，该数据库经 `NETPATH` 环境变量“过滤”（参见 [environ(7)](../man7/environ.7.md)）。其他直接访问网络配置数据库的例程参见 [getnetconfig(3)](getnetconfig.3.md)。`NETPATH` 变量是由冒号分隔的网络标识符列表。

`getnetpath` 函数返回指向与第一个有效 `NETPATH` 组件对应的 netconfig 数据库条目的指针。netconfig 条目的格式为 `struct netconfig`。在随后的每次调用中，`getnetpath` 返回指向与下一个有效 `NETPATH` 组件对应的 netconfig 条目的指针。因此，`getnetpath` 函数可用于在 netconfig 数据库中搜索 `NETPATH` 变量中包含的所有网络。当 `NETPATH` 耗尽时，`getnetpath` 返回 `NULL`。

调用 `setnetpath` 可“绑定”或“回绕” `NETPATH`。在首次调用 `getnetpath` 之前必须调用 `setnetpath`，也可在任何其他时间调用。它返回一个由 `getnetpath` 使用的句柄。

`getnetpath` 函数会静默忽略无效的 `NETPATH` 组件。如果 netconfig 数据库中没有对应的条目，则该 `NETPATH` 组件无效。

如果 `NETPATH` 变量未设置，`getnetpath` 的行为如同 `NETPATH` 被设置为 netconfig 数据库中 “default” 或 “visible” 网络的序列，顺序与其列出的顺序相同。

处理完成后，可以调用 `endnetpath` 函数“解绑” `NETPATH`，释放资源以供重用。但程序员应注意，`endnetpath` 会释放 `getnetpath` 为 `struct netconfig` 数据结构分配的所有内存。

## 返回值

`setnetpath` 函数返回一个由 `getnetpath` 使用的句柄。发生错误时，`setnetpath` 返回 `NULL`。

`endnetpath` 函数成功时返回 0，失败时返回 -1（例如，如果之前未调用 `setnetpath`）。可以使用 `nc_perror` 或 `nc_sperror` 函数打印失败原因。参见 [getnetconfig(3)](getnetconfig.3.md)。

首次调用时，`getnetpath` 返回指向与第一个有效 `NETPATH` 组件对应的 netconfig 数据库条目的指针。当 `NETPATH` 耗尽时，`getnetpath` 返回 `NULL`。

## 参见

[getnetconfig(3)](getnetconfig.3.md), netconfig(5), [environ(7)](../man7/environ.7.md)
