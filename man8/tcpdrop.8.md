  TCPDROP(8)  

TCPDROP(8)

FreeBSD System Manager's Manual

TCPDROP(8)

[名称](#__u540D___u79F0_)
=======================

`tcpdrop` —

丢弃 TCP 连接

[概要](#__u6982___u8981_)
=======================

`tcpdrop` local-address local-port foreign-address foreign-port `tcpdrop` \[`-l`\] `-a` `tcpdrop` \[`-l`\] `-S` stack `tcpdrop` \[`-l`\] `-s` state `tcpdrop` \[`-l`\] `-S` stack `-s` state

[描述](#__u63CF___u8FF0_)
=======================

`tcpdrop` 命令可用于从命令行删除 TCP 连接。

如果指定了 `-a` 则 `tcpdrop` 将尝试丢弃所有 TCP 连接。

如果指定了 `-S` stack ，则 `tcpdrop` 将尝试使用 TCP 堆栈 stack 删除所有连接。

如果指定了 `-s` state ，则 `tcpdrop` 将尝试丢弃所有处于 state 状态的 TCP 连接。 state 是 `SYN_SENT`, `SYN_RCVD`, `ESTABLISHED`, `CLOSE_WAIT`, `FIN_WAIT_1`, `CLOSING`, `LAST_ACK`, `FIN_WAIT_2`, `或` `TIME_WAIT` 。

如果指定了 `-S` stack 和 `-s` state , `tcpdrop` 将尝试丢弃所有处于 state 状态并使用 TCP 堆栈 stack 的 TCP 连接。 由于处于 `TIME_WAIT` 状态的 TCP 连接不绑定到任何 TCP 堆栈，使用选项 `-s` `TIME_WAIT` 与 `-S` stack 选项会导致 `tcpdrop` 不会丢弃任何 TCP 连接。

除了 `-a`, `-S`, 或 `-s` 选项之外，还可以给出 `-l` 标志，以列出 tcpdrop 调用以一次删除所有相应的 TCP 连接。

如果没有指定 `-a`, `-S` 或 `-s` 选项，则只有给定的本地地址 local-address, 端口 local-port, 和外部地址 foreign-address, 端口 foreign-port 之间的连接将被丢弃。

地址和端口可以通过名称或数值指定。 支持 IPv4 和 IPv6 地址格式。

地址和端口可以用句点或冒号而不是空格分隔。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `tcpdrop` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

如果与 httpd(8) 的连接导致网络链路拥塞，则可以丢弃负责的 TCP 会话：

\# sockstat -c | grep httpd www httpd 16525 3 tcp4 \\ 192.168.5.41:80 192.168.5.1:26747 

以下命令将断开连接：

\# tcpdrop 192.168.5.41 80 192.168.5.1 26747 

以下命令将删除所有连接，但与端口 22（ sshd(8) 使用的端口）之间的连接除外：

\# tcpdrop -l -a | grep -vw 22 | sh 

以下命令将使用 TCP 堆栈 fastack 删除所有连接：

\# tcpdrop -S fastack 

要丢弃所有处于 LAST\_ACK 状态的 TCP 连接，请使用：

\# tcpdrop -s LAST\_ACK 

要使用 TCP 堆栈 fastack 并处于 LAST\_ACK 状态删除所有 TCP 连接，请使用：

\# tcpdrop -S fastack -s LAST\_ACK 

[参见](#__u53C2___u89C1_)
=======================

netstat(1), sockstat(1), tcp(4), tcp\_functions(9)

[作者](#__u4F5C___u8005_)
=======================

Markus Friedl <[markus@openbsd.org](mailto:markus@openbsd.org)\> Juli Mallett <[jmallett@FreeBSD.org](mailto:jmallett@FreeBSD.org)\>

September 15, 2017

FreeBSD 13.1-RELEASE