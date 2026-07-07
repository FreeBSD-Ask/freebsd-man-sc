# accf_dns(9)

`accf_dns` — 缓冲传入 DNS 请求直到完整的首个请求到达

## 名称

`accf_dns`

## 概要

```c
options INET
options ACCEPT_FILTER_DNS
```

在 **rc.conf** 中：

```sh
kld_list="accf_dns"
```

## 描述

这是一个放置在将要使用 `accept` 接收传入连接的 socket 上的过滤器。

它阻止应用程序通过 `accept` 接收已连接描述符，直到 socket 上有完整的 DNS 请求可用。它通过读取请求的前两个字节来确定其大小，并等待直到所需数量的数据可供读取。

`ACCEPT_FILTER_DNS` 内核选项也是一个模块，如果 INET 选项已编译进内核，可在运行时通过 [kldload(8)](../man8/kldload.8.md) 启用。

## 实例

如果 `accf_dns` 模块在内核中可用，以下代码将在 socket `sok` 上启用 DNS 接受过滤器。

```c
	struct accept_filter_arg afa;
	bzero(&afa, sizeof(afa));
	strcpy(afa.af_name, "dnsready");
	setsockopt(sok, SOL_SOCKET, SO_ACCEPTFILTER, &afa, sizeof(afa));
```

## 参见

[setsockopt(2)](../sys/getsockopt.2.md), [accept_filter(9)](accept_filter.9.md), [accf_data(9)](accf_data.9.md), [accf_http(9)](accf_http.9.md)

## 历史

接受过滤器机制首次出现于 FreeBSD 4.0。

## 作者

本手册页和过滤器由 David Malone 编写。
