# cap_rights_init(3)

`cap_rights_init` — 管理 `cap_rights_t` 结构

## 名称

`cap_rights_init`, `cap_rights_set`, `cap_rights_clear`, `cap_rights_is_set`, `cap_rights_is_empty`, `cap_rights_is_valid`, `cap_rights_merge`, `cap_rights_remove`, `cap_rights_contains`

## 库

Lb libc

## 概要

`#include <sys/capsicum.h>`

```c
cap_rights_t *
cap_rights_init(cap_rights_t *rights, ...);

cap_rights_t *
cap_rights_set(cap_rights_t *rights, ...);

cap_rights_t *
cap_rights_clear(cap_rights_t *rights, ...);

bool
cap_rights_is_set(const cap_rights_t *rights, ...);

bool
cap_rights_is_empty(const cap_rights_t *rights);

bool
cap_rights_is_valid(const cap_rights_t *rights);

cap_rights_t *
cap_rights_merge(cap_rights_t *dst, const cap_rights_t *src);

cap_rights_t *
cap_rights_remove(cap_rights_t *dst, const cap_rights_t *src);

bool
cap_rights_contains(const cap_rights_t *big, const cap_rights_t *little);
```

## 描述

此处记录的函数用于管理 `cap_rights_t` 结构。

传递给 `cap_rights_init`、`cap_rights_set`、`cap_rights_clear` 和 `cap_rights_is_set` 函数的能力权限（capability rights）应以逗号分隔。例如：

```c
cap_rights_set(&rights, CAP_READ, CAP_WRITE, CAP_FSTAT, CAP_SEEK);
```

完整的能力权限列表可在 [rights(4)](../man4/rights.4.md) 手册页中找到。

`cap_rights_init` 函数初始化所提供的 `cap_rights_t` 结构。只有经过正确初始化的结构才能传递给其余函数。为方便起见，该结构可在初始化时直接填入能力权限，而无需稍后调用 `cap_rights_set` 函数。为更加便利，该函数会返回指向给定结构的指针，因此可直接传递给 [cap_rights_limit(2)](../man2/cap_rights_limit.2.md)：

```c
cap_rights_t rights;
if (cap_rights_limit(fd, cap_rights_init(&rights, CAP_READ, CAP_WRITE)) < 0)
	err(1, "Unable to limit capability rights");
```

`cap_rights_set` 函数将给定的能力权限添加到给定的 `cap_rights_t` 结构中。

`cap_rights_clear` 函数从给定的 `cap_rights_t` 结构中移除给定的能力权限。

`cap_rights_is_set` 函数检查给定的 `cap_rights_t` 结构是否设置了所有给定的能力权限。

`cap_rights_is_empty` 函数检查 `rights` 结构是否为空。

`cap_rights_is_valid` 函数验证给定的 `cap_rights_t` 结构是否有效。

`cap_rights_merge` 函数将 `src` 结构中存在的所有能力权限合并到 `dst` 结构中。

`cap_rights_remove` 函数从 `dst` 结构中移除 `src` 结构中存在的所有能力权限。

`cap_rights_contains` 函数检查 `big` 结构是否包含 `little` 结构中存在的所有能力权限。

## 返回值

这些函数不会失败。如果传入了无效的能力权限或无效的 `cap_rights_t` 结构作为参数，程序将被中止。

`cap_rights_init`、`cap_rights_set` 和 `cap_rights_clear` 函数返回 `rights` 参数中给出的 `cap_rights_t` 结构的指针。

`cap_rights_merge` 和 `cap_rights_remove` 函数返回 `dst` 参数中给出的 `cap_rights_t` 结构的指针。

如果 `rights` 参数中设置了所有给定的能力权限，`cap_rights_is_set` 函数返回 `true`。

如果 `rights` 结构中未设置任何能力权限，`cap_rights_is_empty` 函数返回 `true`。

`cap_rights_is_valid` 函数执行各种检查以确定给定的 `cap_rights_t` 结构是否有效，如果有效则返回 `true`。

如果 `little` 结构中设置的所有能力权限也存在于 `big` 结构中，`cap_rights_contains` 函数返回 `true`。

## 实例

以下示例演示了如何准备一个 `cap_rights_t` 结构以传递给 [cap_rights_limit(2)](../man2/cap_rights_limit.2.md) 系统调用。

```c
cap_rights_t rights;
int fd;
fd = open("/tmp/foo", O_RDWR);
if (fd < 0)
	err(1, "open() failed");
cap_rights_init(&rights, CAP_FSTAT, CAP_READ);
if (allow_write_and_seek)
	cap_rights_set(&rights, CAP_WRITE, CAP_SEEK);
if (dont_allow_seek)
	cap_rights_clear(&rights, CAP_SEEK);
if (cap_rights_limit(fd, &rights) < 0 && errno != ENOSYS)
	err(1, "cap_rights_limit() failed");
```

## 参见

[cap_rights_limit(2)](../man2/cap_rights_limit.2.md), [open(2)](../man2/open.2.md), [capsicum(4)](../man4/capsicum.4.md), [rights(4)](../man4/rights.4.md)

## 历史

`cap_rights_init`、`cap_rights_set`、`cap_rights_clear`、`cap_rights_is_set`、`cap_rights_is_valid`、`cap_rights_merge`、`cap_rights_remove` 和 `cap_rights_contains` 函数首次出现于 FreeBSD 8.3。对 capabilities 和 capabilities 模式的支持作为 TrustedBSD 项目的一部分开发。

## 作者

这一系列函数由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下创建。
