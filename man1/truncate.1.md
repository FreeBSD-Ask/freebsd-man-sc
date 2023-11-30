  TRUNCATE(1)  

TRUNCATE(1)

FreeBSD General Commands Manual

TRUNCATE(1)

[名称](#__u540D___u79F0_)
=======================

`truncate` —

截断或延长文件的长度

[概要](#__u6982___u8981_)
=======================

`truncate` \[`-c`\] `-s` \[`+`|`-` | `%`|`/`\]size\[`K`|`k`|`M`|`m`|`G`|`g`|`T`|`t`\] file ... `truncate` \[`-c`\] `-r` rfile file ...

[描述](#__u63CF___u8FF0_)
=======================

`truncate` 实用程序调整命令行中给出的每个常规文件的长度。

可以使用以下选项：

[`-c`](#c)

如果文件不存在，请不要创建它们。 `truncate` 实用程序不会将此视为错误。 不显示错误消息，退出值不受影响。

[`-r`](#r) rfile

截断或扩展文件到文件 rfile 的长度。

[`-s`](#s) \[`+`|`-`|`%`|`/`\]size\[`K`|`k`|`M`|`m`|`G`|`g`|`T`|`t`\]

如果 size 参数前面有加号 (`+`), 则文件将扩展此字节数。 如果 size 参数前面有一个破折号 (`-`), 则文件长度将减少不超过此字节数，最小长度为零字节。 如果 size 参数前面有百分号 (`%`), 则文件将向上舍入到此字节数的倍数。 如果 size 参数前面有斜杠 (`/`), 则文件将向下舍入到此字节数的倍数，最小长度为零字节。否则， size 参数指定一个绝对长度，所有文件都应该适当地扩展或缩减到该长度。

size 参数可以后缀为 `K`, `M`, `G` 或 `T` （大写或小写）之一，分别表示千字节、兆字节、千兆字节或太字节的倍数。

必须指定 `-r` 和 `-s` 选项之一。

如果文件变小，则其额外数据将丢失。 如果文件变大，它将被扩展，就好像通过写入值为零的字节一样。 如果文件不存在，除非指定 `-c` 选项，否则将创建它。

请注意，虽然截断文件会释放磁盘空间，但扩展文件不会导致分配空间。 要扩展文件并实际分配空间，必须使用（例如）shell 的 ‘`>>`’ 重定向语法或 dd(1) 显式地向其写入数据。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `truncate` utility exits 0 on success, and >0 if an error occurs. 如果某个参数的操作失败，则 `truncate` 将发出诊断信息并继续处理剩余的参数。

[实例](#__u5B9E___u4F8B_)
=======================

将文件 test\_file 的大小调整为 10 MB，但如果它不存在则不要创建它：

truncate -c -s +10M test\_file 

与上面相同，但如果文件不存在则创建文件：

truncate -s +10M test\_file ls -l test\_file -rw-r--r-- 1 root wheel 10485760 Jul 22 18:48 test\_file 

将 test\_file 的大小调整为内核的大小，并创建另一个相同大小的文件 test\_file2 :

truncate -r /boot/kernel/kernel test\_file test\_file2 ls -l /boot/kernel/kernel test\_file\* -r-xr-xr-x 1 root wheel 31352552 May 15 14:18 /boot/kernel/kernel\* -rw-r--r-- 1 root wheel 31352552 Jul 22 19:15 test\_file -rw-r--r-- 1 root wheel 31352552 Jul 22 19:15 test\_file2 

将 test\_file 缩小到 5 MB：

\# truncate -s -5M test\_file ls -l test\_file\* -rw-r--r-- 1 root wheel 26109672 Jul 22 19:17 test\_file -rw-r--r-- 1 root wheel 31352552 Jul 22 19:15 test\_file2 

[参见](#__u53C2___u89C1_)
=======================

dd(1), touch(1), truncate(2)

[标准](#__u6807___u51C6_)
=======================

`truncate` 实用程序不符合任何已知标准。

[历史](#__u5386___u53F2_)
=======================

`truncate` 实用程序首先出现在 FreeBSD 4.2 中。

[作者](#__u4F5C___u8005_)
=======================

`truncate` 实用程序由 Sheldon Hearn <[sheldonh@starjuice.net](mailto:sheldonh@starjuice.net)\> 编写。

July 27, 2020

FreeBSD 13.1-RELEASE