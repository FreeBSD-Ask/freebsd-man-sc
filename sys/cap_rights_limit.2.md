# cap_rights_limit(2)

`cap_rights_limit` — 限制 capability 权限

## 名称

`cap_rights_limit`

## 库

Lb libc

## 概要

`#include <sys/capsicum.h>`

```c
int
cap_rights_limit(int fd, const cap_rights_t *rights);
```

## 描述

当文件描述符由 [fhopen(2)](fhopen.2.md)、[kqueue(2)](kqueue.2.md)、[mq_open(2)](mq_open.2.md)、[open(2)](open.2.md)、[pdfork(2)](pdfork.2.md)、[pipe(2)](pipe.2.md)、[shm_open(2)](shm_open.2.md)、[socket(2)](socket.2.md) 或 [socketpair(2)](socketpair.2.md) 等函数创建时，它被赋予所有 capability 权限；对于 [accept(2)](accept.2.md)、[accept4(2)](accept.2.md) 或 [openat(2)](open.2.md)，它从 "父" 文件描述符继承 capability 权限。这些权限可以通过 `cap_rights_limit()` 系统调用减少（但绝不能扩展）。一旦 capability 权限被减少，对文件描述符的操作将仅限于 `rights` 所允许的范围。

`rights` 参数应使用 [cap_rights_init(3)](../man3/cap_rights_init.3.md) 系列函数来准备。

分配给文件描述符的 capability 权限可通过 [cap_rights_get(3)](../gen/cap_rights_get.3.md) 函数获取。

完整的 capability 权限列表可在 [rights(4)](../man4/rights.4.md) 手册页中找到。

## 返回值

成功完成时，`cap_rights_limit()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 实例

以下示例演示如何将文件描述符的 capability 权限限制为仅允许读取。

```c
cap_rights_t setrights;
char buf[1];
int fd;

fd = open("/tmp/foo", O_RDWR);
if (fd < 0)
        err(1, "open() failed");
if (cap_enter() < 0)
        err(1, "cap_enter() failed");
cap_rights_init(&setrights, CAP_READ);
if (cap_rights_limit(fd, &setrights) < 0)
        err(1, "cap_rights_limit() failed");
buf[0] = 'X';
if (write(fd, buf, sizeof(buf)) > 0)
        errx(1, "write() succeeded!");
if (read(fd, buf, sizeof(buf)) < 0)
        err(1, "read() failed");
```

## 错误

除非发生以下情况，否则 `cap_rights_limit()` 将成功：

**[`EBADF`]** `fd` 参数不是有效的活动描述符。

**[`EINVAL`]** `rights` 中请求了无效的权限。

**[`ENOSYS`]** 正在运行的内核编译时未包含 `options CAPABILITY_MODE`。

**[`ENOTCAPABLE`]** `rights` 参数包含给定文件描述符所不具备的 capability 权限。capability 权限列表只能减少，绝不能扩展。

## 参见

[accept(2)](accept.2.md), [accept4(2)](accept.2.md), [cap_enter(2)](cap_enter.2.md), [fhopen(2)](fhopen.2.md), [kqueue(2)](kqueue.2.md), [mq_open(2)](mq_open.2.md), [open(2)](open.2.md), [openat(2)](open.2.md), [pdfork(2)](pdfork.2.md), [pipe(2)](pipe.2.md), [read(2)](read.2.md), [shm_open(2)](shm_open.2.md), [socket(2)](socket.2.md), [socketpair(2)](socketpair.2.md), [write(2)](write.2.md), [cap_rights_get(3)](../gen/cap_rights_get.3.md), [cap_rights_init(3)](../man3/cap_rights_init.3.md), [err(3)](../gen/err.3.md), [capsicum(4)](../man4/capsicum.4.md), [rights(4)](../man4/rights.4.md)

## 历史

`cap_rights_limit()` 函数首次出现于 FreeBSD 8.3。对 capabilities 和 capability 模式的支持是作为 TrustedBSD 项目的一部分开发的。

## 作者

此函数由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下创建。
