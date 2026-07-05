# kern_reboot.9

`kern_reboot` — 重启、停机或关闭系统电源

## 名称

`kern_reboot`, `shutdown_nice`

## 概要

```c
#include <sys/types.h>
#include <sys/systm.h>
#include <sys/reboot.h>

extern int rebooting;

void
kern_reboot(int howto)

void
shutdown_nice(int howto)
```

```c
#include <sys/eventhandler.h>

EVENTHANDLER_REGISTER(shutdown_pre_sync, shutdown_fn, private, priority)
EVENTHANDLER_REGISTER(shutdown_post_sync, shutdown_fn, private, priority)
EVENTHANDLER_REGISTER(shutdown_final, shutdown_fn, private, priority)
```

## 描述

`kern_reboot` 函数处理最终的系统关闭，并停机、重启或关闭系统电源。要采取的确切操作由 `howto` 中传递的标志决定。

相关标志为：

**`RB_HALT`** 就地停机系统而不是重新启动。
**`RB_POWEROFF`** 关闭系统电源而不是重新启动。
**`RB_POWERCYCLE`** 在重新启动之外还请求电源循环。
**`RB_NOSYNC`** 在关闭期间不同步文件系统。
**`RB_DUMP`** 在关闭期间转储内核内存。

`howto` 字段及其完整标志列表由 reboot(2) 更详细地描述。

`kern_reboot` 执行以下操作：

- 将 `rebooting` 变量设置为 `1`，表示重启过程已开始且无法停止。
- 除非 `howto` 中设置了 `RB_NOSYNC` 标志，否则通过调用 [vfs_unmountall(9)](vfs_unmountall.9.md) 同步并卸载系统磁盘。
- 如果是在 panic 后重启（`howto` 中设置了 `RB_DUMP`，但未设置 `RB_HALT`），通过 `doadump` 启动系统崩溃转储。
- 打印一条消息指示系统即将停机或重启，以及系统总运行时间的报告。
- 执行所有已注册的关闭钩子。参见下文的“关闭钩子”。
- 作为最后手段，如果没有关闭钩子处理重启，调用与机器相关的 `cpu_reset` 函数。在不太可能不支持此操作的情况下，`kern_reboot` 将在函数末尾永远循环。这需要手动重置系统。

`kern_reboot` 可以在系统正常运行时从典型的内核执行上下文中调用。它也可以作为内核 panic 的最后一步调用，或从内核调试器中调用。因此，此函数中的代码受 [panic(9)](panic.9.md) 手册页“执行上下文”一节中描述的限制。

`shutdown_nice` 函数是在系统正常运行条件下执行干净重启或关闭的预期路径。调用此函数将向 [init(8)](../man8/init.8.md) 进程发送信号，指示其执行关闭。当 [init(8)](../man8/init.8.md) 干净地终止其子进程后，它将执行 reboot(2) 系统调用，进而调用 `kern_reboot`。

如果在 [init(8)](../man8/init.8.md) 进程产生之前调用 `shutdown_nice`，或者系统已 panic 或以其他方式停机，则将直接调用 `kern_reboot`。

## 关闭钩子

系统定义了三个独立的 [EVENTHANDLER(9)](EVENTHANDLER.9.md) 事件，在关闭过程中依次调用。它们是 `shutdown_pre_sync`、`shutdown_post_sync` 和 `shutdown_final`。它们将按列出的顺序无条件执行。注册到这些事件中任何一个的处理函数都将接收 `howto` 的值作为其第二个参数，可用于决定要采取的操作。

`shutdown_pre_sync` 事件在将文件系统同步到磁盘之前调用。它使任何必须在此点之前发生的操作或状态转换得以进行。

`shutdown_post_sync` 事件在文件系统同步完成之后立即调用。例如，它使磁盘驱动程序能够通过将缓存刷新到磁盘来完成同步。注意，此事件仍在可选的内核核心转储之前发生。

`shutdown_final` 事件作为 `kern_reboot` 的最后一步调用。诸如 [acpi(4)](../man4/acpi.4.md) 之类的驱动程序和子系统可以向此事件注册处理程序，以执行实际的重启、关机或停机。

值得注意的是，`shutdown_final` 事件也是所有内核模块执行其关闭（`MOD_SHUTDOWN`）钩子的点，以及递归在所有设备上执行 [DEVICE_SHUTDOWN(9)](DEVICE_SHUTDOWN.9.md) 方法的点。

所有事件处理程序与 `kern_reboot` 本身一样，可以在正常关闭上下文或内核 panic 或调试器上下文中运行。处理函数应注意不要触发递归 panic。

## 返回值

`kern_reboot` 函数不返回。

`shutdown_nice` 函数通常会返回给其调用者，并已启动异步系统关闭。当从 panic 或调试器上下文调用，或在早期引导期间调用时，它不会返回。

## 实例

假设的驱动程序 foo(4) 定义了一个 `shutdown_final` 事件处理程序，它可以通过写入设备寄存器来处理系统关机，但不处理停机或重置。

```c
void
foo_poweroff_handler(struct void *arg, int howto)
{
        struct foo_softc *sc = arg;
        uint32_t reg;
        if ((howto & RB_POWEROFF) != 0) {
                reg = FOO_POWEROFF;
                WRITE4(sc, FOO_POWEROFF_REG, reg);
        }
}
```

然后，在设备附加例程中注册该处理程序：

```c
int
foo_attach(device_t dev)
{
        struct foo_softc *sc;
        ...
        /* 将设备的软件上下文作为私有参数传递。 */
        EVENTHANDLER_REGISTER(shutdown_final, foo_poweroff_handler, sc,
            SHUTDOWN_PRI_DEFAULT);
        ...
}
```

此 `shutdown_final` 处理程序使用 `RB_NOSYNC` 标志检测是否发生了 panic 或其他异常情况，并提前返回：

```c
void
bar_shutdown_final(struct void *arg, int howto)
{
        if ((howto & RB_NOSYNC) != 0)
                return;
        /* 一些非 panic 安全的代码。 */
        ...
}
```

## 参见

reboot(2), [init(8)](../man8/init.8.md), [DEVICE_SHUTDOWN(9)](DEVICE_SHUTDOWN.9.md), [EVENTHANDLER(9)](EVENTHANDLER.9.md), [module(9)](module.9.md), [panic(9)](panic.9.md), [vfs_unmountall(9)](vfs_unmountall.9.md)
