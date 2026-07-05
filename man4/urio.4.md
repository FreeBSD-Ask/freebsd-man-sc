# urio.4

`urio` — Rio MP3 播放器的 USB 驱动

## 名称

`urio`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device urio

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
urio_load="YES"
```

## 描述

`urio` 驱动为连接到 USB 端口的 Diamond MultiMedia Rio MP3 播放器提供支持。`urio` 设备必须在内核中配置，同时还需要 *usb* 以及 *uhci* 或 *ohci* 控制器之一。

随后，Rio 用户态应用程序可以使用 **/dev/urio0** 设备。

## 硬件

以下设备受 `urio` 驱动支持：

- Diamond MultiMedia Rio 500
- Diamond MultiMedia Rio 600
- Diamond MultiMedia Rio 800

## 文件

**/dev/urio0** 阻塞型设备节点

## 实例

在内核配置文件中加入以下行可将 `urio` 驱动添加到内核：

```sh
device urio
```

使用 rio_add_song(1) 工具（参见 Sx SEE ALSO 段）通过 USB 连接将歌曲下载到 Rio：

```sh
rio_add_song /usr/local/MP3/TracyChapman/02-Fast-Car.mp3
```

## 参见

[ohci(4)](ohci.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md)

> "The Rio 500 SourceForge Project Web Page".

SourceForge 上的 Rio500 工具是用于下载、格式化或重命名播放器上歌曲的实际用户态工具。编译这些工具时，以下预构建配置命令可确保 `rio_usb.h` 在包含路径中可用，并且所使用的设备为 **/dev/urio0**：

```sh
CFLAGS="-I/usr/include/dev/usb" ./configure \
    --with-devicepath='/dev' --with-deviceentry='urio0'
```

## 作者

`urio` 驱动由 Iwasa Kazmi <kzmi@ca2.so-net.ne.jp> 为 FreeBSD 编写。

本手册页由 Dirk-Willem van Gulik <dirkx@webweaving.org> 编写。
