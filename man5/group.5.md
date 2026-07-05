# group.5

`group` — 组权限文件格式

## 名称

`group`

## 描述

`group` 文件是组信息的本地来源。它可以与 Hesiod 域 `group` 以及 NIS 映射 `group.byname` 和 `group.bygid` 配合使用，由 [nsswitch.conf(5)](nsswitch.conf.5.md) 控制。

`group` 文件由换行符分隔的 ASCII 记录组成，每个组一条记录，包含四个以冒号 `:` 分隔的字段。这些字段如下：

**group** 组的名称。
**passwd** 组的*加密*密码。
**gid** 组的十进制 ID。
**member** 组成员。

第一个非空白字符为井号（#）的行是注释，将被忽略。仅由空格、制表符或换行符组成的空行也会被忽略。

`group` 字段是组名，用于向作为组成员的用户授予文件访问权限。`gid` 字段是与组名关联的数字。二者都应在整个系统（通常也跨一组系统）中保持唯一，因为它们控制文件访问权限。`passwd` 字段是可选的*加密*密码。此字段很少使用，通常在其中放置一个星号而不是留空。`member` 字段包含被授予 `group` 权限的用户名。成员名以逗号分隔，不含空格或换行符。如果某个组是在用户的 **/etc/passwd** 条目中指定的，则该用户自动属于该组，无需在 `group` 文件中再添加到该组。

## 实现说明

[passwd(1)](../man1/passwd.1.md) 命令不会更改 `group` 密码。应改用 [pw(8)](../man8/pw.8.md) 工具的 `groupmod` 命令。

## 限制

有各种限制，在出现这些限制的函数中进行说明；参见 SEE ALSO 一节。

在较早的实现中，一个组不能超过 200 个成员。**/etc/group** 的最大行长度为 1024 个字符。更长的行将被跳过。此限制在 FreeBSD 3.0 中消失了。静态链接的旧二进制文件、依赖旧共享库的二进制文件，或兼容模式下的非 FreeBSD 二进制文件可能仍有此限制。

## 文件

**`/etc/group`**

## 参见

newgrp(1), [passwd(1)](../man1/passwd.1.md), setcred(2), setgroups(2), crypt(3), getgrent(3), initgroups(3), [nsswitch.conf(5)](nsswitch.conf.5.md), [passwd(5)](passwd.5.md), [groups(7)](../man7/groups.7.md), chkgrp(8), [pw(8)](../man8/pw.8.md), [yp(8)](../man8/yp.8.md)

## 历史

`group` 文件格式出现于 Version 6 AT&T UNIX。对注释的支持首次出现于 FreeBSD 3.0。
