# ieee80211_ddb(9)

`ieee80211_ddb` — 802.11 ddb 支持

## 名称

`ieee80211_ddb`

## 概要

> options DDB

> show vap [addr]
> show all vaps
> show com [addr]
> show sta [addr]
> show statab [addr]
> show mesh [addr]

## 描述

`net80211` 层包括 [ddb(4)](../man4/ddb.4.md) 支持以显示重要数据结构。这尤其重要，因为无线应用程序通常为嵌入式环境构建，在这些环境中，kgdb(1)（`ports/devel/gdb`）等跨机或事后调试设施不可行。

最常用的命令是

```sh
show all vaps/a
```

它转储系统中所有 `ieee80211vap`、`ieee80211com` 和 `ieee80211_node` 数据结构的内容。

## 参见

[ddb(4)](../man4/ddb.4.md), [ieee80211(9)](ieee80211.9.md)
