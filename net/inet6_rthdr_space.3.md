# inet6_rthdr_space(3)

`inet6_rthdr_space` — IPv6 路由头选项操作

## 名称

`inet6_rthdr_space`, `inet6_rthdr_init`, `inet6_rthdr_add`, `inet6_rthdr_lasthop`, `inet6_rthdr_reverse`, `inet6_rthdr_segments`, `inet6_rthdr_getaddr`, `inet6_rthdr_getflags`

## 描述

RFC 2292 IPv6 高级 API 已弃用，推荐使用 [inet6_rth_space(3)](inet6_rth_space.3.md) 中所述的较新 RFC 3542 API。在支持该 API 的平台上（目前仅 FreeBSD），请使用较新的 API 来操作路由头选项。

## 参见

[inet6_rth_space(3)](inet6_rth_space.3.md)
