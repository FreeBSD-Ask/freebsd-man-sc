# syscons.4

`syscons` — 旧版控制台驱动程序

## 名称

`syscons`, `sc`

## 概要

`options MAXCONS=N options SC_ALT_MOUSE_IMAGE options SC_CUT_SEPCHARS=_characters_ options SC_CUT_SPACES2TABS options SC_DFLT_TERM options SC_DISABLE_KDBKEY options SC_DISABLE_REBOOT options SC_HISTORY_SIZE=N options SC_MOUSE_CHAR=C options SC_NO_CUTPASTE options SC_NO_FONT_LOADING options SC_NO_HISTORY options SC_NO_PALETTE_LOADING options SC_NO_SUSPEND_VTYSWITCH options SC_NO_SYSMOUSE options SC_NO_TERM_DUMB options SC_NO_TERM_SC options SC_NO_TERM_SCTEKEN options SC_PIXEL_MODE options SC_TWOBUTTON_MOUSE options SC_NORM_ATTR=_attribute_ options SC_NORM_REV_ATTR=_attribute_ options SC_KERNEL_CONS_ATTR=_attribute_ options SC_KERNEL_CONS_ATTRS=_attributes_ options SC_KERNEL_CONS_REV_ATTR=_attribute_ options SC_DFLT_FONT makeoptions SC_DFLT_FONT=_font_name_ device sc`

`在 /boot/device.hints 中： hint.sc.0.at="isa" hint.sc.0.vesa_mode=0x103`

`在 /boot/loader.conf 中： kern.vty=sc`

## 弃用通知

`sc` 控制台已被弃用，并将在未来的 FreeBSD 版本中移除。建议用户迁移到 [vt(4)](vt.4.md) 控制台。

## 描述

`sc` 驱动提供多个虚拟终端。它类似于 SCO 彩色控制台驱动程序。

注意，`sc` 驱动与通过 UEFI(8) 引导的系统不兼容。在此类系统上强制使用 `sc` 将导致无可用的控制台。

`sc` 驱动构建于键盘驱动（[atkbd(4)](atkbd.4.md)）和显卡驱动（[vga(4)](vga.4.md)）之上，因此需要在系统中同时配置这两者。

系统中只能定义一个 `sc` 设备。

### 虚拟终端

`sc` 驱动提供多个虚拟终端，它们看起来就像是独立的终端。其中一个虚拟终端被视为当前终端，独占屏幕和键盘；其他虚拟终端被置于后台。

要使用虚拟终端，必须在 **`/etc/ttys`** 中将它们逐一标记为“on”，这样 getty(8) 才会识别它们为活动状态，并运行 [login(1)](../man1/login.1.md) 让用户登录系统。默认情况下，**`/etc/ttys`** 中只激活前八个虚拟终端。

按住 `Alt` 键加切换键可在虚拟终端之间切换。下表总结了切换键与虚拟终端之间的对应关系。

```sh
Alt-F1   ttyv0      Alt-F7   ttyv6      Shift-Alt-F1   ttyva
Alt-F2   ttyv1      Alt-F8   ttyv7      Shift-Alt-F2   ttyvb
Alt-F3   ttyv2      Alt-F9   ttyv8      Shift-Alt-F3   ttyvc
Alt-F4   ttyv3      Alt-F10  ttyv9      Shift-Alt-F4   ttyvd
Alt-F5   ttyv4      Alt-F11  ttyva      Shift-Alt-F5   ttyve
Alt-F6   ttyv5      Alt-F12  ttyvb      Shift-Alt-F6   ttyvf
```

你也可以使用“nscr”键（通常是 AT 增强型键盘上的 `PrintScreen` 键）在可用的虚拟终端之间循环切换。

可用虚拟终端的默认数量为 16。可以通过内核配置选项 `MAXCONS` 进行更改（见下文）。

注意，X 服务器通常需要一个虚拟终端用于显示，因此至少要保留一个终端不被 getty(8) 使用，以便 X 服务器使用。

### 键定义和功能键字符串

`sc` 驱动与键盘驱动配合，允许用户更改键定义和功能键字符串。kbdcontrol(1) 命令可加载键定义文件（即“keymap”文件）、转储当前键映射，以及为功能键分配字符串。关于键映射文件，请参见 [keyboard(4)](keyboard.4.md) 和 kbdmap(5)。

你可以将 **`/etc/rc.conf.local`** 中的 `keymap` 变量设为所需的键映射文件，使其在系统启动时自动加载。

### 软件字体

对于大多数现代显卡（如 VGA），`sc` 驱动和显卡驱动允许用户更改屏幕上使用的字体。可使用 vidcontrol(1) 命令从 **`/usr/share/syscons/fonts`** 加载字体文件。

字体有不同尺寸：8x8、8x14 和 8x16。8x16 字体通常用于 VGA 卡的 80 列 × 25 行模式。其他视频模式可能需要不同的字体大小。最好始终加载同一字体的所有三种尺寸。

你可以在 **`/etc/rc.conf`** 中设置 `font8x8`、`font8x14` 和 `font8x16` 变量为所需的字体文件，使其在系统启动时自动加载。

也可以将特定字体文件指定为默认字体。参见下文的 `SC_DFLT_FONT` 选项。

### 屏幕映射

如果你的显卡不支持软件字体，仍可以通过重新映射显卡内置的字体来获得类似效果。使用 vidcontrol(1) 加载屏幕映射文件，该文件定义了字符代码之间的映射关系。

### 鼠标支持和复制粘贴

你可以使用鼠标在屏幕上复制文本，并将其粘贴出来，就像手工键入一样。你必须运行鼠标守护进程 [moused(8)](../man8/moused.8.md)，并通过 vidcontrol(1) 在虚拟终端中启用鼠标光标。

按下鼠标按键 1（通常是左键）将开始选择。释放按键 1 将结束选择过程。被选中的文本会以前景色和背景色反转的方式标记。你可以按下按键 3（通常是右键）来扩展所选区域。所选文本会被放入复制缓冲区，可以多次按下按键 2（通常是中键）将其粘贴到光标位置。

如果你的鼠标只有两个按键，可以使用下文的 `SC_TWOBUTTON_MOUSE` 选项让右键粘贴文本。或者让鼠标守护进程模拟中键。更多详情请参见 [moused(8)](../man8/moused.8.md) 手册页。

### 回滚

`sc` 驱动允许用户浏览已经从屏幕顶部“滚动消失”的输出。

按下“slock”键（在许多键盘上通常是 `ScrllLock` / `Scroll Lock` 或 `Pause`），终端进入“回滚”模式。该模式由 `Scroll Lock` LED 指示。使用箭头键、`Page Up/Down` 键和 `Home/End` 键可滚动浏览缓冲的终端输出。再次按下“slock”键可返回正常的终端模式。

回滚缓冲区的大小可通过下文描述的 `SC_HISTORY_SIZE` 选项设置。

### 屏幕保护程序

如果当前虚拟终端空闲（即用户未在键盘上输入或移动鼠标），`sc` 驱动可启动屏幕保护程序。更多详情请参见 [splash(4)](splash.4.md) 和 vidcontrol(1)。

## 驱动配置

### 内核配置选项

以下内核配置选项控制 `sc` 驱动。

`#include <machine/pc/display.h>`

**`MAXCONS=N`** 此选项将虚拟终端的数量设置为 `N`。默认值为 16。

**`SC_ALT_MOUSE_IMAGE`** 此选项选择在虚拟终端中显示鼠标光标的替代方式。对某些显卡而言，绘制箭头形光标开销较大，你可能需要尝试此选项。但替代鼠标光标的外观可能不太美观。注意，如果使用了 `SC_NO_FONT_LOADING` 选项，则必须同时使用此选项才能使用鼠标。

**`SC_CUT_SEPCHARS=_characters_`** 此选项指定驱动程序在执行剪切操作时搜索单词边界时要查找的字符。默认值为“” `ex20` —— 一个空格字符。

**`SC_CUT_SPACES2TABS`** 此选项指示驱动程序在将数据复制到剪切缓冲区时将前导空格转换为制表符。这在复制以制表符缩进的文本时有助于保留缩进。

**`SC_DFLT_TERM=_name_`** 此选项指定首选终端模拟器的名称。

**`SC_DISABLE_KDBKEY`** 此选项禁用“debug”组合键（默认为 `Alt-Esc` 或 `Ctl-PrintScreen`）。它将阻止用户通过按下该组合键进入内核调试器（KDB）。如果内核中包含 KDB，则当内核发生 panic 或命中断点时仍会调用 KDB。如果未定义此选项，此行为可在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 变量 `hw.syscons.kbd_debug` 控制。

**`SC_DISABLE_REBOOT`** 此选项禁用“reboot”键（默认为 `Ctl-Alt-Del`），使普通用户不会意外重启系统。如果未定义此选项，此行为可在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 变量 `hw.syscons.kbd_reboot` 控制。

**`SC_HISTORY_SIZE=N`** 将回滚缓冲区大小设为 `N` 行。默认值为 100。

**`SC_MOUSE_CHAR=C`** 除非指定了上文的 `SC_ALT_MOUSE_IMAGE` 选项，否则 `sc` 驱动会保留四个连续的字符代码，以便在某些系统的虚拟终端中显示鼠标光标。此选项将用于此目的的第一个字符代码指定为 `C`。默认值为 0xd0。一个较好的候选值是 0x03。

**`SC_PIXEL_MODE`** 增加对像素（光栅）模式控制台的支持。此模式在某些笔记本电脑上很有用，但在大多数其他系统上用处不大，并且会向 syscons 添加大量代码。如果未定义此选项，可大幅减小内核体积。参见下文的 `VESAMODE` 标志。

**`SC_TWOBUTTON_MOUSE`** 如果你使用双键鼠标，可以添加此选项以使用鼠标右键粘贴文本。参见上文的鼠标支持和复制粘贴章节。

**`SC_NORM_ATTR=_attribute_`**

**`SC_NORM_REV_ATTR=_attribute_`**

**`SC_KERNEL_CONS_ATTR=_attribute_`**

**`SC_KERNEL_CONS_ATTRS=_attributes_`**

**`SC_KERNEL_CONS_REV_ATTR=_attribute_`** 这些选项将设置默认颜色。可用颜色定义参见下文实例章节。`SC_KERNEL_CONS_ATTRS` 是以二进制格式给出的一串属性序列。该序列将重复至 CPU 数量。注意字符串不能为空，因为内核会除以其长度。

**`SC_DFLT_FONT`** 此选项将指定默认字体。可用字体包括：iso、iso2、koi8-r、koi8-u、cp437、cp850、cp865、cp866 和 cp866u。16 行、14 行和 8 行的字体数据将被编译进来。如果不指定此选项，`sc` 驱动将使用显卡中已加载的字体，除非你在启动时显式加载软件字体。参见下文实例章节。

**`SC_NO_SUSPEND_VTYSWITCH`** 此选项也可作为 [loader(8)](../man8/loader.8.md) 可调参数和 [sysctl(8)](../man8/sysctl.8.md) 变量 `hw.syscons.sc_no_suspend_vtswitch` 使用，用于在挂起/恢复（ACPI 和 APM）期间禁用虚拟终端之间的切换（图形 <-> 文本）。如果你在运行 X 并尝试挂起时系统冻结，请使用此选项。

以下选项将从 `sc` 驱动中移除某些功能并节省内核内存。

**`SC_NO_CUTPASTE`** 此选项禁用虚拟终端中的“复制和粘贴”操作。

**`SC_NO_FONT_LOADING`** `sc` 驱动可在某些显卡上加载软件字体。此选项移除此功能。注意，如果仍希望在此选项下使用鼠标，则必须同时使用 `SC_ALT_MOUSE_IMAGE` 选项。

**`SC_NO_HISTORY`** 此选项禁用虚拟终端中的回滚功能。

**`SC_NO_SYSMOUSE`** 此选项移除 `sc` 驱动中的鼠标支持。如果定义了此选项，鼠标守护进程 [moused(8)](../man8/moused.8.md) 将失败。此选项隐含 `SC_NO_CUTPASTE` 选项。

**`SC_NO_TERM_DUMB`**

**`SC_NO_TERM_SC`**

**`SC_NO_TERM_SCTEKEN`** 这些选项分别移除“dumb”、“sc”和“scteken”终端模拟器。

### 驱动标志

以下驱动标志可用于控制 `sc` 驱动。驱动标志可通过 `hint.sc.0.flags` 可调参数设置，可在 **`/boot/device.hints`** 中，也可在加载器提示符下设置（参见 [loader(8)](../man8/loader.8.md)）。

**0x0080**（VESAMODE）此选项在内核初始化期间将显卡置于由 **`/boot/device.hints`** 变量 `vesa_mode` 指定的 VESA 模式。注意，要使此标志生效，内核必须以上文说明的 `SC_PIXEL_MODE` 选项编译。可用模式列表可通过 vidcontrol(1) 获取。

**0x0100**（AUTODETECT_KBD）此选项指示 syscons 驱动在未附加键盘设备时定期扫描键盘设备。否则，驱动仅在引导期间探测键盘一次。

### 加载器可调参数

这些设置可在 [loader(8)](../man8/loader.8.md) 提示符下或 loader.conf(5) 中输入。

**`kern.vty`** 当 `sc` 和 [vt(4)](vt.4.md) 都已编译进内核时，可通过将此变量设为 `sc` 或 `vt` 来选择用于系统控制台的那个。未设置此值时 `GENERIC` 内核使用 [vt(4)](vt.4.md)。

## 文件

**`/dev/console`**
**`/dev/consolectl`**
**`/dev/ttyv?`** 虚拟终端
**`/etc/ttys`** 终端初始化信息
**`/usr/share/syscons/fonts/*`** 字体文件
**`/usr/share/syscons/keymaps/*`** 键映射文件
**`/usr/share/syscons/scrmaps/*`** 屏幕映射文件

## 实例

由于 `sc` 驱动需要键盘驱动和显卡驱动，内核配置文件应包含以下行。

```sh
device atkbdc
device atkbd
device vga
device sc
device splash
```

这些驱动还需要在 **`/boot/device.hints`** 中加入以下行。

```sh
hint.atkbdc.0.at="isa"
hint.atkbdc.0.port="0x060"
hint.atkbd.0.at="atkbdc"
hint.atkbd.0.irq="1"
hint.vga.0.at="isa"
hint.sc.0.at="isa"
```

如果不打算加载启动画面或使用屏幕保护程序，最后一行不是必需的，可以省略。

注意，键盘控制器驱动 `atkbdc` 是键盘驱动 `atkbd` 所必需的。

以下行将设置默认颜色。普通文本为绿底黑字。反转文本为绿底黄字。注意，由于 [config(8)](../man8/config.8.md) 的当前实现，引号内的字符串中不能包含任何空白字符。

```sh
options SC_NORM_ATTR=(FG_GREEN|BG_BLACK)
```

```sh
options SC_NORM_REV_ATTR=(FG_YELLOW|BG_GREEN)
```

以下行将设置内核消息的默认颜色。内核消息将以黑底亮红色打印。反转消息为红底黑字。

```sh
options SC_KERNEL_CONS_ATTR=(FG_LIGHTRED|BG_BLACK)
```

```sh
options SC_KERNEL_CONS_REV_ATTR=(FG_BLACK|BG_RED)
```

如果未设置 `SC_KERNEL_CONS_ATTR`，或设为默认的黑底亮白色，则以下行将根据 CPU 设置 4 种偏红色颜色用于打印彩色内核消息。

```sh
options SC_KERNEL_CONS_ATTRS=e"ex0cex04ex40ex0ee"
```

对于不超过 8 个 CPU 的情况，默认方案可能更好。要为 8 个以上 CPU 获得唯一颜色，请使用更长的字符串。

要关闭内核消息的所有按 CPU 着色，可将 SC_KERNEL_CONS_ATTR 设为非默认值，或使用长度为 1 的默认模式。

```sh
options SC_KERNEL_CONS_ATTRS=e"ex0fe"
```

以下示例将字体文件 `cp850-8x16.fnt`、`cp850-8x14.font` 和 `cp850-8x8.font` 添加到内核中。

```sh
options SC_DFLT_FONT
```

```sh
makeoptions SC_DFLT_FONT=cp850
```

```sh
device sc
```

## 参见

kbdcontrol(1), [login(1)](../man1/login.1.md), vidcontrol(1), [atkbd(4)](atkbd.4.md), [atkbdc(4)](atkbdc.4.md), [keyboard(4)](keyboard.4.md), [screen(4)](screen.4.md), [splash(4)](splash.4.md), [ukbd(4)](ukbd.4.md), [vga(4)](vga.4.md), [vt(4)](vt.4.md), kbdmap(5), [rc.conf(5)](../man5/rc.conf.5.md), ttys(5), [config(8)](../man8/config.8.md), getty(8), [kldload(8)](../man8/kldload.8.md), [moused(8)](../man8/moused.8.md)

## 历史

`atkbd` 驱动首次出现于 FreeBSD 1.0。

## 作者

`atkbd` 驱动由 Søren Schmidt <sos@FreeBSD.org> 编写。本手册页由 Kazutaka Yokota <yokota@FreeBSD.org> 编写。

## 注意事项

可从剪切缓冲区插入的数据量受 {`MAX_INPUT`} 限制，这是终端输入队列中可存储字节数的系统限制——通常为 1024 字节（参见 [termios(4)](termios.4.md)）。

## 缺陷

本手册页不完整，急需修订。
