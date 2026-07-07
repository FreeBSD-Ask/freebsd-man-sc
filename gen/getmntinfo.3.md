# getmntinfo(3)

`getmntinfo` — 获取已挂载文件系统的信息

## 名称

`getmntinfo`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/ucred.h>`

`#include <sys/mount.h>`

```c
int
getmntinfo(struct statfs **mntbufp, int mode);
```

## 描述

`getmntinfo` 函数返回一个 `statfs` 结构数组，描述每个当前已挂载的文件系统（参见 [statfs(2)](../sys/statfs.2.md)）。

`getmntinfo` 函数将其 `mode` 参数透明地传递给 [getfsstat(2)](../sys/getfsstat.2.md)。

## 返回值

成功完成时，`getmntinfo` 返回数组中元素数量的计数值。指向数组的指针存储到 `mntbufp` 中。

如果发生错误，返回零，并设置外部变量 `errno` 以指示错误。虽然指针 `mntbufp` 不会被修改，但 `getmntinfo` 先前返回的任何信息都会丢失。

## 错误

`getmntinfo` 函数可能失败，并为库例程 [getfsstat(2)](../sys/getfsstat.2.md) 或 malloc(3) 指定的任何错误设置 errno。

## 参见

[getfsstat(2)](../sys/getfsstat.2.md), [mount(2)](../sys/mount.2.md), [statfs(2)](../sys/statfs.2.md), [mount(8)](../man8/mount.8.md)

## 历史

`getmntinfo` 函数首次出现于 4.4BSD。

## 缺陷

`getmntinfo` 函数将结构数组写入一个内部静态对象，并返回指向该对象的指针。后续对 `getmntinfo` 的调用将修改同一对象。

`getmntinfo` 分配的内存无法由应用程序通过 free(3) 释放。
