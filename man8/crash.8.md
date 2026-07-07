# crash(8)

`crash` — FreeBSD 系统故障

## 名称

`crash`

## 描述

本节简要介绍系统崩溃以及（非常简要地）如何分析崩溃转储。

当系统主动崩溃时，它会在控制台上打印如下格式的消息：

- `panic: why i gave up the ghost`

如果已启用转储（参见 dumpon(8)），系统会在大容量存储外设上进行转储，然后调用 [reboot(8)](reboot.8.md) 中所述的自动重启过程。除非由于硬件或软件故障导致文件系统状态出现某种意外的不一致，否则系统将恢复多用户操作。

系统有大量内部一致性检查；如果其中一项失败，系统将 panic 并显示一条非常简短的消息，指明是哪一项失败了。在许多情况下，这将是检测到错误的例程名称，或是对不一致性的两个字描述。要完全理解大多数 panic 消息，需要仔细阅读系统源代码。

系统故障最常见的原因是硬件故障，其表现形式多种多样。以下是最可能出现的消息及其原因提示。在所有情况下，都不排除硬件或软件错误以某种意外方式产生该消息的可能性。

- **Mounting from <device> failed with error <err>** 系统无法挂载已配置的根文件系统。可能是根文件系统已损坏，或者系统试图使用错误的设备作为根文件系统。这不是 panic 消息；相反，它后面会跟一个交互式 **mountroot>** 提示符，操作员可以在其中列出检测到的设备和文件系统，并选择要挂载的替代根文件系统。或者，也可以从恢复介质引导系统来修复此情况。系统安装介质提供了适用于此任务的实时环境。

- **init: not found** 这不是 panic 消息，因为重启很可能徒劳无功。在引导过程的后期，系统无法找到并执行初始化进程 [init(8)](init.8.md)。根文件系统不正确或已损坏，或者 **/sbin/init** 的模式或类型禁止执行，或者完全缺失。

- **ffs_realloccg: bad optim**
- **ffs_valloc: dup alloc**
- **ffs_alloccgblk: cyl groups corrupted**
- **ffs_alloccg: map corrupted**
- **blkfree: freeing free block**
- **blkfree: freeing free frag**
- **ifree: freeing free inode**

这些 panic 消息是检测到文件系统不一致时可能产生的消息之一。问题通常源于崩溃后未能修复受损的文件系统、硬件故障或其他正常情况下不应发生的状况。文件系统检查通常可以更正此问题。

- **init died (signal #, exit #)** 系统初始化进程已以指定的信号号和退出码退出。这是个坏消息，因为之后没有新用户能够登录。重启是唯一的修复方法，因此系统会立即执行。

以上就是你可能看到的 panic 类型列表。

如果系统已配置为进行崩溃转储（参见 dumpon(8)），则当它崩溃时，会（或至少尝试）将内存映像写入转储设备的后端，通常与主交换区相同。系统重启后，savecore(8) 程序会运行，并将此核心映像和当前系统的副本保存到指定目录中以供日后查阅。详情参见 savecore(8)。

要分析转储，应首先在系统加载镜像和核心转储上运行 kgdb(1)（`ports/devel/gdb`）。如果核心映像是 panic 的结果，则会打印 panic 消息。更多细节请参阅 FreeBSD Developers' Handbook（<https://www.freebsd.org/doc/en/books/developers-handbook/>）中关于内核调试的章节。

## 参见

kgdb(1)（`ports/devel/gdb`），[dumpon(8)](dumpon.8.md)，[reboot(8)](reboot.8.md)，savecore(8)

## 历史

`crash` 手册页首次出现于 FreeBSD 2.2。
