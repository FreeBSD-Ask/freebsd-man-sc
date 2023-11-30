  SSH-COPY-ID(1)  

SSH-COPY-ID(1)

FreeBSD General Commands Manual

SSH-COPY-ID(1)

[名称](#__u540D___u79F0_)
=======================

`ssh-copy-id` —

将公钥复制到远程主机

[概要](#__u6982___u8981_)
=======================

`ssh-copy-id` \[`-lv`\] \[`-i` keyfile\] \[`-o` option\] \[`-p` port\] \[user@\]hostname

[描述](#__u63CF___u8FF0_)
=======================

`ssh-copy-id` 实用程序将公钥复制到远程主机的 ~/.ssh/authorized\_keys 文件（如果需要，创建文件和目录）。

可以使用以下选项：

[`-i`](#i) file

复制 file 中包含的公钥。 此选项可以指定多次，并且可以与 `-l` 选项结合使用。 如果指定了私钥并且找到了公钥，则将使用公钥。

[`-l`](#l)

复制 ssh-agent(1) 当前持有的密钥。 如果未指定 `-i` 选项，则这是默认设置。

[`-o`](#o) ssh-option

将此选项直接传递给 ssh(1) 。可以多次指定此选项。

[`-p`](#p) port

连接到远程主机上的指定端口而不是默认端口。

[`-v`](#v)

将 -v 传递给 ssh(1) 。

其余参数是要连接的远程主机列表，每个主机可选地由用户名限定。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `ssh-copy-id` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

要将特定密钥发送到多个主机：

`$ ssh-copy-id -i /path/to/keyfile.pub user@host1 user@host2 user@host3`

[历史](#__u5386___u53F2_)
=======================

`ssh-copy-id` 实用程序由 Eitan Adler <[eadler@FreeBSD.org](mailto:eadler@FreeBSD.org)\> 编写，作为 OpenSSH 包含的现有实用程序的直接替代品。

February 28, 2014

FreeBSD 13.1-RELEASE