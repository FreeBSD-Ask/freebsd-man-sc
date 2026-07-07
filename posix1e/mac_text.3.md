# mac_text(3)

`mac_from_text` — 在 MAC 标签与文本表示之间转换

## 名称

`mac_from_text`, `mac_to_text`

## 库

libc

## 概要

`#include <sys/mac.h>`

```c
int
mac_from_text(mac_t *mac, const char *text);
```

```c
int
mac_to_text(mac_t label, char **text);
```

## 描述

`mac_from_text` 函数将标签的文本表示转换为内部策略标签格式（`mac_t`），并将其置于 `*mac` 中，该内存随后必须通过 [mac_free(3)](mac_free.3.md) 释放。

`mac_to_text` 函数为 `*text` 分配存储空间，该空间将被设置为 `label` 的文本表示，随后必须通过 free(3) 释放。

关于 MAC 标签格式，请参阅 [maclabel(7)](../man7/maclabel.7.md)。

## 返回值

成功完成时，`mac_from_text` 和 `mac_to_text` 函数返回 0。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 兼容性

POSIX.1e 未定义 MAC 标签文本表示的格式。

POSIX.1e 要求使用 `mac_to_text` 分配的文本字符串通过 [mac_free(3)](mac_free.3.md) 释放；在 FreeBSD 实现中，必须使用 free(3) 释放，因为 [mac_free(3)](mac_free.3.md) 仅用于释放 `mac_t` 类型所占用的内存。

## 错误

`[ENOMEM]` 内存不足，无法分配内部存储。

## 参见

free(3), [mac(3)](mac.3.md), [mac_free(3)](mac_free.3.md), [mac_get(3)](mac_get.3.md), [mac_is_present(3)](mac_is_present.3.md), [mac_prepare(3)](mac_prepare.3.md), [mac_set(3)](mac_set.3.md), [posix1e(3)](posix1e.3.md), [mac(4)](../man4/mac.4.md), [maclabel(7)](../man7/maclabel.7.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

强制访问控制支持作为 TrustedBSD 项目的一部分引入于 FreeBSD 5.0。
