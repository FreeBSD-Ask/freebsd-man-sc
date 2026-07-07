# devctl(8)

`devctl` — 设备控制工具

## 名称

`devctl`

## 概要

`devctl attach device`

`devctl clear driver [-f] device`

`devctl detach [-f] device`

`devctl disable [-f] device`

`devctl enable device`

`devctl suspend device`

`devctl resume device`

`devctl set driver [-f] device driver`

`devctl rescan device`

`devctl delete [-f] device`

`devctl freeze`

`devctl thaw`

`devctl reset [-d] device`

`devctl getpath locator device`

## 描述

`devctl` 工具用于调整内核内部设备层次结构中各个设备的状态。每次调用 `devctl` 由一个命令及该命令特有的参数组成。每个命令作用于通过 `device` 参数指定的单个设备。`device` 可以指定为现有设备的名称，也可以指定为特定于总线的地址。有关支持的地址格式的更多细节，请参见 devctl(3)。

支持以下命令：

**`attach`** `device` 强制内核重新探测该设备。如果找到合适的驱动程序，会将其附加到该设备。

**`detach`** [`-f`] `device` 将设备从其当前的设备驱动程序分离。如果指定了 `-f` 标志，即使设备处于忙碌状态，也会分离该设备驱动程序。

**`disable`** [`-f`] `device` 禁用设备。如果设备当前已附加到设备驱动程序，则会将该设备驱动程序从设备分离，但设备会保留其当前名称。如果指定了 `-f` 标志，即使设备处于忙碌状态，也会分离该设备驱动程序。

**`enable`** `device` 启用设备。如果找到合适的设备驱动程序，设备会进行探测并附加。注意，这可以重新启用在引导时通过 loader 可调参数禁用的设备。

**`suspend`** `device` 挂起设备。这可能包括将设备置于降低功耗的状态。

**`resume`** `device` 将挂起的设备恢复到完全工作状态。

**`set driver`** [`-f`] `device driver` 强制设备使用名为 `driver` 的设备驱动程序。如果设备已附加到设备驱动程序，并且指定了 `-f` 标志，则会先将设备从当前设备驱动程序分离，然后再附加到新的设备驱动程序。如果设备已附加到设备驱动程序，并且未指定 `-f` 标志，则不会更改设备。

**`clear driver`** [`-f`] `device` 清除先前强制指定的驱动程序名称，使设备可以使用任何有效的设备驱动程序。清除先前的名称后，会重新探测该设备，以便其他设备驱动程序可以附加到它。这可用于撤销先前的 `set driver` 命令。如果设备当前已附加到设备驱动程序，并且未指定 `-f` 标志，则不会更改设备。

**`rescan`** `device` 重新扫描总线设备，检查已添加或移除的设备。

**`delete`** [`-f`] `device` 从设备树中删除该设备。如果指定了 `-f` 标志，即使设备物理上仍然存在，也会删除该设备。使用此命令时应谨慎，因为已删除但仍存在的设备将无法再使用，除非父总线设备通过重新扫描请求重新发现该设备。

**`freeze`** 冻结为响应驱动程序加载而启动的探测和附加处理。驱动程序会被放置在“冻结列表”中，并在随后发生“解冻”时进行处理。

**`thaw`** 恢复（解冻冻结）为响应驱动程序加载而启动的探测和附加处理。除了恢复之外，还会执行在冻结期间被冻结的所有待处理操作。

**`reset`** [`-d`] `device` 使用特定于总线的复位方法复位设备。被复位的设备的驱动程序会在复位期间被挂起。如果指定了 `-d` 选项，则会改为分离驱动程序。目前，PCIe 总线和 PCI 设备实现了复位功能。对于 PCIe 总线，会先禁用链路然后重新训练，导致该总线的所有子设备复位。使用 [devinfo(8)](devinfo.8.md) 工具的 `-p` 选项可以报告该设备的父总线。对于 PCI 设备，如果实现了功能级复位（Function-Level Reset），会先尝试 FLR；如果失败或未实现，则尝试电源复位。如果你显式地分离或挂起了某个子设备，然后执行复位，该子设备最终会处于已附加状态。

**`getpath`** `locator` `device` 使用 `locator` 方法打印到 `device` 的完整路径，以获取路径名。目前只实现了“UEFI”和“FreeBSD”定位器。UEFI 定位器使用 UEFI 标准中为 DEVICE_PATH 概述的规则构造到设备的路径。FreeBSD 定位器构造一条回到树根的路径，节点之间用斜杠分隔。

## 参见

devctl(3), [devinfo(8)](devinfo.8.md)

## 历史

`devctl` 工具首次出现于 FreeBSD 10.3。

## 缺陷

目前没有管理标志来防止在复位后重新附加或恢复手动分离或挂起的设备。类似地，也没有标志来防止在系统恢复后取消挂起手动挂起的设备。
