# prison_check(9)

`prison_check` — 根据 jail 限制确定主体是否可以查看实体

## 名称

`prison_check`

## 概要

```c
#include <sys/jail.h>
```

```c
int
prison_check(struct ucred *cred1, struct ucred *cred2)
```

## 描述

此函数根据主体可以查看其自身 jail 或其任何子 jail 中的主体或对象的策略，确定具有凭据 `cred1` 的主体是否被拒绝访问具有凭据 `cred2` 的主体或对象。

## 返回值

如果 `cred2` 不在与 `cred1` 相同的 jail 或其子 jail 中，`prison_check` 函数返回 `ESRCH`。在所有其他情况下，`prison_check` 返回零。

## 参见

[jail(2)](../man2/jail.2.md)
