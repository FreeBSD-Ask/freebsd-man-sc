# config_intrhook.9

`config_intrhook` — 调度在启用中断后、挂载根文件系统前运行的函数

## 名称

`config_intrhook`

## 概要

```c
#include <sys/kernel.h>

typedef void (*ich_func_t)(void *arg);

int
config_intrhook_establish(struct intr_config_hook *hook)

void
config_intrhook_disestablish(struct intr_config_hook *hook)

int
config_intrhook_drain(struct intr_config_hook *hook)

void
config_intrhook_oneshot(ich_func_t func, void *arg)
```

## 描述

`config_intrhook_establish` 函数调度在启用中断后、挂载根文件系统前运行的函数。如果系统已通过初始化中的此点，则立即调用该函数。

`config_intrhook_disestablish` 函数从钩子队列中移除该条目。

`config_intrhook_drain` 函数以安全方式从钩子队列中移除该条目。如果钩子当前未活动，它将 `hook` 从钩子队列中移除并返回 `ICHS_QUEUED`。如果钩子活动，它等待钩子完成后再返回 `ICHS_RUNNING`。如果钩子先前已完成，它返回 `ICHS_DONE`。由于 `config_intrhook` 在 `config_intrhook_establish` 之前未定义，此函数只能在该函数返回后调用。

`config_intrhook_oneshot` 函数调度按 `config_intrhook_establish` 描述方式运行的函数；该函数运行后，条目自动从钩子队列中移除。这适用于需要在启用中断后进行额外设备配置，但之后无需拖延引导过程的情况。此函数使用 M_WAITOK 分配内存；不要在持有任何不可睡眠锁时调用此函数。

在挂载根文件系统之前，运行所有先前建立的钩子。然后引导过程被拖延，直到所有处理程序使用 `config_intrhook_disestablish` 从钩子队列中移除其钩子。然后引导过程继续尝试挂载根文件系统。任何可能提供希望作为根挂载的设备的驱动程序必须使用此钩子，或在初始探测中探测所有这些设备。由于在探测过程中禁用中断，许多驱动程序需要一种在启用中断的情况下探测设备的方法。

请求通过 `intr_config_hook` 结构发出。此结构定义如下：

```c
struct intr_config_hook {
	TAILQ_ENTRY(intr_config_hook) ich_links;/* 私有 */
	ich_func_t	ich_func;		/* 要调用的函数 */
	void		*ich_arg;		/* 调用参数 */
};
```

`intr_config_hook` 结构的存储必须由驱动程序提供。它必须在钩子建立之前到钩子解除之后期间保持稳定。

具体来说，钩子在 `SI_SUB_INT_CONFIG_HOOKS` 处运行，即调度器启动后、发现根文件系统设备之前。

## 返回值

返回零表示钩子已成功添加到队列（延迟或立即执行）。返回非零表示无法将钩子添加到队列，因为它已在队列中。

## 参见

[DEVICE_ATTACH(9)](DEVICE_ATTACH.9.md)

## 历史

这些函数在 FreeBSD 3.0 中随 CAM 子系统引入，但可供任何驱动程序使用。

## 作者

这些函数由 Justin Gibbs <gibbs@FreeBSD.org> 编写。本手册页由 M. Warner Losh <imp@FreeBSD.org> 编写。
