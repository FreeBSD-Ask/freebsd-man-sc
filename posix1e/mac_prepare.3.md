# mac_prepare(3)

`mac_prepare` — 为 MAC 标签分配适当的存储空间

## 名称

`mac_prepare`, `mac_prepare_type`, `mac_prepare_file_label`, `mac_prepare_ifnet_label`, `mac_prepare_process_label`

## 概要

`#include <sys/mac.h>`

```c
int
mac_prepare(mac_t *mac, const char *elements);

int
mac_prepare_type(mac_t *mac, const char *name);

int
mac_prepare_file_label(mac_t *mac);

int
mac_prepare_ifnet_label(mac_t *mac);

int
mac_prepare_process_label(mac_t *mac);
```

## 描述

`mac_prepare_ifnet_label` 系列函数分配适当数量的存储空间，并初始化 `*mac` 以供 [mac_get(3)](mac_get.3.md) 使用。当生成的标签传递给 [mac_get(3)](mac_get.3.md) 函数时，内核将尝试填充在准备标签时指定的标签元素。元素以 `null` 结尾的字符串指定，使用逗号分隔字段。元素名称可以加 `?` 前缀，表示内核检索该元素失败不应视为致命错误。

`mac_prepare` 函数接受策略名称列表作为参数，并分配存储空间以容纳相应的标签元素。该系列中的其余函数使用 mac.conf(5) 中定义的系统默认值，而非显式的 `elements` 参数，从指定的对象类型派生默认值。

`mac_prepare_type` 分配存储空间以容纳由 `name` 参数指定类型的对象标签。`mac_prepare_file_label`、`mac_prepare_ifnet_label` 和 `mac_prepare_process_label` 函数分别等效于以 `file`、`ifnet` 和 `process` 为参数调用 `mac_prepare_type`。

## 返回值

成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 参见

[mac(3)](mac.3.md), [mac_free(3)](mac_free.3.md), [mac_get(3)](mac_get.3.md), [mac_is_present(3)](mac_is_present.3.md), [mac_set(3)](mac_set.3.md), [mac(4)](../man4/mac.4.md), mac.conf(5), [maclabel(7)](../man7/maclabel.7.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

对强制访问控制（Mandatory Access Control）的支持作为 TrustedBSD 项目的一部分引入于 FreeBSD 5.0。对通用对象类型的支持首次出现于 FreeBSD 5.2。
