  GPTBOOT(8)  

GPTBOOT(8)

FreeBSD System Manager's Manual

GPTBOOT(8)

[名称](#__u540D___u79F0_)
=======================

`gptboot` —

基于 BIOS 的计算机上 UFS 的 GPT 引导代码

[描述](#__u63CF___u8FF0_)
=======================

`gptboot` 在基于 BIOS 的计算机上用于从 GPT 分区磁盘上的 UFS 分区引导。 `gptboot` 使用 gpart(8) 安装在 `freebsd-boot` 分区中。

当它启动时， `gptboot` 首先读取 GPT 并确定从哪个驱动器和分区启动，如下面的 [BOOTING](#BOOTING) 中所述。 如果它没有找到符合条件的分区，或者如果用户在三秒内按下了一个键， `gptboot` 就会从自动引导切换到交互模式。 交互模式允许手动选择磁盘、分区、文件名和引导选项标志，如 boot(8) 中所述。

[实施说明](#__u5B9E___u65BD___u8BF4___u660E_)
=========================================

GPT 标准允许可变数量的分区，但 `gptboot` 仅从具有 128 个或更少分区的表引导。

[分区属性](#__u5206___u533A___u5C5E___u6027_)
=========================================

`gptboot` 检查和管理 GPT UFS 分区的几个属性。

[`bootme`](#bootme)

尝试从此分区启动。 如果多个分区设置了 `bootme` 属性， `gptboot` 将尝试引导每个分区，直到成功。

[`bootonce`](#bootonce)

仅尝试从该分区引导一次。 使用 gpart(8) 设置此属性也会自动设置 `bootme` 属性。 多个分区可能设置了 `bootonce` 和 `bootme` 属性。

[`bootfailed`](#bootfailed)

[`bootfailed`](#bootfailed_2) 属性标记了设置了 `bootonce` 属性但无法引导的分区。 该属性由系统管理。 有关详细信息，请参阅下面的 [BOOTING](#BOOTING) 和 [POST-BOOT ACTIONS](#POST_BOOT_ACTIONS) 。

[用法](#__u7528___u6CD5_)
=======================

对于正常使用，用户不必设置或管理任何分区属性。 `gptboot` 将从找到的第一个 UFS 分区启动。

`bootonce` 属性可用于在已经运行的计算机上测试升级的操作系统。 现有系统分区保持不变，待测试操作系统的新版本安装在另一个分区上。 `bootonce` 属性是在新的测试分区上设置的。 尝试从测试分区进行下一次引导。 成功或失败将显示在系统日志文件中。 成功启动测试分区后，用户脚本可以检查日志并更改 `bootme` 属性，以便测试分区成为新的系统分区。 因为 `bootonce` 属性在尝试引导后被清除，所以失败的引导不会让系统尝试从永远不会成功的分区引导。 相反，系统将从旧的、已知工作的、尚未修改的操作系统引导。 如果在任何分区上设置了 `bootme` 属性，将首先尝试从它们进行引导。 如果没有找到具有 `bootme` 属性的分区，则将从找到的第一个 UFS 分区尝试引导。

[开机](#__u5F00___u673A_)
=======================

`gptboot` 首先读取分区表。 所有只设置了 `bootonce` 属性（表示引导失败）的 `freebsd-ufs` 分区都设置为 `bootfailed` 。 然后 `gptboot` 扫描所有的 `freebsd-ufs` 分区。 引导行为取决于在这些分区上设置的 `bootme` 和 `bootonce` 属性的组合。

[`bootonce +`](#bootonce_+) `bootme`

最高优先级：尝试从具有这两个属性的每个 `freebsd-ufs` 分区进行引导。 在每个分区上，都会删除 `bootme` 属性并尝试引导。

[`bootme`](#bootme_2)

中优先级：尝试从具有 `bootme` 属性的每个 `freebsd-ufs` 分区进行引导。

如果在任何分区上都找不到 `bootonce` 和 `bootme` 属性，则尝试从磁盘上的第一个 `freebsd-ufs` 分区进行引导。

[启动后操作](#__u542F___u52A8___u540E___u64CD___u4F5C_)
==================================================

启动脚本 /etc/rc.d/gptboot 检查所有 GPT 磁盘上的 `freebsd-ufs` 分区的属性。 具有 `bootfailed` 属性的分区会生成 “boot from X failed” 系统日志消息。 仅具有 `bootonce` 属性的分区（指示成功引导的分区）会生成 “boot from X succeeded” 系统日志消息。 从所有分区中清除 `bootfailed` 的属性。 `bootonce` 属性会从成功引导的分区中清除。 通常只有其中之一。

[文件](#__u6587___u4EF6_)
=======================

/boot/gptboot

引导码二进制

/boot.config

引导块的参数（可选） (optional)

[实例](#__u5B9E___u4F8B_)
=======================

`gptboot` 安装在 `freebsd-boot` 分区中，通常是磁盘上的第一个分区。 “protective MBR” (参见 gpart(8)) 通常与 `gptboot` 一起安装。

在 ada0 驱动器上安装 `gptboot` :

gpart bootcode -b /boot/pmbr -p /boot/gptboot -i 1 ada0 

`gptboot` 也可以在没有 PMBR 的情况下安装：

gpart bootcode -p /boot/gptboot -i 1 ada0 

设置分区 2 的 `bootme` 属性：

gpart set -a bootme -i 2 ada0 

为分区 2 设置 `bootonce` 属性，同时自动设置 `bootme` 属性：

gpart set -a bootonce -i 2 ada0 

[参见](#__u53C2___u89C1_)
=======================

boot.config(5), rc.conf(5), boot(8), gpart(8)

[历史](#__u5386___u53F2_)
=======================

`gptboot` 出现在 FreeBSD 7.1 中。

[作者](#__u4F5C___u8005_)
=======================

本手册页由 Warren Block ⟨wblock@FreeBSD.org⟩ 编写。

April 30, 2019

FreeBSD 13.1-RELEASE