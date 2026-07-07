# wpa_supplicant(8)

`wpa_supplicant` — 用于无线网络设备的 WPA/802.11i 客户端

## 名称

`wpa_supplicant`

## 概要

`wpa_supplicant [-BdhKLqstuvW] [-b br_ifname] -c config-file [-C ctrl] [-D driver] [-f debug file] [-g global ctrl] -i ifname [-o override driver] [-O override ctrl] [-P pid file] [-N -i ifname -c config-file [-C ctrl] [-D driver] [-p driver_param] [-b br_ifname] ...]`

## 描述

`wpa_supplicant` 工具是 WPA 客户端组件的实现，即在客户端站点上运行的部分。它实现了与 WPA 认证器的 WPA 密钥协商，以及与认证服务器的 EAP 认证。此外，`wpa_supplicant` 还控制 [wlan(4)](../man4/wlan.4.md) 模块的漫游和 IEEE 802.11 认证/关联支持，并可根据识别到的网络配置静态 WEP 密钥。

`wpa_supplicant` 工具被设计为一个“daemon”程序，在后台运行并作为控制无线连接的后端组件。它支持独立的前端程序，例如基于文本的 wpa_cli(8) 程序。

以下参数必须在命令行上指定：

**`-i`** `ifname` 使用指定的无线接口。

**`-c`** `config-file` 在管理无线接口时使用指定配置文件中的设置。有关配置文件语法和内容的说明，请参见 wpa_supplicant.conf(5)。对配置文件的更改可以通过向 `wpa_supplicant` 进程发送 `SIGHUP` 信号，或使用 wpa_cli(8) 工具执行“`wpa_cli reconfigure`”来重新加载。

## 选项

可用选项如下：

**`-b`** 可选的网桥接口名称。

**`-B`** 与控制终端分离，作为守护进程在后台运行。

**`-d`** 启用调试消息。若此选项提供两次，将显示更详细的消息。

**`-D`** 驱动程序名称（可以是多个驱动程序：nl80211,wext）。

**`-f`** 将日志输出到调试文件而非 stdout。

**`-g`** 全局 ctrl_interface。

**`-h`** 显示帮助文本。

**`-K`** 在调试输出中包含密钥信息。

**`-L`** 在终端上显示本程序的许可证并退出。

**`-N`** 开始描述一个新接口。

**`-o`** 覆盖新接口的驱动程序参数。

**`-O`** 覆盖新接口的 ctrl_interface 参数。

**`-p`** 指定驱动程序参数。

**`-P`** 保存进程 PID 的文件。

**`-q`** 降低调试详细程度（即抵消 `-d` 标志的使用）。

**`-s`** 通过 [syslog(3)](../gen/syslog.3.md) 而非终端发送日志消息。

**`-t`** 在调试消息中包含时间戳。

**`-v`** 在终端上显示版本信息并退出。

**`-W`** 在启动前等待控制接口监视器。

## 参见

[ath(4)](../man4/ath.4.md), [ipw(4)](../man4/ipw.4.md), [iwi(4)](../man4/iwi.4.md), [ral(4)](../man4/ral.4.md), [rum(4)](../man4/rum.4.md), [ural(4)](../man4/ural.4.md), [wlan(4)](../man4/wlan.4.md), [wpi(4)](../man4/wpi.4.md), [zyd(4)](../man4/zyd.4.md), wpa_supplicant.conf(5), devd(8), [ifconfig(8)](ifconfig.8.md), wpa_cli(8), wpa_passphrase(8)

## 历史

`wpa_supplicant` 工具首次出现在 FreeBSD 6.0 中。

## 作者

`wpa_supplicant` 工具由 Jouni Malinen <j@w1.fi> 编写。本手册页派生自 `wpa_supplicant` 发行版中包含的 `README` 文件。
