# sdoc(7)

`sdoc` — 为手册页添加安全注意事项章节的指南

## 名称

`sdoc`

## 描述

本文档介绍了为手册页添加安全注意事项章节的准则，并提供了两个典型示例。

用 groff_mdoc(7) 编写 FreeBSD 手册页的准则规定，每个描述 FreeBSD 系统功能的手册页都应包含一个安全注意事项章节，描述通过滥用该功能可能破坏哪些安全要求。在编写这些章节时，作者应尝试在两个相互冲突的目标之间取得平衡：简洁性和完整性。一方面，安全注意事项章节不能过于冗长，否则繁忙的读者可能会被劝退而不去阅读。另一方面，安全注意事项章节不能不完整，否则将无法实现指导读者如何避免所有不安全用途的目的。本文档为在 FreeBSD 系统给定功能的安全注意事项章节中平衡简洁性和完整性提供了准则。

### 从何处开始

首先列出通过滥用该功能可能违反的通用安全要求。安全要求分为四类：

***完整性***（示例：非管理员不应修改系统二进制文件），

***机密性***（示例：非管理员不应查看影子密码文件），

***可用性***（示例：Web 服务器应及时响应客户端请求），以及

***正确性***（示例：ps 程序应准确提供其文档中描述的进程表信息列出功能——不多不少。）

好的安全注意事项章节应解释如何通过滥用该功能来违反列表中的每项通用安全要求。每次解释都应附带读者为避免违规而应遵循的说明。当引用 Secure Programming Practices 手册页 [sprog(7)](sprog.7.md) 中描述的潜在漏洞时，同样应交叉引用该文档而不是复制信息。只要可能，请引用本文档而不是复制其中包含的内容。

### 在何处停止

安全问题通常是相互关联的；单个问题往往具有深远的影响。例如，几乎所有动态链接程序的正确性都依赖于运行时链接器的正确实现和配置。而该程序的正确性又依赖于其库的正确性、用于构建它的编译器的正确性、用于构建该编译器的前一个编译器的正确性，依此类推，如 Thompson 所述（参见下文 Sx SEE ALSO ）。

由于需要简洁，安全注意事项章节应仅描述与手册页主题功能直接相关的问题。请引用其他手册页而不是复制其中的内容。

## 实例

大多数单个函数的安全注意事项章节可以遵循以下简单公式：

- 用一两句话描述每个潜在的安全问题。
- 用一两句话描述如何避免每个潜在的安全问题。
- 提供一个简短的代码示例。

以下是 strcpy(3) 手册页的安全注意事项章节示例：

Fn strcpy 函数容易被滥用，使恶意用户能够通过缓冲区溢出攻击任意更改正在运行的程序的功能。

避免使用 Fn strcpy 。改用 Fn strncpy ，并确保复制到目标缓冲区的字符数不超过其容量。不要忘记对目标缓冲区进行 NUL 终止，因为 Fn strncpy 在截断时不会终止目标字符串。

注意，Fn strncpy 也可能有问题。字符串被截断本身可能就是一个安全隐患。由于截断后的字符串不如原始字符串长，它可能指向完全不同的资源，使用截断的资源可能导致非常不正确的行为。示例：

```sh
void
foo(const char *arbitrary_string)
{
	char onstack[8];
#if defined(BAD)
	/*
	 * 第一个 strcpy 是不良行为。不要使用 strcpy()！
	 */
	(void)strcpy(onstack, arbitrary_string);     /* BAD! */
#elif defined(BETTER)
	/*
	 * 下面两行演示了对
	 * strncpy() 的更好使用。
	 */
	(void)strncpy(onstack, arbitrary_string, sizeof(onstack) - 1);
	onstack[sizeof(onstack - 1)] = '\ ';
#elif defined(BEST)
	/*
	 * 由于测试了截断，这些行更加健壮。
	 */
	if (strlen(arbitrary_string) + 1 > sizeof(onstack))
		err(1, "onstack would be truncated");
	(void)strncpy(onstack, arbitrary_string, sizeof(onstack));
#endif
}
```

工具和命令的安全注意事项章节往往不那么公式化。让你列出的可能被违反的安全要求作为指导；以尽可能简洁的方式解释每一项并列出解决方案。

以下是 rtld(1) 手册页的安全注意事项章节示例：

使用 LD_LIBRARY_PATH 和 LD_PRELOAD 环境变量，恶意用户可以使动态链接器将自己设计的共享库链接到运行非 set-user-ID/group-ID 程序的进程的地址空间中。这些共享库可以通过用对自身函数的调用替换对标准库函数的调用来任意更改程序的功能。虽然此功能对于 set-user-ID 和 set-group-ID 程序已禁用，但仍可用于在其他程序中创建特洛伊木马。

所有用户都应注意，非 set-user-ID/group-ID 动态链接程序的正确操作取决于这些环境变量的正确配置，并小心避免可能将它们设置为会导致运行时链接器链接来源不明的共享库的值的操作。

## 参见

groff_mdoc(7), [security(7)](security.7.md), [sprog(7)](sprog.7.md)

> Edward Amoroso, AT&T Bell Laboratories, *Fundamentals of Computer Security Technology*, P T R Prentice Hall, 1994.

> Ken Thompson, "Reflections on Trusting Trust", *Communications of the ACM*, Vol. 27, No. 8, pp. 761-763, Association for Computing Machinery, Inc., August, 1984.

## 历史

`sdoc` 手册页首次出现于 FreeBSD 5.0。

## 作者

Tim Fraser <tfraser@tislabs.com>, NAI Labs CBOSS 项目 Brian Feldman <bfeldman@tislabs.com>, NAI Labs CBOSS 项目
