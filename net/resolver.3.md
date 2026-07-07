# resolver(3)

`res_query` — 解析器例程

## 名称

`res_query`, `res_search`, `res_mkquery`, `res_send`, `res_init`, `dn_comp`, `dn_expand`, `dn_skipname`, `ns_get16`, `ns_get32`, `ns_put16`, `ns_put32`

## 库

libc

## 概要

`#include <resolv.h>`

```c
int
res_query(const char *dname, int class, int type, u_char *answer,
    int anslen);

int
res_search(const char *dname, int class, int type, u_char *answer,
    int anslen);

int
res_mkquery(int op, const char *dname, int class, int type,
    const u_char *data, int datalen, const u_char *newrr_in,
    u_char *buf, int buflen);

int
res_send(const u_char *msg, int msglen, u_char *answer, int anslen);

int
res_init(void);

int
dn_comp(const char *exp_dn, u_char *comp_dn, int length,
    u_char **dnptrs, u_char **lastdnptr);

int
dn_expand(const u_char *msg, const u_char *eomorig,
    const u_char *comp_dn, char *exp_dn, int length);

int
dn_skipname(const u_char *comp_dn, const u_char *eom);

u_int
ns_get16(const u_char *src);

u_long
ns_get32(const u_char *src);

void
ns_put16(u_int src, u_char *dst);

void
ns_put32(u_long src, u_char *dst);
```

## 描述

这些例程用于向 Internet 域名服务器构造、发送和解释查询与应答消息。

解析器例程使用的全局配置和状态信息保存在 `_res` 结构中。大多数值具有合理的默认值，可以忽略。`_res.options` 中存储的选项定义于包含文件

`#include <resolv.h>`

如下所示。选项以简单位掩码的形式存储，包含已启用选项的按位"或"。

**`RES_INIT`** 如果初始名称服务器地址和默认域名已初始化（即已调用 `res_init`），则为真。

**`RES_DEBUG`** 打印调试消息。

**`RES_AAONLY`** 仅接受权威答案。使用此选项时，`res_send` 应继续直到找到权威答案或发现错误。目前未实现此功能。

**`RES_USEVC`** 使用 TCP 连接进行查询而非 UDP 数据报。

**`RES_STAYOPEN`** 与 `RES_USEVC` 一起使用，以在查询之间保持 TCP 连接打开。这仅在定期执行许多查询的程序中有用。UDP 应为正常使用的模式。

**`RES_IGNTC`** 目前未使用（忽略截断错误，即不使用 TCP 重试）。

**`RES_RECURSE`** 在查询中设置递归期望位。这是默认值。（`res_send` 不执行迭代查询，并期望名称服务器处理递归。）

**`RES_DEFNAMES`** 如果设置，`res_search` 会将默认域名追加到单组件名称（不包含点的名称）。此选项默认启用。

**`RES_DNSRCH`** 如果设置此选项，`res_search` 将在当前域和父域中搜索主机名；见 [hostname(7)](../man7/hostname.7.md)。这由标准主机查找例程 [gethostbyname(3)](gethostbyname.3.md) 使用。此选项默认启用。

**`RES_NOALIASES`** 此选项关闭由 `HOSTALIASES` 环境变量控制的用户级别别名功能。网络守护进程应设置此选项。

**`RES_USE_INET6`** 启用对仅 IPv6 应用程序的支持。这导致 IPv4 地址以 IPv4 映射地址的形式返回。例如，**10.1.1.1** 将返回为 **::ffff:10.1.1.1**。此选项仅在特定内核配置下有意义。

**`RES_USE_EDNS0`** 启用对 EDNS0 扩展的 OPT 伪 RR 支持。使用此选项时，解析器代码会将 OPT 伪 RR 附加到 DNS 查询中，以告知接收缓冲区大小。此选项允许 DNS 服务器利用非默认接收缓冲区大小，并发送更大的回复。带有 EDNS0 扩展的 DNS 查询包与非 EDNS0 DNS 服务器不兼容。

`res_init` 例程读取配置文件（如果有；见 [resolver(5)](../man5/resolver.5.md)）以获取默认域名、搜索列表和本地名称服务器的 Internet 地址。如果未配置服务器，则尝试运行解析器的主机。当前域名由主机名定义（如果未在配置文件中指定）；可以通过环境变量 `LOCALDOMAIN` 覆盖。如果你希望按进程覆盖*搜索列表*，此环境变量可以包含多个以空格分隔的标记。这类似于配置文件中的 `search` 命令。另一个环境变量 `RES_OPTIONS` 可以设置以覆盖某些内部解析器选项，这些选项否则通过更改 `_res` 结构中的字段或从配置文件的 `options` 命令继承来设置。`RES_OPTIONS` 环境变量的语法在 [resolver(5)](../man5/resolver.5.md) 中说明。初始化通常在首次调用以下例程之一时发生。

`res_query` 函数提供了对服务器查询机制的接口。它构造查询，将其发送到本地服务器，等待响应，并对回复进行初步检查。查询请求指定完全限定域名 `dname` 的指定 `type` 和 `class` 信息。回复消息留在 `answer` 缓冲区中，长度由调用者以 `anslen` 提供。

`res_search` 例程像 `res_query` 一样构造查询并等待响应，但此外，它还实现由 `RES_DEFNAMES` 和 `RES_DNSRCH` 选项控制的默认和搜索规则。它返回第一个成功的回复。

其余例程是 `res_query` 使用的较低级别例程。`res_mkquery` 函数构造标准查询消息并将其放入 `buf`。它返回查询的大小，如果查询大于 `buflen` 则返回 -1。查询类型 `op` 通常为 `QUERY`，但可以是定义于

`#include <arpa/nameser.h>`

的任何查询类型。查询的域名由 `dname` 给出。`newrr_in` 参数目前未使用，但旨在用于构造更新消息。

`res_send` 例程发送预格式化的查询并返回答案。如果未设置 `RES_INIT`，它将调用 `res_init`，将查询发送到本地名称服务器，并处理超时和重试。返回回复消息的长度，出错时返回 -1。

`dn_comp` 函数压缩域名 `exp_dn` 并将其存储在 `comp_dn` 中。返回压缩名称的大小，出错时返回 -1。`comp_dn` 所指向数组的大小由 `length` 给出。压缩使用指针数组 `dnptrs` 指向当前消息中先前压缩的名称。第一个指针指向消息的开头，列表以 `NULL` 结束。数组的限制由 `lastdnptr` 指定。`dn_comp` 的一个副作用是更新消息中插入标签的指针列表，因为名称会被压缩。如果 `dnptr` 为 `NULL`，则不压缩名称。如果 `lastdnptr` 为 `NULL`，则不更新标签列表。

`dn_expand` 条目将压缩的域名 `comp_dn` 展开为完整域名。压缩名称包含在查询或回复消息中；`msg` 是指向消息开头的指针。未压缩的名称放置在 `exp_dn` 指示的缓冲区中，其大小为 `length`。返回压缩名称的大小，出错时返回 -1。

`dn_skipname` 函数跳过压缩的域名，该域名从 `comp_dn` 指向的位置开始。压缩名称包含在查询或回复消息中；`eom` 是指向消息末尾的指针。返回压缩名称的大小，出错时返回 -1。

`ns_get16` 函数从 `src` 指向的缓冲区中获取一个 16 位量。

`ns_get32` 函数从 `src` 指向的缓冲区中获取一个 32 位量。

`ns_put16` 函数将一个 16 位量 `src` 放入 `dst` 指向的缓冲区。

`ns_put32` 函数将一个 32 位量 `src` 放入 `dst` 指向的缓冲区。

## 实现注释

此解析器实现是线程安全的，但如果程序员尝试声明自己的 `_res` 结构以替换该宏所引用的每线程版本，则无法正常工作。

必要时，可以指定以下编译时选项来更改解析器例程的默认行为。

**`RES_ENFORCE_RFC1034`** 如果在编译时定义了此符号，`res_search` 将强制执行 RFC 1034 检查，即不允许在主机名中使用下划线字符。这由标准主机查找例程（如 [gethostbyname(3)](gethostbyname.3.md)）使用。由于兼容性原因，此选项默认未启用。

## 返回值

`res_init` 函数成功时返回 0，在线程程序中如果无法分配每线程存储则返回 -1。

`res_mkquery`、`res_search` 和 `res_query` 函数成功时返回响应的大小，出错时返回 -1。可以检查整数 `h_errno` 以确定错误原因。更多信息见 [gethostbyname(3)](gethostbyname.3.md)。

## 文件

**/etc/resolv.conf** 配置文件，见 [resolver(5)](../man5/resolver.5.md)。

## 参见

[gethostbyname(3)](gethostbyname.3.md), [resolver(5)](../man5/resolver.5.md), [hostname(7)](../man7/hostname.7.md)

RFC1032, RFC1033, RFC1034, RFC1035, RFC974

## 历史

`res_query` 函数首次出现于 4.3BSD。
