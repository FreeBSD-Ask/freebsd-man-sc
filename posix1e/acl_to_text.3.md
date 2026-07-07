# acl_to_text(3)

`acl_to_text` — 将 ACL 转换为文本

## 名称

`acl_to_text`, `acl_to_text_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
char *
acl_to_text(acl_t acl, ssize_t *len_p);
```

```c
char *
acl_to_text_np(acl_t acl, ssize_t *len_p, int flags);
```

## 描述

`acl_to_text` 和 `acl_to_text_np` 函数将参数 `acl` 所指向的 ACL 转换为以 NULL 结尾的字符串。若指针 `len_p` 不为 NULL，则函数将在 `len_p` 所指向的位置返回字符串的长度（不包括 NULL 终止符）。若 ACL 为 POSIX.1e 类型，`acl_to_text` 返回的文本字符串格式为 POSIX.1e 长 ACL 格式。若 ACL 为 NFSv4 类型，文本字符串的格式为紧凑格式，除非指定了 `ACL_TEXT_VERBOSE` 标志。

指定的标志由以下值按位或运算构成：

| ACL_TEXT_VERBOSE | 使用详细格式化 ACL |
| ---------------- | ------------------ |
| ACL_TEXT_NUMERIC_IDS | 不将 ID 解析为用户或组名 |
| ACL_TEXT_APPEND_ID | 除用户和组名外，附加数字 ID |

该函数分配容纳字符串所需的内存，并返回指向该字符串的指针。当不再需要新字符串时，调用者应通过以 `(void*)char` 为参数调用 [acl_free(3)](acl_free.3.md) 来释放可释放的内存。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，该函数将返回指向 ACL 长文本形式的指针。否则，返回 `(char*)NULL`，并设置 `errno` 以指示错误。

## 错误

若发生以下任一情况，`acl_to_text` 函数将返回 `(acl_t)NULL`，并将 `errno` 设置为相应值：

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。`acl` 所表示的 ACL 包含一个或多个格式不正确的 ACL 条目，或因其他原因无法转换为 ACL 的文本形式。

`[ENOMEM]` 要返回的字符串所需的内存超过了硬件或软件所施加的内存管理约束所允许的范围。

## 参见

[acl(3)](acl.3.md), [acl_free(3)](acl_free.3.md), [acl_from_text(3)](acl_from_text.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。如需加入该列表，请参阅 FreeBSD POSIX.1e 实现页面获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在继续。

## 作者

Robert N M Watson

## 缺陷

`acl_from_text` 和 `acl_to_text` 函数依赖于 getpwent(3) 库调用来管理用户名和 uid 映射，以及 getgrent(3) 库调用来管理组名和 gid 映射。这些调用不是线程安全的，因此 `acl_from_text` 和 `acl_to_text` 也不是线程安全的。这些函数还可能与 `getpwent` 和 `getgrent` 调用相关的有状态调用产生干扰。
