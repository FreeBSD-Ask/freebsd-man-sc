# stdckdint.3

`stdckdint` — 检查整数运算

## 名称

`stdckdint`

## 概要

```c
#include <stdckdint.h>
```

```c
bool
ckd_add(type1 *result, type2 a, type3 b);

bool
ckd_sub(type1 *result, type2 a, type3 b);

bool
ckd_mul(type1 *result, type2 a, type3 b);
```

## 描述

类函数宏 `ckd_add`、`ckd_sub` 和 `ckd_mul` 分别执行检查整数加法、减法和乘法。如果将 `a` 和 `b` 相加、相减或相乘（如同它们各自的类型具有无限范围）的结果适合 `type1`，则将其存储在 `result` 指向的位置，宏求值为 `false`。否则，宏求值为 `true`，`result` 指向位置的内容是运算结果回绕到 `type1` 范围后的值。

## 返回值

`ckd_add`、`ckd_sub` 和 `ckd_mul` 宏在请求的运算溢出结果类型时求值为 `true`，否则为 `false`。

## 实例

```c
#include <assert.h>
#include <limits.h>
#include <stdckdint.h>
int main(void)
{
	int result;
	assert(!ckd_add(&result, INT_MAX, 0));
	assert(result == INT_MAX);
	assert(ckd_add(&result, INT_MAX, 1));
	assert(result == INT_MIN);
	assert(!ckd_sub(&result, INT_MIN, 0));
	assert(result == INT_MIN);
	assert(ckd_sub(&result, INT_MIN, 1));
	assert(result == INT_MAX);
	assert(!ckd_mul(&result, INT_MAX / 2, 2));
	assert(result == INT_MAX - 1);
	assert(ckd_mul(&result, INT_MAX / 2 + 1, 2));
	assert(result == INT_MIN);
	return 0;
}
```

## 历史

`ckd_add`、`ckd_sub` 和 `ckd_mul` 宏首次引入于 FreeBSD 14.0。

## 作者

`ckd_add`、`ckd_sub` 和 `ckd_mul` 宏及本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
