  FTP(1)  

FTP(1)

FreeBSD General Commands Manual

FTP(1)

[名称](#__u540D___u79F0_)
=======================

`ftp` —

Internet 文件传输程序

[概要](#__u6982___u8981_)
=======================

`ftp` \[`-46AadefginpRtVv`\] \[`-N` netrc\] \[`-o` output\] \[`-P` port\] \[`-q` quittime\] \[`-r` retry\] \[`-s` srcaddr\] \[`-T` dir,max \[,inc\]\] \[\[user`@`\]host \[port\]\] \[\[user`@`\]host`:`\[path\]\[`/`\]\] \[`file:///`path\] \[`ftp://`\[user\[`:`password\]`@`\]host\[`:`port\]`/`path\[`/`\]\[`;type=`X\]\] \[`http://`\[user\[`:`password\]`@`\]host\[`:`port\]`/`path\] \[...\] `ftp` `-u` URL file \[...\]

[描述](#__u63CF___u8FF0_)
=======================

`ftp` 是 Internet 标准文件传输协议的用户界面。 该程序允许用户将文件传输到远程网络站点或从远程网络站点传输文件。

最后五个参数将使用 FTP 或 HTTP 协议或通过直接复制来获取文件到当前目录。 这是脚本的理想选择。 有关详细信息，请参阅下面的 [AUTO-FETCHING 文件](#AUTO_FETCHING___u6587___u4EF6_) 。

选项可以在命令行中指定，也可以在命令解释器中指定。

[`-4`](#4)

强制 `ftp` 仅使用 IPv4 地址。

[`-6`](#6)

强制 `ftp` 仅使用 IPv6 地址。

[`-A`](#A)

强制激活模式 ftp。 默认情况下， `ftp`-
将尝试使用被动模式 ftp 并在服务器不支持被动时回退到主动模式。 此选项使 `ftp` 始终使用活动连接。 它仅对连接到未正确实施被动模式的非常旧的服务器有用。

[`-a`](#a)

使 `ftp` 绕过正常的登录过程，而使用匿名登录。

[`-d`](#d)

启用调试。

[`-e`](#e)

禁用命令行编辑。这对于 Emacs ange-ftp 模式很有用。

[`-f`](#f)

强制为通过 FTP 或 HTTP 代理的传输重新加载缓存。

[`-g`](#g)

禁用文件名通配。

[`-i`](#i)

在多个文件传输期间关闭交互式提示。

[`-N`](#N) netrc

使用 netrc 而不是 ~/.netrc 。 有关更多信息，请参阅 [.netrc](#.netrc) 文件。

[`-n`](#n)

限制 `ftp` 在初始连接时尝试 “auto-login” 以进行非自动获取传输。 如果启用了自动登录， `ftp` 将检查用户主目录中的 .netrc （见下文）文件中是否存在描述远程计算机上帐户的条目。 如果不存在条目， `ftp` 将提示输入远程机器的登录名（默认是本地机器上的用户身份），并且如果需要，提示输入密码和登录帐户。 要覆盖自动获取传输的自动登录，请根据需要指定用户名（以及可选的密码）。

[`-o`](#o) output

自动获取文件时，将内容保存在 output 中。 根据下面的文 [文件命名约定](#__u6587___u4EF6___u547D___u540D___u7EA6___u5B9A_) 解析 output 。 如果 output 不是 ‘-’ 或不以 ‘|’ 开头，那么只有指定的第一个文件将被检索到 output; 所有其他文件将被检索到其远程名称的基本名称中。

[`-P`](#P) port

将端口号设置为 port 。

[`-p`](#p)

启用被动模式操作以在连接过滤防火墙后面使用。 此选项已被弃用，因为 `ftp` 现在默认尝试使用被动模式，如果服务器不支持被动连接，则回退到主动模式。

[`-q`](#q) quittime

如果连接停止了 quittime 秒，则退出。

[`-R`](#R)

重新启动所有非代理自动提取。

[`-r`](#r) wait

如果连接失败，请重试连接尝试，暂停 wait 几秒钟。

[`-s`](#s) srcaddr

使用 srcaddr 作为所有连接的本地 IP 地址。

[`-t`](#t)

启用数据包跟踪。

[`-T`](#T) direction,maximum\[,increment\]

将 direction 的最大传输速率设置为 maximum 字节/秒，如果指定，则将增量设置为 increment 字节/秒。 有关更多信息，请参阅 `rate` 。

[`-u`](#u) URL file \[...\]

在命令行上将文件上传到 URL ，其中 URL 是 auto-fetch 支持的一种 ftp URL 类型（对于单个文件上传具有可选的目标文件名），并且 file 是要上传的一个或多个本地文件。

[`-V`](#V)

禁用 `verbose` 和 `progress` 当输出到终端时覆盖默认启用。

[`-v`](#v)

启用 `verbose` 和 `progress` 。 如果输出到终端，这是默认设置（在 `progress` 的情况下， `ftp` 是前台进程）。 强制 `ftp` 显示来自远程服务器的所有响应，并报告数据传输统计信息。

可以在命令行上指定 `ftp` 与之通信的客户端主机。 如果这样做了， `ftp` 将立即尝试与该主机上的 FTP 服务器建立连接；否则， `ftp` 将进入其命令解释器并等待用户的指令。 当 `ftp` 正在等待来自用户的命令时，会向用户提供提示 ‘`ftp>`’ 。 `ftp` 可以识别以下命令：

[`!`](#!) \[command \[args\]\]

在本地机器上调用交互式 shell。 如果有参数，则第一个被视为直接执行的命令，其余参数作为其参数。

[`$`](#$) macro-name \[args\]

执行使用 `macdef` 命令定义的 macro-name 。 参数被传递给未覆盖的宏。

[`account`](#account) \[passwd\]

成功完成登录后，提供远程系统访问资源所需的补充密码。 如果不包含参数，将在非回显输入模式下提示用户输入帐户密码。

[`append`](#append) local-file \[remote-file\]

将本地文件附加到远程计算机上的文件。 如果未指定 remote-file ，则本地文件名在被任何 `ntrans` 或 `nmap` 设置更改后用于命名远程文件。 文件传输使用 `type 、` `format 、` `mode` 和 `structure` 的当前设置。

[`ascii`](#ascii)

将文件传输 `type` 设置为网络 ASCII 。 这是默认类型。

[`bell`](#bell)

安排在每个文件传输命令完成后响铃。

[`binary`](#binary)

设置文件传输 `type` 以支持二进制图像传输。

[`bye`](#bye)

终止与远程服务器的 FTP 会话并退出 `ftp` 。 文件结束也将终止会话并退出。

[`case`](#case)

在 `get 、` `mget` 和 `mput` 命令期间切换远程计算机文件名大小写映射。 `case` 写开启时（默认关闭），远程计算机文件名全部大写，写入本地目录，字母映射为小写。

[`cd`](#cd) remote-directory

将远程机器上的工作目录更改为 remote-directory 。

[`cdup`](#cdup)

将远程机器工作目录更改为当前远程机器工作目录的父级。

[`chmod`](#chmod) mode remote-file

将远程系统上的文件 remote-file 的权限模式更改为 mode 。

[`close`](#close)

终止与远程服务器的 FTP 会话，并返回命令解释器。 任何定义的宏都会被删除。

[`cr`](#cr)

在 ascii 类型文件检索期间切换回车剥离。 在 ascii 类型文件传输期间，记录由回车/换行序列表示。 当 `cr` 打开时（默认），从这个序列中去除回车符以符合 UNIX 单换行记录分隔符。 非 UNIX 远程系统上的记录可能包含单个换行符；当进行 ascii 类型的传输时，只有当 `cr` 关闭时，这些换行符才能与记录分隔符区分开来。

[`delete`](#delete) remote-file

删除远程机器上的文件 remote-file 。

[`dir`](#dir) \[remote-path \[local-file\]\]

打印远程机器上目录内容的列表。 该列表包括服务器选择包含的任何系统相关信息；例如，大多数 UNIX 系统会从命令 ‘`ls -l`’ 产生输出。 如果未指定 remote-path ，则使用当前工作目录。 如果交互式提示打开， `ftp` 将提示用户验证最后一个参数是否确实是接收 `dir` 输出的目标本地文件。 如果未指定本地文件，或者 local-file 为 ‘`-`’ ，则将输出发送到终端。

[`disconnect`](#disconnect)

[`close`](#close_2) 的同义词。

[`edit`](#edit)

切换命令行编辑以及上下文相关的命令和文件完成。 如果输入来自终端，则会自动启用，否则禁用。

[`epsv epsv4 epsv6`](#epsv_epsv4_epsv6)

分别在所有 IP、IPv4 和 IPv6 连接上切换扩展 `EPSV` 和 `EPRT` 命令的使用。 首先尝试 `EPSV /` `EPRT`, 然后再尝试 `PASV /` `PORT` 。 这是默认启用的。如果扩展命令失败，则此选项将在当前连接期间暂时禁用，或者直到 `epsv 、` `epsv4` 或 `epsv6` 再次执行。

[`exit`](#exit)

[`bye`](#bye_2) 的同义词。

[`features`](#features)

显示远程服务器支持的功能（使用 `FEAT` 命令）。

[`fget`](#fget) localfile

检索 localfile 中列出的文件，每个文件名有一行。

[`form`](#form) format

将文件传输 `form` 设置为 format 。 默认（也是唯一受支持的）格式是 “non-print” 。

[`ftp`](#ftp) host \[port\]

[`open`](#open) 的同义词。

[`ftp_debug`](#ftp_debug) \[ftp\_debug-value\]

切换调试模式。 如果指定了可选的 ftp\_debug-value ，则它用于设置调试级别。 当调试打开时， `ftp` 打印发送到远程机器的每个命令，前面是字符串 ‘`-->`’ 。

[`gate`](#gate) \[host \[port\]\]

切换 gate-ftp 模式，该模式用于通过 TIS FWTK 和 Gauntlet ftp 代理进行连接。 如果尚未设置 gate-ftp 服务器（无论是由用户明确设置，还是来自 `FTPSERVER` 环境变量），则不允许这样做。 如果给定了 host ，则将启用 gate-ftp 模式，并将 gate-ftp 服务器设置为 host 。 如果还给出了 port ，则该端口将用作连接到 gate-ftp 服务器的端口。

[`get`](#get) remote-file \[local-file\]

检索 remote-file 并将其存储在本地计算机上。 如果未指定本地文件名，则使用与远程计算机上相同的名称，但会受到当前 `case 、` `ntrans` 和 `nmap` 设置的更改。 传输文件时使用 `type 、` `form 、` `mode` 和 `structure` 的当前设置。

[`glob`](#glob)

切换 `mdelete 、` `mget 、` `mput` 和 `mreget` 的文件名扩展。 如果使用 `glob` 关闭了 globbing，则文件名参数按字面意思获取，而不是扩展。 `mput` 的通配符在 csh(1) 中完成。 对于 `mdelete 、` `mget` 和 `mreget`, 每个远程文件名在远程计算机上单独展开，并且列表不会合并。 目录名的扩展可能和普通文件名的扩展不同：具体结果取决于国外操作系统和ftp服务器，可以通过 ‘`mls remote-files -`’ 来预览 注意： `mget 、` `mput` 和 `mreget` 并不意味着传输文件的整个目录子树。 这可以通过传输子树的 tar(1) 存档（以二进制模式）来完成。

[`hash`](#hash) \[size\]

为每个传输的数据块切换哈希符号 (‘#’) 打印。 数据块的大小默认为 1024 字节。 这可以通过以字节为单位指定 size 来更改。 启用 `hash` 会禁用 `progress` 。

[`help`](#help) \[command\]

打印有关 command 含义的信息性消息。如果没有给出参数， `ftp`-
会打印一个已知命令的列表。

[`idle`](#idle) \[seconds\]

将远程服务器上的不活动计时器设置为 seconds 秒。 如果省略 seconds ，则打印当前的不活动计时器。

[`image`](#image)

[`binary`](#binary_2) 的同义词。

[`lcd`](#lcd) \[directory\]

更改本地计算机上的工作目录。 如果未指定 directory ，则使用用户的主目录。

[`less`](#less) file

[`page`](#page) 的同义词。

[`lpage`](#lpage) local-file

使用 `set pager` 选项指定的程序显示 local-file 。

[`lpwd`](#lpwd)

打印本地机器上的工作目录。

[`ls`](#ls) \[remote-path \[local-file\]\]

[`dir`](#dir_2) 的同义词。

[`macdef`](#macdef) macro-name

定义一个宏。 后续行存储为 macro-name; 空行（文件中的连续换行符或终端回车）终止宏输入模式。 在所有定义的宏中有 16 个宏和 4096 个字符的限制。 宏名称最多可包含 8 个字符。 宏仅适用于它们在其中定义的当前会话（或者如果在会话之外定义，则适用于使用下一个打 `open` 命令调用的会话），并且在执行 `close` 命令之前一直保持定义。 要调用宏，请使用 `$` 命令（见上文）。

宏处理器将 ‘$’ 和 ‘\\’ 解释为特殊字符。 ‘$’ 后跟一个数字（或多个数字）被宏调用命令行上的相应参数替换。 ‘$’ 后跟 ‘i’ 向宏处理器发出信号，表明正在执行的宏将被循环。 在第一次传递中， “$i” 被宏调用命令行上的第一个参数替换，在第二次传递中，它被第二个参数替换，依此类推。 后跟任何字符的 ‘\\’ 将被该字符替换。 使用 ‘\\’ 防止对 ‘$’ 进行特殊处理。

[`mdelete`](#mdelete) \[remote-files\]

删除远程机器上的 remote-files 。

[`mdir`](#mdir) remote-files local-file

与 `dir` 类似，但可以指定多个远程文件。 如果交互式提示打开， `ftp` 将提示用户验证最后一个参数是否确实是接收 `mdir` 输出的目标本地文件。

[`mget`](#mget) remote-files

展开远程机器上的 remote-files ，并对由此产生的每个文件名执行一次 `get` 。 有关文件名扩展的详细信息，请参见 `glob` 。 然后将根据 `case 、` `ntrans` 和 `nmap` 设置处理生成的文件名。 文件转移到本地工作目录，可以用 ‘`lcd directory`’; 可以使用 ‘`! mkdir directory`’ 创建新的本地目录。

[`mkdir`](#mkdir) directory-name

在远程机器上创建一个目录。

[`mls`](#mls) remote-files local-file

和 `ls` 一样，除了可以指定多个远程文件，而且必须指定 local-file 。 如果交互式提示打开， `ftp` 将提示用户验证最后一个参数是否确实是接收 `mls` 输出的目标本地文件。

[`mlsd`](#mlsd) \[remote-path\]

使用 `MLSD` 以机器可解析的形式显示 remote-path 的内容（如果没有给出，则默认为当前目录）。 显示的格式可以用 ‘remopts mlst ...’ 来改变。

[`mlst`](#mlst) \[remote-path\]

使用 `MLST` 以机器可解析的形式显示 remote-path 的详细信息（如果未给出，则默认为当前目录）。 显示的格式可以用 ‘remopts mlst ...’ 来改变。

[`mode`](#mode) mode-name

将文件传输 `mode` 设置为 mode-name 。 默认（也是唯一受支持的）模式是 “stream” 。

[`modtime`](#modtime) remote-file

以 `RFC2822` 格式显示文件在远程机器上的最后修改时间。

[`more`](#more) file

[`page`](#page_2) 的同义词。

[`mput`](#mput) local-files

在作为参数给出的本地文件列表中展开通配符，并对结果列表中的每个文件执行 `put` 。 有关文件名扩展的详细信息，请参见 `glob` 。 然后将根据 `ntrans` 和 `nmap` 设置处理生成的文件名。

[`mreget`](#mreget) remote-files

根据 `mget`, 但执行 `reget` 而不是 `get` 。

[`msend`](#msend) local-files

[`mput`](#mput_2) 的同义词。

[`newer`](#newer) remote-file \[local-file\]

仅当远程文件的修改时间比当前系统上的文件更新时才获取该文件。 如果当前系统上不存在该文件，则认为远程文件 `newer` 。 否则，此命令与 get 相同。

[`nlist`](#nlist) \[remote-path \[local-file\]\]

[`ls`](#ls_2) 的同义词。

[`nmap`](#nmap) \[inpattern outpattern\]

设置或取消设置文件名映射机制。 如果未指定参数，则未设置文件名映射机制。 如果指定了参数，则在 `mput` 命令期间映射远程文件名，并在没有指定远程目标文件名的情况下发出 `put` 命令。 如果指定了参数，则在 `mget` 命令期间映射本地文件名，并在没有指定本地目标文件名的情况下发出 `get` 命令。 当连接到具有不同文件命名约定或实践的非 UNIX 远程计算机时，此命令很有用。 映射遵循由 inpattern 和 outpattern 设置的模式。 \[Inpattern\] 是传入文件名的模板（可能已经根据 `ntrans` 和 `case` 设置进行了处理）。 变量模板是通过在 inpattern 中包含序列 “$1 、” “$2 、” ... “$9” 来完成的。 使用 ‘\\’ 来防止对 ‘$’ 字符进行这种特殊处理。 所有其他字符都按字面意思处理，并用于确定 `nmap` \[inpattern\] 变量值。 例如， inpattern $1.$2 和远程文件名 "mydata.data", $1 将具有值 "mydata"，而 $2 将具有值 "data"。 outpattern 确定生成的映射文件名。 序列 “$1 、” “$2 、” ... “$9” 被替换为来自 inpattern 模板的任何值。 序列 “$0” 被原始文件名替换。 此外，如果 \[seq1\] 不是空字符串，则序列 “\[seq1, seq2\]” 被替换为 seq1 ；否则被 seq2 替换。 例如，命令

nmap $1.$2.$3 \[$1,$2\].\[$2,file\] 

将为输入文件名 "myfile.data" 和 "myfile.data.old" 生成输出文件名 "myfile.data" ，为输入文件名 "myfile" 生成输出文件名 "myfile.file" ，为输入文件名生成 ".myfile" 生成输出文件名 "myfile.myfile" 。 空格可能包含在 outpattern 中，如示例中所示：

`nmap $1 sed s/ *$// > $1`

使用 ‘\\’ 字符可防止对 ‘$ 、’ ‘\[ 、’ ‘\]’ 和 ‘,’ 字符进行特殊处理。

[`ntrans`](#ntrans) \[inchars \[outchars\]\]

设置或取消设置文件名字符翻译机制。 如果未指定参数，则未设置文件名字符转换机制。 如果指定了参数，则远程文件名中的字符在 `mput` 命令和未指定远程目标文件名的情况下发出的 `put` 命令期间进行转换。 如果指定了参数，本地文件名中的字符将在 `mget` 命令和 `get` 命令期间进行转换，而无需指定本地目标文件名。 当连接到具有不同文件命名约定或实践的非 UNIX 远程计算机时，此命令很有用。 与 inchars 中的字符匹配的文件名中的字符将替换为 outchars 中的相应字符。 如果字符在 inchars 中的位置长于 outchars 的长度，则从文件名中删除该字符。

[`open`](#open_2) host \[port\]

建立与指定 host FTP 服务器的连接。 可以提供可选的端口号，在这种情况下， `ftp` 将尝试联系该端口的 FTP 服务器。 如果 `set auto-login` 选项打开（默认）， `ftp` 还将尝试自动将用户登录到 FTP 服务器（见下文）。

[`page`](#page_3) file

使用 `set pager` 选项指定的程序检索 `file` 并显示。

[`passive`](#passive) \[`auto`\]

切换被动模式（如果没有给出参数）。 如果给出了 `auto` ，就好像 `FTPMODE` 设置为 ‘auto’ 一样。 如果被动模式打开（默认）， `ftp` 将为所有数据连接发送 `PASV` 命令而不是 `PORT` 命令。 `PASV` 命令请求远程服务器为数据连接打开一个端口并返回该端口的地址。 远程服务器侦听该端口，客户端连接到它。 当使用更传统的 `PORT` 命令时，客户端侦听端口并将该地址发送到远程服务器，远程服务器连接回它。 当通过网关路由器或控制流量方向的主机使用 `ftp` 时，被动模式很有用。 （请注意，尽管 `RFC1123` 要求 FTP 服务器支持 `PASV` 命令，但有些不支持。）

[`pdir`](#pdir) \[remote-path\]

执行 `dir` \[remote-path\], 并使用 `set pager` 选项指定的程序显示结果。

[`pls`](#pls) \[remote-path\]

执行 `ls` \[remote-path\], 并使用 `set pager` 选项指定的程序显示结果。

[`pmlsd`](#pmlsd) \[remote-path\]

执行 `mlsd` \[remote-path\], 并使用 `set pager` 选项指定的程序显示结果。

[`preserve`](#preserve)

切换对检索到的文件的修改时间的保留。

[`progress`](#progress)

切换传输进度条的显示。 对于 local-file 为 ‘`-`’ 或以 ‘|’ 开头的命令的传输，进度条将被禁用。 有关详细信息，请参阅 [文件命名约定](#__u6587___u4EF6___u547D___u540D___u7EA6___u5B9A_) 。启用 `progress` 会禁用 `hash` 。

[`prompt`](#prompt)

切换交互式提示。 在多个文件传输期间发生交互式提示，以允许用户有选择地检索或存储文件。 如果提示关闭（默认开启），任何 `mget` 或 `mput` 都会传输所有文件，任何 `mdelete` 都会删除所有文件。

提示打开时，提示符下可以使用以下命令：

[`a`](#a_2)

对当前文件回答 ‘yes’ ，并自动对当前命令的任何剩余文件回答 ‘yes’ 。

[`n`](#n_2)

回答 ‘no’ ，不要传输文件。

[`p`](#p_2)

对当前文件回答 ‘yes’ ，并关闭提示模式（因为已给出 “prompt off” ）。

[`q`](#q_2)

终止当前操作。

[`y`](#y)

回答 ‘yes’ ，然后传输文件。

[`?`](#?)

显示帮助消息。

任何其他响应都会对当前文件回答 ‘yes’ 。

[`proxy`](#proxy) ftp-command

代理 ftp 命令 在辅助控制连接上执行 ftp 命令。 此命令允许同时连接到两个远程 FTP 服务器，以便在两个服务器之间传输文件。 第一个 `proxy` 命令应该是 `open` 的，以建立辅助控制连接。 输入命令 "proxy ?" 查看辅助连接上可执行的其他 FTP 命令。 以下命令以 `proxy` 开头时的行为不同： `open` 不会在自动登录过程中定义新的宏， `close` 不会删除现有的宏定义， `get` 和 `mget` 将文件从主控制连接上的主机传输到辅助控制连接上的主机控制连接，以及从辅助控制连接上的主机到主控制连接上的主机的 `put 、` `mput` 和 `append` 传输文件。 第三方文件传输取决于辅助控制连接上的服务器对 FTP 协议 `PASV` 命令的支持。

[`put`](#put) local-file \[remote-file\]

在远程机器上存储本地文件。 如果未指定 remote-file ，则在根据任何 `ntrans` 或 `nmap` 设置处理后使用本地文件名来命名远程文件。 文件传输使用 `type 、` `format 、` `mode` 和 `structure` 的当前设置。

[`pwd`](#pwd)

打印远程机器上当前工作目录的名称。

[`quit`](#quit)

[`bye`](#bye_3) 的同义词。

[`quote`](#quote) arg1 arg2 ...

指定的参数被逐字发送到远程 FTP 服务器。

[`rate`](#rate) direction \[maximum \[increment\]\]

将最大传输速率限制为 maximum 字节/秒。 如果 maximum 值为 0，则禁用油门。

direction 可以是以下之一：

[`all`](#all)

两个方向。

[`get`](#get_2)

传入转账。

[`put`](#put_2)

传出转账。

每次接收到给定信号时， maximum 可以通过 increment 字节（默认值：1024）动态修改：

[`SIGUSR1`](#SIGUSR1)

按 increment 字节递增 maximum 。

[`SIGUSR2`](#SIGUSR2)

按 increment 节递减 maximum 。 结果必须是正数。

如果未提供 maximum ，则显示当前油门速率。

注意：尚未为 ascii 模式传输实现 `rate` 。

[`rcvbuf`](#rcvbuf) size

将套接字接收缓冲区的大小设置为 size 。

[`recv`](#recv) remote-file \[local-file\]

[`get`](#get_3) 的同义词。

[`reget`](#reget) remote-file \[local-file\]

[`reget`](#reget_2) 的行为类似于 `get`, 除了如果 local-file 存在并且小于 remote-file, 则假定 local-file 是 remote-file 的部分传输副本，并且从明显的故障点继续传输。 当通过容易断开连接的网络传输非常大的文件时，此命令很有用。

[`remopts`](#remopts) command \[command-options\]

将远程 FTP 服务器上的 command 选项设置为 command-options （其缺失将根据特定命令进行处理）。 已知支持选项的远程 FTP 命令包括： ‘MLST’ （用于 `MLSD` 和 `MLST` )。

[`rename`](#rename) \[from \[to\]\]

将 from 从远程机器上重命名为文件 to 。

[`reset`](#reset)

清除回复队列。 此命令将命令/回复序列与远程 FTP 服务器重新同步。 在远程服务器违反 FTP 协议后，可能需要重新同步。

[`restart`](#restart) marker

在指示的 marker 处重新启动紧随其后的 `get` 或 `put` 。 在 UNIX 系统上，标记通常是文件中的字节偏移量。

[`rhelp`](#rhelp) \[command-name\]

向远程 FTP 服务器请求帮助。 如果指定了 command-name ，它也会提供给服务器。

[`rmdir`](#rmdir) directory-name

删除远程机器上的目录。

[`rstatus`](#rstatus) \[remote-file\]

不带参数，显示远程机器的状态。 如果指定了 remote-file ，则显示远程机器上 remote-file 的状态。

[`runique`](#runique)

切换在本地系统上使用唯一文件名存储文件。 如果已存在名称等于 `get` 或 `mget` 命令的目标本地文件名的文件，则在名称后附加 ".1" 。 如果生成的名称与另一个现有文件匹配，则会将 ".2" 附加到原始名称。 如果此过程持续到 ".99", 则会打印一条错误消息，并且不会进行传输。 将报告生成的唯一文件名。 请注意， `runique` 不会影响从 shell 命令生成的本地文件（见下文）。 默认值为关闭。

[`send`](#send) local-file \[remote-file\]

[`put`](#put_3) 的同义词。

[`sendport`](#sendport)

切换 `PORT` 命令的使用。 默认情况下， `ftp` 将在为每次数据传输建立连接时尝试使用 `PORT` 命令。 使用 `PORT` 命令可以防止在执行多个文件传输时出现延迟。 如果 `PORT` 命令失败， `ftp` 将使用默认数据端口。 当禁止使用 `PORT` 命令时，不会尝试对每次数据传输使用 `PORT` 命令。 这对于某些忽略 FTP 命令但错误地表明它们已被接受的 `PORT` 实现很有用。

[`set`](#set) \[option value\]

将 option 设置为 value 。如果未给出 option 和 value ，则显示所有选项及其值。当前支持的选项有：

[`anonpass`](#anonpass)

默认为 `$FTPANONPASS`

[`ftp_proxy`](#ftp_proxy)

默认为 `$ftp_proxy`

[`http_proxy`](#http_proxy)

默认为 `$http_proxy`

[`no_proxy`](#no_proxy)

默认为 `$no_proxy`

[`pager`](#pager)

默认为 `$PAGER`

[`prompt`](#prompt_2)

默认为 `$FTPPROMPT`

[`rprompt`](#rprompt)

默认为 `$FTPRPROMPT`

[`site`](#site) arg1 arg2 ...

指定的参数作为 `SITE` 命令逐字发送到远程 FTP 服务器。

[`size`](#size) remote-file

返回远程机器上 remote-file 的大小。

[`sndbuf`](#sndbuf) size

将套接字发送缓冲区的大小设置为 size 。

[`status`](#status)

显示 `ftp` 的当前状态。

[`struct`](#struct) struct-name

将文件传输 structure 设置为 struct-name 。 默认（也是唯一受支持的）结构是 “file” 。

[`sunique`](#sunique)

切换以唯一文件名在远程计算机上存储文件。 远程 FTP 服务器必须支持 FTP 协议 `STOU` 命令才能成功完成。 远程服务器将报告唯一名称。默认值为关闭

[`system`](#system)

显示远程机器上运行的操作系统类型。

[`tenex`](#tenex)

将文件传输类型设置为与 TENEX 机器通信所需的类型。

[`throttle`](#throttle)

[`rate`](#rate_2) 的同义词。

[`trace`](#trace)

切换数据包跟踪。

[`type`](#type) \[type-name\]

将文件传输 `type` 设置为 type-name 。 如果未指定类型，则打印当前类型。 默认类型是网络 ASCII 。

[`umask`](#umask) \[newmask\]

将远程服务器上的默认 umask 设置为 newmask 。 如果省略 newmask ，则打印当前的 umask。

[`unset`](#unset) option

取消设置 option 。有关详细信息，请参阅 `set` 。

[`usage`](#usage) command

打印 command 的使用信息。

[`user`](#user) user-name \[password \[account\]\]

向远程 FTP 服务器表明自己的身份。 如果没有指定 password 并且服务器需要它， `ftp` 将提示用户输入它（在禁用本地回显之后）。 如果未指定 account 字段，而 FTP 服务器需要它，则会提示用户输入。 如果指定了 account 字段，则在远程服务器不需要登录时，将在登录序列完成后将帐户命令中继到远程服务器。 除非在禁用 “auto-login” 的情况下调用 `ftp` ，否则此过程会在初始连接到 FTP 服务器时自动完成。

[`verbose`](#verbose)

切换详细模式。 在详细模式下，来自 FTP 服务器的所有响应都会显示给用户。 此外，如果打开详细信息，当文件传输完成时，会报告有关传输效率的统计信息。 默认情况下，详细是打开的。

[`xferbuf`](#xferbuf) size

将套接字发送和接收缓冲区的大小设置为 size 。

[`?`](#?_2) \[command\]

[`help`](#help_2) 的同义词。

嵌入空格的命令参数可以用引号 ‘"’ 标记。

切换设置的命令可以采用明确的 `on` 或 `off` 参数来适当地强制设置。

将字节数作为参数的命令（例如， `hash 、` `rate` 和 `xferbuf`) 支持参数上的可选后缀，这会改变参数的解释。 支持的后缀是：

[`b`](#b)

导致没有修改。（选修的）

[`k`](#k)

Kilo; 将参数乘以 1024

[`m`](#m)

Mega; 将参数乘以 1048576

[`g`](#g_2)

Giga; 将参数乘以 1073741824

如果 `ftp` 在传输过程中收到 `SIGINFO` （参见 stty(1) 的 “status” 参数）或 `SIGQUIT` 信号，则当前传输速率统计信息将被写入标准错误输出，格式与标准完成相同信息。

[AUTO-FETCHING FILES](#AUTO_FETCHING_FILES)
===========================================

除了标准命令外，此版本的 `ftp` 还支持自动获取功能。 要启用自动获取，只需在命令行上传递主机名/文件列表。

以下格式是自动获取元素的有效语法：

\[user`@`\]host`:`\[path\]\[`/`\]

“Classic” FTP 格式。

如果 path 包含一个 glob 字符并且启用了 glob，（请参阅 `glob`), 则执行相当于 ‘`mget path`’ 的操作。

如果 path-
的目录组件不包含通配符，则在当前目录中以 `path` 的名称 basename（请参阅 basename(1)) 本地存储。 否则，使用完整的远程名称作为本地名称，相对于本地根目录。

[`ftp://`](#ftp://)\[user\[`:`password\]`@`\]host\[`:`port\]`/`path\[`/`\]\[`;type=`X\]

如果未定义设置 `set ftp_proxy` ，则使用 FTP 协议检索 FTP URL。 否则，通过 `set ftp_proxy` 中定义的代理使用 HTTP 传输 URL。如果未定义 `set ftp_proxy` 并且给出了 user ，则以 user 身份登录。 在这种情况下，如果提供了 password ，请使用密码，否则提示用户输入密码。

如果提供了 ‘;type=A’ 或 ‘;type=I’ 的后缀，则传输类型将分别以 ascii 或二进制进行。 默认传输类型是二进制。

为了符合 `RFC3986`, `ftp` 将 “ftp://” 自动获取 URL 的 path 部分解释如下：

*   host\[`:`port\] 之后的 ‘`/`’ 被解释为 path 之前的分隔符，而不是 path 本身的一部分。
*   该 path 被解释为以 ‘`/` 分隔的名称组件列表。 对于除最后一个这样的组件之外的所有组件， `ftp` 执行相当于 `cd` 命令。 对于最后一个路径组件， `ftp` 执行与 `get` 命令等效的操作。’
*   由 path 中的 ‘`//`’ 或 path 开头的额外 ‘`/`’ 产生的空名称组件将导致相当于没有目录名称的 `cd` 命令。这不太可能有用。
*   路径组件中的任何 ‘`%`XX’ 代码（根据 `RFC3986`) 都将被解码，其中 XX 表示十六进制的字符代码。 此解码发生在 path 被拆分为组件之后，但在每个组件用于相当于 `cd` 或 `get` 命令之前。 一些常用的代码是 ‘`%2F`’ (代表 ‘`/`’) 和 ‘`%7E`’ (代表 ‘`~`’ )。

上述解释具有以下后果：

*   该路径相对于指定用户或 ‘anonymous’ 用户的默认登录目录进行解释。 如果需要 / 目录，请使用 “%2F” 的前导路径。 如果需要用户的主目录（并且远程服务器支持该语法），请使用 “%7Euser/” 的前导路径。 例如，要以用户 ‘myname’ 和密码 ‘mypass’ 的身份从 ‘localhost’ 检索 /etc/motd ，请使用 “ftp://myname:mypass@localhost/%2fetc/motd”
*   精确的 `cd` 和 `get` 命令可以通过仔细选择在何处使用 ‘/’ 以及在何处使用 ‘%2F’ (或 ‘%2f’ ）来控制。 例如，以下 URL 对应于指示命令的等效项：
    
    ftp://host/dir1/dir2/file
    
    “cd dir1”, “cd dir2”, “get file”.
    
    ftp://host/%2Fdir1/dir2/file
    
    “cd /dir1”, “cd dir2”, “get file”.
    
    ftp://host/dir1%2Fdir2/file
    
    “cd dir1/dir2”, “get file”.
    
    ftp://host/%2Fdir1%2Fdir2/file
    
    “cd /dir1/dir2”, “get file”.
    
    ftp://host/dir1%2Fdir2%2Ffile
    
    “get dir1/dir2/file”.
    
    ftp://host/%2Fdir1%2Fdir2%2Ffile
    
    “get /dir1/dir2/file”.
    
*   您必须对与 `cd` 命令等效的每个中间目录具有适当的访问权限。

[`http://`](#http://)\[user\[`:`password\]`@`\]host\[`:`port\]`/`path

使用 HTTP 协议检索的 HTTP URL。 如果定义了 `set http_proxy` ，它将用作 HTTP 代理服务器的 URL。 如果需要 HTTP 授权来检索 path, 并且 ‘user’ (以及可选的 ‘password’) 在 URL 中，则使用它们进行首次身份验证。

[`file:///`](#file:///)path

本地 URL，从本地主机上的 /path 复制。

[`about:`](#about:)topic

显示有关 topic 的信息；没有为此自动获取的元素检索文件。 支持的值包括：

[`about:ftp`](#about:ftp)

有关 `ftp` 的信息。

[`about:version`](#about:version)

`ftp` 的版本。 在报告问题时提供。

除非上面另有说明，并且没有给出 `-o` output ，否则该文件将作为 path 的 basename(1) 存储在当前目录中。 请注意，如果收到 HTTP 重定向，则使用服务器提供的新目标 URL 和相应的新 path 重试获取。 建议使用显式 `-o` output ，以避免写入意外的文件名。

如果经典格式或 FTP URL 格式有尾随 ‘/’ 或空 path 组件，则 `ftp` 将连接到站点并 `cd` 到作为路径给出的目录，并让用户处于交互模式以准备进一步输入。 如果正在使用 `set ftp_proxy` ，这将不起作用。

直接 HTTP 传输使用 HTTP 1.1。代理 FTP 和 HTTP 传输使用 HTTP 1.0。

如果给出 `-R` ，所有不通过 FTP 或 HTTP 代理的自动获取将重新启动。 对于 FTP, 这是通过使用 `reget` 而不是 `get` 来实现的。 对于 HTTP, 这是通过使用 ‘Range: bytes=’ HTTP/1.1 指令来实现的。

如果需要 WWW 或代理 WWW 身份验证，系统将提示您输入用户名和密码以进行身份验证。

在 URL 中指定 IPv6 数字地址时，您需要将地址括在方括号中。 例如： “ftp://\[::1\]:21/” 。 这是因为冒号用于 IPv6 数字地址以及作为端口号的分隔符。

[正在中止文件传输](#__u6B63___u5728___u4E2D___u6B62___u6587___u4EF6___u4F20___u8F93_)
=============================================================================

要中止文件传输，请使用终端中断键（通常为 Ctrl-C）。 发送转账将立即停止。 通过向远程服务器发送 FTP 协议 `ABOR` 命令并丢弃接收到的任何进一步数据，将停止接收传输。 完成此操作的速度取决于远程服务器对 `ABOR` 处理的支持。 如果远程服务器不支持 `ABOR` 命令，则在远程服务器完成发送请求的文件之前不会出现提示。

如果在 `ftp` 等待远程服务器对 ABOR 处理的回复时使用终端中断键序列，则连接将被关闭。 这与传统行为（在此阶段忽略终端中断）不同，但被认为更有用。

[文件命名约定](#__u6587___u4EF6___u547D___u540D___u7EA6___u5B9A_)
===========================================================

根据以下规则处理指定为 `ftp` 命令的参数的文件。

1.  如果指定了文件名 ‘`-`’ ，则使用 stdin （用于读取）或 stdout （用于写入）。
2.  如果文件名的第一个字符是 ‘|’, 则参数的其余部分被解释为 shell 命令。 然后 `ftp` 使用带有参数的 popen(3) 分叉一个 shell，并从标准输出 (stdin) 读取（写入）。 如果 shell 命令包含空格，则参数必须加引号；例如 ““`| ls -lt`”” 。 这种机制的一个特别有用的例子是： “`dir "" |more`” 。
3.  如果上述检查失败，如果启用了 “globbing” ，则本地文件名将根据 csh(1) 中使用的规则进行扩展；请参阅 `glob` 命令。 如果 `ftp` 命令需要一个本地文件（例如 `put` ），则只使用 "globbing" 操作生成的第一个文件名。
4.  对于未指定本地文件名的 `mget` 命令和 `get` 命令，本地文件名是远程文件名，可以通过 `case 、` `ntrans` 或 `nmap` 设置进行更改。 如果 `runique` 打开，则生成的文件名可能会被更改。
5.  对于具有未指定远程文件名的 `mput` 命令和 `put` 命令，远程文件名是本地文件名，可以通过 `ntrans` 或 `nmap` 设置进行更改。 如果打开了 `sunique` ，远程服务器可能会更改生成的文件名。

[文件传输参数](#__u6587___u4EF6___u4F20___u8F93___u53C2___u6570_)
===========================================================

FTP 规范指定了许多可能影响文件传输的参数。 `type` 可以是 “ascii 、” “image” （二进制）、 “ebcdic” 和 “local byte size” 之一（主要用于 PDP-10's 和 PDP-20's )。 `ftp` 支持 ascii 和 image 类型的文件传输，以及用于 `tenex` 模式传输的本地字节大小 8。

`ftp` 仅支持其余文件传输参数的默认值： `mode 、` `form` 和 `struct` 。

[.netrc 文件](#.netrc___u6587___u4EF6_)
=====================================

.netrc 文件包含自动登录过程使用的登录和初始化信息。 它驻留在用户的主目录中，除非被 `-N` netrc 选项覆盖，或在 `NETRC` 环境变量中指定。 识别以下标记；它们可以用空格、制表符或换行符分隔：

[`machine`](#machine) name

识别远程机器 name 。 自动登录进程在 .netrc 文件中搜索与 `ftp` 命令行上指定的远程机器匹配的 `machine` 令牌或作为 `open` 命令参数。 一旦匹配成功，后续的 .netrc 令牌就会被处理，当到达文件末尾或遇到另一 `machine` 或 `default` 令牌时停止。

[`default`](#default)

除了 `default` 匹配任何名称外，这与 `machine` name 相同。 `default` 令牌只能有一个，而且必须是所有 `machine` 令牌。 这通常用作：

`default login anonymous password user@site`

从而使用户可以自动匿名 FTP 登录到 .netrc 中未指定的机器。这可以通过使用 `-n` 标志来禁用自动登录来覆盖。

[`login`](#login) name

识别远程机器上的用户。 如果存在此令牌，则自动登录过程将使用指定的 name 启动登录。

[`password`](#password) string

提供密码。 如果存在此令牌，并且远程服务器在登录过程中需要密码，则自动登录过程将提供指定的字符串。 请注意，如果 .netrc 文件中存在除 anonymous 以外的任何用户的此令牌，则如果该用户以外的任何人都可以读取 .netrc ，则 `ftp` 将中止自动登录过程。

[`account`](#account_2) string

提供额外的帐户密码。 如果此令牌存在，如果远程服务器需要额外的帐户密码，自动登录进程将提供指定的字符串，否则自动登录进程将启动 `ACCT` 命令。

[`macdef`](#macdef_2) name

定义一个宏。此令牌的功能类似于 `ftp` `macdef` 命令功能。 使用指定名称定义宏；它的内容从下一个 .netrc 行开始，一直持续到遇到空行（连续的换行符）。 与 .netrc 文件中的其他标记一样， `macdef` 仅适用于它之前的 `machine` 定义。 一个 `macdef` 条目不能被多个 `machine` 定义使用；相反，它必须在它打算使用的每台 `machine` 之后定义。 如果定义了名为 `init` 的宏，它会作为自动登录过程的最后一步自动执行。例如，

default macdef init epsv4 off 

后跟一个空行。

[命令行编辑](#__u547D___u4EE4___u884C___u7F16___u8F91_)
==================================================

`ftp` 通过 editline(3) 库支持交互式命令行编辑。 它通过 `edit` 命令启用，如果输入来自 tty，则默认启用。 可以使用箭头键调用和编辑以前的行，也可以使用其他 GNU Emacs 样式的编辑键。

editline(3) 库配置了一个 .editrc 文件 - 请参阅 editrc(5) 了解更多信息。

`ftp` 可以使用额外的键绑定来提供上下文相关的命令和文件名完成（包括远程文件完成）。 要使用它，请将一个键绑定到 editline(3) 命令 `ftp-complete` 。 默认情况下，它绑定到 TAB 键。

[命令行提示](#__u547D___u4EE4___u884C___u63D0___u793A_)
==================================================

默认情况下， `ftp` 向用户显示命令行提示符 “ftp> ” 。 这可以使用 `set prompt` 命令进行更改。

使用 `set rprompt` 命令可以在屏幕右侧（输入命令后）显示提示。

以下格式序列由给定信息替换：

[`%/`](#_/)

当前的远程工作目录。

%c\[\[`0`\]n\],`%.`\[\[`0`\]n\]

当前远程工作目录的尾随组件，如果给出数字 _n_ ，则为 _n_ 尾随组件。 如果 _n_ 以 ‘0’ 开头，则跳过的组件数在尾随组件之前，格式为 “`/``<`number`>`trailing” (用于 ‘%c’) 或 “`...`trailing” (用于 ‘%.’) 。

[`%M`](#_M)

远程主机名。

[`%m`](#_m)

远程主机名，直到第一个 ‘.’ 。

[`%n`](#_n)

远程用户名。

[`%%`](#__)

一个 ‘%’ 。

[环境](#__u73AF___u5883_)
=======================

`ftp` 使用以下环境变量。

[`FTPANONPASS`](#FTPANONPASS)

在匿名 FTP 传输中发送的密码。默认为 “``` `whoami`@```” 。

[`FTPMODE`](#FTPMODE)

覆盖默认操作模式。 支持值是：

[`active`](#active)

仅主动模式 FTP

[`auto`](#auto)

自动确定被动或主动（这是默认设置）

[`gate`](#gate_2)

gate-ftp 模式

[`passive`](#passive_2)

仅被动模式 FTP

[`FTPPROMPT`](#FTPPROMPT)

要使用的命令行提示符。 默认为 “ftp> ” 。 有关详细信息，请参阅 [命令行提示](#__u547D___u4EE4___u884C___u63D0___u793A_) 。

[`FTPRPROMPT`](#FTPRPROMPT)

要使用的命令行右侧提示。 默认为 “” 。 有关详细信息，请参阅 [命令行提示](#__u547D___u4EE4___u884C___u63D0___u793A_) 。

[`FTPSERVER`](#FTPSERVER)

启用 `gate` 时用作 gate-ftp 服务器的主机。

[`FTPSERVERPORT`](#FTPSERVERPORT)

启用 `gate` 时连接到 gate-ftp 服务器时使用的端口。 默认是 “ftpgate/tcp” 的 `getservbyname`() 查找返回的端口。

[`FTPUSERAGENT`](#FTPUSERAGENT)

为 HTTP User-Agent 标头发送的值。

[`HOME`](#HOME)

对于 .netrc 文件的默认位置（如果存在）。

[`NETRC`](#NETRC)

.netrc 文件的备用位置。

[`PAGER`](#PAGER)

由各种命令用来显示文件。如果为空或未设置，则默认为 more(1) 。

[`SHELL`](#SHELL)

对于默认 shell。

[`ftp_proxy`](#ftp_proxy_2)

发出 FTP URL 请求时使用的 FTP 代理的 URL（如果未定义，则使用标准 FTP 协议）。

有关代理使用的更多说明，请参阅 `http_proxy` 。

[`http_proxy`](#http_proxy_2)

发出 HTTP URL 请求时使用的 HTTP 代理的 URL。 如果需要代理身份验证并且此 URL 中有用户名和密码，它们将在首次尝试对代理进行身份验证时自动使用。

如果用户名或密码中需要 “unsafe” 的 URL 字符（例如 ‘@’ 或 ‘/’), 请使用 `RFC3986` ‘`%`XX’ 编码对它们进行编码。

请注意，在 `ftp_proxy` 和 `http_proxy` 中使用用户名和密码可能与使用它的其他程序（例如 lynx(1)) 不兼容。

_注意_: 注意：这不用于交互式会话，仅用于命令行获取。

[`no_proxy`](#no_proxy_2)

不使用代理的主机（或域）的空格或逗号分隔列表。 每个条目可能有一个可选的尾随 ":port", 它将匹配限制为与该端口的连接。

[扩展被动模式和防火墙](#__u6269___u5C55___u88AB___u52A8___u6A21___u5F0F___u548C___u9632___u706B___u5899_)
===============================================================================================

某些防火墙配置不允许 `ftp` 使用扩展被动模式。 如果您发现即使是简单的 `ls` 在打印如下消息后也出现挂起：

`229 Entering Extended Passive Mode (|||58551|)`

那么您将需要在关闭 `epsv4` 的情况下禁用扩展被动模式。 有关如何自动执行此操作的示例，请参见上面的 [.netrc](#.netrc) 文件部分。

[参见](#__u53C2___u89C1_)
=======================

getservbyname(3), editrc(5), services(5), ftpd(8)

[标准](#__u6807___u51C6_)
=======================

`ftp` 尝试遵守：

[`RFC0959`](#RFC0959)

_文件传输协议_

[`RFC1123`](#RFC1123)

_主机要求 - 应用程序和支持_

[`RFC1635`](#RFC1635)

_如何使用匿名 FTP_

[`RFC2389`](#RFC2389)

_文件传输协议的特性协商机制_

[`RFC2428`](#RFC2428)

_IPv6 和 NAT 的 FTP 扩展_

[`RFC2616`](#RFC2616)

_超文本传输协议——HTTP/1.1_

[`RFC2822`](#RFC2822)

_互联网消息格式_

[`RFC3659`](#RFC3659)

_FTP 扩展_

[`RFC3986`](#RFC3986)

_统一资源标识符 (URI)_

[历史](#__u5386___u53F2_)
=======================

`ftp` 命令出现在 4.2BSD 中。

各种功能，例如命令行编辑、上下文相关的命令和文件完成、动态进度条、文件和 URL 的自动获取、修改时间保存、传输速率限制、可配置的命令行提示符，以及标准 BSD `ftp` 的其他增强功能都在 NetBSD 1.3 及更高版本由 Luke Mewburn ⟨lukem@NetBSD.org⟩ 。

WIDE/KAME 项目添加了 IPv6 支持（但可能不会出现在该程序的所有非 NetBSD 版本中，这取决于操作系统是否以与 KAME 类似的方式支持 IPv6）。

[缺陷](#__u7F3A___u9677_)
=======================

许多命令的正确执行取决于远程服务器的正确行为。

4.2BSD ascii 模式传输代码中的回车处理错误已得到纠正。 此更正可能导致二进制文件与使用 ascii 类型的 4.2BSD 服务器之间的错误传输。 使用二进制图像类型可以避免此问题。

`ftp` 假定所有 IPv4 映射地址（格式为 `::ffff:10.1.1.1` 的 IPv6 地址）表示可以由 `AF_INET` 套接字处理的 IPv4 目标。 但是，在某些 IPv6 网络配置中，此假设不成立。 在这样的环境中，IPv4 映射地址必须直接传递给 `AF_INET6` 套接字。 例如，如果您的站点使用 SIIT 转换器进行 IPv6 到 IPv4 的转换，则 `ftp` 无法支持您的配置。

May 10, 2008

FreeBSD 13.1-RELEASE