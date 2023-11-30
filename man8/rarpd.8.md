  RARPD(8)  

RARPD(8)

FreeBSD System Manager's Manual

RARPD(8)

[名称](#__u540D___u79F0_)
=======================

`rarpd` —

反向 ARP 守护进程

[概要](#__u6982___u8981_)
=======================

`rarpd` `-a` \[`-dfsv`\] \[`-t` directory\] \[`-P` pidfile\] `rarpd` \[`-dfsv`\] \[`-t` directory\] \[`-P` pidfile\] interface

[描述](#__u63CF___u8FF0_)
=======================

`rarpd` 实用程序为连接到 interface 的以太网上的反向 ARP 请求提供服务。 收到请求后， `rarpd` 接到接口的以太网上的反向 ARP 请求提供服务。 收到请求后，rarpd 通过其名称将目标硬件地址映射到 IP 地址，该名称必须存在于 ethers(5) 和 hosts(5) 数据库中。 如果主机在两个数据库中都不存在，则翻译无法继续并且不会发送回复。

默认情况下，只有当服务器（即运行 `rarpd` 的主机）可以 "boot" 目标时，才会接受请求。即存在与 /tftpboot/_ipaddr_\* 匹配的文件或目录，其中 _ipaddr_ 是十六进制的目标 IP 地址。 例如，如果存在 /tftpboot/CCD81B12, /tftpboot/CCD81B12.SUN3 或 /tftpboot/CCD81B12-boot 中的任何一个，则会回复IP 地址204.216.27.18。 可以使用 `-s` 标志覆盖此要求（见下文）。

在正常操作中， `rarpd` 会创建一个自身的副本并在后台运行。 通过 syslog(3) 报告异常和错误。

可以使用以下选项：

[`-a`](#a)

监听连接到系统的所有以太网。 如果省略 `-a` ，则必须指定接口。

[`-d`](#d)

如果还指定了 `-f` , `rarpd` 会将消息记录到 _stdout_ 和 _stderr_ ，而不是通过 syslog(3) 。

[`-f`](#f)

在前台运行。

[`-P`](#P)

指定 PID 文件的路径名。 如果未指定，将根据 `-a` 标志或指定的接口名称使用 /var/run/rarpd.pid 或 /var/run/rarpd.ifname.pid 。

[`-s`](#s)

对存在以太网到 IP 地址映射的任何 RARP 请求提供响应；不依赖于 /tftpboot/_ipaddr_\* 的存在。

[`-t`](#t)

为 /tftpboot 提供一个备用 tftp 根目录，类似于 tftpd(8) 的 `-s` 选项。 这允许 `rarpd` 选择性地响应 RARP 请求，但使用备用目录进行 IP 检查。

[`-v`](#v)

启用详细的系统日志记录。

[文件](#__u6587___u4EF6_)
=======================

/etc/ethers

/etc/hosts

/tftpboot

/var/run/rarpd.pid

[参见](#__u53C2___u89C1_)
=======================

bpf(4) Finlayson, R., Mann, T., Mogul, J.C., and Theimer, M., RFC 903: Reverse Address Resolution Protocol, June 1984, 4 p.

[作者](#__u4F5C___u8005_)
=======================

Craig Leres <[leres@ee.lbl.gov](mailto:leres@ee.lbl.gov)\> 和 Steven McCanne <[mccanne@ee.lbl.gov](mailto:mccanne@ee.lbl.gov)\> >。 加利福尼亚大学伯克利分校劳伦斯伯克利实验室。

[缺陷](#__u7F3A___u9677_)
=======================

`rarpd` 实用程序可以依赖 DNS 来解析从 /etc/ethers 中发现的名称。 如果此名称不在 DNS 中但在 /etc/hosts 中，则 DNS 查找会导致 RARP 响应延迟，因此在这种情况下建议配置 nsswitch.conf(5) 以首先读取 /etc/hosts 。

July 9, 2012

FreeBSD 13.1-RELEASE