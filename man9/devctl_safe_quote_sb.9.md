# devctl_safe_quote_sb(9)

`devctl_safe_quote_sb` — 将正确转义的字符串插入 sbuf

## 名称

`devctl_safe_quote_sb`

## 概要

```c
#include <sys/devctl.h>
#include <sys/sbuf.h>

void
devctl_safe_quote_sb(struct sbuf *sb, const char *src)
```

## 描述

将字符串从 `src` 复制到 `sb`。所有反斜杠字符都被双写。所有双引号字符‘"’前也会加一个反斜杠。所有其他字符均原样复制。[devctl(4)](../man4/devctl.4.md) 协议要求引号字符串按此方式转义。此例程集中了此知识。

## 参见

devd(8)

## 作者

本手册页由 M. Warner Losh 编写。
