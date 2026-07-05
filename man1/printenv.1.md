# printenv.1

`printenv` — 打印环境变量

## 名称

`printenv`

## 概要

`printenv [name]`

## 描述

`printenv` 实用程序打印环境中各变量的名称和值，每行一个名称/值对。如果指定了 `name`，则只打印其对应的值。

某些 shell 可能提供内建的 `printenv` 命令，与本实用程序类似或相同。请参阅 [builtin(1)](builtin.1.md) 手册页。

## 退出状态

`printenv` 实用程序成功时退出值为 0，发生错误时大于 0。

## 参见

[csh(1)](csh.1.md), [env(1)](env.1.md), [sh(1)](sh.1.md), [environ(7)](../man7/environ.7.md)

## 标准

`printenv` 实用程序是为了与早期 BSD 和 FreeBSD 版本兼容而保留的，并未被任何标准所规定。`printenv` 的功能可以使用 echo(1) 和 [env(1)](env.1.md) 实用程序来复制实现。

## 历史

`printenv` 命令首次出现于 3.0BSD。
