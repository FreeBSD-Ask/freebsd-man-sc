# cr_bsd_visible(9)

`cr_bsd_visible` — 根据BSD安全策略判断主体是否可见对应实体

## 名称

`cr_bsd_visible`

## 概要

```c
#include <sys/proc.h>

int
cr_bsd_visible(struct ucred *u1, struct ucred *u2);
```

## 描述

该函数判断持有凭据 `u1` 的主体是否被以下策略及其对应的 [sysctl(8)](../man8/sysctl.8.md) 开关禁止查看与凭据 `u2` 关联的对象或主体：

**`security.bsd.seeotheruids`** 若设置为 0，则当主体与对象或主体不关联相同的真实用户 ID 时，主体无法看到对方。对应的内部函数为 [cr_canseeotheruids(9)](cr_canseeotheruids.9.md)。

**`security.bsd.seeothergids`** 若设置为 0，则当两个主体不属于至少一个公共组时，主体无法看到对方。对应的内部函数为 [cr_canseeothergids(9)](cr_canseeothergids.9.md)。

**`security.bsd.see_jail_proc`** 若设置为 0，则当主体与对象或主体不关联相同的 jail 时，主体无法看到对方。对应的内部函数为 [cr_canseejailproc(9)](cr_canseejailproc.9.md)。

按惯例，超级用户（有效用户 ID 为 0）不受上述任何策略限制，前提是 [sysctl(8)](../man8/sysctl.8.md) 变量 `security.bsd.suser_enabled` 为非零值，且没有活动的 MAC 策略明确拒绝此豁免（参见 [priv_check_cred(9)](priv_check_cred.9.md)）。

此函数旨在作为实现 [cr_cansee(9)](cr_cansee.9.md) 及类似函数的辅助工具。

## 返回值

若在上述活动策略下，持有凭据 `u1` 的主体可以查看持有凭据 `u2` 的主体或对象，此函数返回 0；否则返回 `ESRCH`。

## 错误

[`ESRCH`] 凭据 `u1` 和 `u2` 没有相同的真实用户 ID。

[`ESRCH`] 凭据 `u1` 和 `u2` 不属于任何公共组（由 [realgroupmember(9)](realgroupmember.9.md) 判定）。

[`ESRCH`] 凭据 `u1` 和 `u2` 不在同一 jail 中。

## 参见

[cr_cansee(9)](cr_cansee.9.md), [cr_canseejailproc(9)](cr_canseejailproc.9.md), [cr_canseeothergids(9)](cr_canseeothergids.9.md), [cr_canseeotheruids(9)](cr_canseeotheruids.9.md), [priv_check_cred(9)](priv_check_cred.9.md)

## 作者

该函数及其手册页由 Olivier Certner <olce.freebsd@certner.fr> 编写。
