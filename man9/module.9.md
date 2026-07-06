# module.9

`module` — 描述内核模块的结构

## 名称

`module`

## 描述

内核中的每个模块都由一个 `module_t` 结构描述。该结构包含设备名称、唯一的 ID 号、指向事件处理函数的指针以及传递给事件处理函数的参数指针，还有一些内核内部数据。如果事件处理函数为 `NULL`，模块将改用一个空操作函数处理程序。

[DECLARE_MODULE(9)](declare_module.9.md) 宏用于向系统注册模块。

当模块加载时，事件处理函数被调用，`what` 参数设置为 `MOD_LOAD`。

在卸载时，首先以 `what` 设置为 `MOD_QUIESCE` 调用该函数。如果卸载不是强制进行的，非零返回值将阻止卸载。

如果卸载继续进行，`what` 设置为 `MOD_UNLOAD`。如果模块对此返回非零值，卸载将不会发生。

`MOD_QUIESCE` 与 `MOD_UNLOAD` 的区别在于：模块当前正在使用时应使 `MOD_QUIESCE` 失败，而 `MOD_UNLOAD` 仅在无法卸载模块时才应失败，例如存在无法撤销的针对该模块的内存引用。

当系统关机时，`what` 包含 `MOD_SHUTDOWN` 值。

对于 `what` 不受支持和无法识别的值，模块应返回 `EOPNOTSUPP`。

## 实例

```c
#include <sys/param.h>
#include <sys/kernel.h>
#include <sys/module.h>
static int foo_handler(module_t mod, int /*modeventtype_t*/ what,
                       void *arg);
static moduledata_t mod_data= {
        "foo",
        foo_handler,
	NULL
};
MODULE_VERSION(foo, 1);
MODULE_DEPEND(foo, bar, 1, 3, 4);
DECLARE_MODULE(foo, mod_data, SI_SUB_EXEC, SI_ORDER_ANY);
```

## 参见

[DECLARE_MODULE(9)](declare_module.9.md), [DEV_MODULE(9)](dev_module.9.md), [DRIVER_MODULE(9)](driver_module.9.md), [MODULE_DEPEND(9)](module_depend.9.md), [MODULE_PNP_INFO(9)](module_pnp_info.9.md), [MODULE_VERSION(9)](module_version.9.md), [SYSCALL_MODULE(9)](syscall_module.9.md)

**/usr/share/examples/kld**

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写。
