# dev_clone.9

`dev_clone` — devfs 中基于名称的设备克隆事件处理器

## 名称

`dev_clone`, `drain_dev_clone_events`

## 概要

```c
#include <sys/param.h>
#include <sys/conf.h>

void
clone_handler(void *arg, struct ucred *cr, char *name, int namelen,
    struct cdev **dev)
```

```c
EVENTHANDLER_REGISTER(dev_clone, clone_handler, arg, priority);
```

```c
void
drain_dev_clone_events(void)
```

## 描述

设备驱动程序可以注册一个监听器，每当在 [devfs(4)](../man4/devfs.4.md) 挂载点上进行的名称查找未能找到 vnode 时，该监听器就会收到通知。监听器应为 `dev_clone` 事件注册。当被调用时，它接收在处理程序注册时指定的第一个参数 `arg`、适当的凭据 `cr`，以及我们要查找的长度为 `namelen` 的名称 `name`。如果处理程序认为该名称合适并希望创建与此名称关联的设备，应在 `dev` 参数中将其返回给 devfs。

`drain_dev_clone_events` 函数是一个屏障。保证在 `drain_dev_clone_events` 调用之前开始的所有 `dev_clone` 事件处理程序调用，都在它返回控制权之前完成。

## 参见

[devfs(4)](../man4/devfs.4.md), [namei(9)](namei.9.md)
