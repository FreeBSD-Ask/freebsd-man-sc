# KASSERT.9

`KASSERT` — 内核表达式验证宏

## 名称

`KASSERT`

## 概要

```c
options INVARIANTS

#include <sys/param.h>

#include <sys/systm.h>

KASSERT(expression, msg)
MPASS(expression)
```

## 描述

断言在 FreeBSD 内核中广泛用于验证编程假设。对于运行时假设和不变式的违反，期望尽快、尽可能响亮地失败。断言是可选代码；对于不可恢复的错误条件，通常首选显式调用 [panic(9)](panic.9.md)。

`KASSERT` 宏测试给定的布尔 `expression`。如果 `expression` 求值为 `false`，且内核编译时启用了 `options INVARIANTS`，则调用 [panic(9)](panic.9.md) 函数。这会在错误点终止运行中的系统，可能进入内核调试器或启动内核核心转储。第二个参数 `msg` 是一个 [printf(9)](printf.9.md) 格式字符串及其参数，用括号括起。格式化后的字符串将成为 panic 字符串。

在未启用 `options INVARIANTS` 构建的内核中，断言宏定义为空操作。这消除了内核发布版本中广泛断言的运行时开销。因此，可在常数时间内完成的检查可作为断言添加，而不必担心其性能影响。更昂贵的检查，如输出到控制台的检查或验证对象链完整性的检查，通常最好隐藏在 `DIAGNOSTIC` 内核选项之后。

`MPASS` 宏（读作 “must-pass”）是 `KASSERT` 的便捷包装，自动生成包含文件和行信息的简单断言消息。

### 断言指南

添加新断言时，请记住其主要目的：帮助识别和调试复杂的错误条件。

断言失败导致的 panic 消息在没有生成内核转储时也应有用；该消息可能包含在错误报告中，应包含判别断言如何被违反所需的相关信息。当错误条件难以或无法由开发者本地重现时，这尤为重要。

因此，断言应遵循以下指南：

- 只要有可能，断言条件检查的运行时变量的值应出现在其消息中。
- 不相关的条件必须出现在单独的断言中。
- 多个相关条件应可区分（例如通过值），或拆分为单独的断言。
- 如有疑问，打印更多信息，而不是更少。

综合起来，这能更清晰地了解断言 panic 的确切原因；参见下文的实例。

## 实例

假设的 `struct foo` 对象在调用 `foo_dealloc` 时不得设置其 'active' 标志：

```c
void
foo_dealloc(struct foo *fp)
{
	KASSERT((fp->foo_flags & FOO_ACTIVE) == 0,
	    ("%s: fp %p is still active, flags=%x", __func__, fp,
	    fp->foo_flags));
	...
}
```

此断言提供对象的完整标志集以及内存指针，调试器可使用该指针详细检查对象（例如在 [ddb(4)](../man4/ddb.4.md) 中使用 'show foo' 命令）。

断言

```c
MPASS(td == curthread);
```

位于名为 foo.c 的文件第 87 行，将生成以下 panic 消息：

```c
panic: Assertion td == curthread failed at foo.c:87
```

这是一个简单的条件，消息提供了足够的信息来调查失败。

断言

```c
MPASS(td == curthread && (sz >= SIZE_MIN && sz <= SIZE_MAX));
```

不够有用。消息未指示断言的哪部分被违反，也未报告 `sz` 的值，而这对于理解断言为何失败可能至关重要。

根据上述指南，这应正确表达为：

```c
MPASS(td == curthread);
KASSERT(sz >= SIZE_MIN && sz <= SIZE_MAX,
    ("invalid size argument: %u", sz));
```

## 历史

`MPASS` 宏首次出现于 BSD/OS，并导入 FreeBSD 5.0。该名称最初是 “multi-processor assert” 的首字母缩写，但已演变为意为 “must pass” 或 “must-pass assert”。

## 参见

[panic(9)](panic.9.md)

## 作者

本手册页由 Jonathan M. Bresler <jmb@FreeBSD.org> 和 Mitchell Horne <mhorne@FreeBSD.org> 编写。
