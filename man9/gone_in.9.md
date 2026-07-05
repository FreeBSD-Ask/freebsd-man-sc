# gone_in.9

`gone_in` — 弃用通知函数

## 名称

`gone_in`, `gone_in_dev`

## 概要

```c
#include <sys/systm.h>
```

```c
void
gone_in(int major, const char *msg, ...)
void
gone_in_dev(device_t dev, int major, const char *msg, ...)
```

## 描述

`gone_in` 函数用于提供内核正在积极使用已弃用的驱动程序或某些其他功能、并计划在未来的 FreeBSD 版本中移除的通知。该通知发送到内核 [dmesg(8)](../man8/dmesg.8.md) 日志，并出现在控制台上。`major` 参数指定将移除弃用功能的 FreeBSD 版本的主版本号。该通知仅打印一次，因此 `gone_in` 函数在经常执行的代码路径中使用是安全的。

`gone_in_dev` 会在通知前添加驱动程序名称。

在 `major` 之前的版本中，提供的通知将附加“To be removed in FreeBSD `major`”。

## 实例

```c
void
example_api(foo_t *args)
{
	gone_in(16, "Warning! %s[%u] uses obsolete API. ",
	    curthread->td_proc->p_comm, curthread->td_proc->p_pid);
	/* API 实现省略。 */
}
int
example_driver_attach(struct example_driver_softc *sc)
{
	/* 附加代码省略。 */
        gone_in_dev(sc->dev, 16, "driver is deprecated");
}
```

## 历史

`gone_in_dev` 函数首次出现于 FreeBSD 11。
