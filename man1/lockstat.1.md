# lockstat.1

`lockstat` — 报告内核锁和性能分析统计信息

## 名称

`lockstat`

## 概要

`lockstat [-ACEHIV] [-e event-list] [-i rate] [-b | -t | -h | -s depth] [-n num-records] [-l lock[,size]] [-d duration] [-f function[,size]] [-T] [-kgwWRpP] [-D count] [-o filename] [-x opt[=val]] command [args]`

## 描述

`lockstat` 实用程序收集并显示内核锁定和性能分析统计信息。`lockstat` 允许你指定要监视的事件（例如，在自适应互斥锁上自旋、由于等待写入者而在 rwlock 的读访问上阻塞等）、为每个事件收集多少数据以及如何显示数据。默认情况下，`lockstat` 监视所有锁竞争事件，收集这些事件的频率和计时数据，并按频率递减顺序显示数据，以便最常见的事件首先出现。

`lockstat` 收集数据直到指定的命令完成。例如，要收集固定时间间隔的统计信息，可使用 [sleep(1)](sleep.1.md) 作为命令，如下所示：

```sh
# lockstat sleep 5
```

当指定 `-I` 选项时，`lockstat` 会建立一个每处理器的高级周期性中断源来收集性能分析数据。中断处理程序仅生成一个 `lockstat` 事件，其调用者是被中断的 PC（程序计数器）。性能分析事件与其他任何 `lockstat` 事件一样，因此所有正常的 `lockstat` 选项都适用。

`lockstat` 依赖 DTrace 修改运行中内核的代码文本以拦截感兴趣的事件。这会对所有系统活动施加少量但可测量的开销，因此默认情况下 `lockstat` 的访问权限仅限于超级用户。

## 选项

支持以下选项：

**`-V`** 打印用于收集请求数据的 D 程序。

### 事件选择

如果未指定事件选择选项，默认为 `-C`。

**`-A`** 监视所有锁事件。`-A` 等同于 `-CH`。

**`-C`** 监视竞争事件。

**`-E`** 监视错误事件。

**`-e`** `event-list` 仅监视指定的事件。`event-list` 是以逗号分隔的事件或事件范围列表，例如 1,4-7,35。运行不带参数的 `lockstat` 可获取所有事件的简要描述。

**`-H`** 监视持有事件。

**`-I`** 监视性能分析中断事件。

**`-i`** `rate` `-I` 的中断速率（次/秒）。默认为 97 Hz，以使性能分析不与时钟中断（运行于 100 Hz）同步运行。

### 数据收集

**`-x`** `arg`[=`val`] 启用或修改 [dtrace(1)](dtrace.1.md) 运行时选项或 D 编译器选项。布尔选项通过指定其名称来启用。带值的选项通过用等号分隔选项名和值来设置。

### 数据收集（互斥）

**`-b`** 基本统计：锁、调用者、事件数。

**`-h`** 直方图：计时加时间分布直方图。

**`-s`** `depth` 栈追踪：直方图加深达 `depth` 帧的栈追踪。

**`-t`** 计时：基本统计加所有事件的计时（默认）。

### 数据过滤

**`-d`** `duration` 仅监视持续时间长于 `duration` 的事件。

**`-f`** `func`[,`size`] 仅监视由 `func` 生成的事件，`func` 可以指定为符号名称或十六进制地址。`size` 默认为 ELF 符号大小（如果可用），否则为 1。

**`-l`** `lock`[,`size`] 仅监视 `lock`，`lock` 可以指定为符号名称或十六进制地址。`size` 默认为 ELF 符号大小，如果符号大小不可用则为 1。

**`-n`** `num-records` 最大数据记录数。

**`-T`** 追踪（而非采样）事件。默认关闭。

### 数据报告

**`-D`** `count` 仅显示每种类型的前 `count` 个事件。

**`-g`** 显示按函数生成的总事件数。例如，如果 `foo()` 在循环中调用 `bar()`，则 `bar()` 所做的工作计为 `foo()` 生成的工作（连同 `foo()` 本身所做的工作）。`-g` 选项通过统计每个函数出现的栈帧总数来工作。这意味着两点：（1）如果栈追踪不够深，`-g` 报告的数据可能会产生误导；（2）递归调用的函数可能显示超过 100% 的活动。鉴于问题（1），使用 `-g` 时的默认数据收集模式为 `-s 50`。

**`-k`** 合并函数内的 PC。

**`-o`** `filename` 将输出定向到 `filename`。

**`-P`** 按（count * time）乘积排序数据。

**`-p`** 可解析的输出格式。

**`-R`** 显示速率（每秒事件数）而非计数。

**`-W`** Whichever：仅按调用者区分事件，不按锁区分。

**`-w`** Wherever：仅按锁区分事件，不按调用者区分。

## 显示格式

以下标题出现在各数据列上方。

**Count** 或 ops/s 此事件发生的次数，或指定 `-R` 时的速率（每秒次数）。

**indv** 此单个事件占所有事件的百分比。

**genr** 此函数生成的所有事件的百分比。

**cuml** 累计百分比；单个事件的运行总计。

**rcnt** 平均引用计数。对于独占锁（互斥锁、自旋锁、作为写入者持有的 rwlock），此值始终为 1，但对于共享锁（作为读取者持有的 rwlock），可以大于 1。

**nsec** 事件的平均持续时间（纳秒），视事件而定。对于性能分析事件，持续时间指中断延迟。

**Lock** 锁的地址；尽可能以符号方式显示。

**CPU+Pri_Class** CPU 加被中断线程的优先级类。例如，如果 CPU 4 在运行分时线程时被中断，将报告为 `cpu[4]+TShar`。

**Caller** 调用者的地址；尽可能以符号方式显示。

## 实例

**实例 1** 测量内核锁竞争

```sh
# lockstat sleep 5
```

```sh
Adaptive mutex spin: 41411 events in 5.011 seconds (8263 events/sec)
Count indv cuml rcnt     nsec Lock                   Caller
-------------------------------------------------------------------------------
13750  33%  33% 0.00       72 vm_page_queue_free_mtx vm_page_free_toq+0x12e
13648  33%  66% 0.00       66 vm_page_queue_free_mtx vm_page_alloc+0x138
 4023  10%  76% 0.00       51 vm_dom+0x80            vm_page_dequeue+0x68
 2672   6%  82% 0.00      186 vm_dom+0x80            vm_page_enqueue+0x63
  618   1%  84% 0.00       31 0xfffff8000cd83a88     qsyncvp+0x37
  506   1%  85% 0.00      164 0xfffff8000cb3f098     vputx+0x5a
  477   1%  86% 0.00       69 0xfffff8000c7eb180     uma_dbg_getslab+0x5b
  288   1%  87% 0.00       77 0xfffff8000cd8b000     vn_finished_write+0x29
  263   1%  88% 0.00      103 0xfffff8000cbad448     vinactive+0xdc
  259   1%  88% 0.00       53 0xfffff8000cd8b000     vfs_ref+0x24
  237   1%  89% 0.00       20 0xfffff8000cbad448     vfs_hash_get+0xcc
  233   1%  89% 0.00       22 0xfffff8000bfd9480     uma_dbg_getslab+0x5b
  223   1%  90% 0.00       20 0xfffff8000cb3f098     cache_lookup+0x561
  193   0%  90% 0.00       16 0xfffff8000cb40ba8     vref+0x27
  175   0%  91% 0.00       34 0xfffff8000cbad448     vputx+0x5a
  169   0%  91% 0.00       51 0xfffff8000cd8b000     vfs_unbusy+0x27
  164   0%  92% 0.00       31 0xfffff8000cb40ba8     vputx+0x5a
[...]
Adaptive mutex block: 10 events in 5.011 seconds (2 events/sec)
Count indv cuml rcnt     nsec Lock                   Caller
-------------------------------------------------------------------------------
    3  30%  30% 0.00    17592 vm_page_queue_free_mtx vm_page_alloc+0x138
    2  20%  50% 0.00    20528 vm_dom+0x80            vm_page_enqueue+0x63
    2  20%  70% 0.00    55502 0xfffff8000cb40ba8     vputx+0x5a
    1  10%  80% 0.00    12007 vm_page_queue_free_mtx vm_page_free_toq+0x12e
    1  10%  90% 0.00     9125 0xfffff8000cbad448     vfs_hash_get+0xcc
    1  10% 100% 0.00     7864 0xfffff8000cd83a88     qsyncvp+0x37
-------------------------------------------------------------------------------
[...]
```

**实例 2** 测量持有时间

```sh
# lockstat -H -D 10 sleep 1
```

```sh
Adaptive mutex hold: 109589 events in 1.039 seconds (105526 events/sec)
Count indv cuml rcnt     nsec Lock                   Caller
-------------------------------------------------------------------------------
 8998   8%   8% 0.00      617 0xfffff8000c7eb180     uma_dbg_getslab+0xd4
 5901   5%  14% 0.00      917 vm_page_queue_free_mtx vm_object_terminate+0x16a
 5040   5%  18% 0.00      902 vm_dom+0x80            vm_page_free_toq+0x88
 4884   4%  23% 0.00     1056 vm_page_queue_free_mtx vm_page_alloc+0x44e
 4664   4%  27% 0.00      759 vm_dom+0x80            vm_fault_hold+0x1a13
 4011   4%  31% 0.00      888 vm_dom                 vm_page_advise+0x11b
 4010   4%  34% 0.00      957 vm_dom+0x80            _vm_page_deactivate+0x5c
 3743   3%  38% 0.00      582 0xfffff8000cf04838     pmap_is_prefaultable+0x158
 2254   2%  40% 0.00      952 vm_dom                 vm_page_free_toq+0x88
 1639   1%  41% 0.00      591 0xfffff800d60065b8     trap_pfault+0x1f7
-------------------------------------------------------------------------------
[...]
R/W writer hold: 64314 events in 1.039 seconds (61929 events/sec)
Count indv cuml rcnt     nsec Lock                   Caller
-------------------------------------------------------------------------------
 7421  12%  12% 0.00     2994 pvh_global_lock        pmap_page_is_mapped+0xb6
 4668   7%  19% 0.00     3313 pvh_global_lock        pmap_enter+0x9ae
 1639   3%  21% 0.00      733 0xfffff80168d10200     vm_object_deallocate+0x683
 1639   3%  24% 0.00     3061 0xfffff80168d10200     unlock_and_deallocate+0x2b
 1639   3%  26% 0.00     2966 0xfffff80168d10200     vm_fault_hold+0x16ee
 1567   2%  29% 0.00      733 0xfffff80168d10200     vm_fault_hold+0x19bc
  821   1%  30% 0.00      786 0xfffff801eb0cc000     vm_object_madvise+0x32d
  649   1%  31% 0.00     4918 0xfffff80191105300     vm_fault_hold+0x16ee
  648   1%  32% 0.00     8112 0xfffff80191105300     unlock_and_deallocate+0x2b
  647   1%  33% 0.00     1261 0xfffff80191105300     vm_object_deallocate+0x683
-------------------------------------------------------------------------------
```

**实例 3** 测量包含特定函数的栈追踪的持有时间

```sh
# lockstat -H -f tcp_input -s 50 -D 10 sleep 1
```

```sh
Adaptive mutex hold: 68 events in 1.026 seconds (66 events/sec)
-------------------------------------------------------------------------------
Count indv cuml rcnt     nsec Lock                   Caller
   32  47%  47% 0.00     1631 0xfffff800686f50d8     tcp_do_segment+0x284b

      nsec ------ Time Distribution ------ count     Stack
      1024 |@@@@@@@@@@                     11        tcp_input+0xf54
      2048 |@@@@@@@@@@@@@                  14        ip_input+0xc8
      4096 |@@@@@                          6         swi_net+0x192
      8192 |                               1         intr_event_execute_handlers+0x93
                                                     ithread_loop+0xa6
                                                     fork_exit+0x84
                                                     0xffffffff808cf9ee
-------------------------------------------------------------------------------
Count indv cuml rcnt     nsec Lock                   Caller
   29  43%  90% 0.00     4851 0xfffff800686f50d8     sowakeup+0xf8

      nsec ------ Time Distribution ------ count     Stack
      4096 |@@@@@@@@@@@@@@@                15        tcp_do_segment+0x2423
      8192 |@@@@@@@@@@@@                   12        tcp_input+0xf54
     16384 |@@                             2         ip_input+0xc8
                                                     swi_net+0x192
                                                     intr_event_execute_handlers+0x93
                                                     ithread_loop+0xa6
                                                     fork_exit+0x84
                                                     0xffffffff808cf9ee
-------------------------------------------------------------------------------
[...]
```

## 参见

[dtrace(1)](dtrace.1.md), [ksyms(4)](../man4/ksyms.4.md), [locking(9)](../man9/locking.9.md)

## 历史

`lockstat` 实用程序首次出现于 FreeBSD 7.1。

## 注释

尾调用消除可能影响调用点。例如，如果 `foo()+0x50` 调用 `bar()`，而 `bar()` 最后做的事是调用 `mtx_unlock()`，编译器可以安排 `bar()` 分支到 `mtx_unlock()`，返回地址为 `foo()+0x58`。因此，`bar()` 中的 `mtx_unlock()` 将看起来像是发生在 `foo()+0x58` 处。

中断发生时栈帧中的 PC 可能是伪造的，因为在函数调用之间，编译器可以自由使用返回地址寄存器进行本地存储。

当同时使用 `-I` 和 `-s` 选项时，被中断的 PC 通常不会出现在栈的任何位置，因为中断处理程序是异步进入的，而非通过该 PC 的函数调用。
