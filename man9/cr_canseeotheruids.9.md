# cr_canseeotheruids(9)

`cr_canseeotheruids` — 判断主体能否看到具有不同用户 ID 的实体

## 名称

`cr_canseeotheruids`

## 概要

```c
int
cr_canseeotheruids(struct ucred *u1, struct ucred *u2);
```

## 描述

> **注意**：此函数为内部函数。其功能已集成到 [cr_bsd_visible(9)](cr_bsd_visible.9.md) 中，应改用后者。

此函数检查持有凭据 `u1` 的主体是否被某项策略禁止查看持有凭据 `u2` 的主体或对象，该策略要求两份凭据具有相同的真实用户 ID。

当且仅当 [sysctl(8)](../man8/sysctl.8.md) 变量 `security.bsd.see_other_uids` 设置为 0 时，此策略生效。

按惯例，超级用户（有效用户 ID 为 0）不受此策略限制，前提是 [sysctl(8)](../man8/sysctl.8.md) 变量 `security.bsd.suser_enabled` 为非零值，且没有活动的 MAC 策略明确拒绝此豁免（参见 [priv_check_cred(9)](priv.9.md)）。

## 返回值

若策略被禁用、两份凭据具有相同的真实用户 ID，或 `u1` 拥有可豁免此策略的特权，`cr_canseeotheruids` 函数返回 0；否则返回 `ESRCH`。

## 参见

[cr_bsd_visible(9)](cr_bsd_visible.9.md), [priv_check_cred(9)](priv.9.md)
