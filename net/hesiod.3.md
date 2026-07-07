# hesiod(3)

`hesiod` — Hesiod 名字服务器接口库

## 名称

`hesiod`, `hesiod_init`, `hesiod_resolve`, `hesiod_free_list`, `hesiod_to_bind`, `hesiod_end`

## 库

libc

## 概要

`#include <hesiod.h>`

```c
int
hesiod_init(void **context);

char **
hesiod_resolve(void *context, const char *name, const char *type);

void
hesiod_free_list(void *context, char **list);

char *
hesiod_to_bind(void *context, const char *name, const char *type);

void
hesiod_end(void *context);
```

## 描述

这一族函数允许你查找 Hesiod 信息，这些信息以文本记录的形式存储在域名服务（DNS）中。要进行查找，你必须首先初始化一个 `context`（上下文），这是一个不透明对象，用于存储库在调用之间内部使用的信息。`hesiod_init` 函数初始化一个上下文，将指向该上下文的指针存储在 `context` 参数所指向的位置。`hesiod_end` 函数释放上下文所使用的资源。

`hesiod_resolve` 函数是该库的主要接口。如果成功，它返回一个包含一个或多个字符串的列表，这些字符串给出了与 `name` 和 `type` 匹配的记录。列表的最后一个元素后跟一个 `NULL` 指针。调用者有责任调用 `hesiod_free_list` 来释放返回列表所使用的资源。

`hesiod_to_bind` 函数将 `name` 和 `type` 转换为 `hesiod_resolve` 所使用的 DNS 名称。调用者有责任使用 `free` 释放返回的字符串。

## 返回值

成功时，`hesiod_init` 返回 0。失败时，`hesiod_resolve` 和 `hesiod_to_bind` 返回 `NULL`，并设置全局变量 `errno` 以指示错误。

## 环境变量

**`HES_DOMAIN`** 如果设置了环境变量 `HES_DOMAIN`，它将覆盖 Hesiod 配置文件中的域。

**`HESIOD_CONFIG`** 如果设置了环境变量 `HESIOD_CONFIG`，它指定 Hesiod 配置文件的位置。

## 错误

Hesiod 调用可能因以下原因失败：

**[ENOMEM]** 没有足够的内存来执行所请求的操作。

**[ENOEXEC]** `hesiod_init` 函数失败，因为 Hesiod 配置文件无效。

**[ECONNREFUSED]** `hesiod_resolve` 函数失败，因为无法联系到任何名字服务器来应答查询。

**[EMSGSIZE]** `hesiod_resolve` 或 `hesiod_to_bind` 函数失败，因为查询或响应太大，无法放入数据包缓冲区。

**[ENOENT]** `hesiod_resolve` 函数失败，因为名字服务器没有与 `name` 和 `type` 匹配的文本记录；或 `hesiod_to_bind` 失败，因为 `name` 参数具有的域扩展无法在本地 Hesiod 域中以 "rhs-extension" 类型解析。

## 参见

[hesiod.conf(5)](../man5/hesiod.conf.5.md)

> "Hesiod - Project Athena Technical Plan -- Name Service".

## 作者

Steve Dyer, IBM/Project Athena

Greg Hudson, MIT Team Athena

Copyright 1987, 1988, 1995, 1996 by the Massachusetts Institute of Technology.

## 缺陷

与 Hesiod 函数设置的 `errno` 值对应的字符串并不能特别说明出了什么问题，尤其是 `ENOEXEC` 和 `ENOENT`。
