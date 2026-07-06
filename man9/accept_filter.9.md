# accept\_filter.9

`accept_filter` — 过滤传入连接

## 名称

`accept_filter`, `accept_filt_add`, `accept_filt_del`, `accept_filt_generic_mod_event`, `accept_filt_get`

## 概要

```c
#include <sys/types.h>

#include <sys/module.h>

#include <sys/socket.h>

#define ACCEPT_FILTER_MOD

#include <sys/socketvar.h>

int
accept_filt_add(struct accept_filter *filt)

int
accept_filt_del(char *name)

int
accept_filt_generic_mod_event(module_t mod, int event, void *data)

struct accept_filter *
accept_filt_get(char *name)
```

## 描述

接受过滤器（accept filter）允许应用程序请求内核对传入连接进行预处理。通过 setsockopt(2) 系统调用请求接受过滤器，传入 `SO_ACCEPTFILTER` 作为 `optname`。

## 实现说明

希望成为接受过滤器的模块必须向系统提供一个 `struct accept_filter`：

```c
struct accept_filter {
	char	accf_name[16];
	void	(*accf_callback)(struct socket *so, void *arg, int waitflag);
	void *	(*accf_create)(struct socket *so, char *arg);
	void	(*accf_destroy)(struct socket *so);
	SLIST_ENTRY(accept_filter) accf_next;	/* 链表中的下一项 */
};
```

模块应通过 `accept_filt_add` 函数注册该结构，传入指向由 [malloc(9)](malloc.9.md) 分配的 `struct accept_filter` 的指针。

`struct accept_filter` 的字段如下：

**`accf_name`** 过滤器的名称；用户态将通过此名称访问它。

**`accf_callback`** 连接建立后内核将调用的回调函数。它与 socket upcall 相同，在连接建立时以及 socket 上每次有新数据到达时被调用，除非回调修改了 socket 的标志。

**`accf_create`** 在 setsockopt(2) 将过滤器安装到监听 socket 时调用。

**`accf_destroy`** 在用户移除 socket 上的接受过滤器时调用。

`accept_filt_del` 函数接受与 `accept_filt_add` 注册时 `accept_filter.accf_name` 中使用的相同字符串，内核随后将禁止用户态继续使用该过滤器。

`accept_filt_get` 函数在内部使用，通过 setsockopt(2) 系统调用定位要使用的接受过滤器。

`accept_filt_generic_mod_event` 函数提供了一种简单的方式，避免对于不使用参数字段来加载和卸载自身的接受过滤器重复代码。此函数可用于 [DECLARE_MODULE(9)](DECLARE_MODULE.9.md) 宏的 `moduledata_t` 结构。

## 参见

setsockopt(2), [accf_data(9)](accf_data.9.md), [accf_dns(9)](accf_dns.9.md), [accf_http(9)](accf_http.9.md), [malloc(9)](malloc.9.md)

## 历史

接受过滤器机制引入于 FreeBSD 4.0。

## 作者

本手册页由 Alfred Perlstein、Sheldon Hearn 和 Jeroen Ruigrok van der Werven 编写。

接受过滤器概念由 Yahoo! 的 David Filo 首创，并由 Alfred Perlstein 改进为可加载模块系统。
