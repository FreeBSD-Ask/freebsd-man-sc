# watchdog.4

`watchdog` — 硬件和软件看门狗

## 名称

`watchdog`

## 概要

`#include <sys/watchdog.h>`

## 描述

`watchdog` 设施用于控制硬件和软件看门狗。

设备 **/dev/fido** 支持若干可选的 ioctl(2) 调用进行配置，并响应一组操作 ioctl(2) 调用：

**`WDIOCPATPAT`** 喂狗（pat the watchdog）。

**`WDIOC_CONTROL`** 启用、禁用或重置看门狗。

`WDIOCPATPAT` ioctl(2) 调用接受单个参数，表示以 `sbintime_t` 形式指定的看门狗超时周期值。

如果可用的 [watchdog(9)](../man9/watchdog.9.md) 实现中至少有一个支持将超时设置为指定值，`WDIOCPATPAT` ioctl(2) 调用将返回成功。这意味着至少有一个看门狗已启用。默认情况下，如果存在硬件看门狗，将使用硬件看门狗；但如果没有硬件看门狗能处理请求，将启用默认的软件看门狗。如果调用失败（例如所有 [watchdog(9)](../man9/watchdog.9.md) 实现都不支持该超时时长），则所有看门狗都将被禁用，必须显式重新启用。

要禁用看门狗，使用带 `WD_CTRL_DISABLE` 标志的 `WDIOC_CONTROL` ioctl(2) 调用。如果解除看门狗失败，将返回错误。但看门狗可能仍处于启用状态！要重新启用看门狗，使用带 `WD_CTRL_ENABLE` 标志的 `WDIOC_CONTROL` ioctl(2) 调用。喂狗的另一种方法是使用带 `WDIOC_CTRL_RESET` 标志的 `WDIOC_CONTROL` ioctl(2) 调用。

此处列出了可选的配置 ioctl(2) 命令及其使用的参数类型。使用示例可在 [watchdogd(8)](../man8/watchdogd.8.md) 中找到。

**`WDIOC_SETTIMEOUT`** `sbintime_t` 设置/重置定时器

**`WDIOC_GETTIMEOUT`** `sbintime_t` 获取总超时

**`WDIOC_GETTIMELEFT`** `sbintime_t` 获取剩余时间

**`WDIOC_GETPRETIMEOUT`** `sbintime_t` 获取预超时

**`WDIOC_SETPRETIMEOUT`** `sbintime_t` 设置预超时

**`WDIOC_SETPRETIMEOUTACT`** `int` 设置预超时发生时的动作（参见下文的 `WD_SOFT_*`）。

**`WDIOC_SETSOFT`** `int` 使用内部软件看门狗代替硬件看门狗。还有一种外部软件看门狗，在没有附加硬件看门狗时默认使用。

**`WDIOC_SETSOFTTIMEOUTACT`** `int` 设置软超时发生时的动作。

此处列出了可为预超时或内部软件看门狗指定的动作。可通过 OR 运算组合指定多个动作。

**`WD_SOFT_PANIC`** panic

**`WD_SOFT_DDB`** 进入调试器

**`WD_SOFT_LOG`** log(9)

**`WD_SOFT_PRINT`** printf(9)

## 返回值

`WDIOCPATPAT` ioctl(2) 成功时返回零，失败时返回非零值。

**[Er EOPNOTSUPP]** 内核中不存在看门狗，或所有看门狗都不支持请求的超时值（非零超时值）。

**[Er EOPNOTSUPP]** 看门狗无法禁用（超时值为 0）。

**[Er EINVAL]** 传递了无效的标志组合。

配置 ioctl(2) 操作成功时返回零，失败时返回非零值。

## 实例

```sh
#include <paths.h>
#include <sys/watchdog.h>
#define WDPATH	"/dev/" _PATH_WATCHDOG
int wdfd = -1;
static void
wd_init(void)
{
	wdfd = open(WDPATH, O_RDWR);
	if (wdfd == -1)
		err(1, WDPATH);
}
static void
wd_reset(u_int timeout)
{
	if (ioctl(wdfd, WDIOCPATPAT, &timeout) == -1)
		err(1, "WDIOCPATPAT");
}
/* 在 main() 中 */
wd_init();
wd_reset(WD_ACTIVE|WD_TO_8SEC);
/* 潜在的冻结点 */
wd_reset(WD_TO_NEVER);
```

启用看门狗以从潜在的代码冻结中恢复。

```sh
options SW_WATCHDOG
```

在你的内核配置中加入此选项，即使配置了硬件看门狗，也会强制配置内核中的软件看门狗，触发时进入 KDB 或 panic，具体取决于 KDB 和 KDB_UNATTENDED 内核配置选项。

## 参见

[watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`watchdog` 代码最早出现在 FreeBSD 5.1 中。

## 作者

`watchdog` 设施由 Poul-Henning Kamp <phk@FreeBSD.org> 编写。软件看门狗代码和本手册页由 Sean Kelly <smkelly@FreeBSD.org> 编写。Jeff Roberson <jeff@FreeBSD.org> 也作出了一些贡献。

## 缺陷

`WD_PASSIVE` 选项尚未实现。
