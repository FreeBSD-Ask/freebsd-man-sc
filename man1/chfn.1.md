# chfn.1

`chpass` — 添加或更改用户数据库信息

## 名称

`chpass`, `chfn`, `chsh`, `ypchpass`, `ypchfn`, `ypchsh`

## 概要

`chpass [-a list] [-e expiretime] [-p encpass] [-s newshell] [user]`

`ypchpass [-loy] [-a list] [-d domain] [-e expiretime] [-h host] [-p encpass] [-s newshell] [user]`

## 描述

`chpass` 实用程序允许编辑与 `user` 关联的用户数据库信息，默认为当前用户。

`chfn`、`chsh`、`ypchpass`、`ypchfn` 和 `ypchsh` 实用程序的行为与 `chpass` 完全相同。（实际上只有一个程序。）

信息会被格式化并提供给编辑器进行修改。

仅显示允许用户更改的信息。

选项如下：

**`-a`** `list` 超级用户可以直接以参数形式提供用户数据库条目，格式由 [passwd(5)](../man5/passwd.5.md) 指定。该参数必须是以冒号（“:”）分隔的所有用户数据库字段的列表，但字段可以为空。

**`-e`** `expiretime` 更改账户过期时间。此选项用于从脚本中设置过期时间，如同在交互式编辑器中完成一样。

**`-p`** `encpass` 超级用户可以直接以参数形式提供加密密码字段，格式采用 crypt(3) 所用的格式。

**`-s`** `newshell` 尝试将用户的 shell 更改为 `newshell`。

可能显示的项目如下：

**Login:** 用户的登录名
**Password:** 用户的加密密码
**Uid:** 用户的登录
**Gid:** 用户的登录组
**Class:** 用户的一般分类
**Change:** 密码更改时间
**Expire:** 账户过期时间
**Full** Name: 用户的真实姓名
**Office** Location: 用户的办公室位置 (1)
**Office** Phone: 用户的办公电话 (1)
**Home** Phone: 用户的家庭电话 (1)
**Other** Information: 为用户定义的任何本地参数 (1)
**Home** Directory: 用户的主目录
**Shell:** 用户的登录 shell
**NOTE(1)** - 在实际的 master.passwd 文件中，这些字段是嵌入在 FullName 字段中以逗号分隔的字段。

`login` 字段是用于访问计算机账户的用户名。

`password` 字段包含用户密码的加密形式。

`uid` 字段是与 `login` 字段关联的编号。这两个字段都应在整个系统内（通常也跨越一组系统）保持唯一，因为它们控制文件访问。

虽然可以存在多个具有相同登录名和/或相同用户 ID 的条目，但这样做通常是错误的。操作这些文件的例程通常只会返回多个条目中的一个，并且是随机选择的那一个。

`gid` 字段是用户登录时所属的组。由于 BSD 支持多个组（参见 [groups(1)](groups.1.md)），该字段目前几乎没有特殊含义。此字段可以填写数字或组名（参见 [group(5)](../man5/group.5.md)）。

`class` 字段引用 **`/etc/login.conf`** 中的类别描述，通常用于在用户登录时初始化其系统资源限制。

`change` 字段是密码必须更改的日期。

`expire` 字段是账户过期的日期。

`change` 和 `expire` 字段均应以“month day year”的形式输入，其中 `month` 为月份名称（前三个字符即可），`day` 为该月中的日期，`year` 为年份。

有五个字段可用于存储用户的 `full name , office location`、`work` 和 `home telephone` 号码，最后是 `other information`，它是一个以逗号分隔的字符串，用于表示任何附加的 gecos 字段（通常用于特定站点的用户信息）。注意，finger(1) 会将办公室位置和办公电话一起显示在 `Office:` 标题下。

用户的 `home directory` 是用户登录时所处的完整 UNIX 路径名。

`shell` 字段是用户偏好的命令解释器。如果 `shell` 字段为空，则假定为 POSIX shell，即 **`/bin/sh`**。在更改登录 shell 时，如果不是超级用户，用户不能从非标准 shell 更改或更改为非标准 shell。非标准定义为未在 **`/etc/shells`** 中找到的 shell。

信息经过验证后，`chpass` 使用 pwd_mkdb(8) 更新用户数据库。

## 环境变量

除非将环境变量 `EDITOR` 设置为其他编辑器，否则将使用 [vi(1)](vi.1.md) 编辑器。编辑器退出时，信息会被重新读取并用于更新用户数据库本身。只有用户本人或超级用户才能编辑与该用户关联的信息。

有关设置 `PW_SCAN_BIG_IDS` 环境变量的影响说明，请参见 pwd_mkdb(8)。

## NIS 交互

`chpass` 实用程序也可以与 NIS 结合使用，但有一些限制。目前，`chpass` 只能通过 rpc.yppasswdd(8) 对 NIS passwd 映射进行更改，而 rpc.yppasswdd(8) 通常只允许更改用户的密码、shell 和 GECOS 字段。除非由 NIS 主服务器上的超级用户调用，否则 `chpass`（以及类似的 [passwd(1)](passwd.1.md)）无法使用 rpc.yppasswdd(8) 服务器更改其他用户信息或向 NIS passwd 映射添加新记录。此外，rpc.yppasswdd(8) 要求在进行任何更改之前进行密码认证。唯一允许在不提供密码的情况下提交更改的用户是 NIS 主服务器上的超级用户；所有其他用户，包括在 NIS 客户端（和 NIS 从服务器）上具有 root 权限的用户，都必须输入密码。（允许 NIS 主服务器上的超级用户绕过这些限制主要是为了方便：拥有 NIS 主服务器 root 访问权限的用户已经具备更新 NIS 映射所需的权限，但手动编辑映射源文件可能比较繁琐。

注意：这些例外仅当 NIS 主服务器是 FreeBSD 系统时适用）。

因此，除另有说明外，当 `chpass` 与 NIS 一起使用时，以下限制适用：

- *仅可更改 shell 和 GECOS 信息。* 所有其他字段都受限，即使由超级用户调用 `chpass` 也是如此。虽然可以添加对更改其他字段的支持，但这会导致与其他支持 NIS 的系统产生兼容性问题。即使超级用户在编辑条目时可以为其他字段提供数据，这些额外信息（密码除外——见下文）也会被静默丢弃。例外：NIS 主服务器上的超级用户可以更改任何字段。
- *需要密码认证。* `chpass` 实用程序在执行任何更改之前会提示输入用户的 NIS 密码。如果密码无效，所有更改都将被丢弃。例外：NIS 主服务器上的超级用户可以不提供密码而提交更改。（超级用户可以使用下面描述的 `-o` 标志关闭此功能。）
- *不建议向本地密码数据库添加新记录。* `chpass` 实用程序允许管理员在启用 NIS 时向本地密码数据库添加新记录，但这可能导致混乱，因为新记录会附加到主密码文件的末尾，通常位于特殊的 NIS “+”条目之后。管理员应使用 vipw(8) 在 NIS 运行时修改本地密码文件。NIS 主服务器上的超级用户可以向 NIS 密码映射添加新记录，前提是 rpc.yppasswdd(8) 服务器已使用 `-a` 标志启动以允许添加（默认情况下拒绝添加）。`chpass` 实用程序默认尝试更新本地密码数据库；要改为更新 NIS 映射，请使用 `-y` 标志调用 chpass。
- *不允许更改密码。* 用户应使用 [passwd(1)](passwd.1.md) 或 [yppasswd(1)](yppasswd.1.md) 来更改其 NIS 密码。超级用户可以指定新密码（尽管“Password:”字段不会出现在编辑器模板中，超级用户可以手动将其添加回去），但即使是超级用户也必须提供用户的原始密码，否则 rpc.yppasswdd(8) 将拒绝更新 NIS 映射。例外：NIS 主服务器上的超级用户可以使用 `chpass` 更改用户的 NIS 密码。

当 `chpass` 编译时包含 NIS 支持时，还有一些额外的选项标志可用：

**`-d`** `domain` 指定特定的 NIS 域。`chpass` 实用程序默认使用由 domainname(1) 实用程序设置的系统域名。`-d` 选项可用于覆盖默认值，或在未设置系统域名时指定一个域。

**`-h`** `host` 指定要查询的 NIS 服务器的名称或地址。通常，`chpass` 会与 `master.passwd` 或 `passwd` 映射中指定的 NIS 主机进行通信。在未配置为 NIS 客户端的主机上，除非用户提供服务器的主机名，否则程序无法确定此信息。注意，指定的主机名不必是 NIS 主服务器的主机名；给定 NIS 域中任何服务器（主服务器或从服务器）的名称均可。使用 `-d` 选项时，主机名默认为“localhost”。`-h` 选项可与 `-d` 选项结合使用，此时用户指定的主机名将覆盖默认值。

**`-l`** 当用户同时存在于本地和 NIS 数据库中时，强制 `chpass` 修改用户密码信息的本地副本。

**`-o`** 强制在与 rpc.yppasswdd(8) 通信时使用基于 RPC 的更新（“旧模式”）。当由 NIS 主服务器上的超级用户调用时，`chpass` 允许使用专用的非基于 RPC 的机制（在本例中为 UNIX 域套接字）对 NIS passwd 映射进行不受限制的更改。`-o` 标志可用于强制 `chpass` 使用标准更新机制。此选项主要用于测试目的。

**`-y`** 与 `-l` 效果相反。此标志基本上是多余的，因为如果启用了 NIS，`chpass` 默认对 NIS 条目进行操作。

## 文件

**`/etc/master.passwd`** 用户数据库
**`/etc/passwd`** Version 7 格式密码文件
**`/etc/pw.XXXXXX`** 临时文件
**`/etc/shells`** 已批准的 shell 列表

## 实例

将当前用户的 shell 更改为 **`/usr/local/bin/zsh`**：

```sh
chsh -s /usr/local/bin/zsh
```

## 参见

finger(1), [login(1)](login.1.md), [passwd(1)](passwd.1.md), getusershell(3), login.conf(5), [passwd(5)](../man5/passwd.5.md), [pw(8)](../man8/pw.8.md), pwd_mkdb(8), vipw(8)

> Robert Morris, Ken Thompson, "UNIX Password security".

## 历史

`chpass` 实用程序首次出现于 4.3BSD-Reno。

## 缺陷

用户信息应该（最终也会）存储在其他地方。
