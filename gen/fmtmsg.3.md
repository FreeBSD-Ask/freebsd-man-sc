# fmtmsg(3)

`fmtmsg` — 显示详细的诊断消息

## 名称

`fmtmsg`

## 库

libc

## 概要

`#include <fmtmsg.h>`

```c
int
fmtmsg(long classification, const char *label, int severity,
    const char *text, const char *action, const char *tag);
```

## 描述

`fmtmsg` 函数根据所提供的参数，向 `stderr` 和/或系统控制台显示一条详细的诊断消息。

`classification` 参数是以下各分类组中零个或一个清单常量的按位或。输出分类组是例外，因为 `MM_PRINT` 和 `MM_CONSOLE` 可以同时指定。

**`MM_PRINT`** 输出应在 `stderr` 上进行。

**`MM_CONSOLE`** 输出应在系统控制台上进行。

**`MM_HARD`** 该情况的来源与硬件相关。

**`MM_SOFT`** 该情况的来源与软件相关。

**`MM_FIRM`** 该情况的来源与固件相关。

**`MM_APPL`** 该情况在应用程序层被检测到。

**`MM_UTIL`** 该情况在工具层被检测到。

**`MM_OPSYS`** 该情况在操作系统层被检测到。

**`MM_RECOVER`** 应用程序可从该情况中恢复。

**`MM_NRECOV`** 应用程序无法从该情况中恢复。

**输出**

**情况来源**（主要）

**情况来源**（次要）

**状态**

或者，可以使用 `MM_NULLMC` 清单常量来指定无分类。

`label` 参数指示消息的来源。它由以冒号（`:`）分隔的两个字段组成。第一个字段最多 10 字节，第二个字段最多 14 字节。可以使用 `MM_NULLLBL` 清单常量来指定无标签。

`severity` 参数标识该情况的重要程度。此参数应使用以下清单常量之一。

**`MM_HALT`** 应用程序遇到严重故障并正在停止。

**`MM_ERROR`** 应用程序检测到一个故障。

**`MM_WARNING`** 应用程序检测到一个异常情况，可能表示存在问题。

**`MM_INFO`** 应用程序正在提供关于非错误情况的信息。

**`MM_NOSEV`** 未提供严重级别。

`text` 参数详述导致该消息的错误情况。此字符串的长度没有限制。可以使用 `MM_NULLTXT` 清单常量来指定无文本。

`action` 参数详述错误恢复过程应如何开始。输出时，`fmtmsg` 会在 `action` 参数的开头加上 `TO FIX:` 前缀。可以使用 `MM_NULLACT` 清单常量来指定无操作。

`tag` 参数应引用该消息的在线文档。这通常包括 `label` 和一个唯一标识编号。一个标签示例是 `BSD:ls:168`。可以使用 `MM_NULLTAG` 清单常量来指定无标签。

## 返回值

`fmtmsg` 函数成功时返回 `MM_OK` ；向 `stderr` 输出失败时返回 `MM_NOMSG` ；向系统控制台输出失败时返回 `MM_NOCON` ；向 `stderr` 和系统控制台输出均失败时返回 `MM_NOTOK` 。

## 环境变量

`MSGVERB` （消息详细级别）环境变量指定 `fmtmsg` 的哪些参数将输出到 `stderr` ，以及以何种顺序输出。`MSGVERB` 应为一个以冒号（`:`）分隔的标识符列表。有效的标识符包括：`label` 、 `severity` 、 `text` 、 `action` 和 `tag` 。如果指定了无效的标识符或分隔不正确，将使用默认的消息详细级别和顺序。默认顺序等同于 `MSGVERB` 的值为 `label:severity:text:action:tag` 。

## 实例

代码：

```c
fmtmsg(MM_UTIL | MM_PRINT, "BSD:ls", MM_ERROR,
    "illegal option -- z", "refer to manual", "BSD:ls:001");
```

将向 `stderr` 输出：

```sh
BSD:ls: ERROR: illegal option -- z
TO FIX: refer to manual BSD:ls:001
```

相同的代码，在 `MSGVERB` 设置为 `text:severity:action:tag` 时，产生：

```sh
illegal option -- z: ERROR
TO FIX: refer to manual BSD:ls:001
```

## 参见

[err(3)](err.3.md), exit(3), strerror(3)

## 标准

`fmtmsg` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。

## 历史

`fmtmsg` 函数首次出现于 FreeBSD 5.0。

## 缺陷

为 `classification` 参数指定 `MM_NULLMC` 几乎没有意义，因为在未指定输出的情况下，`fmtmsg` 无法做任何有用的事情。

为使 `fmtmsg` 能够向系统控制台输出，有效用户必须具有写入 **/dev/console** 的适当权限。这意味着在大多数系统上，除非有效用户为 root，`fmtmsg` 将返回 `MM_NOCON` 。
