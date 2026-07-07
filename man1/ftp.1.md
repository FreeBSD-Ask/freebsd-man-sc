# ftp(1)

`ftp` — Internet 文件传输程序

## 名称

`ftp`

## 概要

`ftp [-46AadefginpRtVv] [-N netrc] [-o output] [-P port] [-q quittime] [-r retry] [-s srcaddr] [-T direction,maximum[,increment]] [[user@]host [port]] [[user@]host:path[/]] [file:///path] [ftp://[user[:password]@]host[:port]/path[/][;type=X]] [http://[user[:password]@]host[:port]/path] [...]`

`ftp -u URL file [...]`

## 描述

`ftp` 是 Internet 标准文件传输协议的用户界面。该程序允许用户在远程网络站点之间传输文件。

最后五种参数格式将通过 FTP 或 HTTP 协议获取文件，或通过直接复制将其存入当前目录。这非常适合脚本使用。更多信息请参见下文"自动获取文件"章节。

选项可在命令行或命令解释器中指定。

**`-4`** 强制 `ftp` 仅使用 IPv4 地址。

**`-6`** 强制 `ftp` 仅使用 IPv6 地址。

**`-A`** 强制使用主动模式 ftp。默认情况下，`ftp` 会尝试使用被动模式 ftp，若服务器不支持被动模式则回退到主动模式。此选项使 `ftp` 始终使用主动连接。仅当连接到无法正确实现被动模式的旧服务器时才有用。

**`-a`** 使 `ftp` 跳过正常登录过程，改用匿名登录。

**`-d`** 启用调试。

**`-e`** 禁用命令行编辑。适用于 Emacs ange-ftp 模式。

**`-f`** 强制对通过 FTP 或 HTTP 代理进行的传输重新加载缓存。

**`-g`** 禁用文件名通配。

**`-i`** 在多文件传输期间关闭交互式提示。

**`-N`** `netrc` 使用 `netrc` 替代 `~/.netrc`。更多信息请参见下文"THE .netrc FILE"章节。

**`-n`** 限制 `ftp` 在非自动获取传输的初始连接时尝试"自动登录"。如果启用了自动登录，`ftp` 会检查用户主目录中的 `.netrc` 文件（见下文），查找描述远程机器账户的条目。如果不存在此类条目，`ftp` 会提示输入远程机器登录名（默认为本地机器上的用户身份），如有必要还会提示输入密码和登录账户。要为自动获取传输覆盖自动登录，请按需指定用户名（可选密码）。

**`-o`** `output` 自动获取文件时，将内容保存到 `output`。`output` 按下文"文件命名约定"章节解析。如果 `output` 不是 ‘-’ 或不以 ‘|’ 开头，则只有第一个指定的文件会被检索到 `output` 中；所有其他文件将以远程名称的基本名（basename）保存。

**`-P`** `port` 将端口号设置为 `port`。

**`-p`** 启用被动模式操作，适用于连接过滤防火墙之后的环境。此选项已被弃用，因为 `ftp` 现在默认尝试使用被动模式，若服务器不支持被动连接则回退到主动模式。

**`-q`** `quittime` 如果连接停滞超过 `quittime` 秒则退出。

**`-`** 重启所有非代理的自动获取。

**`-r`** `wait` 如果连接尝试失败则重试，暂停 `wait` 秒。

**`-s`** `srcaddr` 将 `srcaddr` 用作所有连接的本地 IP 地址。

**`-t`** 启用数据包跟踪。

**`-T`** `direction`,`maximum`[,`increment`] 将 `direction` 方向的最大传输速率设置为 `maximum` 字节/秒，如指定则将增量设置为 `increment` 字节/秒。更多信息请参见 `rate`。

**`-u`** `URL file` [...] 将命令行上的文件上传到 `URL`，其中 `URL` 是自动获取所支持的某种 ftp URL 类型（单文件上传可指定目标文件名），`file` 是一个或多个要上传的本地文件。

**`-V`** 禁用 `verbose` 和 `progress`，覆盖输出到终端时默认启用的设置。

**`-v`** 启用 `verbose` 和 `progress`。当输出到终端时（且对于 `progress`，`ftp` 是前台进程），这是默认行为。强制 `ftp` 显示来自远程服务器的所有响应，并报告数据传输统计信息。

可以在命令行上指定 `ftp` 要通信的客户端主机。如果这样做，`ftp` 会立即尝试建立到该主机 FTP 服务器的连接；否则，`ftp` 将进入其命令解释器并等待用户指令。当 `ftp` 等待用户命令时，会向用户提供 `ftp` 提示符。`ftp` 识别以下命令：

```sh
nmap $1.$2.$3 [$1,$2].[$2,file]
```

```sh
nmap $1 sed s/ *$// $1
```

**`a`** 对当前文件回答"yes"，并对当前命令的剩余所有文件自动回答"yes"。

**`n`** 回答"no"，不传输该文件。

**`p`** 对当前文件回答"yes"，并关闭提示模式（等同于执行"prompt off"）。

**`q`** 终止当前操作。

**`y`** 回答"yes"，并传输该文件。

**`?`** 显示帮助信息。

**`all`** 双向（传入和传出）。

**`get`** 传入传输。

**`put`** 传出传输。

**`SIGUSR1`** 将 `maximum` 增加 `increment` 字节。

**`SIGUSR2`** 将 `maximum` 减少 `increment` 字节。结果必须为正数。

**`anonpass`** 默认为 `$FTPANONPASS`。

**`ftp_proxy`** 默认为 `$ftp_proxy`。

**`http_proxy`** 默认为 `$http_proxy`。

**`no_proxy`** 默认为 `$no_proxy`。

**`pager`** 默认为 `$PAGER`。

**`prompt`** 默认为 `$FTPPROMPT`。

**`rprompt`** 默认为 `$FTPRPROMPT`。

**`!`** [`command` [`args`]] 在本地机器上调用交互式 shell。如果有参数，第一个参数被视为要直接执行的命令，其余参数作为该命令的参数。

**`$`** `macro-name` [`args`] 执行由 `macdef` 命令定义的宏 `macro-name`。参数以未通配的形式传递给宏。

**`account`** [`passwd`] 提供远程系统在成功登录后访问资源所需的补充密码。如果不带参数，用户将以非回显输入模式被提示输入账户密码。

**`append`** `local-file` [`remote-file`] 将本地文件追加到远程机器上的文件。如果未指定 `remote-file`，本地文件名在经过 `ntrans` 或 `nmap` 设置处理后用作远程文件名。文件传输使用当前的 `type`、`format`、`mode` 和 `structure` 设置。

**`ascii`** 将文件传输 `type` 设置为网络 ASCII。这是默认类型。

**`bell`** 安排在每个文件传输命令完成后响铃。

**`binary`** 将文件传输 `type` 设置为支持二进制图像传输。

**`bye`** 终止与远程服务器的 FTP 会话并退出 `ftp`。文件结束符（EOF）也会终止会话并退出。

**`case`** 切换 `get`、`mget` 和 `mput` 命令期间远程计算机文件名的大小写映射。当 `case` 打开时（默认为关闭），远程计算机上全部字母为大写的文件名在写入本地目录时映射为小写。

**`cd`** `remote-directory` 将远程机器的工作目录更改为 `remote-directory`。

**`cdup`** 将远程机器工作目录更改为当前远程机器工作目录的父目录。

**`chmod`** `mode remote-file` 将远程系统上文件 `remote-file` 的权限模式更改为 `mode`。

**`close`** 终止与远程服务器的 FTP 会话，并返回命令解释器。所有已定义的宏都会被清除。

**`cr`** 切换 ascii 类型文件检索期间的回车符剥离。ascii 类型文件传输时，记录由回车符/换行符序列表示。当 `cr` 打开时（默认），此序列中的回车符会被剥离，以符合 UNIX 单换行符记录分隔符的规范。非 UNIX 远程系统上的记录可能包含单个换行符；进行 ascii 类型传输时，只有当 `cr` 关闭时才能将这些换行符与记录分隔符区分开来。

**`delete`** `remote-file` 删除远程机器上的文件 `remote-file`。

**`dir`** [`remote-path` [`local-file`]] 打印远程机器上目录内容的列表。该列表包含服务器选择包含的任何依赖于系统的信息；例如，大多数 UNIX 系统会产生 `ls -l` 命令的输出。如果未指定 `remote-path`，则使用当前工作目录。如果启用了交互式提示，`ftp` 会提示用户确认最后一个参数确实是接收 `dir` 输出的目标本地文件。如果未指定本地文件，或 `local-file` 为 ‘`-`’，输出将发送到终端。

**`disconnect`** `close` 的同义词。

**`edit`** 切换命令行编辑以及上下文敏感的命令和文件补全。如果输入来自终端则自动启用，否则禁用。

**`epsv epsv4 epsv6`** 分别在所有 IP、IPv4 和 IPv6 连接上切换扩展 `EPSV` 和 `EPRT` 命令的使用。首先尝试 `EPSV`/`EPRT`，然后尝试 `PASV`/`PORT`。默认启用。如果扩展命令失败，则在当前连接期间或再次执行 `epsv`、`epsv4` 或 `epsv6` 之前临时禁用此选项。

**`exit`** `bye` 的同义词。

**`features`** 显示远程服务器支持的功能（使用 `FEAT` 命令）。

**`fget`** `localfile` 检索 `localfile` 中列出的文件，每行一个文件名。

**`form`** `format` 将文件传输 `form` 设置为 `format`。默认（且唯一支持的）格式为"non-print"。

**`ftp`** `host` [`port`] `open` 的同义词。

**`ftp_debug`** [`ftp_debug-value`] 切换调试模式。如果指定了可选的 `ftp_debug-value`，则用于设置调试级别。启用调试时，`ftp` 会打印发送到远程机器的每条命令，前缀为字符串 `--`。

**`gate`** [`host` [`port`]] 切换 gate-ftp 模式，用于通过 TIS FWTK 和 Gauntlet ftp 代理连接。如果未设置 gate-ftp 服务器（用户显式设置或从 `FTPSERVER` 环境变量获取），则不允许此操作。如果指定了 `host`，则启用 gate-ftp 模式，并将 gate-ftp 服务器设置为 `host`。如果还指定了 `port`，则将其用作连接 gate-ftp 服务器的端口。

**`get`** `remote-file` [`local-file`] 检索 `remote-file` 并存储在本地机器上。如果未指定本地文件名，则使用与远程机器上相同的名称，但需经过当前 `case`、`ntrans` 和 `nmap` 设置的处理。传输文件时使用当前的 `type`、`form`、`mode` 和 `structure` 设置。

**`glob`** 切换 `mdelete`、`mget`、`mput` 和 `mreget` 的文件名扩展。如果通过 `glob` 关闭了通配，文件名参数按字面意义使用而不进行扩展。`mput` 的通配按 csh(1) 的方式进行。对于 `mdelete`、`mget` 和 `mreget`，每个远程文件名在远程机器上单独扩展，列表不合并。目录名扩展的结果可能不同于普通文件名扩展：确切结果取决于外来的操作系统和 ftp 服务器，可通过执行 `mls remote-files -` 预览。注意：`mget`、`mput` 和 `mreget` 不用于传输整个目录子树。可以通过传输子树的 tar(1) 归档（在二进制模式下）来实现。

**`hash`** [`size`] 切换每个传输数据块的哈希符号（‘#’）打印。数据块大小默认为 1024 字节。可通过以字节为单位指定 `size` 来更改。启用 `hash` 会禁用 `progress`。

**`help`** [`command`] 打印关于 `command` 含义的信息性消息。如果不带参数，`ftp` 会打印已知命令列表。

**`idle`** [`seconds`] 将远程服务器上的非活动计时器设置为 `seconds` 秒。如果省略 `seconds`，则打印当前非活动计时器。

**`image`** `binary` 的同义词。

**`lcd`** [`directory`] 更改本地机器上的工作目录。如果未指定 `directory`，则使用用户的主目录。

**`less`** `file` `page` 的同义词。

**`lpage`** `local-file` 使用 `set pager` 选项指定的程序显示 `local-file`。

**`lpwd`** 打印本地机器上的工作目录。

**`ls`** [`remote-path` [`local-file`]] `dir` 的同义词。

**`macdef`** `macro-name` 定义宏。后续行存储为宏 `macro-name`；空行（文件中连续的换行符或终端的回车）终止宏输入模式。所有已定义宏的总数限制为 16 个，总字符数限制为 4096。宏名最多 8 个字符。宏仅适用于定义它的当前会话（如果在会话外定义，则适用于下一次 `open` 命令调用的会话），并保持定义直到执行 `close` 命令。要调用宏，使用 `$` 命令（见上文）。宏处理器将 ‘$’ 和 ‘e’ 解释为特殊字符。‘$’ 后跟一个或多个数字将被替换为宏调用命令行上的相应参数。‘$’ 后跟 ‘i’ 通知宏处理器正在执行的宏将循环。第一次遍历时"$i"被替换为宏调用命令行上的第一个参数，第二次遍历时替换为第二个参数，依此类推。‘e’ 后跟任何字符将被替换为该字符。使用 ‘e’ 可防止 ‘$’ 的特殊处理。

**`mdelete`** [`remote-files`] 删除远程机器上的 `remote-files`。

**`mdir`** `remote-files local-file` 类似于 `dir`，但可指定多个远程文件。如果启用了交互式提示，`ftp` 会提示用户确认最后一个参数确实是接收 `mdir` 输出的目标本地文件。

**`mget`** `remote-files` 在远程机器上扩展 `remote-files`，并为由此产生的每个文件名执行一次 `get`。有关文件名扩展的详细信息，请参见 `glob`。生成的文件名将根据 `case`、`ntrans` 和 `nmap` 设置进行处理。文件传输到本地工作目录，可通过 `lcd directory` 更改；可使用 `! mkdir directory` 创建新的本地目录。

**`mkdir`** `directory-name` 在远程机器上创建目录。

**`mls`** `remote-files local-file` 类似于 `ls`，但可指定多个远程文件，且必须指定 `local-file`。如果启用了交互式提示，`ftp` 会提示用户确认最后一个参数确实是接收 `mls` 输出的目标本地文件。

**`mlsd`** [`remote-path`] 使用 `MLSD` 以机器可解析的形式显示 `remote-path`（如未指定则默认为当前目录）的内容。显示格式可通过 ‘remopts mlst ...’ 更改。

**`mlst`** [`remote-path`] 使用 `MLST` 以机器可解析的形式显示 `remote-path`（如未指定则默认为当前目录）的详细信息。显示格式可通过 ‘remopts mlst ...’ 更改。

**`mode`** `mode-name` 将文件传输 `mode` 设置为 `mode-name`。默认（且唯一支持的）模式为"stream"。

**`modtime`** `remote-file` 以 `RFC2822` 格式显示远程机器上文件的最后修改时间。

**`more`** `file` `page` 的同义词。

**`mput`** `local-files` 扩展作为参数给出的本地文件列表中的通配符，并为结果列表中的每个文件执行一次 `put`。有关文件名扩展的详细信息，请参见 `glob`。生成的文件名将根据 `ntrans` 和 `nmap` 设置进行处理。

**`mreget`** `remote-files` 类似于 `mget`，但执行 `reget` 而非 `get`。

**`msend`** `local-files` `mput` 的同义词。

**`newer`** `remote-file` [`local-file`] 仅当远程文件的修改时间比当前系统上的文件更新时才获取该文件。如果当前系统上不存在该文件，则认为远程文件更新。否则，此命令与 `get` 相同。

**`nlist`** [`remote-path` [`local-file`]] `ls` 的同义词。

**`nmap`** [`inpattern outpattern`] 设置或取消文件名映射机制。如果不指定参数，则取消文件名映射机制。如果指定参数，则在 `mput` 命令和未指定远程目标文件名的 `put` 命令期间映射远程文件名。如果指定参数，则在 `mget` 命令和未指定本地目标文件名的 `get` 命令期间映射本地文件名。此命令在连接到具有不同文件命名约定或做法的非 UNIX 远程计算机时很有用。映射遵循 `inpattern` 和 `outpattern` 设置的模式。`inpattern` 是传入文件名的模板（可能已经根据 `ntrans` 和 `case` 设置处理过）。通过在 `inpattern` 中包含序列"$1"、"$2"、... "$9"来实现变量模板。使用 ‘e’ 可防止 ‘$’ 字符的这种特殊处理。所有其他字符按字面意义处理，用于确定 `nmap` [`inpattern`] 变量的值。例如，给定 `inpattern` $1.$2 和远程文件名"mydata.data"，$1 的值为"mydata"，$2 的值为"data"。`outpattern` 决定生成的映射文件名。序列"$1"、"$2"、... "$9"被 `inpattern` 模板产生的任何值替换。序列"$0"被原始文件名替换。此外，序列"[`seq1`, `seq2`]"在 `seq1` 不是空字符串时被替换为 `seq1`；否则被替换为 `seq2`。例如，该命令对于输入文件名"myfile.data"和"myfile.data.old"会生成输出文件名"myfile.data"，对于输入文件名"myfile"生成"myfile.file"，对于输入文件名".myfile"生成"myfile.myfile"。`outpattern` 中可包含空格，如示例所示：使用 ‘e’ 字符可防止 ‘$’、‘[’、‘]’ 和 ‘,’ 字符的特殊处理。

**`ntrans`** [`inchars` [`outchars`]] 设置或取消文件名字符转换机制。如果不指定参数，则取消文件名字符转换机制。如果指定参数，则在 `mput` 命令和未指定远程目标文件名的 `put` 命令期间转换远程文件名中的字符。如果指定参数，则在 `mget` 命令和未指定本地目标文件名的 `get` 命令期间转换本地文件名中的字符。此命令在连接到具有不同文件命名约定或做法的非 UNIX 远程计算机时很有用。文件名中匹配 `inchars` 中字符的字符将被替换为 `outchars` 中的对应字符。如果字符在 `inchars` 中的位置超过 `outchars` 的长度，则从文件名中删除该字符。

**`open`** `host` [`port`] 建立到指定 `host` FTP 服务器的连接。可提供可选端口号，此时 `ftp` 会尝试联系该端口上的 FTP 服务器。如果 `set auto-login` 选项打开（默认），`ftp` 还会尝试自动将用户登录到 FTP 服务器（见下文）。

**`page`** `file` 检索 `file` 并使用 `set pager` 选项指定的程序显示。

**`passive`** [`auto`] 切换被动模式（不带参数时）。如果指定 `auto`，行为如同 `FTPMODE` 设置为 ‘auto’。如果打开被动模式（默认），`ftp` 会对所有数据连接发送 `PASV` 命令而非 `PORT` 命令。`PASV` 命令请求远程服务器为数据连接打开一个端口并返回该端口的地址。远程服务器在该端口监听，客户端连接到它。使用更传统的 `PORT` 命令时，客户端在某个端口监听并将该地址发送给远程服务器，由远程服务器回连。当通过控制流量方向的网关路由器或主机使用 `ftp` 时，被动模式很有用。（注意，虽然 `RFC1123` 要求 FTP 服务器支持 `PASV` 命令，但有些服务器不支持。）

**`pdir`** [`remote-path`] 执行 `dir` [`remote-path`]，并使用 `set pager` 选项指定的程序显示结果。

**`pls`** [`remote-path`] 执行 `ls` [`remote-path`]，并使用 `set pager` 选项指定的程序显示结果。

**`pmlsd`** [`remote-path`] 执行 `mlsd` [`remote-path`]，并使用 `set pager` 选项指定的程序显示结果。

**`preserve`** 切换是否保留检索文件的修改时间。

**`progress`** 切换传输进度条的显示。对于 `local-file` 为 ‘`-`’ 或以 ‘|’ 开头的命令的传输，进度条将被禁用。更多信息请参见下文"文件命名约定"章节。启用 `progress` 会禁用 `hash`。

**`prompt`** 切换交互式提示。交互式提示在多文件传输期间出现，允许用户选择性检索或存储文件。如果关闭提示（默认为打开），任何 `mget` 或 `mput` 都会传输所有文件，任何 `mdelete` 都会删除所有文件。启用提示时，提示符下可使用以下命令：任何其他响应都会对当前文件回答 ‘yes’。

**`proxy`** `ftp-command` 在辅助控制连接上执行 ftp 命令。此命令允许同时连接两个远程 FTP 服务器以在两台服务器之间传输文件。第一个 `proxy` 命令应该是 `open`，以建立辅助控制连接。输入命令"proxy ?"可查看辅助连接上可执行的其他 FTP 命令。以下命令在前面加上 `proxy` 时行为不同：`open` 在自动登录过程中不会定义新宏，`close` 不会清除已存在的宏定义，`get` 和 `mget` 将文件从主控制连接上的主机传输到辅助控制连接上的主机，`put`、`mput` 和 `append` 将文件从辅助控制连接上的主机传输到主控制连接上的主机。第三方文件传输取决于辅助控制连接上的服务器是否支持 FTP 协议 `PASV` 命令。

**`put`** `local-file` [`remote-file`] 将本地文件存储到远程机器上。如果未指定 `remote-file`，本地文件名在经过 `ntrans` 或 `nmap` 设置处理后用作远程文件名。文件传输使用当前的 `type`、`format`、`mode` 和 `structure` 设置。

**`pwd`** 打印远程机器上当前工作目录的名称。

**`quit`** `bye` 的同义词。

**`quote`** `arg1 arg2 ...` 指定的参数原样发送到远程 FTP 服务器。

**`rate`** `direction` [`maximum` [`increment`]] 将最大传输速率限制为 `maximum` 字节/秒。如果 `maximum` 为 0，则禁用限制。`direction` 可以是以下之一：`maximum` 可在每次收到给定信号时按 `increment` 字节（默认：1024）即时修改：如果未提供 `maximum`，则显示当前限制速率。注意：`rate` 尚未在 ascii 模式传输中实现。

**`rcvbuf`** `size` 将套接字接收缓冲区大小设置为 `size`。

**`recv`** `remote-file` [`local-file`] `get` 的同义词。

**`reget`** `remote-file` [`local-file`] `reget` 类似于 `get`，但如果 `local-file` 已存在且小于 `remote-file`，则假定 `local-file` 是 `remote-file` 的部分传输副本，并从明显的失败点继续传输。此命令在通过容易断开连接的网络传输非常大的文件时很有用。

**`remopts`** `command` [`command-options`] 为 `command` 在远程 FTP 服务器上设置选项为 `command-options`（其缺失按命令特定方式处理）。已知支持选项的远程 FTP 命令包括：‘MLST’（用于 `MLSD` 和 `MLST`）。

**`rename`** [`from` [`to`]] 将远程机器上的文件 `from` 重命名为 `to`。

**`reset`** 清除回复队列。此命令重新同步与远程 FTP 服务器的命令/回复序列。在远程服务器违反 FTP 协议后，可能需要重新同步。

**`restart`** `marker` 在指示的 `marker` 处重启紧随其后的 `get` 或 `put`。在 UNIX 系统上，marker 通常是文件中的字节偏移量。

**`rhelp`** [`command-name`] 请求远程 FTP 服务器的帮助。如果指定了 `command-name`，也会将其提供给服务器。

**`rmdir`** `directory-name` 删除远程机器上的目录。

**`rstatus`** [`remote-file`] 不带参数时显示远程机器的状态。如果指定了 `remote-file`，则显示远程机器上 `remote-file` 的状态。

**`runique`** 切换在本地系统上以唯一文件名存储文件。如果 `get` 或 `mget` 命令的目标本地文件名已存在同名文件，则在名称后追加".1"。如果结果名称与另一个现有文件匹配，则在原始名称后追加".2"。如果此过程继续到".99"，将打印错误消息且不进行传输。会报告生成的唯一文件名。注意，`runique` 不会影响从 shell 命令生成的本地文件（见下文）。默认值为关闭。

**`send`** `local-file` [`remote-file`] `put` 的同义词。

**`sendport`** 切换 `PORT` 命令的使用。默认情况下，`ftp` 在为每次数据传输建立连接时会尝试使用 `PORT` 命令。使用 `PORT` 命令可防止在执行多文件传输时的延迟。如果 `PORT` 命令失败，`ftp` 会使用默认数据端口。禁用 `PORT` 命令时，不会为每次数据传输尝试使用 `PORT` 命令。这对于某些忽略 `PORT` 命令但错误地表示已接受它们的 FTP 实现很有用。

**`set`** [`option` `value`] 将 `option` 设置为 `value`。如果不提供 `option` 和 `value`，则显示所有选项及其值。当前支持的选项有：

**`site`** `arg1 arg2 ...` 指定的参数作为 `SITE` 命令原样发送到远程 FTP 服务器。

**`size`** `remote-file` 返回远程机器上 `remote-file` 的大小。

**`sndbuf`** `size` 将套接字发送缓冲区大小设置为 `size`。

**`status`** 显示 `ftp` 的当前状态。

**`struct`** `struct-name` 将文件传输 `structure` 设置为 `struct-name`。默认（且唯一支持的）结构为"file"。

**`sunique`** 切换在远程机器上以唯一文件名存储文件。远程 FTP 服务器必须支持 FTP 协议 `STOU` 命令才能成功完成。远程服务器会报告唯一名称。默认值为关闭。

**`system`** 显示远程机器上运行的操作系统类型。

**`tenex`** 将文件传输类型设置为与 TENEX 机器通信所需的类型。

**`throttle`** `rate` 的同义词。

**`trace`** 切换数据包跟踪。

**`type`** [`type-name`] 将文件传输 `type` 设置为 `type-name`。如果未指定类型，则打印当前类型。默认类型为网络 ASCII。

**`umask`** [`newmask`] 将远程服务器上的默认 umask 设置为 `newmask`。如果省略 `newmask`，则打印当前 umask。

**`unset`** `option` 取消设置 `option`。更多信息请参见 `set`。

**`usage`** `command` 打印 `command` 的用法消息。

**`user`** `user-name` [`password` [`account`]] 向远程 FTP 服务器标识自己。如果未指定 `password` 而服务器需要它，`ftp` 会提示用户输入（在禁用本地回显之后）。如果未指定 `account` 字段而 FTP 服务器需要它，用户将被提示输入。如果指定了 `account` 字段，则在登录序列完成后，如果远程服务器登录时不需要它，将向远程服务器中继一条 account 命令。除非以禁用"自动登录"的方式调用 `ftp`，否则此过程会在初始连接 FTP 服务器时自动完成。

**`verbose`** 切换详细模式。在详细模式下，FTP 服务器的所有响应都会显示给用户。此外，如果启用了 verbose，当文件传输完成时，会报告有关传输效率的统计信息。默认启用 verbose。

**`xferbuf`** `size` 将套接字发送和接收缓冲区大小设置为 `size`。

**`?`** [`command`] `help` 的同义词。

包含嵌入空格的命令参数可以用引号 ‘"’ 括起来。

切换设置的命令可以接受显式的 `on` 或 `off` 参数以强制相应设置。

以字节计数为参数的命令（例如 `hash`、`rate` 和 `xferbuf`）支持参数上的可选后缀以更改参数的解释。支持的后缀有：

**`b`** 不进行修改。（可选）

**`k`** Kilo；将参数乘以 1024。

**`m`** Mega；将参数乘以 1048576。

**`g`** Giga；将参数乘以 1073741824。

如果 `ftp` 在传输进行中收到 `SIGINFO`（参见 stty(1) 的"status"参数）或 `SIGQUIT` 信号，当前传输速率统计信息将以与标准完成消息相同的格式写入标准错误输出。

## 自动获取文件

除标准命令外，此版本的 `ftp` 支持自动获取功能。要启用自动获取，只需在命令行上传递主机名/文件列表。

以下格式是自动获取元素的有效语法：

- `host`[`:`[`port`]] 之后的 ‘`/`’ 被解释为 `path` 之前的分隔符，而非 `path` 本身的一部分。
- `path` 被解释为由 ‘`/`’ 分隔的名称组件列表。对于除最后一个组件外的所有组件，`ftp` 执行等效于 `cd` 命令的操作。对于最后一个路径组件，`ftp` 执行等效于 `get` 命令的操作。
- 由 `path` 中的 ‘`//`’ 或 `path` 开头多余的 ‘`/`’ 产生的空名称组件，会导致执行不带目录名的等效 `cd` 命令。这不太可能有用。
- 路径组件中的任何 ‘`%``XX`’ 代码（按 `RFC3986`）都会被解码，`XX` 表示十六进制的字符代码。此解码发生在 `path` 被拆分为组件之后，但在每个组件用于等效 `cd` 或 `get` 命令之前。常用的代码有 ‘`%2F`’（表示 ‘`/`’）和 ‘`%7E`’（表示 ‘`~`’）。

**ftp://host/dir1/dir2/file** “cd dir1”、“cd dir2”、“get file”。

**ftp://host/%2Fdir1/dir2/file** “cd /dir1”、“cd dir2”、“get file”。

**ftp://host/dir1%2Fdir2/file** “cd dir1/dir2”、“get file”。

**ftp://host/%2Fdir1%2Fdir2/file** “cd /dir1/dir2”、“get file”。

**ftp://host/dir1%2Fdir2%2Ffile** “get dir1/dir2/file”。

**ftp://host/%2Fdir1%2Fdir2%2Ffile** “get /dir1/dir2/file”。

- 路径相对于指定用户或 ‘anonymous’ 用户的默认登录目录解释。如果需要 `/` 目录，使用前导路径"%2F"。如果需要用户主目录（且远程服务器支持此语法），使用前导路径"%7Euser/"。例如，要以用户 ‘myname’、密码 ‘mypass’ 从 ‘localhost’ 检索 `/etc/motd`，使用 “ftp://myname:mypass@localhost/%2fetc/motd”
- 通过仔细选择在何处使用 ‘/’ 以及何处使用 ‘%2F’（或 ‘%2f’），可以控制确切的 `cd` 和 `get` 命令。例如，以下 URL 对应于所指示命令的等效操作：
- 你必须对等效 `cd` 命令中使用的每个中间目录具有适当的访问权限。

**`about:ftp`** 关于 `ftp` 的信息。

**`about:version`** `ftp` 的版本。在报告问题时提供此信息很有用。

[`user`[`@`]]`host`[`:`[`path`[`/`]]] “经典”FTP 格式。如果 `path` 包含通配字符且启用了通配（参见 `glob`），则执行等效于 `mget path` 的操作。如果 `path` 的目录组件不包含通配字符，则按 [basename(1)](basename.1.md) 的基本名存储在当前目录中。否则，使用完整的远程名称作为本地名称，相对于本地根目录。

**`ftp://`** [`user`[`:`[`password`]]`@`]`host`[`:`[`port`]]`/``path`[`/`][`;type=`[`X`]] FTP URL，如果未定义 `set ftp_proxy`，则使用 FTP 协议检索。否则，通过 `set ftp_proxy` 中定义的代理使用 HTTP 传输 URL。如果未定义 `set ftp_proxy` 且指定了 `user`，则以 `user` 身份登录。此时，如果提供了 `password` 则使用之，否则提示用户输入。如果提供了 ‘;type=A’ 或 ‘;type=I’ 后缀，则传输类型分别为 ascii 或二进制。默认传输类型为二进制。为了符合 `RFC3986`，`ftp` 按以下方式解释 “ftp://” 自动获取 URL 的 `path` 部分：上述解释有以下后果：

**`http://`** [`user`[`:`[`password`]]`@`]`host`[`:`[`port`]]`/``path` HTTP URL，使用 HTTP 协议检索。如果定义了 `set http_proxy`，则将其用作 HTTP 代理服务器的 URL。如果检索 `path` 需要 HTTP 授权，且 URL 中包含 ‘user’（可选 ‘password’），则将其用于第一次认证尝试。

**`file:///`** `path` 本地 URL，从本地主机的 `/``path` 复制。

**`about:`** `topic` 显示关于 `topic` 的信息；此自动获取元素不会检索任何文件。支持的值包括：

除非上文另有说明，且未指定 `-o` `output`，否则文件以 `path` 的 [basename(1)](basename.1.md) 存储在当前目录中。注意，如果收到 HTTP 重定向，将使用服务器提供的新目标 URL 重试获取，并对应新的 `path`。建议使用显式的 `-o` `output`，以避免写入意外的文件名。

如果经典格式或 FTP URL 格式以 ‘/’ 结尾或 `path` 组件为空，则 `ftp` 会连接到该站点并 `cd` 到作为路径给出的目录，然后让用户留在交互模式以等待进一步输入。如果正在使用 `set ftp_proxy`，则此功能无效。

直接 HTTP 传输使用 HTTP 1.1。代理 FTP 和 HTTP 传输使用 HTTP 1.0。

如果指定 `-`，所有不通过 FTP 或 HTTP 代理的自动获取都将重启。对于 FTP，这通过使用 `reget` 代替 `get` 来实现。对于 HTTP，这通过使用 ‘Range: bytes=’ HTTP/1.1 指令实现。

如果需要 WWW 或代理 WWW 认证，将提示你输入用户名和密码进行认证。

在 URL 中指定 IPv6 数字地址时，需要用方括号括起地址。例如：“ftp://[::1]:21/”。这是因为冒号既用于 IPv6 数字地址，也用作端口号的分隔符。

## 中止文件传输

要中止文件传输，使用终端中断键（通常是 Ctrl-C）。发送传输会立即停止。接收传输会通过向远程服务器发送 FTP 协议 `ABOR` 命令并丢弃后续接收的任何数据来停止。完成此操作的速度取决于远程服务器对 `ABOR` 处理的支持。如果远程服务器不支持 `ABOR` 命令，则在远程服务器完成发送所请求文件之前不会出现提示符。

如果在 `ftp` 等待远程服务器对 ABOR 处理的回复时使用终端中断键序列，则连接将被关闭。这不同于传统行为（在此阶段忽略终端中断），但被认为更有用。

## 文件命名约定

作为 `ftp` 命令参数指定的文件按以下规则处理。

- 如果指定文件名 ‘`-`’，则使用 `stdin`（用于读取）或 `stdout`（用于写入）。
- 如果文件名的第一个字符是 ‘|’，参数的其余部分被解释为 shell 命令。`ftp` 然后使用所提供参数通过 popen(3) 派生 shell，并从 stdout（写入时从 stdin）读取（写入）。如果 shell 命令包含空格，参数必须用引号括起；例如 “"" `| ls\ -lt`”。此机制的一个特别有用的示例是：“`dir "" |more`”。
- 如果上述检查都失败，且启用了 "globbing"，本地文件名按 csh(1) 中使用的规则扩展；参见 `glob` 命令。如果 `ftp` 命令期望单个本地文件（例如 `put`），仅使用 "globbing" 操作生成的第一个文件名。
- 对于未指定本地文件名的 `mget` 命令和 `get` 命令，本地文件名就是远程文件名，可能被 `case`、`ntrans` 或 `nmap` 设置更改。如果 `runique` 打开，结果文件名可能再被更改。
- 对于未指定远程文件名的 `mput` 命令和 `put` 命令，远程文件名就是本地文件名，可能被 `ntrans` 或 `nmap` 设置更改。如果 `sunique` 打开，结果文件名可能再被远程服务器更改。

## 文件传输参数

FTP 规范指定了许多可能影响文件传输的参数。`type` 可以是 "ascii"、"image"（二进制）、"ebcdic" 和 "local byte size"（主要用于 PDP-10 和 PDP-20）。`ftp` 支持 ascii 和 image 类型的文件传输，以及用于 `tenex` 模式传输的本地字节大小 8。

`ftp` 仅支持其余文件传输参数的默认值：`mode`、`form` 和 `struct`。

## THE .netrc FILE

`.netrc` 文件包含自动登录过程使用的登录和初始化信息。它位于用户主目录中，除非通过 `-N` `netrc` 选项覆盖，或在 `NETRC` 环境变量中指定。识别以下标记；它们可以用空格、制表符或换行符分隔：

```sh
default login anonymous password user@site
```

```sh
default
macdef init
epsv4 off
```

**`machine`** `name` 标识远程机器 `name`。自动登录过程在 `.netrc` 文件中搜索与 `ftp` 命令行或 `open` 命令参数指定的远程机器匹配的 `machine` 标记。一旦匹配，后续的 `.netrc` 标记将被处理，直到到达文件末尾或遇到另一个 `machine` 或 `default` 标记时停止。

**`default`** 这与 `machine` `name` 相同，区别在于 `default` 匹配任何名称。只能有一个 `default` 标记，且必须位于所有 `machine` 标记之后。通常用法为：从而为用户在 `.netrc` 中未指定的机器提供自动匿名 FTP 登录。可通过使用 `-n` 标志禁用自动登录来覆盖此行为。

**`login`** `name` 标识远程机器上的用户。如果存在此标记，自动登录过程将使用指定的 `name` 发起登录。

**`password`** `string` 提供密码。如果存在此标记，当远程服务器需要密码作为登录过程的一部分时，自动登录过程会提供指定的字符串。注意，如果 `.netrc` 文件中除 `anonymous` 外的任何用户存在此标记，且 `.netrc` 可被用户以外的任何人读取，`ftp` 将中止自动登录过程。

**`account`** `string` 提供额外的账户密码。如果存在此标记，当远程服务器需要额外账户密码时，自动登录过程会提供指定的字符串，否则自动登录过程会发起 `ACCT` 命令。

**`macdef`** `name` 定义宏。此标记的功能类似于 `ftp` 的 `macdef` 命令。以指定名称定义宏；其内容从 `.netrc` 的下一行开始，直到遇到空行（连续的换行符）。与 `.netrc` 文件中的其他标记一样，`macdef` 仅适用于其前面的 `machine` 定义。一个 `macdef` 条目不能被多个 `machine` 定义使用；相反，它必须定义在每个要使用它的 `machine` 之后。如果定义了名为 `init` 的宏，它将作为自动登录过程的最后一步自动执行。例如，后跟一个空行。

## 命令行编辑

`ftp` 通过 editline(3) 库支持交互式命令行编辑。通过 `edit` 命令启用，如果输入来自 tty 则默认启用。可通过方向键召回和编辑前面的行，也可使用其他 GNU Emacs 风格的编辑键。

editline(3) 库通过 `.editrc` 文件配置——更多信息请参见 editrc(5)。

`ftp` 还提供了一个额外的键绑定，用于上下文敏感的命令和文件名补全（包括远程文件补全）。要使用此功能，将一个键绑定到 editline(3) 命令 `ftp-complete`。默认绑定到 TAB 键。

## 命令行提示符

默认情况下，`ftp` 向用户显示命令行提示符"ftp"。可通过 `set prompt` 命令更改。

可通过 `set rprompt` 命令在屏幕右侧（命令输入之后）显示提示符。

以下格式序列被替换为相应信息：

**`%/`** 当前远程工作目录。

**%c[[`0`]]`n`]]`%.`[[`0`]]`n`]]** 当前远程工作目录的末尾组件，或如果给出数字 *n* 则为末尾 *n* 个组件。如果 *n* 以 ‘0’ 开头，则跳过的组件数量以 “ `/` `` `number` `` `trailing` ” 格式（对于 ‘%c’）或 “`...``trailing`” 格式（对于 ‘%.’）位于末尾组件之前。

**`%M`** 远程主机名。

**`%m`** 远程主机名，截取到第一个 ‘.’ 之前。

**`%n`** 远程用户名。

**`%%`** 单个 ‘%’。

## 环境变量

`ftp` 使用以下环境变量。

**`active`** 仅主动模式 FTP。

**`auto`** 自动确定被动或主动模式（默认）。

**`gate`** gate-ftp 模式。

**`passive`** 仅被动模式 FTP。

**`FTPANONPASS`** 匿名 FTP 传输中发送的密码。默认为 “``whoami`@`”。

**`FTPMODE`** 覆盖默认操作模式。支持的值有：

**`FTPPROMPT`** 使用的命令行提示符。默认为 “ftp”。更多信息请参见下文"命令行提示符"章节。

**`FTPRPROMPT`** 使用的命令行右侧提示符。默认为 “”。更多信息请参见下文"命令行提示符"章节。

**`FTPSERVER`** 启用 `gate` 时用作 gate-ftp 服务器的主机。

**`FTPSERVERPORT`** 启用 `gate` 时连接 gate-ftp 服务器使用的端口。默认为 getservbyname 查询 “ftpgate/tcp” 返回的端口。

**`FTPUSERAGENT`** HTTP User-Agent 头发送的值。

**`HOME`** `.netrc` 文件的默认位置（如果存在）。

**`NETRC`** `.netrc` 文件的备用位置。

**`PAGER`** 各种命令用于显示文件。如果为空或未设置，默认为 more(1)。

**`SHELL`** 默认 shell。

**`ftp_proxy`** 发出 FTP URL 请求时使用的 FTP 代理 URL（如果未定义，使用标准 FTP 协议）。有关代理使用的更多说明，请参见 `http_proxy`。

**`http_proxy`** 发出 HTTP URL 请求时使用的 HTTP 代理 URL。如果需要代理认证且此 URL 中包含用户名和密码，它们将自动用于第一次代理认证尝试。如果用户名或密码中需要"不安全"的 URL 字符（例如 ‘@’ 或 ‘/’），请使用 `RFC3986` 的 ‘`%``XX`’ 编码。注意，在 `ftp_proxy` 和 `http_proxy` 中使用用户名和密码可能与使用它的其他程序（如 lynx(1)）不兼容。*注意：*这不用于交互式会话，仅用于命令行获取。

**`no_proxy`** 以空格或逗号分隔的主机（或域）列表，对这些主机不使用代理。每个条目可带有可选的尾部 ":port"，将匹配限制为到该端口的连接。

## 扩展被动模式与防火墙

某些防火墙配置不允许 `ftp` 使用扩展被动模式。如果发现即使是简单的 `ls` 在打印如下消息后也似乎挂起：

```sh
229 Entering Extended Passive Mode (|||58551|)
```

则需要使用 `epsv4 off` 禁用扩展被动模式。有关如何自动执行此操作的示例，请参见上文"THE .netrc FILE"章节。

## 参见

getservbyname(3), editrc(5), services(5)

## 标准

`ftp` 尝试符合以下标准：

**`RFC0959`** *File Transfer Protocol*

**`RFC1123`** *Requirements for Internet Hosts - Application and Support*

**`RFC1635`** *How to Use Anonymous FTP*

**`RFC2389`** *Feature negotiation mechanism for the File Transfer Protocol*

**`RFC2428`** *FTP Extensions for IPv6 and NATs*

**`RFC2616`** *Hypertext Transfer Protocol -- HTTP/1.1*

**`RFC2822`** *Internet Message Format*

**`RFC3659`** *Extensions to FTP*

**`RFC3986`** *Uniform Resource Identifier (URI)*

## 历史

`ftp` 命令首次出现于 4.2BSD。

命令行编辑、上下文敏感的命令和文件补全、动态进度条、自动获取文件和 URL、修改时间保留、传输速率限制、可配置命令行提示符以及对标准 BSD `ftp` 的其他增强等功能，由 Luke Mewburn <lukem@NetBSD.org> 在 NetBSD 1.3 及后续版本中实现。

IPv6 支持由 WIDE/KAME 项目添加（但可能不在此程序的所有非 NetBSD 版本中存在，取决于操作系统是否以类似 KAME 的方式支持 IPv6）。

## 缺陷

许多命令的正确执行取决于远程服务器的正确行为。

4.2BSD ascii 模式传输代码中对回车符处理的错误已被修正。此修正可能导致使用 ascii 类型与 4.2BSD 服务器之间进行二进制文件传输时出现错误。通过使用二进制 image 类型可避免此问题。

`ftp` 假定所有 IPv4 映射地址（形如 `::ffff:10.1.1.1` 的 IPv6 地址）都指示可由 `AF_INET` 套接字处理的 IPv4 目标。然而，在某些 IPv6 网络配置中，此假设不成立。在这种环境中，必须将 IPv4 映射地址直接传递给 `AF_INET6` 套接字。例如，如果你的站点使用 SIIT 转换器进行 IPv6 到 IPv4 的转换，`ftp` 将无法支持你的配置。
