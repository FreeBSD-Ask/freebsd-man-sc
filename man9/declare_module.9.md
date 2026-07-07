# DECLARE_MODULE(9)

`DECLARE_MODULE` — 内核模块声明宏

## 名称

`DECLARE_MODULE`

## 概要

```c
#include <sys/param.h>
#include <sys/kernel.h>
#include <sys/module.h>
```

```c
DECLARE_MODULE(name, moduledata_t data, sub, order);
DECLARE_MODULE_TIED(name, moduledata_t data, sub, order);
```

## 描述

`DECLARE_MODULE` 宏声明一个通用内核模块。它用于使用 `SYSINIT` 宏向系统注册模块。`DECLARE_MODULE` 通常在其他宏中使用，例如 [DRIVER_MODULE(9)](driver_module.9.md)、[DEV_MODULE(9)](dev_module.9.md) 和 [SYSCALL_MODULE(9)](syscall_module.9.md)。当然，它也可以直接调用，例如用于实现动态 sysctl。

使用 `DECLARE_MODULE_TIED` 声明的模块只有在运行中的内核版本（由 `__FreeBSD_version` 指定）与构建时的内核版本完全相同时才会加载。此声明应用于依赖于稳定内核 KBI 之外接口的模块（例如依赖内部内核结构的 ABI 模拟器或 hypervisor）。当与内核一起编译时，`DECLARE_MODULE` 的行为类似于 `DECLARE_MODULE_TIED`。这允许锁和其他同步原语被安全地内联。

参数如下：

`#include <sys/kernel.h>`

**`name`** 模块名，将在 `SYSINIT` 调用中用于标识模块。

**`data`** `moduledata_t` 结构，包含两个主要项：模块的正式名称（将在 `module_t` 结构中使用）和指向类型为 `modeventhand_t` 的事件处理函数的指针。

**`sub`** 传递给 `SYSINIT` 宏的参数。有效值包含在 `sysinit_sub_id` 枚举中（参见并指定系统启动接口的类型。例如，[DRIVER_MODULE(9)](driver_module.9.md) 宏在此处使用 `SI_SUB_DRIVERS` 值，因为这些模块包含设备驱动程序。对于在运行时加载的内核模块，通常使用 `SI_SUB_EXEC` 值。

**`order`** `SYSINIT` 的参数。它表示 KLD 在子系统内初始化的顺序。有效值定义在 `sysinit_elem_order` 枚举中（**sys/kernel.h**）。

## 参见

[DEV_MODULE(9)](dev_module.9.md), [DRIVER_MODULE(9)](driver_module.9.md), [module(9)](module.9.md), [SYSCALL_MODULE(9)](syscall_module.9.md)

**/usr/include/sys/kernel.h**, **/usr/share/examples/kld**

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写，灵感来自 Andrew Reiter <arr@watson.org> 的 KLD Facility Programming Tutorial。
