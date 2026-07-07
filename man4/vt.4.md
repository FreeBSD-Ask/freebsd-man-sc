# vt(4)

`vt` — 虚拟终端系统视频控制台驱动

## 名称

`vt`

## 概要

`options TERMINAL_KERN_ATTR=<attribute>`

`options TERMINAL_NORM_ATTR=<attribute>`

`options VT_MAXWINDOWS=<N>`

`options VT_ALT_TO_ESC_HACK=1`

`options VT_TWOBUTTON_MOUSE`

`options VT_FB_MAX_WIDTH=<X>`

`options VT_FB_MAX_HEIGHT=<Y>`

`options SC_NO_CUTPASTE`

`device vt`

`在 loader.conf(5) 中：`

`hw.vga.textmode=1`

`hw.vga.acpi_ignore_no_vga=1`

`kern.vty=vt`

`kern.vt.color.<colornum>.rgb=<colorspec>`

`kern.vt.fb.default_mode=<X>x<Y>`

`kern.vt.fb.modes.<connector>=<X>x<Y>`

`kern.vt.slow_down=<delay>`

`screen.font=<X>x<Y>`

`在 loader.conf(5) 或 sysctl.conf(5) 中：`

`kern.consmute=1`

`kern.vt.kbd_halt=1`

`kern.vt.kbd_poweroff=1`

`kern.vt.kbd_reboot=1`

`kern.vt.kbd_debug=1`

`kern.vt.kbd_panic=0`

`kern.vt.enable_altgr=0`

`kern.vt.enable_bell=1`

## 描述

`vt` 设备提供多个虚拟终端，具备以下丰富功能：

- 支持 Unicode UTF-8 文本和双宽字符。
- 在图形模式下支持大字体映射，包括对亚洲字符集的支持。
- 图形模式控制台。
- 与 KMS（内核模式设置）视频驱动集成，可在 *X Window System* 与虚拟终端之间切换。

### 虚拟终端

单台计算机上提供多个虚拟终端。最多可定义 16 个虚拟终端。同一时间只有一个虚拟终端连接到屏幕和键盘。使用组合键选择虚拟终端。Alt-F1 至 Alt-F12 对应前 12 个虚拟终端。如果创建的虚拟终端超过 12 个，使用 Shift-Alt-F1 至 Shift-Alt-F4 切换到额外的终端。

### 用鼠标复制和粘贴文本

支持使用鼠标从屏幕复制和粘贴文本。按住鼠标 1 键（通常是左键）并移动鼠标以选择文本。所选文本以前景色和背景色反相显示。要在释放鼠标 1 键后选择更多文本，按鼠标 3 键（通常是右键）。要粘贴已选择的文本，按鼠标 2 键（通常是中键）。文本将像从键盘输入一样输入。对于只有两个按键的鼠标，可使用 `VT_TWOBUTTON_MOUSE` 内核选项。设置此选项使第二个鼠标按键成为粘贴按键。更多信息参见 [moused(8)](../man8/moused.8.md)。

### 回滚查看

按 Scroll Lock 键，然后使用方向键上下滚动，可查看已滚动出屏幕的输出。Page Up 和 Page Down 键每次向上或向下滚动整屏。Home 和 End 键跳转到回滚缓冲区的开头或末尾。查看完毕后，再次按 Scroll Lock 键返回正常使用。某些笔记本电脑键盘没有 Scroll Lock 键，使用特殊的功能键组合（如 Fn + K）访问 Scroll Lock。

## 驱动配置

### 内核配置选项

这些内核选项控制 `vt` 驱动。

`#include <sys/terminal.h>`

**`TERMINAL_NORM_ATTR=`** <`attribute`>

**`TERMINAL_KERN_ATTR=`** <`attribute`> 这些选项更改普通文本和内核文本使用的默认颜色。可用颜色定义见下文实例章节。

**`VT_MAXWINDOWS=`** <`N`> 设置要创建的虚拟终端数为 `N`。默认值为 12。

**`VT_ALT_TO_ESC_HACK=`** `1` 当按住 Alt 键再按其他键时，发送 ESC 序列而不是 Alt 键。

**`VT_TWOBUTTON_MOUSE`** 如果定义，交换鼠标按键 2 和 3 的功能。实际上，这使鼠标右键执行粘贴。这些选项按所示顺序检查。

**`SC_NO_CUTPASTE`** 禁用鼠标支持。

**VT_FB_MAX_WIDTH=<`X`>** 设置最大宽度为 `X`。

**VT_FB_MAX_HEIGHT=<`Y`>** 设置最大高度为 `Y`。

## 向后兼容性

提供了若干选项以兼容先前的控制台设备 sc(4)。这些选项将在未来的 FreeBSD 版本中移除。

| **vt 选项名** | **sc 选项名** |
| ------------- | ------------- |
| `TERMINAL_KERN_ATTR` | `SC_KERNEL_CONS_ATTR` |
| `TERMINAL_NORM_ATTR` | `SC_NORM_ATTR` |
| `VT_TWOBUTTON_MOUSE` | `SC_TWOBUTTON_MOUSE` |
| `VT_MAXWINDOWS` | `MAXCONS` |
| none | `SC_NO_CUTPASTE` |

## X86 BIOS 系统的启动操作

计算机 BIOS 以文本模式启动，FreeBSD [loader(8)](../man8/loader.8.md) 运行，加载内核。如果设置了 `hw.vga.textmode`，系统保持文本模式。否则，`vt` 使用 `vt_vga` 切换到 640x480x16 VGA 模式。如果 KMS（内核模式设置）视频驱动可用，显示切换到高分辨率，KMS 驱动接管。当 KMS 驱动不可用时，`vt_vga` 保持活动状态。

## 加载器可调参数

这些设置可在 [loader(8)](../man8/loader.8.md) 提示符下输入，或在 loader.conf(5) 中设置。

**`hw.vga.textmode`** 设置为 1 以在 BIOS 引导时使用文本模式而非图形模式的虚拟终端。需要图形模式的功能（如可加载字体）将被禁用。如果加载了 KMS 驱动，控制台将切换到图形模式并保持在该模式。此外，此可调参数对 UEFI(8) 引导无效，因为它不使用 VGA 模式。

**`hw.vga.acpi_ignore_no_vga`** 设置为 1 以强制使用 VGA 驱动，无论 ACPI IAPC_BOOT_ARCH 是否表示不支持 VGA。可用于绕过 ACPI 表中的固件缺陷。注意，只有在虚拟化环境中运行时才会确认不支持 VGA。太多有缺陷的固件错误地在物理硬件上报告不支持 VGA。

**`kern.vty`** 将此值设置为 `vt` 或 `sc` 以选择特定的系统控制台，覆盖默认值。未设置此值时 `GENERIC` 内核使用 `vt`。注意，`sc` 不兼容 UEFI(8) 引导。

**`kern.vt.color`**.`colornum`.`rgb` 设置此值以覆盖颜色 `colornum` 的默认调色板条目，`colornum` 应在 0 至 15 范围内。该值可以是 0 至 255 范围内的红、绿、蓝值的逗号分隔三元组，也可以是类似 HTML 的十六进制三元组。参见下文实例。注意：`vt` VGA 硬件驱动不支持调色板配置。

**`kern.vt.fb.default_mode`** 将此值设置为图形模式以覆盖 `vt` 后端选择的默认值。此模式应用于所有输出连接器。目前仅在与 KMS 视频驱动配对时由 `vt_fb` 后端支持。

**`kern.vt.fb.modes`**.<`connector_name`> 设置此值以覆盖 `vt` 后端为输出连接器 `connector_name` 选择的默认图形模式。此模式仅应用于该连接器。它优先于 `kern.vt.fb.default_mode`。可用连接器名称可在加载 KMS 驱动后通过 [dmesg(8)](../man8/dmesg.8.md) 查找。其中会列出连接器及其关联的可调参数。目前仅在与 KMS 视频驱动配对时由 `vt_fb` 后端支持。

**`kern.vt.slow_down`** 在现代笔记本电脑上调试内核时，屏幕通常是唯一可用的控制台，相关信息会在被肉眼或相机捕获之前滚出视野。将 `kern.vt.slow_down` 设置为非零数字会使控制台输出同步（即不依赖定时器和中断），并按该数字比例减慢速度。

**`screen.font`** 将此值设置为位于 **/boot/fonts** 中所需字体文件的基本名称。该字体必须在那里存在的 `INDEX.fonts` 文件中指定。可使用 vtfontcvt(8) 转换字体以供使用。

## 键盘 SYSCTL 可调参数

这些设置控制是否启用或忽略某些特殊按键组合。具体按键组合可通过 keymap(5) 文件配置。

这些设置可在 [loader(8)](../man8/loader.8.md) 提示符下输入，或在 loader.conf(5) 中设置，也可在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 命令更改。

**`kern.vt.enable_altgr`** 启用 AltGr 键（不将右 Alt 键视为 Alt）。

**`kern.vt.kbd_halt`** 启用 halt 键组合。

**`kern.vt.kbd_poweroff`** 启用关机键组合。

**`kern.vt.kbd_reboot`** 启用重启键组合，通常是 Ctrl+Alt+Del。

**`kern.vt.kbd_debug`** 启用调试请求键组合，通常是 Ctrl+Alt+Esc。

**`kern.vt.kbd_panic`** 启用 panic 键组合。

## 其他 SYSCTL 可调参数

这些设置可在 [loader(8)](../man8/loader.8.md) 提示符下输入，在 loader.conf(5) 中设置，或在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 更改。

**`kern.consmute`** 禁止将内核消息打印到系统控制台。

**`kern.vt.enable_bell`** 启用终端响铃。

## 文件

**`/dev/console`**

**`/dev/consolectl`**

**`/dev/ttyv*`** 虚拟终端

**`/etc/ttys`** 终端初始化信息

**`/usr/share/vt/fonts/*.fnt`** 控制台字体

**`/usr/share/vt/keymaps/*.kbd`** 键盘布局

## DEVCTL 消息

| 系统 | 子系统 | 类型 | 描述 |
| ---- | ------ | ---- | ---- |
| `VT` | BELL | RING | 控制台响铃已响铃的通知。 |

| 变量 | 含义 |
| ---- | ---- |
| `duration_ms` | 请求响铃的时长（毫秒）。 |
| `enabled` | true 或 false，指示响铃时是否在管理上启用。 |
| `hushed` | true 或 false，指示响铃时是否被用户静音。 |
| `hz` | 请求的音调（Hz）。 |

## 实例

要将回滚缓冲区大小增加到 22500 行，在 **/etc/rc.conf** 中加入以下行：

```sh
allscreens_flags="-h 22500"
```

此示例将普通文本的默认颜色更改为黑底绿字，反相时为绿底黑字。注意，由于 [config(8)](../man8/config.8.md) 的当前实现，属性字符串内不能使用空格。

```sh
options TERMINAL_NORM_ATTR=(FG_GREEN|BG_BLACK)
```

此行将内核消息的默认颜色更改为黑底亮红字，反相时为亮红底黑字。

```sh
options TERMINAL_KERN_ATTR=(FG_LIGHTRED|BG_BLACK)
```

要在所有输出连接器上设置 1024x768 模式，在 **/boot/loader.conf** 中加入以下行：

```sh
kern.vt.fb.default_mode="1024x768"
```

要仅在笔记本电脑内置屏幕上设置 800x600，改用以下行：

```sh
kern.vt.fb.modes.LVDS-1="800x600"
```

连接器名称可在 [dmesg(8)](../man8/dmesg.8.md) 中找到：

```sh
info: [drm] Connector LVDS-1: get mode from tunables:
```

```sh
info: [drm] - kern.vt.fb.modes.LVDS-1
```

```sh
info: [drm] - kern.vt.fb.default_mode
```

设置控制台调色板的黑白颜色：

```sh
kern.vt.color.0.rgb="10,10,10"
```

```sh
kern.vt.color.15.rgb="#f0f0f0"
```

在引导时从 **/boot/fonts/*.fnt[.gz]** 在 loader.conf(5) 中加载 8x16 字体：

```sh
screen.font="8x16"
```

## 参见

kbdcontrol(1), [login(1)](../man1/login.1.md), vidcontrol(1), [atkbd(4)](atkbd.4.md), [atkbdc(4)](atkbdc.4.md), [kbdmux(4)](kbdmux.4.md), [keyboard(4)](keyboard.4.md), [screen(4)](screen.4.md), [splash(4)](splash.4.md), [syscons(4)](syscons.4.md), [ukbd(4)](ukbd.4.md), kbdmap(5), loader.conf(5), [rc.conf(5)](../man5/rc.conf.5.md), ttys(5), [config(8)](../man8/config.8.md), getty(8), [kldload(8)](../man8/kldload.8.md), [moused(8)](../man8/moused.8.md), vtfontcvt(8)

## 历史

`vt` 驱动最早出现在 FreeBSD 9.3 中。

## 作者

`vt` 设备驱动由 Ed Schouten <ed@FreeBSD.org>、Ed Maste <emaste@FreeBSD.org> 和 Aleksandr Rybalko <ray@FreeBSD.org> 开发，由 FreeBSD 基金会赞助。本手册页由 Warren Block <wblock@FreeBSD.org> 编写。

## 注意事项

粘贴缓冲区大小受系统值 {`MAX_INPUT`} 限制，即终端输入队列中可存储的字节数，通常为 1024 字节（参见 [termios(4)](termios.4.md)）。
