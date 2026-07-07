# longrun(4)

`longrun` — Transmeta(TM) Crusoe(TM) LongRun(TM) 支持

## 名称

`longrun`

## 概要

`LongRun 支持是 Transmeta Crusoe 芯片的省电模式集合，其范围类似于 Intel 的 SpeedStep。以下 sysctl(8) MIB 控制不同的 CPU 模式：`

**名称	类型	可更改	描述**
| hw.crusoe.longrun | 整数 | 是 | LongRun 模式： |
| --- | --- | --- | --- |
|  |  |  | 0：最低频率模式 |
|  |  |  | 1：省电模式 |
|  |  |  | 2：性能模式 |
|  |  |  | 3：最高频率模式 |
| hw.crusoe.frequency | 整数 | 否 | 当前频率（MHz）。 |
| hw.crusoe.voltage | 整数 | 否 | 当前电压（mV）。 |
| hw.crusoe.percentage | 整数 | 否 | 处理性能（%）。 |

## 实例

打印当前状态：

```sh
% sysctl hw.crusoe
```

将 LongRun 模式设置为面向性能的可变频率模式（较少省电）：

```sh
# sysctl hw.crusoe.longrun=2
```

## 历史

Transmeta(TM) Crusoe(TM) LongRun(TM) 支持首次出现于 FreeBSD 4.4。

## 作者

LongRun 支持和本手册页由 Tamotsu HATTORI <athlete@kta.att.ne.jp> 和 Mitsuru IWASAKI <iwasaki@FreeBSD.org> 编写。
