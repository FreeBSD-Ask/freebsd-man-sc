# mac_priority(4)

`mac_priority` — 非_root_用户的调度特权策略

## 名称

`mac_priority`

## 概要

要将 mac_priority 策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_PRIORITY

或者，要在引导时加载 mac_priority 策略模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_priority_load="YES"
```

## 描述

`mac_priority` 策略根据 [group(5)](../man5/group.5.md) 成员资格授予调度特权。“realtime”组（gid 47）中的用户或进程允许以实时调度优先级运行线程和进程。“idletime”组（gid 48）中的用户或进程允许以空闲调度优先级运行线程和进程。

在 `mac_priority` 实时策略启用时，特权用户可以使用 rtprio(1) 工具以实时优先级启动进程。特权应用程序可以通过 rtprio(2) 系统调用将线程和进程提升为实时优先级。

在 idletime 策略启用时，特权用户可以使用 idprio(1) 工具以空闲优先级启动进程。特权应用程序可以通过 rtprio(2) 系统调用将线程和进程降级为空闲优先级。

### 授予的特权

实时策略向任何以实时组 ID 运行的进程授予以下内核特权：

**`PRIV_SCHED_RTPRIO`**
**`PRIV_SCHED_SETPOLICY`**

idletime 策略授予的内核特权为：

**`PRIV_SCHED_IDPRIO`**

### 运行时配置

以下 [sysctl(8)](../man8/sysctl.8.md) MIB 可用于微调此 MAC 策略。所有 [sysctl(8)](../man8/sysctl.8.md) 变量也可在 loader.conf(5) 中设置为 [loader(8)](../man8/loader.8.md) 可调参数。

**`security.mac.priority.realtime`** 启用实时策略。（默认值：1。）

**`security.mac.priority.realtime_gid`** realtime 组的数字 gid。（默认值：47。）

**`security.mac.priority.idletime`** 启用 idletime 策略。（默认值：1。）

**`security.mac.priority.idletime_gid`** idletime 组的数字 gid。（默认值：48。）

## 参见

idprio(1), rtprio(1), rtprio(2), [mac(4)](mac.4.md)

## 历史

MAC 首次出现于 FreeBSD 5.0，`mac_priority` 首次出现于 FreeBSD 13.1。
