  DEVCTL(8)  

DEVCTL(8)

FreeBSD System Manager's Manual

DEVCTL(8)

[名称](#__u540D___u79F0_)
=======================

`devctl` —

备控制实用程序

[概要](#__u6982___u8981_)
=======================

`devctl` `attach` device `devctl` `clear driver` \[`-f`\] device `devctl` `detach` \[`-f`\] device `devctl` `disable` \[`-f`\] device `devctl` `enable` device `devctl` `suspend` device `devctl` `resume` device `devctl` `set driver` \[`-f`\] device driver `devctl` `rescan` device `devctl` `delete` \[`-f`\] device `devctl` `reset` \[`-d`\] device

[描述](#__u63CF___u8FF0_)
=======================

`devctl` 实用程序调整内核内部设备层次结构中各个设备的状态。 `devctl` 的每次调用都由一个命令和特定于命令的参数组成。 每个命令都在通过 device 参数指定的单个设备上运行。 device 可以指定为现有设备的名称或总线特定地址。 有关支持的地址格式的更多详细信息，请参见 devctl(3) 。

支持以下命令：

[`attach`](#attach) device

强制内核重新探测设备。 如果找到合适的驱动程序，则将其连接到设备。

[`detach`](#detach) \[`-f`\] device

将设备与其当前设备驱动程序分离。 如果指定了 `-f` 标志，即使设备繁忙，设备驱动程序也会被分离。

[`disable`](#disable) \[`-f`\] device

禁用设备。 如果设备当前附加到设备驱动程序，设备驱动程序将从设备分离，但设备将保留其当前名称。 如果指定了 `-f` 标志，即使设备繁忙，设备驱动程序也会被分离。

[`enable`](#enable) device

启用设备。 如果找到合适的设备驱动程序，设备将探测并附加。 请注意，这可以通过加载程序可调参数重新启用在引导时禁用的设备。

[`suspend`](#suspend) device

挂起设备。 这可能包括将设备置于低功耗状态。

[`resume`](#resume) device

将挂起的设备恢复到完全工作状态。

[`set driver`](#set_driver) \[`-f`\] device driver

强制设备使用名为 driver 的设备驱动程序。 如果设备已经附加到设备驱动程序并且指定了 `-f` 标志，则设备将在附加到新设备驱动程序之前与其当前设备驱动程序分离。 如果设备已附加到设备驱动程序并且未指定 `-f` 标志，则不会更改设备。

[`clear driver`](#clear_driver) \[`-f`\] device

清除以前强制的驱动程序名称，以便设备能够使用任何有效的设备驱动程序。 清除以前的名称后，将重新探测设备，以便其他设备驱动程序可以附加到它。 这可用于撤消较早的 `set driver` 命令。 如果设备当前附加到设备驱动程序并且未指定 `-f` 标志，则不会更改设备。

[`rescan`](#rescan) device

重新扫描总线设备，检查已添加或删除的设备。

[`delete`](#delete) \[`-f`\] device

从设备树中删除设备。 如果指定了 `-f` 标志，则即使设备实际存在，它也会被删除。 应谨慎使用此命令，因为除非父总线设备通过重新扫描请求重新发现设备，否则无法再使用已删除但存在的设备。

[`reset`](#reset) \[`-d`\] device

使用总线特定的复位方法复位器件。 正在重置的设备的驱动程序在重置前后暂停。 如果指定了 `-d` 选项，则改为分离驱动程序。

目前，为 PCIe 总线和 PCI 设备实现了复位。 对于 PCIe 总线，链路被禁用然后重新训练，导致总线的所有子级复位。 使用 devinfo(8) 工具的 `-p` 选项报告设备的父总线。 对于PCI设备，如果它实现了Function-Level Reset，则先尝试FLR；如果失败或未实施，则尝试电源重置。

如果您已明确分离或暂停子设备，然后进行重置，则子设备将最终连接。

[参见](#__u53C2___u89C1_)
=======================

devctl(3), devinfo(8)

[历史](#__u5386___u53F2_)
=======================

`devctl` 实用程序首次出现在 FreeBSD 10.3 中。

[缺陷](#__u7F3A___u9677_)
=======================

目前没有管理标志来防止手动分离或挂起的设备在重置后重新连接或恢复。 类似地，没有标志可以防止系统恢复后手动挂起的设备解除挂起。

April 4, 2019

FreeBSD 13.1-RELEASE