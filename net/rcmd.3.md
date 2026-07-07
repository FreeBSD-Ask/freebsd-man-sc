# rcmd(3)

`rcmd` — 返回到远程命令的流的相关例程

## 名称

`rcmd`, `rresvport`, `iruserok`, `ruserok`, `rcmd_af`, `rresvport_af`, `iruserok_sa`

## 库

libc

## 概要

`#include <unistd.h>`

```c
int
rcmd(char **ahost, int inport, const char *locuser, const char *remuser,
    const char *cmd, int *fd2p);

int
rresvport(int *port);

int
iruserok(u_long raddr, int superuser, const char *ruser,
    const char *luser);

int
ruserok(const char *rhost, int superuser, const char *ruser,
    const char *luser);

int
rcmd_af(char **ahost, int inport, const char *locuser,
    const char *remuser, const char *cmd, int *fd2p, int af);

int
rresvport_af(int *port, int af);

int
iruserok_sa(const void *addr, int addrlen, int superuser,
    const char *ruser, const char *luser);
```

## 描述

`rcmd` 函数供超级用户使用，通过基于保留端口号的认证方案在远程机器上执行命令。`rresvport` 函数返回一个套接字描述符，该套接字具有特权端口空间中的地址。`ruserok` 函数供服务器用来认证通过 `rcmd` 请求服务的客户端。这三个函数都位于同一个文件中，并被 rshd(8) 服务器（以及其他程序）使用。

`rcmd` 函数使用 [gethostbyname(3)](gethostbyname.3.md) 查找主机 `*ahost`，如果主机不存在则返回 -1。否则，`*ahost` 将被设置为主机的标准名称，并建立到位于知名 Internet 端口 `inport` 的服务器的连接。

如果连接成功，将向调用者返回一个 Internet 域中类型为 `SOCK_STREAM` 的套接字，并将其作为 `stdin` 和 `stdout` 提供给远程命令。如果 `fd2p` 非零，则将建立一个到控制进程的辅助通道，并将该通道的描述符置于 `*fd2p` 中。控制进程将通过此通道返回命令的诊断输出（单元 2），并接受此通道上的字节作为 UNIX 信号编号，转发给命令的进程组。如果 `fd2p` 为 0，则 `stderr`（远程命令的单元 2）将与 `stdout` 相同，并且不提供向远程进程发送任意信号的功能，但你可能可以通过使用带外数据来引起其注意。

该协议在 rshd(8) 中有详细描述。

`rresvport` 函数用于获取一个套接字，该套接字绑定了一个具有特权 Internet 端口的地址。此套接字适合 `rcmd` 和其他几个函数使用。特权 Internet 端口是 0 到 1023 范围内的端口。只有超级用户才允许将此类地址绑定到套接字。

`iruserok` 和 `ruserok` 函数接收远程主机的 IP 地址或名称（由 [gethostbyname(3)](gethostbyname.3.md) 例程返回）、两个用户名以及一个指示本地用户名是否为超级用户的标志。然后，如果用户*不是*超级用户，它会检查 **/etc/hosts.equiv** 文件。如果未进行该查找，或查找不成功，则检查本地用户主目录中的 `.rhosts` 文件，以确定是否允许该服务请求。

如果此文件不存在、不是常规文件、由用户或超级用户以外的人拥有，或可由所有者以外的人写入，则检查自动失败。如果机器名称列在 `hosts.equiv` 文件中，或主机和远程用户名在 `.rhosts` 文件中找到，则返回零；否则 `iruserok` 和 `ruserok` 返回 -1。如果本地域（通过 [gethostname(3)](../gen/gethostname.3.md) 获取）与远程域相同，则只需指定机器名称。

出于安全原因，强烈推荐使用 `iruserok` 函数。它最多只需要信任本地 DNS，而 `ruserok` 函数需要信任整个 DNS，而 DNS 可能被欺骗。

带有 `_af` 或 `_sa` 后缀的函数，即 `rcmd_af`、`rresvport_af` 和 `iruserok_sa`，与不带后缀的相应函数工作方式相同，只是它们能够同时处理 IPv6 和 IPv4 端口。

`_af` 后缀表示该函数有一个额外的 `af` 参数，用于指定地址族（见下文）。`af` 参数扩展是为没有二进制地址参数的函数实现的。相反，`af` 参数指定所需的地址族。

`_sa` 后缀表示该函数具有通用的套接字地址和长度参数。由于套接字地址是协议无关的数据结构，因此可以按需传递 IPv4 和 IPv6 套接字地址。`sa` 参数扩展是为传递协议相关二进制地址参数的函数实现的。需要将该参数替换为更通用的地址结构，以通用的方式支持多种地址族。

既不带 `_af` 后缀也不带 `_sa` 后缀的函数仅适用于 IPv4，但 `ruserok` 可以处理 IPv6 和 IPv4。要切换地址族，`af` 参数必须填充为 `AF_INET` 或 `AF_INET6`。对于 `rcmd_af`，还允许使用 `PF_UNSPEC`。

## 环境变量

**`RSH`** 使用 `rcmd` 函数时，此变量用作要运行的程序，以替代 rsh(1)。

## 诊断

`rcmd` 函数成功时返回有效的套接字描述符。出错时返回 -1，并在标准错误输出上打印诊断信息。

`rresvport` 函数成功时返回有效的、已绑定的套接字描述符。出错时返回 -1，并根据失败原因设置全局值 `errno`。错误代码 `EAGAIN` 被重载为“所有网络端口都在使用中”的含义。

## 参见

rlogin(1), rsh(1), [intro(2)](../sys/intro.2.md), rlogind(8), rshd(8)

> W. Stevens, M. Thomas, "Advanced Socket API for IPv6", RFC2292.

> W. Stevens, M. Thomas, E. Nordmark, "Advanced Socket API for IPv6", RFC3542.

## 历史

这些函数中的大部分出现于 4.2BSD。`rresvport_af` 函数出现于 RFC2292，由 WIDE 项目为 Hydrangea IPv6 协议栈工具包实现。`rcmd_af` 函数出现于 draft-ietf-ipngwg-rfc2292bis-01.txt，并在 WIDE/KAME IPv6 协议栈工具包中实现。`iruserok_sa` 函数出现于 IETF ipngwg 邮件列表的讨论中，并在 FreeBSD 4.0 中实现。
