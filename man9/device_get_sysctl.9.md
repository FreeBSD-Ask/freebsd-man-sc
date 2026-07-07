# device_get_sysctl(9)

`device_get_sysctl_ctx` — 操作驱动程序特定 sysctl 节点的 sysctl oid 树

## 名称

`device_get_sysctl_ctx`, `device_get_sysctl_tree`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

struct sysctl_ctx_list *
device_get_sysctl_ctx(device_t dev);

struct sysctl_oid *
device_get_sysctl_tree(device_t dev);
```

## 描述

newbus 系统会自动为系统中的每个设备添加一个 sysctl 节点。可以使用 `device_get_sysctl_tree` 函数访问此节点。可以使用 `device_get_sysctl_ctx` 函数获取该节点的上下文。

## 参见

[device(9)](device.9.md)

## 作者

本手册页由 Warner Losh 编写。
