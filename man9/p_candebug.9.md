# p\_candebug.9

`p_candebug` — 确定进程的可调试性

## 名称

`p_candebug`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/proc.h>
```

```c
int
p_candebug(struct thread *td, struct proc *p)
```

## 描述

此函数确定给定进程 `p` 是否可被某线程 `td` 调试。

以下 [sysctl(8)](../man8/sysctl.8.md) 变量直接影响 `p_candebug` 的行为：

**`security.bsd.unprivileged_proc_debug`** 必须设置为非零值才能允许非特权进程访问内核的调试设施。

**`kern.securelevel`** 如果此变量为 `1` 或更大，则不允许调试 init 进程。

其他此类变量间接影响它；参见 [cr_bsd_visible(9)](cr_bsd_visible.9.md)。

## 返回值

`p_candebug` 函数如果由 `p` 表示的进程可被线程 `td` 调试，则返回 `0`，否则返回非零错误值。

## 错误

**[EPERM]** 一个非特权进程尝试调试另一个进程，但系统配置为拒绝此操作（参见上文 [sysctl(8)](../man8/sysctl.8.md) 变量 `security.bsd.unprivileged_proc_debug`）。

**[ESRCH]** 线程 `td` 已被监禁，且要调试的进程不属于同一 jail 或其子 jail，由 [prison_check(9)](prison_check.9.md) 确定。

**[ESRCH]** [cr_bsd_visible(9)](cr_bsd_visible.9.md) 根据生效的 BSD 安全策略拒绝了可见性。

**[EPERM]** 线程 `td` 缺少超级用户凭证，且其（有效）组集合不是进程 `p` 整个组集合（包括实际、有效和保存的组 ID）的超集。

**[EPERM]** 线程 `td` 缺少超级用户凭证，且其（有效）用户 ID 与进程 `p` 的所有用户 ID 不匹配。

**[EPERM]** 线程 `td` 缺少超级用户凭证，且进程 `p` 正在执行 set-user-ID 或 set-group-ID 可执行文件。

**[EPERM]** 进程 `p` 表示初始进程 `initproc`，且 [sysctl(8)](../man8/sysctl.8.md) 变量 `kern.securelevel` 大于零。

**[EBUSY]** 进程 `p` 正在被 `exec`。

**[EPERM]** 进程 `p` 拒绝可调试性（参见 procctl(2)，命令 `PROC_TRACE_CTL`）。

## 参见

procctl(2), [cr_bsd_visible(9)](cr_bsd_visible.9.md), [mac(9)](mac.9.md), [p_cansee(9)](p_cansee.9.md), [prison_check(9)](prison_check.9.md)
