# device\_set\_desc.9

`device_set_desc` — 访问设备的描述

## 名称

`device_set_desc`, `device_set_descf`, `device_set_desc_copy`, `device_get_desc`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

void
device_set_desc(device_t dev, const char *desc);

void
device_set_descf(device_t dev, const char *fmt, ...);

void
device_set_desc_copy(device_t dev, const char *desc);

const char *
device_get_desc(device_t dev);
```

## 描述

操作设备的详细描述。此描述（若存在）会在自动配置期间 attach 时作为消息的一部分打印。若传入的字符串是临时缓冲区且会被覆盖，使用 `device_set_desc_copy` 变体来设置描述。此情况下系统会复制该字符串，否则将直接使用传入的指针。`device_set_descf` 是 `device_set_desc` 的类 printf 版本。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
