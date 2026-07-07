# getenv.3

`getenv`, `clearenv`, `getenv_r`, `putenv`, `secure_getenv`, `setenv`, `unsetenv` — 环境变量函数

## 名称

`clearenv`, `getenv`, `getenv_r`, `putenv`, `secure_getenv`, `setenv`, `unsetenv`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
clearenv(void);

char *
getenv(const char *name);

int
getenv_r(const char *name, char *buf, size_t len);

char *
secure_getenv(const char *name);

int
setenv(const char *name, const char *value, int overwrite);

int
putenv(char *string);

int
unsetenv(const char *name);
```

## 描述

这些函数用于设置、删除和获取宿主环境列表中的环境变量。

`clearenv` 函数清除所有环境变量。可以使用 `setenv` 和 `putenv` 添加新变量。

`getenv` 函数获取由 `name` 指定的环境变量的当前值。应用程序不应修改 `getenv` 函数所返回字符串指向的内容。

`getenv_r` 函数获取由 `name` 指定的环境变量的当前值，并将其复制到长度为 `len` 的缓冲区 `buf` 中。

`secure_getenv` 在环境不可信时返回 `NULL`，否则其行为与 `getenv` 相同。当前，当 [issetugid(2)](../sys/issetugid.2.md) 返回非零值时环境不可信，但未来可能添加其他条件。

`setenv` 函数在当前环境列表中插入或重置环境变量 `name`。若列表中不存在变量 `name`，则将其与给定 `value` 一起插入。若变量已存在，则测试 `overwrite` 参数；若 `overwrite` 为零，则不重置该变量，否则将其重置为给定 `value`。

`putenv` 函数接受一个 `name=value` 形式的参数，并将其直接放入当前环境中，因此修改该参数将改变环境。若列表中不存在变量 `name`，则将其与给定 `value` 一起插入。若变量 `name` 已存在，则将其重置为给定 `value`。

`unsetenv` 函数从列表中删除 `name` 所指变量名的所有实例。

若在为内部使用而复制 `environ` 时检测到损坏（例如没有值的名称），则 `setenv`、`unsetenv` 和 `putenv` 将向 `stderr` 输出有关该问题的警告，丢弃损坏的条目并完成任务而不报错。

## 返回值

`getenv` 函数以 `NUL` 结尾字符串的形式返回环境变量的值。若变量 `name` 不在当前环境中，则返回 `NULL`。

`secure_getenv` 函数在进程处于"安全执行"状态时返回 `NULL`，否则调用 `getenv`。

成功完成时，`clearenv`、`getenv_r`、`setenv`、`putenv` 和 `unsetenv` 函数返回 0。否则返回 -1，并设置 `errno` 以指示错误。

## 错误

**[`EINVAL`]** `getenv`、`getenv_r`、`setenv` 或 `unsetenv` 函数失败，因为 `name` 是 `NULL` 指针、指向空字符串，或指向包含 `=` 字符的字符串。`putenv` 函数失败，因为 `string` 是 `NULL` 指针、`string` 不含 `=` 字符，或 `=` 是 `string` 中的第一个字符。这不遵循 POSIX 规范。

**[`ENOENT`]** `getenv_r` 函数失败，因为在环境中未找到所请求的变量。

**[`ENOMEM`]** `setenv`、`unsetenv` 或 `putenv` 函数失败，因为无法为环境分配内存。

**[`ERANGE`]** `getenv_r` 函数失败，因为所请求变量的值过长，无法放入提供的缓冲区。

## 参见

[csh(1)](../man1/csh.1.md), [sh(1)](../man1/sh.1.md), [execve(2)](../sys/execve.2.md), [environ(7)](../man7/environ.7.md)

## 标准

`getenv` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`setenv`、`putenv` 和 `unsetenv` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。`secure_getenv` 函数遵循 -p1003.1-2024。

## 历史

`setenv` 和 `unsetenv` 函数首次出现于 Version 7 AT&T UNIX。`putenv` 函数首次出现于 4.3BSD。

在 FreeBSD 7.0 之前，`putenv` 会复制 `string` 并使用 `setenv` 将其插入环境。此后改为将 `string` 用作 `name=value` 对的内存位置，以遵循 POSIX 规范。

`clearenv` 和 `secure_getenv` 函数添加于 FreeBSD 14。

`getenv_r` 函数首次出现于 NetBSD 4.0，并添加于 FreeBSD 15。

## 缺陷

连续调用 `setenv` 为同一 `name` 赋予比之前任何值都大的 `value` 将导致内存泄漏。FreeBSD 中此函数的语义（即 `value` 的内容被复制，且旧值无限期保持可访问）使得该缺陷无法避免。未来版本可能取消这两条语义保证中的一条或全部以修复此缺陷。
