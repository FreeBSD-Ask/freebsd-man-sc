# gmultipath(8)

`gmultipath` — 磁盘多路径控制工具

## 名称

`gmultipath`

## 概要

`gmultipath create [-ARv] name prov ...`

`gmultipath label [-ARv] name prov ...`

`gmultipath configure [-APRv] name`

`gmultipath add [-v] name prov`

`gmultipath remove [-v] name prov`

`gmultipath fail [-v] name prov`

`gmultipath restore [-v] name prov`

`gmultipath rotate [-v] name`

`gmultipath prefer [-v] name prov`

`gmultipath getactive [-v] name`

`gmultipath destroy [-v] name`

`gmultipath stop [-v] name`

`gmultipath clear [-v] prov ...`

`gmultipath list`

`gmultipath status`

`gmultipath load`

`gmultipath unload`

## 描述

`gmultipath` 工具用于设备多路径配置。

多路径设备可以使用两种不同的方法配置：“手动”（manual）或“自动”（automatic）。使用“手动”方法时，设备上不存储任何元数据，因此每次需要时都必须手动配置多路径设备。额外的设备路径也不会被自动检测。“自动”方法使用磁盘上元数据来检测设备及其所有路径。元数据使用底层磁盘设备的最后一个扇区，包含设备名称和 UUID。UUID 在共享存储环境中保证唯一性，但通常过于繁琐不便使用。名称是通过设备接口导出的内容。

`gmultipath` 的第一个参数表示要执行的操作：

**`create`** 使用“手动”方法创建多路径设备，不写入任何磁盘上元数据。如何正确识别设备路径由管理员决定。内核仅会检查所有给定 provider 是否具有相同的介质和扇区大小。`-A` 选项启用 Active/Active 模式，`-R` 选项启用 Active/Read 模式，否则默认使用 Active/Passive 模式。

**`label`** 使用“自动”方法创建多路径设备。使用指定的 `name` 为第一个给定 provider 标记磁盘上元数据。其余给定 provider 将被重新品尝（retaste）以检测这些元数据。这能可靠地防止指定无关的 provider。未检测到匹配元数据的 provider 将不会被添加到设备中。`-A` 选项启用 Active/Active 模式，`-R` 选项启用 Active/Read 模式，否则默认使用 Active/Passive 模式。

**`configure`** 配置给定的多路径设备。`-A` 选项启用 Active/Active 模式，`-P` 选项启用 Active/Passive 模式，`-R` 选项启用 Active/Read 模式。

**`add`** 将给定 provider 作为路径添加到给定的多路径设备。通常仅应用于使用“手动”方法创建的设备，除非你清楚自己在做什么（你确定它是另一个设备路径，但无法以常规“自动”方式品尝其元数据）。

**`remove`** 将给定 provider 作为路径从给定的多路径设备中移除。如果移除的是最后一条路径，多路径设备将被销毁。

**`fail`** 将指定多路径设备的指定 provider 路径标记为失败。如果存在其他路径，新的请求将被转发到那些路径。

**`restore`** 将指定多路径设备的指定 provider 路径标记为可操作，允许其处理请求。

**`rotate`** 在 Active/Passive 模式下将活动 provider/路径切换到下一个可用 provider。

**`prefer`** 在 Active/Passive 模式下将活动 provider/路径切换到指定 provider。

**`getactive`** 获取当前活动的 provider/路径。

**`destroy`** 销毁给定的多路径设备并清除元数据。

**`stop`** 停止给定的多路径设备但不清除元数据。

**`clear`** 清除给定 provider 上的元数据。

**`list`** 参见 geom(8)。

**`status`** 参见 geom(8)。

**`load`** 参见 geom(8)。

**`unload`** 参见 geom(8)。

## SYSCTL 变量

以下 [sysctl(8)](sysctl.8.md) 变量可用于控制 `MULTIPATH` GEOM 类的行为。

**`kern.geom.multipath.debug`** : 0 `MULTIPATH` GEOM 类的调试级别。可设置为 0（默认）或 1 以禁用或启用各种形式的详细输出。

**`kern.geom.multipath.exclusive`** : 1 以独占方式打开底层 provider，阻止单独路径访问。

## 退出状态

成功时退出状态为 0，命令失败时为 1。

## 多路径架构

这是一种多路径架构，除了大小匹配外，不内置任何设备知识或假设。因此，用户在选择确实代表同一底层磁盘设备多条路径的 provider 时必须谨慎。原因在于，跨多种底层传输类型存在若干可以 `指示` 身份的标准，但在所有方面，这种身份很少能被认为是 `确定性` 的。

例如，如果使用光纤通道磁盘对象的全球端口名（WWPN），可能会认为在不同路径（甚至不相交的光纤网络）上具有相同 WWPN 的两块磁盘是同一块磁盘。几乎在所有情况下这都是一个安全的假设，直到你意识到 WWPN 像以太网 MAC 地址一样是一个软可编程实体，而配置错误的 Director Class 交换机可能让你错误地认为找到了同一设备的多条路径。这是一个极端且理论性的案例，但确实有可能发生，这表明关于哪些多路径名指向同一设备的决策策略应交由系统操作员，他们使用工具和对自己存储子系统的了解来做出正确的配置选择。

支持 Active/Passive、Active/Read 和 Active/Active 操作模式。在 Active/Passive 模式下，任意时刻只有一条路径上有 I/O 流动。此 I/O 持续进行，直到 I/O 返回通用 I/O 错误或“Nonexistent Device”错误。发生这种情况时，该路径被标记为 FAIL，列表中的下一条路径被选为活动路径，失败的 I/O 被重新发送。在 Active/Active 模式下，所有未标记为 FAIL 的路径可同时处理 I/O。请求在路径之间分布以均衡负载。对于有能力的设备，它允许利用所有路径上的可用带宽。在 Active/Read 模式下，所有未标记为 FAIL 的路径可同时处理读请求，但与 Active/Active 模式不同，任意时刻只有一条路径处理写请求；如果上层需要数据一致性，则严格遵循原始写请求顺序（在发送依赖写之前不等待必需的写完成）。

当新设备添加到系统时，`MULTIPATH` GEOM 类有机会品尝这些新设备。如果新设备具有 `MULTIPATH` 磁盘上元数据标签，该设备要么用于创建新的 `MULTIPATH` GEOM，要么被添加到现有 `MULTIPATH` GEOM 的路径列表中。

正是此机制与基于 [isp(4)](../man4/isp.4.md) 和 [mpt(4)](../man4/mpt.4.md) 的光纤通道磁盘设备配合良好。对于这些设备，当设备消失时（例如由于拔掉线缆或交换机断电），设备会被主动标记为已消失，对其的 I/O 将失败。这会触发前述的 `MULTIPATH` 故障事件。

当光纤通道事件通知 [isp(4)](../man4/isp.4.md) 或 [mpt(4)](../man4/mpt.4.md) 主机总线适配器可能有新设备到达时（例如从 Fabric Domain Controller 收到 RSCN 事件），它们可以触发重新扫描，并导致任何（当前）新设备的附加和配置，从而触发上述品尝事件。

这意味着此多路径架构不是一次性路径故障切换，只要故障路径被修复（自动或其他方式），就可视为处于稳定状态。

自动重新扫描并非必需，光纤通道也不是。相同的故障切换机制对传统“并行”SCSI 同样有效，但可能需要使用 [camcontrol(8)](camcontrol.8.md) 手动干预以重新附加修复的设备链接。

## 实例

以下示例展示如何使用 [camcontrol(8)](camcontrol.8.md) 查找可能的多路径设备并为它们创建 `MULTIPATH` GEOM 类。

```sh
mysys# camcontrol devlist
<ECNCTX @WESTVILLE >   at scbus0 target 0 lun 0 (da0,pass0)
<ECNCTX @WESTVILLE >   at scbus0 target 0 lun 1 (da1,pass1)
<ECNCTX @WESTVILLE >   at scbus1 target 0 lun 0 (da2,pass2)
<ECNCTX @WESTVILLE >   at scbus1 target 0 lun 1 (da3,pass3)
mysys# camcontrol inquiry da0 -S
ECNTX0LUN000000SER10ac0d01
mysys# camcontrol inquiry da2 -S
ECNTX0LUN000000SER10ac0d01
```

既然你已使用序列号比较了两条磁盘路径，得出它们是同一设备的多条路径的结论并非完全不合理。然而，只有熟悉自己存储的用户才有资格做出此判断。

然后你可以使用 `MULTIPATH` 命令标记并创建名为 `FRED` 的 `MULTIPATH` GEOM provider。

```sh
gmultipath label -v FRED /dev/da0 /dev/da2
disklabel -Bw /dev/multipath/FRED auto
newfs /dev/multipath/FREDa
mount /dev/multipath/FREDa /mnt....
```

生成的控制台输出类似于：

```sh
GEOM_MULTIPATH: da0 added to FRED
GEOM_MULTIPATH: da0 is now active path in FRED
GEOM_MULTIPATH: da2 added to FRED
```

要在引导时加载 `MULTIPATH` 模块，将以下条目添加到 **/boot/loader.conf**：

```sh
geom_multipath_load="YES"
```

## 参见

[geom(4)](../man4/geom.4.md), [isp(4)](../man4/isp.4.md), [mpt(4)](../man4/mpt.4.md), [loader.conf(5)](../man5/loader.conf.5.md), [camcontrol(8)](camcontrol.8.md), geom(8), [mount(8)](mount.8.md), newfs(8), [sysctl(8)](sysctl.8.md)

## 历史

`MULTIPATH` 工具首次出现在 FreeBSD 7.0 中。

## 作者

Matthew Jacob <mjacob@FreeBSD.org> Alexander Motin <mav@FreeBSD.org>
