# kbdmux.4

`kbdmux` — 键盘多路复用器

## 名称

`kbdmux`

## 概要

`device kbdmux`

`在 /boot/device.hints 中： hint.kbdmux.0.disabled="1"`

## 描述

`kbdmux` 键盘驱动提供对基本键盘多路复用的支持。它围绕“超级键盘”的概念构建。`kbdmux` 驱动作为主键盘，使用来自挂接到它的所有从键盘的输入。

可以使用 kbdcontrol(1) 工具将键盘挂接到 `kbdmux` 键盘驱动或从中卸下。

## 参见

kbdcontrol(1), [atkbd(4)](atkbd.4.md), syscons(4), ukbd(4), vt(4)

## 历史

`kbdmux` 模块实现于 FreeBSD 6.0。

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>

## 注意事项

`kbdmux` 键盘驱动将所有从键盘切换到 `K_RAW` 模式。因此，挂接到 `kbdmux` 键盘的所有从键盘共享相同的状态。`kbdmux` 键盘在逻辑上等价于一个具有大量重复按键的键盘。
