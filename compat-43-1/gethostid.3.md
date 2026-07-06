# gethostid.3

`gethostid` — 获取/设置当前主机的唯一标识符

## 名称

`gethostid`, `sethostid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

`Ft long Fn gethostid void Ft void Fn sethostid long hostid`

## 描述

`sethostid` 函数为当前处理器建立一个 32 位标识符，旨在所有现存 UNIX 系统中保持唯一。通常为本地机器的 DARPA Internet 地址。此调用仅允许超级用户执行，通常在引导时进行。

`gethostid` 函数返回当前处理器的 32 位标识符。

此函数已被弃用。hostid 应通过 [sysctl(3)](sysctl.3.md) 设置或获取。

## 参见

[gethostname(3)](gethostname.3.md), [sysctl(3)](sysctl.3.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`gethostid` 和 `sethostid` 系统调用出现于 4.2BSD，在 4.4BSD 中被移除。

## 缺陷

32 位标识符太小。
