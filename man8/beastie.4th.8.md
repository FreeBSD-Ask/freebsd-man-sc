  BEASTIE.4TH(8)  

BEASTIE.4TH(8)

FreeBSD System Manager's Manual

BEASTIE.4TH(8)

[名称](#__u540D___u79F0_)
=======================

`beastie.4th` —

FreeBSD ASCII 艺术引导模块

[描述](#__u63CF___u8FF0_)
=======================

名为 `beastie.4th` 的文件是一组命令，用于在引导加载程序菜单的右侧绘制 ASCII 艺术 FreeBSD 吉祥物（简称为 _beastie_ ）。 `beastie.4th` 的命令本身不足以满足大多数用途。 请参阅下面的示例了解最常见的情况，并参阅 loader(8) 了解其他命令。

在使用 `beastie.4th` 中提供的任何命令之前，必须通过命令包含它：

`include beastie.4th`

此行存在于默认的 /boot/loader.rc 文件中，因此在正常设置中不需要（也不应该重新发布）。

它提供的命令是：

[`draw-beastie`](#draw-beastie)

绘制 FreeBSD 徽标。

通过将 loader.conf(5) 中的 `loader_logo` 变量设置为 “`beastie`”, “`beastiebw`”, “`fbsdbw`”, “`orb`” 和 “`orbbw`” （默认值）之一来配置绘制的徽标。

可以通过在 loader.conf(5) 中设置 `loader_logo_x` 和 `loader_logo_y` 变量来配置 logo 的位置。 默认值为 46 (x) 和 4 (y)。

[`clear-beastie`](#clear-beastie)

清除野兽的屏幕。

[`beastie-start`](#beastie-start)

初始化交互式引导加载程序菜单。

`loader_delay` 变量可以在 loader.conf(5) 中配置为您希望延迟加载启动菜单的秒数。 在延迟期间，用户可以按 Ctrl-C 退回到 `autoboot` 或 ENTER 继续。 默认行为是不延迟。

影响其行为的环境变量是：

loader\_logo

在 beastie 启动菜单中选择所需的徽标。 可能的值为： “`fbsdbw`”, “`beastie`”, “`beastiebw`”, “`orb`”, “`orbbw`” （默认）和 “`none`” 。

loader\_logo\_x

设置徽标的所需列位置。 默认值为 46。

loader\_logo\_y

设置徽标的所需行位置。 默认值为 4。

beastie\_disable

如果设置为 “YES”, 将跳过 beastie 启动菜单。如果运行非 x86 硬件，总是会跳过 beastie 启动菜单。

loader\_delay

如果设置为大于零的数字，则会在启动 beastie 引导菜单之前引入延迟。 在延迟期间，用户可以按 Ctrl-C 跳过菜单或按 ENTER 进入菜单。 默认是加载菜单时不延迟。

[文件](#__u6587___u4EF6_)
=======================

/boot/loader

loader(8) 。

/boot/beastie.4th

`beastie.4th` 本身。

/boot/loader.rc

loader(8) 引导脚本。

[实例](#__u5B9E___u4F8B_)
=======================

标准 i386 /boot/loader.rc:

include /boot/beastie.4th beastie-start 

在 loader.conf(5) 中设置不同的 logo：

loader\_logo="beastie" 

[参见](#__u53C2___u89C1_)
=======================

loader.conf(5), loader(8), loader.4th(8)

[历史](#__u5386___u53F2_)
=======================

`beastie.4th` 指令集最早出现在 FreeBSD 5.1 中。

[作者](#__u4F5C___u8005_)
=======================

`beastie.4th` 指令集由 Scott Long ⟨scottl@FreeBSD.org⟩, Aleksander Fafula ⟨alex@fafula.com⟩ 和 Devin Teske ⟨dteske@FreeBSD.org⟩ 编写。

January 6, 2016

FreeBSD 13.1-RELEASE