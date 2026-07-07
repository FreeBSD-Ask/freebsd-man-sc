# boot.config(5)

`boot.config` — 旧版引导块的配置文件

## 名称

`boot.config`

## 描述

`boot.config` 文件包含 FreeBSD 引导块代码的选项。

当 FreeBSD 第一阶段和第二阶段引导加载器运行时，它们会在引导分区的 “`a`” 切片中搜索 `boot.config` 文件（因此，缺少 “`a`” 分区的切片在引导过程中需要用户干预）。如果找到 `boot.config` 文件，其内容将用作引导块代码的默认配置选项，并回显到系统控制台。

此文件的有效格式是将 BIOS 驱动器号、控制器类型、单元号、分区、内核文件名以及任何其他有效的 [boot(8)](../man8/boot_i386.8.md) 选项放在一行上，如同在 “`boot:`” 提示符处所做的那样。

下文所述与引导映像选择相关的选项，以及 `boot.config` 可用的所有其他选项，都在 [boot(8)](../man8/boot_i386.8.md) 手册页中有详细记录。

## 文件

**/boot.config** 引导块参数（可选）

**/boot/config** 引导配置信息的备用位置

## 实例

命令：

```sh
# echo "-P" > /boot.config
```

会在没有键盘时激活 FreeBSD 的串行控制台，否则将使用视频控制台。

命令：

```sh
# echo "1:ad(1,a)/boot/loader" > /boot.config
```

会指示第一块磁盘上 [boot(8)](../man8/boot_i386.8.md) 的第二阶段从第二块磁盘上的 [boot(8)](../man8/boot_i386.8.md) 第三阶段引导。

命令：

```sh
# echo "1:ad(1,a)/boot/loader -P" > /boot.config
```

会同时执行上述两项操作。

## 参见

[boot(8)](../man8/boot_i386.8.md), [loader(8)](../man8/loader.8.md)

## 作者

本手册页由 Daniel Gerzo <danger@FreeBSD.org> 编写。
