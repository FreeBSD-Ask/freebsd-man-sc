# kcov.4

`kcov` — 收集内核代码覆盖信息的接口

## 名称

`kcov`

## 概要

`要将 KCOV 编译进内核，请在你的内核配置文件中加入以下行：`

> options COVERAGE
> options KCOV

`以下头文件定义了 KCOV 提供的应用程序接口：`

`#include <sys/kcov.h>`

## 描述

`kcov` 是一个用于从内核收集代码覆盖信息的模块。它依赖 `COVERAGE` 内核选项启用的代码插桩。当 `kcov` 由用户态线程启用时，它仅收集该线程的覆盖信息，不包括硬中断处理程序。因此，`kcov` 不适合收集整个内核的全面覆盖数据；其主要目的是为覆盖引导的系统调用模糊测试器提供输入。

在典型用法中，用户态线程首先分配一块与 `kcov` 共享的内存。然后该线程启用覆盖追踪，内核将覆盖数据写入共享内存区域。禁用追踪后，内核放弃对共享内存区域的访问，可以消费已写入的覆盖数据。

共享内存缓冲区可视为一个 64 位无符号整数后跟一个记录数组。该整数记录有效记录数，由内核在记录覆盖信息时更新。可通过向此字段写入值 0 来重置追踪缓冲区状态。记录布局取决于使用 `KIOENABLE` ioctl 设置的追踪模式。

实现了两种追踪模式：`KCOV_MODE_TRACE_PC` 和 `KCOV_MODE_TRACE_CMP`。PC 追踪为启用追踪时执行的每个基本块记录一个程序计数器值。在此模式下，每个记录是一个包含程序计数器值的 64 位无符号整数。比较追踪提供有关数据流的信息；记录有关动态变量比较的信息。此类记录提供有关 [c(7)](../man7/c.7.md) `if` 或 `switch` 语句结果的信息。在此模式下，每个记录由四个 64 位无符号整数组成。第一个整数是位掩码，定义参与比较的变量的属性。如果其中一个变量在编译时具有常量值，则设置 `KCOV_CMP_CONST`；`KCOV_CMP_SIZE(n)` 指定变量的宽度：

**`KCOV_CMP_SIZE(0)`** ：8 位整数比较

**`KCOV_CMP_SIZE(1)`** ：16 位整数比较

**`KCOV_CMP_SIZE(2)`** ：32 位整数比较

**`KCOV_CMP_SIZE(3)`** ：64 位整数比较

第二和第三个字段记录两个变量的值，第四个也是最后一个字段存储比较的程序计数器值。

## IOCTL 接口

应用程序使用 ioctl(2) 系统调用与 `kcov` 交互。每个使用 `kcov` 的线程必须为 `/dev/kcov` 使用单独的文件描述符。定义了以下 ioctl：

**`KIOSETBUFSIZE`** `size_t entries` 以 `KCOV_ENTRY_SIZE` 为单位设置追踪缓冲区大小。然后可通过在 `kcov` 设备文件上调用 mmap(2) 将缓冲区映射到调用线程的地址空间。

**`KIOENABLE`** `int mode` 为调用线程启用覆盖追踪。有效模式为 `KCOV_MODE_TRACE_PC` 和 `KCOV_MODE_TRACE_CMP`。

**`KIODISABLE`** 为调用线程禁用覆盖追踪。

## 文件

`kcov` 创建 `/dev/kcov` 设备文件。

## 实例

以下代码示例收集有关执行打印 `Hello, world` 时内核代码的基本块覆盖信息。

```sh
size_t sz;
uint64_t *buf;
int fd;
fd = open("/dev/kcov", O_RDWR);
if (fd == -1)
	err(1, "open(/dev/kcov)");
sz = 1ul << 20; /* 1MB */
if (ioctl(fd, KIOSETBUFSIZE, sz / KCOV_ENTRY_SIZE) != 0)
	err(1, "ioctl(KIOSETBUFSIZE)");
buf = mmap(NULL, sz, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
if (buf == MAP_FAILED)
	err(1, "mmap");
/* 启用 PC 追踪。 */
if (ioctl(fd, KIOENABLE, KCOV_MODE_TRACE_PC) != 0)
	err(1, "ioctl(KIOENABLE)");
/* 清除前一次 ioctl() 调用的追踪记录。 */
buf[0] = 0;
printf("Hello, world!n");
/* 禁用 PC 追踪。 */
if (ioctl(fd, KIODISABLE, 0) != 0)
	err(1, "ioctl(KIODISABLE)");
for (uint64_t i = 1; i < buf[0]; i++)
	printf("%#jxn", (uintmax_t)buf[i]);
```

此程序的输出可大致映射到内核源代码中的行号：

```sh
# ./kcov-test | sed 1d | addr2line -e /usr/lib/debug/boot/kernel/kernel.debug
```

## 参见

ioctl(2), mmap(2)

## 历史

`kcov` 最早出现于 FreeBSD 13.0。

## 缺陷

FreeBSD 的 `kcov` 实现尚不支持远程追踪。
