# menu.4th(8)

`menu.4th` — FreeBSD 动态菜单引导模块

## 名称

`menu.4th`

## 描述

名为 `menu.4th` 的文件是一组命令，旨在显示通过精心命名的环境变量系统管理的动态菜单系统。对于大多数用途来说，仅 `menu.4th` 的命令本身是不够的。请参考下面的示例了解最常见的情况，并参考loader(8)获取其他命令。

在使用 `menu.4th` 提供的任何命令之前，必须通过以下命令将其包含进来：

```sh
include menu.4th
```

此行存在于默认的 **`/boot/menu.rc`** 文件中，因此在正常设置中不需要（也不应重复发出）。

它提供的命令如下：

**`menu-init`** 绘制菜单边界框并初始化一些内部状态变量。应在调用任何其他与菜单相关的函数之前调用此命令。

**`menu-display`** 显示菜单（通过下面记录的环境变量配置）并阻塞等待键盘输入，等待用户操作。

**`menu-erase`** 清除菜单边界框内的屏幕区域。

**`menu-redraw`** 调用 `menu-erase` 然后重新绘制菜单。

**`menu-unset`** 取消设置与各个菜单项关联的环境变量，为新菜单腾出空间。

**`menu-clear`** 调用 `menu-unset`，然后调用 `menu-erase`。

影响其行为的环境变量如下：

**`loader_color`** 如果设置为“`NO`”（不区分大小写）或“`0`”，则使菜单不带颜色显示。默认是在可能的情况下使用 ANSI 着色。如果启用了串口引导，则默认禁用颜色。颜色功能包括对菜单项左侧的数字使用 ANSI 粗体以及使用下面描述的特殊“`ansi`”变量。

**`autoboot_delay`** `menu-display` 在执行 `menu_timeout_command`（默认为 `boot`）之前等待的秒数，除非按下了某个键。如果设置为“`NO`”（不区分大小写），`menu-display` 将等待用户输入且永不执行 `menu_timeout_command`。如果设置为“`-1`”，`menu-display` 将立即引导，阻止对 `autoboot` 过程的中断和转义到 loader 提示符。默认为“`10`”。有关更多信息，请参见loader(8)。

**`menu_timeout_command`** 如果未按下键，在 `autoboot_delay` 秒后执行的命令。默认为 `boot`。

**`loader_menu_frame`** 设置在引导菜单周围绘制的所需边框样式。可能的值为：“`single`”（默认）、“`double`”和“`none`”。

**`loader_menu_timeout_x`** 设置倒计时文本的所需列位置。默认为 4。

**`loader_menu_timeout_y`** 设置倒计时文本的所需行位置。默认为 23。

**`loader_menu_title`** 在菜单上方显示的文本。默认为“`Welcome to FreeBSD`”。

**`loader_menu_title_align`** 默认将 `loader_menu_title` 在菜单上方居中对齐。可以设置为“`left`”或“`right`”，分别以左对齐或右对齐方式显示标题。

**`loader_menu_x`** 设置引导菜单的所需列位置。默认为 5。

**`loader_menu_y`** 设置引导菜单的所需行位置。默认为 10。

**`menu_caption[x]`** 为编号为“`x`”的菜单项显示的文本。

**`menu_command[x]`** 当按下与菜单项“`x`”关联的数字时执行的命令。请参阅下面包含的 FICL 字列表以获取一些想法。

**`menu_keycode[x]`** 与菜单项“`x`”关联的可选十进制 ASCII 键码。按下时，将导致执行 `menu_command[x]`。

**`ansi_caption[x]`** 如果设置了 `loader_color`（默认启用），则为菜单项“`x`”使用此标题而不是 `menu_caption[x]`。

**`toggled_text[x]`** 对于 `menu_command[x]` 设置为“`toggle_menuitem`”（或其派生命令）的菜单项，显示的文本将在此与 `menu_caption[x]` 之间切换。

**`toggled_ansi[x]`** 类似于 `toggled_text[x]`，但在启用 `loader_color` 时使用（默认）。

**`menu_caption[x][y]`** 对于 `menu_command[x]` 设置为“`cycle_menuitem`”（或其派生命令）的菜单项，显示的文本将在此与其他 `menu_caption[x][y]` 条目之间循环。

**`ansi_caption[x][y]`** 类似于 `menu_caption[x][y]`，但在启用 `loader_color` 时使用（默认）。

**`menu_acpi`** 当设置为与给定菜单项关联的数字“`x`”时，该菜单项仅在运行于 ACPI 兼容硬件、设置了 `acpi.rsdp`（表示loader(8)检测到了硬件 ACPI 支持）且未设置 `hint.acpi.0.disabled` 时才出现。在非 i386 硬件上，在“`menu_acpi`”菜单项之后配置的菜单项将使用较小的数字（以补偿缺失的 ACPI 菜单项），但仍继续按预期工作。在缺少 ACPI 支持的 i386 兼容硬件上（由loader(8)检测），后续菜单项将保留其关联的数字。

**`acpi.rsdp`** 在引导时检测到 ACPI 支持时，由loader(8)在 ACPI 兼容硬件上自动设置。影响“`menu_acpi`”菜单项的显示（如果已配置）。

**`hint.acpi.0.disabled`** 影响 `menu_acpi` 菜单项的显示。如果设置，菜单项将显示 `toggled_text[x]`（如果设置了 `loader_color`，则为 `toggled_ansi[x]`），否则显示 `menu_caption[x]`（如果设置了 `loader_color`，则为 `ansi_caption[x]`）。

**`menu_options`** 当设置为数字“`x`”时，在 `menu_caption[x-1]` 和 `menu_caption[x]`（如果已配置）之间插入一个空行和一个“`Options`”标题。

**`menu_reboot`** 如果设置，在最后一个已配置的菜单项末尾添加一个内建的“`Reboot`”菜单项。如果配置了 `menu_options`，“`Reboot`”菜单项将插入到“Options”分隔符之前。

此外，它还提供以下 FICL 字：

**`arch-i386? ( -- BOOL )`** 在 i386 上返回 true (-1)，否则返回 false (0)。

**`acpipresent? ( -- BOOL )`** 如果存在 ACPI 则返回 true (-1)，否则返回 false (0)。

**`acpienabled? ( -- BOOL )`** 如果已启用 ACPI 则返回 true (-1)，否则返回 false (0)。

**`toggle_menuitem ( N -- N )`** 在 `menu_caption[x]` 和 `toggled_text[x]` 之间切换菜单项“`N`”（其中“`N`”表示“`x`”的 ASCII 十进制值）。

**`cycle_menuitem ( N -- N )`** 在 `menu_caption[x][y]` 条目之间循环菜单项“`N`”（其中 `N` 表示 `x` 的 ASCII 十进制值）。

对于上面所有“`x`”值，请使用 1 到 9 之间的任何数字。抱歉，目前不支持双位数。

## 文件

**`/boot/loader`** loader(8)。

**`/boot/menu.4th`** `menu.4th` 本身。

**`/boot/loader.rc`** loader(8)引导脚本。

## 实例

一个简单的引导菜单：

```sh
include /boot/menu.4th
menu-init
set menu_caption[1]="Boot"
set menu_command[1]="boot"
set menu_options=2
set menu_caption[2]="Option: NO"
set toggled_text[2]="Option: YES"
set menu_command[2]="toggle_menuitem"
set menu_timeout_command="boot"
set menu_reboot
menu-display
```

## 参见

loader.conf(5), [beastie.4th(8)](beastie.4th.8.md), [loader(8)](loader.8.md), [loader.4th(8)](loader.4th.8.md)

## 历史

`menu.4th` 命令集首次出现在 FreeBSD 9.0 中。

## 作者

`menu.4th` 命令集由 Devin Teske <dteske@FreeBSD.org> 编写。
