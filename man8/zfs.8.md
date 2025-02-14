  ZFS(8)  

ZFS(8)

FreeBSD System Manager's Manual

ZFS(8)

[名称](#__u540D___u79F0_)
=======================

`zfs` —

配置 ZFS 文件系统

[概要](#__u6982___u8981_)
=======================

`zfs` `-?V` `zfs` `version` `zfs` `<subcommand>` \[<args>\]

[描述](#__u63CF___u8FF0_)
=======================

`zfs` 命令在 ZFS 存储池中配置 ZFS 数据集，如 zpool(8) 中所述。 数据集由 ZFS 命名空间内的唯一路径标识。例如：

pool/{filesystem,volume,snapshot} 

其中数据集名称的最大长度为 `MAXNAMELEN` (256 字节) ，路径中允许的最大嵌套量为 50 级深度。

数据集可以是以下之一：

**file system**

**filesystem** 的 ZFS 数据集可以挂载在标准系统命名空间中，并且其行为类似于其他文件系统。 虽然 ZFS 文件系统被设计为与 POSIX 兼容，但在某些情况下存在妨碍遵从性的已知问题。 在检查文件系统可用空间时，依赖于标准一致性的应用程序可能会由于非标准行为而失败。

**volume**

导出为原始设备或块设备的逻辑卷。 只有在需要块设备时才应使用这种类型的数据集。 文件系统通常用于大多数环境。

**snapshot**

给定时间点的文件系统或卷的只读版本。 它被指定为 filesystem@name 或 volume@name 。

**bookmark**

很像 **snapshot** ，但没有保留磁盘数据。 它可以用作发送源（但不能用作接收源）。 它被指定为 filesystem#name 或 volume#name 。

有关详细信息，请参阅 zfsconcepts(8) 。

[特性](#__u7279___u6027_)
-----------------------

属性分为两种类型，原生属性和用户定义 (或 “user”) 属性。 本机属性要么导出内部统计信息，要么控制 ZFS 行为。 此外，本机属性要么是可编辑的，要么是只读的。 用户属性对 ZFS 行为没有影响，但您可以使用它们以在您的环境中有意义的方式注释数据集。 有关属性的更多信息，请参见 zfsprops(8) 手册页。

[加密](#__u52A0___u5BC6_)
-----------------------

启用 **encryption** 功能允许创建加密的文件系统和卷。 ZFS 将加密文件和 zvol 数据、文件属性、ACL、权限位、目录列表、FUID 映射和 **userused** / **groupused** 数据。 有关加密的概述，请参见 zfs-load-key(8) 命令手册。

[子命令](#__u5B50___u547D___u4EE4_)
================================

所有修改状态的子命令都以其原始形式永久记录到池中。

`zfs` `-`?

显示帮助消息。

`zfs` `-V`, `--version`

`zfs` `version` 子命令的别名。

`zfs` `version`

显示 `zfs` 用户空间实用程序和 zfs 内核模块的软件版本。

[数据集管理](#__u6570___u636E___u96C6___u7BA1___u7406_)
--------------------------------------------------

zfs-list(8)

以表格形式列出给定数据集的属性信息。

zfs-create(8)

创建新的 ZFS 文件系统或卷。

zfs-destroy(8)

销毁给定的数据集、快照或书签。

zfs-rename(8)

重命名给定的数据集（文件系统或快照）。

zfs-upgrade(8)

管理升级文件系统的磁盘版本。

[快照](#__u5FEB___u7167_)
-----------------------

zfs-snapshot(8)

创建具有给定名称的快照。

zfs-rollback(8)

将给定的数据集回滚到以前的快照。

zfs-hold(8) / zfs-release(8)

添加或删除对指定快照或快照的保留引用。 如果快照上存在保留，则尝试使用 `zfs` `destroy` 命令销毁该快照会返回 `EBUSY` 。

zfs-diff(8)

显示给定文件系统的快照与该文件系统稍后的另一个快照或文件系统的当前内容之间的差异。

[克隆](#__u514B___u9686_)
-----------------------

zfs-clone(8)

创建给定快照的克隆。

zfs-promote(8)

提升克隆文件系统不再依赖于其 “origin” 快照。

[发送和接收](#__u53D1___u9001___u548C___u63A5___u6536_)
--------------------------------------------------

zfs-send(8)

生成一个发送流，它可能是一个文件系统，并且可能是一个书签的增量。

zfs-receive(8)

创建一个快照，其内容在标准输入提供的流中指定。 如果接收到一个完整的流，那么也会创建一个新的文件系统。 流是使用 zfs-send(8) 子命令创建的，默认情况下会创建一个完整的流。

zfs-bookmark(8)

创建给定快照或书签的新书签。 书签标记创建快照的时间点，并可用作 `zfs` `send` 命令的增量源。

zfs-redact(8)

生成一个新的修订书签。 此功能可用于允许文件系统的克隆在远程系统上可用，以防它们的父级不需要（或不需要）可用。

[特性](#__u7279___u6027__2)
-------------------------

zfs-get(8)

显示给定数据集的属性。

zfs-set(8)

将属性或属性列表设置为每个数据集的给定值。

zfs-inherit(8)

清除指定的属性，使其从祖先继承，如果没有祖先设置属性，则恢复为默认值，或者使用 `-S` 选项恢复为接收到的值（如果存在）。

[配额](#__u914D___u989D_)
-----------------------

zfs-userspace(8) / zfs-groupspace(8) / zfs-projectspace(8)

显示指定文件系统或快照中的每个用户、组或项目消耗的空间和配额。

zfs-project(8)

列出、设置或清除项目 ID 和/或继承文件或目录上的标志。

[挂载点](#__u6302___u8F7D___u70B9_)
--------------------------------

zfs-mount(8)

显示当前挂载的所有 ZFS 文件系统，或将 ZFS 文件系统挂载到由其 **mountpoint** 属性描述的路径上。

zfs-unmount(8)

卸载当前挂载的 ZFS 文件系统。

[分享](#__u5206___u4EAB_)
-----------------------

zfs-share(8)

共享可用的 ZFS 文件系统。

zfs-unshare(8)

取消共享当前共享的 ZFS 文件系统。

[委托管理](#__u59D4___u6258___u7BA1___u7406_)
-----------------------------------------

zfs-allow(8)

委派指定文件系统或卷的权限。

zfs-unallow(8)

删除指定文件系统或卷上的委派权限。

[加密](#__u52A0___u5BC6__2)
-------------------------

zfs-change-key(8)

在指定数据集上添加或更改加密密钥。

zfs-load-key(8)

加载指定加密数据集的密钥，启用访问。

zfs-unload-key(8)

卸载指定数据集的密钥，删除访问数据集的能力。

[频道节目](#__u9891___u9053___u8282___u76EE_)
-----------------------------------------

zfs-program(8)

通过 Lua 脚本语言通道程序以编程方式执行 ZFS 管理操作。

[Jails](#Jails)
---------------

zfs-jail(8)

将文件系统附加到 jail 。

zfs-unjail(8)

从 jail 中分离文件系统。

[等待](#__u7B49___u5F85_)
-----------------------

zfs-wait(8)

等待文件系统中的后台活动完成。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

`zfs` 实用程序在成功时退出 0，如果发生错误则退出 1，如果指定了无效的命令行选项，则退出 2。

[实例](#__u5B9E___u4F8B_)
=======================

**创建 ZFS 文件系统层次结构**

以下命令创建一个名为 _pool/home_ 的文件系统和一个名为 _pool/home/bob_ 的文件系统。 挂载点 /export/home 是为父文件系统设置的，并由子文件系统自动继承。

\# zfs create pool/home # zfs set mountpoint=/export/home pool/home # zfs create pool/home/bob 

**示例 2 创建 ZFS 快照**

以下命令创建一个名为 **yesterday** 的快照。 此快照按需挂载在 .zfs/snapshot 文件系统根目录的 _pool/home/bob_ 目录中。

\# zfs snapshot pool/home/bob@yesterday 

**示例 3 创建和销毁多个快照**

以下命令创建名为 **yesterday** 的 _pool/home_ 及其所有后代文件系统的快照。 每个快照都按需挂载在其文件系统根目录的 .zfs/snapshot 目录中。 第二个命令销毁新创建的快照。

\# zfs snapshot -r pool/home@yesterday # zfs destroy -r pool/home@yesterday 

**示例 4 禁用和启用文件系统压缩**

以下命令禁用 _pool/home_ 下所有文件系统的 **compression** 属性。 下一个命令显式启用 _pool/home/anne_ 的 **compression** 。

\# zfs set compression=off pool/home # zfs set compression=on pool/home/anne 

**示例 5 列出 ZFS 数据集**

以下命令列出系统中所有活动的文件系统和卷。 如果 **listsnaps** 属性 **on** ，则会显示快照。 默认为 **off** 。 有关池属性的更多信息，请参阅 zpool(8) 。

\# zfs list NAME USED AVAIL REFER MOUNTPOINT pool 450K 457G 18K /pool pool/home 315K 457G 21K /export/home pool/home/anne 18K 457G 18K /export/home/anne pool/home/bob 276K 457G 276K /export/home/bob 

**示例 6 在 ZFS 文件系统上设置配额**

以下命令为 _pool/home/bob_ 设置了 50 GB 的配额。

\# zfs set quota=50G pool/home/bob 

**示例 7 列出 ZFS 属性**

以下命令列出了 _pool/home/bob_ 的所有属性。

\# zfs get all pool/home/bob NAME PROPERTY VALUE SOURCE pool/home/bob type filesystem - pool/home/bob creation Tue Jul 21 15:53 2009 - pool/home/bob used 21K - pool/home/bob available 20.0G - pool/home/bob referenced 21K - pool/home/bob compressratio 1.00x - pool/home/bob mounted yes - pool/home/bob quota 20G local pool/home/bob reservation none default pool/home/bob recordsize 128K default pool/home/bob mountpoint /pool/home/bob default pool/home/bob sharenfs off default pool/home/bob checksum on default pool/home/bob compression on local pool/home/bob atime on default pool/home/bob devices on default pool/home/bob exec on default pool/home/bob setuid on default pool/home/bob readonly off default pool/home/bob zoned off default pool/home/bob snapdir hidden default pool/home/bob acltype off default pool/home/bob aclmode discard default pool/home/bob aclinherit restricted default pool/home/bob canmount on default pool/home/bob xattr on default pool/home/bob copies 1 default pool/home/bob version 4 - pool/home/bob utf8only off - pool/home/bob normalization none - pool/home/bob casesensitivity sensitive - pool/home/bob vscan off default pool/home/bob nbmand off default pool/home/bob sharesmb off default pool/home/bob refquota none default pool/home/bob refreservation none default pool/home/bob primarycache all default pool/home/bob secondarycache all default pool/home/bob usedbysnapshots 0 - pool/home/bob usedbydataset 21K - pool/home/bob usedbychildren 0 - pool/home/bob usedbyrefreservation 0 - 

以下命令获取单个属性值。

\# zfs get -H -o value compression pool/home/bob on 

以下命令列出了具有 _pool/home/bob_ 本地设置的所有属性。

\# zfs get -r -s local -o name,property,value all pool/home/bob NAME PROPERTY VALUE pool/home/bob quota 20G pool/home/bob compression on 

**示例 8 回滚 ZFS 文件系统**

以下命令将 _pool/home/anne_ 的内容恢复为 **yesterday** 命名的快照，删除所有中间快照。

\# zfs rollback -r pool/home/anne@yesterday 

**示例 9 创建 ZFS 克隆**

以下命令创建一个可写文件系统，其初始内容与 _pool/home/bob@yesterday_ 相同。

\# zfs clone pool/home/bob@yesterday pool/clone 

**示例 10 升级 ZFS 克隆**

以下命令说明了如何测试对文件系统的更改，然后使用克隆、克隆提升和重命名将原始文件系统替换为更改后的文件系统：

\# zfs create pool/project/production populate /pool/project/production with data # zfs snapshot pool/project/production@today # zfs clone pool/project/production@today pool/project/beta make changes to /pool/project/beta and test them # zfs promote pool/project/beta # zfs rename pool/project/production pool/project/legacy # zfs rename pool/project/beta pool/project/production once the legacy version is no longer needed, it can be destroyed # zfs destroy pool/project/legacy 

**示例 11 继承 ZFS 属性**

以下命令导致 _pool/home/bob_ 和 _pool/home/anne_ 从其父级继承 **checksum** 和属性。

\# zfs inherit checksum pool/home/bob pool/home/anne 

**示例 12 远程复制 ZFS 数据**

以下命令发送一个完整的流，然后将一个增量流发送到远程机器，分别将它们恢复到 _poolB/received/fs@a_ 和 _poolB/received/fs@b_ 中。 _poolB_ 必须包含文件系统 _poolB/received_, 并且最初不得包含 _poolB/received/fs_ 。

\# zfs send pool/fs@a | \\ ssh host zfs receive poolB/received/fs@a # zfs send -i a pool/fs@b | \\ ssh host zfs receive poolB/received/fs 

**示例 13 使用 zfs receive -d 选项**

以下命令将 _poolA/fsA/fsB@snap_ 的完整流发送到远程计算机，并将其接收到 _poolB/received/fsA/fsB@snap_ 中。 接收到的快照名称的 _fsA/fsB@snap_ 部分由发送的快照名称确定。 _poolB_ 必须包含文件系统 _poolB/received_ 。 如果 _poolB/received/fsA_ 不存在，则将其创建为空文件系统。

\# zfs send poolA/fsA/fsB@snap | \\ ssh host zfs receive -d poolB/received 

**示例 14 设置用户属性**

以下示例为数据集设置用户定义的 **com.example:department** 属性。

\# zfs set com.example:department=12345 tank/accounting 

**示例 15 执行滚动快照**

以下示例显示如何使用一致的命名方案维护快照历史记录。 为了保留一周的快照，用户销毁最旧的快照，重命名剩余的快照，然后创建一个新快照，如下所示：

\# zfs destroy -r pool/users@7daysago # zfs rename -r pool/users@6daysago @7daysago # zfs rename -r pool/users@5daysago @6daysago # zfs rename -r pool/users@4daysago @5daysago # zfs rename -r pool/users@3daysago @4daysago # zfs rename -r pool/users@2daysago @3daysago # zfs rename -r pool/users@yesterday @2daysago # zfs rename -r pool/users@today @yesterday # zfs snapshot -r pool/users@today 

**示例 16 在 ZFS 文件系统上设置 sharenfs 属性选项**

以下命令显示如何设置 **sharenfs** 属性选项以启用对一组 **IP** 地址的 **rw** 访问，并为 _tank/home_ 文件系统上的系统 **neo** 启用 root 访问。

\# zfs set sharenfs='rw=@123.123.0.0/16,root=neo' tank/home 

如果您使用 **DNS** 进行主机名解析，请指定完全限定的主机名。

**示例 17 委派 ZFS 数据集上的 ZFS 管理权限**

以下示例显示如何设置权限，以便用户 **cindys** 可以在 _tank/cindys_ 上创建、销毁、挂载和拍摄快照。 还显示了 _tank/cindys_ 的权限。

\# zfs allow cindys create,destroy,mount,snapshot tank/cindys # zfs allow tank/cindys ---- Permissions on tank/cindys -------------------------------------- Local+Descendent permissions: user cindys create,destroy,mount,snapshot 

因为 _tank/cindys_ 挂载点权限默认设置为 755，所以用户 **cindys** 将无法挂载 _tank/cindys_ 下的文件系统。 添加类似于以下语法的 ACE 以提供挂载点访问：

\# chmod A+user:cindys:add\_subdirectory:allow /tank/cindys 

**示例 18 委派 ZFS 数据集上的创建时间权限**

以下示例显示如何授予组 **staff** 人员中的任何人在 _tank/users_ 中创建文件系统。 此语法还允许工作人员破坏他们自己的文件系统，但不能破坏任何其他人的文件系统。 还显示了 _tank/users_ 的权限。

\# zfs allow staff create,mount tank/users # zfs allow -c destroy tank/users # zfs allow tank/users ---- Permissions on tank/users --------------------------------------- Permission sets: destroy Local+Descendent permissions: group staff create,mount 

**示例 19 在 ZFS 数据集上定义和授予权限集**

以下示例显示了如何在 _tank/users_ 文件系统上定义和授予权限集。 还显示了 _tank/users_ 的权限。

\# zfs allow -s @pset create,destroy,snapshot,mount tank/users # zfs allow staff @pset tank/users # zfs allow tank/users ---- Permissions on tank/users --------------------------------------- Permission sets: @pset create,destroy,mount,snapshot Local+Descendent permissions: group staff @pset 

**示例 20 委派 ZFS 数据集的属性权限**

以下示例显示授予在 _users/home_ 文件系统上设置配额和保留的能力。 _users/home_ 的权限也会显示。

\# zfs allow cindys quota,reservation users/home # zfs allow users/home ---- Permissions on users/home --------------------------------------- Local+Descendent permissions: user cindys quota,reservation cindys% zfs set quota=10G users/home/marks cindys% zfs get quota users/home/marks NAME PROPERTY VALUE SOURCE users/home/marks quota 10G local 

**示例 21 删除 ZFS 数据集上的 ZFS 委派权限**

以下示例显示如何从 _tank/users_ 文件系统上的 **staff** 组中删除快照权限。 还显示了 _tank/users_ 的权限。

\# zfs unallow staff snapshot tank/users # zfs allow tank/users ---- Permissions on tank/users --------------------------------------- Permission sets: @pset create,destroy,mount,snapshot Local+Descendent permissions: group staff @pset 

**示例 22 显示快照和 ZFS 数据集之间的差异**

以下示例显示了如何查看 ZFS 数据集的先前快照与其当前状态之间发生的变化。 `-F` 选项用于指示受影响文件的类型信息。

\# zfs diff -F tank/test@before tank/test M / /tank/test/ M F /tank/test/linked (+1) R F /tank/test/oldname -> /tank/test/newname - F /tank/test/deleted + F /tank/test/created M F /tank/test/modified 

**示例 23 创建书签**

以下示例为快照创建书签。 然后可以使用此书签代替发送流中的快照。

\# zfs bookmark rpool@snapshot rpool#bookmark 

**示例 24 在 ZFS 文件系统上设置 sharemb 属性选项**

以下示例展示了如何通过 ZFS 共享 SMB 文件系统。 请注意，必须提供用户及其密码。

\# smbmount //127.0.0.1/share\_tmp /mnt/tmp \\ -o user=workgroup/turbo,password=obrut,uid=1000 

需要最少的 _/etc/samba/smb.conf_ 配置：

Samba 需要侦听“localhost”（127.0.0.1），以便 ZFS 实用程序与 Samba 通信。这是大多数 Linux 发行版的默认行为。

Samba 必须能够对用户进行身份验证。 这可以通过多种方式完成，具体取决于是使用系统密码文件、LDAP 还是 Samba 特定的 smbpasswd 文件。 如何执行此操作超出了本手册的范围。 有关更多信息，请参阅 smb.conf(5) 手册页。

请参阅 smb.conf(5) 手册页的 **USERSHARE section** 部分了解所有配置选项，以防您之后需要修改共享的任何选项。 请注意，如果共享未共享（例如在重新启动时等），则使用 net(8) 命令所做的任何更改都将被撤消。

[环境变量](#__u73AF___u5883___u53D8___u91CF_)
=========================================

[`ZFS_MOUNT_HELPER`](#ZFS_MOUNT_HELPER)

导致 `zfs mount` 使用 _/bin/mount_ 来挂载 zfs 数据集。 提供此选项是为了向后兼容较旧的 zfs 版本。

[接口稳定性](#__u63A5___u53E3___u7A33___u5B9A___u6027_)
==================================================

**坚定的。**

[参见](#__u53C2___u89C1_)
=======================

attr(1), gzip(1), ssh(1), chmod(2), fsync(2), stat(2), write(2), acl(5), attributes(5), exports(5), exportfs(8), mount(8), net(8), selinux(8), zfs-allow(8), zfs-bookmark(8), zfs-change-key(8), zfs-clone(8), zfs-create(8), zfs-destroy(8), zfs-diff(8), zfs-get(8), zfs-groupspace(8), zfs-hold(8), zfs-inherit(8), zfs-jail(8), zfs-list(8), zfs-load-key(8), zfs-mount(8), zfs-program(8), zfs-project(8), zfs-projectspace(8), zfs-promote(8), zfs-receive(8), zfs-redact(8), zfs-release(8), zfs-rename(8), zfs-rollback(8), zfs-send(8), zfs-set(8), zfs-share(8), zfs-snapshot(8), zfs-unallow(8), zfs-unjail(8), zfs-unload-key(8), zfs-unmount(8), zfs-unshare(8), zfs-upgrade(8), zfs-userspace(8), zfs-wait(8), zfsconcepts(8), zfsprops(8), zpool(8)

June 30, 2019

FreeBSD 13.1-RELEASE