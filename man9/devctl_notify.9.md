# devctl_notify(9)

`devctl_notify` — 通过 devctl 向用户态发送消息

## 名称

`devctl_notify`

## 概要

```c
#include <sys/devctl.h>

void
devctl_notify(const char *system, const char *subsystem,
    const char *type, const char *data)
```

## 描述

通过 [devctl(4)](../man4/devctl.4.md) 向用户态发送通知。这些消息的格式参见 [devctl(4)](../man4/devctl.4.md)。

`devctl_notify` 函数使用以下模板创建字符串：

```sh
snprintf(buffer, sizeof(buffer), "!system=%s subsystem=%s type=%s",
   system, subsystem, type);
```

`system`、`subsystem` 和 `type` 指针不能为 NULL。

`data` 参数可以为 NULL（表示无附加内容）或为 [devctl(4)](../man4/devctl.4.md) 正确格式的消息。会在上述模板后添加一个空格，并将此参数原样复制以构成传递给用户态的消息。发送者应在仅传递用户态无法自行发现的数据与传递用户态决定如何处理消息时所需的所有数据之间取得平衡。

当前总消息长度限制略低于 1kb。发送者应尽量保持远低于此限制。

## 参见

[devctl(4)](../man4/devctl.4.md), devd(8)

## 作者

本手册页由 M. Warner Losh 编写。
