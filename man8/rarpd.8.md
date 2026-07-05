# rarpd.8

`rarpd` — 反向 ARP 守护进程

## 名称

`rarpd`

## 概要

`rarpd -a [-dfsv] [-t directory] [-P pidfile]`
`rarpd [-dfsv] [-t directory] [-P pidfile] interface`

## 描述

`rarpd` 工具为连接到 `interface` 的以太网上的反向 ARP 请求提供服务。收到请求后，`rarpd` 通过名称将目标硬件地址映射到 IP 地址，该名称必须同时存在于 [ethers(5)](../man5/ethers.5.md) 和 [hosts(5)](../man5/hosts.5.md) 数据库中。如果某台主机在两个数据库中都不存在，则无法进行转换，也不会发送回复。

默认情况下，仅当服务器（即运行 `rarpd` 的主机）能够“引导”目标时，请求才会被响应；也就是说，存在与通配符 **/tftpboot/ipaddr\*** 匹配的文件或目录，其中 *ipaddr* 是目标 IP 地址的十六进制表示。例如，如果 **/tftpboot/CCD81B12**、**/tftpboot/CCD81B12.SUN3** 或 **/tftpboot/CCD81B12-boot** 中的任何一个存在，则会回复 IP 地址 204.216.27.18。可以使用 `-s` 标志覆盖此要求（见下文）。

在正常操作中，`rarpd` 会派生自身的副本并在后台运行。异常和错误通过 syslog(3) 报告。

可用选项如下：

**`-a`** 在连接到系统的所有以太网上监听。如果省略 `-a`，则必须指定一个接口。

**`-d`** 如果同时指定了 `-f`，`rarpd` 将消息记录到 *stdout* 和 *stderr*，而不是通过 syslog(3)。

**`-f`** 在前台运行。

**`-P`** 指定 PID 文件的路径名。未指定时，将根据 `-a` 标志或指定的接口名使用 **/var/run/rarpd.pid** 或 **/var/run/rarpd.ifname.pid**。

**`-s`** 对任何存在以太网到 IP 地址映射的 RARP 请求都提供响应；不依赖于 **/tftpboot/ipaddr\*** 的存在。

**`-t`** 提供替代的 tftp 根目录以代替 **/tftpboot**，类似于 [tftpd(8)](tftpd.8.md) 的 `-s` 选项。这使得 `rarpd` 可以选择性地响应 RARP 请求，但使用替代目录进行 IP 检查。

**`-v`** 启用详细的 syslog 记录。

## 文件

**/etc/ethers**
**/etc/hosts**
**/tftpboot**
**/var/run/rarpd.pid**

## 参见

[bpf(4)](../man4/bpf.4.md)

> Finlayson, R., Mann, T., Mogul, J.C., Theimer, M., "RFC 903: Reverse Address Resolution Protocol", June 1984, 4 p.

## 作者

Craig Leres <leres@ee.lbl.gov> 和 Steven McCanne <mccanne@ee.lbl.gov>。Lawrence Berkeley Laboratory, University of California, Berkeley, CA.

## 缺陷

`rarpd` 工具可能依赖 DNS 来解析从 **/etc/ethers** 中发现的名称。如果此名称不在 DNS 中但在 **/etc/hosts** 中，DNS 查找可能导致 RARP 响应延迟，因此在这种情况下建议配置 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 以优先读取 **/etc/hosts**。
