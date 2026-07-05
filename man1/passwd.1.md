# passwd.1

`passwd` — 修改用户密码

## 名称

`passwd`, `yppasswd`

## 概要

`passwd [-l] [user]`

`yppasswd [-l] [-y] [-d domain] [-h host] [-o]`

## 描述

`passwd` 实用程序修改用户的本地、Kerberos 或 NIS 密码。如果用户不是超级用户，`passwd` 首先提示输入当前密码，除非输入了正确的密码，否则不会继续。

输入新密码时，所输入的字符不会回显，以避免密码被旁人看到。`passwd` 实用程序会两次提示输入新密码，以检测输入错误。

密码的总长度必须小于 `_PASSWORD_LEN`（当前为 128 个字符）。

密码验证通过后，`passwd` 将新密码信息传送给 Kerberos 认证主机。

可用选项如下：

**`-l`** 仅在本地密码文件中更新密码，而不更新 Kerberos 数据库。仅修改本地密码时，使用 pwd_mkdb(8) 更新密码数据库。

修改本地或 NIS 密码时，下一次密码更改日期根据用户登录类别中的 “passwordtime” 能力设置。

要修改其他用户的 Kerberos 密码，必须先运行 kinit(1)，然后再运行 `passwd`。如果仅修改本地密码，超级用户无需提供用户的当前密码。

## NIS 交互

`passwd` 实用程序内建了对 NIS 的支持。如果用户存在于 NIS 密码数据库中但本地不存在，`passwd` 会自动切换到 `yppasswd` 模式。如果指定的用户在本地密码数据库和 NIS 密码映射中都不存在，`passwd` 返回错误。

修改 NIS 密码时，无特权用户需要提供旧密码进行认证（rpc.yppasswdd(8) 守护进程要求提供原始密码后才允许对 NIS 密码映射进行任何更改）。此限制甚至适用于超级用户，但有一个重要例外：在 NIS 主服务器上，超级用户的密码认证会被绕过。这意味着 NIS 主服务器上的超级用户可以对任何人的 NIS 密码进行无限制的更改。NIS 客户端系统和 NIS 从服务器上的超级用户仍需提供密码后才能处理更新。

以下附加选项用于 NIS：

**`-y`** 覆盖 `passwd` 的检查启发式方法，强制进入 NIS 模式。

**`-l`** 启用 NIS 时，`-l` 标志可用于强制 `passwd` 进入“仅本地”模式。当 NIS 用户与本地用户使用相同的登录名时，可以使用此标志修改本地用户的条目。例如，有时会在 NIS 密码映射和本地用户数据库中同时找到 `bin` 或 `daemon` 等系统“占位”用户的条目。默认情况下，`passwd` 会尝试修改 NIS 密码。可以使用 `-l` 标志改为修改本地密码。

**`-d`** `domain` 指定修改 NIS 密码时使用的域。默认情况下，`passwd` 假定应使用系统默认域。此标志主要供 NIS 主服务器上的超级用户使用：单个 NIS 服务器可以支持多个域。NIS 主服务器上的域名可能未设置（NIS 服务器不必同时是客户端），此时需要告知 `passwd` 命令在哪个域上操作。

**`-h`** `host` 指定 NIS 服务器的名称。此选项与 `-d` 选项结合使用，可在非本地 NIS 服务器上修改 NIS 密码。当使用 `-d` 选项指定域且 `passwd` 无法确定 NIS 主服务器的名称时（可能是因为本地域名未设置），NIS 主服务器的名称假定为 “localhost”。可以使用 `-h` 标志覆盖此假定。指定的主机名不必是 NIS 主服务器的名称：通过查询域中的任何 NIS 服务器（主服务器或从服务器）可以确定给定映射的 NIS 主服务器名称，因此指定从服务器的名称同样有效。

**`-o`** 不自动绕过 NIS 主服务器上超级用户的密码认证检查；改为假定“旧”模式。此标志的实际用途有限，但可用于测试。

## 文件

**/etc/master.passwd** 用户数据库

**/etc/passwd** Version 7 格式密码文件

**/etc/passwd.XXXXXX** 密码文件的临时副本

**/etc/login.conf** 登录类别能力数据库

## 参见

chpass(1), kinit(1), [login(1)](login.1.md), login.conf(5), passwd(5), kerberos(8), kpasswdd(8), pam_passwdqc(8), [pw(8)](../man8/pw.8.md), pwd_mkdb(8), vipw(8)

> Robert Morris, Ken Thompson, "UNIX password security".

## 注释

`yppasswd` 命令实际上只是 `passwd` 的一个链接。

## 历史

`passwd` 命令出现于 Version 6 AT&T UNIX。
