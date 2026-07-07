# passwd(5)

`passwd` — 密码文件格式

## 名称

`passwd`, `master.passwd`, `pwd.db`, `spwd.db`

## 描述

`spwd.db` 文件是密码信息的本地数据源。它们可以与 Hesiod 域 “`passwd`” 和 “`uid`”，以及 NIS 映射 “`passwd.byname`”、“`passwd.byuid`”、“`master.passwd.byname`” 和 “`master.passwd.byuid`” 结合使用，由 [nsswitch.conf(5)](nsswitch.conf.5.md) 控制。

为保持一致性，这些文件都不应被手动修改。

`master.passwd` 文件仅可由 root 读取，由换行符分隔的记录组成，每个用户一条记录，包含十个以冒号（`:`）分隔的字段。这些字段如下：

**`name`** 用户的登录名。

**`password`** 用户的 *加密* 密码。

**`uid`** 用户 ID。

**`gid`** 用户的登录组 ID。

**`class`** 用户的登录类。

**`change`** 密码更改时间。

**`expire`** 账户过期时间。

**`gecos`** 关于用户的一般信息。

**`home_dir`** 用户的主目录。

**`shell`** 用户的登录 shell。

`master.passwd` 文件由 pwd_mkdb(8) 从 `master.passwd` 文件生成，移除了 `class`、`change` 和 `expire` 字段，并将 `password` 字段替换为 `*` 字符。

`name` 字段是用于访问计算机账户的登录名，`uid` 字段是与之关联的数字。两者都应在整个系统（通常也跨越一组系统）中保持唯一，因为它们控制文件访问。

虽然可以有多条具有相同登录名和/或相同用户 ID 的记录，但这样做通常是错误的。操作这些文件的例程通常只会返回多条记录中的一条，并且是随机选择的一条。

登录名不能以连字符（`-`）开头，不能包含 8 位字符、制表符或空格，也不能包含以下任何符号：`,:+&#%^()!@~*?<>=|\`。美元符号（`$`）仅允许作为最后一个字符，以用于 Samba。任何字段都不能包含冒号（`:`），因为历史上一直使用它来分隔用户数据库中的字段。

大小写敏感。登录名 `Lrrr` 和 `lrrr` 代表不同的用户。在与不具有大小写敏感登录名的系统互操作时请注意这一点。

在 `master.passwd` 文件中，`password` 字段是密码的 *加密* 形式，参见 crypt(3)。如果 `password` 字段为空，则访问该机器不需要密码。这几乎总是一个错误，因此 PAM 等认证组件可以强制禁止对无密码账户的远程访问。由于此文件包含加密的用户密码，没有适当权限的任何人都不应读取它。

`*` 密码表示该账户的密码认证已被禁用（通过其他形式的认证登录，例如使用 [ssh(1)](../man1/ssh.1.md) 密钥，仍然可以工作）。该字段仅包含加密密码，而 `*` 永远不可能是加密密码的结果。

以 `*LOCKED*` 为前缀的加密密码意味着该账户已被临时锁定，任何人都无法使用任何认证方式登录。有关账户锁定的便捷命令行界面，请参见 [pw(8)](../man8/pw.8.md)。

`group` 字段是用户登录时将归属的组。由于此系统支持多个组（参见 [groups(1)](../man1/groups.1.md)），此字段目前几乎没有特殊含义。

`class` 字段是用户登录类的键。登录类在 login.conf(5) 中定义，这是一个 termcap(5) 风格的用户属性、记账、资源和环境设置数据库。

`change` 字段是从纪元（UTC）起至账户密码必须更改的秒数。此字段可以留空以关闭密码老化功能；值为零等同于将该字段留空。

`expire` 字段是从纪元（UTC）起至账户过期的秒数。此字段可以留空以关闭账户老化功能；值为零等同于将该字段留空。

`gecos` 字段通常包含以逗号（`,`）分隔的子字段，如下所示：

**`name`** 用户的全名

**`office`** 用户的办公室号码

**`wphone`** 用户的工作电话号码

**`hphone`** 用户的家庭电话号码

完整的 `name` 可以包含与号（`&`），当 `gecos` 字段被 finger(1)、sendmail(8) 等程序显示或使用时，它将被替换为首字母大写的登录 `name`。

`office` 和电话号码子字段由 finger(1) 程序以及其他可能的应用程序使用。

用户的主目录 `home_dir` 是用户登录时将归属的完整 UNIX 路径名。

`shell` 字段是用户首选的命令解释器。如果 `shell` 字段为空，则假定使用 Bourne shell（**/bin/sh**）。一劳永逸地禁用账户登录的常规做法（如对系统账户所做的那样）是将其 `shell` 设置为 **/sbin/nologin**（参见 nologin(8)）。

## HESIOD 支持

如果在 [nsswitch.conf(5)](nsswitch.conf.5.md) 中为 “`passwd`” 数据库指定了 “`dns`”，则 `master.passwd` 查找将从 “`passwd`” Hesiod 域进行。

## NIS 支持

如果在 [nsswitch.conf(5)](nsswitch.conf.5.md) 中为 “`passwd`” 数据库指定了 “`nis`”，则 `master.passwd` 查找将从 “`passwd.byname`”、“`passwd.byuid`”、“`master.passwd.byname`” 和 “`master.passwd.byuid`” NIS 映射进行。

## COMPAT 支持

如果在 [nsswitch.conf(5)](nsswitch.conf.5.md) 中为 “`passwd`” 数据库指定了 “`compat`”，并且为 “`passwd_compat`” 数据库指定了 “`dns`” 或 “`nis`”，则 `master.passwd` 文件还支持基于用户名和 netgroup 的标准 “`+`/`-`” 排除和包含。

以 `-`（减号）开头的行是标记为从任何后续包含中排除的条目，包含以 `+`（加号）标记。

如果行的第二个字符是 `@`（at 符号），则操作涉及由 `name` 字段其余字符指定的 netgroup 中所有条目的用户字段。否则，假定 `name` 字段的其余部分是特定的用户名。

`+` 标记也可以单独出现在 `name` 字段中，这将导致来自 Hesiod 域 `master.passwd`（使用 “`passwd_compat: dns`”）或 “`passwd.byname`” 和 “`passwd.byuid`” NIS 映射（使用 “`passwd_compat: nis`”）的所有用户被包含。

如果条目包含非空的 `uid` 或 `gid` 字段，则指定的数字将覆盖从 Hesiod 域或 NIS 映射检索到的信息。同样，如果 `gecos`、`dir` 或 `shell` 条目包含文本，它将覆盖通过 Hesiod 或 NIS 包含的信息。在某些系统上，`passwd` 字段也可能被覆盖。

## 文件

**/etc/passwd** ASCII 密码文件，已移除密码

**/etc/pwd.db** db(3) 格式的密码数据库，已移除密码

**/etc/master.passwd** ASCII 密码文件，密码完整

**/etc/spwd.db** db(3) 格式的密码数据库，密码完整

## 兼容性

密码文件格式自 4.3BSD 以来已更改。以下 awk 脚本可用于将旧式密码文件转换为新式密码文件。新增的 `class`、`change` 和 `expire` 字段会被添加，但默认情况下处于关闭状态（将这些字段设置为零等同于将它们留空）。Class 目前未实现，但 change 和 expire 已实现；要设置它们，请使用从纪元起的当前秒数 + 你想要的任何偏移秒数。

```sh
BEGIN { FS = ":"}
{ print $1 ":" $2 ":" $3 ":" $4 "::0:0:" $5 ":" $6 ":" $7 }
```

## 参见

chpass(1), [login(1)](../man1/login.1.md), [passwd(1)](../man1/passwd.1.md), crypt(3), getpwent(3), login.conf(5), netgroup(5), [nsswitch.conf(5)](nsswitch.conf.5.md), [groups(7)](../man7/groups.7.md), [adduser(8)](../man8/adduser.8.md), nologin(8), [pw(8)](../man8/pw.8.md), pwd_mkdb(8), vipw(8), [yp(8)](../man8/yp.8.md)

Managing NFS and NIS (O'Reilly & Associates)

## 历史

`master.passwd` 文件格式首次出现在 Version 1 AT&T UNIX 中。

NIS `master.passwd` 文件格式首次出现在 SunOS 中。

Hesiod 支持首次出现在 FreeBSD 4.1 中。它是从 NetBSD 项目导入的，最初出现在 NetBSD 1.4 中。

## 缺陷

用户信息应当（最终将会）存储在其他地方。

将 “`compat`” 排除条目放在文件中任何包含条目之后会产生意外结果。
