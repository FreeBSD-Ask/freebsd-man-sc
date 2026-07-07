# mac_free(3)

`mac_free` — 释放 MAC 标签

## 名称

`mac_free`

## 库

libc

## 概要

`#include <sys/mac.h>`

```c
int
mac_free(mac_t label);
```

## 描述

`mac_free` 函数释放为容纳 `mac_t` 而分配的存储空间。

## 返回值

`mac_free` 函数始终返回 0。警告：关于该函数的使用，请参阅缺陷章节中的说明。

## 参见

[mac(3)](mac.3.md), [mac_get(3)](mac_get.3.md), [mac_prepare(3)](mac_prepare.3.md), [mac_set(3)](mac_set.3.md), [mac_text(3)](mac_text.3.md), [posix1e(3)](posix1e.3.md), [mac(4)](../man4/mac.4.md), [mac(9)](../man9/mac.9.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

对强制访问控制（Mandatory Access Control）的支持作为 TrustedBSD 项目的一部分引入于 FreeBSD 5.0。

## 缺陷

POSIX.1e 规定 `mac_free` 将用于释放由 [mac_to_text(3)](mac_text.3.md) 创建的文本字符串。由于 `mac_t` 在 TrustedBSD 实现中是一个复杂结构，`mac_free` 专用于 `mac_t`，不得用于释放由 `mac_to_text` 返回的字符串。这样做可能导致未定义行为。
