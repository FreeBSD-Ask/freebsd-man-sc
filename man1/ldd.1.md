# ldd.1

`ldd` — 列出动态对象依赖

## 名称

`ldd`

## 概要

`ldd [-a] [-f format [-f format]] program ...`

## 描述

`ldd` 实用程序显示运行给定程序或加载给定共享对象所需的所有共享对象。与 nm(1) 不同，该列表包括"间接"依赖，即所需的共享对象本身又依赖于其他共享对象所产生的依赖。

可以给出零个、一个或两个 `-f` 选项。其参数为传递给 rtld(1) 的格式字符串，允许自定义 `ldd` 的输出。如果给出一个，则设置 `LD_TRACE_LOADED_OBJECTS_FMT1`。如果给出两个，则分别设置 `LD_TRACE_LOADED_OBJECTS_FMT1` 和 `LD_TRACE_LOADED_OBJECTS_FMT2`。有关详细信息，包括可识别的转换字符列表，请参见 rtld(1)。

`-a` 选项显示每个加载对象所需的所有对象的列表。

## 实现说明

`ldd` 通过设置 rtld(1) 环境变量并在子进程中运行可执行文件来列出其依赖项。如果可执行文件损坏或无效，`ldd` 可能因此失败，而不提供任何诊断错误消息。

## 实例

以下是使用 `-f` 选项的 shell 管道示例。它将打印当前目录中所有链接到旧版 libc.so.6 的 ELF 二进制文件的报告：

```sh
find . -type f | xargs file -F ' ' | grep 'ELF.*dynamically' | cut -f1 -d' ' | xargs ldd -f '%A %o\n' | grep -F libc.so.6
```

## 参见

[ld(1)](ld.1.md), nm(1), [readelf(1)](readelf.1.md), rtld(1)

## 历史

`ldd` 实用程序首次出现于 SunOS 4.0，其当前形式出现于 FreeBSD 1.1。
