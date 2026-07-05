# uptime.1

`uptime` — 显示系统已运行多久

## 名称

`uptime`

## 概要

`uptime [--libxo]`

## 描述

`uptime` 实用程序显示当前时间、系统已运行的时间长度、用户数以及系统在过去 1、5 和 15 分钟内的负载平均值。

可用选项如下：

**`--libxo`** 通过 libxo(3) 以多种人类和机器可读格式生成输出。命令行参数的细节参见 xo_options(7)。

## 文件

**/boot/kernel/kernel** 系统名称列表

## 实例

```sh
$ uptime
11:23AM  up  3:01, 8 users, load averages: 21.09, 15.43, 12.79
```

## 参见

[w(1)](w.1.md), libxo(3), xo_options(7)

## 历史

`uptime` 命令出现于 3.0BSD。
