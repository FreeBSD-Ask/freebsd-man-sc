# device\_get\_name.9

`device_get_name` — 访问设备的设备类或实例名称

## 名称

`device_get_name`, `device_get_nameunit`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

const char *
device_get_name(device_t dev);

const char *
device_get_nameunit(device_t dev);
```

## 描述

`device_get_name` 函数返回设备的设备类名称。

`device_get_nameunit` 函数返回设备的实例名称。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Warner Losh 编写。
