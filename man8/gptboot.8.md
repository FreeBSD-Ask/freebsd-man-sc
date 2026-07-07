# gptboot(8)

`gptboot` — 用于基于 BIOS 的计算机上从 UFS 启动的 GPT 引导代码

## 名称

`gptboot`

## 描述

`gptboot` 用于在基于 BIOS 的计算机上从 GPT 分区的磁盘上的 UFS 分区引导系统。`gptboot` 通过 [gpart(8)](gpart.8.md) 安装到一个 `freebsd-boot` 分区中。对于 UEFI，则改用 gptboot.efi(8)。虽然两者在概念上相似，但细节有所不同。

启动时，`gptboot` 首先读取 GPT，并确定从哪个驱动器和分区引导，具体如下文“引导”一节所述。如果未找到符合条件的分区，或者用户在三秒内按下任意键，`gptboot` 会从自动引导切换到交互模式。交互模式允许手动选择磁盘、分区、文件名和引导选项标志，详见 [boot(8)](boot.8.md)。

## 实现说明

GPT 标准允许可变数量的分区，但 `gptboot` 只能从包含 128 个或更少分区的分区表引导。

## 分区属性

`gptboot` 检查并管理 GPT UFS 分区的多个属性。

**`bootme`** 尝试从该分区引导。如果多个分区设置了 `bootme` 属性，`gptboot` 会依次尝试从每个分区引导，直到成功。

**`bootonce`** 仅尝试从该分区引导一次。使用 [gpart(8)](gpart.8.md) 设置此属性时会自动同时设置 `bootme` 属性。多个分区可以同时设置 `bootonce` 和 `bootme` 属性。

**`bootfailed`** `bootfailed` 属性标记那些设置了 `bootonce` 属性但引导失败的分区。此属性由系统管理。详见下文“引导”和“引导后操作”一节。

## 用法

对于正常使用，用户无需设置或管理任何分区属性。`gptboot` 会从找到的第一个 UFS 分区引导。

`bootonce` 属性可用于在已经正常工作的计算机上测试升级后的操作系统。现有系统分区保持不变，而要测试的新版本操作系统安装在另一个分区上。在该新的测试分区上设置 `bootonce` 属性。下一次引导将尝试从测试分区进行。成功或失败将显示在系统日志文件中。测试分区成功引导后，用户脚本可以检查日志并更改 `bootme` 属性，使测试分区成为新的系统分区。由于 `bootonce` 属性在尝试引导后会被清除，因此引导失败不会导致系统持续尝试从一个永远无法成功的分区引导。相反，系统会从较旧的、已知可正常工作且未被修改的操作系统引导。如果任何分区上设置了 `bootme` 属性，则会先尝试从这些分区引导。如果未找到带有 `bootme` 属性的分区，则会尝试从找到的第一个 UFS 分区引导。

## 引导

`gptboot` 首先读取分区表。所有仅设置了 `bootonce` 属性（表示引导失败）的 `freebsd-ufs` 分区会被设置为 `bootfailed`。然后 `gptboot` 会扫描所有 `freebsd-ufs` 分区。引导行为取决于这些分区上设置的 `bootme` 和 `bootonce` 属性的组合。

**`bootonce +`** `bootme` 最高优先级：依次尝试从具有这两个属性的每个 `freebsd-ufs` 分区引导。在每个分区上，会移除 `bootme` 属性并尝试引导。

**`bootme`** 中等优先级：依次尝试从具有 `bootme` 属性的每个 `freebsd-ufs` 分区引导。

如果任何分区上都未找到 `bootonce` 或 `bootme` 属性，则尝试从磁盘上第一个 `freebsd-ufs` 分区引导。

## 引导后操作

启动脚本 `/etc/rc.d/gptboot` 会检查所有 GPT 磁盘上 `freebsd-ufs` 分区的属性。带有 `bootfailed` 属性的分区会生成一条“boot from X failed”的系统日志消息。仅带有 `bootonce` 属性（表示该分区已成功引导）的分区会生成一条“boot from X succeeded”的系统日志消息。所有分区上的 `bootfailed` 属性会被清除。成功引导的分区上的 `bootonce` 属性会被清除。通常这种情况只会有一个。

## 文件

**`/boot/gptboot`** 引导代码二进制文件

**`/boot.config`** 引导块参数（可选）

## 实例

`gptboot` 安装在 `freebsd-boot` 分区中，通常是磁盘上的第一个分区。“保护性 MBR”（参见 [gpart(8)](gpart.8.md)）通常与 `gptboot` 配合使用。

在 `ada0` 驱动器上安装 `gptboot`：

```sh
gpart bootcode -b /boot/pmbr -p /boot/gptboot -i 1 ada0
```

也可以不带 PMBR 安装 `gptboot`：

```sh
gpart bootcode -p /boot/gptboot -i 1 ada0
```

为分区 2 设置 `bootme` 属性：

```sh
gpart set -a bootme -i 2 ada0
```

为分区 2 设置 `bootonce` 属性，同时自动设置 `bootme` 属性：

```sh
gpart set -a bootonce -i 2 ada0
```

## 参见

[boot.config(5)](../man5/boot.config.5.md), [rc.conf(5)](../man5/rc.conf.5.md), [boot(8)](boot.8.md), [gpart(8)](gpart.8.md)

## 历史

`gptboot` 出现于 FreeBSD 7.1。

## 作者

本手册页由 Warren Block <wblock@FreeBSD.org> 编写。
