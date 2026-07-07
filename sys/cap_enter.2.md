# cap_enter(2)

`cap_enter` — capability mode 系统调用

## 名称

`cap_enter`, `cap_getmode`

## 库

Lb libc

## 概要

`#include <sys/capsicum.h>`

```c
int
cap_enter(void);

int
cap_getmode(u_int *modep);
```

## 描述

`cap_enter()` 将当前进程置入 capability mode，这是一种执行模式，进程在此模式下只能发起作用于文件描述符或读取有限全局系统状态的系统调用。禁止访问诸如文件系统或 IPC 命名空间之类的全局命名空间。如果进程已处于 capability mode 沙盒中，则该系统调用为空操作。未来通过 [fork(2)](fork.2.md) 或 [pdfork(2)](pdfork.2.md) 创建的进程后代将从起始时即处于 capability mode。

将 `cap_enter()` 与 [cap_rights_limit(2)](cap_rights_limit.2.md)、[cap_ioctls_limit(2)](cap_ioctls_limit.2.md)、[cap_fcntls_limit(2)](cap_fcntls_limit.2.md) 配合使用，可创建由内核强制执行的沙盒，在其中运行经过适当编写的应用程序或应用程序组件。

`cap_getmode()` 返回一个标志，指示进程是否处于 capability mode 沙盒中。

## 运行时设置

如果将 `kern.trap_enotcap` sysctl MIB 设置为非零值，则对于在 capability mode 沙盒中执行的任何进程，任何导致 `ENOTCAPABLE` 或 `ECAPMODE` 错误的系统调用还会在该系统调用返回时向线程发送同步 `SIGTRAP` 信号。在信号传递时，`siginfo` 信号处理程序参数的 `si_errno` 成员被设置为系统调用错误值，`si_code` 成员被设置为 `TRAP_CAP`。

关于类似的逐进程功能，另请参见 [procctl(2)](procctl.2.md) 函数的 `PROC_TRAPCAP_CTL` 和 `PROC_TRAPCAP_STATUS` 操作。

## 返回值

成功完成时，`cap_enter()` 和 `cap_getmode()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

当进程处于 capability mode 时，`cap_getmode()` 将标志设置为非零值。值为零表示进程未处于 capability mode。

## 错误

`cap_enter()` 和 `cap_getmode()` 系统调用在以下情况下会失败：

**[`ENOSYS`]** 运行中的内核编译时未包含 `options CAPABILITY_MODE`。

`cap_getmode()` 系统调用还可能返回以下错误：

**[`EFAULT`]** 指针 `modep` 指向进程所分配地址空间之外。

## 参见

[cap_fcntls_limit(2)](cap_fcntls_limit.2.md), [cap_ioctls_limit(2)](cap_ioctls_limit.2.md), [cap_rights_limit(2)](cap_rights_limit.2.md), fexecve(2), [procctl(2)](procctl.2.md), cap_sandboxed(3), [capsicum(4)](../man4/capsicum.4.md), [sysctl(9)](../man9/sysctl.9.md)

## 历史

`cap_getmode()` 系统调用首次出现于 FreeBSD 8.3。对 capabilities 和 capabilities mode 的支持是作为 TrustedBSD 项目的一部分开发的。

## 作者

这些函数和 capability 功能由 Robert N. M. Watson 在剑桥大学计算机实验室创建，并得到了 Google, Inc. 的资助。

## 注意事项

创建有效的进程沙盒是一个棘手的过程，需要识别进程所需的尽可能少的权限，然后以安全的方式将这些权限传递给进程。`cap_enter()` 的使用者还应留意其他继承的权限，例如对 VM 资源、内存内容以及其他应予考虑的进程属性的访问。建议使用 fexecve(2) 在沙盒内部创建一个运行时环境，使其隐式获取的权限尽可能少。
