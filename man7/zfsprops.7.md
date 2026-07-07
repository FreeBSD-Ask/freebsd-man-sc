# zfsprops(7)

`zfsprops` — ZFS 数据集的原生和用户定义属性

## 名称

`zfsprops`

## 描述

属性分为两种类型：原生属性和用户定义（或“用户”）属性。原生属性要么导出内部统计信息，要么控制 ZFS 行为。此外，原生属性要么可编辑，要么只读。用户属性对 ZFS 行为没有影响，但你可以用它们以对你的环境有意义的方式注释数据集。有关用户属性的更多信息，请参见下文的 Sx User Properties 章节。

### 原生属性

每个数据集都有一组属性，用于导出有关数据集的统计信息以及控制各种行为。属性从父级继承，除非被子级覆盖。某些属性仅适用于某些类型的数据集（文件系统、卷或快照）。

数值属性的值可以使用人类可读的后缀指定（例如 **k,** **KB,** **M,** **Gb,** 等等，直到 **Z** 表示 zettabyte）以下都是有效（且相等）的指定：`1536M`、`1.5g`、`1.50GB`。

非数值属性的值区分大小写，必须为小写，**mountpoint、** **sharenfs** 和 **sharesmb** 除外。

以下原生属性由有关数据集的只读统计信息组成。这些属性既不能设置，也不能继承。除非另有说明，原生属性适用于所有数据集类型。

- POSIX 名称（“joe”）
- POSIX 数字 ID（“789”）
- SID 名称（“joe.smith@mydomain”）
- SID 数字 ID（“S-1-123-456-789”）

****available**** 数据集及其所有子级可用的空间量，假设池中没有其他活动。由于空间在池内共享，可用性可能受多种因素限制，包括物理池大小、配额、预留或池中的其他数据集。此属性也可以通过其缩短的列名 **avail** 引用。

****compressratio**** 对于非快照，此数据集的 **used** 空间所达到的压缩比，以乘数表示。**used** 属性包括后代数据集，对于克隆，不包括与原始快照共享的空间。对于快照，**compressratio** 与 **refcompressratio** 属性相同。可以通过运行 `zfs` `set` **compression**=**on** `dataset` 来启用压缩。默认值为 **off。**

****createtxg**** 创建数据集的事务组（txg）。书签与其最初关联的快照具有相同的 **createtxg**。此属性适用于对快照列表进行排序，例如用于增量发送和接收。

****creation**** 创建此数据集的时间。

****clones**** 对于快照，此属性是克隆此快照的文件系统或卷的以逗号分隔的列表。克隆的 **origin** 属性是此快照。如果 **clones** 属性不为空，则此快照不能被销毁（即使使用 `-r` 或 `-f` 选项）。原始和克隆的角色可以通过使用 `zfs` `promote` 命令提升克隆来交换。

****defer_destroy**** 如果通过使用 `zfs` `destroy` `-d` 命令将快照标记为延迟销毁，则此属性为 **on**。否则，属性为 **off。**

****encryptionroot**** 对于加密数据集，指示数据集当前从哪里继承其加密密钥。为 **encryptionroot** 加载或卸载密钥将隐式加载/卸载任何继承数据集的密钥（详见 `zfs` `load-key` 和 `zfs` `unload-key`）。克隆将始终与其原始共享加密密钥。详见 zfs-load-key(8) 的 Sx Encryption 章节。

****filesystem_count**** 数据集树中此位置下存在的文件系统和卷的总数。此值仅在数据集所在的树中某处设置了 **filesystem_limit** 时可用。

****keystatus**** 指示加密密钥当前是否加载到 ZFS 中。可能的值为 **none、** **available** 和 **unavailable。** 参见 `zfs` `load-key` 和 `zfs` `unload-key`。

****guid**** 此数据集或书签的 64 位 GUID，在其整个生命周期内不变。当快照发送到另一个池时，接收到的快照具有相同的 GUID。因此，**guid** 适用于跨池标识快照。

****logicalreferenced**** 此数据集“逻辑上”可访问的空间量。参见 **referenced** 属性。逻辑空间忽略 **compression** 和 **copies** 属性的影响，给出的数量更接近应用程序看到的数据量。但是，它确实包括元数据消耗的空间。此属性也可以通过其缩短的列名 **lrefer** 引用。

****logicalused**** 此数据集及其所有后代“逻辑上”消耗的空间量。参见 **used** 属性。逻辑空间忽略 **compression** 和 **copies** 属性的影响，给出的数量更接近应用程序看到的数据量。但是，它确实包括元数据消耗的空间。此属性也可以通过其缩短的列名 **lused** 引用。

****mounted**** 对于文件系统，指示文件系统当前是否已挂载。此属性可以为 **yes** 或 **no。**

****objsetid**** 池中此数据集的唯一标识符。与数据集的 **guid** 不同，当快照通过发送/接收操作复制到其他池时，数据集的 **objsetid** 不会传输到其他池。数据集删除后，**objsetid** 可以重用（用于新数据集）。

****origin**** 对于克隆文件系统或卷，创建克隆所用的快照。另请参见 **clones** 属性。

****receive_resume_token**** 对于具有从 `zfs` `receive` `-s` 保存的部分完成状态的文件系统或卷，此不透明令牌可以提供给 `zfs` `send` `-t` 以恢复并完成 `zfs` `receive`。

****redact_snaps**** 对于书签，这是书签包含其删除列表的快照 GUID 列表。对于快照，这是快照被删除时所依据的快照 GUID 列表。

****referenced**** 此数据集可访问的数据量，可能与池中的其他数据集共享也可能不共享。当创建快照或克隆时，它最初引用与其创建自的文件系统或快照相同数量的空间，因为其内容相同。此属性也可以通过其缩短的列名 **refer** 引用。

****refcompressratio**** 此数据集的 **referenced** 空间所达到的压缩比，以乘数表示。另请参见 **compressratio** 属性。

****snapshot_count**** 数据集树中此位置下存在的快照总数。此值仅在数据集所在的树中某处设置了 **snapshot_limit** 时可用。

****type**** 数据集的类型：**filesystem、** **volume、** **snapshot** 或 **bookmark。**

****used**** 此数据集及其所有后代消耗的空间量。这是根据此数据集的配额和预留检查的值。使用的空间不包括此数据集的预留，但确实考虑了任何后代数据集的预留。数据集从其父级消耗的空间量，以及如果递归销毁此数据集将释放的空间量，是其使用空间和预留中的较大者。快照的已用空间（参见 zfsconcepts(7) 的 Sx Snapshots 章节）是仅由此快照引用的空间。如果此快照被销毁，将释放 **used** 空间量。多个快照共享的空间不在此指标中计算。当快照被销毁时，先前与此快照共享的空间可能成为相邻快照独有的，从而更改这些快照的已用空间。最新快照的已用空间也可能受文件系统更改的影响。注意，快照的 **used** 空间是快照 **written** 空间的子集。已用、可用或引用的空间量不考虑挂起的更改。挂起的更改通常在几秒钟内计算。使用 [fsync(2)](../sys/fsync.2.md) 或 **O_SYNC** 将更改提交到磁盘不一定保证空间使用信息立即更新。

****usedby\**** **usedby\*** 属性将 **used** 属性分解为使用空间的各种原因。具体来说，**used** = **usedbychildren** + **usedbydataset** + **usedbyrefreservation** + **usedbysnapshots。** 这些属性仅适用于在 `zpool` “version 13”池上创建的数据集。

****usedbychildren**** 此数据集的子级使用的空间量，如果所有数据集的子级都被销毁，将释放此空间。

****usedbydataset**** 此数据集本身使用的空间量，如果数据集被销毁（在首先移除任何 **refreservation** 并销毁任何必要的快照或后代之后），将释放此空间。

****usedbyrefreservation**** 此数据集上设置的 **refreservation** 使用的空间量，如果移除 **refreservation**，将释放此空间。

****usedbysnapshots**** 此数据集的快照消耗的空间量。特别是，它是如果此数据集的所有快照都被销毁将释放的空间量。注意，这不只是快照的 **used** 属性之和，因为空间可以由多个快照共享。

****userused**@`user`** 指定用户在此数据集中消耗的空间量。空间计入每个文件的所有者，如 `ls` `-l` 所示。计入的空间量由 `du` 和 `ls` `-s` 显示。详见 `zfs` `userspace` 命令。非特权用户只能访问自己的空间使用情况。root 用户或已被 `zfs` `allow` 授予 **userused** 特权的用户可以访问所有人的使用情况。**userused**@`…` 属性不通过 `zfs` `get` **all** 显示。用户名必须附加在 **@** 符号之后，使用以下形式之一：在 Linux 上创建的文件始终具有 POSIX 所有者。

****userobjused**@`user`** **userobjused** 属性类似于 **userused**，但它计算用户消耗的对象数。此属性计算代表用户分配的所有对象，它可能与 `df` `-i` 等系统工具的结果不同。当文件系统上设置 **xattr**=**on** 属性时，将为每个文件创建额外对象以存储扩展属性。这些额外对象反映在 **userobjused** 值中，并计入用户的 **userobjquota。** 当文件系统配置为使用 **xattr**=**sa** 时，通常不需要额外的内部对象。

****userrefs**** 此属性设置为此快照上的用户保留数。用户保留通过使用 `zfs` `hold` 命令设置。

****groupused**@`group`** 指定组在此数据集中消耗的空间量。空间计入每个文件的组，如 `ls` `-l` 所示。详见 **userused**@`user` 属性。非特权用户只能访问自己组的空间使用情况。root 用户或已被 `zfs` `allow` 授予 **groupused** 特权的用户可以访问所有组的使用情况。

****groupobjused**@`group`** 指定组在此数据集中消耗的对象数。使用扩展属性时，每个文件可能将多个对象计入该组。详见 **userobjused**@`user` 属性。非特权用户只能访问自己组的空间使用情况。root 用户或已被 `zfs` `allow` 授予 **groupobjused** 特权的用户可以访问所有组的使用情况。

****projectused**@`project`** 指定项目在此数据集中消耗的空间量。项目通过基于对象的数字属性的项目标识符（ID）标识。创建对象时，对象可以从其父对象继承项目 ID（如果父对象具有可通过 `chattr` `-/+P` 或 `zfs` `-s` 设置和更改的继承项目 ID 标志）。特权用户可以随时通过 `chattr` `-p` 或 `zfs` `-s` 设置和更改对象的项目 ID。空间计入每个文件的项目，如 `lsattr` `-p` 或 `zfs` 所示。详见 **userused**@`user` 属性。root 用户或已被 `zfs` 授予 **projectused** 特权的用户可以访问所有项目的使用情况。

****projectobjused**@`project`** **projectobjused** 类似于 **projectused**，但它计算项目消耗的对象数。当文件系统上设置 **xattr**=**on** 属性时，ZFS 将为每个文件创建额外对象以存储扩展属性。这些额外对象反映在 **projectobjused** 值中，并计入项目的 **projectobjquota。** 当文件系统配置为使用 **xattr**=**sa** 时，不需要额外的内部对象。详见 **userobjused**@`user` 属性。root 用户或已被 `zfs` 授予 **projectobjused** 特权的用户可以访问所有项目的对象使用情况。

****snapshots_changed**** 提供一种机制，无需挂载数据集或迭代快照列表即可快速确定快照列表是否已更改。指定数据集上次创建或删除快照的时间。这使我们能够更高效地查询快照频率。仅当启用了 **extensible_dataset** 功能时，此属性在挂载和卸载操作之间持久存在。

****snapshots_changed_nsecs**** 指定数据集上次创建或删除快照的 UTC 时间，表示为自 Unix 纪元以来的纳秒数。这是 **snapshots_changed** 的高精度版本，以纳秒而非秒的分辨率表示同一时刻。仅当启用了 **extensible_dataset** 功能时，此属性在挂载和卸载操作之间持久存在。

****volblocksize**** 对于卷，指定卷的块大小。**blocksize** 在写入卷后无法更改，因此应在创建卷时设置。指定的大小必须是大于或等于 `512` 且小于或等于 `128 KiB` 的 2 的幂。如果池上启用了 **large_blocks** 功能，大小可以最大为 `16 MiB`。默认大小为 `16 KiB`。此属性也可以通过其缩短的列名 **volblock** 引用。

****written**** 此数据集 **referenced** 的空间量，自上一个快照以来写入的（即上一个快照未引用的）。

****written**@`snapshot`** 自指定快照以来写入此数据集的 **referenced** 空间量。这是此数据集引用但指定快照未引用的空间。`snapshot` 可以指定为短快照名（仅 **@** 之后的部分），在这种情况下，它将被解释为与此数据集在同一文件系统中的快照。`snapshot` 可以是完整快照名（`filesystem`@`snapshot`），对于克隆，可以是原始文件系统（或原始的原始文件系统等）中的快照。

以下原生属性可用于更改 ZFS 数据集的行为。

****discard**** 不继承任何 ACE。
****noallow**** 仅继承指定“deny”权限的可继承 ACE。
****restricted**** 默认，继承 ACE 时移除 **write_acl** 和 **write_owner** 权限。
****passthrough**** 继承所有可继承 ACE 而不做任何修改。
****passthrough-x**** 与 **passthrough** 含义相同，只是 **owner@、group@** 和 **everyone@** ACE 仅在文件创建模式也请求执行位时才继承执行权限。

****discard**** 默认，删除所有 **ACE**，除了表示 [chmod(2)](../sys/chmod.2.md) 请求的文件或目录模式的那些。
****groupmask**** 减少 **ACL** 中所有 **ALLOW** 条目授予的权限，使其不大于 [chmod(2)](../sys/chmod.2.md) 指定的组权限。
****passthrough**** 表示除了创建或更新必要的 ACL 条目以表示文件或目录的新模式外，不对 ACL 进行任何更改。
****restricted**** 将导致 [chmod(2)](../sys/chmod.2.md) 操作在用于任何具有无法由模式表示的非平凡 ACL 的文件或目录时返回错误。[chmod(2)](../sys/chmod.2.md) 需要更改文件或目录上的设置用户 ID、设置组 ID 或粘滞位，因为它们没有等效的 ACL 条目。要在 **aclmode** 设置为 **restricted** 时对具有非平凡 ACL 的文件或目录使用 [chmod(2)](../sys/chmod.2.md)，你必须先移除所有不表示当前模式的 ACL 条目。

****off**** 在 Linux 上为默认，当文件系统的 **acltype** 属性设置为 off 时，ACL 被禁用。
****noacl**** **off** 的别名
****nfsv4**** 在 FreeBSD 上为默认，指示应使用 NFSv4 风格的 ZFS ACL。这些 ACL 可以使用 getfacl(1) 和 setfacl(1) 管理。**nfsv4** ZFS ACL 类型在 Linux 上尚不受支持。
****posix**** 指示应使用 POSIX ACL。POSIX ACL 是 Linux 特有的，在其他平台上不起作用。POSIX ACL 作为扩展属性存储，因此不会覆盖可能已设置的任何现有 NFSv4 ACL。
****posixacl**** **posix** 的别名

```sh
# `dd` **if=/dev/urandom bs=32 count=1** **of=**`/path/to/output/key`
```

- POSIX 名称（“joe”）
- POSIX 数字 ID（“789”）
- SID 名称（“joe.smith@mydomain”）
- SID 数字 ID（“S-1-123-456-789”）

```sh
sec=sys,rw,crossmnt,no_subtree_check
```

****L0**（认证）** 用户命名空间所有者 UID 必须与 **zoned_uid** 值匹配。
****L1**（dsl_deleg）** 池管理员必须使用 zfs-allow(8) 在委派根上授予每操作权限。当池委派为 OFF（`zpool` `set` **delegation**=**off**）时，无论能力如何，所有写操作都被拒绝。
****L2**（能力层）** 用户命名空间内的 Linux 能力决定允许的操作类：**CAP_FOWNER** 用于非破坏性操作（创建、快照、设置属性），**CAP_SYS_ADMIN** 用于破坏性操作（销毁、重命名、克隆）。两者都是限定于用户命名空间而非 init 命名空间的命名空间化能力。

```sh
# zfs create tank/containers
# zfs set zoned_uid=1000 tank/containers
# zfs set mountpoint=none tank/containers
# zfs allow -u 1000 create,destroy,mount,snapshot,rename,clone tank/containers
```

**Xo** **aclinherit**=**discard**|**noallow**| **restricted**|**passthrough**|**passthrough-x** Xc 控制创建文件和目录时如何继承 ACE。当属性值设置为 **passthrough** 时，文件以由可继承 ACE 确定的模式创建。如果不存在影响模式的可继承 ACE，则模式根据应用程序请求的模式设置。**aclinherit** 属性不适用于 POSIX ACL。

**Xo** **aclmode**=**discard**|**groupmask**| **passthrough**|**restricted** Xc 控制 chmod(2) 期间如何修改 ACL 以及文件创建模式如何修改继承的 ACE：

****acltype**=**off**|**nfsv4**|**posix**** 控制 ACL 是否启用以及如果启用则使用哪种类型的 ACL。当此属性设置为当前平台不支持的 ACL 类型时，行为与设置为 **off** 相同。在设置 **posix** 时，强烈建议用户设置 **xattr**=**sa** 属性以获得最佳性能。这将导致 POSIX ACL 在磁盘上更高效地存储。但作为后果，所有新的扩展属性将只能从支持 **xattr**=**sa** 属性的 OpenZFS 实现访问。详见 **xattr** 属性。

****atime**=**on**|**off**** 控制读取文件时是否更新文件的访问时间。关闭此属性可避免读取文件时产生写入流量，并能显著提高性能，尽管它可能会混淆邮件程序和其他类似实用程序。值 **on** 和 **off** 等效于 **atime** 和 **noatime** 挂载选项。默认值为 **on。** 另请参见下文的 **relatime**。

****canmount**=**on**|**off**|**noauto**** 如果此属性设置为 **off**，文件系统无法挂载，并被 `zfs` `mount` `-a` 忽略。将此属性设置为 **off** 类似于将 **mountpoint** 属性设置为 **none**，除了数据集仍具有正常的 **mountpoint** 属性，可以被继承。将此属性设置为 **off** 允许数据集仅用作继承属性的机制。设置 **canmount**=**off** 的一个例子是让两个数据集具有相同的 **mountpoint**，这样两个数据集的子级都出现在同一目录中，但可能具有不同的继承特性。设置为 **noauto** 时，数据集只能显式挂载和卸载。数据集在创建或导入时不会自动挂载，也不会被 `zfs` `mount` `-a` 命令挂载或被 `zfs` `unmount` `-a` 命令卸载。此属性不可继承。

**Xo** **checksum**=**on**|**off**|**fletcher2**| **fletcher4**|**sha256**|**noparity**| **sha512**|**skein**|**edonr**|**blake3** Xc 控制用于验证数据完整性的校验和。默认值为 **on**，自动选择适当的算法（当前为 **fletcher4**，但在未来版本中可能更改）。值 **off** 禁用用户数据的完整性检查。值 **noparity** 不仅禁用完整性，还禁用为用户数据维护奇偶校验。此设置由位于 RAID-Z 池上的转储设备内部使用，不应被任何其他数据集使用。禁用校验和*不是*推荐的做法。**sha512、** **skein、** **edonr** 和 **blake3** 校验和算法需要在池上启用相应的功能。有关这些算法的更多信息，请参见 zpool-features(7)。更改此属性仅影响新写入的数据。

**Xo** **compression**=**on**|**off**|**gzip**| **gzip-**`N`|**lz4**|**lzjb**|**zle**|**zstd**| **zstd-**`N`|**zstd-fast**|**zstd-fast-**`N` Xc 控制用于此数据集的压缩算法。设置为 **on**（默认）时，指示应使用当前默认压缩算法。默认在压缩和解压缩速度与压缩比之间取得平衡，预计适用于各种工作负载。与此属性的所有其他设置不同，**on** 不选择固定的压缩类型。随着新压缩算法被添加到 ZFS 并在池上启用，默认压缩算法可能会更改。当前默认压缩算法为 **lzjb**，或者如果启用了 **lz4_compress** 功能，则为 **lz4。** **lz4** 压缩算法是 **lzjb** 算法的高性能替代品。它具有明显更快的压缩和解压缩速度，以及比 **lzjb** 稍高的压缩比，但只能在 **lz4_compress** 功能设置为 **enabled** 的池上使用。详见 zpool-features(7) 了解 ZFS 功能标志和 **lz4_compress** 功能。**lzjb** 压缩算法在提供良好数据压缩的同时针对性能进行了优化。**gzip** 压缩算法使用与 [gzip(1)](../man1/gzip.1.md) 命令相同的压缩。可以通过使用值 **gzip-**`N` 指定 **gzip** 级别，其中 `N` 是从 1（最快）到 9（最佳压缩比）的整数。目前，**gzip** 等效于 **gzip-6**（这也是 [gzip(1)](../man1/gzip.1.md) 的默认值）。**zstd** 压缩算法提供高压缩比和良好性能。可以通过使用值 **zstd-**`N` 指定 **zstd** 级别，其中 `N` 是从 1（最快）到 19（最佳压缩比）的整数。**zstd** 等效于 **zstd-3。** 可以通过设置负 **zstd** 级别来请求以压缩比为代价的更快速度。这通过 **zstd-fast-**`N` 完成，其中 `N` 是 [**1**-**10**、**20**、**30**、…、**100**、**500**、**1000**] 中的整数，映射到负 **zstd** 级别。级别越低，压缩越快——**1000** 提供最快的压缩和最低的压缩比。**zstd-fast** 等效于 **zstd-fast-**`1`。**zle** 压缩算法压缩零的运行。此属性也可以通过其缩短的列名 **compress** 引用。更改此属性仅影响新写入的数据。当选择 **off** 以外的任何设置时，压缩将显式检查仅由零组成的块（NUL 字节）。当检测到零填充块时，它作为空洞存储，不使用指示的压缩算法进行压缩。所有块都分配为整数个扇区（2^**ashift** 字节的块，例如 **512B** 或 **4KB**）。压缩可能导致非扇区对齐的大小，将向上舍入到整数个扇区。如果压缩节省的空间少于一个整扇区，块将以未压缩方式存储。因此，逻辑大小为少量扇区的块将经历较少的压缩（例如，对于 **recordsize**=**16K** 和 **4K** 扇区，每个块有 4 个扇区，压缩需要节省至少 25% 才能实际节省磁盘空间）。除了扇区舍入外，还有 **12.5%** 的默认压缩阈值。

**Xo** **context**=**none**| `SELinux-User`:`SELinux-Role`:`SELinux-Type`:`Sensitivity-Level` Xc 此标志为文件系统挂载点下文件系统中的所有文件设置 SELinux 上下文。详见 selinux(8)。

**Xo** **fscontext**=**none**| `SELinux-User`:`SELinux-Role`:`SELinux-Type`:`Sensitivity-Level` Xc 此标志为正在挂载的文件系统设置 SELinux 上下文。详见 selinux(8)。

**Xo** **defcontext**=**none**| `SELinux-User`:`SELinux-Role`:`SELinux-Type`:`Sensitivity-Level` Xc 此标志为未标记的文件设置 SELinux 默认上下文。详见 selinux(8)。

**Xo** **rootcontext**=**none**| `SELinux-User`:`SELinux-Role`:`SELinux-Type`:`Sensitivity-Level` Xc 此标志为文件系统的根 inode 设置 SELinux 上下文。详见 selinux(8)。

****copies**=**1**|**2**|**3**** 控制为此数据集存储的数据副本数。这些副本是对池提供的任何冗余（例如镜像或 RAID-Z）的补充。如果可能，副本存储在不同的磁盘上。多个副本使用的空间计入关联的文件和数据集，更改 **used** 属性并计入配额和预留。更改此属性仅影响新写入的数据。因此，通过使用 `-o` **copies**=`N` 选项在文件系统创建时设置此属性。请记住，ZFS 不会导入缺少顶级 vdev 的池。*不要*例如创建一个双磁盘条带化池并在某些数据集上设置 **copies**=`2`，以为它们设置了冗余。当磁盘发生故障时，你将无法导入池，并且会丢失所有数据。加密数据集不能有 **copies**=`3`，因为实现在通常存储第三副本的位置存储一些加密元数据。

****devices**=**on**|**off**** 控制是否可以在此文件系统上打开设备节点。默认值为 **on。** 值 **on** 和 **off** 等效于 **dev** 和 **nodev** 挂载选项。

**Xo** **dedup**=**off**|**on**|**verify**| **sha256**[,**verify**]|**sha512**[,**verify**]| **skein**[,**verify**]|**edonr**[,**verify**]| **blake3**[,**verify**] Xc 为数据集配置去重。默认值为 **off。** 默认去重校验和为 **sha256**（未来可能更改）。启用 **dedup** 时，此处定义的校验和覆盖 **checksum** 属性。将值设置为 **verify** 与设置 **sha256,verify** 具有相同效果。如果设置为 **verify**，ZFS 将在两个块具有相同签名的情况下进行字节到字节比较，以确保块内容相同。对于 **edonr** 算法，指定 **verify** 是必需的。除非必要，不应在系统上启用去重。参见 zfsconcepts(7) 的 Sx Deduplication 章节。

**Xo** **direct**=**disabled**|**standard**|**always** Xc 控制 Direct I/O 请求（例如 `O_DIRECT`）的行为。Direct I/O 请求的 **standard** 行为是在可能时绕过 ARC。这些请求不会被缓存，性能将受底层磁盘原始速度的限制（`这是默认值`）。**always** 使每个正确对齐的读取或写入被视为直接请求。**disabled** 使 O_DIRECT 标志被静默忽略，所有直接请求将由 ARC 处理。这是 OpenZFS 2.2 及之前版本的默认行为。绕过 ARC 要求直接请求正确对齐。对于写请求，请求的起始偏移量和大小必须是 **recordsize** 对齐的，如果不是，则请求的未对齐部分将通过 ARC 静默重定向。对于读请求，起始偏移量或大小都没有 **recordsize** 对齐限制。所有直接请求必须使用页对齐的内存缓冲区，请求大小必须是页面大小的倍数，否则返回错误。并发混合缓冲和直接请求到文件的重叠区域可能会降低性能。但是，生成的文件将始终是一致的。例如，缓冲写入后的直接读取将返回缓冲写入的数据。此外，如果应用程序使用基于 [mmap(2)](../sys/mmap.2.md) 的文件访问，则为维护一致性，在文件映射期间所有直接请求都转换为缓冲请求。目前 Direct I/O 不支持 zvols。如果数据集上启用了去重，Direct I/O 写入将不检查去重。去重和 Direct I/O 写入目前不兼容。

**Xo** **dnodesize**=**legacy**|**auto**|**1k**| **2k**|**4k**|**8k**|**16k** Xc 为文件系统中 dnode 的大小指定兼容模式或字面值。默认值为 **legacy。** 将此属性设置为 **legacy** 以外的值需要启用 **large_dnode** 池功能。如果数据集使用 **xattr**=**sa** 属性设置且工作负载大量使用扩展属性，请考虑将 **dnodesize** 设置为 **auto**。这可能适用于启用 SELinux 的系统、Lustre 服务器和 Samba 服务器等。支持字面值用于预先知道最佳大小的情况和性能测试。如果需要在未启用 **large_dnode** 功能的池上接收此数据集的发送流，或者需要在不支持 **large_dnode** 功能的系统上导入此池，则将 **dnodesize** 设置为 **legacy**。此属性也可以通过其缩短的列名 **dnsize** 引用。

**Xo** **encryption**=**off**|**on**|**aes-128-ccm**| **aes-192-ccm**|**aes-256-ccm**|**aes-128-gcm**| **aes-192-gcm**|**aes-256-gcm** Xc 控制用于此数据集的加密密码套件（分组密码、密钥长度和模式）。需要在池上启用 **encryption** 功能。需要在数据集创建时设置 **keyformat**。创建数据集时选择 **encryption**=**on** 表示将选择默认加密套件，当前为 **aes-256-gcm。** 为了提供一致的数据保护，必须在数据集创建时指定加密，之后无法更改。有关加密的更多详细信息和注意事项，请参见 zfs-load-key(8) 的 Sx Encryption 章节。

****keyformat**=**raw**|**hex**|**passphrase**** 控制用户加密密钥将以何种格式提供。此属性仅在数据集加密时设置。原始密钥和十六进制密钥必须为 32 字节长（无论选择的加密套件如何），并且必须随机生成。可以使用以下命令生成原始密钥：口令短语必须为 8 到 512 字节长，在使用之前将通过 PBKDF2 处理（参见 **pbkdf2iters** 属性）。尽管加密套件在数据集创建后无法更改，但 keyformat 可以通过 `zfs` `change-key` 更改。

**Xo** **keylocation**=**prompt**|**file://**`/absolute/file/path`|**https://**`address`|**http://**`address` Xc 控制 `zfs` `load-key` 和 `zfs` `mount` `-l` 等命令默认从哪里加载用户的加密密钥。此属性仅为加密根的加密数据集设置。如果未指定，默认为 **prompt。** 尽管加密套件在数据集创建后无法更改，但 keylocation 可以通过 `zfs` `set` 或 `zfs` `change-key` 更改。如果选择 **prompt**，ZFS 将在需要访问加密数据时要求提供密钥（详见 `zfs` `load-key`）。如果 stdin 是 TTY，ZFS 将要求提供密钥。否则，stdin 应为要使用的密钥，并将按此处理。用户应小心不要将应保密的密钥放在命令行上，因为大多数操作系统可能向其他进程公开命令行参数。如果使用“raw”**keyformat**，则必须通过 stdin 提供密钥。如果选择文件 URL，密钥将从指定的绝对文件路径加载。如果选择 HTTPS 或 HTTP URL，将根据编译时配置和运行时可用性使用 fetch(3)、libcurl 或不使用任何工具进行 GET。可以设置 **SSL_CA_CERT_FILE** 环境变量以设置连接证书存储的位置。可以设置 **SSL_CA_CERT_PATH** 环境变量以覆盖包含证书授权包的目录位置。可以设置 **SSL_CLIENT_CERT_FILE** 和 **SSL_CLIENT_KEY_FILE** 环境变量以配置客户端证书及其密钥的路径。

****pbkdf2iters**=`iterations`** 控制将 **passphrase** 加密密钥处理为加密密钥时应运行的 PBKDF2 迭代次数。此属性仅在启用加密且选择 **passphrase** 的 keyformat 时定义。PBKDF2 的目标是显著增加暴力破解用户口令短语所需的计算难度。这是通过强制攻击者在得出结果密钥之前多次通过计算昂贵的哈希函数运行每个口令短语来实现的。实际知道口令短语的用户只需支付一次此成本。随着 CPU 处理能力的提高，此数字应提高以确保暴力破解攻击仍然不可行。当前默认值为 **350000**，最小值为 **100000。** 此属性可以通过 `zfs` `change-key` 更改。

****exec**=**on**|**off**** 控制是否可以从此文件系统中执行进程。默认值为 **on。** 值 **on** 和 **off** 等效于 **exec** 和 **noexec** 挂载选项。

****volthreading**=**on**|**off**** 控制内部 zvol 线程。值 **off** 禁用 zvol 线程，zvol 依赖于应用程序线程。默认值为 **on**，启用 zvol 内的线程。请注意，此属性将被 **zvol_request_sync** 模块参数覆盖。此属性仅适用于 Linux。

****filesystem_limit**=`count`|**none**** 限制数据集树中此点下可以存在的文件系统和卷的数量。如果允许用户更改限制，则不强制执行限制。在已有 **filesystem_limit** 的文件系统的后代上设置 **filesystem_limit** 不会覆盖祖先的 **filesystem_limit**，而是施加额外限制。必须启用此功能才能使用（参见 zpool-features(7)）

****special_small_blocks**=`size`** 此值表示将小文件或 zvol 块包含到特殊分配类中的阈值块大小。压缩和加密后小于或等于此值的块将分配到特殊分配类，而大于此值的块将分配到常规类。有效值为 0 到最大块大小（`16 MiB`）。默认大小为 0，表示不会在特殊类中分配小文件或 zvol 块。在设置此属性之前，必须向池添加特殊类 vdev。有关特殊分配类的更多详细信息，请参见 zpoolconcepts(7)。

****mountpoint**=`path`|**none**|**legacy**** 控制用于此文件系统的挂载点。有关如何使用此属性的更多信息，请参见 zfsconcepts(7) 的 Sx Mount Points 章节。当文件系统的 **mountpoint** 属性更改时，文件系统和任何继承挂载点的子级都会被卸载。如果新值为 **legacy**，则它们保持卸载状态。否则，如果属性先前为 **legacy** 或 **none**，它们会自动重新挂载到新位置。此外，任何共享的文件系统都会取消共享并在新位置共享。当使用 `zfs` `set` `-u` 设置 **mountpoint** 属性时，**mountpoint** 属性会更新，但数据集不会被挂载或卸载，保持原样。

****nbmand**=**on**|**off**** 控制文件系统是否应以 **nbmand**（非阻塞强制锁）方式挂载。对此属性的更改仅在文件系统卸载并重新挂载后生效。这仅在 Linux 5.15 之前受支持，且在那里有 bug，FreeBSD 不支持。在 Solaris 上它用于 SMB 客户端。

****longname**=**on**|**off**** 控制对超过 255 字节的文件名的支持，最多 1023 字节。默认为 **off。** 将此属性设置为 **on** 会激活 **longname** 池功能，必须启用该功能（参见 zpool-features(7)）。一旦创建了具有长名称的文件，该功能将变为活动状态，池将无法再由不支持它的 OpenZFS 实现导入。

****overlay**=**on**|**off**** 允许在繁忙目录或已包含文件或目录的目录上挂载。这是 Linux 和 FreeBSD 文件系统的默认挂载行为。在这些平台上，属性默认为 **on**。设置为 **off** 以禁用覆盖挂载，以便与其他平台上的 OpenZFS 保持一致。

****primarycache**=**all**|**none**|**metadata**** 控制在主缓存（ARC）中缓存什么。如果此属性设置为 **all**，则用户数据和元数据都被缓存。如果此属性设置为 **none**，则用户数据和元数据都不被缓存。如果此属性设置为 **metadata**，则只缓存元数据。默认值为 **all。**

****quota**=`size`|**none**** 限制数据集及其后代可以消耗的空间量。此属性对使用的空间量强制执行硬限制。这包括后代消耗的所有空间，包括文件系统和快照。在已有配额的数据集的后代上设置配额不会覆盖祖先的配额，而是施加额外限制。无法在卷上设置配额，因为 **volsize** 属性充当隐式配额。

****snapshot_limit**=`count`|**none**** 限制可以在数据集及其后代上创建的快照数量。在已有 **snapshot_limit** 的数据集的后代上设置 **snapshot_limit** 不会覆盖祖先的 **snapshot_limit**，而是施加额外限制。如果允许用户更改限制，则不强制执行限制。例如，这意味着从全局区域拍摄的递归快照会计入每个区域内委派的数据集。必须启用此功能才能使用（参见 zpool-features(7)）

****userquota@**`user`=`size`|**none**** 限制指定用户消耗的空间量。用户空间消耗由 **userspace@**`user` 属性标识。用户配额的执行可能会延迟几秒。此延迟意味着用户可能在系统注意到他们超过配额并开始拒绝额外写入（返回 Er EDQUOT 错误消息）之前超过其配额。详见 `zfs` `userspace` 命令。非特权用户只能访问自己组的空间使用情况。root 用户或已被 `zfs` `allow` 授予 **userquota** 特权的用户可以获取和设置所有人的配额。此属性在卷上、版本 4 之前的文件系统上或版本 15 之前的池上不可用。**userquota@**`…` 属性不通过 `zfs` `get` **all** 显示。用户名必须附加在 **@** 符号之后，使用以下形式之一：在 Linux 上创建的文件始终具有 POSIX 所有者。

****defaultuserquota**=`size`|**none**** 设置要应用于每个没有特定用户配额的用户的默认用户配额。值 **0** 禁用 defaultuserquota。

****userobjquota@**`user`=`size`|**none**** **userobjquota** 类似于 **userquota**，但它限制用户可以创建的对象数。有关如何计算对象的更多信息，请参见 **userobjused**。

****defaultuserobjquota**=`size`|**none**** 设置要应用于每个没有特定 userobj 配额的用户的默认用户对象配额。值 **0** 禁用 defaultuserobjquota。

****groupquota@**`group`=`size`|**none**** 限制指定组消耗的空间量。组空间消耗由 **groupused@**`group` 属性标识。非特权用户只能访问自己组的空间使用情况。root 用户或已被 `zfs` `allow` 授予 **groupquota** 特权的用户可以获取和设置所有组的配额。

****defaultgroupquota**=`size`|**none**** 设置要应用于每个没有特定组配额的组的默认组配额。值 **0** 禁用 defaultgroupquota。

****groupobjquota@**`group`=`size`|**none**** **groupobjquota** 类似于 **groupquota**，但它限制组可以消耗的对象数。有关如何计算对象的更多信息，请参见 **userobjused**。

****defaultgroupobjquota**=`size`|**none**** 设置要应用于每个没有特定 groupobj 配额的组的默认组对象配额。值 **0** 禁用 defaultgroupobjquota。

****projectquota@**`project`=`size`|**none**** 限制指定项目消耗的空间量。项目空间消耗由 **projectused@**`project` 属性标识。有关如何标识和设置/更改项目的更多信息，请参见 **projectused**。root 用户或已被 `zfs` 授予 **projectquota** 特权的用户可以访问所有项目的配额。

****defaultprojectquota**=`size`|**none**** 设置要应用于每个没有特定项目配额的项目的默认项目配额。值 **0** 禁用 defaultprojectquota。

****projectobjquota@**`project`=`size`|**none**** **projectobjquota** 类似于 **projectquota**，但它限制项目可以消耗的对象数。有关如何计算对象的更多信息，请参见 **userobjused**。

****defaultprojectobjquota**=`size`|**none**** 设置要应用于每个没有特定 projectobj 配额的项目的默认项目对象配额。值 **0** 禁用 defaultprojectobjquota。

****readonly**=**on**|**off**** 控制是否可以修改此数据集。默认值为 **off。** 值 **on** 和 **off** 等效于 **ro** 和 **rw** 挂载选项。此属性也可以通过其缩短的列名 **rdonly** 引用。

****recordsize**=`size`** 为文件系统中的文件指定建议的块大小。此属性专为以固定大小记录访问文件的数据库工作负载而设计。ZFS 根据针对典型访问模式优化的内部算法自动调整块大小。对于创建非常大的文件但以小的随机块访问它们的数据库，这些算法可能是次优的。指定大于或等于数据库记录大小的 **recordsize** 可以显著提高性能。强烈不建议将此属性用于通用文件系统，可能会对性能产生不利影响。指定的大小必须是大于或等于 `512` 且小于或等于 `128 KiB` 的 2 的幂。如果池上启用了 **large_blocks** 功能，大小可以最大为 `16 MiB`。详见 zpool-features(7) 了解 ZFS 功能标志。注意，在 x86_32 上默认最大大小仍限制为 `1 MiB`，参见 **zfs_max_recordsize** 模块参数。更改文件系统的 **recordsize** 仅影响之后创建的文件；现有文件不受影响。此属性也可以通过其缩短的列名 **recsize** 引用。

****redundant_metadata**=**all**|**most**|**some**|**none**** 控制哪些类型的元数据被冗余存储。ZFS 存储元数据的额外副本，这样如果单个块损坏，丢失的用户数据量是有限的。此额外副本是对池级别提供的任何冗余（例如镜像或 RAID-Z）的补充，也是对 **copies** 属性指定的额外副本的补充（最多总共 3 个副本）。例如，如果池是镜像的，**copies**=2，且 **redundant_metadata**=**most**，则 ZFS 存储大多数元数据的 6 个副本和数据及某些元数据的 4 个副本。设置为 **all** 时，ZFS 存储所有元数据的额外副本。如果单个磁盘上的块损坏，最坏情况下可能丢失单个块的用户数据（长度为 **recordsize** 字节）。设置为 **most** 时，ZFS 存储大多数类型元数据的额外副本。这可以提高随机写入的性能，因为需要写入的元数据更少。实际上，如果单个磁盘上的块损坏，最坏情况下可能丢失约 1000 个块（每个 **recordsize** 字节）的用户数据。哪些元数据块被冗余存储的确切行为可能在未来版本中更改。设置为 **some** 时，ZFS 仅存储关键元数据的额外副本。这可以提高文件创建性能，因为需要写入的元数据更少。如果单个磁盘上的块损坏，可能丢失多个用户文件或目录。设置为 **none** 时，ZFS 不冗余存储任何元数据副本。如果单个磁盘上的块损坏，可能丢失整个数据集。默认值为 **all。**

****refquota**=`size`|**none**** 限制数据集可以消耗的空间量。此属性对使用的空间量强制执行硬限制。此硬限制不包括后代使用的空间，包括文件系统和快照。

****refreservation**=`size`|**none**|**auto**** 保证给数据集的最小空间量，不包括其后代。当使用的空间量低于此值时，数据集被视为占用了 **refreservation** 指定的空间量。**refreservation** 预留计入父数据集的已用空间，并计入父数据集的配额和预留。如果设置了 **refreservation**，仅当此预留之外有足够的可用池空间来容纳数据集中当前“referenced”的字节数时，才允许创建快照。如果 **refreservation** 设置为 **auto**，卷将厚配置（或“非稀疏”）。**refreservation**=**auto** 仅在卷上受支持。有关稀疏卷的更多信息，请参见 Sx Native Properties 章节中的 **volsize**。此属性也可以通过其缩短的列名 **refreserv** 引用。

****relatime**=**on**|**off**** 控制设置 **atime**=**on** 时访问时间的更新方式。打开此属性会导致访问时间相对于修改或更改时间更新。仅当前访问时间早于当前修改或更改时间，或现有访问时间在过去 24 小时内未更新时，才更新访问时间。默认值为 **on。** 值 **on** 和 **off** 等效于 **relatime** 和 **norelatime** 挂载选项。

****reservation**=`size`|**none**** 保证给数据集及其后代的最小空间量。当使用的空间量低于此值时，数据集被视为占用了其预留指定的空间量。预留计入父数据集的已用空间，并计入父数据集的配额和预留。此属性也可以通过其缩短的列名 **reserv** 引用。

****secondarycache**=**all**|**none**|**metadata**** 控制在二级缓存（L2ARC）中缓存什么。如果此属性设置为 **all**，则用户数据和元数据都被缓存。如果此属性设置为 **none**，则用户数据和元数据都不被缓存。如果此属性设置为 **metadata**，则只缓存元数据。默认值为 **all。**

****prefetch**=**all**|**none**|**metadata**** 控制推测性预取做什么。如果此属性设置为 **all**，则预取用户数据和元数据。如果此属性设置为 **none**，则不预取用户数据和元数据。如果此属性设置为 **metadata**，则只预取元数据。默认值为 **all。** 请注意，模块参数 zfs_prefetch_disable=1 可用于完全禁用推测性预取，绕过此属性的任何操作。

****setuid**=**on**|**off**** 控制文件系统是否遵循 setuid 位。默认值为 **on。** 值 **on** 和 **off** 等效于 **suid** 和 **nosuid** 挂载选项。

****sharesmb**=**on**|**off**|`opts`** 控制文件系统是否使用 **Samba USERSHARES** 共享以及要使用的选项。否则，文件系统会通过 `zfs` `share` 和 `zfs` `unshare` 命令自动共享和取消共享。如果属性设置为 on，将调用 net(8) 命令创建 **USERSHARE。** 由于 SMB 共享需要资源名称，因此从数据集名称构造唯一的资源名称。构造的名称是数据集名称的副本，除了数据集名称中在资源名称中无效的字符被替换为下划线（_）字符。Linux 目前不支持可能在 Solaris 上可用的额外选项。如果 **sharesmb** 属性设置为 **off**，文件系统将取消共享。共享以 ACL（访问控制列表）“Everyone:F”（“F”代表“完全权限”，即读写权限）创建，默认不允许访客访问（这意味着 Samba 必须能够认证真实用户——基于 [passwd(5)](../man5/passwd.5.md)/shadow(5)、LDAP 或 smbpasswd(5)）。这意味着任何额外的访问控制（不允许特定用户特定访问等）必须在底层文件系统上完成。当使用 `zfs` `set` `-u` 更新 **sharesmb** 属性时，属性设置为所需值，但不执行共享、重新共享或取消共享数据集的操作。

****sharenfs**=**on**|**off**|`opts`** 控制文件系统是否通过 NFS 共享以及要使用的选项。**sharenfs** 属性为 **off** 的文件系统由 exportfs(8) 命令和 **`/etc/exports`** 文件中的条目管理。否则，文件系统会通过 `zfs` `share` 和 `zfs` `unshare` 命令自动共享和取消共享。如果属性设置为 **on**，数据集使用默认选项共享：请注意，选项以逗号分隔，不同于 exports(5) 中的选项。这样做是为了避免引用的需要，以及使脚本解析更容易。对于 FreeBSD，可能有多组以分号分隔的选项。每组选项必须应用于不同的主机或网络，每组选项将在 exports(5) 中创建单独的行。任何完全由空白组成的分号分隔选项集将被忽略。这种分号的使用目前仅适用于 FreeBSD。有关默认选项的含义，请参见 exports(5)。否则，使用等效于此属性内容的选项调用 exportfs(8) 命令。当数据集的 **sharenfs** 属性更改时，数据集和任何继承该属性的子级将使用新选项重新共享，但仅当属性先前为 **off**，或者它们在属性更改之前已共享。如果新属性为 **off**，文件系统将取消共享。当使用 `zfs` `set` `-u` 更新 **sharenfs** 属性时，属性设置为所需值，但不执行共享、重新共享或取消共享数据集的操作。

****logbias**=**latency**|**throughput**** 向 ZFS 提供有关如何处理此数据集中同步写入请求的提示。如果 **logbias** 设置为 **latency**（默认），ZFS 将使用池日志设备（如果已配置）以低延迟处理写入请求。如果 **logbias** 设置为 **throughput**，ZFS 将不使用已配置的池日志设备存储写入数据。ZFS 将改为优化同步操作以实现全局池吞吐量和资源的高效利用。

****snapdev**=**hidden**|**visible**** 控制 **`/dev/zvol/`**<`pool`> 下的卷快照设备是隐藏还是可见。默认值为 **hidden。**

****snapdir**=**disabled**|**hidden**|**visible**** 控制 `.zfs` 目录在文件系统根目录中是禁用、隐藏还是可见，如 zfsconcepts(7) 的 Sx Snapshots 章节所述。默认值为 **hidden。**

****sync**=**standard**|**always**|**disabled**** 控制同步请求（例如 fsync、O_DSYNC）的行为。**standard** 是 POSIX 指定的行为，确保所有同步请求写入稳定存储并刷新所有设备以确保数据不被设备控制器缓存（这是默认值）。**always** 使每个文件系统事务在其系统调用返回之前写入并刷新。这有很大的性能损失。**disabled** 禁用同步请求。文件系统事务仅定期提交到稳定存储。此选项将提供最高性能。但是，它非常危险，因为 ZFS 将忽略应用程序（如数据库或 NFS）的同步事务需求。管理员应仅在了解风险时使用此选项。

****version**=`N`|**current**** 此文件系统的磁盘版本，与池版本无关。此属性只能设置为更高支持的版本。参见 `zfs` `upgrade` 命令。

****volsize**=`size`** 对于卷，指定卷的逻辑大小。默认情况下，创建卷会建立相等大小的预留。对于版本号为 9 或更高的存储池，改为设置 **refreservation**。对 **volsize** 的任何更改都会反映在预留（或 **refreservation**）的等效更改中。**volsize** 只能设置为 **volblocksize** 的倍数，且不能为零。预留保持等于卷的逻辑大小，以防止消费者出现意外行为。没有预留，卷可能耗尽空间，导致未定义行为或数据损坏，具体取决于卷的使用方式。这些影响也可能在卷正在使用时更改卷大小时发生（特别是在缩小大小时）。调整卷大小时应格外小心。虽然不推荐，但可以通过向 `zfs` `create` `-V` 命令指定 `-s` 选项，或在卷创建后更改 **refreservation** 属性（或池版本 8 或更早的 **reservation** 属性）的值来创建“稀疏卷”（也称为“精简配置”）。稀疏卷是 **refreservation** 值小于卷大小加上存储其元数据所需空间的卷。因此，当池空间不足时，对稀疏卷的写入可能因 Er ENOSPC 而失败。对于稀疏卷，对 **volsize** 的更改不会反映在 **refreservation** 中。非稀疏卷被称为“厚配置”。通过将 **refreservation** 设置为 **auto**，稀疏卷可以变为厚配置。

****volmode**=**default**|**full**|**geom**|**dev**|**none**** 此属性指定卷应如何暴露给操作系统。设置为 **full** 将卷暴露为功能齐全的块设备，提供最大功能。值 **geom** 只是 **full** 的别名，为兼容性而保留。设置为 **dev** 隐藏其分区。属性设置为 **none** 的卷不在 ZFS 外部暴露，但可以被快照、克隆、复制等，这可能适合备份目的。值 **default** 表示卷的暴露由系统范围可调参数 **zvol_volmode** 控制，其中 **full、** **dev** 和 **none** 分别编码为 1、2 和 3。默认值为 **full。**

****vscan**=**on**|**off**** 控制是否应在文件打开和关闭时扫描常规文件的病毒。除了启用此属性外，还必须启用病毒扫描服务才能进行病毒扫描。默认值为 **off。** 此属性不被 OpenZFS 使用。

****xattr**=**on**|**off**|**dir**|**sa**** 控制是否为此文件系统启用扩展属性。支持两种样式的扩展属性：基于目录的或基于系统属性的。基于目录的扩展属性可以通过将值设置为 **dir** 来启用。这种样式的扩展属性对可以在文件上设置的属性的大小或数量没有实际限制。尽管在 Linux 下，getxattr(2) 和 setxattr(2) 系统调用将最大大小限制为 **64K**。这是最兼容的扩展属性样式，所有 ZFS 实现都支持。基于系统属性的 xattr 可以通过将值设置为 **sa**（默认且等效于 **on**）来启用。此类 xattr 的主要优势是提高性能。将扩展属性存储为系统属性可显著减少所需的磁盘 I/O 量。每个文件最多可以在系统属性保留的空间中存储 **64K** 数据。如果扩展属性没有足够的可用空间，它将自动作为基于目录的 xattr 写入。基于系统属性的扩展属性在不支持 **xattr**=**sa** 功能的平台上不可访问。OpenZFS 在 FreeBSD 和 Linux 上都支持 **xattr**=**sa**。强烈建议 SELinux 或 POSIX ACL 的用户使用基于系统属性的 xattr。这两个功能都严重依赖扩展属性，并从减少的访问时间中受益匪浅。值 **on** 和 **off** 等效于 **xattr** 和 **noxattr** 挂载选项。

****jailed**=**off**|**on**** 控制数据集是否从 jail 管理。详见 zfs-jail(8)。Jail 是 FreeBSD 功能，此属性在其他平台上不可用。

****zoned**=**off**|**on**** 控制数据集是否从非全局区域或命名空间管理。详见 zfs-zone(8)。Zoning 是 Linux 功能，此属性在其他平台上不可用。

****zoned_uid**=`uid`** 将数据集可见性和管理委派给指定 UID 拥有的所有用户命名空间。此属性使用原生 ZFS 存储启用无根容器支持。例如，设置 **zoned_uid**=1000 允许用户 1000 的无根 Podman 容器使用 ZFS 作为存储层。这是仅限 Linux 的功能。授权使用累加三层模型，所有层都必须通过：只读操作（`zfs` `list`、`zfs` `get`）不需要能力且不需要 `zfs` `allow` 授权；可见性仅由 **zoned_uid** 委派范围控制。可以委派的写操作包括 `zfs` `create`、`zfs` `destroy`、`zfs` `snapshot`、`zfs` `clone`、`zfs` `rename`（在委派子树内）和 `zfs` `set`。委派根数据集（zoned_uid 本地设置的位置）不能从用户命名空间内销毁，保护父数据集免受未授权移除。重命名也受约束以保持在委派子树内。命名空间用户不能修改 **zoned_uid** 或 **zoned** 属性，也不能覆盖管理员在委派根上设置的 **filesystem_limit** 或 **snapshot_limit**（但可以对子数据集施加更严格的子限制）。设置为 **0**（或继承）以禁用基于 UID 的委派。与需要现有命名空间文件的 `zfs` `zone` 不同，**zoned_uid** 适用于指定 UID 拥有的任何用户命名空间，使其适合在每次调用时创建新命名空间的容器运行时。有关特定于命名空间的委派，请参见 zfs-zone(8)。无根 Podman 的示例设置：

以下三个属性在创建文件系统后无法更改，因此应在创建文件系统时设置。如果未使用 `zfs` `create` 或 `zpool` `create` 命令设置这些属性，则从父数据集继承。如果父数据集由于在这些功能受支持之前创建而缺少这些属性，则新文件系统将具有这些属性的默认值。

**Xo** **casesensitivity**=**sensitive**| **insensitive**|**mixed** Xc 指示文件系统使用的文件名匹配算法应区分大小写、不区分大小写，还是允许两种匹配样式的组合。**casesensitivity** 属性的默认值为 **sensitive。** 传统上，UNIX 和 POSIX 文件系统具有区分大小写的文件名。**casesensitivity** 属性的 **mixed** 值表示文件系统可以支持区分大小写和不区分大小写匹配行为的请求。目前，支持混合行为的文件系统上的不区分大小写匹配行为仅限于 SMB 服务器产品。有关 **mixed** 值行为的更多信息，请参见“ZFS Administration Guide”。

**Xo** **normalization**=**none**|**formC**| **formD**|**formKC**|**formKD** Xc 指示文件系统是否应在比较两个文件名时执行文件名的 **Unicode** 规范化，以及应使用哪种规范化算法。文件名始终以未修改的方式存储，名称作为任何比较过程的一部分进行规范化。如果此属性设置为 **none** 以外的合法值，且 **utf8only** 属性未指定，则 **utf8only** 属性自动设置为 **on。** **normalization** 属性的默认值为 **none。** 此属性在创建文件系统后无法更改。

****utf8only**=**on**|**off**** 指示文件系统是否应拒绝包含 **UTF-8** 字符代码集中不存在的字符的文件名。如果此属性显式设置为 **off**，则 normalization 属性必须要么未显式设置，要么设置为 **none。** **utf8only** 属性的默认值为 **off。** 此属性在创建文件系统后无法更改。

**casesensitivity、** **normalization** 和 **utf8only** 属性也是新权限，可以通过使用 ZFS 委派管理功能分配给非特权用户。

### 临时挂载点属性

当文件系统通过 [mount(8)](../man8/mount.8.md) 进行传统挂载或通过 `zfs` `mount` 命令进行正常文件系统挂载时，其挂载选项根据其属性设置。属性和挂载选项之间的相关性如下：

****atime**** atime/noatime
****canmount**** auto/noauto
****devices**** dev/nodev
****exec**** exec/noexec
****readonly**** ro/rw
****relatime**** relatime/norelatime
****setuid**** suid/nosuid
****xattr**** xattr/noxattr
****nbmand**** mand/nomand
****context**=** context=
****fscontext**=** fscontext=
****defcontext**=** defcontext=
****rootcontext**=** rootcontext=

此外，这些选项可以使用 `-o` 选项按挂载设置，而不影响存储在磁盘上的属性。命令行上指定的值覆盖存储在数据集中的值。**nosuid** 选项是 **nodevices,****nosetuid** 的别名。这些属性被 `zfs` `get` 命令报告为“临时”。如果在数据集挂载时更改了属性，新设置会覆盖任何临时设置。

### 用户属性

除了标准原生属性外，ZFS 还支持任意用户属性。用户属性对 ZFS 行为没有影响，但应用程序或管理员可以使用它们注释数据集（文件系统、卷和快照）。

用户属性名必须包含冒号（“**:**”）字符，以将它们与原生属性区分开。它们可以包含小写字母、数字和以下标点字符：冒号（“**:**”）、连字符（“**-**”）、句点（“**.**”）和下划线（“**_**”）。预期约定是属性名分为两部分，如 `module`:`property`，但此命名空间不被 ZFS 强制执行。用户属性名最多 256 个字符，且不能以连字符（“**-**”）开头。

当以编程方式使用用户属性时，强烈建议对属性名的 `module` 组件使用反向 DNS 域名，以减少两个独立开发的包出于不同目的使用相同属性名的机会。

用户属性的值是任意字符串，始终被继承，且从不验证。所有操作属性的命令（`zfs` `list`、`zfs` `get`、`zfs` `set` 等）都可以用于操作原生属性和用户属性。使用 `zfs` `inherit` 命令清除用户属性。如果属性未在任何父数据集中定义，则完全移除。属性值限制为 8192 字节。
