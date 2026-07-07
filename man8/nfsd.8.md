# nfsd(8)

`nfsd` — 远程 NFS 服务器

## 名称

`nfsd` NFS 服务器

## 概要

`nfsd [-arduteN] [-n num_servers] [-h bindip] [-p pnfs_setup] [-m mirror_level] [-P pidfile] [-V virtual_hostname] [--maxthreads max_threads] [--minthreads min_threads]`

## 描述

`nfsd` 工具运行在服务器机器上，为来自客户端机器的 NFSv4 和/或 NFSv3 请求提供服务。一台机器要作为服务器运行，至少必须有一个 `nfsd` 在运行。

除非另有说明，将为 UDP 传输每 CPU 启动八个服务器。

`nfsd` 服务器可配置为服务 NFSv3、NFSv4 或两者。当在 [rc.conf(5)](../man5/rc.conf.5.md) 中设置

```sh
nfs_server_enable="YES"
```

时，默认情况下 `nfsd` 配置为仅服务 NFSv3。要将 `nfsd` 配置为服务 NFSv4，你还必须：

```sh
nfsv4_server_enable="YES"
```

```sh
nfsv4_server_only="YES"
```

- 在 exports(5) 中添加 “V4:” 行。（这以及每个导出文件系统的 ZFS sharenfs 属性或 exports 行都是必需的。）
- 选择以“字符串”方式处理 uid，除非你执行 kerberos(7) 挂载或运行 nfsuserd(8)，否则这可能是最简单的方法（选择其一，不要两者都用）。将 sysctl MIB `vfs.nfs.enable_uidtostring` 和 `vfs.nfsd.enable_stringtouid` 设置为 1 并不运行 nfsuserd 即选择以“字符串”方式处理 uid。
- 在 [rc.conf(5)](../man5/rc.conf.5.md) 中设置，或者如果你不想服务 NFSv3，则在 [rc.conf(5)](../man5/rc.conf.5.md) 中设置。

当 `nfsd` 在适当配置的 vnet jail 中运行时，服务器仅限于 TCP 传输，不提供 pNFS 服务。因此，在 vnet jail 中运行时必须指定 `-t` 选项，并且不能指定 `-u`、`-p` 和 `-m` 选项中的任何一个。更多信息请参见 [jail(8)](jail.8.md)。

以下选项可用：

**`-r`** 向 rpcbind(8) 注册 NFS 服务，但不创建任何服务器。此选项可与 `-u` 或 `-t` 选项一起使用，以便在 rpcbind 服务器重启时重新注册 NFS。

**`-d`** 向 rpcbind(8) 取消注册 NFS 服务，但不创建任何服务器。

**`-P`** `pidfile` 指定主进程 PID 存储的文件的备用位置。默认位置为 **/var/run/nfsd.pid**。

**`-V`** `virtual_hostname` 指定用作主体名称的主机名，而不是默认主机名。

**`-n`** `threads` 此选项已弃用，且最多限制为 256 个线程。现在应使用 `--maxthreads` 和 `--minthreads` 选项。`--minthreads` 和 `--maxthreads` 的 `threads` 参数可以设置为相同的值，以避免线程数的动态变化。

**`--maxthreads`** `threads` 指定保留以服务请求的最大服务器数。

**`--minthreads`** `threads` 指定保留以服务请求的最小服务器数。

**`-h`** `bindip` 指定本地主机上要绑定到的 IP 地址或主机名。当主机有多个接口时，建议使用此选项。可以指定多个 `-h` 选项。

**`-a`** 指定 nfsd 应绑定到通配符 IP 地址。如果未给出 `-h` 选项，这是默认值。也可以在任何给定的 `-h` 选项之外额外指定。注意，无论你使用 -a 还是不使用 -h，NFS/UDP 绑定到通配符 IP 地址时都无法正常工作。

**`-p`** `pnfs_setup` 在服务器中启用 pNFS 支持，并指定守护进程启动它所需的信息。此选项只能在一台服务器上使用，指定此服务器将作为 pNFS 服务的元数据服务器（MDS）。只有在至少配置了一台 FreeBSD 系统作为其数据服务器（DS）时才能执行此操作。`pnfs_setup` 字符串是一组由 “,” 字符分隔的字段：每个字段指定一个 DS。它由服务器主机名组成，后跟 “:” 和 DS 的数据存储文件系统在此 MDS 服务器上挂载的目录路径。这可以选择性地后跟 “#” 和 mds_path，mds_path 是此 MDS 上导出文件系统的目录路径。如果指定了此项，意味着此 DS 仅用于存储此 mds_path 文件系统的数据文件。如果此可选组件不存在，DS 将用于存储所有导出的 MDS 文件系统的数据文件。在用此选项指定的 `nfsd` 启动之前，DS 存储文件系统必须挂载到此系统上。例如：nfsv4-data0:/data0,nfsv4-data1:/data1 将指定两台名为 nfsv4-data0 和 nfsv4-data1 的 DS 服务器，它们构成 pNFS 服务的数据存储组件。这两个 DS 将用于存储此 MDS 上所有导出文件系统的数据文件。目录 “/data0” 和 “/data1” 是数据存储服务器导出的存储目录挂载到此系统（将作为 MDS）的位置。而对于示例：nfsv4-data0:/data0#/export1,nfsv4-data1:/data1#/export2 将如上指定两个 DS，但是 nfsv4-data0 将用于存储 “/export1” 的数据文件，nfsv4-data1 将用于存储 “/export2” 的数据文件。为 DS 使用 IPv6 地址时，请谨慎使用链路本地地址。DS 的 IPv6 地址发送给客户端，其中没有作用域区域。因此，链路本地地址可能不适用于 pNFS 客户端到 DS 的 TCP 连接。解析时，`nfsd` 仅在链路本地地址是 [getaddrinfo(3)](../net/getaddrinfo.3.md) 为 DS 主机名返回的唯一地址时才使用它。

**`-m`** `mirror_level` 此选项仅在与 `-p` 选项一起使用时才有意义。它指定 “mirror_level”，定义有多少 DS 将拥有文件数据存储文件的副本。默认值 1 意味着不在 DS 上镜像数据存储文件。“mirror_level” 通常设置为 2 以启用镜像，但最高可达 NFSDEV_MAXMIRRORS。MDS 上每个导出文件系统必须至少有 “mirror_level” 个 DS，如 `-p` 选项中所指定。这意味着，对于上面使用 “#/export1” 和 “#/export2” 的示例，无法进行镜像。需要为 “#/export1” 和 “#/export2” 各有两个 DS 条目才能支持 “mirror_level” 为 2。如果启用镜像，服务器必须使用 Flexible File 布局。如果未启用镜像，服务器默认使用 File 布局，但如果 [sysctl(8)](sysctl.8.md) vfs.nfsd.default_flexfile 设置为非零值，则可以将此默认值更改为 Flexible File 布局。

**`-t`** 服务 TCP NFS 客户端。

**`-u`** 服务 UDP NFS 客户端。

**`-e`** 忽略；为向后兼容而保留。

**`-N`** 使 `nfsd` 在前台执行而不是守护进程模式。

例如，“`nfsd -u -t --minthreads 6 --maxthreads 6`” 使用六个内核线程（服务器）服务 UDP 和 TCP 传输。

对于专用于服务 NFS RPC 的系统，线程（服务器）数应足以处理峰值客户端 RPC 负载。对于执行其他服务的系统，可能需要限制线程（服务器）数，以便为这些其他服务提供资源。

`nfsd` 工具在 NFS 服务器规范中指示的端口上侦听服务请求；参见 Network File System Protocol Specification, RFC1094, NFS: Network File System Version 3 Protocol Specification, RFC1813, Network File System (NFS) Version 4 Protocol, RFC7530, Network File System (NFS) Version 4 Minor Version 1 Protocol, RFC5661, Network File System (NFS) Version 4 Minor Version 2 Protocol, RFC7862, File System Extended Attributes in NFSv4, RFC8276 和 Parallel NFS (pNFS) Flexible File Layout, RFC8435。

如果 `nfsd` 检测到正在运行的内核中未加载 NFS，它将尝试使用 [kldload(2)](../sys/kldload.2.md) 加载包含 NFS 支持的可加载内核模块。如果此操作失败或没有 NFS KLD 可用，`nfsd` 将以错误退出。

如果 `nfsd` 要在具有多个接口或接口别名的主机上运行，建议使用 `-h` 选项。如果不使用此选项，NFS 可能不会响应来自它们发送到的同一 IP 地址的 UDP 数据包。在防火墙机器上保护 NFS 导出时也建议使用此选项，以便 NFS 套接字只能由内部接口访问。然后使用 `ipfw` 工具阻止来自外部接口的 NFS 相关数据包。

如果服务器已停止服务客户端并生成了类似 “`nfsd server cache flooded...`” 的控制台消息，则需要增加 vfs.nfsd.tcphighwater 的值。这应该允许服务器再次处理请求而无需重启。此外，发生这种情况时，你可能还需要考虑将 vfs.nfsd.tcphighwater 的值减少到几分钟（以秒为单位）而不是 12 小时。

不幸的是，将 vfs.nfsd.tcphighwater 设置得太大可能导致达到 mbuf 限制，如类似 “`kern.ipc.nmbufs limit reached`” 的控制台消息所示。如果找不到合适的上述 `sysctl` 值，可以通过将 vfs.nfsd.cachetcp 设置为 0 来禁用 TCP 的 DRC 缓存。

`nfsd` 工具必须用 `SIGUSR1` 终止，不能用 `SIGTERM` 或 `SIGQUIT` 杀死。`nfsd` 工具需要忽略这些信号以便在关机期间尽可能长时间地保持活动，否则回环挂载将无法卸载。如果必须杀死 `nfsd`，只需执行 “`kill -USR1 <PID of master nfsd>`”。

## 退出状态

`nfsd` 工具成功时退出 0，发生错误时退出 >0。

## 参见

[nfsstat(1)](../man1/nfsstat.1.md), [kldload(2)](../sys/kldload.2.md), [nfssvc(2)](../sys/nfssvc.2.md), nfsv4(4), pnfs(4), pnfsserver(4), exports(5), [rc.conf(5)](../man5/rc.conf.5.md), stablerestart(5), kerberos(7), gssd(8), [ipfw(8)](ipfw.8.md), [jail(8)](jail.8.md), mountd(8), [nfsiod(8)](nfsiod.8.md), nfsrevoke(8), nfsuserd(8), rpcbind(8)

## 历史

`nfsd` 工具首次出现在 4.4BSD 中。

## 缺陷

如果 `nfsd` 在 gssd(8) 未运行时启动，它将仅服务 AUTH_SYS 请求。要解决此问题，你必须在 gssd(8) 运行后杀死 `nfsd` 然后重新启动它。

对于 Flexible File 布局 pNFS 服务器，如果有 Linux 客户端执行 NFSv4.1 或 NFSv4.2 挂载，这些客户端可能需要在 MDS 上将 [sysctl(8)](sysctl.8.md) vfs.nfsd.flexlinuxhack 设置为 1 作为变通方法。

Linux 5.n 内核似乎已打补丁，使得不需要设置此 [sysctl(8)](sysctl.8.md)。

对于 NFSv4.2，Copy 操作可能需要很长时间才能完成。如果同时有 ExchangeID 或 DelegReturn 操作需要对所有 NFSv4 状态的独占锁，这可能导致 `nfsd` 服务器的“停顿”。如果你的存储在未启用块克隆的 ZFS 上，将 [sysctl(8)](sysctl.8.md) `vfs.zfs.dmu_offset_next_sync` 设置为 0 通常可以避免此问题。也可以将 [sysctl(8)](sysctl.8.md) `vfs.nfsd.maxcopyrange` 设置为 10-100 兆字节以尝试减少 Copy 操作时间。作为最后手段，将 [sysctl(8)](sysctl.8.md) `vfs.nfsd.maxcopyrange` 设置为 0 可禁用 Copy 操作。
