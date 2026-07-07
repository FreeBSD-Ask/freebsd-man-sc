# getprogname(3)

`getprogname` — 获取或设置程序名

## 名称

`getprogname`, `setprogname`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
const char *
getprogname(void);

void
setprogname(const char *progname);
```

## 描述

`getprogname` 和 `setprogname` 函数操作当前程序的名称。错误报告例程使用它们来产生一致的输出。

`getprogname` 函数返回程序名。如果名称尚未设置，则返回 `NULL`。

`setprogname` 函数将程序名设置为 `progname` 参数的最后一个组件。由于指向给定字符串的指针被保留作为程序名，因此在程序生命周期的剩余时间内不应修改它。

在 FreeBSD 中，程序名由 `main` 之前运行的启动代码设置；因此，运行 `setprogname` 不是必需的。期望最大可移植性的程序仍应调用它；在另一个操作系统上，这些函数可能在可移植性库中实现。调用 `setprogname` 允许上述库获知程序名，而无需修改启动代码。

## 实例

以下示例展示了一个简单程序，它显示 `getprogname` 和 `argv[0]` 之间的区别。

```c
#include <stdio.h>
#include <stdlib.h>
int
main(int argc, char** argv)
{
        printf("getprogname(): %s\n", getprogname());
        printf("argv[0]: %s\n", argv[0]);
        return (0);
}
```

编译并执行后（例如，使用 `./a.out`），程序的输出如下所示：

```sh
getprogname(): a.out
argv[0]: ./a.out
```

## 参见

[err(3)](err.3.md), [setproctitle(3)](setproctitle.3.md)

## 历史

这些函数首次出现于 NetBSD 1.6，并进入 FreeBSD 4.4。
