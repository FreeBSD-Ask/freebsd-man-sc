# sysctl.conf(5)

`sysctl.conf` — 内核状态默认值

## 名称

`sysctl.conf`

## 描述

**/etc/sysctl.conf** 文件在系统进入多用户模式时被读取，用于设置内核的默认状态。**/etc/sysctl.conf** 文件采用 [sysctl(8)](../man8/sysctl.8.md) 命令的格式，即：

```sh
sysctl_mib=value
```

行首的 “#” 表示注释。注释也可以位于行尾，参见下文的实例章节。

对于通过 [rc.subr(8)](../man8/rc.subr.8.md) 系统加载的内核模块，可以通过添加一个相同格式的文件 **/etc/sysctl.kld.d/<modulename>.conf** 来应用额外的模块特定设置。

## 文件

**`/etc/rc.d/sysctl`** 在进入多用户模式过程中较早处理 `sysctl.conf` 的 [rc(8)](../man8/rc.8.md) 脚本。

**`/etc/rc.d/sysctl_lastload`** 在系统即将进入多用户模式前处理 `sysctl.conf` 的 [rc(8)](../man8/rc.8.md) 脚本。

**`/etc/sysctl.conf`** [sysctl(8)](../man8/sysctl.8.md) 的初始设置。

**`/etc/sysctl.conf.local`** 用于具有公共 **/etc/sysctl.conf** 的站点的特定机器设置。

**`/etc/sysctl.kld.d`** 用于通过 [rc.subr(8)](../man8/rc.subr.8.md) 加载的内核模块的模块特定设置。

## 实例

要关闭因致命信号退出程序的日志记录，可以使用如下配置：

```sh
# 配置日志记录。
kern.logsigexit=0	# 不记录致命信号退出（如 sig 11）
```

## 参见

[rc.conf(5)](rc.conf.5.md), [rc(8)](../man8/rc.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`sysctl.conf` 文件出现于 FreeBSD 4.0。

## 缺陷

如果使用可加载内核模块引入额外的内核功能以及管理该功能的 sysctl，`sysctl.conf` 可能在引导过程中处理得太早，以致无法设置这些 sysctl。请参阅 [rcorder(8)](../man8/rcorder.8.md) 了解有关 [rc(8)](../man8/rc.8.md) 脚本顺序的更多信息。
