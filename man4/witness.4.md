# witness.4

`witness` — 锁验证设施

## 名称

`witness`

## 概要

`options WITNESS`

`options WITNESS_COUNT`

`options WITNESS_KDB`

`options WITNESS_NO_VNODE`

`options WITNESS_SKIPSPIN`

## 描述

`witness` 模块跟踪每个线程获取和释放的锁。它还跟踪锁相对于彼此的获取顺序。每次获取锁时，`witness` 使用这两个列表来验证锁没有以错误的顺序获取。如果检测到锁顺序违规，则向内核控制台或日志输出详细说明相关锁和位置的消息。还可配置 witness 在发生顺序违规时进入内核调试器。

`witness` 代码还检查各种其他条件，例如验证不会在非递归锁上递归，或不会尝试升级另一个线程持有的共享锁。如果这些检查中的任何一个失败，内核将 panic。

`WITNESS_COUNT` 内核选项控制内核中跟踪的 `witness` 条目最大数量。最大条目数可通过 `debug.witness.witness_count` sysctl 查询。也可通过 [loader(8)](../man8/loader.8.md) 的 `debug.witness.witness_count` 环境变量设置。

`WITNESS_NO_VNODE` 内核选项告知 `witness` 忽略 [vnode(9)](../man9/vnode.9.md) 对象之间的锁定问题。

控制检测到锁顺序违规时是否进入内核调试器的标志可通过多种方式设置。默认情况下，该标志处于关闭状态，但如果指定了 `WITNESS_KDB` 内核选项，则该标志默认为打开。也可通过 [loader(8)](../man8/loader.8.md) 的 `debug.witness.kdb` 环境变量设置，或在内核引导后通过 `debug.witness.kdb` sysctl 设置。如果该标志设置为零，则不会进入调试器。如果该标志非零，则将进入调试器。

`witness` 代码还可配置为跳过自旋互斥锁的所有检查。默认情况下，此标志处于关闭状态，但可通过指定 `WITNESS_SKIPSPIN` 内核选项打开。也可通过 [loader(8)](../man8/loader.8.md) 环境变量 `debug.witness.skipspin` 设置。如果该变量设置为非零值，则跳过自旋互斥锁。内核引导后，可检查此标志的状态，但不能通过只读 sysctl `debug.witness.skipspin` 设置。

sysctl `debug.witness.watch` 指定 witness 在系统中的参与级别。值为 1 指定启用 witness。值为 0 指定禁用 witness，但可再次启用。这将在系统中保持少量开销。值为 -1 指定永久禁用 witness，无法再次启用。sysctl `debug.witness.watch` 可通过 [loader(8)](../man8/loader.8.md) 设置。

sysctl `debug.witness.trace` 控制 `witness` 在检测到锁违规时是否打印堆栈跟踪。值为 0 禁用堆栈打印。值为 1 指定 `witness` 在发生锁层次结构违规或在进入睡眠或获取可睡眠锁时持有不可睡眠锁时打印堆栈跟踪。值为 2 指定 `witness` 尝试显示所有观察到的、对已建立的锁顺序有贡献的锁链，以及这些锁首次获取时的堆栈跟踪。sysctl `debug.witness.trace` 可通过 [loader(8)](../man8/loader.8.md) 设置。

sysctl `debug.witness.output_channel` 指定用于显示 `witness` 发出的警告的输出通道。可能的值为 `console`（表示警告将打印到系统控制台）、`log`（表示警告将通过 log(9) 记录）和 `none`。此 sysctl 可通过 [loader(8)](../man8/loader.8.md) 设置。

sysctl `debug.witness.badstacks` 显示 `witness` 模块当前锁层次结构视图中缓存的已检测锁顺序违规列表。（这意味着它可能不会显示已销毁锁的信息。）它显示的详细程度与运行时检查生成的消息类似。但是，它总是尝试显示所有观察到的、对已建立的锁顺序有贡献的锁链。（换句话说，它的行为类似于 `debug.witness.trace` 设置为 2。）它使用 '**' 标记因违反 `witness` 代码先前观察到的层次结构而未添加到层次结构中的锁顺序。

如果 `witness` 和 [ddb(4)](ddb.4.md) 都编译到内核中，`witness` 代码还提供了一些额外的 [ddb(4)](ddb.4.md) 命令：

**`show locks`** [thread] 将线程持有的锁列表连同该线程最后获取每个锁的文件名和行号输出到内核控制台。可选的 `thread` 参数可以是 TID、PID 或指向线程结构的指针。如果未指定 `thread`，则显示当前线程持有的锁。

**`show all locks`** 将系统中所有线程持有的锁列表输出到内核控制台。

**`show witness`** 将当前顺序列表转储到内核控制台。代码首先显示所有可睡眠锁的锁顺序树。然后显示所有自旋锁的锁顺序树。最后，显示尚未获取的锁列表。

**`show badstacks`** 显示所有 WITNESS 锁顺序违规的列表。此列表与 `debug.witness.badstacks` sysctl 生成的列表相同。

## 参见

[ddb(4)](ddb.4.md), [loader(8)](../man8/loader.8.md), [sysctl(8)](../man8/sysctl.8.md), [mutex(9)](../man9/mutex.9.md)

## 历史

`witness` 代码最早出现在 BSD/OS 中，并从那里导入到 FreeBSD 5.0 中。
