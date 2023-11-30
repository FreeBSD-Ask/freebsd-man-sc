  MENU.4TH(8)  

MENU.4TH(8)

FreeBSD System Manager's Manual

MENU.4TH(8)

[名称](#__u540D___u79F0_)
=======================

`menu.4th` —

FreeBSD 动态菜单引导模块

[描述](#__u63CF___u8FF0_)
=======================

名为 `menu.4th` 的文件是一组命令，旨在显示通过精心命名的环境变量系统管理的动态菜单系统。 `menu.4th` 本身的命令对于大多数用途来说是不够的。 请参阅下面的示例了解最常见的情况，并参阅 loader(8) 了解其他命令。 在使用菜单中提供的任何命令之前。

在使用 `menu.4th` 中提供的任何命令之前，必须通过命令包含它：

`include menu.4th`

此行存在于默认的 /boot/menu.rc 文件中，因此在正常设置中不需要（也不应该重新发布）。

它提供的命令是：

[`menu-init`](#menu-init)

绘制菜单边界框并初始化一些内部状态变量。 这应该在任何其他与菜单相关的功能之前调用。

[`menu-display`](#menu-display)

显示菜单（通过以下记录的环境变量配置）和键盘输入块，等待用户操作。

[`menu-erase`](#menu-erase)

清除菜单边界框内的屏幕区域。

[`menu-redraw`](#menu-redraw)

调用 `menu-erase` 然后重绘菜单。

[`menu-unset`](#menu-unset)

取消设置与单个菜单项关联的环境变量，为新菜单扫清道路。

[`menu-clear`](#menu-clear)

调用 `menu-unset` 然后 `menu-erase` 。

影响其行为的环境变量是：

loader\_color

如果设置为 “`NO`” （不区分大小写）或 “`0`” ，则菜单显示为无颜色。 默认设置是尽可能使用 ANSI 着色。 如果启用串行引导，则默认禁用颜色。 颜色功能包括对出现在菜单项左侧的数字使用 ANSI 粗体，以及使用下面描述的特殊 “`ansi`” 变量。

autoboot\_delay

执行 menu\_timeout\_command (`boot` 启动）之前 `menu-display` 将等待的秒数，除非按下某个键。 如果设置为 “`NO`” （不区分大小写）， `menu-display` 将等待用户输入并且从不执行 `menu_timeout_command` 。 如果设置为 “`-1`”, `menu-display` 将立即启动，防止 `autoboot` 动过程中断和逃到加载程序提示符。 默认为 “`10`” 。 有关其他信息，请参阅 loader(8) 。

menu\_timeout\_command

如果未按下键，则在 autoboot\_delay 秒后执行的命令。 默认为 `boot` 。

loader\_menu\_frame

设置所需的框样式以围绕启动菜单进行绘制。 可能的值为： “`single`” (默认值), “`double`”, 和 “`none`” 。

loader\_menu\_timeout\_x

设置超时倒计时文本的所需列位置。 默认值为 4。

loader\_menu\_timeout\_y

设置超时倒计时文本的所需行位置。 默认值为 23。

loader\_menu\_title

显示在菜单上方的文本。 默认为 “`Welcome to FreeBSD`” 。

loader\_menu\_title\_align

默认是在菜单上方居中对齐 `loader_menu_title` 。 这可以设置为 “`left`” 或 “`right`” 来代替显示标题左对齐或右对齐 (分别) 。

loader\_menu\_x

设置引导菜单的所需列位置。默认值为 5。

loader\_menu\_y

设置引导菜单的所需行位置。默认值为 10。

menu\_caption\[x\]

要为编号菜单项 “`x`” 显示的文本。

menu\_command\[x\]

当按下与菜单项 “`x`” 相关的数字时要执行的命令。 有关一些想法，请参阅下面包含的 FICL 单词列表。

menu\_keycode\[x\]

与菜单项 “`x`” 关联的可选十进制 ASCII 键码。 按下时，将导致执行 menu\_command\[x\] 。

ansi\_caption\[x\]

如果 loader\_color 已设置 (默认启用) ，请将此标题用于菜单项 “`x`” 而不是 menu\_caption\[x\] 。

toggled\_text\[x\]

对于 menu\_command\[x\] 设置为 “`toggle_menuitem`” （或其派生项）的菜单项，显示的文本将在此和 menu\_caption\[x\] 之间切换。

toggled\_ansi\[x\]

与 toggled\_text\[x\] 类似，但在启用 loader\_color 时使用 (默认) 。

menu\_caption\[x\]\[y\]

对于 menu\_command\[x\] 设置为 “`cycle_menuitem`” （或其派生项）的菜单项，显示的文本将在此和其他 menu\_caption\[x\]\[y\] 条目之间循环。

ansi\_caption\[x\]\[y\]

与 menu\_caption\[x\]\[y\] 类似，但在启用 loader\_color 时使用 (默认) 。

menu\_acpi

当设置为与给定菜单项关联的数字 “`x`” 时，该菜单项仅在 i386 兼容硬件上运行时才会出现， hint.acpi.0.rsdp 已设置（指示加载程序检测到硬件 ACPI 支持的 loader(8) )，并且未设置 hint.acpi.0.disabled 。 在非 i386 硬件上，在 “`menu_acpi`” 菜单项之后配置的菜单项将使用较小的数字（以补偿缺少的 ACPI 菜单项）但继续按预期运行。 在缺少 ACPI 支持的 i386 兼容硬件上（由 loader(8) 检测到），后续菜单项将保留其关联的编号。

hint.acpi.0.rsdp

在启动时检测到 ACPI 支持时，由 i386 兼容硬件上的 loader(8) 自动设置。影响 “`menu_acpi`” 菜单项的显示（如果已配置）。

hint.acpi.0.disabled

影响 menu\_acpi 菜单项的显示。 如果设置，菜单项将显示 toggled\_text\[x\] (如果设置了 loader\_color ，则为 toggled\_ansi\[x\] ), 否则为 menu\_caption\[x\] （如果设置了 loader\_color ，则为 ansi\_caption\[x\] )。

menu\_options

当设置为数字 “`x`” 时，会在 menu\_caption\[x-1\] 和 menu\_caption\[x\] （如果已配置）之间插入一个空白行和一个 “`Options`” 标题。

menu\_reboot

如果设置，将内置的 “`Reboot`” 菜单项添加到最后配置的菜单项的末尾。 如果配置了 menu\_options ，则 “`Reboot`” 菜单项将插入 “Options” 分隔符之前。

此外，它还提供以下 FICL 字词：

[`arch-i386?`](#arch-i386?) (`-- BOOL`)

在 i386 上返回 true (-1)，否则返回 false (0)。

[`acpipresent?`](#acpipresent?) (`-- BOOL`)

如果存在 ACPI，则返回 true (-1)，否则返回 false (0)。

[`acpienabled?`](#acpienabled?) (`-- BOOL`)

如果启用 ACPI，则返回 true (-1)，否则返回 false (0)。

[`toggle_menuitem`](#toggle_menuitem) (`N -- N`)

在 menu\_caption\[x\] 和 toggled\_text\[x\] 之间切换菜单项 “`N`” （其中 “`N`” 表示 “`x`” 的 ASCII 十进制值）。

[`cycle_menuitem`](#cycle_menuitem) (`N -- N`)

在 menu\_caption\[x\]\[y\] 条目之间循环 menuitem “`N`” （其中 N 表示 x 的 ASCII 十进制值）。

对于上述 “`x`” 的所有值，请使用 1 到 9 之间的任意数字。 抱歉，目前不支持两位数。

[文件](#__u6587___u4EF6_)
=======================

/boot/loader

loader(8) 。

/boot/menu.4th

`menu.4th` 本身。

/boot/loader.rc

loader(8) 引导脚本。

[实例](#__u5B9E___u4F8B_)
=======================

一个简单的启动菜单：

include /boot/menu.4th menu-init set menu\_caption\[1\]="Boot" set menu\_command\[1\]="boot" set menu\_options=2 set menu\_caption\[2\]="Option: NO" set toggled\_text\[2\]="Option: YES" set menu\_command\[2\]="toggle\_menuitem" set menu\_timeout\_command="boot" set menu\_reboot menu-display 

[参见](#__u53C2___u89C1_)
=======================

loader.conf(5), beastie.4th(8), loader(8), loader.4th(8)

[历史](#__u5386___u53F2_)
=======================

`menu.4th` 指令集最早出现在 FreeBSD 9.0 中。

[作者](#__u4F5C___u8005_)
=======================

`menu.4th` 命令集由 Devin Teske ⟨dteske@FreeBSD.org⟩ 编写。

August 6, 2013

FreeBSD 13.1-RELEASE