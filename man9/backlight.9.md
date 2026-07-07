# backlight(9)

`backlight` — 背光方法

## 名称

`backlight`, `backlight_register`, `backlight_destroy`, `BACKLIGHT_GET_STATUS`, `BACKLIGHT_SET_STATUS`

## 概要

```c
device backlight
```

```c
#include <backlight_if.h>
#include <sys/sys/backlight.h>
```

```c
int
BACKLIGHT_GET_STATUS(device_t bus, struct backlight_props *props)

int
BACKLIGHT_SET_STATUS(device_t bus, struct backlight_props *props)

struct cdev *
backlight_register(const char *name, device_t dev)

int
backlight_destroy(struct cdev *cdev)
```

## 描述

背光驱动程序提供了处理面板背光的通用方法。

背光系统的驱动程序使用 `backlight_register` 函数全局注册自身。它们必须定义两个方法：`BACKLIGHT_GET_STATUS` 用于查询当前亮度级别，`BACKLIGHT_SET_STATUS` 用于更新亮度级别。

## 接口

**`BACKLIGHT_GET_STATUS`**(device_t bus, struct backlight_props *props) 驱动程序填充当前亮度级别和可选的支持级别。

**`BACKLIGHT_SET_STATUS`**(device_t bus, struct backlight_props *props) 驱动程序根据 props 结构的 brightness 成员更新背光级别。

## 文件

**`/dev/backlight/*`**

## 参见

[backlight(8)](../man8/backlight.8.md)

## 历史

`backlight` 接口首次出现于 FreeBSD 13.0。`backlight` 驱动程序和手册页由 Emmanuel Vadot <manu@FreeBSD.org> 编写。
