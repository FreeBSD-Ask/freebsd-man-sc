# reboot(8)

`reboot` — 停止并重启系统

## 名称

`reboot`, `halt`, `fastboot`, `fasthalt`

## 概要

`halt [-DflNnpq] [-e variable=value] [-k kernel] [-o options]`
`reboot [-cDdflNnpqr] [-e variable=value] [-k kernel] [-o options]`
`fasthalt [-DflNnpq] [-e variable=value] [-k kernel] [-o options]`
`fastboot [-dDflNnpq] [-e variable=value] [-k kernel] [-o options]`

## 描述

`halt` 和 `reboot` 工具分别用于停止和重启系统。

这两个工具都有两种不同的操作模式。在正常模式下，它们向 [init(8)](init.8.md) 进程发送信号，由该进程关闭正在运行的服务并停止或重启系统。在快速模式下，它们将文件系统缓存刷新到磁盘，向所有正在运行的进程发送 `SIGTERM`（随后发送 `SIGKILL`），然后自行停止或重启系统。服务是被杀死而非正常关闭的，这可能导致数据丢失。

无论在哪种模式下，操作都会被记录，包括在用户记账数据库中写入一条停机记录。

可用选项如下：

**`-c`** 系统会关闭电源然后再重新打开（如果支持）。如果关电操作失败，系统将正常停机或重启，取决于调用的是 `halt` 还是 `reboot`。目前仅 [ipmi(4)](../man4/ipmi.4.md) 驱动实现了电源循环功能，且仅在具有支持电源循环的 BMC 的硬件上有效。与关机不同，支持电源循环的硬件数量很少。

**`-D`** 删除现有的 `nextboot` 配置并退出。

**`-d`** 请求系统创建崩溃转储。该选项仅在重启时支持，并且除非先前已用 dumpon(8) 指定了转储设备，否则无效。

**`-e`** `variable=value` 在 loader 和内核环境中将 `variable` 设置为 `value`。如果 `value` 尚未用双引号括起，则在写入 `nextboot` 配置之前会自动添加。如果 `value` 包含对 shell 或 loader 配置解析代码具有特殊含义的字符，需格外小心。

**`-f`** 强制模式。通常，`halt` 或 `reboot` 会检查下一个内核是否存在，以及 **/var/run/noshutdown** 文件是否不存在。未指定此标志时，如果其中任一检查失败，操作将被拒绝。

**`-k`** `kname` 在下次系统引导时引导指定的内核 `kname`。这是一个一次性选项，*默认* 内核将在后续引导中使用。如果 **/boot/kname/kernel** 不存在，则不会执行 `reboot` 或 `halt`，除非指定了 `-f` 标志。

**`-l`** 停机或重启 *不* 记录到系统日志。此选项适用于 [shutdown(8)](shutdown.8.md) 之类的应用程序，它们自行调用 `reboot` 或 `halt` 并记录日志。

**`-N`** 在初始进程清理期间不刷新文件系统缓存，但内核级别的 reboot(2) 仍会通过 sync 处理。当设备可能不可用时（例如设备已断开连接，如 [iscsi(4)](../man4/iscsi.4.md)），此选项可用于执行“尽力而为”的重启。

**`-n`** 不刷新文件系统缓存。可能不应使用此选项。

**`-o`** `options` 此选项允许为下次引导传递内核标志。

**`-p`** 系统会关闭电源（如果支持）。如果关电操作失败，系统将正常停机或重启，取决于调用的是 `halt` 还是 `reboot`。

**`-q`** 系统快速且不优雅地停机或重启，仅执行文件系统缓存刷新（如果未指定 `-n` 选项）。可能不应使用此选项。

**`-r`** 系统杀死所有进程，卸载所有文件系统，挂载新的根文件系统，并开始通常的启动序列。在使用 [kenv(1)](../man1/kenv.1.md) 修改 vfs.root.mountfrom 后，`reboot` `-r` 可用于在保留内核状态的情况下更改根文件系统。这需要加载 [tmpfs(4)](../man4/tmpfs.4.md) 内核模块，因为 [init(8)](init.8.md) 需要在旧根文件系统卸载后、新根文件系统就位前有一个存储自身的位置。

`fasthalt` 和 `fastboot` 工具分别在快速模式下调用 `halt` 和 `reboot`。

[shutdown(8)](shutdown.8.md) 工具不仅可用于立即停止或重启系统，还可用于安排将来的停止或重启，并且与 `halt` 和 `reboot` 不同，它会提前向用户发出即将停机的警告。

## 实例

将当前根文件系统替换为从 **/dev/ada0s1a** 挂载的 UFS：

```sh
kenv vfs.root.mountfrom=ufs:/dev/ada0s1a
reboot -r
```

此机制也可用于 NFS，但需注意它仅适用于 NFSv4，且需要数字 IPv4 地址：

```sh
kenv vfs.root.mountfrom=nfs:192.168.1.1:/share/name
reboot -r
```

## 参见

[kenv(1)](../man1/kenv.1.md), reboot(2), getutxent(3), [ipmi(4)](../man4/ipmi.4.md), [boot(8)](boot.8.md), dumpon(8), nextboot(8), savecore(8), [shutdown(8)](shutdown.8.md), sync(8)

## 历史

`reboot` 工具出现于 4.0BSD。

历史上，当系统需要在正常运行过程中被干净地停止或重启时，使用 [shutdown(8)](shutdown.8.md) 工具；而 `halt` 和 `reboot` 工具是粗略的工具，仅在单用户模式下使用，或在特殊情况下使正常关机不切实际时使用。随着其他操作系统取消了这种区别，并且显然许多用户并不了解这一点，他们使用 `reboot` 时以为它执行的是干净关机，因此它被重写以符合这一预期。
