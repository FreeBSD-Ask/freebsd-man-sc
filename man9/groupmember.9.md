# groupmember.9

`groupmember` — 检查凭据是否要求某些组成员身份

## 名称

`groupmember`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/ucred.h>
```

```c
bool
groupmember(gid_t gid, const struct ucred *cred)
bool
realgroupmember(gid_t gid, const struct ucred *cred)
```

## 描述

`groupmember` 函数检查凭据 `cred` 是否指示关联的主体或对象是由组 ID `gid` 指定的组的成员。

`cred` 中考虑的组是有效组和补充组。不考虑实际组。

`realgroupmember` 函数工作方式相同，区别在于它考虑的是实际组和补充组，而不是有效组。

## 返回值

`groupmember` 和 `realgroupmember` 函数在给定凭据指示为组 `gid` 的成员时返回 `true`，否则返回 `false`。

## 参见

`getgroups(2)`, `setgroups(2)`

## 作者

本手册页最初由 Chad David <davidc@acns.ab.ca> 编写，并由 Olivier Certner <olce.freebsd@certner.fr> 修订。
