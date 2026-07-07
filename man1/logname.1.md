# logname(1)

`logname` — 显示用户的登录名

## 名称

`logname`

## 概要

`logname`

## 描述

`logname` 实用程序将用户的登录名写入标准输出，后跟一个换行符。

`logname` 实用程序显式忽略 `LOGNAME` 和 `USER` 环境变量，因为环境不可信。

## 退出状态

`logname` 实用程序成功时退出值为 0，发生错误时大于 0。

## 参见

[who(1)](who.1.md), [whoami(1)](whoami.1.md), getlogin(2)

## 标准

`logname` 实用程序预期符合 IEEE Std 1003.2 ("POSIX.2")。

## 历史

`logname` 命令首次出现于 4.4BSD。
