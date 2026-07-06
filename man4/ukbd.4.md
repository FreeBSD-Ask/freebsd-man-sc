# ukbd.4

`ukbd` — USB 键盘驱动

## 名称

`ukbd`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ukbd
> device hid
> device usb

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
ukbd_load="YES"
```

## 描述

`ukbd` 驱动为连接到 USB 端口的键盘提供支持。内核中还必须配置 [usb(4)](usb.4.md) 和 [uhci(4)](uhci.4.md) 或 [ohci(4)](ohci.4.md) 之一。

## 配置

默认情况下，键盘子系统尚未创建相应的设备。请确保在内核配置文件中使用以下选项重新配置内核：

```sh
options KBD_INSTALL_CDEV
```

如果同时使用 AT 键盘和 USB 键盘，AT 键盘会在 **`/dev`** 中显示为 `kbd0`。USB 键盘则为 `kbd1 , kbd2` 等。可使用以下命令查看键盘的一些信息：

```sh
kbdcontrol -i < /dev/kbd1
```

或使用以下命令加载键位映射：

```sh
kbdcontrol -l keymaps/pt.iso < /dev/kbd1
```

更多可用选项请参见 kbdcontrol(1)。

可使用以下命令切换控制台键盘：

```sh
kbdcontrol -k /dev/kbd1
```

此后，第一个 USB 键盘将成为控制台使用的键盘。

如果想将 USB 键盘作为默认键盘且完全不使用 AT 键盘，必须从内核配置文件中删除 `device atkbd` 行。由于设备初始化顺序，USB 键盘会在控制台驱动初始化自身*之后*才被检测到，因此必须显式告知控制台驱动使用 USB 键盘。可通过以下两种方式之一完成。

将以下命令作为系统初始化的一部分运行：

```sh
kbdcontrol -k /dev/kbd0 < /dev/ttyv0 > /dev/null
```

（注意，由于 USB 键盘是唯一的键盘，因此以 `/dev/kbd0` 访问）或者通过在内核配置文件中设置标志，告知控制台驱动定期查找键盘：

```sh
device sc0 at isa? flags 0x100
```

使用上述标志，控制台驱动如果在引导时初始化期间未检测到键盘，则会尝试检测系统中的任何键盘。

## 驱动配置

> `options KBD_INSTALL_CDEV`

使键盘可通过 **`/dev`** 中的字符设备访问。

> `options UKBD_DFLT_KEYMAP`

> `makeoptions UKBD_DFLT_KEYMAP=fr.iso`

上述行会将法文 ISO 键位映射放入 ukbd 驱动。可使用此选项指定 **`/usr/share/syscons/keymaps`** 或 **`/usr/share/vt/keymaps`** 中的任意键位映射（取决于所使用的控制台驱动）。

> `options KBD_DISABLE_KEYMAP_LOADING`

不允许用户更改键位映射。

> `options KBD_DELAY1=200`

设置键盘初始按键重复延迟。

> `options KBD_DELAY2=15`

设置键盘按键重复延迟。

注意，这些选项也会影响 AT 键盘驱动 [atkbd(4)](atkbd.4.md)。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.ukbd.debug`** 调试输出级别，0 表示禁用调试，更大的值增加调试消息的详细程度。默认为 0。

**`hw.usb.ukbd.apple_swap_cmd_opt`** 设置为 1 时交换 Apple 键盘上的 Command 和 Option 键。默认为 0。

**`hw.usb.ukbd.apple_swap_cmd_ctl`** 设置为 1 时交换 Apple 键盘上的 Command 和 Control 键。默认为 0。

**`hw.usb.ukbd.apple_fn_mode`** 设置为 1 时无需按住 Fn 即可直接访问媒体键。默认为 0。

**`hw.usb.ukbd.no_leds`** 设置为 1 时禁用键盘 LED 设置。默认为 0。

## 文件

**`/dev/kbd*`** 阻塞型设备节点

## 实例

> `device ukbd`

将 `ukbd` 驱动加入内核。

## 参见

kbdcontrol(1), [ohci(4)](ohci.4.md), [syscons(4)](syscons.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md), [vt(4)](vt.4.md), [config(8)](../man8/config.8.md)

## 作者

`ukbd` 驱动由 Lennart Augustsson <augustss@cs.chalmers.se> 为 NetBSD 编写，并由 Kazutaka YOKOTA <yokota@zodiac.mech.utsunomiya-u.ac.jp> 为 FreeBSD 进行了大量重写。

本手册页由 Nick Hibma <n_hibma@FreeBSD.org> 编写，并大量采纳了 Kazutaka YOKOTA <yokota@zodiac.mech.utsunomiya-u.ac.jp> 的意见。
