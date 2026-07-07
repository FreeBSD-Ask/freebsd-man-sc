# pget(9)

`pget` — 按编号定位进程

## 名称

`pget`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/proc.h>
```

```c
int
pget(pid_t pid, int flags, struct proc **pp)
```

## 描述

此函数接受 `pid` 作为参数，它可以是进程 ID 或线程 ID，并在 `*pp` 中填写指向 `proc` 结构的指针。在后一种情况下，将查找拥有指定线程的进程。该操作通过调用 [pfind(9)](pfind.9.md) 函数执行。找到的进程以锁定状态返回。对于 `PGET_HOLD` 情况，以未锁定（但被持有）状态返回。`pget` 函数可以根据 `flags` 参数执行额外操作。

`flags` 参数是以下某些子集的逻辑或：

**`PGET_HOLD`** 如果设置，找到的进程将被持有并解锁。

**`PGET_CANSEE`** 如果设置，将检查找到的进程的可见性。参见 [p_cansee(9)](p_cansee.9.md)。

**`PGET_CANDEBUG`** 如果设置，将检查找到的进程的可调试性。参见 [p_candebug(9)](p_candebug.9.md)。

**`PGET_ISCURRENT`** 如果设置，将检查找到的进程是否匹配当前进程上下文。

**`PGET_NOTWEXIT`** 如果设置，将检查找到的进程是否未设置进程标志 `P_WEXIT`。

**`PGET_NOTINEXEC`** 如果设置，将检查找到的进程是否未设置进程标志 `P_INEXEC`。

**`PGET_NOTID`** 如果设置，对于大于 `PID_MAX` 的值，不将 `pid` 假定为线程 ID。

**`PGET_WANTREAD`** 如果设置，将检查找到的进程以确保调用者可以对其结构进行读取访问。这是 (`PGET_HOLD | PGET_CANDEBUG | PGET_NOTWEXIT`) 的简写。

## 返回值

如果以指定方式找到进程，则返回零，否则返回适当的错误代码。

## 参见

[p_candebug(9)](p_candebug.9.md), [p_cansee(9)](p_cansee.9.md), [pfind(9)](pfind.9.md)
