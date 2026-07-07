# extattr(3)

`extattr_namespace_to_string` — 将扩展属性命名空间标识符转换为字符串及反向转换

## 名称

`extattr_namespace_to_string`, `extattr_string_to_namespace`

## 库

libutil

## 概要

`#include <sys/extattr.h>`

`#include <libutil.h>`

```c
int
extattr_namespace_to_string(int attrnamespace, char **string);
```

```c
int
extattr_string_to_namespace(const char *string, int *attrnamespace);
```

## 描述

`extattr_namespace_to_string` 函数将 VFS 扩展属性标识符转换为可读字符串；`extattr_string_to_namespace` 函数执行上述操作的逆过程，将表示命名空间的可读字符串转换为命名空间标识符。虽然文件系统可以实现任意命名空间，但这些函数仅支持 `EXTATTR_NAMESPACE_USER`（"user"）和 `EXTATTR_NAMESPACE_SYSTEM`（"system"）命名空间，两者均在 [extattr(9)](../man9/extattr.9.md) 中定义。

这些函数用于错误报告和其他交互式任务。例如，程序可以使用 `extattr_namespace_to_string` 获取可读表示，而不是在错误消息中打印标识扩展属性的整数。同样，交互式程序可以要求用户输入名称并使用 `extattr_string_to_namespace` 获取所需标识符，而不是要求用户输入表示命名空间的整数。

## 返回值

若任一调用失败，返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`[EINVAL]` 无法识别所请求的命名空间。

## 参见

extattr(2), getextattr(8), setextattr(8), [extattr(9)](../man9/extattr.9.md)

## 历史

扩展属性支持作为 TrustedBSD 项目的一部分开发，引入于 FreeBSD 5.0。其开发旨在支持需要为每个文件或目录关联额外标签的安全扩展。
