  SSH-KEYGEN(1)  

SSH-KEYGEN(1)

FreeBSD General Commands Manual

SSH-KEYGEN(1)

[名称](#__u540D___u79F0_)
=======================

`ssh-keygen` —

认证密钥生成、管理和转换

[概要](#__u6982___u8981_)
=======================

`ssh-keygen` \[`-q`\] \[`-b` bits\] \[`-t` `dsa` | `ecdsa` | `ed25519` | `rsa`\] \[`-N` new\_passphrase\] \[`-C` comment\] \[`-f` output\_keyfile\] `ssh-keygen` `-p` \[`-P` old\_passphrase\] \[`-N` new\_passphrase\] \[`-f` keyfile\] `ssh-keygen` `-i` \[`-m` key\_format\] \[`-f` input\_keyfile\] `ssh-keygen` `-e` \[`-m` key\_format\] \[`-f` input\_keyfile\] `ssh-keygen` `-y` \[`-f` input\_keyfile\] `ssh-keygen` `-c` \[`-P` passphrase\] \[`-C` comment\] \[`-f` keyfile\] `ssh-keygen` `-l` \[`-v`\] \[`-E` fingerprint\_hash\] \[`-f` input\_keyfile\] `ssh-keygen` `-B` \[`-f` input\_keyfile\] `ssh-keygen` `-D` pkcs11 `ssh-keygen` `-F` hostname \[`-f` known\_hosts\_file\] \[`-l`\] `ssh-keygen` `-H` \[`-f` known\_hosts\_file\] `ssh-keygen` `-R` hostname \[`-f` known\_hosts\_file\] `ssh-keygen` `-r` hostname \[`-f` input\_keyfile\] \[`-g`\] `ssh-keygen` `-G` output\_file \[`-v`\] \[`-b` bits\] \[`-M` memory\] \[`-S` start\_point\] `ssh-keygen` `-T` output\_file `-f` input\_file \[`-v`\] \[`-a` rounds\] \[`-J` num\_lines\] \[`-j` start\_line\] \[`-K` checkpt\] \[`-W` generator\] `ssh-keygen` `-s` ca\_key `-I` certificate\_identity \[`-h`\] \[`-U`\] \[`-D` pkcs11\_provider\] \[`-n` principals\] \[`-O` option\] \[`-V` validity\_interval\] \[`-z` serial\_number\] file ... `ssh-keygen` `-L` \[`-f` input\_keyfile\] `ssh-keygen` `-A` \[`-f` prefix\_path\] `ssh-keygen` `-k` `-f` krl\_file \[`-u`\] \[`-s` ca\_public\] \[`-z` version\_number\] file ... `ssh-keygen` `-Q` `-f` krl\_file file ...

[描述](#__u63CF___u8FF0_)
=======================

`ssh-keygen` 为 ssh(1) 生成、管理和转换身份验证密钥。 `ssh-keygen` 可以创建供 SSH 协议版本 2 使用的密钥。

要生成的密钥类型使用 `-t` 选项指定。 如果在没有任何参数的情况下调用， `ssh-keygen` 将生成一个 RSA 密钥。

`ssh-keygen` 还用于生成用于 Diffie-Hellman 组交换 (DH-GEX) 的组。 有关详细信息，请参阅 [模数生成](#__u6A21___u6570___u751F___u6210_) 部分。

最后， `ssh-keygen` 可用于生成和更新密钥撤销列表，并测试给定的密钥是否已被撤销。 有关详细信息，请参阅 [密钥撤销列表](#__u5BC6___u94A5___u64A4___u9500___u5217___u8868_) 部分。

通常，每个希望将 SSH 与公钥身份验证一起使用的用户都会运行一次，以在 ~/.ssh/id\_dsa 、 ~/.ssh/id\_ecdsa 、 ~/.ssh/id\_ed25519 或 ~/.ssh/id\_rsa 中创建身份验证密钥。 此外，系统管理员可以使用它来生成主机密钥，如 /etc/rc 中所示。

通常，该程序会生成密钥并要求一个文件来存储私钥。 公钥存储在同名但附加了 “.pub” 的文件中。 该程序还要求输入密码。 密码可以为空表示没有密码（主机密钥必须有一个空的密码），也可以是任意长度的字符串。 密码短语类似于密码，不同之处在于它可以是包含一系列单词、标点符号、数字、空格或任何您想要的字符串的短语。 好的密码短语长度为 10-30 个字符，不是简单的句子或其他容易猜到的（英文散文每个字符只有 1-2 位熵，并且提供了非常糟糕的密码短语），并且包含大小写字母、数字、和非字母数字字符。 稍后可以使用 `-p` 选项更改密码。

没有办法恢复丢失的密码。 如果密码丢失或忘记，则必须生成新密钥并将相应的公钥复制到其他机器。

对于以较新的 OpenSSH 格式存储的密钥，在密钥文件中还有一个注释字段，只是为了方便用户帮助识别密钥。 注释可以说明密钥的用途或有用的信息。 创建密钥时，注释被初始化为 “user@host” ，但可以使用 `-c` 选项进行更改。

生成密钥后，下面的说明详细说明了应将密钥放置在何处以进行激活。

选项如下：

[`-A`](#A)

对于不存在主机密钥的每种密钥类型（rsa、dsa、ecdsa 和 ed25519），使用默认密钥文件路径、空密码、密钥类型的默认位和默认注释生成主机密钥。 如果还指定了 `-f` ，则其参数用作生成的主机密钥文件的默认路径的前缀。 /etc/rc 使用它来生成新的主机密钥。

[`-a`](#a) rounds

保存私钥时，此选项指定使用的 KDF（密钥派生函数）轮数。 较高的数字会导致密码验证速度变慢，并增加对暴力密码破解的抵抗力（如果密钥被盗）。

筛选 DH-GEX 候选人时（使用 `-T` 命令）。 此选项指定要执行的素数测试的数量。

[`-B`](#B)

显示指定私钥或公钥文件的气泡摘要。

[`-b`](#b) bits

指定要创建的密钥中的位数。 对于 RSA 密钥，最小大小为 1024 位，默认为 2048 位。 一般认为 2048 位就足够了。 DSA 密钥必须是 FIPS 186-2 指定的 1024 位。 对于 ECDSA 密钥， `-b` 标志通过从以下三种椭圆曲线大小之一中选择来确定密钥长度：256、384 或 521 位。 尝试对 ECDSA 密钥使用这三个值以外的位长度将失败。 Ed25519 密钥具有固定长度，并且 `-b` 标志将被忽略。

[`-C`](#C) comment

提供新评论。

[`-c`](#c)

请求更改私钥和公钥文件中的注释。 程序将提示输入包含私钥的文件，如果密钥有密码，则提示输入密码，以及新的注释。

[`-D`](#D) pkcs11

下载 PKCS#11 共享库 pkcs11 提供的 RSA 公钥。 当与 `-s` 结合使用时，此选项表示 CA 密钥驻留在 PKCS#11 令牌中（有关详细信息，请参阅 [证书](#__u8BC1___u4E66_) 部分）。

[`-E`](#E) fingerprint\_hash

指定显示密钥指纹时使用的哈希算法。 有效选项为： “md5” 和 “sha256 。” 默认值为 “sha256 。”

[`-e`](#e)

此选项将读取私有或公共 OpenSSH 密钥文件并以 `-m` 选项指定的格式之一将密钥打印到标准输出。 默认导出格式为 “RFC4716” 。 此选项允许导出 OpenSSH 密钥以供其他程序使用，包括几个商业 SSH 实现。

[`-F`](#F) hostname

在 known\_hosts 文件中搜索指定的 hostname ，列出找到的所有匹配项。 此选项对于查找散列主机名或地址很有用，也可以与 `-H` 选项结合使用，以散列格式打印找到的键。

[`-f`](#f) filename

指定密钥文件的文件名。

[`-G`](#G) output\_file

为 DH-GEX 生成候选素数。 这些素数必须在使用前进行安全筛选（使用 `-T` 选项）。

[`-g`](#g)

使用 `-r` 命令打印指纹资源记录时使用通用 DNS 格式。

[`-H`](#H)

散列 known\_hosts 文件。 这将使用指定文件中的散列表示替换所有主机名和地址；原始内容被移动到带有 .old 后缀的文件中。 `ssh` 和 `sshd`, 可以正常使用这些哈希值，但如果文件的内容被泄露，它们不会泄露识别信息。 此选项不会修改现有的散列主机名，因此可以安全地用于混合散列和非散列名称的文件。

[`-h`](#h)

签署密钥时，创建主机证书而不是用户证书。 有关详细信息，请参阅 [证书](#__u8BC1___u4E66_) 部分。

[`-I`](#I) certificate\_identity

签署公钥时指定密钥身份。 有关详细信息，请参阅 [证书](#__u8BC1___u4E66_) 部分。

[`-i`](#i)

此选项将以 `-m` 选项指定的格式读取未加密的私有（或公共）密钥文件，并将 OpenSSH 兼容的私有（或公共）密钥打印到标准输出。 此选项允许从其他软件导入密钥，包括几个商业 SSH 实现。 默认导入格式为 “RFC4716” 。

[`-J`](#J) num\_lines

在使用 `-T` 选项执行 DH 候选筛选时筛选指定数量的行后退出。

[`-j`](#j) start\_line

在使用 `-T` 选项执行 DH 候选筛选时，从指定的行号开始筛选。

[`-K`](#K) checkpt

在使用 `-T` 选项执行 DH 候选筛选时，将处理的最后一行写入文件 checkpt 。 如果作业重新启动，这将用于跳过输入文件中已处理的行。

[`-k`](#k)

生成 KRL 文件。 在这种模式下， `ssh-keygen` 将在通过 `-f` 标志指定的位置生成一个 KRL 文件，该文件会撤销命令行上提供的每个密钥或证书。 要撤销的密钥/证书可以通过公钥文件或使用 [KEY REVOCATION LISTS](#KEY_REVOCATION_LISTS) 部分中描述的格式来指定。

[`-L`](#L)

打印一个或多个证书的内容。

[`-l`](#l)

显示指定公钥文件的指纹。 对于 RSA 和 DSA 密钥， `ssh-keygen` 试找到匹配的公钥文件并打印其指纹。 如果与 `-v` 结合使用，则密钥的视觉 ASCII 艺术表示将与指纹一起提供。

[`-M`](#M) memory

指定为 DH-GEX 生成候选模数时要使用的内存量（以兆字节为单位）。

[`-m`](#m) key\_format

为 `-i` 导入）或 `-e` （导出）转换选项指定密钥格式。 支持的密钥格式为： “RFC4716” RFC 4716/SSH2 公钥或私钥）、 “PKCS8” PEM PKCS8 公钥）或 “PEM” （PEM 公钥）。 默认转换格式为 “RFC4716” 。 在生成或更新支持的私钥类型时设置 “PEM” 格式将导致密钥以旧 PEM 私钥格式存储。

[`-N`](#N) new\_passphrase

提供新密码。

[`-n`](#n) principals

指定签名密钥时要包含在证书中的一个或多个主体（用户名或主机名）。 可以指定多个主体，用逗号分隔。 有关详细信息，请参阅 [证书](#__u8BC1___u4E66_) 部分。

[`-O`](#O) option

签署密钥时指定证书选项。 可以多次指定此选项。 有关详细信息，另请参阅 [证书](#__u8BC1___u4E66_) 部分。

目前，没有标准选项对主机密钥有效。 对用户证书有效的选项是：

[`clear`](#clear)

清除所有启用的权限。这对于清除默认权限集很有用，因此可以单独添加权限。

[`critical`](#critical):name\[=contents\]

[`extension`](#extension):name\[=contents\]

包括任意证书关键选项或扩展。 指定的 name 应包含域后缀，例如 “name@example.com” 。 如果指定了 contents ，则将其作为编码为字符串的扩展/选项的内容包含在内，否则将创建没有内容的扩展/选项（通常指示标志）。 无法识别它们的客户端或服务器可能会忽略扩展，而未知的关键选项将导致证书被拒绝。

[`force-command`](#force-command)\=command

当证书用于身份验证时，强制执行 command 而不是用户指定的任何 shell 或命令。

[`no-agent-forwarding`](#no-agent-forwarding)

禁用 ssh-agent(1) 转发（默认允许）。

[`no-port-forwarding`](#no-port-forwarding)

禁用端口转发（默认允许）。

[`no-pty`](#no-pty)

禁用 PTY 分配（默认允许）。

[`no-user-rc`](#no-user-rc)

通过 sshd(8) 禁用 ~/.ssh/rc 的执行（默认允许）。

[`no-x11-forwarding`](#no-x11-forwarding)

禁用 X11 转发（默认允许）。

[`permit-agent-forwarding`](#permit-agent-forwarding)

允许 ssh-agent(1) 转发。

[`permit-port-forwarding`](#permit-port-forwarding)

允许端口转发。

[`permit-pty`](#permit-pty)

允许 PTY 分配。

[`permit-user-rc`](#permit-user-rc)

允许通过 sshd(8) 执行 ~/.ssh/rc 。

[`permit-X11-forwarding`](#permit-X11-forwarding)

允许 X11 转发。

[`source-address`](#source-address)\=address\_list

限制证书被视为有效的源地址。 address\_list 是 CIDR 格式的一个或多个地址/网络掩码对的逗号分隔列表。

[`-P`](#P) passphrase

提供（旧）密码。

[`-p`](#p)

请求更改私钥文件的密码，而不是创建新的私钥。 程序将提示输入包含私钥的文件，输入旧密码，两次输入新密码。

[`-Q`](#Q)

测试 KRL 中的密钥是否已被撤销。

[`-q`](#q)

沉默 `ssh-keygen` 。

[`-R`](#R) hostname

从 known\_hosts 文件中删除属于 hostname 的所有键。 此选项对于删除散列主机很有用（请参阅上面的 `-H` 选项）。

[`-r`](#r) hostname

打印指定公钥文件的名为 hostname 的 SSHFP 指纹资源记录。

[`-S`](#S) start

在为 DH-GEX 生成候选模数时指定起点（以十六进制表示）。

[`-s`](#s) ca\_key

使用指定的 CA 密钥验证（签名）公钥。 有关详细信息，请参阅 [证书](#__u8BC1___u4E66_) 部分。

生成 KRL 时， `-s` 指定用于通过密钥 ID 或序列号直接撤销证书的 CA 公钥文件的路径。 有关详细信息，请参阅 [KEY REVOCATION LISTS](#KEY_REVOCATION_LISTS) 部分。

[`-T`](#T) output\_file

测试 DH 组交换候选素数（使用 `-G` 选项生成）以确保安全。

[`-t`](#t) `dsa` | [`ecdsa`](#ecdsa) | [`ed25519`](#ed25519) | [`rsa`](#rsa)

指定要创建的密钥类型。可能的值为 “dsa 、” “ecdsa 、” “ed25519” 或 “rsa” 。

[`-U`](#U)

当与 `-s` 结合使用时，此选项表示 CA 密钥驻留在 ssh-agent(1) 中。 有关更多信息，请参阅 [证书](#__u8BC1___u4E66_) 部分。

[`-u`](#u)

更新 KRL。当使用 `-k` 指定时，通过命令行列出的键被添加到现有的 KRL，而不是创建新的 KRL。

[`-V`](#V) validity\_interval

签署证书时指定有效期。 有效性间隔可以由单个时间组成，表明证书从现在开始有效并在那时到期，或者可以由用冒号分隔的两个时间组成，以指示明确的时间间隔。

开始时间可以指定为字符串 “always” 以指示证书没有指定的开始时间、YYYYMMDD 格式的日期、YYYYMMDDHHMM\[SS\] 格式的时间、由减号组成的相对时间（相对于当前时间）符号后跟一个间隔，格式在 sshd\_config(5) 的 TIME FORMATS 部分中描述。

结束时间可以指定为 YYYYMMDD 日期、YYYYMMDDHHMM\[SS\] 时间、以加号字符或字符串 “forever” 开头的相对时间，以指示证书没有到期日期。

例如: “+52w1d” （从现在到 52 周和 1 天后有效）、 “-4w:+4w” （从 4 周前到 4 周后有效）、 “20100101123000:20110101123000” （从 12 :30 PM，2010 年 1 月 1 日至 12:30 PM，2011 年 1 月 1 日）， “-1d:20110101” （从昨天到 2011 年 1 月 1 日午夜有效）。 “-1m:forever” （从一分钟前开始有效，永不过期）。

[`-v`](#v)

详细模式。使 `ssh-keygen` 打印有关其进度的调试消息。 这有助于调试模数生成。多个 `-v` 选项会增加详细程度。 最大值为 3。

[`-W`](#W) generator

在测试 DH-GEX 的候选模量时指定所需的生成器。

[`-y`](#y)

此选项将读取私有 OpenSSH 格式文件并将 OpenSSH 公钥打印到标准输出。

[`-z`](#z) serial\_number

指定要嵌入证书中的序列号，以将此证书与来自同一 CA 的其他证书区分开来。 默认序列号为零。

生成 KRL 时， `-z` 标志用于指定 KRL 版本号。

[模数生成](#__u6A21___u6570___u751F___u6210_)
=========================================

`ssh-keygen` 可用于为 Diffie-Hellman Group Exchange (DH-GEX) 协议生成组。 生成这些组是一个两步过程：首先，使用快速但内存密集的过程生成候选素数。 然后测试这些候选素数的适用性（CPU 密集型过程）。

使用 `-G` 选项生成素数。所需的素数长度可以由 `-b` 选项指定。 例如：

`# ssh-keygen -G moduli-2048.candidates -b 2048`

默认情况下，对素数的搜索从所需长度范围内的随机点开始。这可以使用 `-S` 选项覆盖，该选项指定不同的起点（以十六进制表示）。

一旦生成了一组候选者，就必须对其适用性进行筛选。 这可以使用 `-T` 选项来执行。 在这种模式下， `ssh-keygen` 将从标准输入（或使用 `-f` 选项指定的文件）中读取候选者。 例如：

`# ssh-keygen -T moduli-2048 -f moduli-2048.candidates`

默认情况下，每个候选人都将接受 100 次素性测试。 这可以使用 `-a` 选项覆盖。 DH 生成器值将自动选择用于考虑中的素数。 如果需要特定的生成器，可以使用 `-W` 选项来请求。 有效的生成器值为 2、3 和 5。

屏蔽的 DH 组可以安装在 /etc/moduli 中。 重要的是该文件包含一系列位长度的模数，并且连接的两端共享公共模数。

[证书](#__u8BC1___u4E66_)
=======================

`ssh-keygen` 支持对密钥进行签名以生成可用于用户或主机身份验证的证书。 证书由公钥、一些身份信息、零个或多个主体（用户或主机）名称和一组由证书颁发机构 (CA) 密钥签名的选项组成。 然后，客户端或服务器可能只信任 CA 密钥并验证其在证书上的签名，而不是信任许多用户/主机密钥。 请注意，OpenSSH 证书与 ssl(8) 中使用的 X.509 证书格式不同，而且更简单。

`ssh-keygen` 支持两种类型的证书：用户和主机。 用户证书向服务器验证用户，而主机证书向用户验证服务器主机。 要生成用户证书：

`$ ssh-keygen -s /path/to/ca_key -I key_id /path/to/user_key.pub`

生成的证书将放置在 /path/to/user\_key-cert.pub 中。 主机证书需要 `-h` 选项：

`$ ssh-keygen -s /path/to/ca_key -I key_id -h /path/to/host_key.pub`

主机证书将输出到 /path/to/host\_key-cert.pub 。

可以使用存储在 PKCS#11 令牌中的 CA 密钥进行签名，方法是使用 `-D` 提供令牌库并通过将其公共部分作为参数提供给 `-s` 来识别 CA 密钥：

`$ ssh-keygen -s ca_key.pub -D libpkcs11.so -I key_id user_key.pub`

同样，CA 密钥也可以托管在 ssh-agent(1) 中。 这由 `-U` 标志指示，并且 CA 密钥必须由其公共部分标识。

`$ ssh-keygen -Us ca_key.pub -I key_id user_key.pub`

在所有情况下， key\_id 都是服务器在证书用于身份验证时记录的“密钥标识符”。

证书可能仅限于对一组主体（用户/主机）名称有效。 默认情况下，生成的证书对所有用户或主机都有效。要为一组指定的主体生成证书：

`$ ssh-keygen -s ca_key -I key_id -n user1,user2 user_key.pub`

`$ ssh-keygen -s ca_key -I key_id -h -n host.domain host_key.pub`

可以通过证书选项指定对用户证书的有效性和使用的附加限制。 证书选项可能会禁用 SSH 会话的功能，可能仅在从特定源地址提供时才有效，或者可能会强制使用特定命令。 有关有效证书选项的列表，请参阅上述 `-O` 选项的文档。

最后，证书可以定义有有效期。 `-V` 选项允许指定证书开始和结束时间。 在此范围之外的时间出示的证书将被视为无效。 默认情况下，证书从 UNIX 纪元到遥远的未来都有效。

对于用于用户或主机身份验证的证书，CA 公钥必须被 sshd(8) 或 ssh(1) 信任。 有关详细信息，请参阅这些手册页。

[密钥撤销列表](#__u5BC6___u94A5___u64A4___u9500___u5217___u8868_)
===========================================================

`ssh-keygen` 能够管理 OpenSSH 格式的密钥撤销列表 (KRL)。 这些二进制文件使用紧凑的格式指定要撤销的密钥或证书，如果它们被序列号撤销，则每个证书只需一位。

可以使用 `-k` 标志生成 KRL。 此选项从命令行读取一个或多个文件并生成新的 KRL。 这些文件可能包含 KRL 规范（见下文）或公钥，每行列出一个。 普通公钥通过在 KRL 中列出其散列或内容来撤销，证书通过序列号或密钥 ID 撤销（如果序列为零或不可用）。

使用 KRL 规范撤销密钥可明确控制用于撤销密钥的记录类型，并可用于通过序列号或密钥 ID 直接撤销证书，而无需手头有完整的原始证书。 KRL 规范由包含以下指令之一的行组成，后跟冒号和一些特定于指令的信息。

[`serial`](#serial): serial\_number\[-serial\_number\]

吊销具有指定序列号的证书。 序列号是 64 位值，不包括零，可以用十进制、十六进制或八进制表示。 如果指定两个序列号用连字符分隔，则包括每个序列号和每个序列号之间的序列号范围被撤销。 CA 密钥必须已在 `ssh-keygen` 命令行中使用 `-s` 选项指定。

[`id`](#id): key\_id

吊销具有指定密钥 ID 字符串的证书。 CA 密钥必须已在 `ssh-keygen` 命令行中使用 `-s` 选项指定。

[`key`](#key): public\_key

撤销指定的密钥。 如果列出了证书，则将其作为普通公钥撤销。

[`sha1`](#sha1): public\_key

通过在 KRL 中包含其 SHA1 哈希来撤销指定的密钥。

[`sha256`](#sha256): public\_key

通过在 KRL 中包含其 SHA256 哈希来撤销指定的密钥。 7.9 之前的 OpenSSH 版本不支持通过 SHA256 哈希撤销密钥的 KRL。

[`hash`](#hash): fingerprint

使用指纹哈希撤销密钥，从 sshd(8) 身份验证日志消息或 `ssh-keygen` `-l` 标志获得。 此处仅支持 SHA256 指纹，7.9 之前的 OpenSSH 版本不支持生成的 KRL。

除了 `-k` 之外，还可以使用 `-u` 标志更新 KRL。 指定此选项后，通过命令行列出的键将合并到 KRL 中，并添加到已经存在的键中。

给定一个 KRL，也可以测试它是否撤销了一个特定的密钥（或多个密钥）。 `-Q` 标志将查询现有的 KRL，测试命令行上指定的每个键。 如果命令行中列出的任何密钥已被撤销（或遇到错误），则 `ssh-keygen` 将以非零退出状态退出。 只有在没有撤销密钥的情况下才会返回零退出状态。

[文件](#__u6587___u4EF6_)
=======================

~/.ssh/id\_dsa

~/.ssh/id\_ecdsa

~/.ssh/id\_ed25519

~/.ssh/id\_rsa

包含用户的 DSA、ECDSA、Ed25519 或 RSA 认证身份。 除用户外，任何人都不应读取此文件。 生成密钥时可以指定密码；该密码将用于使用 128 位 AES 加密此文件的私有部分。 `ssh-keygen` 不会自动访问此文件，但它作为私钥的默认文件提供。 ssh(1) 将在尝试登录时读取此文件。

~/.ssh/id\_dsa.pub

~/.ssh/id\_ecdsa.pub

~/.ssh/id\_ed25519.pub

~/.ssh/id\_rsa.pub

包含用于身份验证的 DSA、ECDSA、Ed25519 或 RSA 公钥。 该文件的内容应添加到用户希望使用公钥身份验证登录的所有机器上的 ~/.ssh/authorized\_keys 中。 无需将此文件的内容保密。

/etc/moduli

包含用于 DH-GEX 的 Diffie-Hellman 组。文件格式在 moduli(5) 中描述。

[参见](#__u53C2___u89C1_)
=======================

ssh(1) 、 ssh-add(1) 、 ssh-agent(1) 、 moduli(5) 、 sshd(8) 安全 Shell (SSH) 公钥文件格式, RFC 4716, 2006.

[作者](#__u4F5C___u8005_)
=======================

OpenSSH 是 Tatu Ylonen 的原始免费 ssh 1.2.12 版本的衍生版本。 Aaron Campbell、Bob Beck、Markus Friedl、Niels Provos、Theo de Raadt 和 Dug Song 删除了许多错误，重新添加了新功能并创建了 OpenSSH。 Markus Friedl 贡献了对 SSH 协议版本 1.5 和 2.0 的支持。

September 12, 2018

FreeBSD 13.1-RELEASE