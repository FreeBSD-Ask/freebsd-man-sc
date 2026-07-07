# sizeof(7)

`sizeof` — 返回给定操作数的存储大小

## 名称

`sizeof` 运算符

## 语法

`sizeof` `( type` ) 或 `sizeof` `expression`

## 描述

`sizeof` 运算符返回其操作数的大小。`sizeof` 运算符不能应用于不完整类型、具有不完整类型的表达式（例如 `void` 或前向定义的 `struct foo`）以及函数类型。

C 语言中基本（非派生）数据类型的大小可能因硬件平台和实现而异。它们由相应的应用二进制接口（ABI）规范定义，有关 FreeBSD 使用的 ABI 的详细信息，请参见 [arch(7)](arch.7.md)。程序可能需要或有必要能够确定某个数据类型或对象的存储大小，以适应平台特性。

一元 `sizeof` 运算符以 *char 大小的单位*（C 语言字节）返回表达式或数据类型的存储大小。因此，`sizeof(char)` 始终保证为 1。（每个 `char` 的位数由

`#include <limits.h>`

头文件中的 `CHAR_BIT` 定义给出；许多系统还在

`#include <sys/param.h>`

头文件中将"每字节的位数"定义为 `NBBY`。）

## 实例

不同平台可能使用不同的数据模型。例如，整数、long 和指针使用 32 位的系统（如 i386）被称为使用"ILP32"数据模型，使用 64 位 long 和指针的系统（如 amd64 / x86_64）被称为"LP64"数据模型。

以下示例说明了在 ILP32 和 LP64 系统上调用 `sizeof` 的可能结果：

当应用于简单变量或数据类型时，`sizeof` 返回对象数据类型的存储大小：

| **对象或类型** | **ILP32 结果** | **LP64 结果** |
| --- | --- | --- |
| `sizeof(char)` | 1 | 1 |
| `sizeof(int)` | 4 | 4 |
| `sizeof(long)` | 4 | 8 |
| `sizeof(float)` | 4 | 4 |
| `sizeof(double)` | 8 | 8 |
| `sizeof(char *)` | 4 | 8 |

对于初始化的数据或在编译时已知固定大小的未初始化数组，`sizeof` 将返回正确的存储大小：

```sh
#define DATA "1234567890"
char buf1[] = "abc";
char buf2[1024];
char buf3[1024] = { 'a', 'b', 'c' };
```

| **对象或类型** | **结果** |
| --- | --- |
| `sizeof(DATA)` | 11 |
| `sizeof(buf1)` | 4 |
| `sizeof(buf2)` | 1024 |
| `sizeof(buf3)` | 1024 |

以上示例在 ILP32 和 LP64 平台上结果相同，因为它们基于字符单位。

当应用于结构体或联合时，`sizeof` 返回对象中的总字节数，包括用于在内存中对齐对象的任何内部或尾部填充。因此，该结果可能大于将每个单独成员的存储大小相加的结果：

```sh
struct s1 {
        char c;
};
struct s2 {
        char *s;
        int i;
};
struct s3 {
        char *s;
        int i;
        int j;
};
struct s4 {
	int i;
	uint64_t i64;
};
struct s5 {
        struct s1 a;
        struct s2 b;
        struct s3 c;
        struct s4 d;
};
```

| **对象或类型** | **ILP32 结果** | **LP64 结果** |
| --- | --- | --- |
| `sizeof(struct s1)` | 1 | 1 |
| `sizeof(struct s2)` | 8 | 16 |
| `sizeof(struct s3)` | 12 | 16 |
| `sizeof(struct s4)` | 12 | 16 |
| `sizeof(struct s5)` | 36 | 56 |

当应用于包含灵活数组成员的结构体时，`sizeof` 返回*不包含*该数组的结构体大小，尽管同样可能包括编译器认为适当的任何填充：

```sh
struct flex {
        char c;
        long b;
        char array[];
}
```

| **对象或类型** | **ILP32 结果** | **LP64 结果** |
| --- | --- | --- |
| `sizeof(struct flex)` | 8 | 16 |

`sizeof` 运算符更常见的用途之一是确定要分配的正确内存量：

```sh
int *nums = calloc(512, sizeof(int));
```

`sizeof` 运算符可通过将数组大小除以其中一个元素的大小来计算数组中的元素数量：

```sh
int nums[] = { 1, 2, 3, 4, 5 };
const int howmany = sizeof(nums) / sizeof(nums[0]);
```

许多系统通过

`#include <sys/param.h>`

头文件以宏 `ntimes()` 的形式提供此快捷方式。

## 结果

`sizeof` 运算符的结果是一个无符号整数类型，在 `stddef.h` 头文件中定义为 `size_t`。

## 注释

将 `sizeof` 应用于动态分配的数组是一个常见错误：

```sh
char *buf;
if ((buf = malloc(BUFSIZ)) == NULL) {
        perror("malloc");
}
/* 警告：错误！ */
(void)strncat(buf, input, sizeof(buf) - 1);
```

在这种情况下，该运算符将返回指针的存储大小（`sizeof(char *)`），而不是已分配的内存。

`sizeof` 确定所给表达式结果的 `size`，但*不会*对该表达式求值：

```sh
int a = 42;
printf("%ld - %dn", sizeof(a = 10), a); /* 结果："4 - 42" */
```

由于 `sizeof` 运算符由编译器而非预处理器求值，因此不能在预处理器表达式中使用 `sizeof` 运算符。

## 参见

[arch(7)](arch.7.md), [operator(7)](operator.7.md)

## 标准

`sizeof` 运算符遵循 ANSI X3.159-1989（"ANSI C89"）

对结构体中灵活数组成员的处理遵循 ISO/IEC 9899:1999（"ISO C99"）

## 作者

本手册页由 Jan Schaumann <jschauma@netmeister.org> 编写。
