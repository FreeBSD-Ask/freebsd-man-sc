# getusershell(3)

`getusershell` — 获取有效的用户 shell

## 名称

`getusershell`, `setusershell`, `endusershell`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
char *
getusershell(void);

void
setusershell(void);

void
endusershell(void);
```

## 描述

`getusershell` 函数返回一个指针，指向由系统管理员在 shells 数据库中定义的有效用户 shell，如 [shells(5)](../man5/shells.5.md) 所述。如果 shells 数据库不可用，`getusershell` 的行为就像列出了 **/bin/sh** 和 **/bin/csh** 一样。

`getusershell` 函数读取下一行（如有必要则打开文件）；`setusershell` 回绕文件；`endusershell` 关闭文件。

## 文件

**/etc/shells**

## 诊断

`getusershell` 例程在 `EOF` 时返回空指针（0）。

## 参见

[nsswitch.conf(5)](../man5/nsswitch.conf.5.md), [shells(5)](../man5/shells.5.md)

## 历史

`getusershell` 函数出现于 4.3BSD。

## 缺陷

`getusershell` 函数将其结果留在内部静态对象中，并返回指向该对象的指针。后续对 `getusershell` 的调用将修改同一个对象。
