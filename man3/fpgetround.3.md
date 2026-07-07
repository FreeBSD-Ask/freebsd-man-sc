# fpgetround(3)

`fpgetround` — IEEE 浮点接口

## 名称

`fpgetround`, `fpsetround`, `fpsetprec`, `fpgetprec`, `fpgetmask`, `fpsetmask`, `fpgetsticky`, `fpresetsticky`

## 概要

`#include <ieeefp.h>`

```c
typedef enum {
	FP_RN,		/* 就近舍入 */
	FP_RM,		/* 向负无穷向下舍入 */
	FP_RP,		/* 向正无穷向上舍入 */
	FP_RZ		/* 截断 */
} fp_rnd_t;
```

```c
fp_rnd_t fpgetround(void);
fp_rnd_t fpsetround(fp_rnd_t direction);
```

```c
typedef enum {
	FP_PS,		/* 24 位（单精度） */
	FP_PRS,		/* 保留 */
	FP_PD,		/* 53 位（双精度） */
	FP_PE		/* 64 位（扩展精度） */
} fp_prec_t;
```

```c
fp_prec_t fpgetprec(void);
fp_prec_t fpsetprec(fp_prec_t precision);
```

```c
#define fp_except_t	int
#define FP_X_INV	0x01	/* 无效操作 */
#define FP_X_DNML	0x02	/* 非规范 */
#define FP_X_DZ		0x04	/* 除零 */
#define FP_X_OFL	0x08	/* 溢出 */
#define FP_X_UFL	0x10	/* 下溢 */
#define FP_X_IMP	0x20	/* （不）精确 */
#define FP_X_STK	0x40	/* 栈故障 */
```

```c
fp_except_t fpgetmask(void);
fp_except_t fpsetmask(fp_except_t mask);
fp_except_t fpgetsticky(void);
fp_except_t fpresetsticky(fp_except_t sticky);
```

## 描述

此处描述的例程已弃用。新代码应使用 fenv(3) 提供的功能。

当检测到浮点异常时，会设置异常粘滞标志并测试异常掩码。如果掩码已设置，则发生陷阱。这些例程允许设置浮点异常掩码，并在检测到异常后重置异常粘滞标志。此外，它们还允许设置浮点舍入模式和精度。

`fpgetround` 函数返回当前的浮点舍入模式。

`fpsetround` 函数设置浮点舍入模式，并返回先前的模式。

`fpgetprec` 函数返回当前的浮点精度。

`fpsetprec` 函数设置浮点精度，并返回先前的精度。

`fpgetmask` 函数返回当前的浮点异常掩码。

`fpsetmask` 函数设置浮点异常掩码，并返回先前的掩码。

`fpgetsticky` 函数返回当前的浮点粘滞标志。

`fpresetsticky` 函数清除浮点粘滞标志，并返回先前的标志。

防止除零触发陷阱的示例代码：

```c
fpsetmask(~FP_X_DZ);
a = 1.0;
b = 0;
c = a / b;
fpresetsticky(FP_X_DZ);
fpsetmask(FP_X_DZ);
```

## 实现说明

`fpgetprec` 和 `fpsetprec` 函数提供了许多平台上不可用的功能。目前仅在 i386 和 amd64 平台上实现。更改精度不是受支持的功能：当代码编译为利用 SSE 时可能无效，并且许多库函数和编译器优化依赖于默认精度才能正确运行。

## 参见

fenv(3), isnan(3)

## 历史

这些例程基于 SysV/386 上同名例程。

## 注意事项

发生浮点异常后、设置掩码之前，必须重置粘滞标志。如果在粘滞标志重置之前又发生另一个异常，则可能发出错误的异常类型。
