# btsockstat.1

`btsockstat` — 显示 Bluetooth 套接字信息

## 名称

`btsockstat`

## 概要

`btsockstat [-nrh] [-M core] [-p protocol]`

## 描述

`btsockstat` 实用程序以符号形式显示各种与 Bluetooth 套接字相关的数据结构内容。根据所呈现信息对应选项的不同，输出格式有若干种。`btsockstat` 实用程序将结果输出到标准输出，错误信息输出到标准错误。

选项如下：

**`-h`** 显示用法信息并退出。

**`-M`** `core` 从指定的 core 文件而非默认的 **/dev/kmem** 中提取与名称列表关联的值。

**`-n`** 以数字形式显示 Bluetooth 地址。默认情况下，`btsockstat` 会尝试解析 Bluetooth 地址并以符号形式显示。

**`-p`** `protocol` 显示指定协议的活动套接字（协议控制块）列表。支持的协议有：`hci_raw`、`l2cap_raw`、`l2cap`、`rfcomm` 和 `rfcomm_s`。

**`-r`** 显示指定协议的活动路由条目（如果有）。

## 退出状态

`btsockstat` 实用程序成功时退出值为 0，发生错误时退出值大于 0。

## 参见

[ng_btsocket(4)](../man4/ng_btsocket.4.md)

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>

## 缺陷

很可能存在缺陷。如发现请报告。
