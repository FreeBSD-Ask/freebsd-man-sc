# accf\_tls.9

`accf_tls` — 缓冲传入连接直到类似 TLS 握手的请求到达

## 名称

`accf_tls`

## 概要

```sh
options INET
options ACCEPT_FILTER_TLS
```

在 **rc.conf(5)** 中：

```sh
kld_list="accf_tls"
```

## 描述

这是一个放置在 socket 上的过滤器，该 socket 将使用 accept(2) 来接收传入的 HTTPS 连接。它阻止应用程序通过 accept(2) 接收已连接的描述符，直到内核缓冲了完整的 TLS 握手。`accf_tls` 首先检查偏移 0 处的字节是否为 `0x16`，该值匹配握手类型。然后读取偏移 3 处的 2 字节请求长度值，并继续读取直到缓冲了整个握手长度。如果偏移 0 处的值不是 `0x16`，内核将允许应用程序通过 accept(2) 接收连接描述符。

`accf_tls` 的作用在于，服务器在执行初始请求解析前无需多次上下文切换。这通过保持 Apache 等预派生服务器中的活动进程数量较少，并减小基于 select、poll 或 kevent 的服务器需要管理的文件描述符集合大小，有效降低了处理传入请求所需的 CPU 利用率。

## 实例

假设 ACCEPT_FILTER_TLS 已包含在内核配置文件中，或者 `accf_tls` 模块已加载，以下代码将在 socket `sok` 上启用 TLS 接受过滤器。

```c
struct accept_filter_arg afa;
bzero(&afa, sizeof(afa));
strcpy(afa.af_name, "tlsready");
setsockopt(sok, SOL_SOCKET, SO_ACCEPTFILTER, &afa, sizeof(afa));
```

## 参见

setsockopt(2), [accept_filter(9)](accept_filter.9.md)

## 历史

`accf_tls` 接受过滤器引入于 FreeBSD 15.0。

## 作者

`accf_tls` 过滤器由 Maksim Yevmenkin 编写。
