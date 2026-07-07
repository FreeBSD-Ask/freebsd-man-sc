# arc4random(3)

`arc4random` — 随机数生成器

## 名称

`arc4random`, `arc4random_buf`, `arc4random_uniform`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
uint32_t
arc4random(void);

void
arc4random_buf(void *buf, size_t nbytes);

uint32_t
arc4random_uniform(uint32_t upper_bound);
```

## 描述

此函数系列提供的数据质量高于 [rand(3)](../stdlib/rand.3.md)、[random(3)](../stdlib/random.3.md) 和 [rand48(3)](rand48.3.md) 中所述的函数。

几乎所有随机数使用场景都鼓励使用这些函数，因为其他接口在质量、可移植性、标准化或可用性方面存在不足。这些函数几乎可以在所有编程环境中调用，包括 [pthread(3)](../man3/pthread.3.md) 和 [chroot(2)](../sys/chroot.2.md)。

高质量的 32 位伪随机数生成速度非常快。每次调用时，都使用加密伪随机数生成器来生成新的结果。一个数据池供进程中的所有消费者使用，因此程序流下的使用可以作为额外的搅拌。子系统会定期使用 [getentropy(3)](getentropy.3.md) 从内核 [random(4)](../man4/random.4.md) 子系统重新播种，并在 [fork(2)](../sys/fork.2.md) 时也会重新播种。

`arc4random` 函数返回单个 32 位值。`arc4random` 函数返回 0 到 (2\*\*32)-1 范围内的伪随机数，因此其范围是 [rand(3)](../stdlib/rand.3.md) 和 [random(3)](../stdlib/random.3.md) 的两倍。

`arc4random_buf` 用随机数据填充长度为 `nbytes` 的区域 `buf`。

`arc4random_uniform` 将返回单个 32 位值，均匀分布但小于 `upper_bound`。建议使用此函数而非诸如 "`arc4random() % upper_bound`" 之类的构造，因为它避免了当上界不是 2 的幂时的"取模偏差"。在最坏的情况下，此函数可能会消耗多次迭代以确保均匀性；参见源代码以理解问题和解决方案。

## 返回值

这些函数始终成功，没有保留用于指示错误的返回值。

## 实例

以下代码使用 `arc4random` 生成传统 `rand` 和 `random` 函数的直接替换：

```c
#define foo4random() (arc4random_uniform(RAND_MAX + 1))
```

## 参见

[rand(3)](../stdlib/rand.3.md), [rand48(3)](rand48.3.md), [random(3)](../stdlib/random.3.md)

> Daniel J. Bernstein, "ChaCha, a variant of Salsa20", 2008-01-28, Document ID: 4027b5256e17b9796842e6d0f68b0b5e.

> Daniel Lemire, "Fast Random Integer Generation in an Interval", *ACM Trans. Model. Comput. Simul.*, vol. 29, no. 1, pp. 1-12, Association for Computing Machinery, January 2019.

## 历史

这些函数首次出现于 OpenBSD 2.1。`arc4random` 首次出现于 FreeBSD 3.0。`arc4random_buf` 和 `arc4random_uniform` 首次出现于 FreeBSD 8.0。`arc4random_stir` 在 FreeBSD 12.0 中被移除。

此随机数生成器的原始版本使用 RC4（也称为 ARC4）算法。在 OpenBSD 5.5 中，它被替换为 ChaCha20 密码，并且随着密码技术的进步，未来可能会再次被替换。一个很好的助记法是"A Replacement Call for Random"。

`arc4random` 随机数生成器首次引入于 FreeBSD 2.2.6。基于 ChaCha20 的实现引入于 FreeBSD 12.0，同时移除了过时的 stir 和 addrandom 接口。
