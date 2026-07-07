# confstr(3)

`confstr` — 获取字符串类型的可配置变量

## 名称

`confstr`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
size_t
confstr(int name, char *buf, size_t len);
```

## 描述

此接口由 IEEE Std 1003.1-2001 ("POSIX.1") 规定。[sysctl(3)](sysctl.3.md) 提供了更灵活（但不可移植）的接口。

`confstr` 函数为应用程序提供了一种获取配置定义的字符串值的方法。需要访问这些参数的 shell 程序员应使用 getconf(1) 实用程序。

`name` 参数指定要查询的系统变量。每个 name 值的符号常量可在包含文件 `<unistd.h>` 中找到。

`len` 参数指定 `buf` 参数所引用缓冲区的大小。如果 `len` 非零，`buf` 是非空指针，且 `name` 有值，则最多将 `len` - 1 字节的值复制到缓冲区 `buf` 中。复制的值始终以 null 结尾。

可用的值如下：

**`_CS_PATH`** 返回 `PATH` 环境变量的值，用于查找所有标准实用程序。

## 返回值

如果对 `confstr` 的调用不成功，返回 0 并适当设置 `errno`。否则，如果变量没有配置定义的值，返回 0 且不修改 `errno`。否则，返回保存整个配置定义值所需的缓冲区大小。如果此大小大于参数 `len`，则 `buf` 中的字符串已被截断。

## 错误

`confstr` 函数可能失败并为库函数 malloc(3) 和 [sysctl(3)](sysctl.3.md) 指定的任何错误设置 `errno`。

此外，可能报告以下错误：

**[`EINVAL`]** `name` 参数的值无效。

## 参见

getconf(1), [pathconf(2)](../sys/pathconf.2.md), [sysconf(3)](sysconf.3.md), [sysctl(3)](sysctl.3.md)

## 历史

`confstr` 函数首次出现于 4.4BSD。
