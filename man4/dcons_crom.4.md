# dcons_crom.4

`dcons_crom` — 配置 ROM 桩

## 名称

`dcons_crom` [dcons(4)](dcons.4.md)

## 概要

`device dcons_crom device dcons device firewire`

## 描述

`dcons_crom` 通过 [firewire(4)](firewire.4.md) 的配置 ROM 公开 [dcons(4)](dcons.4.md) 的缓冲区地址。该地址预期由 dconschat(8) 使用。

## 参见

[dcons(4)](dcons.4.md), [firewire(4)](firewire.4.md), [fwohci(4)](fwohci.4.md), dconschat(8), fwcontrol(8)

## 作者

Hidetoshi Shimokawa <simokawa@FreeBSD.org>

## 缺陷

如果在系统引导后手动加载 `dcons_crom.ko`，可能需要使用“`fwcontrol` `-r`”发起总线复位以更新配置 ROM。
