# ssh-copy-id.1

`ssh-copy-id` — 将公钥复制到远程主机

## 名称

`ssh-copy-id`

## 概要

`ssh-copy-id [-lv] [-i keyfile] [-o option] [-p port] [user@]hostname`

## 描述

`ssh-copy-id` 工具将公钥复制到远程主机的 **~/.ssh/authorized_keys** 文件中（如有需要，会创建该文件和目录）。

可用选项如下：

**`-i`** `file` 复制 `file` 中包含的公钥。此选项可多次指定，并可与 `-l` 选项组合使用。如果指定了私钥且找到了对应的公钥，则使用公钥。

**`-l`** 复制 ssh-agent(1) 当前持有的密钥。如果未指定 `-i` 选项，则此为默认行为。

**`-o`** `ssh-option` 将此选项直接传递给 [ssh(1)](ssh.1.md)。此选项可多次指定。

**`-p`** `port` 连接到远程主机上的指定端口，而非默认端口。

**`-v`** 将 `-v` 传递给 [ssh(1)](ssh.1.md)。

其余参数为要连接的远程主机列表，每个主机可附带用户名。

## 退出状态

`ssh-copy-id` 工具成功时退出值为 0，发生错误时大于 0。

## 实例

将特定密钥发送到多台主机：

```sh
$ ssh-copy-id -i /path/to/keyfile.pub user@host1 user@host2 user@host3
```

## 历史

`ssh-copy-id` 工具由 Eitan Adler <eadler@FreeBSD.org> 编写，作为 OpenSSH 中已有同名工具的直接替代品。
