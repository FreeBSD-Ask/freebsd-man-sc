# protect(1)

`protect` — 保护进程在交换空间耗尽时不被杀死

## 名称

`protect`

## 概要

`protect [-i] command protect [-cdi] -g pgrp protect [-cdi] -p pid`

## 描述

`protect` 命令用于将进程标记为受保护。当交换空间耗尽时，内核不会杀死受保护的进程。注意，此受保护状态默认不被子进程继承。

选项如下：

**`-c`** 移除指定进程的保护。

**`-d`** 将操作应用于指定进程的所有当前子进程。

**`-i`** 将操作应用于指定进程的所有未来子进程。

**`-g`** `pgrp` 将操作应用于指定进程组中的所有进程。

**`-p`** `pid` 将操作应用于指定进程。

**`command`** 以受保护进程身份执行 `command`。

注意，调整现有进程状态时只能指定 `-p` 或 `-g` 标志中的一个。

守护进程可以在启动时通过 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `${name}_oomprotect` 选项进行保护。

## 退出状态

`protect` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

将 Xorg 服务器标记为受保护：

```sh
pgrep Xorg | xargs protect -p
```

保护所有 ssh 会话及其子进程：

```sh
pgrep sshd | xargs protect -dip
```

移除所有当前和未来进程的保护：

```sh
protect -cdi -p 1
```

使用 [ps(1)](ps.1.md) 检查进程是否已应用 protect 标志：

```sh
ps -O flags,flags2 -p 64430
```

```sh
PID F F2 TT STAT TIME COMMAND
```

```sh
64430 10104002 00000001 5 S+ 0:00.00 ./main
```

```sh
^P ^PI
```

在上面的示例中，`P` 指向 protect 标志，`PI` 指向继承标志。如果 `P` 位设置为 1，则进程受保护。如果 `PI` 位设置为 1，则此进程的所有子进程也将受保护。

## 诊断

- `protect` 不是由 root 执行。
- `protect` 在 [jail(8)](../man8/jail.8.md) 中执行，目前不支持此操作。

- `protect: procctl: Operation not permitted` — `protect` 命令没有保护所选进程所需的权限。导致此情况的原因有很多，例如：

## 参见

[ps(1)](ps.1.md), [procctl(2)](../sys/procctl.2.md), [rc.conf(5)](../man5/rc.conf.5.md)

## 缺陷

如果保护一个分配所有内存的失控进程，系统将死锁。
