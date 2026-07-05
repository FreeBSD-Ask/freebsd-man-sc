# DEFINE_IFUNC.9

`DEFINE_IFUNC` — 定义在运行时选择实现的内核函数

## 名称

`DEFINE_IFUNC`

## 概要

```c
#include <machine/ifunc.h>
```

```c
DEFINE_IFUNC(qual, ret_type, name, args);
```

## 描述

ifunc 是一种链接器特性，允许程序员定义其实现在启动时或模块加载时选择的函数。`DEFINE_IFUNC` 宏可用于定义 ifunc。选择由解析器函数执行，该函数返回指向所选函数的指针。ifunc 解析器在机器相关的初始化例程早期被调用，或者在动态加载模块时于加载时调用。解析必须在首次调用 ifunc 之前完成。ifunc 解析在 CPU 特性枚举之后和内核环境初始化之后执行。ifunc 的典型用例是其行为依赖于可选 CPU 特性的例程。例如，某 CPU 架构的新一代可能提供优化常见操作的指令。为了避免每次执行操作时都测试 CPU 特性的开销，可以使用 ifunc 为该操作提供两种实现：一种针对具有额外指令的平台，另一种针对较旧的平台。

由于 `DEFINE_IFUNC` 是一个定义动态类型函数的宏，其用法看起来有些不寻常。`qual` 参数是要应用于 ifunc 的零个或多个 C 函数限定符列表。此参数通常为空或 `static` 限定符。`ret_type` 是 ifunc 的返回类型。`name` 是 ifunc 的名称。`args` 是函数参数类型的括号括起的逗号分隔列表，如同它们在 C 函数声明中出现的样子。

`DEFINE_IFUNC` 的使用后必须跟随解析器函数体。解析器必须返回一个返回类型为 `ret_type`、参数类型为 `args` 的函数。解析器函数使用 `resolver` gcc 风格函数属性定义，使相应的 [elf(5)](../man5/elf.5.md) 函数符号类型为 `STT_GNU_IFUNC` 而非 `STT_FUNC`。内核链接器调用解析器来处理针对 ifunc 调用的重定位和引用此类符号的 PLT 条目。

## 实例

ifunc 解析器在引导早期执行，在大多数内核设施可用之前。它们实际上仅限于检查 CPU 特性标志和可调参数。

```c
static size_t
fast_strlen(const char *s __unused)
{
	size_t len;
	/* 快速，但可能并非在所有情况下都正确。 */
	__asm("movq $42,%0n" : "=r" (len));
	return (len);
}
static size_t
slow_strlen(const char *s)
{
	const char *t;
	for (t = s; *t != '\ '; t++);
	return (t - s);
}
DEFINE_IFUNC(, size_t, strlen, (const char *))
{
	int enabled;
	enabled = 1;
	TUNABLE_INT_FETCH("debug.use_fast_strlen", &enabled);
	if (enabled && (cpu_features & CPUID_FAST_STRLEN) != 0)
		return (fast_strlen);
	else
		return (slow_strlen);
}
```

此示例定义了一个 `strlen` 函数，为广播支持该特性的 CPU 提供了优化实现。

## 参见

[elf(5)](../man5/elf.5.md)

## 注意事项

ifunc 需要工具链支持（以发出 `STT_GNU_IFUNC` 类型的函数符号）和内核链接器支持（以在引导或模块加载期间调用 ifunc 解析器）。
