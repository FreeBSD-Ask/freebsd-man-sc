  HEAD(1)  

HEAD(1)

FreeBSD General Commands Manual

HEAD(1)

[名称](#__u540D___u79F0_)
=======================

`head` —

显示文件的第一行

[概要](#__u6982___u8981_)
=======================

`head` \[`-n` count | `-c` bytes\] \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

此过滤器显示每个指定文件的第一个 count 行或 bytes ，如果没有指定文件，则显示标准输入。 如果 count 被省略，则默认为 10。

可以使用以下选项：

[`-c`](#c) bytes, `--bytes`\=bytes

打印每个指定文件的 bytes 。

[`-n`](#n) count, `--lines`\=count

打印每个指定文件的 count 行。

如果指定了多个文件，则每个文件前面都有一个由字符串 “==> XXX <==” 组成的标题，其中 “XXX” 是文件的名称。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `head` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

要显示文件 foo 的前 500 行：

`$ head -n 500 foo`

`head` 可以通过以下方式与 tail(1) 结合使用，例如，仅显示文件 foo 中的第 500 行：

`$ head -n 500 foo | tail -n 1`

[参见](#__u53C2___u89C1_)
=======================

tail(1)

[历史](#__u5386___u53F2_)
=======================

`head` 命令出现在 PWB UNIX 中。

April 10, 2018

FreeBSD 13.1-RELEASE