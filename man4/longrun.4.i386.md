# longrun.4.i386

`longrun` — Transmeta(TM) Crusoe(TM) LongRun(TM) 支持

## 名称

`longrun`

## 概要

`LongRun 支持是 Transmeta Crusoe 芯片的一系列节能模式，作用范围类似于 Intel 的 SpeedStep。以下 sysctl(8) MIB 控制不同的 CPU 模式：`

| **名称 类型 可修改 描述** |
| --- |
| hw.crusoe.longrun |
|  |
|  |
|  |
|  |
| hw.crusoe.frequency |
| hw.crusoe.voltage |
| hw.crusoe.percentage |

## 实例

打印当前状态：

```sh
% sysctl hw.crusoe
```

将 LongRun 模式设为面向性能的可变频率模式（节能较少）：

```sh
# sysctl hw.crusoe.longrun=2
```

## 历史

Transmeta(TM) Crusoe(TM) LongRun(TM) 支持首次出现于 FreeBSD 4.4。

## 作者

LongRun 支持及本手册页由 Tamotsu HATTORI <athlete@kta.att.ne.jp> 和 Mitsuru IWASAKI <iwasaki@FreeBSD.org> 编写。
