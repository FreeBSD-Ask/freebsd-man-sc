# tgmath.3

`tgmath` — 类型通用宏

## 名称

`tgmath`

## 概要

```c
#include <tgmath.h>
```

## 描述

头文件

```c
#include <tgmath.h>
```

为

```c
#include <math.h>
```

和

```c
#include <complex.h>
```

中具有 `float`（后缀为 **f**）、`double` 和 `long double`（后缀为 **l**）版本的函数提供类型通用宏。在三种函数中各不相同且类型分别为 `float`、`double` 和 `long double` 的参数称为*通用参数*。

以下规则描述了调用类型通用宏时实际调用的函数。如果任何通用参数的类型为 `long double` 或 `long double complex`，则调用 `long double` 函数。否则，如果任何通用参数的类型为 `double`、`double complex` 或整数类型，则调用 `double` 版本。否则，宏展开为 `float` 实现。

对于下表中的宏，同时存在实数和复数函数。实数函数的原型在

```c
#include <math.h>
```

中，复数等效函数在

```c
#include <complex.h>
```

中。如果任何通用参数是复数值，则调用复数函数。否则，调用实数等效函数。

| **宏** | **实数函数** | **复数函数** |
| --- | --- | --- |
| `acos()` | `acos()` | `cacos()` |
| `asin()` | `asin()` | `casin()` |
| `atan()` | `atan()` | `catan()` |
| `acosh()` | `acosh()` | `cacosh()` |
| `asinh()` | `asinh()` | `casinh()` |
| `atanh()` | `atanh()` | `catanh()` |
| `cos()` | `cos()` | `ccos()` |
| `sin()` | `sin()` | `csin()` |
| `tan()` | `tan()` | `ctan()` |
| `cosh()` | `cosh()` | `ccosh()` |
| `sinh()` | `sinh()` | `csinh()` |
| `tanh()` | `tanh()` | `ctanh()` |
| `exp()` | `exp()` | `cexp()` |
| `log()` | `log()` | `clog()` |
| `pow()` | `pow()` | `cpow()` |
| `sqrt()` | `sqrt()` | `csqrt()` |
| `fabs()` | `fabs()` | `cabs()` |

以下宏不存在复数函数，因此将复数值传递给通用参数会调用未定义行为：

| `atan2()` | `fma()` | `llround()` | `remainder()` |
| --- | --- | --- | --- |
| `cbrt()` | `fmax()` | `log10()` | `remquo()` |
| `ceil()` | `fmin()` | `log1p()` | `rint()` |
| `copysign()` | `fmod()` | `log2()` | `round()` |
| `erf()` | `frexp()` | `logb()` | `scalbn()` |
| `erfc()` | `hypot()` | `lrint()` | `scalbln()` |
| `exp2()` | `ilogb()` | `lround()` | `tgamma()` |
| `expm1()` | `ldexp()` | `nearbyint()` | `trunc()` |
| `fdim()` | `lgamma()` | `nextafter()` |  |
| `floor()` | `llrint()` | `nexttoward()` |  |

以下宏始终展开为复数函数：

| `carg()` | `cimag()` | `conj()` | `cproj()` | `creal()` |
| --- | --- | --- | --- | --- |

此头文件包含

```c
#include <complex.h>
```

和

```c
#include <math.h>
```

## 标准

头文件

```c
#include <tgmath.h>
```

遵循 ISO/IEC 9899:1999 ("ISO C99") 标准。

## 历史

头文件

```c
#include <tgmath.h>
```

首次出现于 FreeBSD 5.3。

## 编译器支持

在 ISO/IEC 9899:2011 ("ISO C11") 之前，头文件

```c
#include <tgmath.h>
```

无法用严格符合标准的 C 代码实现，需要特殊的编译器支持。从 ISO/IEC 9899:2011 ("ISO C11") 开始，此头文件可以使用 `_Generic` 语言关键字实现。除了支持此关键字的编译器外，此头文件还可以在 GCC 上工作。

## 缺陷

此处提到的许多函数未在

```c
#include <math.h>
```

或

```c
#include <complex.h>
```

中提供原型，因为它们尚未实现。这阻止了相应的类型通用宏正常工作。
