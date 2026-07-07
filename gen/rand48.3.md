# rand48(3)

`drand48` — 伪随机数生成器和初始化例程

## 名称

`drand48`, `erand48`, `lrand48`, `nrand48`, `mrand48`, `jrand48`, `srand48`, `seed48`, `lcong48`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
double
drand48(void);

double
erand48(unsigned short xseed[3]);

long
lrand48(void);

long
nrand48(unsigned short xseed[3]);

long
mrand48(void);

long
jrand48(unsigned short xseed[3]);

void
srand48(long seed);

unsigned short *
seed48(unsigned short xseed[3]);

void
lcong48(unsigned short p[7]);
```

## 描述

> **注意** 本手册页中描述的函数不是加密安全的。加密应用程序应改用 [arc4random(3)](arc4random.3.md)。

`rand48` 系列函数使用对 48 位整数进行运算的线性同余算法生成伪随机数。所采用的特定公式为 r(n+1) = (a * r(n) + c) mod m，其中默认值为乘数 a = 0x5deece66d = 25214903917，加数 c = 0xb = 11。模数始终固定为 m = 2 ** 48。r(n) 称为随机数生成器的种子。

对于下文描述的六个生成器例程，第一个计算步骤都是执行算法的一次迭代。

`drand48` 和 `erand48` 函数返回 double 类型的值。r(n+1) 的完整 48 位被加载到返回值的尾数中，指数设置为使生成的值位于区间 [0.0, 1.0) 内。

`lrand48` 和 `nrand48` 函数返回 long 类型的值，范围在 [0, 2**31-1] 内。r(n+1) 的高 31 位被加载到返回值的低位中，最高（符号）位设置为零。

`mrand48` 和 `jrand48` 函数返回 long 类型的值，范围在 [-2**31, 2**31-1] 内。r(n+1) 的高 32 位被加载到返回值中。

`drand48`、`lrand48` 和 `mrand48` 函数使用内部缓冲区存储 r(n)。对于这些函数，初始值 r(0) = 0x1234abcd330e = 20017429951246。

另一方面，`erand48`、`nrand48` 和 `jrand48` 使用用户提供的缓冲区来存储种子 r(n)，该缓冲区由 3 个 short 组成的数组构成，其中第零个成员保存最低有效位。

所有函数共享相同的乘数和加数。

`srand48` 函数用于初始化 `drand48`、`lrand48` 和 `mrand48` 的内部缓冲区 r(n)，使得种子值的 32 位被复制到 r(n) 的高 32 位中，r(n) 的低 16 位任意设置为 0x330e。此外，算法的常数乘数和加数被重置为上文给出的默认值。

`seed48` 函数也初始化 `drand48`、`lrand48` 和 `mrand48` 的内部缓冲区 r(n)，但此处可在 3 个 short 组成的数组中指定种子的全部 48 位，其中第零个成员指定最低位。同样，算法的常数乘数和加数被重置为上文给出的默认值。`seed48` 函数返回指向包含旧种子的 3 个 short 数组的指针。此数组是静态分配的，因此每次新调用 `seed48` 后其内容都会丢失。

最后，`lcong48` 允许完全控制 `drand48`、`erand48`、`lrand48`、`nrand48`、`mrand48` 和 `jrand48` 中使用的乘数和加数，以及 `drand48`、`lrand48` 和 `mrand48` 中使用的种子。一个由 7 个 short 组成的数组作为参数传递；前三个 short 用于初始化种子；中间三个用于初始化乘数；最后一个 short 用于初始化加数。因此，不能使用大于 0xffff 的值作为加数。

注意，所有三种设置随机数生成器种子的方法都会同时为六个生成器调用中的任何一个设置乘数和加数。

## 参见

[arc4random(3)](arc4random.3.md), [rand(3)](../stdlib/rand.3.md), [random(3)](../stdlib/random.3.md)

## 标准

本页描述的函数预期遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 作者

Martin Birgmeier
