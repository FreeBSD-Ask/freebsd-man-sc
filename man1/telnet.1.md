  TELNET(1)  

TELNET(1)

FreeBSD General Commands Manual

TELNET(1)

[名称](#__u540D___u79F0_)
=======================

`telnet` —

TELNET 协议的用户界面

[概要](#__u6982___u8981_)
=======================

`telnet` \[`-468EFKLNacdfruxy`\] \[`-B` baudrate\] \[`-S` tos\] \[`-X` authtype\] \[`-e` escapechar\] \[`-k` realm\] \[`-l` user\] \[`-n` tracefile\] \[`-s` src\_addr\] \[`-P` policy\] \[host \[port\]\]

[描述](#__u63CF___u8FF0_)
=======================

`telnet` 命令用于使用 TELNET 协议与另一台主机通信。 如果在没有 host 参数的情况下调用 `telnet` ，它将进入命令模式，由其提示符 (“`telnet>`”) 指示。 在这种模式下，它接受并执行下面列出的命令。 如果使用参数调用它，它会使用这些参数执行 `open` 命令。

选项：

[`-4`](#4)

强制 `telnet` 仅使用 IPv4 地址。

[`-6`](#6)

强制 `telnet` 仅使用 IPv6 地址。

[`-8`](#8)

指定 8 位数据路径。 这会导致尝试在输入和输出上协商 `TELNET BINARY` 选项。

[`-B`](#B) baudrate

将波特率设置为 baudrate 。

[`-E`](#E)

阻止任何字符被识别为转义字符。

[`-F`](#F)

如果正在使用 Kerberos V5 身份验证，则 `-F` 选项允许将本地凭据转发到远程系统，包括已转发到本地环境的任何凭据。

[`-K`](#K)

指定不自动登录到远程系统。

[`-L`](#L)

指定输出上的 8 位数据路径。 这会导致在输出时协商 `BINARY` 选项。

[`-N`](#N)

当目标主机作为 IP 地址给出时，防止 IP 地址进行名称查找。

[`-S`](#S) tos

将 telnet 连接的 IP 服务类型 (TOS) 选项设置为值 tos, 该值可以是数字 TOS 值，或者在支持它的系统上，可以是 /etc/iptos 文件中的符号 TOS 名称。

[`-X`](#X) atype

禁用 atype 类型的身份验证。

[`-a`](#a)

尝试自动登录。 现在这是默认设置，因此忽略此选项。 目前，如果远程系统支持，这将通过 `ENVIRON` 选项的 `USER` 变量发送用户名。 如果与当前用户 ID 一致，则使用 getlogin(2) 返回的当前用户的名称，否则为与用户 ID 关联的名称。

[`-c`](#c)

禁用读取用户的 .telnetrc 文件。 （请参阅此手册页上的 `toggle skiprc` 命令。）

[`-d`](#d)

将 `debug` 切换的初始值设置为 `TRUE` 。

[`-e`](#e) escapechar

将初始 `telnet` 转义字符设置为 escapechar 。 如果省略了 escapechar ，则没有转义字符。

[`-f`](#f)

如果正在使用 Kerberos V5 身份验证，则 `-f` 选项允许将本地凭据转发到远程系统。

[`-k`](#k) realm

如果使用 Kerberos 身份验证，则 `-k` 选项请求 `telnet` 获取远程主机在领域 realm 而不是远程主机领域的票证，由 krb\_realmofhost(3) 确定。

[`-l`](#l) user

当连接到远程系统时，如果远程系统理解 `ENVIRON` 选项，那么 user 将作为变量 `USER` 的值被发送到远程系统。 此选项意味着 `-a` 选项。 此选项也可以与 `open` 命令一起使用。

[`-n`](#n) tracefile

打开用于记录跟踪信息的 tracefile 。 请参阅下面的 `set tracefile` 命令。

[`-P`](#P) policy

对连接使用 policy 策略规范字符串策略。 有关详细信息，请参阅 ipsec\_set\_policy(3) 。

[`-r`](#r)

指定类似于 rlogin(1) 的用户界面。 在此模式下，转义字符设置为波浪号 (~) 字符，除非通过 `-e` 选项修改。

[`-s`](#s) src\_addr

将 `telnet` 连接的源IP地址设置为 src\_addr, 可以是IP地址，也可以是主机名。

[`-u`](#u)

强制 `telnet` 仅使用 `AF_UNIX` 地址（例如， UNIX 域套接字，通过文件路径访问）。

[`-x`](#x)

如果可能，打开数据流的加密。 现在这是默认设置，因此忽略此选项。

[`-y`](#y)

抑制数据流的加密。

host

表示远程主机的正式名称、别名或 Internet 地址。 如果 host 以 ‘`/`’ 开头，则 `telnet` 建立到相应命名套接字的连接。

port

表示端口号（应用程序的地址）。 如果未指定数字，则使用默认 `telnet` 端口。

在 rlogin 模式下，一行 ~. 与远程主机断开连接；~ 是 `telnet` 转义字符。 同样， ~^Z 行暂停 `telnet` 会话。 ~^\] 行转义到正常的 `telnet` 转义提示。

打开连接后， `telnet` 将尝试启用 `TELNET LINEMODE` 选项。 如果失败，则 `telnet` 将恢复为两种输入模式之一： “一次一个字符” 或 “逐行旧” ，具体取决于远程系统支持的内容。

当启用 `LINEMODE` 时，字符处理在本地系统上完成，在远程系统的控制下。 当输入编辑或字符回显被禁用时，远程系统将转发该信息。 远程系统还会将更改中继到远程系统上发生的任何特殊字符，以便它们可以在本地系统上生效。

在 “一次一个字符” 模式下，大多数输入的文本会立即发送到远程主机进行处理。

在 “逐行旧” 模式下，所有文本都在本地回显，并且（通常）只有完成的行被发送到远程主机。 “本地回显字符” (最初是 “^E”) 可用于关闭和打开本地回显（这主要用于输入密码而不回显密码）。

如果启用了 `LINEMODE` 选项，或者如果 `localchars` 切换为 `TRUE` (the default for “逐行旧”的默认值；见下文), 用户的 `quit 、` `intr` 和 `flush` 字符将在本地捕获，并作为 TELNET 协议序列发送到远方。 如果 `LINEMODE` 曾经被启用，那么用户的 `susp` 和 `eof` 也作为 TELNET 协议序列发送，而 `quit` 作为 `TELNET ABORT` 而不是 `BREAK` 发送。 有一些选项（请参阅下面的 `toggle` `autoflush` 和 `toggle` `autosynch` ）导致此操作将后续输出刷新到终端（直到远程主机确认 TELNET 序列）并刷新先前的终端输入（在 `quit` 和 `intr` 的情况下）。

当连接到远程主机时，可以通过键入 `telnet` “转义字符” (最初是 “^\]”) 进入 `telnet` 命令模式。在命令模式下，可以使用正常的终端编辑约定。

以下 `telnet` 命令可用。 每个命令只需要输入足以唯一标识它的内容（对于 `mode`, `set`, `toggle`, `unset`, `slc`, `environ` 和 `display` 命令的参数也是如此）。

[`auth`](#auth) argument ...

auth 命令处理通过 `TELNET AUTHENTICATE` 选项发送的信息。 `auth` 命令的有效参数是：

[`disable`](#disable) type

禁用指定类型的身份验证。 要获取可用类型的列表，请使用 `auth disable ?` 命令。

[`enable`](#enable) type

启用指定类型的身份验证。 要获取可用类型的列表，请使用 `auth enable ?`-
命令。

[`status`](#status)

列出各种身份验证的当前状态。

[`close`](#close)

关闭 TELNET 会话并返回命令模式。

[`display`](#display) argument ...

显示全部或部分 `set` 和 `toggle` 值（见下文）。

[`encrypt`](#encrypt) argument ...

encrypt 命令处理通过 `TELNET ENCRYPT` 选项发送的信息。

`encrypt` 命令的有效参数是：

[`disable`](#disable_2) type \[`input` | `output`\]

禁用指定类型的加密。 如果省略输入和输出，则输入和输出都被禁用。 要获取可用类型的列表，请使 `encrypt disable ?` 命令。

[`enable`](#enable_2) type \[`input` | `output`\]

启用指定类型的加密。 如果省略输入和输出，则输入和输出都启用。 要获取可用类型的列表，请使用 `encrypt enable ?`-
命令。

[`input`](#input)

这与 `encrypt start input` 命令相同。

[`-input`](#-input)

这与 `encrypt stop input` 命令相同。

[`output`](#output)

这与 `encrypt start output` 命令相同。

[`-output`](#-output)

这与 `encrypt stop output` 命令相同。

[`start`](#start) \[`input` | `output`\]

尝试开始加密。 如果 `input` 和 `output`, 则输入和输出都启用。 要获取可用类型的列表，请使用 `encrypt enable ?` 命令。

[`status`](#status_2)

列出加密的当前状态。

[`stop`](#stop) \[`input` | `output`\]

停止加密。 如果省略输入和输出，则输入和输出都加密。

[`type`](#type) type

设置用于以后的 `encrypt start` 或 `encrypt stop` 命令的默认加密类型。

[`environ`](#environ) arguments ...

[`environ`](#environ_2) 命令用于操作可能通过 `TELNET ENVIRON` 选项发送的变量。 初始变量集取自用户环境，默认情况下仅导出 `DISPLAY` 和 `PRINTER` 变量。 如果使用 `-a` 或 `-l` 选项，也会导出 `USER` 变量。

`environ` 命令的有效参数是：

[`define`](#define) variable value

将变量 variable 定义为具有 value 的值。 此命令定义的任何变量都会自动导出。 该 value 可以用单引号或双引号括起来，以便可以包含制表符和空格。

[`undefine`](#undefine) variable

从环境变量列表中删除 variable 。

[`export`](#export) variable

标记要导出到远程端的变量 variable 。

[`unexport`](#unexport) variable

除非远程端明确要求，否则将变量 variable 标记为不导出。

[`list`](#list)

列出当前的环境变量集。 标有 `*` 的变量将自动发送，其他变量只有在明确请求时才会发送。

[`?`](#?_&)

打印出 `environ` 命令的帮助信息。

[`logout`](#logout)

将 `TELNET LOGOUT` 选项发送到远程端。 该命令类似于 `close` 命令；但是，如果远程端不支持 `LOGOUT`-
选项，则不会发生任何事情。 但是，如果远程端确实支持 `LOGOUT` 选项，则此命令应导致远程端关闭 TELNET 连接。 如果远程端也支持暂停用户会话以供以后重新连接的概念，则 logout 参数指示您应该立即终止会话。

[`mode`](#mode) type

Type 是几个选项之一，具体取决于 TELNET 会话的状态。 要求远程主机允许进入请求的模式。 如果远程主机能够进入该模式，则将进入请求的模式。

[`character`](#character)

禁用 `TELNET LINEMODE` 选项，或者，如果远程端不理解 `LINEMODE` 选项，则进入 “一次一个字符” 模式。

[`line`](#line)

启用 `TELNET LINEMODE` 选项，或者，如果远程端不理解 `LINEMODE` 选项，则尝试进入 “old-line-by-line” 模式。

[`isig`](#isig) (`-isig`)

尝试启用（禁用 `LINEMODE` 选项的 `TRAPSIG` 模式。这需要启用 `LINEMODE` 选项。

[`edit`](#edit) (`-edit`)

尝试启用（禁用） `LINEMODE` 选项的 `EDIT` 模式。这需要启用 `LINEMODE` 选项。

[`softtabs`](#softtabs) (`-softtabs`)

尝试启用（禁用） `LINEMODE` 选项的 `SOFT_TAB` 模式。 这需要启用 `LINEMODE` 选项。

[`litecho`](#litecho) (`-litecho`)

尝试启用（禁用） `LINEMODE` 选项的 `LIT_ECHO` 模式。 这需要启用 `LINEMODE` 选项。

[`?`](#?_&_2)

打印出 `mode` 命令的帮助信息。

[`open`](#open) \[`-l` user\] \[host\] \[\[`-/+`\]port\]

打开与指定主机的连接。 如果未指定端口号， `telnet` 将尝试在默认端口上联系 TELNET 服务器。 主机规范可以是主机名（请参阅 hosts(5) ）、以 “点表示法” 指定的 Internet 地址（请参阅 inet(3) ）或 IPv6 主机名或 IPv6 冒号十六进制地址。 `-l` 选项可用于指定要通过 `ENVIRON` 选项传递给远程系统的用户名。 连接到非标准端口时， `telnet` 忽略任何自动启动 TELNET 选项。 当端口号前面有一个减号时，初始选项协商完成。 但是，当端口号前面有一个加号时，任何选项协商和理解都被禁止，这使得 POP3/SMTP/NNTP/HTTP 类协议的 telnet 哑客户端使用包括 TELNET IAC 字符 (0xff) 的任何数据。 建立连接后，将打开用户主目录中的 .telnetrc 文件。 以 # 开头的行是注释行。空白行被忽略。 没有空格开始的行是机器条目的开始。 行中的第一件事是正在连接的机器的名称。 它可能是指定为参数 host 的主机名或数字地址，由 getaddrinfo(3) 确定的该字符串的规范名称，或表示所有主机的字符串 “`DEFAULT`” 。 该行的其余部分以及以空格开头的后续行被假定为 `telnet` 命令，并像手动输入到 `telnet` 命令提示符一样进行处理。

[`quit`](#quit)

关闭任何打开的 TELNET 会话并退出 `telnet` 。 文件结束（在命令模式下）也将关闭会话并退出。

[`send`](#send) arguments

向远程主机发送一个或多个特殊字符序列。 以下是可以指定的参数（一次可以指定多个参数）：

[`abort`](#abort)

发送 `TELNET ABORT` （中止进程）序列。

[`ao`](#ao)

发送 `TELNET AO` (Abort Output) 序列，这将导致远程系统将所有输出 _from_ 远程系统刷新 _to_ 用户的终端。

[`ayt`](#ayt)

发送远程系统可能会或可能不会选择响应的 `TELNET AYT` (Are You There) 序列。

[`brk`](#brk)

发送 `TELNET BRK` 序列，这可能对远程系统有意义。

[`ec`](#ec)

发送 `TELNET EC` (擦除字符) 序列，这将导致远程系统擦除最后输入的字符。

[`el`](#el)

发送 `TELNET EL` (擦除行) 序列，这将导致远程系统擦除当前正在输入的线路。

[`eof`](#eof)

发送 `TELNET EOF` (文件结束) 序列。

[`eor`](#eor)

发送 `TELNET EOR` (记录结束) 序列。

[`escape`](#escape)

发送当前 `telnet` 转义字符（最初是 “^”)。

[`ga`](#ga)

发送 `TELNET GA` (Go Ahead) 序列，这可能对远程系统没有意义。

[`getstatus`](#getstatus)

如果远端支持 `TELNET STATUS` 命令， `getstatus` 将发送子协商请求服务器发送其当前选项状态。

[`ip`](#ip)

发送 `TELNET IP` (中断进程) 序列，这将导致远程系统中止当前正在运行的进程。

[`nop`](#nop)

发送 `TELNET NOP` （无操作）序列。

[`susp`](#susp)

发送 `TELNET SUSP` (SUSPend 进程）序列。

[`synch`](#synch)

发送 `TELNET SYNCH` 序列。 此序列导致远程系统丢弃所有先前键入（但尚未读取）的输入。 该序列作为 TCP 紧急数据发送（如果远程系统是 4.2BSD 系统，则可能无法工作——如果无法工作，终端上可能会回显小写 “r” ）。

[`do`](#do) cmd

[`dont`](#dont) cmd

[`will`](#will) cmd

[`wont`](#wont) cmd

发送 `TELNET DO` cmd 序列。 Cmd 可以是 0 到 255 之间的十进制数，也可以是特定 `TELNET` 命令的符号名称。 Cmd 也可以是 `help` 或 `?` 打印帮助信息，包括已知符号名称的列表。

[`?`](#?_&_3)

打印 `send` 命令的帮助信息。

[`set`](#set) argument value

[`unset`](#unset) argument value

[`set`](#set_2) 命令会将许多 `telnet` 变量中的任何一个设置为特定值或 `TRUE` 。 特殊值 `off` 关闭与变量关联的功能，这相当于使用 `unset` 命令。 `unset` 命令将禁用或设置为 `FALSE` 任何指定的功能。 变量的值可以用 `display` 命令查询。 此处列出了可以设置或取消设置但不能切换的变量。 此外， `toggle` 命令的任何变量都可以使用 `set` 和 `unset` 命令显式设置或取消设置。

[`ayt`](#ayt_2)

如果 TELNET 处于 localchars 模式，或者启用了 `LINEMODE` ，并且键入了状态字符，则将 `TELNET AYT` 序列（参见前面的发送 `send ayt` ）发送到远程主机。 “Are You There” 字符的初始值是终端的状态字符。

[`echo`](#echo)

这是值（最初是 “^E” ），当处于 “逐行” 模式时，会在输入字符的本地回显（用于正常处理）和抑制输入字符的回显（例如，输入密码）之间切换）。

[`eof`](#eof_2)

如果 `telnet` 在 `LINEMODE` 或 “旧的逐行” 模式下运行，输入该字符作为一行的第一个字符将导致该字符被发送到远程系统。 eof 字符的初始值被视为终端的 `eof` 字符。

[`erase`](#erase)

如果 `telnet` 处于 `localchars` 模式（请参阅下面的 `toggle` `localchars` ）， **并且** 如果 `telnet` 以 “一次一个字符” 模式运行，则当输入此字符时，将向远程系统发送一个 `TELNET EC` 序列（请参阅上面的 `send` `ec` ） . 擦除字符的初始值被视为终端的 `erase` 字符。

[`escape`](#escape_2)

这是 `telnet` 转义字符（最初是 “^\[” ），它会导致进入 `telnet` 命令模式（当连接到远程系统时）。

[`flushoutput`](#flushoutput)

如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars` ）并且输入了 `flushoutput` 字符，则将 `TELNET AO` AO 序列（参见上面的 `send` `ao` ）发送到远程主机。 刷新字符的初始值被视为终端的 `flush` 字符。

[`forw1`](#forw1)

[`forw2`](#forw2)

如果 `telnet` 在 `LINEMODE` 下运行，这些字符在键入时会导致部分行被转发到远程系统。 转发字符的初始值取自终端的 eol 和 eol2 字符。

[`interrupt`](#interrupt)

如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars` ）并且输入了 `interrupt` 字符，则将 `TELNET IP` 序列（参见上面的 `send` `ip` ）发送到远程主机。 中断字符的初始值被视为终端的 `intr` 字符。

[`kill`](#kill)

如果 `telnet` 处于 `localchars`-
模式（请参阅下面的 `toggle` `localchars` ）， `并且` 如果 `telnet` 以 “一次一个字符” 模式运行，则当键入此字符时，将向远程系统发送一个 `TELNET EL` 序列（请参阅上面的 `send` `el` 。 终止字符的初始值被视为终端的 `kill` 字符。

[`lnext`](#lnext)

如果 `telnet` 在 `LINEMODE` 或 “旧的逐行” 模式下运行，则该字符被视为终端的 `lnext` 字符。 lnext 字符的初始值被视为终端的 `lnext` 字符。

[`quit`](#quit_2)

如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars` ）并且输入了 `quit` 字符，则将 `TELNET BRK` 序列（参见上面的 `send` `brk` ）发送到远程主机。 退出字符的初始值被视为终端的 `quit` 字符。

[`reprint`](#reprint)

如果 `telnet` 在 `LINEMODE` 或 “旧的逐行” 模式下运行，则该字符被视为终端的 `reprint` 字符。 重印字符的初始值被取为终端 `reprint` 字符。

[`rlogin`](#rlogin)

这是 rlogin 转义字符。 如果设置，则忽略正常的 `telnet` 转义字符，除非它在行的开头有此字符。 这个字符，在一行的开头跟一个“.”。关闭连接；当后面跟着一个 ^Z 时，它会暂停 `telnet` 命令。 初始状态是禁用 `rlogin` 转义字符。

[`start`](#start_2)

如果启用了 `TELNET TOGGLE-FLOW-CONTROL` 选项，则该字符被视为终端的 `start` 字符。 起始字符的初始值被视为终端的 `start` 字符。

[`stop`](#stop_2)

如果启用了 `TELNET TOGGLE-FLOW-CONTROL` 选项，则该字符被视为终端的停止 `stop` 字符。 停止字符的初始值被视为终端的 `stop` 字符。

[`susp`](#susp_2)

如果 `telnet` 处于 `localchars` 模式，或者启用了 `LINEMODE` ，并且键入了 `suspend` 字符，则会将 `TELNET SUSP` 序列（参见上面的 `send` `susp` ）发送到远程主机。 挂起字符的初始值被视为终端的 `suspend` 字符。

[`tracefile`](#tracefile)

这是由 `netdata` 或 `option` 跟踪为 `TRUE` 导致的输出将被写入的文件。 如果设置为 “`-`” ，则跟踪信息将被写入标准输出（默认）。

[`worderase`](#worderase)

如果 `telnet` 在 `LINEMODE` 或 “旧的逐行” 模式下运行，则该字符被视为终端的 `worderase` 字符。 worderase 字符的初始值被视为终端的 `worderase` 字符。

[`?`](#?_&_4)

显示合法的 `set` (`unset`) 命令。

[`opie`](#opie) sequence challenge

[`opie`](#opie_2) 命令计算对 OPIE 质询的响应。

[`slc`](#slc) state

[`slc`](#slc_2) 命令（设置本地字符）用于在启用 `TELNET LINEMODE` 选项时设置或更改特殊字符的状态。 特殊字符是映射到 TELNET 命令序列（如 `ip` 或 `quit` ）或行编辑字符（如 `erase` 和 `kill` ）的字符。 默认情况下，导出本地特殊字符。

[`check`](#check)

验证当前特殊字符的当前设置。 请求远程端发送当前所有的特殊字符设置，如果与本地端有任何差异，本地端将切换到远程值。

[`export`](#export_2)

切换到特殊字符的本地默认值。 本地默认字符是启动 `telnet` 时本地终端的字符。

[`import`](#import)

切换到特殊字符的远程默认值。 远程默认字符是建立 TELNET 连接时远程系统的字符。

[`?`](#?_&_5)

打印出e `slc` 命令的帮助信息。

[`status`](#status_3)

显示 `telnet` 的当前状态。 这包括连接到的对等方，以及当前模式。

[`toggle`](#toggle) arguments ...

切换（在 `TRUE` 和 `FALSE` 之间）控制 `telnet` 如何响应事件的各种标志。 可以使用上面列出的 `set` 和 `unset` 命令将这些标志显式设置为 `TRUE` 或 `FALSE` 。 可以指定多个参数。 这些标志的状态可以用 `display` 命令询问。 有效的论点是：

[`authdebug`](#authdebug)

打开验证码的调试信息。

[`autoflush`](#autoflush)

如果 `autoflush` 和 `localchars` 都为 `TRUE` ，那么当 `ao` 或 `quit` 字符被识别（并转换为 TELNET 序列；详见上文 `set` ）时， `telnet` 拒绝在用户终端上显示任何数据，直到远程系统确认（通过 `TELNET TIMING MARK` 选项）它已经处理了那些 TELNET 序列。 如果终端用户没有执行“stty noflsh”，则此切换的初始值为 `TRUE` ，否则为 `FALSE` （参见 stty(1) ）。

[`autodecrypt`](#autodecrypt)

当协商 `TELNET ENCRYPT` 选项时，默认情况下，数据流的实际加密（解密）不会自动启动。 autoencrypt (autodecrypt) 命令指出应尽快启用输出（输入）流的加密。

[`autologin`](#autologin)

如果远程端支持 `TELNET AUTHENTICATION` 选项， `telnet` 会尝试使用它来执行自动身份验证。 如果不支持 `AUTHENTICATION` 选项，则用户的登录名将通过 `TELNET ENVIRON` 选项传播。 此命令与在 `open` 命令上指定 `-a` 选项相同。

[`autosynch`](#autosynch)

如果 `autosynch` 和 `localchars` 都为 `TRUE` ，那么当输入 `intr` 或 `quit` 字符时(请参阅上面的 `set` 以了解 `intr` 和 `quit` 字符的描述)，发送的结果 TELNET 序列后面跟着 `TELNET SYNCH` 序列。 此过程 `应` 导致远程系统开始丢弃所有先前键入的输入，直到两个 TELNET 序列都已被读取并执行。 此切换的初始值为 `FALSE` 。

[`binary`](#binary)

在输入和输出上启用或禁用 `TELNET BINARY` 选项。

[`inbinary`](#inbinary)

在输入上启用或禁用 `TELNET BINARY` 选项。

[`outbinary`](#outbinary)

在输出上启用或禁用 `TELNET BINARY` 选项。

[`crlf`](#crlf)

如果为 `TRUE` ，则回车将作为 `<CR><LF>` 发送。 如果这是 `FALSE` ，则回车将作为 `<CR><NUL>` 发送。 此切换的初始值为 `FALSE` 。

[`crmod`](#crmod)

切换回车模式。 启用此模式后，从远程主机接收到的大多数回车字符将被映射为回车后跟换行符。 此模式不影响用户输入的那些字符，只影响从远程主机接收到的那些字符。 这种模式不是很有用，除非远程主机只发送回车而不是换行。 此切换的初始值为 `FALSE` 。

[`debug`](#debug)

切换套接字级别调试（仅对 `super user` 有用）。 此切换的初始值为 `FALSE` 。

[`encdebug`](#encdebug)

打开加密代码的调试信息。

[`localchars`](#localchars)

如果为 `TRUE`, 则 `flush 、` `interrupt 、` `quit 、` `erase` 和 `kill` 字符（见上文 `set` ）在本地识别，并转换为（希望）适当的 TELNET 控制序列（分别为 `ao 、` `ip 、` `brk 、` `ec` 和 `el`; 见上面 `send` )。 此切换的初始值在 “逐行旧” 模式下 `TRUE` ，在 “一次一个字符” 模式下为 `FALSE` 。 启用 `LINEMODE` 选项时，将忽略 `localchars` 的值，并假定始终为 `TRUE` 。 如果 `LINEMODE` 曾经被启用，则以 `abort` 形式发送 `quit` ，并且以 `eof` 和 `susp` 形式发送 `eof` 和 `suspend` （参见上面的 `send` ）。

[`netdata`](#netdata)

切换所有网络数据的显示（以十六进制格式）。 此切换的初始值为 `FALSE` 。

[`options`](#options)

切换某些内部 `telnet` 协议处理的显示（与 TELNET 选项有关）。 此切换的初始值为 `FALSE` 。

[`prettydump`](#prettydump)

启用 `netdata` 切换后，如果启用了 `prettydump` ，则 `netdata` 命令的输出将被格式化为更易于用户阅读的格式。 输出中的每个字符之间都有空格，并且任何 `telnet` 转义序列的开头都以 '\*' 开头，以帮助定位它们。

[`skiprc`](#skiprc)

当 skiprc 切换为 `TRUE` 时， `telnet` 会在打开连接时跳过读取用户主目录中的 .telnetrc 文件。 此切换的初始值为 `FALSE` 。

[`termdata`](#termdata)

切换所有终端数据的显示（以十六进制格式）。 此切换的初始值为 `FALSE` 。

[`verbose_encrypt`](#verbose_encrypt)

当 `verbose_encrypt` 切换为 `TRUE` 时， `telnet` 会在每次启用或禁用加密时打印出一条消息。 此切换的初始值为 `FALSE` 。

[`?`](#?_&_6)

显示合法的 `toggle` 命令。

[`z`](#z)

挂起 `telnet` 。 此命令仅在用户使用 csh(1) 。

[`!`](#!) \[command\]

在本地系统的子 shell 中执行单个命令。 如果 command 被省略，则调用交互式子 shell。

[`?`](#?_&_7) \[command\]

得到帮助。 不带参数， `telnet` 打印帮助摘要。 如果指定了 command ， `telnet` 将仅打印该命令的帮助信息。

[环境](#__u73AF___u5883_)
=======================

`telnet` 至少使用 `HOME 、` `SHELL 、` `DISPLAY` 和 `TERM` 环境变量。 其他环境变量可以通过 `TELNET ENVIRON` 选项传播到另一端。

[文件](#__u6587___u4EF6_)
=======================

~/.telnetrc

用户自定义的 telnet 启动值

[参见](#__u53C2___u89C1_)
=======================

rlogin(1) 、 rsh(1) 、 hosts(5) 、 nologin(5) 、 telnetd(8)

[历史](#__u5386___u53F2_)
=======================

`telnet` 命令出现在 4.2BSD 中。

WIDE/KAME 项目添加了 IPv6 支持。

[说明](#__u8BF4___u660E_)
=======================

在某些远程系统上，在 “旧的逐行” 模式下必须手动关闭回显。

在 “旧的逐行” 模式或 `LINEMODE` 中，终端的 `eof` 字符仅在它是一行的第一个字符时才被识别（并发送到远程系统）。

August 7, 2020

FreeBSD 13.1-RELEASE