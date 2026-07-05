# id.1

`id` — 返回用户身份

## 名称

`id`

## 概要

`id [user] id -A id -G [-n] [user] id -M id -P [user] id -c id -d [user] id -g [-nr] [user] id -p [user] id -s [user] id -u [-nr] [user]`

## 描述

`id` 实用程序将调用进程的用户和组名以及数字 ID 显示到标准输出。如果实际 ID 和有效 ID 不同，则两者都显示；否则只显示实际 ID。

如果指定了 `user`（登录名或用户 ID），则显示该用户的用户和组 ID。在这种情况下，假定实际 ID 和有效 ID 相同。

选项如下：

**`-A`** 显示进程审计用户 ID 和其他进程审计属性，这需要特权。

**`-G`** 以空格分隔的数字形式显示不同的组 ID（有效的、实际的和补充的），顺序不定。

**`-M`** 显示当前进程的 MAC 标签。

**`-P`** 以密码文件条目的形式显示 ID。

**`-a`** 为兼容其他 `id` 实现而忽略。

**`-c`** 显示当前登录类。

**`-d`** 显示当前或指定用户的家目录。

**`-g`** 以数字形式显示有效组 ID。

**`-n`** 对于 `-G`、`-g` 和 `-u` 选项，显示用户或组 ID 的名称而非数字。如果任何 ID 号无法映射为名称，则照常显示数字。

**`-p`** 使输出易于阅读。如果 getlogin(2) 返回的用户名与用户 ID 引用的登录名不同，则显示 getlogin(2) 返回的名称，前面加上关键字 "login"。用户 ID 以名称形式显示，前面加上关键字 "uid"。如果有效用户 ID 与实际用户 ID 不同，则实际用户 ID 以名称形式显示，前面加上关键字 "euid"。如果有效组 ID 与实际组 ID 不同，则实际组 ID 以名称形式显示，前面加上关键字 "rgid"。然后以名称形式显示用户所属的组列表，前面加上关键字 "groups"。每项显示单独一行。

**`-r`** 对于 `-g` 和 `-u` 选项，显示实际 ID 而非有效 ID。

**`-s`** 显示当前或指定用户的 shell。

**`-u`** 以数字形式显示有效用户 ID。

## 退出状态

`id` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

以密码文件条目的形式显示用户 `bob` 的信息：

```sh
$ id -P bob
bob:*:0:0::0:0:Robert:/bob:/usr/local/bin/bash
```

与 root 用户的 [groups(1)](groups.1.md) 输出相同：

```sh
$ id -Gn root
wheel operator
```

显示关于 `alice` 的易读信息：

```sh
$ id -p alice
uid     alice
groups  alice webcamd vboxusers
```

假设用户 `bob` 执行了 “`su` `-l`” 来模拟 root 登录，比较以下命令的结果：

```sh
# id -un
root
# who am i
bob          pts/5        Dec  4 19:51
```

## 参见

[groups(1)](groups.1.md), [who(1)](who.1.md), [groups(7)](../man7/groups.7.md)

## 标准

`id` 实用程序预期符合 IEEE Std 1003.1-2024 (POSIX.1)。`-A`、`-M`、`-P`、`-c`、`-d`、`-p` 和 `-s` 选项是 FreeBSD 扩展。

## 历史

历史上的 [groups(1)](groups.1.md) 命令等同于 “`id` `-Gn` [`user`]”。

历史上的 [whoami(1)](whoami.1.md) 命令等同于 “`id` `-un`”。

`id` 命令首次出现于 4.4BSD。
