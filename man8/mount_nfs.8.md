# mount_nfs(8)

`mount_nfs` — 挂载 NFS 文件系统

## 名称

`mount_nfs`

## 概要

`mount_nfs [-23bcdiLlNPsTU] [-a maxreadahead] [-D deadthresh] [-g maxgroups] [-R readdirsize] [-o options] [-R retrycnt] [-r readsize] [-t timeout] [-w writesize] [-x retrans] rhost:path node`

## 描述

`mount_nfs` 工具调用 nmount(2) 系统调用，准备并将远程 NFS 文件系统（`rhost`:`path`）嫁接到文件系统树的 `node` 点上。此命令通常由 [mount(8)](mount.8.md) 执行。对于 NFSv2 和 NFSv3，它实现了 RFC 1094 附录 A 和 RFC 1813 附录 I 中描述的挂载协议。对于 NFSv4，它使用 RFC 7530、RFC 5661 和 RFC 7862 中描述的 NFSv4 协议。

默认情况下，`mount_nfs` 会持续重试直到挂载成功。此行为适用于 [fstab(5)](../man5/fstab.5.md) 中列出的、对启动过程至关重要的文件系统。对于非关键文件系统，`bg` 和 `retrycnt` 选项提供了在服务器不可用时防止启动过程挂起的机制。

如果服务器在 NFS 文件系统已挂载的情况下变得无响应，该文件系统上任何新的或未完成的文件操作都将不可中断地挂起，直到服务器恢复。要修改此默认行为，请参见 `intr` 和 `soft` 选项。

选项如下：

```sh
- 聚合在一起的多个网络接口。
- 使用多个队列的快速网络接口。
```

```sh
udp -   在 IPv4 上使用 UDP
tcp -   在 IPv4 上使用 TCP
udp6 -  在 IPv6 上使用 UDP
tcp6 -  在 IPv6 上使用 TCP
```

```sh
krb5 -  使用 KerberosV 认证
krb5i - 使用 KerberosV 认证并对
        RPC 应用完整性校验
krb5p - 使用 KerberosV 认证并
        加密 RPC 数据
sys -   默认的 AUTH_SYS，使用
        uid + gid 列表认证器
```

**`acregmin`**=<`seconds`>

**`acregmax`**=<`seconds`>

**`acdirmin`**=<`seconds`>

**`acdirmax`**=<`seconds`> 当文件属性被缓存时，会计算一个超时值以确定给定的缓存条目是否已过期。这四个值决定了“目录”属性和“常规”（即其他所有）属性超时的上下限。默认值为常规文件 3 -> 60 秒，目录 30 -> 60 秒。计算超时的算法基于文件的年龄。文件越旧，缓存被认为有效的时间越长，但受上述限制约束。

**`actimeo`**=<`seconds`> 将上述四个缓存超时设置为指定值。

**`allgssname`** 此选项可与 `-o` `gssname` 一起使用，指定所有操作都应使用基于主机的发起者凭证。这可用于运行系统守护进程的客户端，这些守护进程需要访问 NFSv4 挂载卷上的文件。

**`bg`** 如果初次尝试联系服务器失败，则派生一个子进程在后台继续尝试挂载。适用于 [fstab(5)](../man5/fstab.5.md)，其中文件系统挂载对多用户操作并非关键。

**`bgnow`** 类似于 `bg`，派生一个子进程在后台继续尝试挂载，但不会先在前台尝试挂载。这消除了服务器无响应时 60 秒以上的超时。适用于在服务器可能不可用时加快客户端的启动过程。对于相互依赖的服务器（如交叉挂载的服务器，两台服务器互为对方的 NFS 客户端）以及必须在文件服务器之前启动的集群节点，这种情况很常见。

**`deadthresh`**=<`value`> 将“死服务器阈值”设置为指定的往返超时间隔数，超过此数后显示“server not responding”消息。

**`dumbtimer`** 关闭动态重传超时估计器。这对于表现出高重传率的 UDP 挂载可能有用，因为动态估计的超时间隔可能太短。

**`fg`** 与不指定 `bg` 相同。

**`gssname`**=<`service-principal-name`> 此选项可与 NFSv4 挂载的 KerberosV 安全风格一起使用，用于指定默认 keytab 文件中基于主机的条目的“service-principal-name”，该文件用于系统操作。它允许由“root”执行挂载，并避免系统操作的缓存凭证过期导致的问题。“service-principal-name”应不带实例或域指定，通常为“host”、“nfs”或“root”，但如果本地系统的 [gethostname(3)](../gen/gethostname.3.md) 值与 keytab 中基于主机的主体不匹配，也可以使用 <`service`>@<`fqdn`> 形式。

**`hard`** 与不指定 `soft` 相同。

**`intr`** 使挂载可中断，这意味着当进程收到终止信号时，由于服务器无响应而延迟的文件系统调用将以 EINTR 失败。为避免在 NFS 服务器上留下不确定状态的文件锁，建议将 `nolockd` 选项与此选项一起使用。

**`maxgroups`**=<`value`> 将凭证的组列表最大大小设置为指定值。这应用于挂载到无法处理 RFC 1057 中指定的 16 个组列表大小的旧服务器。如果许多组中的用户无法从挂载点获得响应，请尝试 8。

**`mountport`**=<`value`> 指定用于与 NFS 服务器上的 mountd(8) 通信的端口号。此选项允许在不运行 rpcbind(8) 服务的情况下执行 NFSv2 或 NFSv3 挂载。此选项对 NFSv4 挂载无意义，因为 NFSv4 不使用 Mount 协议。

**`mntudp`** 强制挂载协议使用 UDP 传输，即使对于 TCP NFS 挂载也是如此。（某些旧 BSD 服务器需要此选项。）

**`nametimeo`**=<`value`> 覆盖 NFS_DEFAULT_NAMETIMEO 的默认值，用于正向名称缓存条目的超时（以秒为单位）。如果设置为 0，则禁用该挂载点的正向名称缓存。

**`negnametimeo`**=<`value`> 覆盖 NFS_DEFAULT_NEGNAMETIMEO 的默认值，用于负向名称缓存条目的超时（以秒为单位）。如果设置为 0，则禁用该挂载点的负向名称缓存。

**`nconnect`**=<`value`> 指定用于 NFS 版本 4 次版本 1 或 2 挂载的 TCP 连接数（1-16）。多个 TCP 连接可以为某些网络配置提供更多的客户端到服务器网络带宽，例如：第一条 TCP 连接将用于所有完全由小型 RPC 消息组成的 RPC。可能有大型 RPC 消息的 RPC（Read/Readdir/Write）以轮询方式分布在额外的 TCP 连接上。此选项会导致使用更多的 IP 端口号。此选项需要 `nfsv4` 选项。注意，对于 AmazonEFS 等 NFS 服务器，每个新的 TCP 连接可能连接到单独维护锁定状态的不同集群，因此不能使用此选项。

**`nfsv2`** 使用 NFS 版本 2 协议（默认为先尝试版本 3 再尝试版本 2）。注意 NFS 版本 2 有 2 GB 的文件大小限制。

**`nfsv3`** 使用 NFS 版本 3 协议。

**`nfsv4`** 使用 NFS 版本 4 协议。此选项将强制挂载使用 TCP 传输。默认情况下，将使用 NFS 版本 4 服务器支持的最高次版本。参见 `minorversion` 选项。确保所有 NFS 版本 4 客户端在 **/etc/hostid** 中具有唯一值。

**`minorversion`**=<`value`> 为 NFS 版本 4 挂载使用指定的次版本，覆盖默认值。支持的次版本为 0、1 和 2。此选项仅在与 `nfsv4` 选项一起使用时才有意义。

**`oneopenown`** 使 NFS 版本 4 协议的次版本 1 或 2 挂载对所有 Open 使用单个 OpenOwner。这对于 OpenOwner 数量限制非常低的服务器（如 AmazonEFS）可能有用。当 NFS 版本 4 Open 累积时（如 [nfsstat(1)](../man1/nfsstat.1.md) 使用 `-c` 和 `-E` 命令行选项显示的“Opens”计数所示），可能是必需的。Open 累积的常见情况是 NFS 挂载内的共享库被多个进程使用，其中至少一个进程始终在运行。此选项不能用于 NFS 版本 4 次版本 0 挂载。当服务器颁发 Delegation 时，它可能无法正常工作，但请注意 AmazonEFS 服务器目前不颁发委托。此选项仅在与 `nfsv4` 选项一起使用时才有意义。

**`pnfs`** 为 NFS 版本 4 协议的次版本 1 或 2 启用并行 NFS（pNFS）支持。此选项仅在与 `nfsv4` 选项一起使用时才有意义。

**`noac`** 禁用属性缓存。

**`noconn`** 对于 UDP 挂载点，不执行 [connect(2)](../sys/connect.2.md)。如果服务器不回复来自标准 NFS 端口号 2049 的请求，或使用不同 IP 地址回复请求（当服务器是多宿主时可能发生），则必须使用此选项。将 `vfs.nfs.nfs_ip_paranoia` sysctl 设置为 0 将使此选项成为默认值。

**`nocto`** 通常，NFS 客户端维护 close-to-open 缓存一致性。这通过在关闭时刷新并在打开时检查来实现。打开时检查通过从服务器获取属性并在属性与客户端缓存的属性不匹配时清除数据缓存来实现。此选项禁用打开时检查。它可以提高只读挂载的性能，但仅应在服务器上的数据很少更改时使用。在启用此选项之前，请务必了解其后果。

**`noinet4 , noinet6`** 禁用 `AF_INET` 或 `AF_INET6` 连接。适用于同一名称同时具有 A 记录和 AAAA 记录的主机。

**`nolockd`** 对于 NFSv3 挂载，*不*通过 NLM 协议通过网络转发 [fcntl(2)](../sys/fcntl.2.md) 锁；对于 NFSv4 挂载，*不*通过 NFSv4 协议转发。所有锁都将是本地的，服务器看不到，同样 NFSv3 或 NFSv4 挂载的其他 NFS 客户端也看不到。这消除了在 NFSv3 挂载的客户端上运行 rpcbind(8) 服务以及 rpc.statd(8) 和 rpc.lockd(8) 服务器的需要。注意，此选项仅在执行初始挂载时生效，如果在更新挂载选项时使用则会被静默忽略。另外注意，NFSv4 挂载不使用这些守护进程。NFSv4 协议处理锁，除非指定了此选项。

**`noncontigwr`** 此挂载选项允许 NFS 客户端合并正在写入的非连续字节范围，使脏字节范围成为脏字节的超集。这显著减少了软件构建的写入次数。如果文件已被文件锁定，则不合并字节范围，因为从多个客户端修改文件的大多数应用程序将使用文件锁定。因此，对于从多个客户端并发修改文件而不使用文件锁定的罕见情况，此选项可能导致文件损坏。

**`principal`** 对于 RPCSEC_GSS 安全风格（如 krb5、krb5i 和 krb5p），此选项设置服务器期望的基于主机的主体名称。此选项覆盖默认值，默认值将是 ``nfs@<server-fqdn>''，通常应该足够。

**`noresvport`** *不*使用保留的套接字端口号（见下文）。

**`port`**=<`port_number`> 为 NFS 请求使用指定的端口号。默认是向 portmapper 查询 NFS 端口。

**`proto`**=<`protocol`> 指定要使用的传输协议版本。当前为：

**`rdirplus`** 与 NFSV3 一起使用，指定应使用 ReaddirPlus RPC。对于 NFSV4，设置此选项具有类似效果，它将使 Readdir 操作获取更多属性。此选项减少了诸如“ls -l”等情况的 RPC 流量，但倾向于用预取条目淹没属性和名称缓存。尝试此选项，看看性能是提高还是降低。可能对于具有大带宽时延乘积的客户端到服务器网络互连最有用。

**`readahead`**=<`value`> 将预读计数设置为指定值。此值范围为 0 - 4，确定在顺序读取大文件时提前读取多少块。对于具有大带宽 * 时延乘积的挂载，建议尝试大于 1 的值。

**`readdirsize`**=<`value`> 将 readdir 读取大小设置为指定值。该值通常应为 `DIRBLKSIZ` 的倍数，且 <= 挂载的读取大小。

**`resvport`** 使用保留的套接字端口号。此标志已过时，仅为兼容性而保留。现在默认使用保留端口号。（对于客户端具有受信任 root 账户但用户不可信且网络电缆位于安全区域的罕见情况，这确实有帮助，但对于普通桌面客户端不适用。）

**`retrans`**=<`value`> 将软挂载的重传超时计数设置为指定值。

**`retrycnt`**=<`count`> 将挂载重试计数设置为指定值。默认重试计数为零，表示永远重试。每次尝试之间有 60 秒延迟。

**`rsize`**=<`value`> 将读取数据大小设置为指定值。它通常应为大于或等于 1024 的 2 的幂。当主动使用挂载点时“fragments dropped due to timeout”值变大时，应用于 UDP 挂载。（使用 [netstat(1)](../man1/netstat.1.md) 的 `-s` 选项查看“fragments dropped due to timeout”值。）

**`sec`**=<`flavor`> 此选项指定挂载应使用的安全风格。当前为：

**`soft`** 软挂载，意味着文件系统调用将在 `retrycnt` 次往返超时间隔后失败。

**`syskrb5`** 此选项指定 KerberosV NFSv4 次版本 1 或 2 挂载对系统操作使用 AUTH_SYS。使用此选项避免了 KerberosV 挂载在默认 keytab 文件中具有基于主体的主体条目（无 `gssname` 选项）的需要，或执行挂载的用户在挂载时具有有效的 KerberosV 票据授予票据（TGT）的要求。此选项旨在与 `sec`=krb5 和 `tls` 选项一起使用，只能用于次版本 1 或 2 的 NFSv4 挂载。

**`tcp`** 使用 TCP 传输。这是默认选项，因为与 UDP 相比，它在 LAN 和 WAN 配置上都提供了更高的可靠性。某些旧 NFS 服务器不支持此方法；可能需要 UDP 挂载以实现互操作性。

**`timeout`**=<`value`> 将初始重传超时设置为指定值，以十分之一秒为单位。可能对于在高丢包率网络或过载服务器上微调 UDP 挂载有用。如果 [nfsstat(1)](../man1/nfsstat.1.md) 在文件系统活动时显示高重传率，请尝试增加间隔；如果重传率低但响应延迟长，请尝试减少该值。（通常，手动调整超时间隔时应指定 `dumbtimer` 选项。）

**`timeo`**=<`value`> `timeout` 的别名。

**`tls`** 此选项指定与服务器的连接必须根据 RFC 9289 使用 TLS。TLS 仅支持 TCP 连接，并且 rpc.tlsclntd(8) 守护进程必须正在运行，NFS over TCP 连接才能使用 TLS。

**`tlscertname`**=<`name`> 此选项指定在 TLS 握手期间向 NFS 服务器提供的备用证书名称。默认证书文件名为“cert.pem”和“certkey.pem”。指定此选项时，`name` 替换上述文件名中的“cert”。例如，如果 `name` 的值指定为“other”，则要使用的证书文件名将为“other.pem”和“otherkey.pem”。这些文件默认存储在 **/etc/rpc.tlsclntd** 中。此选项仅在与 `tls` 选项一起使用且 rpc.tlsclntd(8) 以 `-m` 命令行标志运行时才有意义。

**`udp`** 使用 UDP 传输。

**`vers`**=<`vers_number`> 为 NFS 请求使用指定的版本号。详情参见 `nfsv2`、`nfsv3` 和 `nfsv4` 选项。

**`wcommitsize`**=<`value`> 将最大待处理写入提交大小设置为指定值。这确定了 NFS 客户端愿意为每个文件缓存的待处理写入数据的最大量。

**`wsize`**=<`value`> 将写入数据大小设置为指定值。关于 `rsize` 选项的注释同样适用，但使用服务器上的“fragments dropped due to timeout”值而不是客户端的。注意，`rsize` 和 `wsize` 选项应仅作为挂载不支持 TCP 挂载的服务器时改善性能的最后手段。

**`-o`** 选项通过 `-o` 标志后跟逗号分隔的选项字符串指定。可能的选项及其含义请参见 [mount(8)](mount.8.md) 手册页。以下 NFS 专用选项也可用：

## 实现注释

当未指定 `rsize` 和 `wsize` 选项时，I/O 大小将设置为 NFS 客户端和服务器都支持的最大值。NFS 客户端支持的最大值由可调参数 `vfs.maxbcachebuf` 定义，可设置为 2 的幂，最高到 `kern.maxphys`。

[nfsstat(1)](../man1/nfsstat.1.md) 命令的 `-m` 命令行选项将显示 `mount_nfs` 选项设置实际为挂载使用了哪些值。

## 兼容性

以下命令行标志等同于 `-o` 命名选项，为与旧安装兼容而支持。

**`-2`** 同 `-o` `nfsv2`

**`-3`** 同 `-o` `nfsv3`

**`-D`** 同 `-o` `deadthresh`

**`-R`** 同 `-o` `readdirsize`=<`value`>

**`-L`** 同 `-o` `nolockd`

**`-N`** 同 `-o` `noresvport`

**`-P`** 使用保留的套接字端口号。此标志已过时，仅为兼容性而保留。（对于客户端具有受信任 root 账户但用户不可信且网络电缆位于安全区域的罕见情况，这确实有帮助，但对于普通桌面客户端不适用。）

**`-R`** 同 `-o` `retrycnt`=<`value`>

**`-T`** 同 `-o` `tcp`

**`-U`** 同 `-o` `mntudp`

**`-a`** 同 `-o` `readahead`=<`value`>

**`-b`** 同 `-o` `bg`

**`-c`** 同 `-o` `noconn`

**`-d`** 同 `-o` `dumbtimer`

**`-g`** 同 `-o` `maxgroups`

**`-i`** 同 `-o` `intr`

**`-l`** 同 `-o` `rdirplus`

**`-r`** 同 `-o` `rsize`=<`value`>

**`-s`** 同 `-o` `soft`

**`-t`** 同 `-o` `retransmit`=<`value`>（已弃用）

**`-w`** 同 `-o` `wsize`=<`value`>

**`-x`** 同 `-o` `retrans`=<`value`>

以下 `-o` 命名选项等同于其他 `-o` 命名选项，为与其他操作系统（如 Linux、Solaris 和 OSX）兼容而支持，以简化 [autofs(4)](../man4/autofs.4.md) 支持的使用。

**`-o`** `vers`=2 同 `-o` `nfsv2`

**`-o`** `vers`=3 同 `-o` `nfsv3`

**`-o`** `vers`=4 同 `-o` `nfsv4`

## 参见

[nfsstat(1)](../man1/nfsstat.1.md), nmount(2), unmount(2), [lagg(4)](../man4/lagg.4.md), nfsv4(4), [fstab(5)](../man5/fstab.5.md), gssd(8), [mount(8)](mount.8.md), [nfsd(8)](nfsd.8.md), [nfsiod(8)](nfsiod.8.md), rpcbind(8), rpc.tlsclntd(8), showmount(8)

## 历史

`mount_nfs` 工具的一个版本出现在 4.4BSD 中。

## 缺陷

由于 NFSv4 执行的打开/锁操作其排序由服务器严格强制执行，因此 `intr` 和 `soft` 选项不能安全使用。对于 NFSv4 次版本 1 或 2 挂载，排序通过会话槽完成，NFSv4 客户端现在能相当好地处理中断的会话槽。因此，如果 `nolockd` 选项与 `intr` 和/或 `soft` 一起使用，NFSv4 次版本 1 或 2 挂载应该能相当好地工作，尽管仍不完全正确。对于 NFSv4 次版本 0 挂载，强烈建议使用不带 `intr` 挂载选项的 `hard` 挂载。
