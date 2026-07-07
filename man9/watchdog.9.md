# watchdog(9)

`watchdog` — 软件和硬件看门狗设施

## 名称

`watchdog` — 软件和硬件看门狗设施

## 概要

```c
#include <sys/watchdog.h>

void
watchdog_fn(void *private, u_int cmd, int *error)

EVENTHANDLER_REGISTER(watchdog_list, watchdog_fn, private, 0)

EVENTHANDLER_DEREGISTER(watchdog_list, eventhandler_tag)
```

## 描述

要以软件或硬件方式实现一个看门狗，只需编写单个函数并将其注册到全局的 `watchdog_list` 上即可。

该函数必须检查 `cmd` 参数，并按以下规则执行操作：

如果 `cmd` 为零，则必须禁用看门狗，且 `error` 参数保持不变。如果看门狗无法被禁用，则必须将 `error` 参数设置为 `EOPNOTSUPP`。

否则，应重置看门狗并将其超时配置为 (1 << (`cmd` & `WD_INTERVAL`)) 纳秒或更大值，同时将 `error` 参数设置为零，以表示看门狗已被启用。

如果看门狗无法配置为所提议的超时值，则必须禁用看门狗，并将 `error` 参数保持原样（以避免掩盖另一个看门狗的启用动作）。

对于看门狗超时时应执行的操作没有明确规定，但建议采用硬件复位或类似“激烈但确定”的行为。

## 参见

[watchdog(4)](../man4/watchdog.4.md)

## 作者

`watchdog` 设施及本手册页由 Poul-Henning Kamp <phk@FreeBSD.org> 编写。
