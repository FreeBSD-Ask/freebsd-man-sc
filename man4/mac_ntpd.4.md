# mac_ntpd(4)

`mac_ntpd` — 允许 ntpd 以非 root 用户身份运行的策略

## 名称

`mac_ntpd`

## 概要

要将 ntpd 策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_NTPD

或者，要在引导时加载 ntpd 策略模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_ntpd_load="YES"
```

## 描述

`mac_ntpd` 策略授予任何以用户“ntpd”（uid 123）身份运行的进程所需的特权，以操纵系统时间以及（重新）绑定到特权 NTP 端口。

当 ntpd(8) 在命令行中使用“`-u` `<user>[:group]`”启动时，它会执行所有需要 root 特权的初始化操作，然后切换到给定的用户 ID 以放弃 root 特权。此后，它所需的唯一特权是操纵系统时间的能力，以及在网络接口变更后重新将 UDP 套接字绑定到 NTP 端口（端口 123）的能力。

在 `mac_ntpd` 策略启用时，也可能以非 root 用户身份启动 ntpd，因为默认的 ntpd 选项除了该策略所授予的特权外，不需要任何额外的 root 特权。

### 授予的特权

授予任何以配置 uid 运行的进程的内核特权集合如下：

**`PRIV_ADJTIME`**
**`PRIV_CLOCK_SETTIME`**
**`PRIV_NTP_ADJTIME`**
**`PRIV_NETINET_RESERVEDPORT`**
**`PRIV_NETINET_REUSEPORT`**

### 运行时配置

以下 [sysctl(8)](../man8/sysctl.8.md) MIB 可用于微调此 MAC 策略。所有 [sysctl(8)](../man8/sysctl.8.md) 变量也可在 loader.conf(5) 中设置为 [loader(8)](../man8/loader.8.md) 可调参数。

**`security.mac.ntpd.enabled`** 启用 `mac_ntpd` 策略。（默认值：1。）

**`security.mac.ntpd.uid`** ntpd 用户的数字 uid。（默认值：123。）

## 参见

[mac(4)](mac.4.md), ntpd(8)

## 历史

MAC 首次出现于 FreeBSD 5.0，`mac_ntpd` 首次出现于 FreeBSD 12.0。
