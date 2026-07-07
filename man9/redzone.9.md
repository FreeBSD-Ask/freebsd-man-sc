# redzone(9)

`RedZone` — 缓冲区损坏检测器

## 名称

`RedZone`

## 概要

```c
options KDB
options DDB
options DEBUG_REDZONE
```

## 描述

`RedZone` 在运行时检测缓冲区下溢和缓冲区溢出错误。目前，`RedZone` 仅检测使用 [malloc(9)](malloc.9.md) 分配的内存的缓冲区损坏。当检测到此类损坏时，会在控制台上打印两个回溯。第一个显示内存是从哪里分配的，第二个显示内存是从哪里释放的。默认情况下，检测到缓冲区损坏时系统不会 panic。可以通过将 `vm.redzone.panic` [sysctl(8)](../man8/sysctl.8.md) 变量设置为 1 来更改此行为。为 `RedZone` 需求分配的额外内存量存储在 `vm.redzone.extra_mem` [sysctl(8)](../man8/sysctl.8.md) 变量中。

## 实例

以下示例显示了检测到缓冲区下溢和缓冲区溢出时的日志。

```sh
REDZONE: Buffer underflow detected. 2 bytes corrupted before 0xc8688580 (16 bytes allocated).
Allocation backtrace:
#0 0xc0583e4e at redzone_setup+0x3c
#1 0xc04a23fa at malloc+0x19e
#2 0xcdeb69ca at redzone_modevent+0x60
#3 0xc04a3f3c at module_register_init+0x82
#4 0xc049d96a at linker_file_sysinit+0x8e
#5 0xc049dc7c at linker_load_file+0xed
#6 0xc04a041f at linker_load_module+0xc4
#7 0xc049e883 at kldload+0x116
#8 0xc05d9b3d at syscall+0x325
#9 0xc05c944f at Xint0x80_syscall+0x1f
Free backtrace:
#0 0xc0583f92 at redzone_check+0xd4
#1 0xc04a2422 at free+0x1c
#2 0xcdeb69a6 at redzone_modevent+0x3c
#3 0xc04a438d at module_unload+0x61
#4 0xc049e0b3 at linker_file_unload+0x89
#5 0xc049e979 at kern_kldunload+0x96
#6 0xc049ea00 at kldunloadf+0x2c
#7 0xc05d9b3d at syscall+0x325
#8 0xc05c944f at Xint0x80_syscall+0x1f
REDZONE: Buffer overflow detected. 4 bytes corrupted after 0xc8688590 (16 bytes allocated).
Allocation backtrace:
#0 0xc0583e4e at redzone_setup+0x3c
#1 0xc04a23fa at malloc+0x19e
#2 0xcdeb69ca at redzone_modevent+0x60
#3 0xc04a3f3c at module_register_init+0x82
#4 0xc049d96a at linker_file_sysinit+0x8e
#5 0xc049dc7c at linker_load_file+0xed
#6 0xc04a041f at linker_load_module+0xc4
#7 0xc049e883 at kldload+0x116
#8 0xc05d9b3d at syscall+0x325
#9 0xc05c944f at Xint0x80_syscall+0x1f
Free backtrace:
#0 0xc0584020 at redzone_check+0x162
#1 0xc04a2422 at free+0x1c
#2 0xcdeb69a6 at redzone_modevent+0x3c
#3 0xc04a438d at module_unload+0x61
#4 0xc049e0b3 at linker_file_unload+0x89
#5 0xc049e979 at kern_kldunload+0x96
#6 0xc049ea00 at kldunloadf+0x2c
#7 0xc05d9b3d at syscall+0x325
#8 0xc05c944f at Xint0x80_syscall+0x1f
```

## 参见

[sysctl(8)](../man8/sysctl.8.md), [malloc(9)](malloc.9.md), [memguard(9)](memguard.9.md)

## 历史

`RedZone` 首次出现在 FreeBSD 7.0 中。

## 作者

Pawel Jakub Dawidek <pjd@FreeBSD.org>

## 缺陷

目前，`RedZone` 不与 [memguard(9)](memguard.9.md) 协作。来自由 [memguard(9)](memguard.9.md) 控制的内存类型的分配将被直接跳过，因此在那里不会检测到缓冲区损坏。
