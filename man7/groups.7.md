# groups.7

`groups` — 标准用户组名

## 名称

`groups`

## 描述

标准的 FreeBSD 安装具有以下用户组名：

***wheel*** 有权将自身提升为 root 用户的超级用户权限的用户，即 uid~0。通常 *wheel* 组的 gid~0。不在 *wheel* 组中的用户永远不被 [su(1)](../man1/su.1.md) 允许获得 root 权限。

***daemon*** 由 set-group-id 程序 lpr(1) 和 [rwho(1)](../man1/rwho.1.md) 使用。

***kmem*** 由需要访问内核内存的 set-group-id 程序（如 ktrdump(8)）使用（**/dev/mem** 和 **/dev/kmem** 属于 *kmem* 组）。参见 [mem(4)](../man4/mem.4.md)。

***sys*** 历史组。在现代 FreeBSD 中未使用。

***tty*** 由 set-group-id 程序 [wall(1)](../man1/wall.1.md) 和 write(1) 使用，以允许用户向另一个 tty 发送消息，即使他们不拥有它（静态 tty 设备节点 **/dev/pts/\*** 都属于 *tty* 组）。参见 [tty(4)](../man4/tty.4.md)。

***operator*** 有权对磁盘设备进行备份并关闭机器的用户。磁盘设备节点（如 **/dev/ada0**）属于 *operator* 组并且组可读，因此组中的用户可以从磁盘设备读取，例如使用 dump(8)。磁带设备节点（如 **/dev/sa0**）属于 *operator* 组，并且组可读且组可写，因此组中的用户可以写入磁带设备。[shutdown(8)](../man8/shutdown.8.md) 程序仅可由 root 和 *operator* 组的成员执行。

***mail*** 由邮件代理（如 dma(8)）使用。默认情况下，root 邮件（**/var/mail/root**）属于 *mail* 组。

***bin*** 历史组。在现代 FreeBSD 中未使用。

***news*** 历史组。在现代 FreeBSD 中未使用。

***man*** 历史组；曾经用于管理手册页（参见 [man(1)](../man1/man.1.md)）。

***games*** 由各种 set-group-id 游戏用于维护 **/var/games** 中的高分文件和其他公共文件。此组的成员还被允许访问 **/dev/input/event\*** 设备节点（参见 [hgame(4)](../man4/hgame.4.md)）。另见 [intro(6)](../man6/intro.6.md)。

***ftp*** 曾经由 sysinstall(8)（现已替换为 bsdinstall(8)）用于设置匿名 FTP。在现代 FreeBSD 中未使用。

***staff*** 员工用户，与访客用户相对（参见 *guest* 组）。FreeBSD 不使用；可由管理员自行解释。关于在 *staff* 组中管理账户的一些建议，请参见 [security(7)](security.7.md)。

***sshd*** 由 sshd(8) 安全 shell 守护进程使用的 *sshd* 伪用户的主组。

***smmsp*** 用户 *smmsp* 的主组，如果没有为运行 sendmail(8) 配置非 root 用户，则由 sendmail(8) 使用。该组名称的含义是“SendMail Message Submission Program”。

***mailnull*** 由电子邮件传输代理 sendmail(8) 用作其默认用户 *mailnull* 的组。

***guest*** 访客用户，与员工用户相对（参见 *staff* 组）。FreeBSD 不使用；可由管理员自行解释。

***audio*** 用于访问由 sound(4) 设备驱动程序和 virtual_oss(8) 创建的任何设备节点。

***video*** 用于访问 **/dev/drm/\*** 设备，这些设备用于 GPU 硬件加速。参见 drm(7)。

***realtime*** 由 [mac_priority(4)](../man4/mac_priority.4.md) 使用，允许此组的成员以实时调度优先级运行线程和进程。另见 rtprio(1)。

***idletime*** 由 [mac_priority(4)](../man4/mac_priority.4.md) 使用，允许此组的成员以空闲调度优先级运行进程。另见 idprio(1)。

***bind*** 曾经用作 named(8) Internet 域名服务器使用的 *bind* 伪用户的主组，已在 FreeBSD 10.0 中从基本系统中移除。

***unbound*** 由 local-unbound(8) 递归 DNS 解析器使用的 *unbound* 伪用户的主组。

***proxy*** 由 [ftp-proxy(8)](../man8/ftp-proxy.8.md) 代理守护进程与 [pf(4)](../man4/pf.4.md) 等数据包过滤器一起使用的 *proxy* 伪用户的主组。

***authpf*** 由 set-group-id 程序 [authpf(8)](../man8/authpf.8.md) 使用，用于配置经过身份验证的网关。

***_pflogd*** 由 pflogd(8) 日志守护进程与 [pf(4)](../man4/pf.4.md) 数据包过滤器一起使用的 *_pflogd* 伪用户的主组。

***_dhcp*** 由 dhclient(8) DHCP 客户端使用的 *_dhcp* 伪用户的主组。

***dialer*** 有权进行拨出调制解调器呼叫的用户（参见 cu(1) 和 **/dev/cuauN** 设备）。

***network*** 历史组。在现代 FreeBSD 中未使用。

***audit*** 由 auditd(8) 和 auditdistd(8) 审计守护进程使用的 *auditdistd* 伪用户的主组。

***www*** 用于访问万维网的历史组。在现代 FreeBSD 中未使用。

***u2f*** 用于需要访问 **/dev/u2f/\*** 设备的用户（参见 [u2f(4)](../man4/u2f.4.md)）。

***ntpd*** 由 ntpd(8) 网络时间协议守护进程使用的 *ntpd* 伪用户的主组。

***_ypldap*** 由 ypldap(8) 守护进程使用的 *_ypldap* 伪用户的主组。

***hast*** 由高可用性存储守护进程 hastd(8) 使用的 *hast* 伪用户的主组。

***tests*** 由请求以非特权身份运行的自动测试使用的 *tests* 伪用户的主组。参见 [tests(7)](tests.7.md)。

***nogroup*** 伪组（假组）。它与 *nobody* 组的不同之处在于 *nogroup* 没有专用的用户。例如，此组用于用户 *tty* 和 *kmem*。

***nobody*** 传统 *nobody* 伪用户的主组。现代做法是为每个不同的守护进程分配其自己独立的伪用户账户和组，这样一个守护进程被攻破时不会危及所有其他守护进程。另见 *nogroup* 组。

## 文件

**`/etc/group`** 主组权限文件。
**`/usr/src/etc/group`** 基本系统的组权限文件。
**`/usr/ports/GIDs`** 为 ports 保留的 GID（组 ID）列表（参见 [ports(7)](ports.7.md)）。

关于上述文件的格式，请参见 [group(5)](../man5/group.5.md)。

## 参见

[chgrp(1)](../man1/chgrp.1.md), [groups(1)](../man1/groups.1.md), [id(1)](../man1/id.1.md), newgrp(1), [group(5)](../man5/group.5.md), [pw(8)](../man8/pw.8.md)

## 历史

`groups` 手册页出现于 NetBSD 10.0 和 FreeBSD 15.1。
