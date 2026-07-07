# login(1)

`login` — 登录到计算机

## 名称

`login`

## 概要

`login [-fp] [-h hostname] [user]`

## 描述

`login` 实用程序用于将用户（及伪用户）登录到计算机系统。

如果未指定用户，或指定了用户但该用户认证失败，`login` 会提示输入用户名。用户认证可通过 pam(8) 配置。默认采用密码认证。

可用选项如下：

**`-f`** 当指定了用户名时，此选项表示已完成正确的认证，无需再请求密码。此选项仅可由超级用户使用，或已登录用户以自身身份再次登录时使用。

**`-h`** 指定接收连接的来源主机。该选项被 `telnetd` 等各类守护进程使用。此选项仅可由超级用户使用。

**`-p`** 默认情况下，`login` 会丢弃之前的环境。`-p` 选项禁用此行为。

登录访问可通过 login.access(5) 或 login.conf(5) 中的登录类别进行控制，后者基于时间、tty 和远程主机名提供允许和拒绝记录。

如果文件 **`/etc/fbtab`** 存在，`login` 会更改此文件中指定的某些设备的保护和属主。

在用户登录后，`login` 会立即显示该用户上次登录的日期和时间、当日消息以及其他信息。如果用户主目录中存在文件 `.hushlogin`，所有这些消息都会被抑制。这是为了简化非人类用户（如 uucp(1)）的登录流程。

`login` 实用程序会向环境（参见 [environ(7)](../man7/environ.7.md)）中写入信息，指定用户的主目录（HOME）、命令解释器（SHELL）、搜索路径（PATH）、终端类型（TERM）和用户名（LOGNAME 和 USER）。根据用户系统 passwd 记录中分配的登录类别，登录类别能力数据库中的条目还可能设置其他环境变量。登录类别还控制登录所获得的最大和当前进程资源限制、进程优先级以及用户登录环境的许多其他方面。

某些 shell 可能提供与此实用程序类似或相同的内建 `login` 命令。请参阅 [builtin(1)](builtin.1.md) 手册页。

`login` 实用程序在登录成功或失败时会提交审计记录。如果无法确定当前审计状态，`login` 将以错误退出。

## 文件

**`/etc/fbtab`** 更改设备保护

**`/etc/login.conf`** 登录类别能力数据库

**`/var/run/motd`** 当日消息

**`/var/mail/user`** 系统邮箱

**`.hushlogin`** 使登录更安静

**`/etc/pam.d/login`** pam(8) 配置文件

**`/etc/security/audit_user`** 审计用户标志

**`/etc/security/audit_control`** 全局审计标志

## 参见

[builtin(1)](builtin.1.md), chpass(1), [csh(1)](csh.1.md), newgrp(1), [passwd(1)](passwd.1.md), rlogin(1), getpass(3), [fbtab(5)](../man5/fbtab.5.md), login.access(5), login.conf(5), [environ(7)](../man7/environ.7.md)

## 历史

`login` 实用程序首次出现于 Version 6 AT&T UNIX。
