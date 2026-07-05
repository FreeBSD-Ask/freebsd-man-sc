# orm.4

`orm` — ISA I/O 空间选项 ROM 驱动

## 名称

`orm`

## 概要

`orm 在所有具有 ISA 总线的系统上自动包含。`

## 描述

此驱动在引导时扫描 ISA I/O 内存空间以查找选项 ROM 并占用它们。因此，其他驱动无法使用位于选项 ROM 之上的 ISA I/O 内存。

## 作者

本手册页由 Nikolai Saoukh <nms@otdel-1.org> 编写。

## 缺陷

由于资源管理器的实现方式，其他驱动无法附加到选项 ROM 地址范围。
