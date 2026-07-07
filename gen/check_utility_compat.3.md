# check_utility_compat.3

`check_utility_compat` — 判断工具是否应保持兼容性

## 名称

`check_utility_compat`

## 库

libc

## 概要

`#include <unistd.h>`

```c
int
check_utility_compat(const char *utility);
```

## 描述

`check_utility_compat` 函数检查 `utility` 是否应以传统（与 FreeBSD 4.7 兼容）方式运行，还是遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。配置以逗号分隔的工具名称列表形式给出；如果列表存在但为空，则所有受支持的工具都采用其最兼容的模式。`check_utility_compat` 函数首先检查名为 `_COMPAT_FreeBSD_4` 的环境变量。如果该环境变量不存在，则 `check_utility_compat` 会尝试读取名为 **/etc/compat-FreeBSD-4-util** 的符号链接的内容。如果未找到任何配置，则禁用兼容模式。

## 返回值

如果 `utility` 应实现严格的 IEEE Std 1003.1-2001 ("POSIX.1") 行为，`check_utility_compat` 函数返回零，否则返回非零值。

## 文件

**/etc/compat-FreeBSD-4-util** 如果存在，是一个符号链接，其展开值为 `check_utility_compat` 函数提供系统范围的默认设置。

## 错误

不检测任何错误。

## 历史

`check_utility_compat` 函数首次出现于 FreeBSD 5.0。

## 作者

本手册页由 Garrett Wollman <wollman@FreeBSD.org> 编写。
