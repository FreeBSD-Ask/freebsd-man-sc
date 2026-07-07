# linprocfs(4)

`linprocfs` — Linux 进程文件系统

## 名称

`linprocfs`

## 概要

```sh
linprocfs		/compat/linux/proc	linprocfs	rw 0 0
```

## 描述

Linux 进程文件系统，或 `linprocfs`，模拟 Linux 进程文件系统的一个子集，某些 Linux 二进制文件的完整运行需要它。

`linprocfs` 提供进程空间的二级视图。在最高级别，进程本身根据其进程 ID（十进制，无前导零）命名。还有一个名为 `self` 的特殊节点，始终引用发出查找请求的进程。

每个进程节点是一个包含多个文件的目录：

**`auxv`** 传递给程序的辅助向量。

**`cmdline`** 用于执行进程的命令行。

**`cwd`** 指向进程当前工作目录的符号链接。

**`environ`** 进程的环境变量和值列表。每个变量和值对由 NULL 字节与下一个分隔。

**`exe`** 对读取进程文本的 vnode 的引用。可用于访问进程的符号表，或启动进程的另一个副本。

**`limits`** 进程的软限制和硬限制及其使用的单位。

**`maps`** 进程的内存映射。

**`mem`** 进程的完整虚拟内存镜像。仅可访问进程中存在的地址。对此文件的读取和写入会修改进程。对文本段的写入对进程保持私有。

**`mountinfo`** 有关挂载点的信息。

**`mounts`** 类似于上面。

**`oom_score_adj`** Out Of Memory killer 的分数调整。

**`root`** 指向此进程根目录的符号链接。

**`stat`** 进程统计信息。包括 user、nice、system、idle、iowait、irq、softirq、steal、guest 和 guest_nice。

**`statm`** 进程大小统计。包括总程序大小、常驻集大小、常驻共享页数（未使用）、文本大小、库大小（未使用）、数据 + 栈和脏页（未使用）。

**`status`** 人类可读形式的进程统计信息。包括进程名称、状态、PID 等。

**`task`** 用于避免特定软件（如 Chromium）中出现问题的虚拟目录。

每个节点由进程的用户拥有，并属于该用户的主组，但 `mem` 节点除外，它属于 `kmem` 组。

## 文件

**`/compat/linux/proc`** `linprocfs` 的正常挂载点。

**`/compat/linux/proc/cmdline`** 包含用于引导系统的内核镜像路径。

**`/compat/linux/proc/cpuinfo`** 人类可读形式的 CPU 供应商和型号信息。

**`/compat/linux/proc/devices`** 字符和块设备列表。后者在 FreeBSD 上通常为空。

**`/compat/linux/proc/filesystems`** 受支持的文件系统列表。对于伪文件系统，第一列包含 *nodev.*

**`/compat/linux/proc/meminfo`** 人类可读形式的系统内存信息。

**`/compat/linux/proc/modules`** 已加载的内核模块。目前为空。

**`/compat/linux/proc/mounts`** 设备对应的挂载点。

**`/compat/linux/proc/mtab`** 同上。

**`/compat/linux/proc/partitions`** 分区信息，包括主次设备号、块数和名称。其余字段设置为零。

**`/compat/linux/proc/stat`** 系统统计信息。对于每个 CPU，最多包括用户时间、nice 时间、系统时间和空闲时间、iowait（等待 I/O 完成的时间）、服务 irq 和 softirq 的时间、steal、guest 和 guest_nice 时间（表示在虚拟化环境中不同模式花费的时间）。最后几列设置为零。此文件还包含磁盘、上下文切换等的简要统计信息。

**`/compat/linux/proc/swap`** 有关交换设备的信息（如果有）。

**`/compat/linux/proc/uptime`** 自上次引导以来的时间和空闲状态花费的时间。

**`/compat/linux/proc/version`** 模拟的 linux 系统版本。

**`/compat/linux/proc/`** <`pid` >> 包含进程 `pid` 的进程信息的目录。

**`/compat/linux/proc/self`** 指向包含当前进程进程信息的目录的符号链接。

## 实例

要将 `linprocfs` 文件系统挂载到 **/compat/linux/proc**：

```sh
mount -t linprocfs linprocfs /compat/linux/proc
```

## 参见

mount(2), unmount(2), auxv(3), [linux(4)](linux.4.md), procfs(5), pseudofs(9)

## 历史

`linprocfs` 最早出现于 FreeBSD 4.0。

## 作者

`linprocfs` 由 Pierre Beyssac 从 `procfs` 派生。本手册页由 Dag-Erling Smørgrav 编写，基于 Garrett Wollman 的 procfs(5) 手册页。
