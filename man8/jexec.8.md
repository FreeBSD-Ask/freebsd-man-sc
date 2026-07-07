# jexec(8)

`jexec` — 在已存在的 jail 中执行命令

## 名称

`jexec`

## 概要

`jexec [-l] [-d working-directory] [[-e name=value]...] [-u username | -U username] jail [command ...]`

## 描述

`jexec` 工具在由 jid 或名称标识的 `jail` 内执行 `command`。如果未指定 `command`，则使用用户的 shell。

可用选项如下：

**`-d`** `working-directory` 在 jail 内运行命令的工作目录。默认为 jail 的根目录。

**`-l`** 在干净的环境中执行。除 `HOME`、`SHELL`、`TERM`、`USER`，以及用户登录类能力数据库中的任何内容外，其他环境变量都会被丢弃。`PATH` 被设置为 **/bin:/usr/bin**。如果指定了用户（通过 `-u` 或 `-U`），且未使用 `-d` 选项，则从该（可能位于 jail 内的）用户的目录运行命令。

**`-e`** `name`=`value` 设置环境变量。此参数允许为在 jail 内执行的进程提供任意环境变量，并覆盖之前定义的任何环境变量，例如由 `-l` 参数指定的环境变量。此选项可以多次设置。

**`-u`** `username` 主机环境中运行 `command` 的用户名。此为默认值。

**`-U`** `username` jail 环境中运行 `command` 的用户名。

## 实例

### 示例 1：在 jail 中打开 shell

以下命令通过名称指定 jail，并使用当前用户的 shell：

```sh
# jexec name
```

也可以通过 jid 指定 jail：

```sh
# jexec JID
```

### 示例 2：运行单个命令而不打开 shell

以下命令在名为 "name" 的 jail 中运行 `uname -a`。由于显式指定了命令，`jexec` 不会启动交互式 shell，而是直接执行指定的命令。

```sh
# jexec name uname -a
```

### 示例 3：在干净环境的 jail 中打开 shell

以下命令在具有干净环境的 jail 中打开 [sh(1)](../man1/sh.1.md) shell：

```sh
# jexec -l name sh
```

### 示例 4：使用 login 命令在 jail 中打开 shell

以下命令使用 [login(1)](../man1/login.1.md) 访问 jail，提交审计记录，并显示用户的上次登录信息、系统版权和 [motd(5)](../man5/motd.5.md) 消息：

```sh
# jexec -l name login -f root
```

## 参见

jail_attach(2), [jail(8)](jail.8.md), [jls(8)](jls.8.md)

## 历史

`jexec` 工具在 FreeBSD 5.1 中加入。

## 缺陷

如果 jail 不是通过 `jid` 标识的，则在查找 jail 与在 jail 内执行命令之间可能存在竞争条件。给定 `jid` 也有类似的竞争，因为另一个进程可以在用户查找 `jid` 之后停止该 jail 并启动另一个 jail。
