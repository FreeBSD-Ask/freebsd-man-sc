# devfs.rules(5)

`devfs.rules` — devfs 配置信息

## 名称

`devfs.rules`

## 描述

`devfs.rules` 文件提供了一种简便的方法来创建和应用 devfs(8) 规则，甚至适用于引导时不可用的设备。

对于引导时可用的设备，请参见 [devfs.conf(5)](devfs.conf.5.md)。

此文件的格式很简单。空行和以井号（`#`）开头的行会被忽略。方括号之间的行表示规则集的开始。方括号内应为规则集的名称和编号，以等号分隔。

其他行是 devfs(8) 中 “规则规范” 小节所记录的规则规范。这些行以 “`rule`” 为前缀，并由系统的启动脚本传递给 devfs(8)。重要的是，将包含 glob(3) 特殊字符的路径元素放在引号之间。

规则集应具有唯一的名称和编号。

跟随在规则集声明之后的所有规则都属于该规则集，直到开始一个新的规则集。

必须在 **/etc/rc.conf** 中启用一个自定义规则集，否则默认的系统启动过程不会将其应用到 **/dev** 文件系统。例如，要为 **/dev** 文件系统启用 “`localrules`” 规则集，你需要在 `rc.conf` 文件中使用类似如下的内容：

```sh
devfs_system_ruleset="localrules"
```

规则在引导时通过 devfs 服务加载。要在系统启动后加载修改过的规则，请运行以下命令：

```sh
service devfs restart
```

## 文件

**/etc/defaults/devfs.rules** 默认的 `devfs.rules` 配置文件。

**/etc/devfs.rules** 本地的 `devfs.rules` 配置文件。此处的规则集会覆盖 **/etc/defaults/devfs.rules** 中具有相同规则集编号的规则集，否则两个文件会有效合并。

## 实例

要使 [da(4)](../man4/da.4.md) 设备的所有分区可由其所有者和 “`usb`” 组读写，可使用以下规则：

```sh
[localrules=10]
```

```sh
add path 'da*s*' mode 0660 group usb
```

第一行声明并开始一个新的规则集，名称为 `localrules`，编号为 10。

要给予 usbconfig(8) 和启用了 libusb(3) 的应用程序权限，使其所有者可访问所有 USB 设备并归属于 “`usb`” 组，可使用类似如下的规则：

```sh
add path 'usb/*' mode 0660 group usb
```

## 参见

glob(3), [devfs(4)](../man4/devfs.4.md), [devfs.conf(5)](devfs.conf.5.md), devfs(8), [service(8)](../man8/service.8.md)

## 作者

本手册页由 Roland Smith <rsmith@xs4all.nl> 编写。
