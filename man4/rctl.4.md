# rctl(4)

`rctl` — 资源限制

## 名称

`rctl`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> options RACCT
> options RCTL

## 描述

`rctl` 子系统提供了一种灵活的资源限制机制，由一组可在运行时通过 rctl(8) 管理工具添加或移除的规则控制。

## 加载器可调参数

可调参数可在 [loader(8)](../man8/loader.8.md) 提示符下或 loader.conf(5) 中设置。

**`kern.racct.enable:`** 1 启用 `rctl`。默认值为 1，除非在内核配置文件中设置了 `options RACCT_DEFAULT_TO_DISABLED`。

## 参见

[rctl.conf(5)](../man5/rctl.conf.5.md), rctl(8)

## 历史

`rctl` 子系统最早出现在 FreeBSD 9.0 中。

## 作者

`rctl` 子系统由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。
