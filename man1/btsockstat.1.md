  BTSOCKSTAT(1)  

BTSOCKSTAT(1)

FreeBSD General Commands Manual

BTSOCKSTAT(1)

[名称](#__u540D___u79F0_)
=======================

`btsockstat` —

显示蓝牙套接字信息

[概要](#__u6982___u8981_)
=======================

`btsockstat` \[`-nrh`\] \[`-M` core\] \[`-p` protocol\]

[描述](#__u63CF___u8FF0_)
=======================

`btsockstat` 实用程序象征性地显示各种蓝牙套接字相关数据结构的内容。 输出格式很少，具体取决于所提供信息的选项。 `btsockstat` 实用程序会将结果打印到标准输出，并将错误消息打印到标准错误。

选项如下：

[`-h`](#h)

显示使用信息并退出。

[`-M`](#M) core

从指定的核心而不是默认的 /dev/kmem 中提取与名称列表关联的值。

[`-n`](#n)

将蓝牙地址显示为数字。 通常， `btsockstat` 会尝试解析蓝牙地址，并象征性地显示它们。

[`-p`](#p) protocol

显示每个指定协议的活动套接字（协议控制块）列表。 支持的协议有： `hci_raw 、 l2cap_raw 、 l2cap、 rfcomm` 和 `rfcomm_s` 。

[`-r`](#r)

显示指定协议的活动路由条目（如果有）列表。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `btsockstat` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

ng\_btsocket(4)

[作者](#__u4F5C___u8005_)
=======================

Maksim Yevmenkin <[m\_evmenkin@yahoo.com](mailto:m_evmenkin@yahoo.com)\>

[缺陷](#__u7F3A___u9677_)
=======================

最有可能的。如果发现请报告。

October 12, 2003

FreeBSD 13.1-RELEASE