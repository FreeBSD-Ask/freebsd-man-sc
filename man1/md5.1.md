# md5(1)

`md5` — 计算文件的消息摘要指纹（校验和）

## 名称

`md5`, `sha512`, `rmd160`, `md5sum`, `sha512sum`, `rmd160sum`, `shasum`

## 概要

`shasum [-pqrtx] [-c string] [-s string] [file]`

`md5sum [-bctwz] [--binary] [--check] [--help] [--ignore-missing] [--quiet] [--status] [--strict] [--tag] [--text] [--version] [--warn] [--zero] [file]`

（所有其他哈希工具具有相同的选项和用法。）

`shasum [-0bchqstUvw] [--01] [-a alg | --algorithm alg] [--binary] [--check] [--help] [--ignore-missing] [--quiet] [--status] [--strict] [--tag] [--text] [--UNIVERSAL] [--version] [--warn] [file]`

## 描述

`md5`、`rmd160` 和 `skein1024` 实用程序接受任意长度的消息作为输入，产生输入的 “指纹” 或 “消息摘要” 作为输出。

`md5sum`、`sha512t224sum` 和 `skein1024sum` 实用程序执行相同操作，但命令行选项和输出格式与类似命名的 GNU 实用程序匹配。

`shasum` 实用程序执行相同操作，但命令行选项和输出格式与随 Perl 发布的类似命名实用程序匹配。

在所有情况下，命令行上列出的每个文件单独处理。如果命令行上未列出文件，或文件名给出为 `-`，则从标准输入获取输入。

实用程序的不同模式有不同的输出格式，但在所有情况下，包含不可打印字符的文件名按 vis(3) 中所述使用 `VIS_CSTYLE | VIS_OCTAL` 样式编码。

推测在计算上不可行产生两个具有相同消息摘要的消息，或产生具有给定预定目标消息摘要的任何消息。SHA-224、SHA-256、SHA-384、SHA-512、RIPEMD-160 和 SKEIN 算法用于数字签名应用，其中大文件必须在使用公钥密码系统（如 RSA）下的私钥（密钥）加密之前以安全方式 “压缩”。

MD5 和 SHA-1 算法已被证明易受实际碰撞攻击，不应依赖其产生唯一输出，*也不应将其用作加密签名方案的一部分。*

SHA-512t256 是 SHA-512 截断为仅 256 位的版本。在 64 位硬件上，此算法比 SHA-256 快约 50%，但安全级别相同。哈希不可互换。

SHA-512t224 与 SHA-512t256 相同，但摘要截断为 224 位。

建议所有新应用使用 SHA-512 或 SKEIN-512 而非其他哈希函数之一。

### BSD 选项

以下选项在 BSD 模式下可用，即程序以不以 “sum” 结尾的名称调用时：

**`-c`** `string`, `--check=string` 将文件的摘要与此字符串比较。如果与 `-q` 或 `--quiet` 选项组合，除设置退出状态外，还打印计算的摘要。（注意，如果指定多个文件，此选项尚不可用。）

**`-p`**, `--passthrough` 将标准输入回显到标准输出，并将校验和附加到标准输出。在此模式下，命令行上指定的任何文件被静默忽略。

**`-q`**, `--quiet` 安静模式——仅打印校验和。覆盖 `-r` 或 `--reverse` 选项。

**`-r`**, `--reverse` 反转输出格式。这有助于视觉差异比较。与 `-ptx` 选项组合时无效果。

**`-s`** `string`, `--string=string` 打印给定 `string` 的校验和。在此模式下，命令行上指定的任何文件被静默忽略。

**`-t`**, `--time-trial` 运行内置计时测试。对于 `-sum` 版本，这是为兼容 coreutils 而设的空操作。

**`-x`**, `--self-test` 运行内置测试脚本。

### GNU 选项

以下选项在 GNU 模式下可用，即程序以以 “sum” 结尾的名称调用时：

**`-b`**, `--binary` 以二进制模式读取文件。

**`-c`**, `--check` 作为参数传递的文件必须包含由相同摘要算法以经典 BSD 格式或 GNU coreutils 格式生成的摘要行。对于摘要文件中每个格式良好的行，写入一行包含文件名后跟冒号 “:” 以及 OK 或 FAILED。如果适用，最后打印失败比较的次数和因格式不良而跳过的行数。可使用 `--quiet` 选项静默输出，除非摘要中有不匹配的条目。

**`--help`** 打印用法消息并退出。

**`--ignore-missing`** 验证校验和时，忽略给出了校验和但在磁盘上未找到的文件。

**`--quiet`** 验证校验和时，除非验证失败，否则不打印任何内容。

**`--status`** 验证校验和时，完全不打印任何内容。退出码将反映验证是否成功。

**`--strict`** 验证校验和时，如果输入格式错误则失败。

**`--tag`** 产生 BSD 风格输出。

**`-t`**, `--text` 以文本模式读取文件。这是默认值。注意，此实现不区分二进制和文本模式。

**`--version`** 打印版本信息并退出。

**`-w`**, `--warn` 验证校验和时，警告格式错误的输入。

**`-z`**, `--zero` 以 NUL 而非换行符终止输出行。

### PERL 选项

以下选项在 Perl 模式下可用，即程序以名称 “shasum” 调用时：

**`-0`**, `--01` 以位模式读取文件：ASCII ‘0’ 和 ‘1’ 字符分别对应 0 和 1 位，所有其他字符被忽略。参见 “缺陷”。

**`-a`** `alg`, `--algorithm` `alg` 使用指定算法：“1” 表示 SHA-1（默认），“xxx” 表示 `xxx` 位 SHA-2（例如 “256” 表示 SHA-256），或 “xxxyyy” 表示截断为 `yyy` 位的 `xxx` 位 SHA-2（例如 “512224” 表示 SHA-512/224）。

**`-b`**, `--binary` 以二进制模式读取文件。

**`-c`**, `--check` 作为参数传递的文件必须包含由相同摘要算法以经典 BSD 格式或 GNU coreutils 格式生成的摘要行。对于摘要文件中每个格式良好的行，写入一行包含文件名后跟冒号 “:” 以及 OK 或 FAILED。如果适用，最后打印失败比较的次数和因格式不良而跳过的行数。可使用 `--quiet` 选项静默输出，除非摘要中有不匹配的条目。

**`--help`** 打印用法消息并退出。

**`--ignore-missing`** 验证校验和时，忽略给出了校验和但在磁盘上未找到的文件。

**`--quiet`** 验证校验和时，除非验证失败，否则不打印任何内容。

**`--status`** 验证校验和时，完全不打印任何内容。退出码将反映验证是否成功。

**`--strict`** 验证校验和时，如果输入格式错误则失败。

**`--tag`** 产生 BSD 风格输出。

**`-t`**, `--text` 以文本模式读取文件。这是默认值。注意，此实现不区分二进制和文本模式。

**`-U`**, `--UNIVERSAL` 以通用模式读取文件：任何 CR-LF 对，以及任何后不跟 LF 的 CR，在计算摘要前转换为 LF。

**`--version`** 打印版本信息并退出。

**`-w`**, `--warn` 验证校验和时，警告格式错误的输入。

## 退出状态

`md5`、`sha512t224`、`rmd160` 和 `skein1024` 实用程序成功时退出 0，如果至少一个输入文件无法读取则退出 1，如果至少一个文件的哈希与 `-c` 选项不同则退出 2。

`md5sum`、`sha512t224sum`、`rmd160` 和 `shasum` 实用程序成功时退出 0，如果至少一个输入文件无法读取或验证校验和时不具有预期校验和则退出 1。

## 实例

计算字符串 “Hello” 的 MD5 校验和。

```sh
$ md5 -s Hello
MD5 ("Hello") = 8b1a9953c4611296a827abf8c47804d7
```

同上，但注意输入字符串中缺少换行符：

```sh
$ echo -n Hello | md5
8b1a9953c4611296a827abf8c47804d7
```

计算多个文件的校验和并反转输出：

```sh
$ md5 -r /boot/loader.conf /etc/rc.conf
ada5f60f23af88ff95b8091d6d67bef6 /boot/loader.conf
d80bf36c332dc0fdc479366ec3fa44cd /etc/rc.conf
```

这与 GNU 模式的输出几乎但不完全相同：

```sh
$ md5sum /boot/loader.conf /etc/rc.conf
ada5f60f23af88ff95b8091d6d67bef6  /boot/loader.conf
d80bf36c332dc0fdc479366ec3fa44cd  /etc/rc.conf
```

注意哈希和文件名之间有两个空格。如果请求二进制模式，它们改为由空格和星号分隔：

```sh
$ md5sum -b /boot/loader.conf /etc/rc.conf
ada5f60f23af88ff95b8091d6d67bef6 */boot/loader.conf
d80bf36c332dc0fdc479366ec3fa44cd */etc/rc.conf
```

将 **/boot/loader.conf** 的摘要写入名为 `digest` 的文件。然后再次计算校验和，并与从 `digest` 文件提取的校验和字符串验证：

```sh
$ md5 /boot/loader.conf > digest && md5 -c $(cut -f2 -d= digest) /boot/loader.conf
MD5 (/boot/loader.conf) = ada5f60f23af88ff95b8091d6d67bef6
```

同上，但将摘要与无效字符串（“randomstring”）比较，结果为失败。

```sh
$ md5 -c randomstring /boot/loader.conf
MD5 (/boot/loader.conf) = ada5f60f23af88ff95b8091d6d67bef6 [ Failed ]
```

在 GNU 模式下，`-c` 选项不与作为参数传递的哈希字符串比较。相反，它期望一个摘要文件，如上例中为 **/boot/loader.conf** 创建的名为 `digest` 的文件。

```sh
$ md5sum -c digest
/boot/loader.conf: OK
```

摘要文件可包含任意数量的行，格式为 BSD 或 GNU 模式生成的格式。如果哈希值与文件不匹配，打印 “FAILED” 而非 “OK”。

## 参见

[cksum(1)](cksum.1.md), md5(3), ripemd(3), sha(3), sha256(3), sha384(3), sha512(3), skein(3), vis(3)

> R. Rivest, "The MD5 Message-Digest Algorithm", RFC1321.

> J. Burrows, "The Secure Hash Standard", FIPS PUB 180-2.

> D. Eastlake and P. Jones, "US Secure Hash Algorithm 1", RFC 3174.

RIPEMD-160 是关于专用哈希函数的 ISO 草案标准 "ISO/IEC DIS 10118-3" 的一部分。

Secure Hash Standard (SHS): <https://www.nist.gov/publications/secure-hash-standard-shs>

The RIPEMD-160 page: <https://homes.esat.kuleuven.be/~bosselae/ripemd160.html>

## 注意事项

用于包含不可打印字符的文件名的编码与 GNU coreutils 使用的不兼容。GNU coreutils 使用的编码不可逆，因为某些不可打印字符被编码而其他被简单省略。另一方面，此实用程序使用的编码完全可逆。

如果需要与 GNU coreutils 互操作，建议确保所有文件名仅包含可打印字符。

## 缺陷

在位模式下，原始 `shasum` 脚本能够处理任意长度的输入。此实现不能，如果输入长度不是 8 位的倍数将发出错误。

## 致谢

此实用程序最初源自 RSA Data Security 放入公共域供免费通用使用的程序。

Oliver Eikemeier <eik@FreeBSD.org> 添加了对 SHA-1 和 RIPEMD-160 的支持。

Colin Percival <cperciva@FreeBSD.org> 和 Allan Jude <allanjude@FreeBSD.org> 添加了对 SHA-2 的支持。

Allan Jude <allanjude@FreeBSD.org> 添加了对 SKEIN 的支持。

Warner Losh <imp@FreeBSD.org> 添加了与 GNU coreutils 的兼容性，并由 Dag-Erling Smørgrav <des@FreeBSD.org> 大幅扩展，后者还添加了 Perl 兼容性。
