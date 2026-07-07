# realpath(1)

`realpath` — 返回解析后的物理路径

## 名称

`realpath`

## 概要

`realpath [-q] [path ...]`

## 描述

`realpath` 实用程序使用 realpath(3) 函数解析 `path` 中的所有符号链接、多余的 `/` 字符以及对 **`/./`** 和 **`/../`** 的引用。如果未提供 `path`，则假定使用当前工作目录（‘`.`’）。

如果指定了 `-q`，则在 realpath(3) 失败时不打印警告。

## 退出状态

`realpath` 实用程序成功时退出码为 0，发生错误时大于 0。

## 实例

显示 **`/dev/log`** 目录的物理路径，并抑制任何警告：

```sh
$ realpath -q /dev/log
/var/run/log
```

## 参见

realpath(3)

## 历史

`realpath` 实用程序首次出现于 FreeBSD 4.3。
