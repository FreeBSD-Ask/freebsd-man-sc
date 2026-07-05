# sockstat.1

`sockstat` — 列出打开的套接字

## 名称

`sockstat`

## 概要

`sockstat [--libxo] [-46AbCcfIiLlnqSsUuvw] [-F user] [-j jail] [-p ports] [-P protocols]`

## 描述

`sockstat` 命令列出打开的 Internet 或 UNIX 域套接字。

可用选项如下：

**`--libxo`** 通过 libxo(3) 以多种人类和机器可读格式生成输出。有关命令行参数的详情，参见 xo_options(7)。

**`-4`** 显示 `AF_INET`（IPv4）套接字。

**`-6`** 显示 `AF_INET6`（IPv6）套接字。

**`-A`** 显示与套接字关联的协议控制块（PCB）地址，用于调试。

**`-b`** 显示套接字的 BBLog 状态。目前仅对 TCP 实现。

**`-C`** 显示拥塞控制模块（如适用）。目前仅对 TCP 实现。

**`-c`** 显示已连接的套接字。

**`-F`** `user` 仅显示指定 `user`（用户名或 UID）的套接字。

**`-f`** 显示每个套接字的 FIB 编号。

**`-I`** 显示当前套接字所拼接到的套接字的本地地址（如有）。详情参见 setsockopt(2) 的 `SO_SPLICE` 选项。

**`-i`** 显示 `inp_gencnt`。

**`-j`** `jail` 仅显示属于指定 jail ID 或名称的套接字。

**`-L`** 仅当本地和外部地址不在回环网络前缀 **127.0.0.0/8** 中，或不包含 IPv6 回环地址 **::1** 时，才显示 Internet 套接字。

**`-l`** 显示监听套接字。

**`-n`** 不将数字 UID 解析为用户名。

**`-p`** `ports` 仅当本地或外部端口号在指定列表中时显示 Internet 套接字。`ports` 参数是以逗号分隔的端口号和范围列表，范围以首尾端口号用短划线分隔表示。

**`-P`** `protocols` 仅显示指定 `protocols` 的套接字。`protocols` 参数是以逗号分隔的协议名称列表。可识别的协议有“tcp”、“sctp”、“udp”、“udplite”、“unix/stream”、“unix/dgram”、“unix/seqpack”和“divert”。

**`-q`** 安静模式，不打印标题行。

**`-S`** 显示协议栈（如适用）。目前仅对 TCP 实现。

**`-s`** 显示协议状态（如适用）。目前仅对 SCTP 和 TCP 实现。

**`-U`** 显示远程 UDP 封装端口号（如适用）。目前仅对 SCTP 和 TCP 实现。

**`-u`** 显示 `AF_LOCAL`（UNIX）套接字。

**`-v`** 详细模式。

**`-w`** 自动调整列宽。

如果未指定 `-4`、`-6` 或 `-u`，`sockstat` 将列出所有三个域中的套接字。

如果未指定 `-c` 或 `-l`，`sockstat` 将同时列出监听和已连接的套接字。

每个套接字列出的信息为：

**`USER`** 拥有该套接字的用户。

**`COMMAND`** 持有该套接字的命令。

**`PID`** 持有该套接字的命令的进程 ID。

**`FD`** 该套接字的文件描述符编号。

**`PROTO`** 对于 Internet 套接字，为与套接字关联的传输协议；对于 UNIX 套接字，为套接字类型（stream、datagram 或 seqpacket）。

**`LOCAL ADDRESS`** 对于 Internet 套接字，为套接字本地端绑定的地址（参见 getsockname(2)）。对于已绑定的 UNIX 套接字，打印套接字文件名。对于未绑定的 UNIX 套接字，该字段为空。

**`FOREIGN ADDRESS`** 对于 Internet 套接字，为套接字外部端绑定的地址（参见 getpeername(2)）。对于已绑定的 UNIX 套接字，打印左箭头后跟对端列表。对于通过 connect(2) 系统调用的 UNIX 套接字，打印右箭头后跟对端。对端以方括号形式 [PID FD] 打印。

**`ID`** 若指定 `-i`，则为 inp_gencnt（仅适用于 TCP 或 UDP）。

**`ENCAPS`** 若指定 `-U`，则为远程 UDP 封装端口号（仅适用于 SCTP 或 TCP）。

**`PATH STATE`** 若指定 `-s`，则为路径状态（仅适用于 SCTP）。使用传统文本输出时，仅当至少有一个路径状态可显示时才显示此列。

**`CONN STATE`** 若指定 `-s`，则为连接状态（仅适用于 SCTP 或 TCP）。

**`BBLOG STATE`** 若指定 `-b`，则为 BBLog 状态（仅适用于 TCP）。

**`STACK`** 若指定 `-S`，则为协议栈（仅适用于 TCP）。

**`CC`** 若指定 `-C`，则为拥塞控制（仅适用于 TCP）。

如果一个套接字与多个文件描述符关联，它会显示多次。如果一个套接字未与任何文件描述符关联，前四列无意义。

## 实例

显示使用 TCP 协议在端口 22 上监听的 IPv4 套接字的信息：

```sh
$ sockstat -4 -l -P tcp -p 22
```

显示使用 TCP 或 UDP 的套接字信息，前提是本地和外部地址均不在回环网络中：

```sh
$ sockstat -L -P tcp,udp
```

显示正在监听和已连接（默认）的 TCP IPv6 套接字：

```sh
$ sockstat -6 -P tcp
```

显示所有正在监听的 [unix(4)](../man4/unix.4.md) 数据报套接字：

```sh
$ sockstat -P unix/dgram -l
```

以 JSON 格式整齐对齐地显示所有套接字：

```sh
$ sockstat --libxo json,pretty
```

## 参见

fstat(1), [netstat(1)](netstat.1.md), procstat(1), setfib(1), libxo(3), [inet(4)](../man4/inet.4.md), [inet6(4)](../man4/inet6.4.md), [divert(4)](../man4/divert.4.md), [tcp(4)](../man4/tcp.4.md), [sctp(4)](../man4/sctp.4.md), [udp(4)](../man4/udp.4.md), [unix(4)](../man4/unix.4.md), xo_options(7)

## 历史

`sockstat` 命令首次出现在 FreeBSD 3.1 中。

## 作者

`sockstat` 命令及本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
