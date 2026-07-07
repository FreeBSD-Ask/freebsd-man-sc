# random(3)

`random` — 非加密伪随机数生成器；用于更换生成器的例程

## 名称

`random`, `srandom`, `srandomdev`, `initstate`, `setstate`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
long
random(void);

void
srandom(unsigned int seed);

void
srandomdev(void);

char *
initstate(unsigned int seed, char *state, size_t n);

char *
setstate(char *state);
```

## 描述

> **注意**：本手册页中所述的函数不具备安全性。需要不可预测随机数的应用应改用 [arc4random(3)](../gen/arc4random.3.md)。

除非以少于 32 字节的状态初始化，`random` 函数使用非线性加法反馈随机数生成器，采用 31 个长整数的默认表，返回 0 到 2^31-1 范围内的连续伪随机数。该随机数生成器的周期非常大，约为 16×(2^31-1)。

如果以少于 32 字节的状态初始化，`random` 使用质量较差的 32 位 Park-Miller LCG。

`random` 和 `srandom` 函数类似于 [rand(3)](rand.3.md) 和 [srand(3)](rand.3.md)。

与 [rand(3)](rand.3.md) 类似，`random` 在初始化时隐式执行了相当于显式调用 `srandom(1)` 的操作。

`srandomdev` 例程使用从内核获取的随机数初始化状态数组。这能够生成通过调用 `srandom` 无法重现的状态，因为状态缓冲区中的后续项不再由应用于固定种子的 Park-Miller LCG 算法派生。

`initstate` 例程初始化所提供的由 `uint32_t` 值组成的状态数组，并在将来的 `random` 调用中使用它。（尽管 `state` 的类型为 `char *`，底层对象必须是一个自然对齐的 32 位值数组。）状态数组的大小（以字节为单位）由 `initstate` 用于决定使用多复杂的随机数生成器——状态越多，随机数质量越好。（当前状态信息量的“最优”值为 8、32、64、128 和 256 字节；其他值将向下取整到最近的已知值。使用少于 8 字节将导致错误。）`seed` 的用法与 `srandom` 中相同。`initstate` 函数返回指向先前状态信息数组的指针。

`setstate` 例程将 `random` 切换为使用所提供的状态。它返回指向先前状态的指针。

一旦状态数组被初始化，可以通过调用 `initstate`（使用所需的种子、状态数组及其大小）或同时调用 `setstate`（使用状态数组）和 `srandom`（使用所需的种子）从不同的点重新启动。同时调用 `setstate` 和 `srandom` 的优势在于，状态数组初始化后无需记住其大小。

使用 256 字节的状态信息时，随机数生成器的周期大于 2^69，对大多数用途而言应已足够。

## 诊断

如果 `initstate` 被调用时状态信息少于 8 字节，或 `setstate` 检测到状态信息已被破坏，将返回 `NULL`。

## 参见

[arc4random(3)](../gen/arc4random.3.md), [lrand48(3)](../gen/rand48.3.md), [rand(3)](rand.3.md), [random(4)](../man4/random.4.md)

## 历史

这些函数出现于 4.2BSD。

## 作者

Earl T. Cohen
