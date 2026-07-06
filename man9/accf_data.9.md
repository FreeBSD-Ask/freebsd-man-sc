# accf\_data.9

`accf_data` — 缓冲传入连接直到数据到达

## 名称

`accf_data`

## 概要

```sh
options INET
options ACCEPT_FILTER_DATA
```

在 **rc.conf(5)** 中：

```sh
kld_list="accf_data"
```

## 描述

这是一个放置在 socket 上的过滤器，该 socket 将使用 accept 来接收传入连接。

它阻止应用程序通过 accept 接收已连接的描述符，直到连接上有数据到达。

`ACCEPT_FILTER_DATA` 内核选项同时也是一个模块，如果 INET 选项已编译进内核，则可在运行时通过 [kldload(8)](../man8/kldload.8.md) 启用。

## 实例

假设 ACCEPT_FILTER_DATA 已包含在内核配置文件中，或者 `accf_data` 模块已加载，以下代码将在 socket `sok` 上启用 data 接受过滤器。

```c
struct accept_filter_arg afa;
bzero(&afa, sizeof(afa));
strcpy(afa.af_name, "dataready");
setsockopt(sok, SOL_SOCKET, SO_ACCEPTFILTER, &afa, sizeof(afa));
```

## 参见

setsockopt(2), [accept_filter(9)](accept_filter.9.md), [accf_dns(9)](accf_dns.9.md), [accf_http(9)](accf_http.9.md)

## 历史

接受过滤器机制和 accf_data 过滤器引入于 FreeBSD 4.0。

## 作者

本手册页及过滤器由 Alfred Perlstein 编写。
