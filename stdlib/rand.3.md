# rand(3)

`rand` — 糟糕的随机数生成器

## 名称

`rand`, `rand_r`, `srand`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
rand(void);

int
rand_r(unsigned *ctx);

void
srand(unsigned seed);
```

## 描述

> **注意**：本手册页中所述的函数不具备加密安全性。需要不可预测随机数的应用应改用 [arc4random(3)](../gen/arc4random.3.md)。

`rand` 函数计算 0 到 `RAND_MAX`（含）范围内的伪随机整数序列。

`srand` 函数使用 `seed` 参数为算法设置种子。通过以相同的 `seed` 调用 `srand`，可获得可重复的 `rand` 输出序列。`rand` 在初始化时隐式执行了相当于显式调用 `srand(1)` 的操作。

在 FreeBSD 13 中，`rand` 采用与 [random(3)](random.3.md) 相同的 128 字节状态 LFSR 生成器算法实现。然而，旧的 `rand_r` 函数并非如此（且由于 `*ctx` 大小有限，也无法如此）。`rand_r` 实现的是历史上质量较差的 Park-Miller 32 位 LCG 算法，不应在新设计中使用。

## 实现说明

自 FreeBSD 13 起，`rand` 采用与 [random(3)](random.3.md) 相同的生成器实现，因此低位不再明显比高位差。

## 参见

[arc4random(3)](../gen/arc4random.3.md), [random(3)](random.3.md), [random(4)](../man4/random.4.md)

## 标准

`rand` 和 `srand` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

`rand_r` 函数不属于 ISO/IEC 9899:1990 ("ISO C89")，在 IEEE Std 1003.1-2008 ("POSIX.1") 中被标记为过时。它可能会在未来的 POSIX 修订版中被移除。

## 注意事项

在 FreeBSD 13 之前，`rand` 使用历史上的 Park-Miller 生成器，仅有 32 位状态，产生的输出质量较差，低位尤其如此。早期版本的 FreeBSD 以及其他遵循标准的实现中的 `rand` 可能继续产生质量较差的输出。

**这些函数不应在需要高质量或高性能伪随机数生成器的可移植应用中使用。** 一个可能的替代方案是 [random(3)](random.3.md)，它可移植到 Linux——但它既不是特别快，也未被标准化。

如果需要更广泛的可移植性或更好的性能，可以将任何广泛可用且许可宽松的 SFC64/32、JSF64/32、PCG64/32 或 SplitMix64 算法实现嵌入到你的应用中。这些算法的优势在于比 [random(3)](random.3.md) 占用更少的空间，并且速度相当快（在头文件内联实现中）。
