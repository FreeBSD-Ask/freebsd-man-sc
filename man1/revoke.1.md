# revoke.1

`revoke` — 撤销字符设备

## 名称

`revoke` — 撤销字符设备

## 概要

`revoke file`

## 描述

`revoke` 程序使用 revoke(2) 撤销字符设备。当用于 TTY 时，read(2)、write(2) 和 ioctl(2) 等调用会立即中止，从而有效终止登录会话。

## 参见

revoke(2)

## 历史

`revoke` 程序首次出现于 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
