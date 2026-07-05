# dtrace_lockstat.4

`dtrace_lockstat` — 用于跟踪内核锁定事件的 DTrace 提供者

## 名称

`dtrace_lockstat`

## 概要

`Fn lockstat:::adaptive-acquire struct mtx * Fn lockstat:::adaptive-release struct mtx * Fn lockstat:::adaptive-spin struct mtx * uint64_t Fn lockstat:::adaptive-block struct mtx * uint64_t Fn lockstat:::spin-acquire struct mtx * Fn lockstat:::spin-release struct mtx * Fn lockstat:::spin-spin struct mtx * uint64_t Fn lockstat:::rw-acquire struct rwlock * int Fn lockstat:::rw-release struct rwlock * int Fn lockstat:::rw-block struct rwlock * uint64_t int int int Fn lockstat:::rw-spin struct rwlock * uint64_t Fn lockstat:::rw-upgrade struct rwlock * Fn lockstat:::rw-downgrade struct rwlock * Fn lockstat:::sx-acquire struct sx * int Fn lockstat:::sx-release struct sx * int Fn lockstat:::sx-block struct sx * uint64_t int int int Fn lockstat:::sx-spin struct sx * uint64_t Fn lockstat:::sx-upgrade struct sx * Fn lockstat:::sx-downgrade struct sx * Fn lockstat:::lockmgr-acquire struct lock * int Fn lockstat:::lockmgr-release struct lock * int Fn lockstat:::lockmgr-disown struct lock * int Fn lockstat:::lockmgr-block struct lock * uint64_t int int int Fn lockstat:::lockmgr-upgrade struct lock * Fn lockstat:::lockmgr-downgrade struct lock * Fn lockstat:::thread-spin struct mtx * uint64`

## 描述

DTrace `lockstat` 提供者允许跟踪 FreeBSD 上的锁定相关事件。

`lockstat` 提供者包含用于检查内核锁状态转换的 DTrace 探测。lockmgr(9)、[mutex(9)](../man9/mutex.9.md)、[rwlock(9)](../man9/rwlock.9.md) 和 [sx(9)](../man9/sx.9.md) 锁类型均有探测。[lockstat(1)](../man1/lockstat.1.md) 工具可用于收集和显示从 `lockstat` 提供者收集的数据。每种锁类型都有 Fn acquire 和 Fn release 探测，暴露正在操作的锁结构，以及当线程与其他线程争用锁所有权时触发的探测。

Fn lockstat:::adaptive-acquire 和 Fn lockstat:::adaptive-release 探测分别在获取和释放 `MTX_DEF` [mutex(9)](../man9/mutex.9.md) 时触发。唯一参数是指向描述正在获取或释放的锁的锁结构的指针。

Fn lockstat:::adaptive-spin 探测在线程自旋等待另一个线程释放 `MTX_DEF` [mutex(9)](../man9/mutex.9.md) 时触发。第一个参数是指向描述该锁的锁结构的指针，第二个参数是互斥锁自旋花费的时间（以纳秒为单位）。Fn lockstat:::adaptive-block 探测在线程尝试获取由另一个线程拥有的 `MTX_DEF` [mutex(9)](../man9/mutex.9.md) 时将自己从 CPU 上移除时触发。第一个参数是指向描述该锁的锁结构的指针，第二个参数是等待线程被阻塞的时间长度（以纳秒为单位）。Fn lockstat:::adaptive-block 和 Fn lockstat:::adaptive-spin 探测仅在成功获取锁之后触发，特别是在 Fn lockstat:::adaptive-acquire 探测触发之后。

Fn lockstat:::spin-acquire 和 Fn lockstat:::spin-release 探测分别在获取和释放 `MTX_SPIN` [mutex(9)](../man9/mutex.9.md) 时触发。唯一参数是指向描述正在获取或释放的锁的锁结构的指针。

Fn lockstat:::spin-spin 探测在线程自旋等待另一个线程释放 `MTX_SPIN` [mutex(9)](../man9/mutex.9.md) 时触发。第一个参数是指向描述该锁的锁结构的指针，第二个参数是自旋花费的时间长度（以纳秒为单位）。Fn lockstat:::spin-spin 探测仅在成功获取锁之后触发，特别是在 Fn lockstat:::spin-acquire 探测触发之后。

Fn lockstat:::rw-acquire 和 Fn lockstat:::rw-release 探测分别在获取和释放 [rwlock(9)](../man9/rwlock.9.md) 时触发。第一个参数是指向描述正在获取的锁的结构的指针。第二个参数在作为写入者获取或释放锁时为 `0`，作为读取者获取或释放锁时为 `1`。Fn lockstat:::sx-acquire 和 Fn lockstat:::sx-release，以及 Fn lockstat:::lockmgr-acquire 和 Fn lockstat:::lockmgr-release 探测分别在 [sx(9)](../man9/sx.9.md) 和 lockmgr(9) 锁的相应事件上触发。Fn lockstat:::lockmgr-disown 探测在 lockmgr(9) 排他锁被弃有时触发。在此状态下，锁仍保持排他持有，但可由不同的线程释放。释放被弃有的锁时不会触发 Fn lockstat:::lockmgr-release 探测。第一个参数是指向描述正在被弃有的锁的结构的指针。第二个参数为 `0`，用于与 Fn lockstat:::lockmgr-release 兼容。

Fn lockstat:::rw-block、Fn lockstat:::sx-block 和 Fn lockstat:::lockmgr-block 探测在线程等待获取相应类型锁时将自己从 CPU 上移除时触发。Fn lockstat:::rw-spin 和 Fn lockstat:::sx-spin 探测在线程自旋等待获取相应类型锁时触发。所有探测都采用相同的参数集。第一个参数是指向描述该锁的锁结构的指针。第二个参数是等待线程离开 CPU 或为锁自旋的时间长度（以纳秒为单位）。第三个参数在线程尝试以写入者身份获取锁时为 `0`，以读取者身份获取锁时为 `1`。第四个参数在线程等待读取者释放锁时为 `0`，等待写入者释放锁时为 `1`。第五个参数是线程首次尝试获取锁时持有该锁的读取者数量。如果第四个参数为 `1`，则此参数为 `0`。

Fn lockstat:::lockmgr-upgrade、Fn lockstat:::rw-upgrade 和 Fn lockstat:::sx-upgrade 探测在线程成功将持有的 lockmgr(9)、[rwlock(9)](../man9/rwlock.9.md) 或 [sx(9)](../man9/sx.9.md) 共享/读取者锁升级为排他/写入者锁时触发。唯一参数是指向描述正在获取的锁的结构的指针。Fn lockstat:::lockmgr-downgrade、Fn lockstat:::rw-downgrade 和 Fn lockstat:::sx-downgrade 探测在线程将持有的 lockmgr(9)、[rwlock(9)](../man9/rwlock.9.md) 或 [sx(9)](../man9/sx.9.md) 排他/写入者锁降级为共享/读取者锁时触发。

Fn lockstat:::thread-spin 探测在线程自旋线程锁时触发，线程锁是一种专用的 `MTX_SPIN` [mutex(9)](../man9/mutex.9.md)。第一个参数是指向描述该锁的结构的指针，第二个参数是线程自旋的时间长度（以纳秒为单位）。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [lockstat(1)](../man1/lockstat.1.md), [locking(9)](../man9/locking.9.md), [mutex(9)](../man9/mutex.9.md), [rwlock(9)](../man9/rwlock.9.md), [SDT(9)](../man9/SDT.9.md), [sx(9)](../man9/sx.9.md)

## 历史

`lockstat` 提供者首次出现于 Solaris。FreeBSD 的 `lockstat` 提供者实现首次出现于 FreeBSD 9。

## 作者

本手册页由 George V. Neville-Neil <gnn@FreeBSD.org> 和 Mark Johnston <markj@FreeBSD.org> 编写。

## 缺陷

尚未添加 [rmlock(9)](../man9/rmlock.9.md) 锁的探测。
