# devtoname(9)

`devtoname` — 将字符设备转换为表示设备名称的字符串

## 名称

`devtoname`

## 概要

```c
#include <sys/param.h>
#include <sys/conf.h>

const char *
devtoname(struct cdev *dev);
```

## 描述

`devtoname` 函数返回指向传入设备名称的指针。该名称是在 `make_dev` 中设置的。

## 历史

`devtoname` 接口最早出现于 FreeBSD 4.0。
