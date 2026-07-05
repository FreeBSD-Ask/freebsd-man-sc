# hosts.equiv.5

`hosts.equiv` — 受信任的远程主机和用户名数据库

## 名称

`hosts.equiv`, `rhosts`

## 描述

`hosts.equiv` 和 `.rhosts` 文件包含有关网络上受信任主机和用户的信息。对于每个主机，应存在单独一行，包含以下信息：

简单形式

```sh
hostname [username]
```

或更详细的形式

```sh
[+-][hostname|@netgroup] [[+-][username|@netgroup]]
```

"@" 表示按 netgroup 指定主机或按 netgroup 指定用户。单个 "+" 匹配所有主机或用户。以 "-" 开头的主机名将拒绝所有匹配的主机及其所有用户。以 "-" 开头的用户名将拒绝来自匹配主机的所有匹配用户。

各项之间由任意数量的空格和/或制表符分隔。"#" 表示注释开始；从 "#" 到行尾的字符不会被搜索该文件的例程解释。

主机名以常规的 Internet DNS 点分域 "."（点）表示法指定，使用 Internet 地址操作库 inet(3) 中的 inet_addr(3) 例程。主机名可以包含除字段分隔符、换行符或注释字符以外的任何可打印字符。

出于安全原因，如果用户的 `.rhosts` 文件不是常规文件，或者不属于该用户所有，或者该用户以外的任何人可以写入，则该文件将被忽略。

## 文件

**`/etc/hosts.equiv`** `.rhosts` 文件位于 **/etc**。
**`$HOME/.rhosts`** `.rhosts` 文件位于 `$HOME`。

## 实例

```sh
bar.com foo
```

信任来自主机 "bar.com" 的用户 "foo"。

```sh
+@allclient
```

信任来自 netgroup "allclient" 的所有主机。

```sh
+@allclient -@dau
```

信任来自 netgroup "allclient" 的所有主机及其用户，但来自 netgroup "dau" 的用户除外。

## 参见

gethostbyname(3), inet(3), innetgr(3), ruserok(3), netgroup(5), [ifconfig(8)](../man8/ifconfig.8.md), [yp(8)](../man8/yp.8.md)

## 缺陷

本手册页不完整。更多信息请阅读 `src/lib/libc/net/rcmd.c` 中的源代码或 SunOS 手册页。
