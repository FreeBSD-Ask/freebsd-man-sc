# getdiskbyname.3

`getdiskbyname` — 按名称获取通用磁盘描述

## 名称

`getdiskbyname`

## 库

Lb libc

## 概要

`#include <sys/disklabel.h>`

`Ft struct disklabel * Fn getdiskbyname const char *name`

## 描述

`getdiskbyname` 函数接受一个磁盘名称（如 `rm03`），返回一个原型磁盘标签，描述其几何信息及标准磁盘分区表。所有信息均从 [disktab(5)](../man5/disktab.5.md) 文件获取。

## 参见

[disktab(5)](../man5/disktab.5.md), disklabel(8)

## 历史

`getdiskbyname` 函数出现于 4.3BSD。
