# diskless.8

`diskless` — 通过 PXE 在网络上引导系统

## 名称

`diskless`

## 描述

通过网络引导机器的能力对于 *diskless*（无盘）或 *dataless*（无数据）机器非常有用，也可作为修复或重新安装本地磁盘文件系统时的临时措施。本文件提供了客户端通过网络引导时，客户端与其服务器之间交互的一般性描述。

## 操作

通过网络引导系统时，客户端与服务器之间的交互分为三个阶段：

1. 第一阶段引导程序（通常是内置在以太网卡中的 PXE）加载第二阶段引导程序。
2. 第二阶段引导程序（通常是 pxeboot(8)）加载模块和内核，并引导内核。
3. 内核通过 NFS 挂载根目录，并从此处继续。

下面将分别详细描述每个阶段。

首先，第一阶段引导程序通过网络加载第二阶段引导程序。第一阶段引导程序通常使用 BOOTP 或 DHCP 获取要加载的文件名，然后使用 TFTP 加载该文件。该文件通常称为 `pxeboot`，应从 **/boot/pxeboot** 复制到服务器上的 TFTP 目录中，该目录通常为 **/tftpdir**。

第二阶段引导程序随后加载附加模块和内核。这些文件可能不在 DHCP 或 BOOTP 服务器上。你可以使用 DHCP 配置中提供的 `next-server` 选项来指定存放第二阶段引导文件和内核的服务器。第二阶段程序使用 NFS 或 TFTP 获取这些文件。默认使用 NFS。如果你使用 pxeboot(8)，可以通过在 [make.conf(5)](../man5/make.conf.5.md) 中设置 `LOADER_TFTP_SUPPORT=YES`，然后通过以下命令重新编译并重新安装 pxeboot(8)，来安装使用 TFTP 的版本。在此处通常需要使用 TFTP，这样你就可以将自定义内核放在 **/tftpdir/** 中。如果你使用 NFS 且没有为 `diskless` 客户端准备自定义根文件系统，第二阶段引导将加载服务器的内核作为 `diskless` 机器的内核，这可能不是你想要的结果。

```sh
cd /usr/src/stand
make clean; make; make install
cp /boot/pxeboot /tftpdir/
```

在第三阶段，内核以两种方式之一获取 IP 网络配置，然后继续挂载根文件系统并开始运行。如果第二阶段加载器支持使用内核环境将网络配置传递给内核，则内核将使用该信息配置网络接口。否则，它必须使用 DHCP 或 BOOTP 获取配置信息。引导脚本识别 `diskless` 启动，并执行 **/etc/rc.d/resolv**、**/etc/rc.d/tmp**、**/etc/rc.d/var** 和 **/etc/rc.initdiskless** 中的操作。

## 配置

要运行 `diskless` 客户端，你需要以下内容：

- 一个导出根分区和 **/usr** 分区并具有适当权限的 NFS 服务器。`diskless` 脚本可用于只读分区，只要根分区以 `-maproot=0` 导出，以便访问某些系统文件。例如，**/etc/exports** 可以包含以下行：

```sh
<ROOT> -ro -maproot=0 -alldirs <list of diskless clients>
/usr -ro -alldirs <list of diskless clients>
```

其中 <ROOT> 是服务器上根分区的挂载点。在许多情况下，你可能会决定（同样以只读方式）导出服务器自身使用的根目录。

- 一个 BOOTP 或 DHCP 服务器。可以通过取消 **/etc/inetd.conf** 中 “`bootps`” 行的注释来启用 bootpd(8)。**/etc/bootptab** 示例可能如下：

```sh
 .default:\
    hn:ht=1:vm=rfc1048:\
    :sm=255.255.255.0:\
    :sa=<SERVER>:\
    :gw=<GATEWAY>:\
    :rp="<SERVER>:<ROOT>":
<CLIENT>:ha=0123456789ab:tc=.default
```

其中 <SERVER>、<GATEWAY> 和 <ROOT> 含义明确。

- 一个正确初始化的根分区。如果你刚刚开始，应直接使用服务器自身的根目录 **/**，不要尝试克隆它。

你通常不希望为 `diskless` 引导使用与服务器上相同的 `rc.conf` 或 `rc.local` 文件。`diskless` 引导脚本提供了一种机制，通过该机制你可以覆盖 **/etc** 中的各种文件（以及根目录下的其他子目录）。

你应特别注意的一个差异是 **/etc/defaults/rc.conf** 中 `local_startup` 的值。`diskless` 引导的典型值是 `mountcritremote`，但你的需求可能不同。

脚本提供了四个覆盖目录，分别位于 **/conf/base**、**/conf/default**、**/conf/<broadcast-ip>** 和 **/conf/<machine-ip>**。你应始终创建 **/conf/base/etc**，它将完全替换 `diskless` 机器上服务器的 **/etc**。你可以在此处克隆服务器的 **/etc**，也可以创建一个特殊文件，告诉 `diskless` 引导脚本将服务器的 **/etc** 重新挂载到 **/conf/base/etc**。方法是创建文件 **/conf/base/etc/diskless_remount**，其中包含要用作 `diskless` 机器 **/etc** 基础的挂载点。例如，该文件可能包含：

```sh
10.0.0.1:/etc
```

或者，如果服务器包含多个独立的根目录，该文件可能包含：

```sh
10.0.0.1:/usr/diskless/4.7-RELEASE/etc
```

这可以工作，但如果你将 **/usr/diskless/4.7-RELEASE** 复制到 **/usr/diskless/4.8-RELEASE** 并升级了安装，就需要修改 `diskless_remount` 文件以反映该移动。为避免这种情况，`diskless_remount` 文件中以 **/** 开头的路径会自动加上客户端根目录的实际路径作为前缀，因此该文件可以改为包含：

```sh
/etc
```

`diskless` 脚本创建内存文件系统来保存被覆盖的目录。默认只创建 5MB 的分区，可能不足以满足你的需求。要覆盖此设置，可以创建文件 **/conf/base/etc/md_size**，其中包含要为该目录创建的内存磁盘大小（以 512 字节扇区为单位）。

然后你通常在 **/conf/default/etc** 目录中提供逐文件覆盖。至少必须通过 **/conf/default/etc/fstab**、**/conf/default/etc/rc.conf** 和 **/conf/default/etc/rc.local** 为 **/etc/fstab**、**/etc/rc.conf** 和 **/etc/rc.local** 提供覆盖。

覆盖是分层的。你可以在 **/conf/<BROADCASTIP>/etc** 目录中提供特定于网络的默认值，其中 <BROADCASTIP> 表示通过 BOOTP 获得的 `diskless` 系统的广播 IP 地址。`diskless_remount` 和 `md_size` 功能可在任何这些目录中使用。配置功能也适用于 **/etc** 以外的目录，只需在 **/conf/{base,default,<broadcast>,<ip>}/\*** 中创建要替换或覆盖的目录，并按处理 **/etc** 的方式处理即可。

由于你通常使用 **/conf/base/etc/diskless_remount** 克隆服务器的 **/etc**，你可能希望从内存文件系统中删除不需要的文件。例如，如果服务器有防火墙而你没有，你可能希望删除 **/etc/ipfw.conf**。可以通过创建 **/conf/base/<DIRECTORY>.remove** 文件来实现。例如，**/conf/base/etc.remove** 包含引导脚本应从内存文件系统中删除的相对路径列表。

至少，你通常需要在 **/conf/default/etc/fstab** 中包含以下内容：

```sh
<SERVER>:<ROOT> /     nfs    ro 0 0
<SERVER>:/usr   /usr  nfs    ro 0 0
```

你还需要创建自定义版本的 **/conf/default/etc/rc.conf**，其中应包含 `diskless` 客户端的启动选项，以及 **/conf/default/etc/rc.local**（可以为空，但能防止服务器自身的 **/etc/rc.local** 泄漏到 `diskless` 系统）。

在 `rc.conf` 中，你很可能不需要设置 `hostname` 和 `ifconfig_*`，因为这些将由启动代码设置。最后，如果多个 `diskless` 客户端共享相同的配置文件，使用以 `` `hostname` `` 作为切换变量的 `case` 语句进行特定于机器的配置可能会很方便。

- `diskless` 客户端的内核将通过 NFS 或 TFTP 加载，必须包含对 NFS 客户端的支持：

```sh
options NFSCL
options NFS_ROOT
```

如果你使用的引导机制不通过内核环境将网络配置传递给内核，还需要包含以下选项：

```sh
options BOOTP
options BOOTP_NFSROOT
options BOOTP_COMPAT
```

*注意：* PXE 环境不需要这些选项。

`diskless` 引导环境依赖内存支持的文件系统来支持临时本地存储，以防根文件系统以只读方式挂载；因此，需要在内核配置的 device 部分添加以下内容：

```sh
device md
```

如果你使用防火墙，请记住默认设置为 "open"，否则你的内核将无法发送/接收 BOOTP 数据包。

## 安全问题

请注意，使用未加密的 NFS 挂载根分区和用户分区可能会暴露加密密钥等信息。

## 参见

[ethers(5)](../man5/ethers.5.md), exports(5), [make.conf(5)](../man5/make.conf.5.md), bootpd(8), mountd(8), nfsd(8), pxeboot(8), [reboot(8)](reboot.8.md), [tftpd(8)](tftpd.8.md)

**ports/net/etherboot**

## 历史

`diskless` 环境首次出现于 FreeBSD 2.2.5。

## 缺陷

本手册页可能不完整。

FreeBSD 有时需要写入根分区，因此启动脚本会在某些位置（例如 **/etc** 和 **/var**）挂载 MFS 文件系统，同时尝试保留原始内容。该过程可能无法处理所有情况。
