# assert(3)

`assert` — 表达式验证宏

## 名称

`assert`, `static_assert`

## 概要

`#include <assert.h>`

```c
assert(expression);
static_assert(expression);
static_assert(expression, message);
```

## 描述

`assert` 宏测试给定的标量 `expression`，如果为假，则向 `stderr` 写入诊断消息并调用 abort(3) 函数，从而终止调用进程。

如果 `expression` 为真，`assert` 宏不做任何事情。

在所有编译模式下，`assert` 都定义为带有省略号参数的宏，与 C23 标准一致。这允许包含逗号的表达式直接传递，而无需额外的封闭括号。仅评估单个标量表达式。禁止提供多个参数，因此顶层逗号运算符是不允许的。特别是，这可以防止意外地以 `static_assert` 的风格编写 `assert`，否则会通过逗号运算符被静默评估为始终为真。

通过将 `NDEBUG` 定义为宏（例如使用 [cc(1)](../man1/cc.1.md) 选项 `-DNDEBUG`），可在编译时移除 `assert` 宏。与大多数其他头文件不同，

```c
#include <assert.h>
```

可被多次包含。每次是否定义了 `NDEBUG` 决定了从那时起到该编译单元结束或再次包含

```c
#include <assert.h>
```

之前 assert 的行为。

`assert` 宏仅应用于确保开发者的预期成立。它不适用于常规的运行时错误检测。

在 C23 之前的编译模式下，`static_assert` 作为宏实现并展开为 `_Static_assert`，与 `assert` 相反，它在编译时进行断言。一旦违反约束，编译器会产生包含字符串字面量消息（若提供）的诊断消息。包含字符串字面量消息的 `_Static_assert` 初始形式在 C11 标准中引入，不含字符串字面量的另一种形式遵循 C23 标准。

在 C23 及以后版本中，`static_assert` 是语言关键字，`_Static_assert` 作为一种过时的替代拼写提供，不应在新代码和开发中使用。

## 实例

断言：

```c
assert(1 == 0);
```

会生成类似以下的诊断消息：

```sh
Assertion failed: (1 == 0), function main, file main.c, line 100.
```

以下 assert 试图断言没有发生部分读取：

```c
assert(read(fd, buf, nbytes) == nbytes);
```

但存在两个问题。首先，它检查的是正常条件，而非表示 bug 的条件。其次，如果定义了 `NDEBUG`，该代码会消失，从而改变程序的语义。

以下示例断言反映 `len` 值的复合字面量的 `iov_len` 成员非零。该复合字面量包含一个未被括号保护的逗号，可变参数 `assert` 宏可以透明处理：

```c
assert((struct iovec){ buf, len }.iov_len);
```

以下断言 `S` 结构体的大小为 16。否则，它会产生一条指向该约束并包含所提供字符串字面量的诊断消息：

```c
static_assert(sizeof(struct S) == 16, "size mismatch");
```

如果未提供字符串字面量，则仅指向约束。

## 参见

abort2(2), abort(3)

## 标准

`assert` 宏遵循 -isoC-2023。

`static_assert` 宏遵循 ISO/IEC 9899:2011（"ISO C11"）。在 -isoC-2023 中它是语言关键字；是否定义该宏取决于编译模式。

## 历史

`static_assert` 宏首次出现于 Version 7 AT&T UNIX。从 FreeBSD 15.2 起，它接受可变参数列表，允许包含逗号的表达式（如复合字面量）无需额外的封闭括号即可传递。这符合 -isoC-2023，但在所有编译模式下均可用。
