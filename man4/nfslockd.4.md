# nfslockd(4)

`nfslockd` — NFS 咨询锁定

## 名称

`nfslockd`

## 概要

`要将本驱动编译进内核，请在你的内核配置文件中加入以下行：`

> options NFSLOCKD

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nfslockd_load="YES"
```

## 描述

`nfslockd` 驱动为 NFSv3 咨询锁定提供内核支持。它与 rpc.lockd(8) 协同工作，后者通常会在启动时加载它（如果尚未加载或编译进内核）。

## 参见

rpc.lockd(8)

## 历史

`nfslockd` 驱动首次出现于 FreeBSD 6.4。

## 作者

`nfslockd` 驱动由 Doug Rabson <dfr@FreeBSD.org> 编写。
