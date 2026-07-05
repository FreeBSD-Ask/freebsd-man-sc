# zfs.8

`zfs` — 配置 ZFS 数据集

## 名称

`zfs`

## 概要

`zfs -?V`

`zfs version [-j]`

`zfs subcommand [arguments]`

## 描述

`zfs` 命令用于在 ZFS 存储池中配置 ZFS 数据集，如 zpool(8) 所述。数据集由 ZFS 命名空间中的唯一路径标识：

`pool`[`/component`]/`component`

例如：

```sh
rpool/var/log
```

数据集名称的最大长度为 `ZFS_MAX_DATASET_NAME_LEN` - 1 个 ASCII 字符（当前为 255），且须满足 `[A-Za-z_.:/ -]`。此外，快照允许包含单个 `@` 字符，而书签允许包含单个 `#` 字符。`/` 用作组件之间的分隔符。路径中允许的最大嵌套层数为 `zfs_max_dataset_nesting` 层。ZFS 可调参数（`zfs_*`）在 zfs(4) 中说明。

数据集可以是以下类型之一：

**file system** 可挂载到标准系统命名空间中，行为与其他文件系统类似。虽然 ZFS 文件系统设计为符合 POSIX，但存在已知问题导致在某些情况下不符合标准。依赖标准一致性的应用程序可能会在检查文件系统可用空间时因非标准行为而失败。

**volume** 作为原始或块设备导出的逻辑卷。此类数据集仅应在需要块设备时使用。在大多数环境中通常使用文件系统。

**snapshot** 文件系统或卷在给定时间点的只读版本。指定为 `filesystem`@`name` 或 `volume`@`name`。

**bookmark** 类似于 **snapshot**，但不保留磁盘数据。它可用作发送的源（但不能用于接收）。指定为 `filesystem`#`name` 或 `volume`#`name`。

有关详细信息，请参见 zfsconcepts(7)。

### 属性

属性分为两种类型：原生属性和用户定义（或“用户”）属性。原生属性要么导出内部统计信息，要么控制 ZFS 行为。此外，原生属性要么可编辑，要么为只读。用户属性对 ZFS 行为没有影响，但你可以用它们以对你环境有意义的方式注释数据集。有关属性的更多信息，请参见 zfsprops(7)。

### 加密

启用 **encryption** 功能允许创建加密的文件系统和卷。ZFS 将加密文件和 zvol 数据、文件属性、ACL、权限位、目录列表、FUID 映射，以及 **userused**/**groupused**/**projectused** 数据。有关加密的概述，请参见 zfs-load-key(8)。

## 子命令

所有修改状态的子命令都以其原始形式持久记录到池中。

**`zfs`** `-?` 显示帮助消息。

**`zfs`** `-V, --version`

**`zfs`** `version` [`-j`] 显示 `zfs` 用户空间工具和 zfs 内核模块的软件版本。使用 `-j` 选项以 JSON 格式输出。

### 数据集管理

**zfs-list(8)** 以表格形式列出给定数据集的属性信息。

**zfs-create(8)** 创建新的 ZFS 文件系统或卷。

**zfs-destroy(8)** 销毁给定的数据集、快照或书签。

**zfs-rename(8)** 重命名给定的数据集（文件系统或快照）。

**zfs-upgrade(8)** 管理文件系统磁盘上版本的升级。

### 快照

**zfs-snapshot(8)** 使用给定名称创建快照。

**zfs-rollback(8)** 将给定数据集回滚到先前的快照。

**zfs-hold(8)/zfs-release(8)** 向指定的一个或多个快照添加或删除保留引用。如果快照上存在保留，则使用 `zfs destroy` 命令销毁该快照的尝试将返回 `EBUSY`。

**zfs-diff(8)** 显示给定文件系统的快照与该文件系统后续时间的另一个快照或文件系统当前内容之间的差异。

### 克隆

**zfs-clone(8)** 创建给定快照的克隆。

**zfs-promote(8)** 将克隆文件系统提升，使其不再依赖于其“origin”快照。

### 发送和接收

**zfs-send(8)** 生成发送流，可以是文件系统的，也可以是从书签增量的。

**zfs-receive(8)** 创建一个快照，其内容与标准输入上提供的流中指定的内容相同。如果接收到完整流，则还会创建新文件系统。流是使用 zfs-send(8) 子命令创建的，默认创建完整流。

**zfs-bookmark(8)** 创建给定快照或书签的新书签。书签标记快照创建时的时间点，可用作 `zfs send` 命令的增量源。

**zfs-redact(8)** 生成新的修订书签。此功能可用于允许在远程系统上使用文件系统的克隆，前提是其父级不需要（或需要不）可用。

### 属性

**zfs-get(8)** 显示给定数据集的属性。

**zfs-set(8)** 为每个数据集将属性或属性列表设置为给定值。

**zfs-inherit(8)** 清除指定属性，使其从祖先继承，如果没有祖先设置该属性则恢复为默认值，或使用 `-S` 选项恢复为接收值（如果存在）。

### 配额

**zfs-userspace(8)/zfs-groupspace(8)/zfs-projectspace(8)** 显示指定文件系统或快照中每个用户、组或项目消耗的空间和配额。

**zfs-project(8)** 列出、设置或清除文件或目录的项目 ID 和/或继承标志。

### 挂载点

**zfs-mount(8)** 显示当前已挂载的所有 ZFS 文件系统，或将 ZFS 文件系统挂载到由其 **mountpoint** 属性描述的路径上。

**zfs-unmount(8)** 卸载当前已挂载的 ZFS 文件系统。

### 共享

**zfs-share(8)** 共享可用的 ZFS 文件系统。

**zfs-unshare(8)** 取消共享当前已共享的 ZFS 文件系统。

### 委托管理

**zfs-allow(8)** 在指定的文件系统或卷上委托权限。

**zfs-unallow(8)** 在指定的文件系统或卷上移除委托的权限。

### 加密

**zfs-change-key(8)** 在指定数据集上添加或更改加密密钥。

**zfs-load-key(8)** 加载指定加密数据集的密钥，启用访问。

**zfs-unload-key(8)** 卸载指定数据集的密钥，移除访问该数据集的能力。

### 通道程序

**zfs-program(8)** 通过 Lua 脚本语言通道程序以编程方式执行 ZFS 管理操作。

### 数据重写

**zfs-rewrite(8)** 不修改地重写指定文件。

### Jail

**zfs-jail(8)** 将文件系统附加到 jail。

**zfs-unjail(8)** 从 jail 分离文件系统。

### 等待

**zfs-wait(8)** 等待文件系统中的后台活动完成。

## 退出状态

`zfs` 工具成功时退出 **0**，发生错误时退出 **1**，指定了无效命令行选项时退出 **2**。

## 实例

### 示例 1：创建 ZFS 文件系统层次结构

以下命令创建名为 `pool/home` 的文件系统和名为 `pool/home/bob` 的文件系统。为父文件系统设置挂载点 **/export/home**，子文件系统会自动继承。

```sh
# zfs create pool/home
# zfs set mountpoint=/export/home pool/home
# zfs create pool/home/bob
```

### 示例 2：创建 ZFS 快照

以下命令创建名为 `yesterday` 的快照。此快照按需挂载到 `pool/home/bob` 文件系统根目录的 `.zfs/snapshot` 目录中。

```sh
# zfs snapshot pool/home/bob@yesterday
```

### 示例 3：创建和销毁多个快照

以下命令为 `pool/home` 及其所有后代文件系统创建名为 `yesterday` 的快照。每个快照按需挂载到其文件系统根目录的 `.zfs/snapshot` 目录中。第二条命令销毁新创建的快照。

```sh
# zfs snapshot -r pool/home@yesterday
# zfs destroy -r pool/home@yesterday
```

### 示例 4：禁用和启用文件系统压缩

以下命令禁用 `pool/home` 下所有文件系统的 **compression** 属性。下一条命令显式启用 `pool/home/anne` 的 **compression**。

```sh
# zfs set compression=off pool/home
# zfs set compression=on pool/home/anne
```

### 示例 5：列出 ZFS 数据集

以下命令列出系统中所有活动的文件系统和卷。如果 **listsnaps**=**on**，则显示快照。默认为 **off**。有关池属性的更多信息，请参见 zpoolprops(7)。

```sh
# zfs list
NAME                      USED  AVAIL  REFER  MOUNTPOINT
pool                      450K   457G    18K  /pool
pool/home                 315K   457G    21K  /export/home
pool/home/anne             18K   457G    18K  /export/home/anne
pool/home/bob             276K   457G   276K  /export/home/bob
```

### 示例 6：在 ZFS 文件系统上设置配额

以下命令为 `pool/home/bob` 设置 50 GB 的配额：

```sh
# zfs set quota=50G pool/home/bob
```

### 示例 7：列出 ZFS 属性

以下命令列出 `pool/home/bob` 的所有属性：

```sh
# zfs get all pool/home/bob
NAME           PROPERTY              VALUE                  SOURCE
pool/home/bob  type                  filesystem             -
pool/home/bob  creation              Tue Jul 21 15:53 2009  -
pool/home/bob  used                  21K                    -
pool/home/bob  available             20.0G                  -
pool/home/bob  referenced            21K                    -
pool/home/bob  compressratio         1.00x                  -
pool/home/bob  mounted               yes                    -
pool/home/bob  quota                 20G                    local
pool/home/bob  reservation           none                   default
pool/home/bob  recordsize            128K                   default
pool/home/bob  mountpoint            /pool/home/bob         default
pool/home/bob  sharenfs              off                    default
pool/home/bob  checksum              on                     default
pool/home/bob  compression           on                     local
pool/home/bob  atime                 on                     default
pool/home/bob  devices               on                     default
pool/home/bob  exec                  on                     default
pool/home/bob  setuid                on                     default
pool/home/bob  readonly              off                    default
pool/home/bob  zoned                 off                    default
pool/home/bob  snapdir               hidden                 default
pool/home/bob  acltype               off                    default
pool/home/bob  aclmode               discard                default
pool/home/bob  aclinherit            restricted             default
pool/home/bob  canmount              on                     default
pool/home/bob  xattr                 on                     default
pool/home/bob  copies                1                      default
pool/home/bob  version               4                      -
pool/home/bob  utf8only              off                    -
pool/home/bob  normalization         none                   -
pool/home/bob  casesensitivity       sensitive              -
pool/home/bob  vscan                 off                    default
pool/home/bob  nbmand                off                    default
pool/home/bob  sharesmb              off                    default
pool/home/bob  refquota              none                   default
pool/home/bob  refreservation        none                   default
pool/home/bob  primarycache          all                    default
pool/home/bob  secondarycache        all                    default
pool/home/bob  usedbysnapshots       0                      -
pool/home/bob  usedbydataset         21K                    -
pool/home/bob  usedbychildren        0                      -
pool/home/bob  usedbyrefreservation  0                      -
```

以下命令获取单个属性值：

```sh
# zfs get -H -o value compression pool/home/bob
on
```

以下命令列出 `pool/home/bob` 的所有本地设置属性：

```sh
# zfs get -r -s local -o name,property,value all pool/home/bob
NAME           PROPERTY              VALUE
pool/home/bob  quota                 20G
pool/home/bob  compression           on
```

### 示例 8：回滚 ZFS 文件系统

以下命令将 `pool/home/anne` 的内容回滚到名为 `yesterday` 的快照，删除所有中间快照：

```sh
# zfs rollback -r pool/home/anne@yesterday
```

### 示例 9：创建 ZFS 克隆

以下命令创建一个可写文件系统，其初始内容与 `pool/home/bob@yesterday` 相同。

```sh
# zfs clone pool/home/bob@yesterday pool/clone
```

### 示例 10：提升 ZFS 克隆

以下命令演示如何使用克隆、克隆提升和重命名来测试对文件系统的更改，然后用更改后的文件系统替换原始文件系统：

```sh
# zfs create pool/project/production
  populate /pool/project/production with data
# zfs snapshot pool/project/production@today
# zfs clone pool/project/production@today pool/project/beta
  make changes to /pool/project/beta and test them
# zfs promote pool/project/beta
# zfs rename pool/project/production pool/project/legacy
# zfs rename pool/project/beta pool/project/production
  once the legacy version is no longer needed, it can be destroyed
# zfs destroy pool/project/legacy
```

### 示例 11：继承 ZFS 属性

以下命令使 `pool/home/bob` 和 `pool/home/anne` 从其父级继承 **checksum** 属性。

```sh
# zfs inherit checksum pool/home/bob pool/home/anne
```

### 示例 12：远程复制 ZFS 数据

以下命令向远程机器发送完整流，然后发送增量流，分别恢复为 *poolB/received/fs@a* 和 *poolB/received/fs@b*。*poolB* 必须包含文件系统 *poolB/received*，且最初不得包含 *poolB/received/fs*。

```sh
# zfs send pool/fs@a |
ssh host zfs receive poolB/received/fs@a
# zfs send -i a pool/fs@b |
ssh host zfs receive poolB/received/fs
```

### 示例 13：使用 zfs receive -d 选项

以下命令将 `poolA/fsA/fsB@snap` 的完整流发送到远程机器，接收到 `poolB/received/fsA/fsB@snap`。接收到的快照名称中的 `fsA/fsB@snap` 部分由所发送快照的名称确定。`poolB` 必须包含文件系统 `poolB/received`。如果 `poolB/received/fsA` 不存在，则创建为空文件系统。

```sh
# zfs send poolA/fsA/fsB@snap |
ssh host zfs receive -d poolB/received
```

### 示例 14：设置用户属性

以下示例为数据集设置用户定义的 `com.example:department` 属性：

```sh
# zfs set com.example:department=12345 tank/accounting
```

### 示例 15：执行滚动快照

以下示例展示如何使用一致的命名方案维护快照历史记录。要保留一周的快照，用户销毁最旧的快照，重命名剩余的快照，然后创建新快照，如下所示：

```sh
# zfs destroy -r pool/users@7daysago
# zfs rename -r pool/users@6daysago @7daysago
# zfs rename -r pool/users@5daysago @6daysago
# zfs rename -r pool/users@4daysago @5daysago
# zfs rename -r pool/users@3daysago @4daysago
# zfs rename -r pool/users@2daysago @3daysago
# zfs rename -r pool/users@yesterday @2daysago
# zfs rename -r pool/users@today @yesterday
# zfs snapshot -r pool/users@today
```

### 示例 16：在 ZFS 文件系统上设置 sharenfs 属性选项

以下命令展示如何设置 **sharenfs** 属性选项，以为一组 IP 地址启用读写访问，并为系统 "neo" 启用 `tank/home` 文件系统上的 root 访问：

```sh
# zfs set sharenfs='rw=@123.123.0.0/16:[::1],root=neo' tank/home
```

如果你使用 DNS 进行主机名解析，请指定完全限定主机名。

### 示例 17：在 ZFS 数据集上委托 ZFS 管理权限

以下示例展示如何设置权限，使用户 `cindys` 可以在 `tank/cindys` 上创建、销毁、挂载和拍摄快照。还显示了 `tank/cindys` 上的权限。

```sh
# zfs allow cindys create,destroy,mount,snapshot tank/cindys
# zfs allow tank/cindys
---- Permissions on tank/cindys --------------------------------------
Local+Descendent permissions:
        user cindys create,destroy,mount,snapshot
```

由于 `tank/cindys` 挂载点权限默认设置为 755，用户 `cindys` 将无法在 `tank/cindys` 下挂载文件系统。添加类似以下语法的 ACE 以提供挂载点访问权限：

```sh
# chmod A+user:cindys:add_subdirectory:allow /tank/cindys
```

### 示例 18：在 ZFS 数据集上委托创建时权限

以下示例展示如何授予 `staff` 组中的任何人在 `tank/users` 中创建文件系统的权限。此语法还允许 staff 成员销毁自己的文件系统，但不能销毁其他人的文件系统。还显示了 `tank/users` 上的权限。

```sh
# zfs allow staff create,mount tank/users
# zfs allow -c destroy tank/users
# zfs allow tank/users
---- Permissions on tank/users ---------------------------------------
Permission sets:
        destroy
Local+Descendent permissions:
        group staff create,mount
```

### 示例 19：在 ZFS 数据集上定义和授予权限集

以下示例展示如何在 `tank/users` 文件系统上定义和授予权限集。还显示了 `tank/users` 上的权限。

```sh
# zfs allow -s @pset create,destroy,snapshot,mount tank/users
# zfs allow staff @pset tank/users
# zfs allow tank/users
---- Permissions on tank/users ---------------------------------------
Permission sets:
        @pset create,destroy,mount,snapshot
Local+Descendent permissions:
        group staff @pset
```

### 示例 20：在 ZFS 数据集上委托属性权限

以下示例展示如何授予在 `users/home` 文件系统上设置配额和保留的能力。还显示了 `users/home` 上的权限。

```sh
# zfs allow cindys quota,reservation users/home
# zfs allow users/home
---- Permissions on users/home ---------------------------------------
Local+Descendent permissions:
        user cindys quota,reservation
cindys% zfs set quota=10G users/home/marks
cindys% zfs get quota users/home/marks
NAME              PROPERTY  VALUE  SOURCE
users/home/marks  quota     10G    local
```

### 示例 21：在 ZFS 数据集上移除 ZFS 委托权限

以下示例展示如何从 **tank/users** 文件系统上的 `staff` 组移除快照权限。还显示了 **tank/users** 上的权限。

```sh
# zfs unallow staff snapshot tank/users
# zfs allow tank/users
---- Permissions on tank/users ---------------------------------------
Permission sets:
        @pset create,destroy,mount,snapshot
Local+Descendent permissions:
        group staff @pset
```

### 示例 22：显示快照与 ZFS 数据集之间的差异

以下示例展示如何查看 ZFS 数据集先前快照与其当前状态之间的变化。`-F` 选项用于指示受影响文件的类型信息。

```sh
# zfs diff -F tank/test@before tank/test
M       /       /tank/test/
M       F       /tank/test/linked      (+1)
R       F       /tank/test/oldname -> /tank/test/newname
-       F       /tank/test/deleted
+       F       /tank/test/created
M       F       /tank/test/modified
```

### 示例 23：创建书签

以下示例为快照创建书签。此书签随后可在发送流中替代快照使用。

```sh
# zfs bookmark rpool@snapshot rpool#bookmark
```

### 示例 24：在 ZFS 文件系统上设置 sharesmb 属性选项

以下示例展示如何通过 ZFS 共享 SMB 文件系统。注意必须提供用户及其密码。

```sh
# smbmount //127.0.0.1/share_tmp /mnt/tmp -o user=workgroup/turbo,password=obrut,uid=1000
```

需要最小的 **/etc/samba/smb.conf** 配置，如下所示。

Samba 需要绑定到环回接口，以便 ZFS 工具与 Samba 通信。这是大多数 Linux 发行版的默认行为。

Samba 必须能够验证用户。这可以通过多种方式完成（[passwd(5)](../man5/passwd.5.md)、LDAP、smbpasswd(5) 等）。如何执行此操作超出本文档范围——有关更多信息，请参见 smb.conf(5)。

参见 USERSHARES 章节了解所有配置选项，以防你之后需要修改共享的任何选项。请注意，如果共享被取消共享（例如通过重启），使用 net(8) 命令所做的任何更改都将被撤销。

## 环境变量

**`ZFS_COLOR`** 在 `zfs diff` 和 `zfs list` 输出中使用 ANSI 颜色。

**`ZFS_MOUNT_HELPER`** 使 `zfs mount` 使用 [mount(8)](mount.8.md) 挂载 ZFS 数据集。此选项用于与旧版 ZFS 的向后兼容。

**`ZFS_SET_PIPE_MAX`** 告知 `zfs` 为发送/接收设置最大管道大小。在 Linux 上默认禁用，原因是 Linux 管道大小处理代码中存在未修复的死锁。

**`ZFS_MODULE_TIMEOUT`** 等待 **/dev/zfs** 出现的时间（以秒为单位）。默认为 **10**，最大 **600**（10 分钟）。如果 <**0**，永久等待；如果 **0**，不等待。

## 接口稳定性

**Committed.**

## 参见

attr(1), [gzip(1)](../man1/gzip.1.md), [ssh(1)](../man1/ssh.1.md), chmod(2), fsync(2), stat(2), write(2), acl(5), attributes(5), exports(5), zfsconcepts(7), zfsprops(7), exportfs(8), [mount(8)](mount.8.md), net(8), pam_zfs_key(8), selinux(8), zfs-allow(8), zfs-bookmark(8), zfs-change-key(8), zfs-clone(8), zfs-create(8), zfs-destroy(8), zfs-diff(8), zfs-get(8), zfs-groupspace(8), zfs-hold(8), zfs-inherit(8), zfs-jail(8), zfs-list(8), zfs-load-key(8), zfs-mount(8), zfs-program(8), zfs-project(8), zfs-projectspace(8), zfs-promote(8), zfs-receive(8), zfs-redact(8), zfs-release(8), zfs-rename(8), zfs-rollback(8), zfs-send(8), zfs-set(8), zfs-share(8), zfs-snapshot(8), zfs-unallow(8), zfs-unjail(8), zfs-unload-key(8), zfs-unmount(8), zfs-unshare(8), zfs-upgrade(8), zfs-userspace(8), zfs-wait(8), zpool(8)
