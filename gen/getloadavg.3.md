# getloadavg.3

`getloadavg` — 获取系统负载平均值

## 名称

`getloadavg`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`Ft int Fn getloadavg double loadavg[] int nelem`

## 描述

`getloadavg` 函数返回在不同时间段内取平均的系统运行队列中的进程数。最多检索 `nelem` 个样本，并赋值给 `loadavg`[] 的连续元素。系统最多提供 3 个样本，分别表示最近 1、5 和 15 分钟的平均值。

## 诊断

若无法获取负载平均值，返回 -1；否则返回实际检索到的样本数。

## 参见

[uptime(1)](../man1/uptime.1.md), kvm_getloadavg(3), [sysctl(3)](sysctl.3.md)

## 历史

`getloadavg` 函数出现于 4.3BSD。
