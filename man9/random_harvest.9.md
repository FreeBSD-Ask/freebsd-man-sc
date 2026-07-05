# random\_harvest.9

`random_harvest` — 为熵设备从内核收集熵

## 名称

`random_harvest`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/random.h>
```

```c
void
random_harvest_direct(void *entropy, u_int size, enum esource source)

void
random_harvest_fast(void *entropy, u_int size, enum esource source)

void
random_harvest_queue(void *entropy, u_int size, enum esource source)
```

## 描述

`random_harvest_*` 函数由设备驱动程序和其他内核进程使用，用于将认为（至少部分）随机的数据传递给熵设备。

调用者应在 `entropy` 中传递指向“随机”数据的指针。参数 `size` 包含所指向的字节数。`source` 从 `sys/dev/random.h` 中枚举的值之一中选择，用于指示熵的来源。

`random_harvest_direct` 变体用于在启用任何多任务处理之前的早期收集。

`random_harvest_fast` 变体由不应因收集而遭受性能损失的源使用，因为它们是高速率源。会牺牲一些熵，但高速率的供应将补偿这一点。

`random_harvest_queue` 变体用于一般收集，是大多数熵源（如中断或控制台事件）的默认选择。

中断收集已在一定程度上为内核程序员简化。如果设备驱动程序使用 [BUS_SETUP_INTR(9)](bus_setup_intr.9.md) 或 bus_setup_intr(9) 注册中断处理程序，则只需在 `flags` 参数中包含 `INTR_ENTROPY` 位即可使该中断源用于熵收集。应在可行的任何地方执行此操作。

## 参见

[random(4)](../man4/random.4.md), [BUS_SETUP_INTR(9)](bus_setup_intr.9.md)

## 作者

FreeBSD [random(4)](../man4/random.4.md) 熵设备及相关文档由 Mark R V Murray 编写。
