# BUS_SETUP_INTR(9)

`BUS_SETUP_INTR` — 创建、附加和拆卸中断处理程序

## 名称

`BUS_SETUP_INTR`, `bus_setup_intr`, `BUS_TEARDOWN_INTR`, `bus_teardown_intr`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
BUS_SETUP_INTR(device_t dev, device_t child, struct resource *irq,
    int flags, driver_filter_t *filter, driver_intr_t *ithread,
    void *arg, void **cookiep)

int
bus_setup_intr(device_t dev, struct resource *r, int flags,
    driver_filter_t filter, driver_intr_t ithread, void *arg,
    void **cookiep)

int
BUS_TEARDOWN_INTR(device_t dev, device_t child, struct resource *irq,
    void *cookiep)

int
bus_teardown_intr(device_t dev, struct resource *r, void *cookiep)
```

## 描述

`BUS_SETUP_INTR` 方法为先前由资源管理器的 BUS_ALLOC_RESOURCE(9) 方法分配的中断创建并附加中断处理程序。`flags` 定义于

`#include <sys/bus.h>`

用于给出中断的大致类别。`flags` 还告知中断处理程序有关设备驱动程序的某些特性。`INTR_EXCL` 将该处理程序标记为此中断的独占处理程序。`INTR_MPSAFE` 告知调度程序该中断处理程序在抢占式环境中表现良好（"SMP 安全"），不需要由"Giant Lock"互斥锁保护。`INTR_ENTROPY` 将该中断标记为良好的熵源——这可被熵设备 **/dev/random** 使用。

若要定义不会执行任何潜在阻塞操作的时间关键型处理程序，请使用 `filter` 参数。有关编写过滤例程的信息，参见下文的过滤例程小节。否则，使用 `ithread` 参数。所定义的处理程序将以 `arg` 的值作为其唯一参数被调用。有关编写中断处理程序的更多信息，参见下文的 ithread 例程小节。

`cookiep` 参数是一个指向 `void *` 的指针，如果 `BUS_SETUP_INTR` 成功建立中断，它会为父总线的使用写入一个 cookie。驱动程序编写者可以假定此 cookie 非零。nexus 驱动程序在失败时会向 `cookiep` 写入 0。

中断处理程序将通过 `BUS_TEARDOWN_INTR` 分离。需要将 cookie 传递给 `BUS_TEARDOWN_INTR` 以便拆卸正确的中断处理程序。一旦 `BUS_TEARDOWN_INTR` 返回，可以保证中断函数不再活动，也不会再被调用。

在调用这些函数期间不允许持有互斥锁。

### 过滤例程

过滤例程运行于主中断上下文。在此上下文中，不能使用普通互斥锁。只能使用其自旋锁版本（在初始化互斥锁时通过向 `mtx_init` 传递 `MTX_SPIN` 来指定）。可以调用 wakeup(9) 及类似例程。可以使用 `machine/atomic` 中的原子操作。可以通过 [bus_space(9)](bus_space.9.md) 读写硬件。可以读写 PCI 配置寄存器。不能使用所有其他内核接口。

在此受限环境中，必须注意处理所有竞态。还应仔细分析竞态。例如，多处理一次中断通常比用自旋锁保护变量更划算。如果其他线程正在访问相同的硬件寄存器，则需要仔细分析硬件寄存器的读-改-写周期。

通常，过滤例程会使用以下两种策略之一。第一种策略是简单地屏蔽硬件中的中断，让 `ithread` 例程从硬件读取状态，然后重新启用中断。`ithread` 在重新启用硬件中的中断源之前也会确认中断。大多数 PCI 硬件可以屏蔽其中断源。

第二种常见方法是使用过滤例程配合多个 [taskqueue(9)](taskqueue.9.md) 任务。在这种情况下，过滤例程确认中断并将工作排入适当的任务队列。当需要复用不同类型的中断源（例如网卡的发送和接收路径）时，这可以减少锁争用并提高性能。

你不应在过滤例程中调用 [malloc(9)](malloc.9.md)。不能调用任何使用普通互斥锁的函数。Witness 可能会对此发出警告。

### ithread 例程

在 ithread 例程中可以做任何想做的事，但不能睡眠。必须注意不要在 ithread 中睡眠。此外，应尽量减少 ithread 例程中的锁争用，因为争用的锁会波及该中断上的所有其他 ithread 例程。

### 睡眠

睡眠是指自愿放弃对线程的控制。msleep(9) 中的所有睡眠例程都会睡眠。等待 [condvar(9)](condvar.9.md) 中描述的条件变量属于睡眠。调用执行上述任何操作的函数都属于睡眠。

## 返回值

成功时返回零，否则返回一个适当的错误。

## 参见

[random(4)](../man4/random.4.md), [device(9)](device.9.md), [driver(9)](driver.9.md), [locking(9)](locking.9.md)

## 作者

本手册页由 Jeroen Ruigrok van der Werven <asmodai@FreeBSD.org> 基于 Doug Rabson <dfr@FreeBSD.org> 编写的 `BUS_CREATE_INTR` 和 `BUS_CONNECT_INTR` 手册页编写。
