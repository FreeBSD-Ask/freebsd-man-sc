  CKSUM(1)  

CKSUM(1)

FreeBSD General Commands Manual

CKSUM(1)

[名称](#__u540D___u79F0_)
=======================

`cksum`, `sum` —

显示文件校验和和块计数

[概要](#__u6982___u8981_)
=======================

`cksum` \[`-o` 1 | 2 | 3\] \[file ...\] `sum` \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`cksum` 实用程序将每个输入文件的三个空格分隔字段写入标准输出。 这些字段是校验和 CRC 、文件中的八位字节总数和文件名。 如果未指定文件名，则使用标准输入并且不写入文件名。

`sum` 实用程序与 `cksum` 实用程序相同，只是它默认使用历史算法 1，如下所述。 它只是为了兼容性而提供的。

选项如下：

[`-o`](#o)

使用历史算法而不是（高级）默认算法。

算法 1 是历史 BSD 系统用作 sum(1) 算法和历史 AT&T System V UNIX 系统在使用 `-r` 选项时用作 sum(1) 算法的算法。 这是一个 16 位的校验和，每次加法前都有一个右旋转；溢出被丢弃。

算法 2 是历史上 AT&T System V UNIX 系统用作默认 sum(1) 算法的算法。 这是一个 32 位校验和，定义如下：

s = sum of all bytes; r = s % 2^16 + (s % 2^32) / 2^16; cksum = (r % 2^16) + r / 2^16; 

算法 3 就是通常所说的 ‘`32 位 CRC`’ 算法。 这是一个 32 位校验和。

算法 1 和 2 都向标准输出写入与默认算法相同的字段，只是文件大小（以字节为单位）被替换为文件的大小（以块为单位）。 由于历史原因，算法 1 的块大小为 1024，算法 2 的块大小为 512。 部分区块被四舍五入。

使用的默认 CRC 基于网络标准 ISO 8802-3: 1989 中用于 CRC 错误检查的多项式。 CRC 校验和编码由生成多项式定义：

G(x) = x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1 

在数学上，与给定文件对应的 CRC 值由以下过程定义：

要评估的 n 位被认为是 n\-1 次的 mod 2 多项式 M(x) 的系数。 这 n 位是文件中的位，最高有效位是文件第一个八位字节的最高有效位，最后一位是最后一个八位字节的最低有效位，用零位（如果需要）填充以获得整数个八位位组，后跟一个或多个八位位组，将文件的长度表示为二进制值，最低有效八位位组在前。 使用能够表示该整数的最少八位字节数。

M(x) 乘以 x^32（即左移 32 位）并使用 mod 2 除法除以 G(x)，产生度数 <= 31 的余数 R(x)。

R(x) 的系数被认为是一个 32 位序列。

对位序列进行补码，结果为 CRC。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `cksum` and `sum` utilities exit 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

md5(1)

默认计算与以下 ACM 文章中的伪代码中给出的计算相同。 Dilip V. Sarwate, Computation of Cyclic Redundancy Checks Via Table Lookup, _Communications of the Tn ACM_, August 1988.

[标准](#__u6807___u51C6_)
=======================

`cksum` 实用程序应符合 IEEE Std 1003.2-1992 (“POSIX.2”) 。

[历史](#__u5386___u53F2_)
=======================

`cksum` 实用程序出现在 4.4BSD 中。

April 28, 1995

FreeBSD 13.1-RELEASE