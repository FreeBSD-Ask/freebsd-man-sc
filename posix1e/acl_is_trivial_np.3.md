# acl_is_trivial_np(3)

`acl_is_trivial_np` — 判断 ACL 是否为平凡

## 名称

`acl_is_trivial_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_is_trivial_np(const acl_t aclp, int *trivialp);
```

## 描述

`acl_is_trivial_np` 函数判断参数 `aclp` 所指向的 ACL 是否为平凡。成功完成时，如果 `aclp` 所指向的 ACL 是平凡的，参数 `trivialp` 所引用的位置将被设置为 1，否则设置为 0。

如果 ACL 可以完整地表示为文件模式而不丢失任何访问规则，则该 ACL 是平凡的。对于 POSIX.1e ACL，如果 ACL 具有三条必需条目（一条用于属主、一条用于属组、一条用于其他），则该 ACL 是平凡的。对于 NFSv4 ACL，如果 ACL 与 [acl_strip_np(3)](acl_strip_np.3.md) 生成的 ACL 相同，则该 ACL 是平凡的。具有非平凡 ACL 的文件在 `ls -l` 输出中的模式位后会附加一个加号。

## 返回值

`acl_is_trivial_np` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 参见

[acl(3)](acl.3.md), [acl_strip_np(3)](acl_strip_np.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。`acl_is_trivial_np` 函数添加于 FreeBSD 8.0。

## 作者

Edward Tomasz Napierala <trasz@FreeBSD.org>
