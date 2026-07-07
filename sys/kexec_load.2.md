# kexec_load(2)

`kexec_load` — 准备新内核以供重启进入

## 名称

`kexec_load`

## 库

Lb libc

## 概要

```c
#include <sys/kexec.h>

int
kexec_load(uint64_t entry, unsigned long count,
    struct kexec_segment *segments, unsigned long flags);
```

## 描述

`kexec_load()` 系统调用加载一个新内核，该内核可在稍后通过 [reboot(2)](reboot.2.md) 执行。后续调用将替换先前加载的映像。

`flags` 参数是控制调用操作的标志位掩码。此参数为了与 Linux 兼容而保留，但目前未使用，必须为 0。

`entry` 参数是新内核映像入口点的物理地址。

`count` 参数是映像中的段数，目前限制为 16。值为 0 将卸载当前已暂存的映像（如果存在），而不暂存新映像。

`segments` 参数是包含 `count` 个以下结构成员的数组：

```c
struct  kexec_segment {
    void *buf;
    size_t bufsz;
    vm_paddr_t mem;
    vm_size_t memsz;
};
```

`buf` 和 `bufsz` 成员指定调用者地址空间中包含段源的内存区域。`mem` 和 `memsz` 成员指定段的目标物理区域。`bufsz` 必须小于或等于 `memsz`，且 `mem` 和 `memsz` 必须页对齐。`mem` 所覆盖的区域必须在 `vm.phys_segs` sysctl 所覆盖的列表中。

`kexec_load()` 系统调用将内核映像连同所有机器相关的映像数据暂存到安全内存中，直到以 `RB_KEXEC` 标志调用 [reboot(2)](reboot.2.md) 来加载映像并执行新内核。

## 返回值

`kexec_load()` 系统调用成功时返回 0。失败时返回 -1，并设置 `errno` 以指示错误。成功时，任何先前加载的映像将被卸载并替换为新映像。失败时，先前加载的映像保持不变。

## 错误

可能返回以下错误：

**[EINVAL]** 映像中的段过多。

**[EINVAL]** 一个或多个段中 `bufsz` 的值大于 `memsz`。

**[EINVAL]** 机器相关的加载错误。

**[EBUSY]** 另一个 `kexec_load()` 调用正在进行中。

## 历史

`kexec_load` 系统调用首次出现于 FreeBSD 16.0。