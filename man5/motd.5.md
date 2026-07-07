# motd(5)

`motd` — 包含每日消息的文件

## 名称

`motd`

## 描述

文件 **/var/run/motd** 通常在用户登录之后、运行 shell 之前由 [login(1)](../man1/login.1.md) 显示。该文件一般用于发布重要的全系统公告。系统启动时，会在 **/etc/motd.template** 前面添加一行包含内核版本字符串的内容，并将结果写入 **/var/run/motd**。

更新 **/etc/motd.template** 后，无需重启系统即可通过手动重启 motd 服务来更新 **/var/run/motd**：

```sh
service motd restart
```

用户可以在自己的主目录中创建一个名为 “`.hushlogin`” 的文件，或者通过 login.conf(5) 来禁止显示该文件。

## 文件

**/etc/motd** 指向 **/var/run/motd** 的符号链接。

**/etc/motd.template** 系统管理员可编辑的模板文件。

**/var/run/motd** 每日消息。

**$HOME/.hushlogin** 禁止输出 **/var/run/motd**。

## 实例

```sh
FreeBSD 12.1-RELEASE (GENERIC) #0: Sun Dec 29 03:08:31 PST 2019
/home is full.  Please cleanup your directories.
```

## 参见

[login(1)](../man1/login.1.md), login.conf(5)

## 历史

在 FreeBSD 13.0 之前，`motd` 位于 **/etc** 目录下。
