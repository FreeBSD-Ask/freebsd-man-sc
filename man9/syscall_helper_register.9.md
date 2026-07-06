# syscall_helper_register.9

`syscall_helper_register` — 内核系统调用注册例程

## 名称

`syscall_helper_register`, `syscall_helper_unregister`

## 概要

```c
#include <sys/sysent.h>

int
syscall_helper_register(struct syscall_helper_data *sd, int flags)

int
syscall_helper_unregister(struct syscall_helper_data *sd)
```

### 初始化器宏

```c
struct syscall_helper_data
SYSCALL_INIT_HELPER(syscallname)

struct syscall_helper_data
SYSCALL_INIT_HELPER_F(syscallname, int flags)
```

### 兼容性初始化器宏

```c
struct syscall_helper_data
SYSCALL_INIT_HELPER_COMPAT(syscallname)

struct syscall_helper_data
SYSCALL_INIT_HELPER_COMPAT_F(syscallname, int flags)
```

## 描述

`syscall_helper_register` 注册一个系统调用。此函数接受结构 `struct syscall_helper_data sd`，该结构指定系统调用注册的参数：

```c
struct syscall_helper_data {
	struct sysent	new_sysent;
	struct sysent	old_sysent;
	int		syscall_no;
	int		registered;
};
```

`syscall_helper_register` 的 `flags` 参数的唯一有效标志是 `SY_THR_STATIC`。此标志防止系统调用被注销。

使用前，结构必须使用 `SYSCALL_INIT_HELPER*` 宏之一初始化。在新代码中，系统调用实现函数应命名为 `sys_syscallname` 并使用常规宏。

对于没有 "sys_" 前缀的旧版系统调用函数，可以使用宏的 "COMPAT" 版本。

初始化器宏的 "F" 变体的 `flags` 参数的唯一有效标志是 `SYF_CAPENABLED`。此标志指示系统调用允许在能力模式下使用。

`syscall_helper_unregister` 注销系统调用。此函数接受与上述方式先前初始化的相同结构 `struct syscall_helper_data sd`，并用于成功调用 `syscall_helper_register`。

## 返回值

如果成功，`syscall_helper_register` 和 `syscall_helper_unregister` 将返回 0。否则返回错误。

## 错误

`syscall_helper_register` 调用将失败且系统调用不会注册，如果：

`EINVAL` `flags` 参数包含 `SY_THR_STATIC` 以外的值。

`EINVAL` 指定的系统调用号 `sd.syscall_no`（`SYS_syscallname`）超出有效系统调用号范围（零到 `SYS_MAXSYSCALL`）。

`ENFILE` 系统调用表没有可用的槽位。

`EEXIST` 指定的系统调用号 `sd.syscall_no`（`SYS_syscallname`）已被使用。

## 参见

[SYSCALL_MODULE(9)](SYSCALL_MODULE.9.md)
