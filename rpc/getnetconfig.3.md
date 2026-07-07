# getnetconfig(3)

`getnetconfig` — 获取网络配置数据库条目

## 名称

`getnetconfig`, `setnetconfig`, `endnetconfig`, `getnetconfigent`, `freenetconfigent`, `nc_perror`, `nc_sperror`

## 库

Lb libc

## 概要

`#include <netconfig.h>`

```c
struct netconfig *
getnetconfig(void *handlep);

void *
setnetconfig(void);

int
endnetconfig(void *handlep);

struct netconfig *
getnetconfigent(const char *netid);

void
freenetconfigent(struct netconfig *netconfigp);

void
nc_perror(const char *msg);

char *
nc_sperror(void);
```

## 描述

本页所述的库例程使应用程序能够访问系统网络配置数据库 **/etc/netconfig**。`getnetconfig` 函数返回 netconfig 数据库中当前条目的指针，格式为 `struct netconfig`。连续调用将返回 netconfig 数据库中连续的 netconfig 条目。`getnetconfig` 函数可用于搜索整个 netconfig 文件。`getnetconfig` 函数在文件末尾返回 `NULL`。`handlep` 参数是通过 `setnetconfig` 获取的句柄。

调用 `setnetconfig` 可“绑定”或“回绕” netconfig 数据库。在首次调用 `getnetconfig` 之前必须调用 `setnetconfig`，也可在任何其他时间调用。在调用 `getnetconfigent` 之前无需调用 `setnetconfig`。`setnetconfig` 函数返回一个唯一句柄供 `getnetconfig` 使用。

处理完成后应调用 `endnetconfig` 函数以释放资源供重用。`handlep` 参数是通过 `setnetconfig` 获取的句柄。但程序员应注意，最后一次调用 `endnetconfig` 会释放 `getnetconfig` 为 `struct netconfig` 数据结构分配的所有内存。`endnetconfig` 函数不能在 `setnetconfig` 之前调用。

`getnetconfigent` 函数返回与 `netid` 对应的 netconfig 结构的指针。如果 `netid` 无效（即未命名 netconfig 数据库中的任何条目），则返回 `NULL`。

`freenetconfigent` 函数释放由 `netconfigp` 所指向的 netconfig 结构（先前由 `getnetconfigent` 返回）。

`nc_perror` 函数向标准错误输出打印一条消息，指示上述任何例程失败的原因。该消息前会加上字符串 `msg` 和一个冒号。消息末尾会附加一个换行符。

`nc_sperror` 函数类似于 `nc_perror`，但它不将消息发送到标准错误，而是返回指向包含错误消息的字符串的指针。

`nc_perror` 和 `nc_sperror` 函数也可与 [getnetpath(3)](getnetpath.3.md) 中定义的 `NETPATH` 访问例程配合使用。

## 返回值

`setnetconfig` 函数返回一个唯一句柄供 `getnetconfig` 使用。发生错误时，`setnetconfig` 返回 `NULL`，可使用 `nc_perror` 或 `nc_sperror` 打印失败原因。

`getnetconfig` 函数返回 netconfig 数据库中当前条目的指针，格式为 `struct netconfig`。`getnetconfig` 函数在文件末尾或失败时返回 `NULL`。

`endnetconfig` 函数成功时返回 0，失败时返回 -1（例如，如果之前未调用 `setnetconfig`）。

成功时，`getnetconfigent` 返回与 `netid` 对应的 `struct netconfig` 结构的指针；否则返回 `NULL`。

`nc_sperror` 函数返回指向包含错误消息字符串的缓冲区的指针。该缓冲区在每次调用时被覆盖。在多线程应用程序中，此缓冲区实现为线程特定数据。

## 文件

**/etc/netconfig** 系统网络配置数据库

## 参见

[getnetpath(3)](getnetpath.3.md), netconfig(5)
