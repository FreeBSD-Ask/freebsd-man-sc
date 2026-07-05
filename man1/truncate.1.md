# truncate.1

`truncate` — 调整文件大小或管理文件空间

## 名称

`truncate`

## 概要

`truncate [-c] -s [[+ | - | % | /]size[SUFFIX]] file ...`

`truncate [-c] -r rfile file ...`

`truncate [-c] -d [-o offset[SUFFIX]] -l length[SUFFIX] file ...`

## 描述

`truncate` 实用程序调整命令行上给出的每个常规文件的长度，或对命令行上给出的常规文件按指定偏移量和长度执行空间管理。

以下选项可用：

**`-c`** 如果文件不存在则不创建。`truncate` 实用程序不将此视为错误。不显示错误消息，退出值不受影响。

**`-r`** `rfile` 将文件截断或扩展到文件 `rfile` 的长度。

**`-s`** [[+ | - | % | /]]`size`[`SUFFIX`] 如果 `size` 参数以加号（`+`）开头，文件将扩展此字节数。如果 `size` 参数以减号（`-`）开头，文件长度将减少不超过此字节数，最小长度为零字节。如果 `size` 参数以百分号（`%`）开头，文件将向上取整到此字节数的倍数。如果 `size` 参数以斜杠（`/`）开头，文件将向下取整到此字节数的倍数，最小长度为零字节。否则，`size` 参数指定一个绝对长度，所有文件将据此适当扩展或缩减。

**`-d`** 将指定文件中的某个区域清零。如果给定文件所在文件系统支持打洞（hole-punching），可在操作区域执行文件系统空间释放。

**`-o`** `offset` 空间管理操作在文件中给定的 `offset` 字节处执行。如果未指定此选项，操作在文件开头执行。

**`-l`** `length` 操作范围的字节长度。如果指定了 `-d` 选项，则必须始终指定此选项，且必须大于 0。

`size`、`offset` 和 `length` 参数可后跟 `K`、`M`、`G` 或 `T` 之一（大写或小写均可），分别表示千字节、兆字节、吉字节或太字节的倍数。

必须指定 `-r`、`-s` 和 `-d` 选项中的一个且仅一个。

如果文件变小，其多余数据将丢失。如果文件变大，将如同写入值为零的字节一样扩展。如果文件不存在，除非指定了 `-c` 选项，否则将创建它。

注意，截断文件会释放磁盘空间，但扩展文件不会分配空间。要扩展文件并实际分配空间，需要显式向其写入数据，例如使用 shell 的 `>>` 重定向语法或 [dd(1)](dd.1.md)。

## 退出状态

`truncate` 实用程序成功时退出 0，发生错误时退出 >0。

如果某个参数的操作失败，`truncate` 将发出诊断信息并继续处理剩余参数。

## 实例

将文件 `test_file` 的大小调整为 10 兆字节，但如果不存在则不创建：

```sh
truncate -c -s 10M test_file
```

与上例相同，但如果不存在则创建文件：

```sh
truncate -s +10M test_file
ls -lh test_file
-rw-r--r--  1 root  wheel    10M Jul 22 18:48 test_file
```

将 `test_file` 的大小调整为内核的大小，并创建另一个相同大小的文件 `test_file2`：

```sh
truncate -r /boot/kernel/kernel test_file test_file2
ls -lh /boot/kernel/kernel test_file*
-r--r--r--  1 root  wheel    30M May 15 14:18 /boot/kernel/kernel
-rw-r--r--  1 root  wheel    30M Jul 22 19:15 test_file
-rw-r--r--  1 root  wheel    30M Jul 22 19:15 test_file2
```

将文件 `test_file` 的大小增加 5 兆字节，但如果不存在则不创建：

```sh
truncate -s +5M test_file
ls -l test_file*
-rw-r--r--  1 root  wheel    36595432 Sep 20 19:17 test_file
-rw-r--r--  1 root  wheel    31352552 Sep 20 19:15 test_file2
```

将文件 `test_file` 的大小减少 5 兆字节：

```sh
truncate -s -5M test_file
ls -lh test_file*
-rw-r--r--  1 root  wheel    25M Jul 22 19:17 test_file
-rw-r--r--  1 root  wheel    30M Jul 22 19:15 test_file2
```

## 参见

[dd(1)](dd.1.md), [touch(1)](touch.1.md), fspacectl(2), truncate(2)

## 标准

`truncate` 实用程序不符合任何已知标准。

## 历史

`truncate` 实用程序首次出现于 FreeBSD 4.2。

## 作者

`truncate` 实用程序由 Sheldon Hearn <sheldonh@starjuice.net> 编写。此实用程序的打洞支持由 Ka Ho Ng <khng@FreeBSD.org> 开发。
