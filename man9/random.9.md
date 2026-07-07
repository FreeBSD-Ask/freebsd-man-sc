# random(9)

`arc4rand` — 提供伪随机数

## 名称

`arc4rand`, `arc4random`, `arc4random_buf`, `is_random_seeded`, `random`, `read_random`, `read_random_uio`

## 概要

```c
#include <sys/libkern.h>
```

```c
uint32_t
arc4random(void)

void
arc4random_buf(void *ptr, size_t len)

void
arc4rand(void *ptr, u_int length, int reseed)
```

```c
#include <sys/random.h>
```

```c
bool
is_random_seeded(void)

void
read_random(void *buffer, int count)

int
read_random_uio(struct uio *uio, bool nonblock)
```

### 旧例程

```c
#include <sys/libkern.h>
```

```c
u_long
random(void)
```

## 描述

`arc4random` 和 `arc4random_buf` 函数将返回质量非常好的随机数，适合安全相关用途。两者都是底层 `arc4rand` 接口的包装。`arc4random` 返回一个 32 位随机值，而 `arc4random_buf` 用 `len` 字节的随机数据填充 `ptr`。

`arc4rand` CSPRNG 从 [random(4)](../man4/random.4.md) 内核抽象熵设备中播种。自动重新播种在未指定的时间和字节（输出）间隔发生。可以通过传递非零的 `reseed` 值来强制重新播种。

`read_random` 函数用于直接从内核抽象熵设备读取熵。如果熵设备尚未播种，`read_random` 将阻塞，直到其被播种。提供的 `buffer` 最多填充 `count` 字节。强烈建议不要直接使用 `read_random`；应使用 `arc4rand` 系列函数。

`is_random_seeded` 函数可用于预先检查 `read_random` 是否会阻塞。（如果 random 已播种，则不会阻塞。）

`read_random_uio` 函数的行为与 **`/dev/random`** 上的 read(2) 完全相同。`uio` 参数指向应存储随机数据的缓冲区。如果 `nonblock` 为 true 且随机设备尚未播种，此函数不返回任何数据。否则，此函数可能可中断地阻塞，直到随机设备被播种。如果在随机设备被播种之前函数被中断，则不返回数据。

已弃用的 `random` 函数将返回 31 位值。它已过时，计划在 FreeBSD 16.0 中移除。考虑改用 [prng(9)](prng.9.md)，并参见[安全注意事项](#安全注意事项)。

## 返回值

`arc4rand` 函数使用 Chacha20 算法生成伪随机字节序列。`arc4random` 函数使用 `arc4rand` 生成范围从 0 到 (2\*\*32)-1 的伪随机数。

`read_random` 函数返回放入 `buffer` 中的字节数。

`read_random_uio` 成功时返回零，否则返回错误代码。

`random` 返回范围从 0 到 (2\*\*31)-1 的数字。

## 错误

`read_random_uio` 可能因以下原因失败：

**[`EFAULT`]** `uio` 指向无效的内存区域。

**[`EWOULDBLOCK`]** 随机设备未播种且 `nonblock` 为 true。

## 作者

Dan Moschuk 编写了 `arc4random`。Mark R V Murray 编写了 `read_random`。

## 安全注意事项

不要在新代码中使用 `random`。

重要的是要记住，`random` 函数是完全可预测的。攻击者通过记录一些生成的值，很容易预测 `random` 的未来输出。我们再怎么强调都不为过：`random` 不得用于生成本意是不可预测的值。
