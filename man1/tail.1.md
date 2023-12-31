  TAIL(1)  

TAIL(1)

FreeBSD General Commands Manual

TAIL(1)

[名称](#__u540D___u79F0_)
=======================

`tail` —

显示文件的最后一部分

[概要](#__u6982___u8981_)
=======================

`tail` \[`-F` | `-f` | `-r`\] \[`-q`\] \[`-b` number | `-c` number | `-n` number\] \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`tail` 实用程序将 file 的内容或默认情况下其标准输入的内容显示到标准输出。

显示从输入中的字节、行或 512 字节块位置开始。 带有前导加号 (‘`+`’) 的数字相对于输入的开头，例如， “`-c +2`” 从输入的第二个字节开始显示。 具有前导减号 (‘`-`’) 符号或没有显式符号的数字相对于输入的结尾，例如， “`-n 2`” 显示输入的最后两行。 默认起始位置是 “`-n 10`” ，即输入的最后 10 行。

选项如下：

[`-b`](#b) number, `--blocks`\=number

该位置是 number 为 512 字节的块。

[`-c`](#c) number, `--bytes`\=number

位置是 number 字节。

[`-f`](#f)

[`-f`](#f_2) 选项导致 `tail` 在到达文件末尾时不停止，而是等待附加数据附加到输入。 如果标准输入是管道，则忽略 `-f` 选项，但如果它是 FIFO，则不会。

[`-F`](#F)

[`-F`](#F_2) 选项暗示了 `-f` 选项，但是 `tail` 也会检查被跟踪的文件是否被重命名或旋转。 当 `tail` 检测到正在读取的文件名具有新的 inode 编号时，该文件将关闭并重新打开。

如果被跟踪的文件（尚）不存在或已被删除，tail 将继续查找并在创建文件时从头开始显示该文件。

如果从标准输入而不是文件读取，则 `-F` 选项与 `-f` 选项相同。

[`-n`](#n) number, `--lines`\=number

位置是 number 行。

[`-q`](#q)

在检查多个文件时禁止打印标题。

[`-r`](#r)

[`-r`](#r_2) 选项使输入以相反的顺序按行显示。 此外，此选项会更改 `-b`, `-c` 和 `-n` 选项的含义。 当指定 `-r` 选项时，这些选项指定要显示的字节数、行数或 512 字节块数，而不是从开始显示的输入的开头或结尾的字节数、行数或块数。 `-r` 选项的默认设置是显示所有输入。

如果指定了多个文件，则每个文件前面都有一个由字符串 “`==>` XXX `<==`” 组成的标题，其中 XXX 是文件的名称，除非指定了 `-q` 标志。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `tail` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

要显示文件 foo 的最后 500 行：

`$ tail -n 500 foo`

保持 /var/log/messages 打开，向标准输出显示附加到文件的任何内容：

`$ tail -F /var/log/messages`

[参见](#__u53C2___u89C1_)
=======================

cat(1), head(1), sed(1)

[标准](#__u6807___u51C6_)
=======================

`tail` 实用程序有望成为 IEEE Std 1003.2-1992 (“POSIX.2”) 规范的超集。 特别是， `-F`, `-b` 和 `-r` 选项是对该标准的扩展。

此实现支持 `tail` 的历史命令行语法。 此实现与 of `tail` 历史版本之间的唯一区别是，一旦完成命令行语法转换， `-b`, `-c` 和 `-n` 选项会修改 `-r` 选项，即显示 “`-r -c 4`” 输入最后一行的最后 4 个字符，而历史尾部（使用历史语法 “`-4cr`” ）将忽略 `-c` 选项并显示输入的最后 4 行。

[历史](#__u5386___u53F2_)
=======================

`tail` 命令出现在 PWB UNIX 中。

March 22, 2020

FreeBSD 13.1-RELEASE