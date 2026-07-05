# procfs.4

`procfs` — 进程文件系统

## 名称

`procfs`

## 概要

```sh
proc		/proc	procfs	rw 0 0
```

## 描述

**重要提示：** 此功能已弃用。建议使用 libprocstat(3) 和 kvm(3) 作为替代。

进程文件系统，即 `procfs`，在文件系统中实现了对系统进程表的视图。它通常挂载在 **`/proc`**。

与早期 FreeBSD 1.1 的 `procfs` 实现不同，`procfs` 提供了两层视图的进程空间。在最顶层，进程按照其十进制进程 ID（不带前导零）命名。此外还有一个名为 `curproc` 的特殊节点，它始终指向发起查询请求的进程。

每个节点都是一个目录，其中包含以下条目：

`#include <machine/reg.h>`

`#include <machine/reg.h>`

`#include <vm/vm_object.h>`

**COW** 写时复制区域。
**NCOW** 非写时复制区域。

**NC** 该区域需要复制。
**NNC** 该区域不需要复制。

**dead** 与已失效 VM 对象关联的区域。
**device** 由设备内存支撑的区域。
**none** 无任何支撑的区域。
**phys** 由物理内存支撑的区域。
**swap** 由交换空间支撑的区域。
**unknown** 类型未知的区域。
**vnode** 由文件支撑的区域。

**CH** 该区域正被计费给“charged-uid”字段中指定的用户。
**NCH** 该区域未被计费给任何用户。

**start-address** 该区域的起始地址（含）。
**end-address** 该区域的结束地址（不含）。
**resident** 常驻页数。
**private-resident** 进程私有的常驻页数。
**obj** 描述该内存区域的 `struct vm_object` 内核数据结构的虚拟地址。
**access** 由“r”、“w”和“x”三个字符组成的字符串，分别表示读、写和执行权限。缺少某项权限以 “-” 表示。
**ref_count** 对该区域的引用数。
**shadow_count** 该区域作为其影子的 VM 对象数量。
**flags** 对象的标志，参见以下位置中名为 **OBJ_*** 的标志：
**copy-on-write** 该区域是否为写时复制。取值为：
**needs-copy** 该区域是否需要复制。取值为：
**type** 区域的类型。取值为：
**fullpath** 支撑该内存区域的文件路径，若无此文件则为“-”。
**cred** 取值为：
**charged-uid** 被计费用户的 UID，若无用户被计费则为 -1。

`#include <machine/reg.h>`

- 命令名
- 进程 ID
- 父进程 ID
- 进程组 ID
- 会话 ID
- 控制终端的设备名，若无控制终端则为减号（“-”）。
- 进程标志列表：若有控制终端则为 `ctty`；若进程是会话首领则为 `sldr`；若两者均未设置则为 `noflags`。
- 进程启动时间，以秒和微秒为单位，逗号分隔。
- 用户时间，以秒和微秒为单位，逗号分隔。
- 系统时间，以秒和微秒为单位，逗号分隔。
- 等待通道消息
- 进程的有效 UID
- 进程的实际 UID
- 组列表，以有效 GID 开头，逗号分隔
- 进程所运行于的 Jail 的主机名，若进程未运行于 Jail 中则为 `-`。

**`dbregs`** 由 `struct dbregs` 定义的调试寄存器。`dbregs` 目前仅在 i386 架构上实现。

**`etype`** 由 `file` 条目所引用的可执行文件的类型。

**`file`** 指向进程代码段读取来源文件的符号链接。可用于访问进程的符号表，或启动该进程的另一个副本。若找不到该文件，链接目标为 `unknown`。

**`fpregs`** 由 `struct fpregs` 定义的浮点寄存器。`fpregs` 仅在具有独立通用寄存器集和浮点寄存器集的机器上实现。

**`map`** 一组描述进程内存区域的行，每行包含以下字段：

**`mem`** 进程完整的虚拟内存映像。仅可访问进程中存在的地址。对此文件的读取和写入会修改进程。对代码段的写入在进程内保持私有。

**`note`** 用于向进程发送信号。未实现。

**`notepg`** 用于向进程组发送信号。未实现。

**`osrel`** 允许读取和写入分配给进程的内核 osrel 值。它影响根据该值启停的兼容性垫片。进程的初始值从所执行的 ELF 镜像中的 ABI note 标签读取，若二进制格式不支持该标签或未找到则为零。

**`regs`** 允许读写访问进程的寄存器集。此文件包含一个二进制数据结构 `struct regs`，定义于 `regs`。该文件只能在进程停止时写入。

**`rlimit`** 这是一个只读文件，包含进程当前和最大限制。每行格式为 `rlimit current max`，-1 表示无穷大。

**`status`** 进程状态。此文件为只读，返回包含多个空格分隔字段的单行，如下所示：

每个节点归属于进程的用户，并属于该用户的主组。

## 文件

**`/proc`** `procfs` 的常规挂载点。
**`/proc/pid`** 包含进程 `pid` 进程信息的目录。
**`/proc/curproc`** 包含当前进程信息的目录
**`/proc/self`** 包含当前进程信息的目录
**`/proc/curproc/cmdline`** 进程可执行文件名
**`/proc/curproc/etype`** 可执行文件类型
**`/proc/curproc/exe`** 可执行镜像
**`/proc/curproc/file`** 可执行镜像
**`/proc/curproc/fpregs`** 进程浮点寄存器集
**`/proc/curproc/map`** 进程的虚拟内存映射
**`/proc/curproc/mem`** 进程完整的虚拟地址空间
**`/proc/curproc/note`** 用于向进程发送信号
**`/proc/curproc/notepg`** 用于向进程组发送信号
**`/proc/curproc/osrel`** 进程的 osrel 值
**`/proc/curproc/regs`** 进程寄存器集
**`/proc/curproc/rlimit`** 进程的当前和最大 rlimit
**`/proc/curproc/status`** 进程的当前状态

## 实例

将 `procfs` 文件系统挂载到 **`/proc`**：

```sh
mount -t procfs proc /proc
```

## 参见

procstat(1), mount(2), sigaction(2), unmount(2), kvm(3), libprocstat(3), [pseudofs(9)](../man9/pseudofs.9.md)

## 作者

本手册页由 Garrett Wollman 编写，基于 Jan-Simon Pendry 提供的描述，之后由 Mike Pritchard 进行了改写。
