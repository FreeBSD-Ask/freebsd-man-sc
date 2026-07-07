# kvm(3)

`kvm` — 内核内存接口

## 名称

`kvm`

## 库

Lb libkvm

## 描述

`kvm` 库为访问内核虚拟内存映像（包括运行中的系统和崩溃转储）提供统一接口。对运行中系统的访问，部分函数通过 [sysctl(3)](sysctl.3.md) 实现，其他函数通过 [mem(4)](../man4/mem.4.md) 和 kmem(4) 实现；而崩溃转储可通过 savecore(8) 生成的核心文件进行检查。两种情况下接口的行为类似。可以读写内存、高效查找内核符号地址，并收集有关用户进程的信息。

首先调用 `kvm_open` 函数获取一个描述符，供后续所有调用使用。

## 兼容性

kvm 接口最初在 SunOS 中引入。已有大量程序使用此接口开发，因此向后兼容性极受重视。在大多数方面，Sun 的 kvm 接口是一致且简洁的。因此，该接口的通用部分（即 `kvm_open`、`kvm_close`、`kvm_read`、`kvm_write` 和 `kvm_nlist`）已被纳入 BSD 接口。实际上，许多 kvm 应用程序（即调试器和统计监视器）仅使用此接口的子集。

未保留进程接口。这不属于可移植性问题，因为任何操作进程的代码本质上都依赖于机器体系结构。

最后，Sun 的 kvm 错误报告语义定义不明确。该库可配置为自动将错误打印到 `stderr`，也可配置为完全不打印错误消息。在后一种情况下，无法确定错误的性质。为克服此问题，BSD 接口包含一个例程 kvm_geterr(3)，用于返回（而非打印）与给定描述符上最近一次错误条件相对应的错误消息。

## 交叉调试

`kvm` 库支持检查来自非原生内核的崩溃转储。此类转储仅支持 kvm 接口的一个有限子集。要检查非原生内核的崩溃转储，调用者必须在通过 `kvm_open2` 打开描述符时提供一个 `resolver` 函数。此外，kvm 接口定义了一个整数类型（`kvaddr_t`），其大小足以容纳所有支持体系结构的所有有效地址。该接口还为 `kvm_nlist2` 定义了一个新的名称列表结构类型（`struct kvm_nlist`）。为避免地址截断问题，调用者应分别使用 `kvm_nlist2` 和 `kvm_read2` 替代 `kvm_nlist` 和 `kvm_read`。最后，非原生崩溃转储仅支持有限的一组操作：`kvm_close`、`kvm_geterr`、`kvm_kerndisp`、`kvm_open2`、`kvm_native`、`kvm_nlist2` 和 `kvm_read2`。

## 参见

kvm_close(3), kvm_getargv(3), kvm_getenvv(3), kvm_geterr(3), kvm_getloadavg(3), kvm_getprocs(3), kvm_getswapinfo(3), kvm_kerndisp(3), kvm_native(3), kvm_nlist(3), kvm_nlist2(3), kvm_open(3), kvm_open2(3), kvm_openfiles(3), kvm_read(3), kvm_read2(3), kvm_write(3), [sysctl(3)](sysctl.3.md), kmem(4), [mem(4)](../man4/mem.4.md)

## 历史

`kvm_native`、`kvm_nlist2`、`kvm_open2` 和 `kvm_read2` 函数首次出现在 FreeBSD 11.0 中。
