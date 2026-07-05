# ratecheck.9

`ratecheck` — 事件速率限制

## 名称

`ratecheck`, `ppsratecheck`

## 概要

```c
#include <sys/time.h>
```

```c
int
ratecheck(struct timeval *lasttime, const struct timeval *mininterval)

int
ppsratecheck(struct timeval *lasttime, int *curpps, int maxpps)
```

## 描述

`ratecheck` 和 `ppsratecheck` 函数便于对任意事件进行速率限制。前者强制事件之间的最小间隔，而后者强制每秒最大事件数。

`ratecheck` 函数将当前时间与 `lasttime` 所指向的值进行比较。如果差值等于或大于 `mininterval`，它返回非零值并将 `lasttime` 更新为当前时间。否则，它返回零。

`ppsratecheck` 函数首先将当前时间与 `lasttime` 进行比较。如果至少已过整整一秒，`curpps` 参数所指向的值将重置为 1，`lasttime` 更新为当前时间。否则，`curpps` 递增，`lasttime` 保持不变。在任一情况下，当且仅当更新后的 `curpps` 小于或等于 `maxpps` 或 `maxpps` 为负时，`ppsratecheck` 返回非零值。

## 参见

[counter(9)](counter.9.md)

## 历史

`ratecheck` 和 `ppsratecheck` 函数首次出现在 FreeBSD 5.1 中。
