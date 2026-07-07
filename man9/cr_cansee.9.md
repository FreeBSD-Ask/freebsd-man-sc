# cr_cansee(9)

`cr_cansee` — 根据用户凭据判断对象的可见性

## 名称

`cr_cansee`

## 概要

```c
#include <sys/proc.h>

int
cr_cansee(struct ucred *u1, struct ucred *u2);
```

## 描述

此函数判断持有凭据 `u1` 的主体能否看到与凭据 `u2` 关联的主体或对象。

特定类型的主体可能需要服从额外或不同的限制。例如，对于进程，参见 [p_cansee(9)](p_cansee.9.md)，该函数会调用此函数。

实现依赖于 [cr_bsd_visible(9)](cr_bsd_visible.9.md)，因此其手册页中引用的 [sysctl(8)](../man8/sysctl.8.md) 变量会影响结果。

## 返回值

若持有凭据 `u1` 的主体可以“看到”持有凭据 `u2` 的主体或对象，此函数返回 0；否则返回 `ESRCH`。

## 错误

[`ESRCH`] 持有凭据 `u1` 的主体已被监禁（jailed），且持有凭据 `u2` 的主体或对象不属于同一 jail 或其子 jail，由 [prison_check(9)](prison_check.9.md) 判定。

[`ESRCH`] MAC 子系统拒绝了可见性。

[`ESRCH`] [cr_bsd_visible(9)](cr_bsd_visible.9.md) 根据当前生效的 BSD 安全策略拒绝了可见性。

## 参见

[cr_bsd_visible(9)](cr_bsd_visible.9.md), [mac(9)](mac.9.md), [p_cansee(9)](p_cansee.9.md), [prison_check(9)](prison_check.9.md)
