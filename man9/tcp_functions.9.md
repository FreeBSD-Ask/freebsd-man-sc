# tcp\_functions.9

`tcp_functions` — 替代 TCP 栈框架

## 名称

`tcp_functions`

## 概要

`#include <netinet/tcp.h>`

`#include <netinet/tcp_var.h>`

`int register_tcp_functions(struct tcp_function_block *blk, int wait)`

`int register_tcp_functions_as_name(struct tcp_function_block *blk, const char *name, int wait)`

`int register_tcp_functions_as_names(struct tcp_function_block *blk, int wait, const char *names[], int *num_names)`

`int deregister_tcp_functions(struct tcp_function_block *blk)`

## 描述

`tcp_functions` 框架允许内核开发者实现替代的 TCP 栈。替代栈可以编译进内核，也可以在可加载内核模块中实现。此功能旨在鼓励对 TCP 栈进行实验，并允许在单个系统上为不同的 TCP 连接部署不同的行为。

系统管理员可以设置系统默认栈。默认情况下，所有 TCP 连接将使用系统默认栈。此外，用户可以按连接指定使用特定的栈。（有关设置系统默认栈或为给定连接选择特定栈的详细信息，请参见 [tcp(4)](../man4/tcp.4.md)。）

本手册页将"TCP 栈"视为"函数块"的同义词。这是有意的。"TCP 栈"是实现一组行为的函数集合。因此，替代的"函数块"定义了替代的"TCP 栈"。

`register_tcp_functions()`、`register_tcp_functions_as_name()` 和 `register_tcp_functions_as_names()` 函数请求系统添加指定的函数块并以给定名称注册。模块可以使用不同名称多次注册同一函数块。但是，名称在所有已注册的函数块中必须全局唯一。此外，模块在注册函数块后，不得修改函数块的内容（包括名称），除非模块先成功注销该函数块。

`register_tcp_functions()` 函数请求系统使用函数块 `tfb_tcp_block_name` 字段中定义的名称注册函数块。注意，这是三个注册函数中唯一一个自动使用函数块 `tfb_tcp_block_name` 字段中定义的名称注册函数块的函数。如果模块使用其他注册函数之一，它可以通过显式提供该名称来请求系统使用函数块 `tfb_tcp_block_name` 字段中定义的名称注册函数块。

`register_tcp_functions_as_name()` 函数请求系统使用 `name` 参数中提供的名称注册函数块。

`register_tcp_functions_as_names()` 函数请求系统使用 `names` 参数中提供的所有名称注册函数块。`num_names` 参数提供指向名称数量的指针。此数量不得超过 TCP_FUNCTION_NAME_NUM_MAX。此函数要么成功注册数组中的所有名称，要么不注册数组中的任何名称。失败时，`num_names` 参数将更新为系统遇到错误时正在处理的 `names` 数组条目的索引号。

`deregister_tcp_functions()` 函数请求系统从系统中移除指定的函数块。如果此调用成功，将完全注销该函数块，无论注册该函数块时使用了多少个名称。如果调用因套接字仍在使用指定函数块而失败，系统会将该函数块标记为正在移除中。这将阻止其他套接字使用指定函数块。但是，它不会影响已经在使用该函数块的套接字。

`tcp_functions` 模块必须在初始化期间调用一个或多个注册函数，并在允许模块卸载之前成功调用 `deregister_tcp_functions()` 函数。

`blk` 参数是指向 `struct tcp_function_block` 的指针，其说明见下文（参见函数块结构）。`wait` 参数用作 [malloc(9)](malloc.9.md) 的 `flags` 参数，必须设置为该手册页中定义的有效值之一。

### 函数块结构

`blk` 参数是指向 `struct tcp_function_block` 的指针，该结构具有以下成员：

```c
struct tcp_function_block {
	char	tfb_tcp_block_name[TCP_FUNCTION_NAME_LEN_MAX];
	int	(*tfb_tcp_output)(struct tcpcb *);
	void	(*tfb_tcp_do_segment)(struct mbuf *, struct tcphdr *,
			    struct socket *, struct tcpcb *,
			    int, int, uint8_t,
			    int);
	int     (*tfb_tcp_ctloutput)(struct socket *so,
			    struct sockopt *sopt,
			    struct inpcb *inp, struct tcpcb *tp);
	/* 可选的内存分配/释放例程 */
	void	(*tfb_tcp_fb_init)(struct tcpcb *);
	void	(*tfb_tcp_fb_fini)(struct tcpcb *, int);
	/* 可选定时期，定义一个则必须定义全部 */
	int	(*tfb_tcp_timer_stop_all)(struct tcpcb *);
	void	(*tfb_tcp_timer_activate)(struct tcpcb *,
			    uint32_t, u_int);
	int	(*tfb_tcp_timer_active)(struct tcpcb *, uint32_t);
	void	(*tfb_tcp_timer_stop)(struct tcpcb *, uint32_t);
	/* 可选函数 */
	void	(*tfb_tcp_rexmit_tmr)(struct tcpcb *);
	/* 必需函数 */
	int	(*tfb_tcp_handoff_ok)(struct tcpcb *);
	/* 系统使用 */
	volatile uint32_t tfb_refcnt;
	uint32_t  tfb_flags;
};
```

`tfb_tcp_block_name` 字段标识 TCP 栈的唯一名称，长度不应超过 TCP_FUNCTION_NAME_LEN_MAX-1 个字符。

`tfb_tcp_output`、`tfb_tcp_do_segment` 和 `tfb_tcp_ctloutput` 字段是指向函数的指针，这些函数分别执行与默认 `tcp_output()`、`tcp_do_segment()` 和 `tcp_default_ctloutput()` 函数等效的操作。这些函数指针都必须非 NULL。

如果 TCP 栈需要在套接字首次选择该 TCP 栈时（或套接字首次打开时）初始化数据，应在 `tfb_tcp_fb_init` 字段中设置非 NULL 指针。同样，如果 TCP 栈需要在套接字停止使用该 TCP 栈时（或套接字关闭时）清理数据，应在 `tfb_tcp_fb_fini` 字段中设置非 NULL 指针。

如果 `tfb_tcp_fb_fini` 参数非 NULL，则当内核销毁 TCP 控制块或套接字转换为使用不同的 TCP 栈时，将调用其所指向的函数。该函数以 TCP 控制块和一个整数标志作为参数调用。如果套接字转换为使用另一个 TCP 栈，该标志为零；如果 TCP 控制块正在被销毁，该标志为一。

如果 TCP 栈实现了附加定时器，TCP 栈应在 `tfb_tcp_timer_stop_all`、`tfb_tcp_timer_activate`、`tfb_tcp_timer_active` 和 `tfb_tcp_timer_stop` 字段中设置非 NULL 指针。这些字段应全部为 `NULL` 或全部包含指向函数的指针。当 `tcp_timer_activate()`、`tcp_timer_active()` 和 `tcp_timer_stop()` 函数以非标准类型的定时器类型调用时，将分别调用 `tfb_tcp_timer_activate`、`tfb_tcp_timer_active` 和 `tfb_tcp_timer_stop` 函数。TCP 栈定义的函数与其补充的正常定时器函数具有相同的语义（包括参数和返回值）。

此外，栈可以通过在 `tfb_tcp_rexmit_tmr` 字段中设置非 NULL 函数指针来定义重传定时器触发时要采取的自身操作。此函数在处理重传定时器的过程中很早被调用。但是，必须注意确保重传定时器使 TCP 控制块处于有效状态，以供重传定时器逻辑的其余部分使用。

用户可在任何时候调用前选择新的 TCP 栈。因此，函数指针 `tfb_tcp_handoff_ok` 字段必须非 NULL。如果用户尝试选择该 TCP 栈，内核将调用 `tfb_tcp_handoff_ok` 字段所指向的函数。如果允许用户将套接字切换为使用该 TCP 栈，该函数应返回 0。在此情况下，如果此函数指针非 NULL，内核将调用 `tfb_tcp_fb_init` 所指向的函数，最后执行栈切换。如果不允许用户切换套接字，该函数应撤销对连接状态配置所做的任何更改并返回错误代码，该代码将返回给用户。

`tfb_refcnt` 和 `tfb_flags` 字段由内核的 TCP 代码使用，将在 TCP 栈注册时初始化。

### 替代 TCP 栈的要求

如果 TCP 栈需要存储超出默认 TCP 控制块所存储内容的数据，TCP 栈可以初始化自身的每连接存储。`struct tcpcb` 控制块结构中的 `t_fb_ptr` 字段已保留用于保存指向此每连接存储的指针。如果 TCP 栈使用此替代存储，应理解 `t_fb_ptr` 指针的值可能未被初始化为 `NULL`。因此，应使用 `tfb_tcp_fb_init` 函数初始化此字段。此外，应使用 `tfb_tcp_fb_fini` 函数在套接字关闭时释放存储。

理解替代 TCP 栈可能保留不同的数据集合。但是，为了确保数据以标准化格式对用户和系统其余部分可用，替代 TCP 栈必须在实际可行的最大程度上更新 TCP 控制块中的所有字段。

## 返回值

`register_tcp_functions()`、`register_tcp_functions_as_name()`、`register_tcp_functions_as_names()` 和 `deregister_tcp_functions()` 函数成功时返回零，失败时返回非零值。特别是，`deregister_tcp_functions()` 在没有更多连接使用指定 TCP 栈之前将返回 `EBUSY`。调用 `deregister_tcp_functions()` 的模块必须准备好等待，直到所有连接都停止使用指定的 TCP 栈。

## 错误

`register_tcp_functions()`、`register_tcp_functions_as_name()` 和 `register_tcp_functions_as_names()` 函数在以下情况下将失败：

**[`EINVAL`]** `blk` 参数的任何成员设置不正确。

**[`ENOMEM`]** 函数无法为其内部数据分配内存。

**[`EALREADY`]** `blk` 已注册，或已存在使用相同名称注册的函数块。

此外，`register_tcp_functions_as_names()` 在以下情况下将失败：

**[`E2BIG`]** `num_names` 参数指向的名称数量大于 TCP_FUNCTION_NAME_NUM_MAX。

`deregister_tcp_functions()` 函数在以下情况下将失败：

**[`EPERM`]** `blk` 参数引用内核编译时内置的默认函数块。

**[`EBUSY`]** 函数块仍被一个或多个套接字使用，或被定义为当前默认函数块。

**[`ENOENT`]** `blk` 参数引用当前未注册的函数块。

## 参见

connect(2), listen(2), [tcp(4)](../man4/tcp.4.md), [malloc(9)](malloc.9.md)

## 历史

此框架首次出现在 FreeBSD 11.0 中。

## 作者

`tcp_functions` 框架由 Randall Stewart <rrs@FreeBSD.org> 编写。

本手册页由 Jonathan Looney <jtl@FreeBSD.org> 编写。
