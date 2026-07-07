# ktrace(1)

`ktrace` — 启用内核进程跟踪

## 名称

`ktrace`

## 概要

`ktrace [-aCcdi] [-f trfile] [-g pgrp | -p pid] [-t trstr]`

`ktrace [-adi] [-f trfile] [-t trstr] command`

## 描述

`ktrace` 实用程序为指定进程启用内核跟踪日志记录。内核跟踪数据记录到文件 `ktrace.out` 中。被跟踪的内核操作包括系统调用（参见 intro(2)）、文件系统路径查找（[namei(9)](../man9/namei.9.md)）、信号处理（sigaction(2)）和 I/O。

一旦在进程上启用了跟踪，跟踪数据将被记录直到进程退出或跟踪点被清除。被跟踪的进程可能快速生成大量日志数据；强烈建议用户在尝试跟踪进程之前先记住如何禁用跟踪。以下命令足以禁用所有用户拥有进程的跟踪，如果由 root 执行，则禁用所有进程的跟踪：

```sh
$ ktrace -C
```

跟踪文件不是人类可读的；使用 [kdump(1)](kdump.1.md) 解码它。

该实用程序只能在内核配置文件中包含 "KTRACE" 选项的内核上使用。

选项如下：

**`-a`** 追加到跟踪文件而不是重新创建它。

**`-C`** 禁用所有用户拥有进程的跟踪，如果由 root 执行，则禁用系统中所有进程的跟踪。

**`-c`** 清除与给定文件或进程关联的指定跟踪点。

**`-d`** 后代；对指定进程的所有当前子进程执行操作。另参见 `-i` 选项。

**`-f`** `trfile` 将跟踪记录记录到 `trfile` 而不是 `ktrace.out`。

**`-g`** `pgid` 启用（禁用）进程组中所有进程的跟踪（只允许一个 `-g` 标志）。

**`-i`** 继承；将跟踪标志传递给指定进程的所有未来子进程。另参见 `-d` 选项。

**`-p`** `pid` 启用（禁用）指定进程 ID 的跟踪（只允许一个 `-p` 标志）。

**`-t`** `trstr` 指定要启用或禁用的跟踪点列表，每个字母一个。如果未指定显式列表，则使用默认的跟踪点集合。支持以下跟踪点：

**`c`** 跟踪系统调用

**`f`** 跟踪缺页

**`i`** 跟踪 I/O

**`n`** 跟踪 [namei(9)](../man9/namei.9.md) 转换

**`p`** 跟踪能力检查失败

**`s`** 跟踪信号处理

**`t`** 跟踪各种结构及结构数组

**`u`** 由 utrace(2) 生成的用户态跟踪

**`w`** 上下文切换

**`y`** 跟踪 sysctl(3) 请求

**`a`** 跟踪 execve(2) 参数

**`e`** 跟踪 execve(2) 环境变量

**`x`** 跟踪来自内核的 exterr(2) 扩展错误报告

**`+`** 跟踪默认的跟踪点集合 - `a, c, e, i, n, s, t, u, x, y`

**`command`** 使用指定的跟踪标志执行 `command`。

`-p`、`-g` 和 `command` 选项互斥。

## 能力违规跟踪

当指定 `p` 跟踪点时，`ktrace` 将记录被跟踪进程进行的 [capsicum(4)](../man4/capsicum.4.md) 能力模式违规。无论进程是否实际进入能力模式，违规都将被记录。

对于有兴趣对程序进行 Capsicum 化的开发者，`c, n, p` 跟踪点可以帮助快速识别触发违规的任何系统调用和路径查找。

## 实例

运行 "make"，然后跟踪它及任何子进程：

```sh
$ ktrace -i make
```

跟踪进程 ID 34 的所有内核操作：

```sh
$ ktrace -p 34
```

跟踪进程组 15 中进程的所有内核操作，并将跟踪标志传递给所有当前和未来的子进程：

```sh
$ ktrace -idg 15
```

禁用进程 65 的所有跟踪：

```sh
$ ktrace -cp 65
```

禁用进程 70 及所有当前子进程的信号跟踪：

```sh
$ ktrace -t s -cdp 70
```

启用进程 67 的 I/O 跟踪：

```sh
$ ktrace -ti -p 67
```

禁用到文件 "tracedata" 的所有跟踪：

```sh
$ ktrace -c -f tracedata
```

禁用所有用户拥有进程的跟踪：

```sh
$ ktrace -C
```

## 参见

[dtrace(1)](dtrace.1.md), [kdump(1)](kdump.1.md), [truss(1)](truss.1.md), [intro(2)](../sys/intro.2.md), [ktrace(2)](../sys/ktrace.2.md), [sigaction(2)](../sys/sigaction.2.md), [utrace(2)](../sys/utrace.2.md), [capsicum(4)](../man4/capsicum.4.md), [namei(9)](../man9/namei.9.md)

## 历史

`ktrace` 命令首次出现于 4.4BSD。

## 缺陷

仅在 `trfile` 是常规文件时有效。
