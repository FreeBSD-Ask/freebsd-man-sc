# sem.4

`sem` — POSIX 信号量

## 名称

`sem`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> options P1003_1B_SEMAPHORES

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
sem_load="YES"
```

`要在运行时以模块形式加载此驱动，请以 root 身份执行以下命令：`

> kldload sem

## 描述

`sem` 工具提供标准 C 库（`libc`）使用的系统调用，以实现 POSIX 信号量。此工具为 `sem_init` 和 `sem_wait` 等函数提供支持。它既可以作为内核选项静态包含，也可以作为动态内核模块使用。

## 参见

sem_destroy(3), sem_getvalue(3), sem_init(3), sem_open(3), sem_post(3), sem_wait(3), [config(8)](../man8/config.8.md), [kldload(8)](../man8/kldload.8.md), [kldunload(8)](../man8/kldunload.8.md)

## 历史

`sem` 工具最早出现于 FreeBSD 5.0。
