# nanobsd.8

`nanobsd.sh` — 创建嵌入式 FreeBSD 系统镜像

## 名称

`nanobsd.sh`

## 概要

`nanobsd.sh [-BbfhIiKknpqvWwX] [-c config-file]`

## 描述

`nanobsd.sh` 工具是一个脚本，用于生成 FreeBSD 的最小化实现（称为 `NanoBSD`），通常可容纳在 SD 卡等小型介质或其他大容量存储介质上。它可用于构建专用安装镜像，便于安装和维护。

以下选项可用：

**`-B`** 跳过安装阶段（内核和 world 均如此）。

**`-b`** 跳过构建阶段（内核和 world 均如此）。

**`-c`** `config-file` 指定要使用的配置文件。

**`-f`** 跳过代码切片提取。

**`-h`** 显示用法信息。

**`-I`** 从现有构建/安装构建磁盘镜像。

**`-i`** 跳过磁盘镜像构建阶段。

**`-K`** 跳过构建的 `installkernel` 阶段。

**`-k`** 跳过构建的 `buildkernel` 阶段。

**`-n`** 在每个构建阶段之前不清理。这会抑制 `buildworld` 阶段之前完成的正常清理工作，并向每个构建阶段（world 和内核）使用的 make 命令行添加 `-DNO_CLEAN`。

**`-p`** 不准备镜像。跳过运行自定义和早期自定义脚本，以从 world、内核或包进行增量镜像优化。

**`-q`** 使输出更安静。

**`-v`** 使输出更详细。

**`-W`** 跳过构建的 `installworld` 阶段。

**`-w`** 跳过构建的 `buildworld` 阶段。

**`-X`** 制作 `native-xtools`。

`NanoBSD` 的特性包括：

- Ports 和包在 `NanoBSD` 中的工作方式与 FreeBSD 中相同。每个应用程序都可以像在 FreeBSD 中一样安装并使用于 `NanoBSD` 镜像中。
- 没有缺失的功能。如果在 FreeBSD 中能做某事，则在 `NanoBSD` 中也可做同样的事，除非在创建 `NanoBSD` 镜像时明确移除了特定功能。
- 运行时一切都是只读的。可以安全地拔掉电源。系统非正常关机后无需运行 fsck(8)。
- 易于构建和自定义。仅使用一个 shell 脚本和一个配置文件，即可构建满足任意需求集合的精简和自定义镜像。

### NanoBSD 介质布局

大容量存储介质默认分为三部分（通常以只读方式挂载）：

- 两个镜像分区：`code#1` 和 `code#2`。
- 配置文件分区，可在运行时挂载到 **/cfg** 目录下。

**/etc** 和 **/var** 目录是 [md(4)](../man4/md.4.md)（malloc 支持的）磁盘。

配置文件分区持久保存在 **/cfg** 目录下。它包含 **/etc** 目录的文件，并在系统启动后立即以只读方式短暂挂载，因此如果希望更改在系统重启后持久存在，需要将修改的文件从 **/etc** 复制回 **/cfg** 目录。

## 构建 NanoBSD

`NanoBSD` 镜像使用一个简单的 `NanoBSD` shell 脚本构建，该脚本可在 `src/tools/tools/nanobsd` 目录中找到。此脚本创建一个可启动镜像，可使用 [dd(1)](../man1/dd.1.md) 工具复制到存储介质上。

构建和安装 `NanoBSD` 镜像所需的命令为：

```sh
cd /usr/src/tools/tools/nanobsd
sh nanobsd.sh
cd /usr/obj/nanobsd.full
dd if=_.disk.full of=/dev/da0 bs=64k
```

## 自定义 NanoBSD

这可能是 `NanoBSD` 最重要和最有趣的功能。这也是你在使用 `NanoBSD` 开发时花费最多时间的地方。

自定义通过两种方式进行：

- 配置选项。
- 自定义函数。

通过配置设置，可以配置传递给 `NanoBSD` 构建过程的 `buildworld` 和 `installworld` 阶段的选项，以及传递给 `NanoBSD` 主构建过程的内部选项。通过这些选项可以裁剪系统，使其能容纳在仅 64MB 的空间内。你可以使用配置选项进一步精简系统，直到它仅由内核和用户空间中的两三个文件组成。

配置文件由配置选项组成，这些选项覆盖默认值。最重要的指令为：

**`NANO_NAME`** 构建名称（用于构造工作目录名称）。

**`NANO_SRC`** 用于构建镜像的源码树路径。

**`NANO_KERNEL`** 用于构建内核的内核配置文件名。

**`NANO_ARCH`** 要构建的机器处理器架构。默认为 `uname -p` 的输出。

**`NANO_BOOT0CFG`** 控制传递给 [boot0cfg(8)](boot0cfg.8.md) 的选项；这些选项决定 `boot0` 的行为。

**`NANO_BOOTLOADER`** 相对于 `NANO_WORLDDIR` 变量使用的 `boot0` 加载器。默认为 `boot/boot0sio`，应覆盖为 `boot/boot0` 以提供 VGA 控制台。

**`CONF_BUILD`** 传递给构建的 `buildworld` 阶段的选项。

**`CONF_INSTALL`** 传递给构建的 `installworld` 阶段的选项。

**`CONF_WORLD`** 同时传递给构建的 `buildworld` 和 `installworld` 阶段的选项。

**`FlashDevice`** 定义要使用的介质类型。更多详情请查看 `FlashDevice.sub` 文件。

有关更多配置选项，请查看 `nanobsd.sh` 脚本。

要使用 `nanobsd.conf` 配置文件构建 `NanoBSD` 镜像，使用以下命令：

```sh
sh nanobsd.sh -c nanobsd.conf
```

可以使用配置文件中的 shell 函数微调 `NanoBSD`。以下示例说明自定义函数的基本模型：

```sh
cust_foo () (
	echo "bar=topless" > \
	     ${NANO_WORLDDIR}/etc/foo
)
customize_cmd cust_foo
```

有几个预定义的自定义函数可直接使用：

**`cust_comconsole`** 禁用虚拟 [syscons(4)](../man4/syscons.4.md) 或 [vt(4)](../man4/vt.4.md) 终端（**/dev/ttyv\***）上的 getty(8)，并启用第一个串口作为系统控制台。

**`cust_allow_ssh_root`** 允许 root 通过 sshd(8) 登录。

**`cust_install_files`** 从 `nanobsd/Files` 目录安装文件，该目录包含一些有用的系统管理脚本。

## 文件

- **src/tools/tools/nanobsd** `NanoBSD` 构建脚本的基础目录。

## 实例

对 **/etc/resolv.conf** 进行持久更改：

```sh
vi /etc/resolv.conf
...
mount /cfg
cp /etc/resolv.conf /cfg
umount /cfg
```

以下是一个更有用的自定义函数示例，它将 **/etc** 目录的默认大小从 5MB 更改为 30MB：

```sh
cust_etc_size () (
	cd ${NANO_WORLDDIR}/conf
	echo 30000 > default/etc/md_size
)
customize_cmd cust_etc_size
```

## 参见

[make.conf(5)](../man5/make.conf.5.md), [boot(8)](boot.8.md), [boot0cfg(8)](boot0cfg.8.md)

## 历史

`NanoBSD` 工具首次出现于 FreeBSD 6.0。

## 作者

`NanoBSD` 由 Poul-Henning Kamp <phk@FreeBSD.org> 开发。本手册页由 Daniel Gerzo <danger@FreeBSD.org> 编写。
