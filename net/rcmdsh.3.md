# rcmdsh(3)

`rcmdsh` — 返回到远程命令的流，无需超级用户权限

## 名称

`rcmdsh`

## 概要

`#include <unistd.h>`

```c
int
rcmdsh(char **ahost, int inport, const char *locuser, const char *remuser,
    const char *cmd, const char *rshprog);
```

## 描述

`rcmdsh` 函数供普通用户使用，通过基于保留端口号的认证方案，借助 rshd(8) 或 `rshprog` 的值（若非 `NULL`）在远程机器上执行命令。

`rcmdsh` 函数使用 [gethostbyname(3)](gethostbyname.3.md) 查找主机 `*ahost`，如果主机不存在则返回 -1。否则，`*ahost` 将被设置为主机的标准名称，并建立到位于知名 Internet 端口 `shell/tcp`（或 `rshprog` 所使用的端口）的服务器的连接。`inport` 参数被忽略；它的存在仅是为了提供与 [rcmd(3)](rcmd.3.md) 类似的接口。

如果连接成功，将向调用者返回一个 UNIX 域中类型为 `SOCK_STREAM` 的套接字，并将其作为 `stdin`、`stdout` 和 `stderr` 提供给远程命令。

## 返回值

`rcmdsh` 函数成功时返回有效的套接字描述符。否则返回 -1，并在标准错误输出上打印诊断信息。

## 参见

rsh(1), [socketpair(2)](../sys/socketpair.2.md), [rcmd(3)](rcmd.3.md), rshd(8)

## 历史

`rcmdsh` 函数首次出现于 OpenBSD 2.0，并引入 FreeBSD 4.6。

## 缺陷

如果 rsh(1) 遇到错误，仍会返回一个文件描述符而非 -1。
