# devfs.conf.5

`devfs.conf` — 引导时的 devfs 配置信息

## 名称

`devfs.conf`

## 描述

`devfs.conf` 文件提供了一种简便的方法来设置引导时可用的设备的所有权和权限，或为这些设备创建链接。

它不适用于系统启动运行后插入或拔出的设备，例如 USB 设备。关于为所有设备节点设置所有权和权限，请参见 [devfs.rules(5)](devfs.rules.5.md)；关于设备附加或分离时要执行的操作，请参见 devd.conf(5)。

以井号（`#`）开头的行和空行会被忽略。指定 `devfs.conf` 规则的行由以空白分隔的三个参数组成：

**`action`** 对设备执行的操作。操作名仅以其第一个唯一字符为准。

**`devname`** 由 [devfs(4)](../man4/devfs.4.md) 创建的设备名。

**`arg`** `action` 的参数。

目前支持的操作有：

**`link`** 此操作创建一个名为 `arg` 的符号链接，指向 `devname`，即由 [devfs(4)](../man4/devfs.4.md) 创建的设备名。

**`own`** 此操作更改 `devname` 的所有者。`arg` 参数必须采用 `owner`:`group` 对的形式，格式与 [chown(8)](../man8/chown.8.md) 所用相同。

**`perm`** 此操作更改 `devname` 的权限。`arg` 参数必须是 [chmod(1)](../man1/chmod.1.md) 中所说明的 `mode`。

## 文件

**/etc/devfs.conf**

**/usr/share/examples/etc/devfs.conf**

## 实例

要创建一个指向第一个 CD-ROM 的 **/dev/cdrom** 链接，可在 `devfs.conf` 中添加以下内容：

```sh
link	cd0	cdrom
```

要设置设备的所有者，可指定 `own` 操作：

```sh
own	cd0	root:cdrom
```

要设置设备的权限，应使用 `perm` 操作：

```sh
perm	cd0	0660
```

## 参见

[chmod(1)](../man1/chmod.1.md), [devfs(4)](../man4/devfs.4.md), devd.conf(5), [devfs.rules(5)](devfs.rules.5.md), [chown(8)](../man8/chown.8.md)

## 作者

本手册页由 Roland Smith <rsmith@xs4all.nl> 编写。
