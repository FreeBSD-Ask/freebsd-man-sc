# procdesc.4

`procdesc` — 进程描述符设施

## 名称

`procdesc`

## 描述

`procdesc` 是一种面向文件描述符的进程信号传递与控制接口，它通过 `pdfork(2)` 和 `pdkill(2)` 等新系统调用补充了历史悠久的 UNIX fork(2) 和 kill(2) 原语。`procdesc` 设计用于与 [capsicum(4)](capsicum.4.md) 配合使用，以面向能力的引用取代进程标识符。不过，它也可以独立于 [capsicum(4)](capsicum.4.md) 使用，以替代可能存在竞态条件的 PID。给定一个进程描述符，可以通过 pdgetpid(2) 查询其对应的常规 PID。

## 参见

fork(2), kill(2), kqueue(2), pdfork(2), pdgetpid(2), pdkill(2), wait4(2), [capsicum(4)](capsicum.4.md)

## 历史

`procdesc` 首次出现于 FreeBSD 9.0，由剑桥大学开发。

## 作者

`procdesc` 由剑桥大学的 Robert Watson <rwatson@FreeBSD.org> 和 Jonathan Anderson <jonathan@FreeBSD.org>，以及 Google, Inc. 的 Ben Laurie <benl@FreeBSD.org> 和 Kris Kennaway <kris@FreeBSD.org> 共同开发。
