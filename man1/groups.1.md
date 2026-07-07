# groups(1)

`groups` — 显示用户所属的组

## 名称

`groups`

## 概要

`groups [user]`

## 描述

`groups` 实用程序已被 [id(1)](id.1.md) 实用程序取代，等同于 “`id` `-Gn` [`user`]”。建议在正常交互使用时使用命令 “`id` `-p`”。

`groups` 实用程序显示你（或可选指定的 `user`）所属的组。

## 退出状态

`groups` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

显示 root 用户所属的组：

```sh
$ groups root
wheel operator
```

## 参见

[id(1)](id.1.md), [groups(7)](../man7/groups.7.md)
