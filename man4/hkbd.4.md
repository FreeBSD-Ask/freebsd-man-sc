# hkbd(4)

`hkbd` — HID 键盘驱动

## 名称

`hkbd`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device hkbd
> device hid
> device hidbus
> device evdev
> options EVDEV_SUPPORT

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
hkbd_load="YES"
```

## 描述

`hkbd` 驱动为附加到 HID 传输后端的键盘提供支持。还必须在内核中配置 hid(4)、[hidbus(4)](hidbus.4.md) 以及 [iichid(4)](iichid.4.md) 或 [usbhid(4)](usbhid.4.md) 之一。

## 配置

默认情况下，键盘子系统尚未创建相应设备。请确保在内核配置文件中使用以下选项重新配置内核：

```sh
options KBD_INSTALL_CDEV
```

如果同时使用 AT 键盘和 HID 键盘，AT 键盘在 **`/dev`** 中将显示为 `kbd0`。HID 键盘将为 `kbd1 , kbd2` 等。可使用以下命令查看键盘的一些信息：

```sh
kbdcontrol -i < /dev/kbd1
```

或加载键映射：

```sh
kbdcontrol -l keymaps/pt.iso < /dev/kbd1
```

更多可用选项请参见 kbdcontrol(1)。

可使用以下命令切换控制台键盘：

```sh
kbdcontrol -k /dev/kbd1
```

此后，第一个 HID 键盘将成为控制台使用的键盘。

如果你想将 HID 键盘作为默认键盘且完全不使用 AT 键盘，必须从内核配置文件中删除 `device atkbd` 行。由于设备初始化顺序，HID 键盘会在控制台驱动初始化自身*之后*才被检测到，你必须显式告知控制台驱动使用已存在的 HID 键盘。可通过以下两种方式之一完成。

作为系统初始化的一部分运行以下命令：

```sh
kbdcontrol -k /dev/kbd0 < /dev/ttyv0 > /dev/null
```

（注意，由于 HID 键盘是唯一的键盘，它通过 **`/dev/kbd0`** 访问）或者通过在内核配置文件中设置标志，告知控制台驱动定期查找键盘：

```sh
device sc0 at isa? flags 0x100
```

使用上述标志，控制台驱动如果在引导时初始化期间未检测到键盘，会尝试检测系统中的任何键盘。

## 驱动配置

> `options KBD_INSTALL_CDEV`

使键盘通过 **`/dev`** 中的字符设备可用。

> `options HKBD_DFLT_KEYMAP`

> `makeoptions HKBD_DFLT_KEYMAP=fr.iso`

上述行会将 French ISO 键映射放入 ukbd 驱动。可使用此选项指定 **`/usr/share/syscons/keymaps`** 或 **`/usr/share/vt/keymaps`** （取决于所使用的控制台驱动）中的任意键映射。

> `options KBD_DISABLE_KEYMAP_LOADING`

不允许用户更改键映射。注意，这些选项也会影响 AT 键盘驱动 [atkbd(4)](atkbd.4.md)。

## SYSCTL 变量

以下变量既是 [sysctl(8)](../man8/sysctl.8.md) 变量，也是 [loader(8)](../man8/loader.8.md) 可调参数：

**`hw.hid.hkbd.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

**`hw.hid.hkbd.apple_swap_cmd_opt`** 设置为 1 时交换 Apple 键盘上的 Command 和 Option 键。默认值为 0。

**`hw.hid.hkbd.apple_swap_cmd_ctl`** 设置为 1 时交换 Apple 键盘上的 Command 和 Control 键。默认值为 0。

**`hw.hid.hkbd.apple_fn_mode`** 设置为 1 时无需按住 Fn 即可直接访问媒体键。默认值为 0。

**`hw.hid.hkbd.no_leds`** 设置为 1 时禁用键盘 LED 设置。默认值为 0。

## 文件

**`/dev/kbd*`** 阻塞型设备节点

**`/dev/input/event*`** 输入事件设备节点。

## 实例

> `device hkbd`

将 `hkbd` 驱动加入内核。

## 参见

kbdcontrol(1), hid(4), [hidbus(4)](hidbus.4.md), [iichid(4)](iichid.4.md), [syscons(4)](syscons.4.md), [usbhid(4)](usbhid.4.md), [vt(4)](vt.4.md), [config(8)](../man8/config.8.md)

## 作者

`hkbd` 驱动最初由 Lennart Augustsson <augustss@cs.chalmers.se> 为 NetBSD 编写，并由 Kazutaka YOKOTA <yokota@zodiac.mech.utsunomiya-u.ac.jp> 为 FreeBSD 大幅重写。

本手册页由 Nick Hibma <n_hibma@FreeBSD.org> 编写，其中大量内容来自 Kazutaka YOKOTA <yokota@zodiac.mech.utsunomiya-u.ac.jp> 的输入。
