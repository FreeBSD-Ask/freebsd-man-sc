# amdsmn.4

`amdsmn` — AMD 处理器系统管理网络设备驱动

## 名称

`amdsmn` AMD 处理器系统管理网络

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device amdsmn

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
amdsmn_load="YES"
```

## 描述

`amdsmn` 驱动为 AMD Family 17h 处理器中系统管理网络总线上的资源提供支持。

## 参见

[loader(8)](../man8/loader.8.md)

## 历史

`amdsmn` 驱动首次出现于 FreeBSD 12.0。

## 作者

Conrad Meyer <cem@FreeBSD.org>
