# prng.9

`prng` — 内核伪随机数生成器

## 名称

`prng`

## 概要

```c
#include <sys/prng.h>
```

```c
uint32_t
prng32(void)

uint32_t
prng32_bounded(uint32_t bound)

uint64_t
prng64(void)

uint64_t
prng64_bounded(uint64_t bound)
```

## 描述

### 通用 PRNG 例程

`prng` 是一系列快速、*非加密* 伪随机数生成器。与 [random(9)](random.9.md) 不同，`prng32`、`prng32_bounded`、`prng64` 和 `prng64_bounded` 避免使用共享全局状态，消除了 SMP 系统上不必要的争用。这些例程未显式绑定到任何特定实现，可能在不同的主机、重启或 FreeBSD 版本上产生不同的特定序列。SMP 系统中的不同 CPU 保证产生不同的整数序列。

有关由 [random(4)](../man4/random.4.md) 内核加密安全随机数生成器子系统生成的*加密安全*随机数，请参见 arc4random(9)。

**`prng32`** 生成均匀分布在 [0, 2^32-1] 范围内的 32 位整数。

**`prng32_bounded`** `bound` 生成均匀分布在 [0, bound-1] 范围内的整数。

**`prng64`** 生成均匀分布在 [0, 2^64-1] 范围内的 64 位整数。

**`prng64_bounded`** `bound` 生成均匀分布在 [0, bound-1] 范围内的整数。

这些例程不可重入；在中断处理程序（bus_setup_intr(9) 术语中的“中断过滤器”）中使用它们不安全。它们可在所有其他内核上下文中安全使用，包括中断线程（“ithreads”）。

### 可重现 PRNG API

除了这些每 CPU 辅助函数外，

```c
#include <sys/prng.h>
```

头文件还以内联函数形式公开了 PCG 系列 PRNG 的整个 API。PCG-C API 在 <https://www.pcg-random.org/using-pcg-c.html> 中有完整描述。

## 历史

`prng` 在 FreeBSD 13 中引入。
