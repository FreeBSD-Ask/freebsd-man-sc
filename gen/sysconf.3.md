# sysconf(3)

`sysconf` — 获取可配置的系统变量

## 名称

`sysconf`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

long
sysconf(int name);
```

## 描述

本接口由 IEEE Std 1003.1-1988 ("POSIX.1") 定义。使用 [sysctl(3)](sysctl.3.md) 可获得更为完整的接口。

`sysconf` 函数为应用程序提供了一种方法，用以确定某个可配置系统限制或选项变量的当前值。`name` 参数指定要查询的系统变量。每个 name 值对应的符号常量定义于头文件

`#include <unistd.h>`

中。需要访问这些参数的 shell 程序员应使用 getconf(1) 实用程序。

可用的值如下：

**`_SC_ARG_MAX`** 传递给 [execve(2)](../sys/execve.2.md) 的参数的最大字节数。

**`_SC_CHILD_MAX`** 每个用户 ID 允许的同时存在的最大进程数。

**`_SC_CLK_TCK`** 统计时钟的频率，以每秒滴答数为单位。

**`_SC_IOV_MAX`** readv(2)、writev(2)、recvmsg(2) 和 sendmsg(2) 所使用的 I/O 向量中元素的最大数量。

**`_SC_NGROUPS_MAX`** 附加组的最大数量。

**`_SC_NPROCESSORS_CONF`** 已配置的处理器数量。

**`_SC_NPROCESSORS_ONLN`** 当前在线的处理器数量，并考虑当前的 jail 限制，仅报告对该进程可用的处理器数量。

**`_SC_OPEN_MAX`** 系统可能分配给新文件描述符的最大值加一。

**`_SC_PAGESIZE`** 系统页面的字节大小。

**`_SC_PAGE_SIZE`** 等同于 `_SC_PAGESIZE`。

**`_SC_STREAM_MAX`** 一个进程在任一时刻可以打开的最小最大流数量。

**`_SC_TZNAME_MAX`** 时区名称所支持的最小最大类型数量。

**`_SC_JOB_CONTROL`** 如果本系统支持作业控制则返回 1，否则返回 -1。

**`_SC_SAVED_IDS`** 如果保存的 set-group 和保存的 set-user ID 可用则返回 1，否则返回 -1。

**`_SC_VERSION`** 系统试图遵循的 IEEE Std 1003.1 ("POSIX.1") 版本。

**`_SC_BC_BASE_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中 ibase/obase 的最大值。

**`_SC_BC_DIM_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中的最大数组大小。

**`_SC_BC_SCALE_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中的最大 scale 值。

**`_SC_BC_STRING_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中的最大字符串长度。

**`_SC_COLL_WEIGHTS_MAX`** 在区域定义文件中可分配给 LC_COLLATE order 关键字的任何条目的最大权重数。

**`_SC_EXPR_NEST_MAX`** expr(1) 实用程序中可在括号内嵌套的最大表达式数。

**`_SC_LINE_MAX`** 文本处理实用程序输入行的最大长度（以字节为单位）。

**`_SC_RE_DUP_MAX`** 使用区间表示法时允许的正则表达式重复出现的最大次数。

**`_SC_2_VERSION`** 系统试图遵循的 IEEE Std 1003.2 ("POSIX.2") 版本。

**`_SC_2_C_BIND`** 如果系统的 C 语言开发工具支持 C 语言绑定选项则返回 1，否则返回 -1。

**`_SC_2_C_DEV`** 如果系统支持 C 语言开发实用程序选项则返回 1，否则返回 -1。

**`_SC_2_CHAR_TERM`** 如果系统支持至少一种能够执行 IEEE Std 1003.2 ("POSIX.2") 中所述全部操作的终端类型则返回 1，否则返回 -1。

**`_SC_2_FORT_DEV`** 如果系统支持 FORTRAN 开发实用程序选项则返回 1，否则返回 -1。

**`_SC_2_FORT_RUN`** 如果系统支持 FORTRAN 运行时实用程序选项则返回 1，否则返回 -1。

**`_SC_2_LOCALEDEF`** 如果系统支持创建区域则返回 1，否则返回 -1。

**`_SC_2_SW_DEV`** 如果系统支持软件开发实用程序选项则返回 1，否则返回 -1。

**`_SC_2_UPE`** 如果系统支持用户可移植性实用程序选项则返回 1，否则返回 -1。

**`_SC_AIO_LISTIO_MAX`** 单次列表 I/O 调用中支持的最大 I/O 操作数。

**`_SC_AIO_MAX`** 支持的未完成异步 I/O 操作的最大数量。

**`_SC_AIO_PRIO_DELTA_MAX`** 进程可将其异步 I/O 优先级从其自身调度优先级降低的最大幅度。

**`_SC_DELAYTIMER_MAX`** 定时器过期溢出的最大数量。

**`_SC_MQ_OPEN_MAX`** 一个进程可持有的打开消息队列描述符的最大数量。

**`_SC_RTSIG_MAX`** 为应用程序使用保留的实时信号的最大数量。

**`_SC_SEM_NSEMS_MAX`** 一个进程可拥有的最大信号灯数。

**`_SC_SEM_VALUE_MAX`** 信号灯可具有的最大值。

**`_SC_SIGQUEUE_MAX`** 一个进程在任一时刻可发送且在接收端挂起的最大排队信号数。

**`_SC_TIMER_MAX`** 每个进程支持的最大定时器数。

**`_SC_GETGR_R_SIZE_MAX`** 组条目缓冲区大小的建议初始值。

**`_SC_GETPW_R_SIZE_MAX`** 口令条目缓冲区大小的建议初始值。

**`_SC_HOST_NAME_MAX`** 从 `gethostname` 函数返回的主机名最大长度（不包括终止的空字符）。

**`_SC_LOGIN_NAME_MAX`** 登录名的最大长度。

**`_SC_THREAD_STACK_MIN`** 线程栈存储的最小字节大小。

**`_SC_THREAD_THREADS_MAX`** 每个进程可创建的最大线程数。

**`_SC_TTY_NAME_MAX`** 终端设备名称的最大长度。

**`_SC_SYMLOOP_MAX`** 在不存在循环的情况下，解析路径名时可可靠遍历的最大符号链接数。

**`_SC_ATEXIT_MAX`** 可向 `atexit` 注册的函数的最大数量。

**`_SC_XOPEN_VERSION`** 大于或等于 4 的整数值，指示本系统所遵循的 X/Open 可移植性指南版本。

**`_SC_XOPEN_XCU_VERSION`** 指示本系统所遵循的 XCU 规范版本的整数值。

这些值也存在，但可能并非标准：

**`_SC_CPUSET_SIZE`** 内核 cpuset 的大小。

**`_SC_PHYS_PAGES`** 物理内存的页数。注意，该值与 `_SC_PAGESIZE` 的乘积在某些 32 位机器的配置下可能会溢出 `long`。

## 返回值

如果对 `sysconf` 的调用不成功，则返回 -1，并适当设置 `errno`。否则，如果该变量关联的功能不受支持，则返回 -1，且不修改 `errno`。否则，返回该变量的当前值。

## 错误

`sysconf` 函数可能失败并为 [sysctl(3)](sysctl.3.md) 库函数所指定的任何错误设置 `errno`。此外，可能报告以下错误：

**[`EINVAL`]** `name` 参数的值无效。

## 参见

getconf(1), [pathconf(2)](../sys/pathconf.2.md), [confstr(3)](confstr.3.md), [sysctl(3)](sysctl.3.md)

## 标准

除了 `sysconf` 返回的值可能在调用进程的生命周期内发生变化这一事实外，本函数遵循 IEEE Std 1003.1-1988 ("POSIX.1")。

## 历史

`sysconf` 函数首次出现于 4.4BSD。

## 缺陷

`_SC_STREAM_MAX` 的值是一个最小最大值，且要求与 ANSI C 的 `FOPEN_MAX` 相同，因此返回的值是一个小得离谱且具有误导性的数字。
