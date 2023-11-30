  CHECK-PASSWORD.4TH(8)  

CHECK-PASSWORD.4TH(8)

FreeBSD System Manager's Manual

CHECK-PASSWORD.4TH(8)

[名称](#__u540D___u79F0_)
=======================

`check-password.4th` —

FreeBSD 密码检查启动模块

[描述](#__u63CF___u8FF0_)
=======================

名为 `check-password.4th` 的文件是一组命令，旨在执行以下一项或多项操作：

`o 防止无密码启动`

`o 防止在没有密码的情况下修改引导选项`

`o 提供挂载geli(8) 加密根磁盘的密码`

`check-password.4th` 本身的命令对于大多数用途来说是不够的。 请参阅下面的示例了解最常见的情况，并参阅 loader(8) 了解其他命令。

在使用 `check-password.4th` 中提供的任何命令之前，必须通过命令包含它：

`include check-password.4th`

此行存在于 /boot/loader.4th 文件中，因此在正常设置中不需要（也不应该重新发布）。

它提供的命令是：

[`check-password`](#check-password)

多用途功能，可以保护交互式启动菜单，防止无密码启动，或提示输入 geli(8) 密码 (取决于 loader.conf(5) 设置) 。

首先检查 bootlock\_password 和 if-set，用户在输入正确密码之前无法继续。

接下来，检查 geom\_eli\_passphrase\_prompt ，如果设置为 `YES` (case-insensitive) ，则提示用户输入他们的 GELI 密码，以便以后在引导期间安装根设备。

最后，检查 password ，尝试 `autoboot` ，并且仅在失败或用户中断时提示输入密码。 有关更多信息，请参见 loader.conf(5) 。

影响其行为的环境变量是：

bootlock\_password

设置引导锁定密码（最多 255 个字符长），在允许系统引导之前， `check-password` 需要输入该密码。

geom\_eli\_passphrase\_prompt

选择 loader(8) 是否会提示输入 GELI 凭据，并移交给内核以供以后安装 geli(8) 加密的根设备。

password

设置允许用户访问启动菜单之前 `check-password`-
所需的密码（最长 255 个字符）。

[文件](#__u6587___u4EF6_)
=======================

/boot/loader

loader(8) 。

/boot/check-password.4th

`check-password.4th` 本身。

/boot/loader.rc

loader(8) 引导脚本。

[实例](#__u5B9E___u4F8B_)
=======================

标准 i386 /boot/loader.rc:

include /boot/loader.4th check-password 

在 loader.conf(5) 中设置密码以防止修改引导选项：

password="abc123" 

在 loader.conf(5) 中设置密码，防止无密码启动：

bootlock\_password="boot" 

将以下内容添加到 loader.conf(5) 以在启动时生成提示以收集 GELI 凭据以安装 geli(8) 加密的根设备：

geom\_eli\_passphrase\_prompt="YES" 

[参见](#__u53C2___u89C1_)
=======================

loader.conf(5), loader(8), loader.4th(8)

[历史](#__u5386___u53F2_)
=======================

第 4 组命令 `check-password.4th` 首次出现在 FreeBSD 9.0 中。

[作者](#__u4F5C___u8005_)
=======================

`check-password.4th` 命令集由 Devin Teske ⟨dteske@FreeBSD.org⟩ 编写。

June 24, 2018

FreeBSD 13.1-RELEASE