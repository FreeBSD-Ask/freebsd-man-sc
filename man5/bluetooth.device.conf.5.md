# bluetooth.device.conf(5)

`bluetooth.device.conf` — 蓝牙设备配置文件

## 名称

`bluetooth.device.conf`

## 描述

蓝牙设备配置框架提供了按设备调整某些蓝牙设备参数的能力。

蓝牙设备配置文件是纯文本文件，应符合基本的 [sh(1)](../man1/sh.1.md) 语法。虽然蓝牙设备配置文件不完全是 shell 脚本，但它们会被解析并通过 shell `eval` 命令执行。这使得在蓝牙设备配置文件中使用各种 shell 技巧成为可能。

**/etc/rc.d/bluetooth** 脚本用于启动和停止蓝牙设备。系统启动时默认不执行此脚本。它由 devd(8) 在响应蓝牙设备到达和离开事件时调用。如有需要，也可以手动执行此脚本。该脚本接受蓝牙设备驱动程序名作为额外参数。

系统范围的蓝牙设备配置文件名为 **/etc/defaults/bluetooth.device.conf**。系统范围蓝牙设备配置文件中设置的配置参数适用于连接到系统的每个蓝牙设备。

针对特定蓝牙设备的配置参数覆盖应放在 **/etc/bluetooth/`DEVICE_DRIVER_NAME`.conf** 文件中。其中 `DEVICE_DRIVER_NAME` 是该蓝牙设备的设备驱动程序名。

以下列表提供了可在蓝牙设备配置文件中设置的每个变量的名称和简短说明。

**`authentication_enable`** （`bool`）`authentication_enable` 参数控制设备在连接建立时是否需要对远程设备进行认证。如果设置为 “`YES`”，设备将在连接建立时尝试对另一端设备进行认证。蓝牙认证请求由 hcsecd(8) 守护进程处理。

**`class`** （`str`）`class` 参数用于向其他设备指示本设备的能力。更多细节请参见 “Assigned Numbers - Bluetooth Baseband” 文档。

**`connectable`** （`bool`）`connectable` 参数控制设备是否应定期扫描来自其他设备的寻呼尝试。如果设置为 “`YES`”，设备将定期扫描来自其他设备的寻呼尝试。

**`discoverable`** （`bool`）`discoverable` 参数控制设备是否应定期扫描来自其他设备的查询请求。如果设置为 “`YES`”，设备将定期扫描来自其他设备的查询请求。

**`encryption_mode`** （`str`）`encryption_mode` 参数控制设备在连接建立时是否需要对远程设备进行加密。在连接建立时，只有启用了 `authentication_enable` 参数和 `encryption_mode` 参数的设备才会尝试对到另一端设备的连接进行加密。可选值为 “`NONE`” 禁用加密、“`P2P`” 仅对点到点分组进行加密，或 “`ALL`” 对点到点和广播分组都进行加密。

**`hci_debug_level`** （`int`）HCI 节点调试级别。值越高输出越详细。

**`l2cap_debug_level`** （`int`）L2CAP 节点调试级别。值越高输出越详细。

**`local_name`** （`str`）`local_name` 参数提供了修改设备用户友好名称的能力。

**`role_switch`** （`bool`）`role_switch` 参数控制本地设备是否应执行角色切换。默认情况下，如果支持角色切换，本地设备会在传入连接时尝试执行角色切换并成为主设备（Master）。某些设备不支持角色切换，因此来自此类设备的传入连接将失败。如果禁用了 `role switch`，则接受方设备将保持从设备（Slave）身份。

## 文件

**/etc/defaults/bluetooth.device.conf**

**/etc/rc.d/bluetooth**

## 实例

**/etc/bluetooth/ubt0.conf** 文件应用于指定第一个 USB 蓝牙设备（设备驱动程序名为 `ubt0`）的配置参数覆盖。

**/etc/bluetooth/ubt1.conf** 文件应用于指定第二个 USB 蓝牙设备的配置参数覆盖。

## 参见

[ng_hci(4)](../man4/ng_hci.4.md), [ng_l2cap(4)](../man4/ng_l2cap.4.md), [ng_ubt(4)](../man4/ng_ubt.4.md), devd(8), hccontrol(8), hcsecd(8), l2control(8)

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>
