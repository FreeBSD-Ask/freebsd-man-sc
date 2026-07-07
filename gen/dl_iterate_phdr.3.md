# dl_iterate_phdr(3)

`dl_iterate_phdr` — 遍历程序头

## 名称

`dl_iterate_phdr`

## 库

对于动态链接的二进制文件，该服务由 ld-elf.so.1(1) 动态链接器提供。静态链接的程序使用 libc 中的 `dl_iterate_phdr()` 实现。

## 概要

```c
#include <link.h>

int
dl_iterate_phdr(int (*callback)(struct dl_phdr_info *, size_t, void *), void *data);
```

## 描述

`dl_iterate_phdr()` 函数遍历加载到进程地址空间中的所有 ELF 对象，为每个对象调用 `callback`，并向其传递有关该对象程序头的信息以及 `data` 参数。当所有对象都已传递完毕，或下一次 `callback` 调用返回非零值时，遍历终止。有关程序头的信息通过一个结构传递，该结构的定义如下：

```c
struct dl_phdr_info {
        Elf_Addr        dlpi_addr;
        const char      *dlpi_name;
        const Elf_Phdr  *dlpi_phdr;
        Elf_Half        dlpi_phnum;
        unsigned long long int dlpi_adds;
        unsigned long long int dlpi_subs;
        size_t          dlpi_tls_modid;
        void            *dlpi_tls_data;
};
```

`struct dl_phdr_info` 的成员具有以下含义：

**`dlpi_addr`** 对象映射到调用进程地址空间中的基地址。

**`dlpi_name`** 该 ELF 对象的路径名。

**`dlpi_phdr`** 指向该对象程序头的指针。

**`dlpi_phnum`** 该对象中程序头的数量。

**`dlpi_adds`** 动态链接器执行的对象加载计数器。

**`dlpi_subs`** 动态链接器执行的对象卸载计数器。

**`dlpi_tls_modid`** 该对象的 TLS 索引。

**`dlpi_tls_data`** 指向调用线程针对该模块的 TLS 数据段的指针（如果已分配），否则为 `NULL`。

未来版本的 FreeBSD 可能会向该结构添加更多成员。为了使程序能够检查是否添加了任何新成员，该结构的大小作为第二个参数传递给 `callback`。

callback 的第三个参数是传递给 `dl_iterate_phdr()` 调用的 `data` 值，从而使 `callback` 能够拥有上下文。

## 返回值

`dl_iterate_phdr()` 返回最后一次执行的 `callback` 调用所返回的值。

## 参见

ld(1), ld-elf.so.1(1), [dlopen(3)](dlopen.3.md), [elf(5)](../man5/elf.5.md)

## 历史

`dl_iterate_phdr` 函数首次出现在 FreeBSD 7.0。
