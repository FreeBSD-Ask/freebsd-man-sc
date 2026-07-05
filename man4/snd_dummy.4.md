# snd_dummy.4

`snd_dummy` — 虚拟音频驱动

## 名称

`snd_dummy`

## 概要

`要在引导时加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
snd_dummy_load="YES"
```

## 描述

`snd_dummy` 驱动实现了一个虚拟测试设备，即它不对应于物理声卡。它用于测试目的，使测试程序无需依赖机器中存在的硬件即可运行。

该驱动作为常规 sound(4) 设备附加，具有两个声道（一个播放和一个录制）以及一个混音器。

播放通过丢弃所有输入工作，录制通过返回静音（零）工作。

## 文件

**`/dev/dsp.dummy`** 到由 sound(4) 创建的设备 **/dev/dsp%d** 文件的别名。当系统中存在多个设备时，便于测试程序打开虚拟设备。

## 参见

sound(4), loader.conf(5), [loader(8)](../man8/loader.8.md)

## 作者

`snd_dummy` 驱动由 Christos Margiolis <christos@FreeBSD.org> 在 FreeBSD 基金会赞助下实现。

## 注意事项

由于驱动在模块加载后会自动附加，因此只能附加一次。
