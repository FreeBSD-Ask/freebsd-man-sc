# splash(4)

`splash` — 启动画面/屏幕保护接口

## 名称

`splash`

## 概要

`device splash`

## 描述

`splash` 伪设备驱动为内核添加启动画面和屏幕保护支持。如果要加载启动位图图像或使用任何屏幕保护程序，则需要此驱动。

### 启动画面

当系统即将启动时，你可以加载并显示任意位图图像文件作为屏幕上的欢迎横幅。此图像将在内核初始化过程中一直显示，直到屏幕上出现登录提示，或直到加载并初始化屏幕保护程序。如果你按任意键，图像也会消失，但如果内核仍在探测设备，则此操作可能不会立即生效。

如果在加载内核时指定了 `-c` 或 `-v` 引导选项，启动画面将不会出现。但是，它仍会被加载，并可在稍后用作屏幕保护程序：见下文。

为了显示位图，位图文件本身和匹配的启动图像解码器模块必须由引导加载器加载。目前提供以下解码器模块：

**`splash_bmp.ko`** Windows BMP 文件解码器。虽然 BMP 文件格式允许各种颜色深度的图像，但此解码器目前仅处理 256 色位图。其他颜色深度的位图不会被显示。

**`splash_pcx.ko`** ZSoft PCX 解码器。此解码器目前仅支持 version 5 8-bpp 单平面图像。

**`splash_txt.ko`** TheDraw 二进制 ASCII 绘图文件解码器。显示文本模式的 80x25 ASCII 绘图，例如 TheDraw 中 Binary 保存格式所生成的绘图。此格式由一系列表示 80x25 显示的两字节对组成，其中第一个字节是要绘制的 ASCII 字符，第二个字节指示绘制该字符时使用的颜色/属性。

Sx EXAMPLES 章节说明了如何设置启动画面。

如果使用标准 VGA 视频模式，位图大小必须为 320x200 或更小。如果在内核中启用 VESA 模式支持，无论是通过静态链接 VESA 模块还是通过加载 VESA 模块（参见 [vga(4)](vga.4.md)），都可以加载最高 1024x768 分辨率的位图，具体取决于 VESA BIOS 和显卡上的视频内存量。

### 屏幕保护

当系统被视为空闲时，屏幕保护程序将激活：即当用户在指定时间段内未键入按键或移动鼠标时。由于屏幕保护程序是可选模块，必须显式加载到内存中。目前提供以下屏幕保护模块：

**`blank_saver.ko`** 此屏幕保护程序只是清空屏幕。

**`beastie_saver.ko`** 动画图形 BSD Daemon。

**`daemon_saver.ko`** 动画 BSD Daemon 屏幕保护程序。

**`dragon_saver.ko`** 绘制随机龙形曲线。

**`fade_saver.ko`** 屏幕将逐渐淡出。

**`fire_saver.ko`** 随负载增加而升高的火焰。

**`green_saver.ko`** 屏幕将被清空，类似于 `blank_saver.ko`。如果显示器和显卡 BIOS 支持，屏幕还将被关闭电源。

**`logo_saver.ko`** 动画图形 FreeBSD 标志。

**`plasma_saver.ko`** 绘制动画干涉图案。

**`rain_saver.ko`** 在屏幕上绘制阵雨。

**`snake_saver.ko`** 绘制字符串蛇。

**`star_saver.ko`** 闪烁的星星。

**`warp_saver.ko`** 流星。

可使用 [kldload(8)](../man8/kldload.8.md) 加载屏幕保护模块：

```sh
kldload logo_saver
```

超时值（以秒为单位）可按如下方式指定：

```sh
vidcontrol -t N
```

或者，你可以在 **/etc/rc.conf** 中将 `saver` 变量设为你选择的屏幕保护程序，将超时值设为 `blanktime` 变量，以便在系统启动时自动加载屏幕保护程序并设置超时值。

可以通过按 `saver` 键立即激活屏幕保护程序：默认情况下，AT 增强键盘上为 *Shift-Pause*，AT 84 键盘上为 *Shift-Ctrl-NumLock/Pause*。你可以通过修改键映射来更改 `saver` 键（参见 kbdcontrol(1)、keymap(5)），并将 `saver` 功能分配给你偏好的键。

如果屏幕不处于文本模式，屏幕保护程序将不会运行。

### 将启动画面作为屏幕保护程序

如果加载了启动画面但未加载屏幕保护程序，可以继续将 splash 模块用作屏幕保护程序。可按上文 Sx Screen saver 章节中所述指定屏幕清空间隔。

## 文件

**`/boot/defaults/loader.conf`** 引导加载器配置默认值

**`/etc/rc.conf`** 系统配置信息

**`/boot/kernel/splash_*.ko`** 启动图像解码器模块

**`/boot/kernel/*_saver.ko`** 屏幕保护模块

**`/boot/kernel/vesa.ko`** VESA 支持模块

## 实例

要加载启动画面或屏幕保护程序，必须在内核配置文件中加入以下行。

```sh
device splash
```

接下来对于 [syscons(4)](syscons.4.md)，编辑 **/boot/loader.conf**（参见 loader.conf(5)）并加入以下行：

```sh
splash_bmp_load="YES"
bitmap_load="YES"
bitmap_name="/boot/chuck.bmp"
```

在上面的示例中，加载了文件 **/boot/chuck.bmp**。在以下示例中，加载了 VESA 模块，以便无法在标准 VGA 模式下显示的位图文件可使用一种 VESA 视频模式显示。

```sh
splash_pcx_load="YES"
vesa_load="YES"
bitmap_load="YES"
bitmap_name="/boot/chuck.pcx"
```

如果 VESA 支持已静态链接到内核，则无需加载 VESA 模块。只需按上面第一个示例加载位图文件和启动解码器模块即可。

要加载二进制 ASCII 绘图并在引导时显示，请将以下内容加入 **/boot/loader.conf**：

```sh
splash_txt_load="YES"
bitmap_load="YES"
bitmap_name="/boot/splash.bin"
```

对于 [vt(4)](vt.4.md)，编辑 **/boot/loader.conf**（参见 loader.conf(5)）并加入以下行：

```sh
splash="/boot/images/freebsd-logo-rev.png"
boot_mute="YES"
```

可按如下方式指定在关机时显示的启动画面：

```sh
shutdown_splash="/boot/images/freebsd-logo-rev.png"
boot_mute="YES"
```

## 参见

vidcontrol(1), [syscons(4)](syscons.4.md), [vga(4)](vga.4.md), loader.conf(5), [rc.conf(5)](../man5/rc.conf.5.md), [kldload(8)](../man8/kldload.8.md), [kldunload(8)](../man8/kldunload.8.md)

## 历史

`splash` 驱动首次出现于 FreeBSD 3.1。

## 作者

`splash` 驱动和本手册页由 Kazutaka Yokota <yokota@FreeBSD.org> 编写。`splash_bmp` 模块由 Michael Smith <msmith@FreeBSD.org> 和 Kazutaka Yokota 编写。`splash_pcx` 模块由 Dag-Erling Sm(/orgrav <des@FreeBSD.org> 基于 `splash_bmp` 代码编写。`splash_txt` 模块由 Antony Mawer <antony@mawer.org> 基于 `splash_bmp` 代码编写，并从 `daemon_saver` 代码中获得了一些额外灵感。`logo_saver`、`plasma_saver`、`rain_saver` 和 `warp_saver` 模块由 Dag-Erling Sm(/orgrav <des@FreeBSD.org> 编写。[vt(4)](vt.4.md) 的 `splash` png 支持由 Emmanuel Vadot <manu@FreeBSD.org> 编写，并由 Quentin Thébault <quentin.thebault@defenso.fr> 扩展以支持关机。

## 注意事项

屏幕保护程序仅与 [syscons(4)](syscons.4.md) 配合工作。

对于 vt 启动画面，仅支持 RGBA png。

## 缺陷

如果在已加载另一屏幕保护程序的情况下加载屏幕保护程序，第一个屏幕保护程序不会自动卸载，将保留在内存中，浪费内核内存空间。
