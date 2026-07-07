# mpsutil(8)

`mpsutil` — 管理 LSI Fusion-MPT 2/3 控制器的实用工具

## 名称

`mpsutil`, `mprutil`

## 概要

`mprutil version`  
`mprutil [-u unit] show adapter`  
`mprutil [-u unit] show adapters`  
`mprutil [-u unit] show all`  
`mprutil [-u unit] show cfgpage page [num] [addr]`  
`mprutil [-u unit] show devices`  
`mprutil [-u unit] show enclosures`  
`mprutil [-u unit] show expanders`  
`mprutil [-u unit] show iocfacts`  
`mprutil [-u unit] set ncq [enable|disable]`  
`mprutil [-u unit] flash save [firmware|bios] [file]`  
`mprutil [-u unit] flash update [firmware|bios] file`

## 描述

`mpsutil` 工具可用于显示或修改 LSI Fusion-MPS 2 控制器上的各种参数。

`mprutil` 工具可用于显示或修改 LSI Fusion-MPS 3 控制器上的各种参数。

`mpsutil` 和 `mprutil` 命令的行为完全相同。

每次调用 `mprutil` 由零个或多个全局选项后跟一个命令组成。命令可以在命令之后支持额外的可选或必需参数。

当前支持一个全局选项：

**`-u`** `unit` `unit` 指定要使用的控制器单元。如果未指定单元，则使用单元 0。

`mprutil` 工具支持几组不同的命令。第一组命令提供有关控制器的信息。第二组命令用于管理控制器范围的操作。

信息命令包括：

**`version`** 显示 `mprutil` 的版本。

**`show adapter`** 显示有关控制器的信息，如型号或固件版本。

**`show adapters`** 显示所有适配器的摘要。

**`show all`** 显示所有设备、扩展器和机箱。

**`show devices`** 显示所有设备。

**`show expanders`** 显示所有扩展器。

**`show enclosures`** 显示所有机箱。

**`show iocfacts`** 显示 IOC Facts 消息。

**`show cfgpage page`** [`num`][`addr`] 以十六进制转储原始配置页。

控制器管理命令包括：

**`set ncq`** [`enable`|`disable`] 在卡片的 NVRAM 中启用或禁用 NCQ。

**`flash save`** [`firmware`|`bios`][`file`] 将控制器中的 `firmware` 或 `bios` 保存到本地 `file`。如果未指定 `file`，则文件将命名为 `firmware` 或 `bios`。

**`flash update`** [`firmware`|`bios`]`file` 用通过 `file` 指定的固件或 BIOS 替换控制器中的 `firmware` 或 `bios`。

## 参见

[mpr(4)](../man4/mpr.4.md), [mps(4)](../man4/mps.4.md)

## 历史

`mprutil` 工具首次出现在 FreeBSD 11.0 中。

## TODO

在大端架构上不支持 Flash 操作（保存/更新）。
