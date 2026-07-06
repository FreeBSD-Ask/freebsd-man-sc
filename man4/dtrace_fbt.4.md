# dtrace_fbt.4

`dtrace_fbt` — 基于函数边界的动态内核跟踪 DTrace 提供者

## 名称

`dtrace_fbt`

## 概要

`fbt:module:function:entry fbt:module:function:return`

## 描述

函数边界跟踪（Function Boundary Tracing，`fbt`）提供者检测内核和已加载内核模块中对应于 [elf(5)](../man5/elf.5.md) 符号的几乎所有内核函数的入口和返回。

`fbt``:``module``:``function``:entry` 在 `function` 被调用时触发。`fbt``:``module``:``function``:return` 在 `function` 返回时触发。

探测描述中的 `module` 是已加载内核模块的名称，对于编译进内核的函数则为 `kernel`。

### 函数边界检测

`fbt` 始终会检测函数的入口，但其返回仅在能找到 `ret` 指令时才被检测。

在某些情况下，`fbt` 无法检测函数的入口和/或返回。有关更多详情，请参见 Sx Frame Pointer 小节。

### 探测参数

入口探测（`fbt``:``module``:``function``:entry`）的参数是被跟踪函数调用的参数。

（例如，[malloc(9)](../man9/malloc.9.md) 的 `size`）

（例如，[malloc(9)](../man9/malloc.9.md) 的 `*type`）

（例如，[malloc(9)](../man9/malloc.9.md) 的 `flags`）

| **入口探测参数** | **定义** |
| ---------------- | -------- |
| `args[0]` | 函数的第一个参数，带类型 |
| `args[1]` | 函数的第二个参数，带类型 |
| `args[2]` | 函数的第三个参数，带类型 |
| `...` | ... |

返回探测（`fbt``:``module``:``function``:return`）的参数为 `args[0]`（触发的返回指令在函数内的偏移；用于区分单个函数中的两个不同返回语句）和 `args[1]`（返回值，如果有）。

（例如，从成功的 [malloc(9)](../man9/malloc.9.md) 返回时的内核虚拟地址）

| **返回探测参数** | **定义** |
| ---------------- | -------- |
| `args[0]` | 被跟踪返回指令的偏移 |
| `args[1]` | 函数的返回值 |

Sx Example 2 : Getting Details About Probe's Arguments 小节展示了如何直接使用 [dtrace(1)](../man1/dtrace.1.md) 获取探测的参数数量和类型，而无需查阅函数的源代码或文档。

## 实例

### 实例 1：列出可用的 FBT 探测

以下示例展示如何列出所有可用的 `fbt` 探测。

```sh
# dtrace -l -P fbt
   ID   PROVIDER     MODULE              FUNCTION NAME
[...]
31868        fbt     kernel           hammer_time entry
31869        fbt     kernel           hammer_time return
[...]
```

由于 Fn hammer_time 是内核的一部分而非单独的已加载模块，`module` 列显示为 `kernel`。

### 实例 2：获取探测参数的详情

以下示例展示如何生成 [malloc(9)](../man9/malloc.9.md) 入口和返回探测的程序稳定性报告。此类报告有助于查看探测的参数数量及其类型。

```sh
# dtrace -l -v -n fbt::malloc:entry
[...]
        Argument Types
                args[0]: size_t
                args[1]: struct malloc_type *
                args[2]: int
```

`fbt``::malloc:entry` 参数的数量和类型与 [malloc(9)](../man9/malloc.9.md) 的函数签名匹配：`args[0]` 为 Ft size_t，`args[1]` 为 Ft struct malloc_type *，`args[2]` 为 Ft int。

```sh
# dtrace -l -v -n fbt::malloc:return
[...]
        Argument Types
                args[0]: int
                args[1]: void *
```

`return` 探测报告两个参数及其类型：返回指令偏移（通常为 Ft int）和函数的返回值，此例中为 Ft void *，因为 [malloc(9)](../man9/malloc.9.md) 返回内核虚拟地址。

### 实例 3：按函数统计内核 Slab 内存分配

```sh
# dtrace -n 'fbt::kmem*:entry { @[probefunc] = count(); }'
dtrace: description 'fbt::kmem*:entry ' matched 47 probes
^C
  kmem_alloc_contig                                     1
  kmem_alloc_contig_domainset                           1
  kmem_cache_reap_active                                1
  kmem_alloc_contig_pages                               2
  kmem_free                                             2
  kmem_std_destructor                                  19
  kmem_std_constructor                                 26
  kmem_cache_free                                     151
  kmem_cache_alloc                                    181
```

### 实例 4：按调用函数统计内核 Slab 内存分配

```sh
# dtrace -q -n 'fbt::kmem*:entry { @[caller] = count(); } END { printa("%40a %@16den", @); }'
^C
                kernel`contigmalloc+0x33                1
                        kernel`free+0xd3                1
           kernel`kmem_alloc_contig+0x29                1
kernel`kmem_alloc_contig_domainset+0x19a                1
           zfs.ko`arc_reap_cb_check+0x16                1
```

### 实例 5：按调用函数统计内核 malloc() 调用

```sh
# dtrace -q -n 'fbt::malloc:entry { @[caller] = count(); } END { printa("%45a %@16den", @); }'
^C
        kernel`devclass_get_devices+0xa8                1
                   kernel`sys_ioctl+0xb7                1
           dtrace.ko`dtrace_ioctl+0x15c1                1
            dtrace.ko`dtrace_ioctl+0x972                2
        dtrace.ko`dtrace_dof_create+0x35                2
             kernel`kern_poll_kfds+0x2f0                4
             kernel`kern_poll_kfds+0x28a               19
```

### 实例 6：按内核栈回溯统计内核 malloc() 调用

```sh
# dtrace -q -n 'fbt::malloc:entry { @[stack()] = count(); }'
^C
              dtrace.ko`dtrace_dof_create+0x35
              dtrace.ko`dtrace_ioctl+0x827
              kernel`devfs_ioctl+0xd1
              kernel`VOP_IOCTL_APV+0x2a
              kernel`vn_ioctl+0xb6
              kernel`devfs_ioctl_f+0x1e
              kernel`kern_ioctl+0x286
              kernel`sys_ioctl+0x12f
              kernel`amd64_syscall+0x169
              kernel`0xffffffff81092b0b
                2
```

### 实例 7：按竞技场名称和大小分布汇总 vmem_alloc() 调用

```sh
# dtrace -q -n 'fbt::vmem_alloc:entry { @[args[0]->vm_name] = quantize(arg1); }'
^C
  kernel arena dom
           value  ------------- Distribution ------------- count
            2048 |                                         0
            4096 |@@@@@@@@@@@@@@@@@@@@@@@@@@@              4
            8192 |@@@@@@@@@@@@@                            2
           16384 |                                         0
```

### 实例 8：测量执行函数所花费的总时间

此 DTrace 脚本测量在 Fn vm_page* 内核函数中花费的总时间。Fn quantize 聚合将测量结果组织到 2 的幂次桶中，为每个函数提供以纳秒为单位的时间分布。

```sh
fbt::vm_page*:entry {
    self->start = timestamp;
}
fbt::vm_page*:return /self->start/ {
    @[probefunc] = quantize(timestamp - self->start);
    self->start = 0;
}
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_kinst(4)](dtrace_kinst.4.md), [tracing(7)](../man7/tracing.7.md)

> Brendan Gregg, Jim Mauro, *DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and FreeBSD*, pp. pp. 898-903, Prentice Hall, 2011.

> *The illumos Dynamic Tracing Guide*, 2008, Chapter fbt Provider.

## 作者

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。

## 注意事项

### 稳定性与可移植性

`fbt` 探测按定义与内核代码紧密耦合；如果脚本底层的代码发生变化，脚本可能无法运行或产生不正确的结果。为某一版本 FreeBSD 编写的脚本可能无法在其他版本上运行，且几乎肯定无法在其他操作系统上运行。

单个 `fbt` 探测通常不能很好地对应到逻辑系统事件。例如，考虑一个 DTrace 脚本，在内核将每个 IP 数据包交给网卡驱动（NIC）时打印其目标地址。基于 `fbt` 实现此类脚本是一项令人沮丧的困难任务：它涉及在 IPv4 和 IPv6 代码的不同部分检测至少四个不同的函数。同时，使用 [dtrace_ip(4)](dtrace_ip.4.md) 提供者，该脚本只需简单的一行：

```sh
dtrace -n 'ip:::send {printf("%s", args[2]->ip_daddr);}'
```

在用 `fbt` 提供者实现自定义脚本之前，请务必先查看可用的 [dtrace(1)](../man1/dtrace.1.md) 提供者。如果没有任何 DTrace 提供者提供所需的探测，请考虑添加新的静态定义跟踪探测（[SDT(9)](../man9/sdt.9.md)）。

### 帧指针

内联函数无法被 `fbt` 检测，因为它们没有帧指针。开发者可以通过在函数定义中添加 `__noinline` 属性来显式禁用内联，但这当然需要重新编译内核。使用 `-fno-omit-frame-pointer` 构建内核是保留帧指针的另一种方法。注意，有时编译器会在叶函数中省略帧指针，即使配置了 `-fno-omit-frame-pointer`。

通过尾调用进行的函数返回也无法被 `fbt` 检测。因此，一个函数可能有一个入口探测和一组混合的已检测与不可检测的返回。

使用 [dtrace_kinst(4)](dtrace_kinst.4.md) 跟踪内核函数内的任意指令，以解决 `fbt` 的某些限制。

### 跟踪 DTrace

`fbt` 提供者无法附加到 DTrace 提供者内核模块内的函数。
