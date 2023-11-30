  LOCKSTAT(1)  

LOCKSTAT(1)

FreeBSD General Commands Manual

LOCKSTAT(1)

[名称](#__u540D___u79F0_)
=======================

`lockstat` —

报告内核锁和分析统计信息

[概要](#__u6982___u8981_)
=======================

`lockstat` \[`-ACEHIV`\] \[`-e` event-list\] \[`-i` rate\] \[`-b` | `-t` | `-h` | `-s` depth\] \[`-n` num-records\] \[`-l` lock \[,size\]\] \[`-d` duration\] \[`-f` function \[,size\]\] \[`-T`\] \[`-kgwWRpP`\] \[`-D` count\] \[`-o` `-filename`\] \[`-x` opt \[=val\]\] command \[\[args\]\]

[描述](#__u63CF___u8FF0_)
=======================

`lockstat` 实用程序收集并显示内核锁定和分析统计信息。 `lockstat` 允许您指定要监视的事件（例如，自旋自适应互斥体、由于等待写入者而阻止对 rwlock 的读取访问等）、为每个事件收集多少数据以及如何显示数据。 默认情况下， `lockstat` 监控所有锁争用事件，收集有关这些事件的频率和时间数据，并按频率降序显示数据，以便最常见的事件首先出现。

`lockstat` 收集数据，直到指定的命令完成。 例如，要收集固定时间间隔的统计信息，请使用 sleep(1) 作为命令，如下所示：

`# lockstat sleep 5`

当指定 `-I` 选项时， `lockstat` 会建立一个每个处理器的高级周期性中断源来收集分析数据。 中断处理程序只是生成一个 `lockstat` 事件，其调用者是被中断的 PC（程序计数器）。 分析事件就像任何其他 `lockstat` 事件一样，因此所有正常的 `lockstat` 选项都适用。

`lockstat` 依靠 DTrace 修改正在运行的内核的文本以拦截感兴趣的事件。 这会对所有系统活动造成很小但可衡量的开销，因此默认情况下，对 `lockstat` 的访问仅限于超级用户。

[选项](#__u9009___u9879_)
=======================

支持以下选项：

[`-V`](#V)

打印用于收集请求数据的 D 程序。

[事件选择](#__u4E8B___u4EF6___u9009___u62E9_)
-----------------------------------------

如果未指定事件选择选项，则默认值为 `-C` 。

[`-A`](#A)

观看所有锁定事件。 `-A` 等价于 `-CH` 。

[`-C`](#C)

观看争用事件。

[`-E`](#E)

观察错误事件。

[`-e`](#e) event-list

只观看指定的事件。 event-list 是以逗号分隔的事件列表或事件范围，例如 1,4-7,35。 不带参数运行 `lockstat` 以获得所有事件的简要描述。

[`-H`](#H)

观看举行活动。

[`-I`](#I)

观察分析中断事件。

[`-i`](#i) rate

[`-I`](#I_2) 的中断率（每秒）。 默认值为 97 Hz，因此分析不会与时钟中断（以 100 Hz 运行）同步运行。

[数据收集](#__u6570___u636E___u6536___u96C6_)
-----------------------------------------

[`-x`](#x) arg \[=val\]

启用或修改 dtrace(1) 运行时选项或 D 编译器选项。 布尔选项通过指定它们的名称来启用。 带有值的选项是通过用等号分隔选项名称和值来设置的。

[数据收集（互斥）](#__u6570___u636E___u6536___u96C6___uFF08___u4E92___u65A5___uFF09_)
-----------------------------------------------------------------------------

[`-b`](#b)

基本统计：锁、调用者、事件数。

[`-h`](#h)

直方图：时序加时间分布直方图。

[`-s`](#s) depth

堆栈跟踪：直方图加上堆栈跟踪，直至 depth 帧。

[`-t`](#t)

计时：所有事件的基本加计时（默认）。

[数据过滤](#__u6570___u636E___u8FC7___u6EE4_)
-----------------------------------------

[`-d`](#d) duration

只观看超过 duration 时间的事件。

[`-f`](#f) func\[,size\]

仅监听 func 生成的事件，可以指定为符号名或十六进制地址。 size 默认为 ELF 符号大小（如果可用），否则为 1。

[`-l`](#l) lock\[,size\]

只观看 lock ，可以指定为符号名或十六进制地址。 size 默认为 ELF 符号大小，如果符号大小不可用，则默认为 1。

[`-n`](#n) num-records

最大数据记录数。

[`-T`](#T)

跟踪（而不是样本）事件。 默认情况下这是关闭的。

[数据报告](#__u6570___u636E___u62A5___u544A_)
-----------------------------------------

[`-D`](#D) count

仅显示每种类型的最高 count 事件。

[`-g`](#g)

显示函数生成的总事件。 例如，如果 `foo`() 在循环中调用 `bar`() ，则 `bar`() 完成的工作算作 `foo`() 生成的工作（连同 `foo`() 本身完成的任何工作）。 `-g` 选项通过计算每个函数出现的堆栈帧总数来工作。 这意味着两件事：(1) 如果堆栈跟踪不够深， `-g` 报告的数据可能会产生误导，以及 (2) 递归调用的函数可能显示大于 100% 的活动。 针对问题（1），使用 `-g` 时默认的数据收集模式是 `-s` `-50` 。

[`-k`](#k)

在功能内合并 PC。

[`-o`](#o) filename

直接输出到 filename 。

[`-P`](#P)

按（_count \* time_) 产品对数据进行排序。

[`-p`](#p)

可解析的输出格式。

[`-R`](#R)

显示速率（每秒事件数）而不是计数。

[`-W`](#W)

无论哪种方式：仅通过调用者区分事件，而不是通过锁。

[`-w`](#w)

Wherever: 仅通过锁来区分事件，而不是调用者。

[显示格式](#__u663E___u793A___u683C___u5F0F_)
=========================================

以下标题出现在不同的数据列中。

Count or ops/s

如果指定了 `-R` ，则此事件发生的次数或速率（每秒次数）。

indv

此单个事件所代表的所有事件的百分比。

genr

此函数生成的所有事件的百分比。

cuml

累计百分比；个人的总和。

rcnt

平均引用计数。 对于独占锁（互斥锁、自旋锁、作为写入器持有的 rwlock），这将始终为 1，但对于共享锁（作为读取器持有的 rwlock），它可以大于 1。

nsec

事件的平均持续时间（以纳秒为单位），视事件而定。 对于分析事件，持续时间意味着中断延迟。

Lock

锁的地址；如果可能，象征性地显示。

CPU+Pri\_Class

CPU 加上被中断线程的优先级。 例如，如果 CPU 4 在运行分时线程时中断，则会报告为 ‘`cpu[4]+TShar`’ 。

Caller

来电者的地址；如果可能，象征性地显示。

[实例](#__u5B9E___u4F8B_)
=======================

示例 1 测量内核锁争用

`# lockstat sleep 5`

Adaptive mutex spin: 41411 events in 5.011 seconds (8263 events/sec) Count indv cuml rcnt nsec Lock Caller ------------------------------------------------------------------------------- 13750 33% 33% 0.00 72 vm\_page\_queue\_free\_mtx vm\_page\_free\_toq+0x12e 13648 33% 66% 0.00 66 vm\_page\_queue\_free\_mtx vm\_page\_alloc+0x138 4023 10% 76% 0.00 51 vm\_dom+0x80 vm\_page\_dequeue+0x68 2672 6% 82% 0.00 186 vm\_dom+0x80 vm\_page\_enqueue+0x63 618 1% 84% 0.00 31 0xfffff8000cd83a88 qsyncvp+0x37 506 1% 85% 0.00 164 0xfffff8000cb3f098 vputx+0x5a 477 1% 86% 0.00 69 0xfffff8000c7eb180 uma\_dbg\_getslab+0x5b 288 1% 87% 0.00 77 0xfffff8000cd8b000 vn\_finished\_write+0x29 263 1% 88% 0.00 103 0xfffff8000cbad448 vinactive+0xdc 259 1% 88% 0.00 53 0xfffff8000cd8b000 vfs\_ref+0x24 237 1% 89% 0.00 20 0xfffff8000cbad448 vfs\_hash\_get+0xcc 233 1% 89% 0.00 22 0xfffff8000bfd9480 uma\_dbg\_getslab+0x5b 223 1% 90% 0.00 20 0xfffff8000cb3f098 cache\_lookup+0x561 193 0% 90% 0.00 16 0xfffff8000cb40ba8 vref+0x27 175 0% 91% 0.00 34 0xfffff8000cbad448 vputx+0x5a 169 0% 91% 0.00 51 0xfffff8000cd8b000 vfs\_unbusy+0x27 164 0% 92% 0.00 31 0xfffff8000cb40ba8 vputx+0x5a \[...\] Adaptive mutex block: 10 events in 5.011 seconds (2 events/sec) Count indv cuml rcnt nsec Lock Caller ------------------------------------------------------------------------------- 3 30% 30% 0.00 17592 vm\_page\_queue\_free\_mtx vm\_page\_alloc+0x138 2 20% 50% 0.00 20528 vm\_dom+0x80 vm\_page\_enqueue+0x63 2 20% 70% 0.00 55502 0xfffff8000cb40ba8 vputx+0x5a 1 10% 80% 0.00 12007 vm\_page\_queue\_free\_mtx vm\_page\_free\_toq+0x12e 1 10% 90% 0.00 9125 0xfffff8000cbad448 vfs\_hash\_get+0xcc 1 10% 100% 0.00 7864 0xfffff8000cd83a88 qsyncvp+0x37 ------------------------------------------------------------------------------- \[...\] 

示例 2 测量保持时间

`# lockstat -H -D 10 sleep 1`

Adaptive mutex hold: 109589 events in 1.039 seconds (105526 events/sec) Count indv cuml rcnt nsec Lock Caller ------------------------------------------------------------------------------- 8998 8% 8% 0.00 617 0xfffff8000c7eb180 uma\_dbg\_getslab+0xd4 5901 5% 14% 0.00 917 vm\_page\_queue\_free\_mtx vm\_object\_terminate+0x16a 5040 5% 18% 0.00 902 vm\_dom+0x80 vm\_page\_free\_toq+0x88 4884 4% 23% 0.00 1056 vm\_page\_queue\_free\_mtx vm\_page\_alloc+0x44e 4664 4% 27% 0.00 759 vm\_dom+0x80 vm\_fault\_hold+0x1a13 4011 4% 31% 0.00 888 vm\_dom vm\_page\_advise+0x11b 4010 4% 34% 0.00 957 vm\_dom+0x80 \_vm\_page\_deactivate+0x5c 3743 3% 38% 0.00 582 0xfffff8000cf04838 pmap\_is\_prefaultable+0x158 2254 2% 40% 0.00 952 vm\_dom vm\_page\_free\_toq+0x88 1639 1% 41% 0.00 591 0xfffff800d60065b8 trap\_pfault+0x1f7 ------------------------------------------------------------------------------- \[...\] R/W writer hold: 64314 events in 1.039 seconds (61929 events/sec) Count indv cuml rcnt nsec Lock Caller ------------------------------------------------------------------------------- 7421 12% 12% 0.00 2994 pvh\_global\_lock pmap\_page\_is\_mapped+0xb6 4668 7% 19% 0.00 3313 pvh\_global\_lock pmap\_enter+0x9ae 1639 3% 21% 0.00 733 0xfffff80168d10200 vm\_object\_deallocate+0x683 1639 3% 24% 0.00 3061 0xfffff80168d10200 unlock\_and\_deallocate+0x2b 1639 3% 26% 0.00 2966 0xfffff80168d10200 vm\_fault\_hold+0x16ee 1567 2% 29% 0.00 733 0xfffff80168d10200 vm\_fault\_hold+0x19bc 821 1% 30% 0.00 786 0xfffff801eb0cc000 vm\_object\_madvise+0x32d 649 1% 31% 0.00 4918 0xfffff80191105300 vm\_fault\_hold+0x16ee 648 1% 32% 0.00 8112 0xfffff80191105300 unlock\_and\_deallocate+0x2b 647 1% 33% 0.00 1261 0xfffff80191105300 vm\_object\_deallocate+0x683 ------------------------------------------------------------------------------- 

示例 3 测量包含特定函数的堆栈跟踪的保持时间

`# lockstat -H -f tcp_input -s 50 -D 10 sleep 1`

Adaptive mutex hold: 68 events in 1.026 seconds (66 events/sec) ------------------------------------------------------------------------------- Count indv cuml rcnt nsec Lock Caller 32 47% 47% 0.00 1631 0xfffff800686f50d8 tcp\_do\_segment+0x284b nsec ------ Time Distribution ------ count Stack 1024 |@@@@@@@@@@ 11 tcp\_input+0xf54 2048 |@@@@@@@@@@@@@ 14 ip\_input+0xc8 4096 |@@@@@ 6 swi\_net+0x192 8192 | 1 intr\_event\_execute\_handlers+0x93 ithread\_loop+0xa6 fork\_exit+0x84 0xffffffff808cf9ee ------------------------------------------------------------------------------- Count indv cuml rcnt nsec Lock Caller 29 43% 90% 0.00 4851 0xfffff800686f50d8 sowakeup+0xf8 nsec ------ Time Distribution ------ count Stack 4096 |@@@@@@@@@@@@@@@ 15 tcp\_do\_segment+0x2423 8192 |@@@@@@@@@@@@ 12 tcp\_input+0xf54 16384 |@@ 2 ip\_input+0xc8 swi\_net+0x192 intr\_event\_execute\_handlers+0x93 ithread\_loop+0xa6 fork\_exit+0x84 0xffffffff808cf9ee ------------------------------------------------------------------------------- \[...\] 

[参见](#__u53C2___u89C1_)
=======================

dtrace(1), ksyms(4), locking(9)

[历史](#__u5386___u53F2_)
=======================

`lockstat` 实用程序首次出现在 FreeBSD 7.1 。

[笔记](#__u7B14___u8BB0_)
=======================

尾部呼叫消除会影响呼叫站点。 例如，如果 `foo`()+0x50 调用 `bar`() 并且 `bar`() 做的最后一件事是调用 `mtx_unlock`(), 编译器可以安排 `bar`() 分支到 `mtx_unlock`() 返回地址为 `foo`()+0x58 。 因此， `mtx_unlock`() 中的 `bar`() 将看起来好像它发生在 `foo`()+0x58 处。

发生中断的堆栈帧中的 PC 可能是伪造的，因为在函数调用之间，编译器可以自由地使用返回地址寄存器进行本地存储。

当同时使用 `-I` 和 `-s` 选项时，被中断的 PC 通常不会出现在堆栈中的任何位置，因为中断处理程序是异步进入的，而不是通过来自该 PC 的函数调用。

February 25, 2020

FreeBSD 13.1-RELEASE