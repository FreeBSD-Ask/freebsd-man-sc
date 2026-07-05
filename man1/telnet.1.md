# telnet.1

`telnet` — TELNET 协议的用户界面

## 名称

`telnet` TELNET 协议

## 概要

`telnet [-468EFKLNQacdfruxy] [-B baudrate] [-S tos] [-X authtype] [-e escapechar] [-k realm] [-l user] [-n tracefile] [-s src_addr] [-P policy] [host [port]]`

## 描述

`telnet` 命令用于使用 TELNET 协议与另一台主机通信。如果在没有 `host` 参数的情况下调用 `telnet`，它会进入命令模式，由其提示符（“`telnet>`”）指示。在此模式下，它接受并执行下面列出的命令。如果带参数调用，它会使用这些参数执行 `open` 命令。

选项：

**`-4`** 强制 `telnet` 仅使用 IPv4 地址。

**`-6`** 强制 `telnet` 仅使用 IPv6 地址。

**`-8`** 指定 8 位数据路径。这会导致在输入和输出上尝试协商 `TELNET BINARY` 选项。

**`-B`** `baudrate` 将波特率设置为 `baudrate`。

**`-E`** 阻止任何字符被识别为转义字符。

**`-F`** 如果使用 Kerberos V5 认证，`-F` 选项允许将本地凭证转发到远程系统，包括已经转发到本地环境的任何凭证。

**`-K`** 指定不自动登录到远程系统。

**`-L`** 指定输出上的 8 位数据路径。这会导致在输出上协商 `BINARY` 选项。

**`-N`** 当目标主机以 IP 地址形式给出时，阻止 IP 地址到名称的查找。

**`-Q`** 安静模式。这会抑制 `telnet` 在连接或断开连接时通常会输出的消息。

**`-S`** `tos` 将 telnet 连接的 IP 服务类型（TOS）选项设置为值 `tos`，可以是数字 TOS 值，或在支持它的系统上，是 **/etc/iptos** 文件中找到的符号 TOS 名称。

**`-X`** `atype` 禁用 `atype` 类型的认证。

**`-a`** 尝试自动登录。这现在是默认行为，因此此选项被忽略。目前，如果远程系统支持，它会通过 `ENVIRON` 选项的 `USER` 变量发送用户名。使用的名称是 getlogin(2) 返回的当前用户名（如果与当前用户 ID 一致），否则是与用户 ID 关联的名称。

**`-c`** 禁用读取用户的 `.telnetrc` 文件。（参见本手册页中的 `toggle skiprc` 命令。）

**`-d`** 将 `debug` 切换的初始值设置为 `TRUE`。

**`-e`** `escapechar` 将初始 `telnet` 转义字符设置为 `escapechar`。如果省略 `escapechar`，则不会有转义字符。

**`-f`** 如果使用 Kerberos V5 认证，`-f` 选项允许将本地凭证转发到远程系统。

**`-k`** `realm` 如果使用 Kerberos 认证，`-k` 选项请求 `telnet` 从远程主机获取 realm `realm` 的票据，而非远程主机的 realm（由 krb_realmofhost(3) 确定）。

**`-l`** `user` 连接到远程系统时，如果远程系统理解 `ENVIRON` 选项，`user` 将作为变量 `USER` 的值发送到远程系统。此选项隐含 `-a` 选项。此选项也可与 `open` 命令一起使用。

**`-n`** `tracefile` 打开 `tracefile` 以记录跟踪信息。参见下面的 `set tracefile` 命令。

**`-P`** `policy` 为连接使用 IPsec 策略规范字符串 `policy`。详情参见 ipsec_set_policy(3)。

**`-r`** 指定类似于 rlogin(1) 的用户界面。在此模式下，转义字符设置为波浪号（~），除非通过 `-e` 选项修改。

**`-s`** `src_addr` 将 `telnet` 连接的源 IP 地址设置为 `src_addr`，可以是 IP 地址或主机名。

**`-u`** 强制 `telnet` 仅使用 `AF_UNIX` 地址（例如，通过文件路径访问的 UNIX 域套接字）。

**`-x`** 如果可能，打开数据流加密。这现在是默认行为，因此此选项被忽略。

**`-y`** 抑制数据流加密。

**`host`** 指示远程主机的正式名称、别名或 Internet 地址。如果 `host` 以 `/` 开头，`telnet` 会建立到对应命名套接字的连接。

**`port`** 指示端口号（应用程序地址）。如果未指定数字，则使用默认的 `telnet` 端口。

在 rlogin 模式下，~. 形式的行会断开与远程主机的连接；~ 是 `telnet` 转义字符。类似地，行 ~^Z 暂停 `telnet` 会话。行 ~^] 转义到正常的 `telnet` 转义提示符。

连接打开后，`telnet` 会尝试启用 `TELNET LINEMODE` 选项。如果失败，`telnet` 会恢复到两种输入模式之一：“逐字符”或“旧逐行”模式，具体取决于远程系统支持哪种。

启用 `LINEMODE` 后，字符处理在本地系统上完成，由远程系统控制。当需要禁用输入编辑或字符回显时，远程系统会转发该信息。远程系统还会转发其上发生的任何特殊字符的更改，以便它们能在本地系统上生效。

在“逐字符”模式下，输入的大多数文本会立即发送到远程主机进行处理。

在“旧逐行”模式下，所有文本在本地回显，（通常）仅完整的行会发送到远程主机。“本地回显字符”（初始为 `^E`）可用于打开和关闭本地回显（这主要用于输入密码时不回显密码）。

如果启用了 `LINEMODE` 选项，或 `localchars` 切换为 `TRUE`（“旧逐行”模式的默认值；参见下文），用户的 `quit`、`intr` 和 `flush` 字符会在本地捕获，并作为 TELNET 协议序列发送到远程端。如果曾经启用过 `LINEMODE`，则用户的 `susp` 和 `eof` 也会作为 TELNET 协议序列发送，`quit` 会作为 `TELNET ABORT` 而非 `BREAK` 发送。有些选项（参见下面的 `toggle` `autoflush` 和 `toggle` `autosynch`）会导致此操作刷新后续到终端的输出（直到远程主机确认 TELNET 序列）并刷新先前的终端输入（在 `quit` 和 `intr` 的情况下）。

连接到远程主机时，可以通过键入 `telnet` “转义字符”（初始为 `^]`）进入 `telnet` 命令模式。在命令模式下，可使用正常的终端编辑约定。

以下 `telnet` 命令可用。只需键入每个命令中足以唯一识别它的部分即可（这对于 `mode`、`set`、`toggle`、`unset`、`slc`、`environ` 和 `display` 命令的参数同样适用）。

**`auth`** `argument ...` auth 命令操作通过 `TELNET AUTHENTICATE` 选项发送的信息。`auth` 命令的有效参数为：

**`disable`** `type` 禁用指定类型的认证。要获取可用类型列表，使用 `auth disable ?` 命令。

**`enable`** `type` 启用指定类型的认证。要获取可用类型列表，使用 `auth enable ?` 命令。

**`status`** 列出各种认证类型的当前状态。

**`close`** 关闭 TELNET 会话并返回命令模式。

**`display`** `argument ...` 显示所有或部分 `set` 和 `toggle` 值（参见下文）。

**`encrypt`** `argument ...` encrypt 命令操作通过 `TELNET ENCRYPT` 选项发送的信息。`encrypt` 命令的有效参数为：

**`disable`** `type` [`input | output`] 禁用指定类型的加密。如果省略 input 和 output，两者都会被禁用。要获取可用类型列表，使用 `encrypt disable ?` 命令。

**`enable`** `type` [`input | output`] 启用指定类型的加密。如果省略 input 和 output，两者都会被启用。要获取可用类型列表，使用 `encrypt enable ?` 命令。

**`input`** 这与 `encrypt start input` 命令相同。

**`-input`** 这与 `encrypt stop input` 命令相同。

**`output`** 这与 `encrypt start output` 命令相同。

**`-output`** 这与 `encrypt stop output` 命令相同。

**`start`** [`input | output`] 尝试启动加密。如果省略 `input` 和 `output`，两者都会被启用。要获取可用类型列表，使用 `encrypt enable ?` 命令。

**`status`** 列出加密的当前状态。

**`stop`** [`input | output`] 停止加密。如果省略 input 和 output，加密在输入和输出上都开启。

**`type`** `type` 设置用于后续 `encrypt start` 或 `encrypt stop` 命令的默认加密类型。

**`environ`** `arguments ...` `environ` 命令用于操作可通过 `TELNET ENVIRON` 选项发送的变量。初始变量集取自用户环境，默认仅导出 `DISPLAY` 和 `PRINTER` 变量。如果使用 `-a` 或 `-l` 选项，`USER` 变量也会被导出。`environ` 命令的有效参数为：

**`define`** `variable value` 将变量 `variable` 定义为值 `value`。此命令定义的任何变量都会自动导出。`value` 可用单引号或双引号括起，以包含制表符和空格。

**`undefine`** `variable` 从环境变量列表中删除 `variable`。

**`export`** `variable` 标记变量 `variable` 以导出到远程端。

**`unexport`** `variable` 标记变量 `variable` 不导出，除非远程端明确请求。

**`list`** 列出当前的环境变量集。标记有 `*` 的变量会自动发送，其他变量仅在明确请求时发送。

**`?`** 打印 `environ` 命令的帮助信息。

**`logout`** 向远程端发送 `TELNET LOGOUT` 选项。此命令类似于 `close` 命令；但是，如果远程端不支持 `LOGOUT` 选项，则什么也不会发生。如果远程端支持 `LOGOUT` 选项，此命令应导致远程端关闭 TELNET 连接。如果远程端还支持暂停用户会话以便稍后重新连接的概念，logout 参数表示你应立即终止会话。

**`mode`** `type` `Type` 是多个选项之一，取决于 TELNET 会话的状态。会向远程主机请求进入所请求模式的权限。如果远程主机能够进入该模式，则进入所请求的模式。

**`character`** 禁用 `TELNET LINEMODE` 选项，或如果远程端不理解 `LINEMODE` 选项，则进入“逐字符”模式。

**`line`** 启用 `TELNET LINEMODE` 选项，或如果远程端不理解 `LINEMODE` 选项，则尝试进入“旧逐行”模式。

**`isig`**（`-isig`）尝试启用（禁用）`LINEMODE` 选项的 `TRAPSIG` 模式。这要求 `LINEMODE` 选项已启用。

**`edit`**（`-edit`）尝试启用（禁用）`LINEMODE` 选项的 `EDIT` 模式。这要求 `LINEMODE` 选项已启用。

**`softtabs`**（`-softtabs`）尝试启用（禁用）`LINEMODE` 选项的 `SOFT_TAB` 模式。这要求 `LINEMODE` 选项已启用。

**`litecho`**（`-litecho`）尝试启用（禁用）`LINEMODE` 选项的 `LIT_ECHO` 模式。这要求 `LINEMODE` 选项已启用。

**`?`** 打印 `mode` 命令的帮助信息。

**`open`** [`-l` `user`] [`host`] [[`-/+`]`port`] 打开到指定主机的连接。如果未指定端口号，`telnet` 会尝试在默认端口联系 TELNET 服务器。主机规范可以是主机名（参见 [hosts(5)](../man5/hosts.5.md)）、以“点分表示法”指定的 Internet 地址（参见 inet(3)），或 IPv6 主机名或 IPv6 冒号十六进制地址。`-l` 选项可用于指定通过 `ENVIRON` 选项传递给远程系统的用户名。连接到非标准端口时，`telnet` 会省略任何 TELNET 选项的自动发起。当端口号前有减号时，会进行初始选项协商。但是，当端口号前有加号时，禁止任何选项协商和理解，使 telnet 成为 POP3/SMTP/NNTP/HTTP 类协议的笨客户端，包括 TELNET IAC 字符（0xff）在内的任何数据。建立连接后，会打开用户主目录中的 `.telnetrc` 文件。以 # 开头的行是注释行。空行被忽略。不以空白开头的行是机器条目的开始。该行上的第一个内容是正在连接的机器的名称。它可以是作为参数 `host` 指定的主机名或数字地址、由 getaddrinfo(3) 确定的该字符串的规范名称，或表示所有主机的字符串 “`DEFAULT`”。该行的其余部分以及以空白开头的后续行被假定为 `telnet` 命令，并像手动键入到 `telnet` 命令提示符一样处理。

**`quit`** 关闭任何打开的 TELNET 会话并退出 `telnet`。（命令模式下的）文件结束符也会关闭会话并退出。

**`send`** `arguments` 向远程主机发送一个或多个特殊字符序列。以下是可以指定的参数（一次可以指定多个参数）：

**`abort`** 发送 `TELNET ABORT`（中止进程）序列。

**`ao`** 发送 `TELNET AO`（中止输出）序列，这应导致远程系统刷新从远程系统到用户终端的所有输出。

**`ayt`** 发送 `TELNET AYT`（你在吗）序列，远程系统可能选择响应也可能不响应。

**`brk`** 发送 `TELNET BRK`（中断）序列，这可能与远程系统有关。

**`ec`** 发送 `TELNET EC`（擦除字符）序列，这应导致远程系统擦除最后输入的字符。

**`el`** 发送 `TELNET EL`（擦除行）序列，这应导致远程系统擦除当前正在输入的行。

**`eof`** 发送 `TELNET EOF`（文件结束）序列。

**`eor`** 发送 `TELNET EOR`（记录结束）序列。

**`escape`** 发送当前的 `telnet` 转义字符（初始为 `^]`）。

**`ga`** 发送 `TELNET GA`（继续）序列，这可能与远程系统无关。

**`getstatus`** 如果远程端支持 `TELNET STATUS` 命令，`getstatus` 会发送子协商以请求服务器发送其当前选项状态。

**`ip`** 发送 `TELNET IP`（中断进程）序列，这应导致远程系统中止当前运行的进程。

**`nop`** 发送 `TELNET NOP`（无操作）序列。

**`susp`** 发送 `TELNET SUSP`（挂起进程）序列。

**`synch`** 发送 `TELNET SYNCH` 序列。此序列导致远程系统丢弃所有先前键入（但尚未读取）的输入。此序列作为 TCP 紧急数据发送（如果远程系统是 4.2BSD 系统，可能不起作用——如果不起作用，终端上可能会回显小写字母 “r”）。

**`do`** `cmd`

**`dont`** `cmd`

**`will`** `cmd`

**`wont`** `cmd` 发送 `TELNET DO` `cmd` 序列。`Cmd` 可以是 0 到 255 之间的十进制数字，或特定 `TELNET` 命令的符号名称。`Cmd` 也可以是 `help` 或 `?` 以打印帮助信息，包括已知符号名称列表。

**`?`** 打印 `send` 命令的帮助信息。

**`set`** `argument value`

**`unset`** `argument value` `set` 命令将多个 `telnet` 变量之一设置为特定值或 `TRUE`。特殊值 `off` 关闭与变量关联的功能，这等效于使用 `unset` 命令。`unset` 命令会禁用或将任何指定功能设置为 `FALSE`。变量的值可通过 `display` 命令查询。此处列出可设置或取消设置但不可切换的变量。此外，`toggle` 命令的任何变量都可使用 `set` 和 `unset` 命令显式设置或取消设置。

**`ayt`** 如果 TELNET 处于 localchars 模式，或启用了 `LINEMODE`，并且键入了状态字符，则会向远程主机发送 `TELNET AYT` 序列（参见前面的 `send ayt`）。“你在吗”字符的初始值是终端的状态字符。

**`echo`** 这是（初始为 `^E`）在“逐行”模式下切换是否对输入字符进行本地回显（用于正常处理）和抑制输入字符回显（用于输入密码）的值。

**`eof`** 如果 `telnet` 在 `LINEMODE` 或“旧逐行”模式下运行，将此字符作为行首第一个字符输入会导致此字符被发送到远程系统。eof 字符的初始值取自终端的 `eof` 字符。

**`erase`** 如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars`），**且** `telnet` 在“逐字符”模式下运行，则当键入此字符时，会向远程系统发送 `TELNET EC` 序列（参见上面的 `send` `ec`）。erase 字符的初始值取自终端的 `erase` 字符。

**`escape`** 这是 `telnet` 转义字符（初始为 `^[`），导致进入 `telnet` 命令模式（当连接到远程系统时）。

**`flushoutput`** 如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars`）并且键入了 `flushoutput` 字符，会向远程主机发送 `TELNET AO` 序列（参见上面的 `send` `ao`）。flush 字符的初始值取自终端的 `flush` 字符。

**`forw1`**

**`forw2`** 如果 `telnet` 在 `LINEMODE` 下运行，这些是当键入时导致部分行被转发到远程系统的字符。转发字符的初始值取自终端的 eol 和 eol2 字符。

**`interrupt`** 如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars`）并且键入了 `interrupt` 字符，会向远程主机发送 `TELNET IP` 序列（参见上面的 `send` `ip`）。interrupt 字符的初始值取自终端的 `intr` 字符。

**`kill`** 如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars`），`and` 如果 `telnet` 在“逐字符”模式下运行，则当键入此字符时，会向远程系统发送 `TELNET EL` 序列（参见上面的 `send` `el`）。kill 字符的初始值取自终端的 `kill` 字符。

**`lnext`** 如果 `telnet` 在 `LINEMODE` 或“旧逐行”模式下运行，则此字符取自终端的 `lnext` 字符。lnext 字符的初始值取自终端的 `lnext` 字符。

**`quit`** 如果 `telnet` 处于 `localchars` 模式（参见下面的 `toggle` `localchars`）并且键入了 `quit` 字符，会向远程主机发送 `TELNET BRK` 序列（参见上面的 `send` `brk`）。quit 字符的初始值取自终端的 `quit` 字符。

**`reprint`** 如果 `telnet` 在 `LINEMODE` 或“旧逐行”模式下运行，则此字符取自终端的 `reprint` 字符。reprint 字符的初始值取自终端的 `reprint` 字符。

**`rlogin`** 这是 rlogin 转义字符。如果设置，正常的 `telnet` 转义字符会被忽略，除非在行首此前有此字符。此字符在行首后跟 “.” 会关闭连接；后跟 ^Z 会暂停 `telnet` 命令。初始状态是禁用 `rlogin` 转义字符。

**`start`** 如果启用了 `TELNET TOGGLE-FLOW-CONTROL` 选项，则此字符取自终端的 `start` 字符。start 字符的初始值取自终端的 `start` 字符。

**`stop`** 如果启用了 `TELNET TOGGLE-FLOW-CONTROL` 选项，则此字符取自终端的 `stop` 字符。stop 字符的初始值取自终端的 `stop` 字符。

**`susp`** 如果 `rlogin` 处于 `localchars` 模式，或启用了 `LINEMODE`，并且键入了 `suspend` 字符，会向远程主机发送 `TELNET SUSP` 序列（参见上面的 `send` `susp`）。suspend 字符的初始值取自终端的 `suspend` 字符。

**`tracefile`** 这是由 `netdata` 或 `option` 跟踪为 `TRUE` 时所导致的输出写入的文件。如果设置为 “`-`”，则跟踪信息会写入标准输出（默认）。

**`worderase`** 如果 `rlogin` 在 `LINEMODE` 或“旧逐行”模式下运行，则此字符取自终端的 `worderase` 字符。worderase 字符的初始值取自终端的 `worderase` 字符。

**`?`** 显示合法的 `set`（`unset`）命令。

**`slc`** `state` `slc` 命令（设置本地字符）用于在启用 `TELNET LINEMODE` 选项时设置或更改特殊字符的状态。特殊字符是映射到 TELNET 命令序列（如 `ip` 或 `quit`）或行编辑字符（如 `erase` 和 `kill`）的字符。默认情况下，本地特殊字符会被导出。

**`check`** 验证当前特殊字符的当前设置。请求远程端发送所有当前特殊字符设置，如果与本地端有任何差异，本地端会切换到远程值。

**`export`** 切换到特殊字符的本地默认值。本地默认字符是 `rlogin` 启动时本地终端的字符。

**`import`** 切换到特殊字符的远程默认值。远程默认字符是建立 TELNET 连接时远程系统的字符。

**`?`** 打印 `slc` 命令的帮助信息。

**`status`** 显示 `telnet` 的当前状态。这包括连接的对端以及当前模式。

**`toggle`** `arguments ...` 切换（在 `TRUE` 和 `FALSE` 之间）控制 `telnet` 如何响应事件的各种标志。这些标志可使用上面列出的 `set` 和 `unset` 命令显式设置为 `TRUE` 或 `FALSE`。可指定多个参数。这些标志的状态可通过 `display` 命令查询。有效参数为：

**`authdebug`** 打开认证代码的调试信息。

**`autoflush`** 如果 `autoflush` 和 `localchars` 都为 `TRUE`，则当识别 `ao` 或 `quit` 字符（并转换为 TELNET 序列；详情参见上面的 `set`）时，`telnet` 拒绝在远程系统确认（通过 `TELNET TIMING MARK` 选项）已处理这些 TELNET 序列之前在用户终端上显示任何数据。如果终端用户未执行 “stty noflsh”，此切换的初始值为 `TRUE`，否则为 `FALSE`（参见 stty(1)）。

**`autodecrypt`** 协商 `TELNET ENCRYPT` 选项时，默认情况下数据流的实际加密（解密）不会自动开始。autoencrypt（autodecrypt）命令表示应尽快启用输出（输入）流的加密。

**`autologin`** 如果远程端支持 `TELNET AUTHENTICATION` 选项，`telnet` 会尝试使用它进行自动认证。如果 `AUTHENTICATION` 选项不受支持，用户的登录名会通过 `TELNET ENVIRON` 选项传播。此命令与在 `open` 命令上指定 `-a` 选项相同。

**`autosynch`** 如果 `autosynch` 和 `localchars` 都为 `TRUE`，则当键入 `intr` 或 `quit` 字符（参见上面 `set` 中对 `intr` 和 `quit` 字符的描述）时，发送的 TELNET 序列后会跟 `TELNET SYNCH` 序列。此过程应导致远程系统开始丢弃所有先前键入的输入，直到两个 TELNET 序列都被读取并处理。此切换的初始值为 `FALSE`。

**`binary`** 在输入和输出上启用或禁用 `TELNET BINARY` 选项。

**`inbinary`** 在输入上启用或禁用 `TELNET BINARY` 选项。

**`outbinary`** 在输出上启用或禁用 `TELNET BINARY` 选项。

**`crlf`** 如果为 `TRUE`，则回车符会作为 `<CR><LF>` 发送。如果为 `FALSE`，则回车符会作为 `<CR><NUL>` 发送。此切换的初始值为 `FALSE`。

**`crmod`** 切换回车模式。启用此模式时，从远程主机接收到的大多数回车字符会被映射为回车后跟换行。此模式不影响用户键入的字符，仅影响从远程主机接收的字符。除非远程主机仅发送回车从不发送换行，否则此模式不太有用。此切换的初始值为 `FALSE`。

**`debug`** 切换套接字级调试（仅对超级用户有用）。此切换的初始值为 `FALSE`。

**`encdebug`** 打开加密代码的调试信息。

**`localchars`** 如果为 `TRUE`，则 `flush`、`interrupt`、`quit`、`erase` 和 `kill` 字符（参见上面的 `set`）在本地识别，并转换为（希望是）适当的 TELNET 控制序列（分别是 `ao`、`ip`、`brk`、`ec` 和 `el`；参见上面的 `send`）。此切换在“旧逐行”模式下的初始值为 `TRUE`，在“逐字符”模式下为 `FALSE`。启用 `LINEMODE` 选项时，`localchars` 的值会被忽略，并假定始终为 `TRUE`。如果曾经启用过 `LINEMODE`，则 `quit` 会作为 `abort` 发送，`eof` 和 `suspend` 会作为 `eof` 和 `susp` 发送（参见上面的 `send`）。

**`netdata`** 切换所有网络数据的显示（以十六进制格式）。此切换的初始值为 `FALSE`。

**`options`** 切换一些内部 `telnet` 协议处理的显示（与 TELNET 选项有关）。此切换的初始值为 `FALSE`。

**`prettydump`** 当 `netdata` 切换启用时，如果启用 `prettydump`，`netdata` 命令的输出会以更易读的格式排版。输出中每个字符之间会放置空格，任何 `telnet` 转义序列的开头前会有一个 '*' 以帮助定位。

**`skiprc`** 当 skiprc 切换为 `TRUE` 时，`telnet` 在打开连接时会跳过读取用户主目录中的 `.telnetrc` 文件。此切换的初始值为 `FALSE`。

**`termdata`** 切换所有终端数据的显示（以十六进制格式）。此切换的初始值为 `FALSE`。

**`verbose_encrypt`** 当 `verbose_encrypt` 切换为 `TRUE` 时，`telnet` 每次启用或禁用加密时都会打印消息。此切换的初始值为 `FALSE`。

**`?`** 显示合法的 `toggle` 命令。

**`z`** 挂起 `telnet`。此命令仅在用户使用 [csh(1)](csh.1.md) 时有效。

**`!`** [`command`] 在本地系统的子 shell 中执行单个命令。如果省略 `command`，则调用交互式子 shell。

**`?`** [`command`] 获取帮助。不带参数时，`telnet` 打印帮助摘要。如果指定了 `command`，`telnet` 会仅打印该命令的帮助信息。

## 环境变量

`telnet` 至少使用 `HOME`、`SHELL`、`DISPLAY` 和 `TERM` 环境变量。其他环境变量可通过 `TELNET ENVIRON` 选项传播到另一端。

## 文件

**`~/.telnetrc`** 用户自定义的 telnet 启动值

## 参见

rlogin(1), rsh(1), [hosts(5)](../man5/hosts.5.md), nologin(5), telnetd(8) （`ports/net/freebsd-telnetd`）

## 历史

`telnet` 命令首次出现于 4.2BSD。

IPv6 支持由 WIDE/KAME 项目添加。

## 注释

在某些远程系统上，在“旧逐行”模式下必须手动关闭回显。

在“旧逐行”模式或 `LINEMODE` 下，终端的 `eof` 字符仅在它是行首第一个字符时才被识别（并发送到远程系统）。
