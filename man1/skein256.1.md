  MD5(1)  

MD5(1)

FreeBSD General Commands Manual

MD5(1)

[名称](#__u540D___u79F0_)
=======================

`md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `sha512t256`, `rmd160`, `skein256`, `skein512`, `skein1024` —

计算文件的消息摘要指纹（校验和）

[概要](#__u6982___u8981_)
=======================

`md5` \[`-pqrtx`\] \[`-c` string\] \[`-s` string\] \[file ...\]

(All other hashes have the same options and usage.)

[描述](#__u63CF___u8FF0_)
=======================

The `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `sha512t256`, `rmd160`, `skein256`, `skein512` 和 `skein1024` 实用程序将任意长度的消息作为输入，并生成输入的 “fingerprint” 或 “message digest” 作为输出。 推测产生具有相同消息摘要的两个消息或产生具有给定的预定目标消息摘要的任何消息在计算上是不可行的。 SHA-224 , SHA-256 , SHA-384 , SHA-512, RIPEMD-160, 和 SKEIN 算法适用于数字签名应用程序，其中必须以安全方式 “compressed” 大文件，然后才能使用私有加密公钥密码系统（如 RSA）下的（秘密）密钥。

MD5 和 SHA-1 算法已被证明容易受到实际冲突攻击，不应依赖它们产生唯一的输出，也不应将它们用作加密签名方案的一部分。 截至 2017 年 3 月 2 日，没有公开已知的方法来 _reverse_ 任一算法，即找到产生特定输出的输入。

SHA-512t256 是 SHA-512 的一个版本，仅截断为 256 位。 在 64 位硬件上，此算法比 SHA-256 快大约 50%，但安全级别相同。-
哈希值不可互换。

建议所有新应用程序使用 SHA-512 或 SKEIN-512 而不是其他哈希函数之一。

以下选项可以任意组合使用，并且必须位于命令行中命名的任何文件之前。-
处理选项后，将打印命令行中列出的每个文件的十六进制校验和。

[`-c`](#c) string

将文件的摘要与此字符串进行比较。 （请注意，如果指定了多个文件，则此选项还没有用。）

[`-s`](#s) string

打印给定 string 的校验和。

[`-p`](#p)

将标准输入回显到标准输出并将校验和附加到标准输出。

[`-q`](#q)

安静模式 — 只打印校验和。覆盖 `-r` 选项。

[`-r`](#r)

反转输出的格式。-
这有助于视觉差异。与 `-ptx` 选项结合使用时不执行任何操作。

[`-t`](#t)

运行内置计时赛。

[`-x`](#x)

运行内置测试脚本。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `md5`, `sha1`, `sha224`, `sha256`, `sha512`, `sha512t256`, `rmd160`, `skein256`, `skein512`, 和 `skein1024` 实用程序在成功时退出 0，如果至少一个输入文件无法读取，则退出 1，如果至少一个文件无法读取，则退出 2具有与 `-c` 选项相同的哈希值。

[实例](#__u5B9E___u4F8B_)
=======================

计算字符串 “Hello” 的 MD5 校验和。

$ md5 -s Hello MD5 ("Hello") = 8b1a9953c4611296a827abf8c47804d7 

与上面相同，但请注意输入字符串中没有换行符：

$ echo -n Hello | md5 8b1a9953c4611296a827abf8c47804d7 

计算多个文件的校验和反转输出：

$ md5 -r /boot/loader.conf /etc/rc.conf ada5f60f23af88ff95b8091d6d67bef6 /boot/loader.conf d80bf36c332dc0fdc479366ec3fa44cd /etc/rc.conf 

将 /boot/loader.conf 的摘要写入一个名为 digest 的文件中。然后再次计算校验和，并根据从 digest 文件中提取的校验和字符串对其进行验证：

$ md5 /boot/loader.conf > digest && md5 -c $(cut -f2 -d= digest) /boot/loader.conf MD5 (/boot/loader.conf) = ada5f60f23af88ff95b8091d6d67bef6 

与上面相同，但将摘要与无效字符串 (“randomstring”) 进行比较，这会导致失败。

$ md5 -c randomstring /boot/loader.conf MD5 (/boot/loader.conf) = ada5f60f23af88ff95b8091d6d67bef6 \[ Failed \] 

[参见](#__u53C2___u89C1_)
=======================

cksum(1), md5(3), ripemd(3), sha(3), sha256(3), sha384(3), sha512(3), skein(3) R. Rivest, The MD5 Message-Digest Algorithm, RFC1321. J. Burrows, The Secure Hash Standard, FIPS PUB 180-2. D. Eastlake and P. Jones, US Secure Hash Algorithm 1, RFC 3174.

RIPEMD-160 is part of the ISO draft standard “ISO/IEC DIS 10118-3” on dedicated hash functions.

Secure Hash Standard (SHS): http://csrc.nist.gov/cryptval/shs.html.

The RIPEMD-160 page: http://www.esat.kuleuven.ac.be/~bosselae/ripemd160.html.

[致谢](#__u81F4___u8C22_)
=======================

该程序被放置在公共领域，供 RSA Data Security 免费使用。

Oliver Eikemeier <[eik@FreeBSD.org](mailto:eik@FreeBSD.org)\> 添加了对 SHA-1 和 RIPEMD-160 的支持。

June 19, 2020

FreeBSD 13.1-RELEASE