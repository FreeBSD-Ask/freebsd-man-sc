  BASENAME(1)  

BASENAME(1)

FreeBSD General Commands Manual

BASENAME(1)

[名称](#__u540D___u79F0_)
=======================

`basename`, `dirname` —

返回路径名的文件名或目录部分

[概要](#__u6982___u8981_)
=======================

`basename` string \[suffix\] `basename` \[`-a`\] \[`-s` suffix\] string \[...\] `dirname` string \[...\]

[描述](#__u63CF___u8FF0_)
=======================

`basename` 实用程序删除任何以 string 中存在的最后一个斜杠 ‘`/`’ 字符结尾的前缀（在第一次去除尾随斜杠之后）和 suffix 如果给定的话。 如果 suffix 与 string 中的其余字符相同，则不会去除后缀。 结果文件名被写入标准输出。 不存在的后缀将被忽略。 如果指定了 `-a` ，则每个参数都被视为一个 string ，就好像只使用一个参数调用了 `basename` 。 如果指定了 `-s` ，则将 suffix 作为其参数，并将所有其他参数视为 string 。

`dirname` 实用程序删除文件名部分，从最后一个斜杠 ‘`/`’ 字符开始到 string 的末尾（在第一次去除尾部斜杠之后），并将结果写入标准输出。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `basename` and `dirname` utilities exit 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

以下行将 shell 变量 `FOO` 设置为 /usr/bin 。

```FOO=`dirname /usr/bin/trail` ```

[参见](#__u53C2___u89C1_)
=======================

csh(1), sh(1), basename(3), dirname(3)

[标准](#__u6807___u51C6_)
=======================

`basename` 和 `dirname` 实用程序应与 IEEE Std 1003.2 (“POSIX.2”) 兼容。

[历史](#__u5386___u53F2_)
=======================

`basename` 和 `dirname` 实用程序首先出现在 4.4BSD 中。

May 26, 2020

FreeBSD 13.1-RELEASE