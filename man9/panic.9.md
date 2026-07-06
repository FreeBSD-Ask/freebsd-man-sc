# panic.9

`panic` — 在致命错误时关闭系统

## 名称

`panic`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/systm.h>
```

```c
extern char *panicstr;

void
panic(const char *fmt, ...)

void
vpanic(const char *fmt, va_list ap)

KERNEL_PANICKED()
```

## 描述

`panic` 和 `vpanic` 函数终止正在运行的系统。消息 `fmt` 是一个 printf(3) 风格的格式字符串。该消息会打印到控制台，并将 `panicstr` 设置为指向消息文本的地址。稍后可以从核心转储中检索此值。

进入 `panic` 函数时，恐慌线程会禁用中断并调用 [critical_enter(9)](critical_enter.9.md)。这可以防止线程在系统仍处于运行状态时被抢占或中断。接下来，它会指示系统中的其他 CPU 停止。这与其他线程同步，以防止并发恐慌相互干扰。在不太可能发生的并发恐慌中，只有一个恐慌线程会继续。

控制权将通过 `kdb_enter` 传递给内核调试器。这取决于是否安装并启用了调试器，由 `debugger_on_panic` 变量控制；参见 [ddb(4)](../man4/ddb.4.md) 和 [gdb(4)](../man4/gdb.4.md)。调试器可能启动系统重置，或者最终返回。

最后，`panic` 函数会调用 [kern_reboot(9)](kern_reboot.9.md) 重启系统，并请求内核转储。如果递归调用 `panic`（例如从磁盘同步例程中），会指示 `kern_reboot` 不要同步磁盘。

`vpanic` 函数实现了 `panic` 的主体。它适合由执行自己的可变长度参数处理的函数调用。在所有其他情况下，优先使用 `panic`。

`KERNEL_PANICKED` 宏是确定系统是否已恐慌的首选方式。它返回一个布尔值。最常见的是，这用于避免在恐慌上下文中执行不可能成功的操作。

## 执行上下文

一旦恐慌启动，在恐慌上下文中执行的代码受以下限制：

- 单线程执行。调度器已禁用，其他 CPU 已停止/强制空闲。必须避免操作调度器状态的函数。这包括但不限于 wakeup(9) 和 [sleepqueue(9)](sleepqueue.9.md) 函数。
- 中断已禁用。设备 I/O（例如到控制台）必须通过轮询完成。
- 不能依赖动态内存分配，必须避免。
- 锁的获取/释放会被忽略，这意味着这些操作看似成功。
- 在资源上休眠并非严格禁止，但会导致睡眠函数立即返回。基于时间的睡眠如 pause(9) 可能以忙等待方式执行。

## 返回值

`panic` 和 `vpanic` 函数不返回。

## 参见

printf(3), [ddb(4)](../man4/ddb.4.md), [gdb(4)](../man4/gdb.4.md), [KASSERT(9)](kassert.9.md), [kern_reboot(9)](kern_reboot.9.md)
