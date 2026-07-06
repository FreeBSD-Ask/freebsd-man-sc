# DEV\_MODULE.9

`DEV_MODULE` — 设备驱动模块声明宏

## 名称

`DEV_MODULE`

## 概要

```c
#include <sys/param.h>

#include <sys/kernel.h>

#include <sys/module.h>

#include <sys/conf.h>

DEV_MODULE(name, modeventhand_t evh, void *arg)
```

## 描述

`DEV_MODULE` 宏声明一个设备驱动内核模块。它填充一个 `moduledata_t` 结构，然后使用正确的参数调用 `DECLARE_MODULE`，其中 `name` 是模块的名称，`evh`（及其参数 `arg`）是模块的事件处理程序（更多信息参见 [DECLARE_MODULE(9)](DECLARE_MODULE.9.md)）。事件处理程序应在加载时通过 `make_dev` 创建设备，并在卸载时使用 `destroy_dev` 销毁它。

## 实例

```c
#include <sys/module.h>
#include <sys/conf.h>
static struct cdevsw foo_devsw = { ... };
static struct cdev *sdev;
static int
foo_load(module_t mod, int cmd, void *arg)
{
    int err = 0;
    switch (cmd) {
    case MOD_LOAD:
        sdev = make_dev(&foo_devsw, 0, UID_ROOT, GID_WHEEL, 0600, "foo");
        break;          /* 成功*/
    case MOD_UNLOAD:
    case MOD_SHUTDOWN:
        destroy_dev(sdev);
        break;          /* 成功*/
    default:
        err = EINVAL;
        break;
    }
    return(err);
}
DEV_MODULE(foo, foo_load, NULL);
```

## 参见

[DECLARE_MODULE(9)](DECLARE_MODULE.9.md), destroy_dev(9), [make_dev(9)](make_dev.9.md), [module(9)](module.9.md)

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写。
