# ctermid(3)

`ctermid` — 生成终端路径名

## 名称

`ctermid`, `ctermid_r`

## 库

Lb libc

## 概要

`#include <stdio.h>`

```c
char *
ctermid(char *buf);

char *
ctermid_r(char *buf);
```

## 描述

`ctermid` 函数生成一个字符串，当用作路径名时，引用调用进程的当前控制终端。

如果 `buf` 是 `NULL` 指针，则返回指向静态区域的指针。否则，路径名被复制到 `buf` 所引用的内存中。假设参数 `buf` 至少有 `L_ctermid`（定义在头文件

`#include <stdio.h>`

中）字节长。

`ctermid_r` 函数提供与 `ctermid` 相同的功能，不同之处在于如果 `buf` 是 `NULL` 指针，则返回 `NULL`。

如果无法对控制终端名称进行合适的查找，此实现返回 **/dev/tty**。

## 返回值

`ctermid` 函数在 `buf` 为非 `NULL` 时返回 `buf`，否则返回静态缓冲区的地址。`ctermid_r` 函数始终返回 `buf`，即使它是 NULL 指针。

## 错误

当前实现未检测到任何错误条件。

## 参见

[ttyname(3)](ttyname.3.md)

## 标准

`ctermid` 函数遵循 IEEE Std 1003.1-1988（"POSIX.1"）。

## 缺陷

默认情况下，`ctermid` 函数将所有信息写入内部静态对象。后续对 `ctermid` 的调用将修改同一对象。