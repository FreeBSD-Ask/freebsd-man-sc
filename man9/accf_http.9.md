# accf\_http.9

`accf_http` — 缓冲传入连接直到某个完整的 HTTP 请求到达

## 名称

`accf_http`

## 概要

```sh
options INET
options ACCEPT_FILTER_HTTP
```

在 **rc.conf(5)** 中：

```sh
kld_list="accf_http"
```

## 描述

这是一个放置在 socket 上的过滤器，该 socket 将使用 accept 来接收传入的 HTTP 连接。

它阻止应用程序通过 accept 接收已连接的描述符，直到内核缓冲了完整的 HTTP/1.0 或 HTTP/1.1 HEAD 或 GET 请求。

如果收到的不是 HTTP/1.0 或 HTTP/1.1 HEAD 或 GET 请求，内核将允许应用程序通过 accept 接收连接描述符。

`accf_http` 的作用在于，服务器在执行初始请求解析前无需多次上下文切换。这通过保持 Apache 等预派生服务器中的活动进程数量较少，并减小基于 select、poll 或 kevent 的服务器需要管理的文件描述符集合大小，有效降低了处理传入请求所需的 CPU 利用率。

`accf_http` 内核选项同时也是一个模块，如果 INET 选项已编译进内核，则可在运行时通过 [kldload(8)](../man8/kldload.8.md) 启用。

## 实例

假设 ACCEPT_FILTER_HTTP 已包含在内核配置文件中，或者 `accf_http` 模块已加载，以下代码将在 socket `sok` 上启用 http 接受过滤器。

```c
struct accept_filter_arg afa;
bzero(&afa, sizeof(afa));
strcpy(afa.af_name, "httpready");
setsockopt(sok, SOL_SOCKET, SO_ACCEPTFILTER, &afa, sizeof(afa));
```

## 参见

setsockopt(2), [accept_filter(9)](accept_filter.9.md)

## 历史

接受过滤器机制和 accf_http 过滤器引入于 FreeBSD 4.0。

## 作者

本手册页及过滤器由 Alfred Perlstein 编写。
