# vga(4)

`vga` — 通用显卡接口

## 名称

`vga`

## 概要

`options VESA options VESA_DEBUG=N options VGA_ALT_SEQACCESS options VGA_NO_FONT_LOADING options VGA_NO_MODE_CHANGE options VGA_SLOW_IOACCESS options VGA_WIDTH90 device vga`

`在 /boot/device.hints 中： hint.vga.0.at="isa"`

## 描述

`vga` 驱动是一个通用显卡驱动，提供对显卡的访问。控制台驱动 [syscons(4)](syscons.4.md) 需要此驱动。控制台驱动会调用 `vga` 驱动来操作视频硬件（切换视频模式、加载字体等）。

`vga` 驱动支持标准显卡：MDA、CGA、EGA 和 VGA。此外，如果显卡支持 VESA BIOS 扩展，该驱动也能利用它们。VESA 支持可静态编译进内核，也可作为独立模块加载。

为将 VESA 支持静态链接到内核，必须在内核配置文件中定义 `VESA` 选项（见下文）。

可使用 [kldload(8)](../man8/kldload.8.md) 将 `vesa` 模块动态加载到内核中。

## 驱动配置

### 内核配置选项

以下内核配置选项（参见 [config(8)](../man8/config.8.md)）可用于控制 `vesa` 驱动。这些选项提供了与某些 VGA 卡的兼容性。

**`VGA_ALT_SEQACCESS`** 如果鼠标指针显示不正确，或 VGA 卡上的字体似乎未能正确加载，可尝试此选项。但在某些系统上可能引起闪烁。

**`VGA_SLOW_IOACCESS`** 旧款 VGA 卡可能需要此选项才能正常工作。它使驱动对 VGA 寄存器执行按字节 I/O，速度会有所下降。

**`VGA_WIDTH90`** 此选项启用 90 列模式：90x25、90x30、90x43、90x50、90x60。这些模式并不总是被显卡和显示器支持。LCD 显示器很可能无法在这些模式下工作。

以下选项为驱动添加可选功能。

**`VESA`** 为驱动添加 VESA BIOS 支持。如果 VGA 卡具有 VESA BIOS 扩展 1.2 或更高版本，此选项将利用 VESA BIOS 服务切换到高分辨率模式。

**`VESA_DEBUG=N`** 将 VESA 支持的调试级别设置为 `N`。默认值为零，抑制所有调试输出。

以下选项会从 `vesa` 驱动中移除某些功能并节省内核内存。

**`VGA_NO_FONT_LOADING`** `vesa` 驱动可将软件字体加载到 EGA 和 VGA 卡上。此选项移除该功能。注意，若使用此选项但仍希望在控制台上使用鼠标，则还必须使用 `SC_ALT_MOUSE_IMAGE` 选项。参见 [syscons(4)](syscons.4.md)。

**`VGA_NO_MODE_CHANGE`** 此选项阻止驱动更改视频模式。

## 实例

你的内核配置通常应包含：

```sh
device vga
```

并且你需要在 **/boot/device.hints** 中加入以下行。

```sh
hint.vga.0.at="isa"
```

为启用 VESA BIOS 扩展支持，内核配置文件中应包含以下行。

```sh
options VESA
```

```sh
device vga
```

如果你不希望将 VESA 支持包含进内核，但偶尔需要使用，则不要添加 `VESA` 选项。按需加载 `vesa` 模块：

```sh
kldload vesa
```

## 参见

vgl(3), [syscons(4)](syscons.4.md), [config(8)](../man8/config.8.md), [kldload(8)](../man8/kldload.8.md), [kldunload(8)](../man8/kldunload.8.md)

## 标准

> Video Electronics Standards Association, "VESA BIOS Extension (VBE)".

## 历史

`vesa` 驱动最早出现于 FreeBSD 3.1。

## 作者

`vesa` 驱动由 Søren Schmidt <sos@FreeBSD.org> 和 Kazutaka Yokota <yokota@FreeBSD.org> 编写。本手册页由 Kazutaka Yokota 编写。
