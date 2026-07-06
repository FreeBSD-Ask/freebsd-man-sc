# bios.9

`bios_sigsearch` — 与 PC BIOS 交互

## 名称

`bios_sigsearch`, `bios32_SDlookup`, `bios32`, `bios_oem_strings`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/pmap.h>
#include <machine/pc/bios.h>

uint32_t
bios_sigsearch(uint32_t start, u_char *sig, int siglen, int paralen,
    int sigofs)

int
bios32_SDlookup(struct bios32_SDentry *ent)

int
bios32(struct bios_regs *br, u_int offset, u_short segment)

BIOS_PADDRTOVADDR(addr)
BIOS_VADDRTOPADDR(addr)

extern struct bios32_SDentry PCIbios;
extern struct SMBIOS_table SMBIOStable;
extern struct DMI_table DMItable;

int
bios_oem_strings(struct bios_oem *oem, u_char *buffer, size_t maxlen)
```

```c
struct bios_oem_signature {
        char * anchor;          /* 在 BIOS 内存中搜索锚字符串 */
        size_t offset;          /* 从锚的偏移量（可为负） */
        size_t totlen;          /* 要复制的 BIOS 字符串总长度 */
};
struct bios_oem_range {
        u_int from;             /* 不应低于 0xe0000 */
        u_int to;               /* 不应高于 0xfffff */
};
struct bios_oem {
        struct bios_oem_range range;
        struct bios_oem_signature signature[];
};
```

## 描述

这些函数提供了处理 x86 PC 架构系统中遇到的 BIOS 功能和数据的通用接口。

**`bios_sigsearch`** 在 BIOS 地址空间中搜索服务签名，通常是由下划线包围的大写 ASCII 序列。搜索从 `start` 开始，如果 `start` 为零则从 BIOS 开头开始。在距当前位置 `sigofs` 字节偏移处比较 BIOS 映像的 `siglen` 字节与 `sig`。如果未找到匹配，当前位置递增 `paralen` 字节并重复搜索。如果找到签名，返回其有效物理地址。如果未找到签名，返回零。

**`bios_oem_strings`** 在给定 BIOS 内存范围内搜索一个或多个字符串，并组合找到的字符串的可打印连接。该例程需要一个描述 BIOS 地址 `range`（在 **0xe0000** - **0xfffff** 内）的结构，以及一个以 { `NULL`, `0, 0` } 终止的 `bios_oem_signature` 结构数组，这些结构定义 `anchor` 字符串、从匹配开始的 `offset`（可为负），以及从该偏移量开始从 BIOS 内存收集的 `totlen` 字节数。未匹配的锚被忽略，而匹配项从 BIOS 内存中对应的 `offset` 开始复制，不可打印字符替换为空格，连续空格被抑制。此组合字符串存储在 `buffer` 中，最多 `maxlen` 字节（包括尾部的 '\0'，并抑制任何尾部空格）。如果遇到错误，即尝试读取所述 BIOS 范围之外、其他无效输入或 `buffer` 溢出，返回负整数，否则返回组合字符串的长度。特别是，返回值 0 表示在指定 BIOS 内存范围内未找到任何给定的锚字符串。

**`BIOS_VADDRTOPADDR`** 返回对应于内核虚拟地址 `addr` 的有效物理地址。

**`BIOS_PADDRTOVADDR`** 返回对应于有效物理地址 `addr` 的内核虚拟地址。

**`SMBIOStable`** 如果不为 NULL，指向一个 `struct SMBIOS_table` 结构，包含系统启动时从系统管理 BIOS 表读取的信息。

**`DMItable`** 如果不为 NULL，指向一个 `struct DMI_table` 结构，包含系统启动时从桌面管理接口参数表读取的信息。

## BIOS32

系统启动时，扫描 BIOS 以查找 BIOS32 服务目录（PCI 规范的一部分），并记录目录的存在。然后可用于定位其他服务。

**`bios32_SDlookup`** 尝试定位匹配 `ent` 参数的 `ident` 字段中传递的 4 字节标识符的 BIOS32 服务。

**`bios32`** 调用 bios32 函数。这假定该函数能够在内核段内工作（通常如此）。入口点的虚拟地址在 `entry` 中提供，函数的寄存器参数在 `args` 中提供。

**`PCIbios`** 如果不为 NULL，指向一个 `struct bios32_SDentry` 结构，描述系统启动时找到的 PCI BIOS 入口点。
