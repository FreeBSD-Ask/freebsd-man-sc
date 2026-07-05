# lindebugfs.4

`lindebugfs` — 用于调试的 Linux 文件系统

## 名称

`lindebugfs`

## 概要

```sh
lindebugfs		/sys/kernel/debug	lindebugfs	rw 0 0
```

## 描述

调试文件系统，或 debugfs，通过在内核和用户空间之间提供简单的数据传输 API，使进程调试更容易。Debugfs 不是通用文件系统，不应用作存储介质。相反，开发人员可在其代码中实现 debugfs 接口，以在运行时生成有关其程序的调试信息。FreeBSD 的 `lindebugfs` 使用 [pseudofs(9)](../man9/pseudofs.9.md) 文件系统构建工具包，以 Linux 的 debugfs 为模型构建。`lindebugfs` API 旨在与利用 FreeBSD LinuxKPI 兼容层的程序一起使用。

挂载后，`lindebugfs` 将从调用 `debugfs_create_file()` 的任何运行进程填充伪文件。由于 `debugfs_create_file()` 是一个伪文件系统，文件内容将根据程序提供的文件操作动态生成。当前的 `debugfs_create_file()` 实现正式支持 seq_file 和 simple_attr_file 虚拟文件格式。

## 实例

加载 `debugfs_create_file()` 内核模块：

```sh
kldload lindebugfs
```

将 `debugfs_create_file()` 文件系统挂载到 **/sys/kernel/debug**：

```sh
mount -t lindebugfs lindebugfs /sys/kernel/debug
```

## 参见

mount(1), [linprocfs(4)](linprocfs.4.md), [linsysfs(4)](linsysfs.4.md), [linux(4)](linux.4.md), pseudofs(9)

## 历史

`debugfs_create_file()` 文件系统最早出现于 FreeBSD 12.1。

## 作者

`debugfs_create_file()` 的初始实现由 Matthew Macy 创建。本手册页由 Jake Freeland 编写。
