# cpuctl.4

`cpuctl` — cpuctl 伪设备

## 名称

`cpuctl`

## 概要

要将此驱动编译进内核，请在你的内核配置文件中加入以下行：

> device cpuctl

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下内容：

```sh
cpuctl_load="YES"
```

## 描述

特殊设备 **/dev/cpuctl** 提供了访问系统 CPU 的接口。它提供了检索 CPUID 信息、读/写机器特定寄存器（MSR）以及执行 CPU 固件更新的功能。

对于系统中的每个 CPU，将创建具有相应索引的特殊设备 **/dev/cpuctl%d**。对于多核 CPU，将为每个核心创建这样的特殊设备。

目前仅支持 i386 和 amd64 处理器。

## ioctl 接口

所有支持的操作均通过 ioctl(2) 系统调用发起。当前定义了以下 ioctl：

`#include <sys/cpuctl.h>`

```sh
typedef struct {
	int		msr;	/* 要读取的 MSR */
	uint64_t	data;
} cpuctl_msr_args_t;
```

```sh
typedef struct {
	int		level;		/* CPUID 级别 */
	uint32_t	data[4];
} cpuctl_cpuid_args_t;
```

```sh
typedef struct {
	int		level;		/* CPUID 级别 */
	int		level_type;	/* CPUID 级别类型 */
	uint32_t	data[4];
} cpuctl_cpuid_count_args_t;
```

`#include <sys/cpuctl.h>`

```sh
typedef struct {
	void	*data;
	size_t	size;
} cpuctl_update_args_t;
```

**`CPUCTL_RDMSR`** `cpuctl_msr_args_t *args`

**`CPUCTL_WRMSR`** `cpuctl_msr_args_t *args` 读/写 CPU 机器特定寄存器。`cpuctl_msr_args_t` 结构定义如下：

**`CPUCTL_MSRSBIT`** `cpuctl_msr_args_t *args`

**`CPUCTL_MSRCBIT`** `cpuctl_msr_args_t *args` 根据 `data` 字段中给出的掩码设置/清除 MSR 位。

**`CPUCTL_CPUID`** `cpuctl_cpuid_args_t *args` 检索 CPUID 信息。参数在以下结构中提供：它等价于 `level_type` 设为 0 的 `CPUCTL_CPUID_COUNT` 请求。

**`CPUCTL_CPUID_COUNT`** `cpuctl_cpuid_count_args_t *args` 检索 CPUID 信息。参数在以下结构中提供：`level` 字段指示要检索的 CPUID 级别，在执行 CPUID 指令前将其加载到 `%eax` 寄存器中；`level_type` 字段指示要检索的 CPUID 级别类型，将其加载到 `%ecx` 寄存器中。`data` 字段用于存储接收到的 CPUID 数据。即 `data[0]` 包含执行 CPUID 指令后 `%eax` 寄存器的值，`data[1]` 对应 `%ebx`，`data[2]` 对应 `%ecx`，`data[3]` 对应 `%edx`。

**`CPUCTL_UPDATE cpuctl_update_args_t *args`** 更新 CPU 固件（微码）。该结构定义如下：`data` 字段应指向大小为 `size` 的固件映像。

有关更多信息，请参见 `cpuctl.h`。

## 文件

**`/dev/cpuctl`**

## 错误

**[Er** ENXIO] 设备不支持所请求的操作（例如，不受支持的架构或 CPU 已禁用）。

**[Er** EINVAL] 提供了不正确的请求，或微码映像不正确。

**[Er** ENOMEM] 没有可用的物理内存来完成请求。

**[Er** EFAULT] 固件映像地址指向进程地址空间之外。

## 参见

[hwpmc(4)](hwpmc.4.md), cpucontrol(8)

## 历史

`cpuctl` 驱动首次出现于 FreeBSD 7.2。

## 作者

`cpuctl` 模块及本手册页由 Stanislav Sedov <stas@FreeBSD.org> 编写。

## 缺陷

是的，可能存在，如有发现请报告。
