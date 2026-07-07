# ssh-keygen(1)

`ssh-keygen` — OpenSSH 认证密钥工具

## 名称

`ssh-keygen`

## 概要

`ssh-keygen [-q] [-a rounds] [-b bits] [-C comment] [-f output_keyfile] [-m format] [-N new_passphrase] [-O option] [-t ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa] [-w provider] [-Z cipher]`

`ssh-keygen -p [-a rounds] [-f keyfile] [-m format] [-N new_passphrase] [-P old_passphrase] [-Z cipher]`

`ssh-keygen -i [-f input_keyfile] [-m key_format]`

`ssh-keygen -e [-f input_keyfile] [-m key_format]`

`ssh-keygen -y [-f input_keyfile]`

`ssh-keygen -c [-a rounds] [-C comment] [-f keyfile] [-P passphrase]`

`ssh-keygen -l [-v] [-E fingerprint_hash] [-f input_keyfile]`

`ssh-keygen -B [-f input_keyfile]`

`ssh-keygen -D pkcs11`

`ssh-keygen -F hostname [-lv] [-f known_hosts_file]`

`ssh-keygen -H [-f known_hosts_file]`

`ssh-keygen -K [-a rounds] [-w provider]`

`ssh-keygen -R hostname [-f known_hosts_file]`

`ssh-keygen -r hostname [-g] [-f input_keyfile]`

`ssh-keygen -M generate [-O option] output_file`

`ssh-keygen -M screen [-f input_file] [-O option] output_file`

`ssh-keygen -I certificate_identity -s ca_key [-hU] [-D pkcs11_provider] [-n principals] [-O option] [-V validity_interval] [-z serial_number] file ...`

`ssh-keygen -L [-f input_keyfile]`

`ssh-keygen -A [-a rounds] [-f prefix_path]`

`ssh-keygen -k -f krl_file [-u] [-s ca_public] [-z version_number] file ...`

`ssh-keygen -Q [-l] -f krl_file file ...`

`ssh-keygen -Y find-principals [-O option] -s signature_file -f allowed_signers_file`

`ssh-keygen -Y match-principals -I signer_identity -f allowed_signers_file`

`ssh-keygen -Y check-novalidate [-O option] -n namespace -s signature_file`

`ssh-keygen -Y sign [-O option] -f key_file -n namespace file ...`

`ssh-keygen -Y verify [-O option] -f allowed_signers_file -I signer_identity -n namespace -s signature_file [-r revocation_file]`

## 描述

`ssh-keygen` 为 [ssh(1)](ssh.1.md) 生成、管理和转换认证密钥。`ssh-keygen` 可创建用于 SSH 协议版本 2 的密钥。

待生成密钥的类型由 `-t` 选项指定。如果不带任何参数调用，`ssh-keygen` 将生成一个 Ed25519 密钥。

`ssh-keygen` 还用于生成 Diffie-Hellman 组交换（DH-GEX）中使用的组。详情参见“模数生成”小节。

最后，`ssh-keygen` 可用于生成和更新密钥撤销列表（Key Revocation Lists），以及测试给定密钥是否已被撤销。详情参见“密钥撤销列表”小节。

通常，每个希望使用 SSH 公钥认证的用户运行此程序一次，在 `~/.ssh/id_ecdsa`、`~/.ssh/id_ecdsa_sk`、`~/.ssh/id_ed25519`、`~/.ssh/id_ed25519_sk` 或 `~/.ssh/id_rsa` 中创建认证密钥。此外，系统管理员可使用此程序生成主机密钥，如 **/etc/rc** 中所示。

通常此程序生成密钥并询问存储私钥的文件。公钥存储在同名但附加 “.pub” 的文件中。程序还会询问口令。口令可以为空以指示无口令（主机密钥必须有空口令），也可以是任意长度的字符串。口令类似于密码，但它可以是由一系列单词、标点符号、数字、空格或任何所需字符组成的短语。好的口令长度为 10-30 个字符，不是简单的句子或容易猜测的（英文散文每字符仅 1-2 位熵，提供的口令非常糟糕），并包含大小写字母、数字和非字母数字字符的混合。口令可稍后使用 `-p` 选项更改。

无法恢复丢失的口令。如果口令丢失或遗忘，必须生成新密钥并将相应的公钥复制到其他机器。

`ssh-keygen` 默认以 OpenSSH 专用格式写入密钥。此格式更受推荐，因为它为静态密钥提供更好的保护，并允许在私钥文件本身中存储密钥注释。密钥注释可能有助于识别密钥。注释在创建密钥时初始化为 “user@host”，但可使用 `-c` 选项更改。

`ssh-keygen` 仍可使用 `-m` 标志写入以前使用的 PEM 格式私钥。这可在生成新密钥时使用，现有的新格式密钥也可使用此选项结合 `-p`（更改口令）标志进行转换。

生成密钥后，`ssh-keygen` 会询问密钥应放置在何处以激活。

选项如下：

**`-A`** 如果所有默认密钥类型（rsa、ecdsa 和 ed25519）的主机密钥尚不存在，则生成它们。主机密钥使用默认密钥文件路径、空口令、密钥类型的默认位数和默认注释生成。如果还指定了 `-f`，其参数用作生成的主机密钥文件默认路径的前缀。**/etc/rc** 使用此选项生成新主机密钥。

**`-a`** `rounds` 保存私钥时，此选项指定使用的 KDF（密钥派生函数，当前为 bcrypt_pbkdf(3)）轮数。数值越高，口令验证越慢，对暴力密码破解的抵抗力越强（如果密钥被盗）。默认为 16 轮。

**`-B`** 显示指定私钥或公钥文件的 bubblebabble 摘要。

**`-b`** `bits` 指定要创建的密钥位数。对于 RSA 密钥，最小为 1024 位，默认为 3072 位。通常认为 3072 位已足够。对于 ECDSA 密钥，`-b` 标志通过从三种椭圆曲线大小（256、384 或 521 位）中选择来确定密钥长度。对 ECDSA 密钥尝试使用这三种值以外的位长度会失败。ECDSA-SK、Ed25519 和 Ed25519-SK 密钥具有固定长度，`-b` 标志将被忽略。

**`-C`** `comment` 提供新注释。

**`-c`** 请求更改私钥和公钥文件中的注释。程序将提示包含私钥的文件、密钥的口令（如果有）以及新注释。

**`-D`** `pkcs11` 下载 PKCS#11 共享库 `pkcs11` 提供的公钥。与 `-s` 组合使用时，此选项指示 CA 密钥位于 PKCS#11 令牌中（详情参见“证书”小节）。

**`-E`** `fingerprint_hash` 指定显示密钥指纹时使用的哈希算法。有效选项为：“md5” 和 “sha256”。默认为 “sha256”。

**`-e`** 此选项读取私钥或公钥 OpenSSH 密钥文件，并以 `-m` 选项指定的格式之一向 stdout 打印公钥。默认导出格式为 “RFC4716”。此选项允许导出 OpenSSH 密钥供其他程序使用，包括几种商业 SSH 实现。

**`-F`** `hostname | [hostname]:port` 在 `known_hosts` 文件中搜索指定的 `hostname`（带可选端口号），列出找到的所有匹配项。此选项可用于查找哈希主机名或地址，也可与 `-H` 选项组合以哈希格式打印找到的密钥。

**`-f`** `filename` 指定密钥文件名。

**`-g`** 使用 `-r` 命令打印指纹资源记录时使用通用 DNS 格式。

**`-H`** 对 `known_hosts` 文件进行哈希处理。这会将指定文件中的所有主机名和地址替换为哈希表示；原始内容移动到带 .old 后缀的文件中。`ssh` 和 `sshd` 可正常使用这些哈希，但如果文件内容泄露，它们不会透露识别信息。此选项不会修改现有的哈希主机名，因此可安全地用于混合哈希和非哈希名称的文件。

**`-h`** 签名密钥时，创建主机证书而非用户证书。详情参见“证书”小节。

**`-I`** `certificate_identity` 签名公钥时指定密钥身份。详情参见“证书”小节。

**`-i`** 此选项读取以 `-m` 选项指定格式的未加密私钥（或公钥）文件，并向 stdout 打印 OpenSSH 兼容的私钥（或公钥）。此选项允许从其他软件导入密钥，包括几种商业 SSH 实现。默认导入格式为 “RFC4716”。

**`-K`** 从 FIDO 认证器下载驻留密钥。每个下载的密钥的公钥和私钥文件将写入当前目录。如果连接了多个 FIDO 认证器，将从第一个被触摸的认证器下载密钥。更多信息参见“FIDO 认证器”小节。

**`-k`** 生成 KRL 文件。在此模式下，`ssh-keygen` 将在通过 `-f` 标志指定的位置生成 KRL 文件，撤销命令行上显示的每个密钥或证书。要撤销的密钥/证书可通过公钥文件或“密钥撤销列表”小节中描述的格式指定。

**`-L`** 打印一个或多个证书的内容。

**`-l`** 显示指定公钥文件的指纹。`ssh-keygen` 将尝试查找匹配的公钥文件并打印其指纹。如果与 `-v` 组合使用，指纹会附带可视 ASCII 艺术表示。

**`-M`** `generate` 生成候选 Diffie-Hellman 组交换（DH-GEX）参数，供 “diffie-hellman-group-exchange-*” 密钥交换方法最终使用。此操作生成的数字必须在使用前进一步筛选。更多信息参见“模数生成”小节。

**`-M`** `screen` 筛选 Diffie-Hellman 组交换的候选参数。这会接受候选数字列表并测试它们是否为具有可接受组生成器的安全（Sophie Germain）素数。此操作的结果可添加到 **/etc/moduli** 文件。更多信息参见“模数生成”小节。

**`-m`** `key_format` 指定密钥生成的密钥格式，以及 `-i`（导入）、`-e`（导出）转换选项和 `-p` 更改口令操作。后者可用于在 OpenSSH 私钥和 PEM 私钥格式之间转换。支持的密钥格式为：“RFC4716”（RFC 4716/SSH2 公钥或私钥）、“PKCS8”（PKCS8 公钥或私钥）或 “PEM”（PEM 公钥）。默认情况下，OpenSSH 将新生成的私钥以其自身格式写入，但转换公钥以导出时，默认格式为 “RFC4716”。在生成或更新支持的私钥类型时设置为 “PEM” 格式将导致密钥以传统 PEM 私钥格式存储。

**`-N`** `new_passphrase` 提供新口令。

**`-n`** `principals` 指定签名密钥时包含在证书中的一个或多个主体（用户或主机名）。可指定多个主体，以逗号分隔。详情参见“证书”小节。

**`-O`** `option` 指定键/值选项。这些选项特定于 `ssh-keygen` 被请求执行的操作。签名证书时，可在此指定“证书”小节中列出的选项之一。执行模数生成或筛选时，可指定“模数生成”小节中列出的选项之一。生成 FIDO 认证器支持的密钥时，可指定“FIDO 认证器”小节中列出的选项。使用 `-Y` 标志执行签名相关选项时，接受以下选项：

**`hashalg`**=`algorithm` 选择用于哈希待签名消息的哈希算法。有效算法为 “sha256” 和 “sha512”。默认为 “sha512”。

**`print-pubkey`** 在签名验证后将完整公钥打印到标准输出。

**`verify-time`**=`timestamp` 指定验证签名时使用的时间，而非当前时间。时间可以 YYYYMMDD[Z] 或 YYYYMMDDHHMM[SS][Z] 格式的日期或时间指定。日期和时间将在当前系统时区中解释，除非以 Z 字符为后缀，此时它们在 UTC 时区中解释。

使用 `-r` 标志从公钥生成 SSHFP DNS 记录时，接受以下选项：

**`hashalg`**=`algorithm` 选择使用 `-D` 标志打印 SSHFP 记录时使用的哈希算法。有效算法为 “sha1” 和 “sha256”。默认两者都打印。

`-O` 选项可多次指定。

**`-P`** `passphrase` 提供（旧）口令。

**`-p`** 请求更改私钥文件的口令而非创建新私钥。程序将提示包含私钥的文件、旧口令，并两次询问新口令。

**`-Q`** 测试密钥是否已在 KRL 中被撤销。如果还指定了 `-l` 选项，则打印 KRL 的内容。

**`-q`** 静默 `ssh-keygen`。

**`-R`** `hostname | [hostname]:port` 从 `known_hosts` 文件中删除属于指定 `hostname`（带可选端口号）的所有密钥。此选项可用于删除哈希主机（参见上文的 `-H` 选项）。

**`-r`** `hostname` 为指定公钥文件打印名为 `hostname` 的 SSHFP 指纹资源记录。

**`-s`** `ca_key` 使用指定 CA 密钥认证（签名）公钥。详情参见“证书”小节。生成 KRL 时，`-s` 指定 CA 公钥文件路径，用于按密钥 ID 或序列号直接撤销证书。详情参见“密钥撤销列表”小节。

**`-t`** `ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa` 指定要创建的密钥类型。可能值为 “ecdsa”、“ecdsa-sk”、“ed25519（默认）”、“ed25519-sk” 或 “rsa”。此标志也可用于指定使用 RSA CA 密钥签名证书时的所需签名类型。可用的 RSA 签名变体为 “ssh-rsa”（SHA1 签名，不推荐）、“rsa-sha2-256” 和 “rsa-sha2-512”（RSA 密钥的默认值）。

**`-U`** 与 `-s` 或 `-Y` `sign` 组合使用时，此选项指示 CA 密钥位于 ssh-agent(1) 中。更多信息参见“证书”小节。

**`-u`** 更新 KRL。与 `-k` 一起指定时，通过命令行列出的密钥将添加到现有 KRL 中，而非创建新 KRL。

**`-V`** `validity_interval` 签名证书时指定有效间隔。有效间隔可由单个时间组成，表示证书从现在开始有效到该时间过期；也可由用冒号分隔的两个时间组成，以指示显式时间间隔。开始时间可指定为：

- 字符串 “always”，表示证书没有指定的开始时间。
- 系统时区中格式为 YYYYMMDD 或 YYYYMMDDHHMM[SS] 的日期或时间。
- UTC 时区中格式为 YYYYMMDDZ 或 YYYYMMDDHHMM[SS]Z 的日期或时间。
- 当前系统时间之前的相对时间，由减号后跟 sshd_config(5) 的 TIME FORMATS 小节中描述的格式间隔组成。
- 自纪元（1970 年 1 月 1 日 00:00:00 UTC）以来的原始秒数，以 “0x” 开头的十六进制数。

结束时间可类似于开始时间指定：

- 字符串 “forever”，表示证书没有指定的结束时间。
- 系统时区中格式为 YYYYMMDD 或 YYYYMMDDHHMM[SS] 的日期或时间。
- UTC 时区中格式为 YYYYMMDDZ 或 YYYYMMDDHHMM[SS]Z 的日期或时间。
- 当前系统时间之后的相对时间，由加号后跟 sshd_config(5) 的 TIME FORMATS 小节中描述的格式间隔组成。
- 自纪元（1970 年 1 月 1 日 00:00:00 UTC）以来的原始秒数，以 “0x” 开头的十六进制数。

例如：

**`+52w1d`** 从现在起有效至 52 周零一天后。

**`-4w:+4w`** 从四周前有效至四周后。

**`20100101123000:20110101123000`** 从 2010 年 1 月 1 日下午 12:30 有效至 2011 年 1 月 1 日下午 12:30。

**`20100101123000Z:20110101123000Z`** 类似，但在 UTC 时区而非系统时区中解释。

**`-1d:20110101`** 从昨天有效至 2011 年 1 月 1 日午夜。

**`0x1:0x2000000000`** 从大约 1970 年初有效至 2033 年 5 月。

**`-1m:forever`** 从一分钟前有效且永不过期。

**`-v`** 详细模式。使 `ssh-keygen` 打印有关其进度的调试消息。这有助于调试模数生成。多个 `-v` 选项增加详细程度。最大为 3。

**`-w`** `provider` 指定创建 FIDO 认证器托管密钥时使用的库路径，覆盖使用内部 USB HID 支持的默认值。

**`-Y`** `find-principals` 查找与签名公钥关联的主体，签名通过 `-s` 标志提供，授权签名者文件通过 `-f` 标志提供。授权签名者文件的格式记录在下文的“授权签名者”小节中。如果找到一个或多个匹配的主体，它们将在标准输出上返回。

**`-Y`** `match-principals` 查找与通过 `-I` 标志提供的主体名称匹配的主体，在通过 `-f` 标志指定的授权签名者文件中。如果找到一个或多个匹配的主体，它们将在标准输出上返回。

**`-Y`** `check-novalidate` 检查使用 `ssh-keygen` `-Y` `sign` 生成的签名是否具有有效结构。这不验证签名是否来自授权签名者。测试签名时，`ssh-keygen` 接受标准输入上的消息和使用 `-n` 的签名命名空间。还必须使用 `-s` 标志提供包含相应签名的文件。签名测试成功由 `ssh-keygen` 返回零退出状态指示。

**`-Y`** `sign` 使用 SSH 密钥对文件或某些数据进行加密签名。签名时，`ssh-keygen` 接受命令行上零个或多个待签名文件——如果未指定文件，`ssh-keygen` 将对标准输入上呈现的数据进行签名。签名写入输入文件路径并附加 “.sig”，如果待签名消息是从标准输入读取的，则写入标准输出。用于签名的密钥通过 `-f` 选项指定，可引用私钥或通过 ssh-agent(1) 提供私钥部分的公钥。必须通过 `-n` 标志提供额外的签名命名空间，用于防止跨不同使用域的签名混淆（例如文件签名与邮件签名）。命名空间是任意字符串，可包括：用于文件签名的 “file”，用于邮件签名的 “email”。对于自定义用途，建议使用遵循 NAMESPACE@YOUR.DOMAIN 模式的名称以生成明确的命名空间。

**`-Y`** `verify` 请求验证如上所述使用 `ssh-keygen` `-Y` `sign` 生成的签名。验证签名时，`ssh-keygen` 接受标准输入上的消息和使用 `-n` 的签名命名空间。还必须使用 `-s` 标志提供包含相应签名的文件，以及使用 `-I` 的签名者身份和通过 `-f` 标志的授权签名者列表。授权签名者文件的格式记录在下文的“授权签名者”小节中。可通过 `-r` 标志传递包含已撤销密钥的文件。撤销文件可以是 KRL 或每行一个公钥的列表。授权签名者成功验证由 `ssh-keygen` 返回零退出状态指示。

**`-y`** 此选项读取私钥 OpenSSH 格式文件并向 stdout 打印 OpenSSH 公钥。

**`-Z`** `cipher` 指定写入 OpenSSH 格式私钥文件时用于加密的密码。可用密码列表可使用 "ssh -Q cipher" 获取。默认为 “aes256-ctr”。

**`-z`** `serial_number` 指定嵌入证书中的序列号，以区分此证书与同一 CA 的其他证书。如果 `serial_number` 以 “+” 字符为前缀，则序列号将在单个命令行上签名的每个证书递增。默认序列号为零。生成 KRL 时，`-z` 标志用于指定 KRL 版本号。

## 模数生成

`ssh-keygen` 可用于生成 Diffie-Hellman 组交换（DH-GEX）协议的组。生成这些组是一个两步过程：首先，使用快速但内存密集的过程生成候选素数。然后筛选这些候选素数的适用性（一个 CPU 密集型过程）。

使用 `-M` `generate` 选项执行素数生成。可通过 `-O` `bits` 选项指定所需素数长度。例如：

```sh
# ssh-keygen -M generate -O bits=2048 moduli-2048.candidates
```

默认情况下，从所需长度范围内的随机点开始搜索素数。可使用 `-O` `start` 选项覆盖，该选项指定不同的起始点（十六进制）。

生成候选集后，必须筛选其适用性。可使用 `-M` `screen` 选项执行。在此模式下，`ssh-keygen` 从标准输入（或使用 `-f` 选项指定的文件）读取候选。例如：

```sh
# ssh-keygen -M screen -f moduli-2048.candidates moduli-2048
```

默认情况下，每个候选将接受 100 次素性测试。可使用 `-O` `prime-tests` 选项覆盖。DH 生成器值将针对考虑中的素数自动选择。如果需要特定生成器，可使用 `-O` `generator` 选项请求。有效生成器值为 2、3 和 5。

筛选后的 DH 组可安装到 **/etc/moduli**。此文件包含一系列位长度的模数非常重要。

通过 `-O` 标志可为模数生成和筛选提供多个选项：

**`lines`**=`number` 在执行 DH 候选筛选时筛选指定行数后退出。

**`start-line`**=`line-number` 在执行 DH 候选筛选时从指定行号开始筛选。

**`checkpoint`**=`filename` 在执行 DH 候选筛选时将最后处理的行写入指定文件。如果作业重新启动，这将用于跳过输入文件中已处理的行。

**`start`**=`hex-value` 为 DH-GEX 生成候选模数时指定起始点（十六进制）。

**`generator`**=`value` 为 DH-GEX 测试候选模数时指定所需生成器（十进制）。

## 证书

`ssh-keygen` 支持对密钥进行签名以生成证书，证书可用于用户或主机认证。证书由公钥、一些身份信息、零个或多个主体（用户或主机）名称和一组由认证机构（CA）密钥签名的选项组成。客户端或服务器随后可仅信任 CA 密钥并验证其在证书上的签名，而非信任许多用户/主机密钥。注意，OpenSSH 证书是与 ssl(8) 中使用的 X.509 证书不同且简单得多的格式。

`ssh-keygen` 支持两种类型的证书：用户证书和主机证书。用户证书向服务器认证用户，而主机证书向用户认证服务器主机。要生成用户证书：

```sh
$ ssh-keygen -s /path/to/ca_key -I id -n user \
    /path/to/user_key.pub
```

生成的证书将放在 `/path/to/user_key-cert.pub`。`-I` 的参数是将在日志中使用的密钥标识符，也可用于撤销密钥。`-n` 的参数是证书表示的一个或多个（逗号分隔）主体，通常是用户名。主机证书需要 `-h` 选项：

```sh
$ ssh-keygen -s /path/to/ca_key -I id -h -n foo.example.org \
    /path/to/host_key.pub
```

对于主机证书，使用 `-n` 参数指定的主体是主机名，可包含通配符。

主机证书将输出到 `/path/to/host_key-cert.pub`。

可通过使用 `-D` 提供令牌库并使用 `-s` 参数提供公钥部分作为 CA 密钥标识，使用存储在 PKCS#11 令牌中的 CA 密钥进行签名：

```sh
$ ssh-keygen -s ca_key.pub -D libpkcs11.so -I id -n user \
    user_key.pub
```

类似地，CA 密钥可托管在 ssh-agent(1) 中。这由 `-U` 标志指示，同样，CA 密钥必须通过其公钥部分标识。

```sh
$ ssh-keygen -Us ca_key.pub -I id -n user user_key.pub
```

在所有情况下，`key_id` 是当证书用于认证时由服务器记录的“密钥标识符”。

证书限于对一组主体（用户/主机）名称有效。要为指定主体集生成证书：

```sh
$ ssh-keygen -s ca_key -I id -n user1,user2 user_key.pub
```

```sh
$ ssh-keygen -s ca_key -I id -h -n host.domain host_key.pub
```

可通过证书选项指定对用户证书有效性和使用的额外限制。证书选项可禁用 SSH 会话的某些功能，可仅在从特定源地址呈现时有效，或可强制使用特定命令。

对用户证书有效的选项有：

**`clear`** 清除所有启用的权限。这可用于清除默认权限集，以便单独添加权限。

**`critical`**:`name`[=`contents`]

**`extension`**:`name`[=`contents`] 包含任意证书关键选项或扩展。指定的 `name` 应包含域名后缀，例如 “name@example.com”。如果指定 `contents`，则将其作为字符串编码的扩展/选项内容包含；否则以无内容创建扩展/选项（通常指示标志）。不识别扩展的客户端或服务器可忽略扩展，而未知关键选项将导致证书被拒绝。

**`force-command`**=`command` 强制在使用证书进行认证时执行 `command`，而非用户指定的任何 shell 或命令。

**`no-agent-forwarding`** 禁用 ssh-agent(1) 转发（默认允许）。

**`no-port-forwarding`** 禁用端口转发（默认允许）。

**`no-pty`** 禁用 PTY 分配（默认允许）。

**`no-user-rc`** 禁用 sshd(8) 执行 `~/.ssh/rc`（默认允许）。

**`no-x11-forwarding`** 禁用 X11 转发（默认允许）。

**`permit-agent-forwarding`** 允许 ssh-agent(1) 转发。

**`permit-port-forwarding`** 允许端口转发。

**`permit-pty`** 允许 PTY 分配。

**`permit-user-rc`** 允许 sshd(8) 执行 `~/.ssh/rc`。

**`permit-X11-forwarding`** 允许 X11 转发。

**`no-touch-required`** 不要求使用此密钥进行的签名包含用户存在的证明（例如，通过让用户触摸认证器）。此选项仅对 FIDO 认证器算法 `ecdsa-sk` 和 `ed25519-sk` 有意义。

**`source-address`**=`address_list` 限制证书有效的源地址。`address_list` 是一个或多个 CIDR 格式的地址/网络掩码对的逗号分隔列表。

**`verify-required`** 要求使用此密钥进行的签名指示用户已首先验证，例如通过 PIN 或令牌上的生物识别。此选项仅对 FIDO 认证器算法 `ecdsa-sk` 和 `ed25519-sk` 有意义。

目前，没有标准选项对主机密钥有效。

最后，证书可定义有效生命周期。`-V` 选项允许指定证书的开始和结束时间。在此范围外呈现的证书不会被视为有效。默认情况下，证书从 UNIX 纪元到遥远未来有效。

要使证书用于用户或主机认证，CA 公钥必须被 sshd(8) 或 [ssh(1)](ssh.1.md) 信任。详情参见那些手册页。

## FIDO 认证器

`ssh-keygen` 能够生成 FIDO 认证器支持的密钥，之后只要在使用密钥时连接了硬件认证器，它们就可以像 OpenSSH 支持的任何其他密钥类型一样使用。FIDO 认证器通常要求用户通过触摸或点击明确授权操作。FIDO 密钥由两部分组成：存储在磁盘上私钥文件中的密钥句柄部分，以及每个 FIDO 认证器独有的、无法从认证器硬件导出的每设备私钥。这些在认证时由硬件组合以派生用于签名认证挑战的实际密钥。支持的密钥类型为 `ecdsa-sk` 和 `ed25519-sk`。

对 FIDO 密钥有效的选项有：

**`application`** 覆盖默认的 “ssh:” FIDO 应用/源字符串。这在生成主机或域特定的驻留密钥时可能有用。指定的应用字符串必须以 “ssh:” 开头。

**`challenge`**=`path` 指定在密钥生成期间传递给 FIDO 认证器的挑战字符串路径。挑战字符串可用作密钥注册带外协议的一部分（默认使用随机挑战）。

**`device`** 显式指定要使用的 fido(4) 设备，而非让认证器中间件选择一个。

**`no-touch-required`** 指示生成的私钥在生成签名时不需要触摸事件（用户存在）。注意 sshd(8) 默认拒绝此类签名，除非通过 authorized_keys 选项覆盖。

**`resident`** 指示密钥句柄应存储在 FIDO 认证器本身上。这使在多台计算机上使用认证器更容易。驻留密钥可能在 FIDO2 认证器上受支持，通常要求在生成前在认证器上设置 PIN。可使用 ssh-add(1) 从认证器加载驻留密钥。将密钥的两部分都存储在 FIDO 认证器上会增加攻击者能够使用被盗认证器设备的可能性。

**`user`** 与驻留密钥关联的用户名，覆盖空的默认用户名。为同一应用名称生成多个驻留密钥时，指定用户名可能有用。

**`verify-required`** 指示此私钥应要求每次签名进行用户验证。并非所有 FIDO 认证器都支持此选项。目前 PIN 认证是唯一支持的验证方法，但未来可能支持其他方法。

**`write-attestation`**=`path` 可在密钥生成时用于记录 FIDO 认证器在密钥生成期间返回的证明数据。此信息可能敏感。默认情况下，此信息被丢弃。

## 密钥撤销列表

`ssh-keygen` 能够管理 OpenSSH 格式的密钥撤销列表（KRL）。这些二进制文件使用紧凑格式指定要撤销的密钥或证书，如果按序列号撤销，每个证书仅占用一位。

KRL 可使用 `-k` 标志生成。此选项从命令行读取一个或多个文件并生成新 KRL。文件可包含 KRL 规范（见下文）或公钥，每行一个。普通公钥通过在 KRL 中列出其哈希或内容来撤销，证书通过序列号或密钥 ID 撤销（如果序列号为零或不可用）。

使用 KRL 规范撤销密钥提供对用于撤销密钥的记录类型的显式控制，并可用于直接按序列号或密钥 ID 撤销证书，而无需手头有完整的原始证书。KRL 规范由包含以下指令之一后跟冒号和一些指令特定信息的行组成。

**`serial`** : `serial_number`[-`serial_number`] 撤销具有指定序列号的证书。序列号是 64 位值，不包括零，可以十进制、十六进制或八进制表示。如果指定了两个用连字符分隔的序列号，则撤销每个序列号之间及包括每个序列号的范围内的序列号。CA 密钥必须已使用 `-s` 选项在 `ssh-keygen` 命令行上指定。

**`id`** : `key_id` 撤销具有指定密钥 ID 字符串的证书。CA 密钥必须已使用 `-s` 选项在 `ssh-keygen` 命令行上指定。

**`key`** : `public_key` 撤销指定密钥。如果列出证书，则作为普通公钥撤销。

**`sha1`** : `public_key` 通过在 KRL 中包含其 SHA1 哈希来撤销指定密钥。

**`sha256`** : `public_key` 通过在 KRL 中包含其 SHA256 哈希来撤销指定密钥。按 SHA256 哈希撤销密钥的 KRL 不受 7.9 之前的 OpenSSH 版本支持。

**`hash`** : `fingerprint` 使用指纹哈希撤销密钥，指纹哈希可从 sshd(8) 认证日志消息或 `ssh-keygen` `-l` 标志获取。此处仅支持 SHA256 指纹，生成的 KRL 不受 7.9 之前的 OpenSSH 版本支持。

KRL 可在 `-k` 之外使用 `-u` 标志更新。指定此选项时，通过命令行列出的密钥将合并到 KRL 中，添加到已存在的密钥中。

给定 KRL，还可以测试它是否撤销了特定密钥。`-Q` 标志将查询现有 KRL，测试命令行上指定的每个密钥。如果命令行上列出的任何密钥已被撤销（或遇到错误），`ssh-keygen` 将以非零退出状态退出。仅当未撤销任何密钥时才返回零退出状态。

## 授权签名者

验证签名时，`ssh-keygen` 使用简单的身份和密钥列表来确定签名是否来自授权源。此“授权签名者”文件使用模仿 sshd(8) 中描述的 AUTHORIZED_KEYS FILE FORMAT 的格式。文件的每一行包含以下以空格分隔的字段：主体、选项、密钥类型、base64 编码的密钥。空行和以 `#` 开头的行作为注释被忽略。

主体字段是一个模式列表（参见 ssh_config(5) 中的 PATTERNS），由一个或多个逗号分隔的 USER@DOMAIN 身份模式组成，这些模式被接受用于签名。验证时，通过 `-I` 选项呈现的身份必须与主体模式匹配，相应密钥才会被视为可接受验证。

选项（如果存在）由逗号分隔的选项规范组成。不允许空格，双引号内除外。支持以下选项规范（注意选项关键字不区分大小写）：

**`cert-authority`** 指示此密钥被接受为认证机构（CA），由此 CA 签名的证书可被接受用于验证。

**`namespaces`**=namespace-list 指定此密钥接受的命名空间模式列表。如果存在此选项，则签名对象中嵌入的签名命名空间和验证命令行上呈现的签名命名空间必须与指定列表匹配，密钥才会被视为可接受。

**`valid-after`**=`timestamp` 指示密钥在指定时间戳或之后有效，时间戳可以是 YYYYMMDD[Z] 或 YYYYMMDDHHMM[SS][Z] 格式的日期或时间。日期和时间将在当前系统时区中解释，除非以 Z 字符为后缀，此时它们在 UTC 时区中解释。

**`valid-before`**=`timestamp` 指示密钥在指定时间戳或之前有效。

验证由证书进行的签名时，预期的主体名称必须同时匹配授权签名者文件中的主体模式和证书本身中嵌入的主体。

授权签名者文件示例：

```sh
# Comments allowed at start of line
user1@example.com,user2@example.com ssh-rsa AAAAX1...
# A certificate authority, trusted for all principals in a domain.
*@example.com cert-authority ssh-ed25519 AAAB4...
# A key that is accepted only for file signing.
user2@example.com namespaces="file" ssh-ed25519 AAA41...
```

## 环境变量

**`SSH_SK_PROVIDER`** 指定加载任何 FIDO 认证器托管密钥时使用的库路径，覆盖使用内置 USB HID 支持的默认值。

## 文件

**`~/.ssh/id_ecdsa`**

**`~/.ssh/id_ecdsa_sk`**

**`~/.ssh/id_ed25519`**

**`~/.ssh/id_ed25519_sk`**

**`~/.ssh/id_rsa`** 包含用户的 ECDSA、认证器托管的 ECDSA、Ed25519、认证器托管的 Ed25519 或 RSA 认证身份。此文件不应被除用户以外的任何人读取。生成密钥时可指定口令；该口令将用于使用 128 位 AES 加密此文件的私钥部分。`ssh-keygen` 不会自动访问此文件，但它作为私钥的默认文件提供。[ssh(1)](ssh.1.md) 将在尝试登录时读取此文件。

**`~/.ssh/id_ecdsa.pub`**

**`~/.ssh/id_ecdsa_sk.pub`**

**`~/.ssh/id_ed25519.pub`**

**`~/.ssh/id_ed25519_sk.pub`**

**`~/.ssh/id_rsa.pub`** 包含用于认证的 ECDSA、认证器托管的 ECDSA、Ed25519、认证器托管的 Ed25519 或 RSA 公钥。此文件的内容应添加到用户希望使用公钥认证登录的所有机器上的 `~/.ssh/authorized_keys` 中。无需将此文件的内容保密。

**`/etc/moduli`** 包含用于 DH-GEX 的 Diffie-Hellman 组。文件格式在 [moduli(5)](../man5/moduli.5.md) 中描述。

## 参见

[ssh(1)](ssh.1.md), ssh-add(1), ssh-agent(1), [moduli(5)](../man5/moduli.5.md), sshd(8)

> "The Secure Shell (SSH) Public Key File Format", 2006.

## 作者

OpenSSH 是 Tatu Ylonen 发布的原始免费 ssh 1.2.12 版本的衍生作品。Aaron Campbell、Bob Beck、Markus Friedl、Niels Provos、Theo de Raadt 和 Dug Song 修复了许多错误，重新添加了较新的功能并创建了 OpenSSH。Markus Friedl 贡献了对 SSH 协议版本 1.5 和 2.0 的支持。
