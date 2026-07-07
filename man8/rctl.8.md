# rctl(8)

`rctl` — 显示和更新资源限制数据库

## 名称

`rctl`

## 概要

`rctl [-h] [-n] [filter ...]` `rctl -a rule ...` `rctl -l [-h] [-n] filter ...` `rctl -r filter ...` `rctl -u [-h] filter ...`

## 描述

不带选项调用时，`rctl` 命令将当前定义的 RCTL 规则写入标准输出。

如果指定了 `filter` 参数，则仅显示匹配该过滤器的规则。选项如下：

**`-a`** `rule` 将 `rule` 添加到 RCTL 数据库。

**`-l`** `filter` 显示适用于由 `filter` 定义的进程的规则。注意，这与不带任何选项调用时显示规则不同，因为它不仅显示主体等于该进程的规则，还显示适用于该进程的用户、Jail 和登录类的规则。

**`-r`** `filter` 从 RCTL 数据库中移除匹配 `filter` 的规则。

**`-u`** `filter` 显示匹配 `filter` 的主体（ **process** 、 **user** 、 **loginclass** 或 **jail** ）的资源使用情况。

**`-h`** “人类可读”输出。使用单位后缀：Byte、Kilobyte、Megabyte、Gigabyte、Terabyte 和 Petabyte。

**`-n`** 以数字形式显示用户 ID，而不是将其转换为用户名。

修改规则会影响所有当前运行以及未来匹配该规则的进程。

## 规则语法

规则的语法为 subject:subject-id:resource:action=amount/per。

**subject** 定义规则适用的实体类型。可以是 **process** 、 **user** 、 **loginclass** 或 **jail** 。

**subject-id** 标识 *subject* 。可以是进程 ID、用户名、数字用户 ID、来自 [login.conf(5)](../man5/login.conf.5.md) 的登录类名或 Jail 名称。

**resource** 标识规则控制的资源。详情参见下文的 RESOURCES 章节。

**action** 定义当进程超过允许的 *amount* 时会发生什么。详情参见下文的 ACTIONS 章节。

**amount** 定义在触发所定义的 *action* 之前，进程可以使用多少资源。限制字节数的资源可以使用 expand_number(3) 中的前缀。

**per** 定义 *amount* 针对哪个实体进行核算。例如，规则 "loginclass:users:vmemoryuse:deny=100M/process" 表示属于登录类 "users" 的任何用户的每个进程最多可分配 100MB 虚拟内存。规则 "loginclass:users:vmemoryuse:deny=100M/user" 表示对于属于登录类 "users" 的每个用户，该用户所有进程分配的虚拟内存总和不会超过 100MB。规则 "loginclass:users:vmemoryuse:deny=100M/loginclass" 表示属于该登录类的所有用户的所有进程分配的虚拟内存总和不会超过 100MB。

有效的规则指定了所有这些字段，但 *per* 除外，它默认为 *subject* 的值。

过滤器是 *per* 之外的一个或多个字段留空的规则。例如，匹配每条规则的过滤器可以写成 ":::=/"，或简写为 ":"。匹配所有登录类的过滤器为 "loginclass:"。匹配 **maxproc** 资源的所有已定义规则的过滤器为 "::maxproc"。

## 主体

| **process** | 数字进程 ID |
| --- | --- |
| **user** | 用户名或数字用户 ID |
| **loginclass** | 来自 [login.conf(5)](../man5/login.conf.5.md) 的登录类 |
| **jail** | Jail 名称 |

## 资源

| **cputime** | CPU 时间，以秒为单位 |
| --- | --- |
| **datasize** | 数据大小，以字节为单位 |
| **stacksize** | 栈大小，以字节为单位 |
| **coredumpsize** | 核心转储大小，以字节为单位 |
| **memoryuse** | 驻留集大小，以字节为单位 |
| **memorylocked** | 锁定内存，以字节为单位 |
| **maxproc** | 进程数 |
| **openfiles** | 文件描述符表大小 |
| **vmemoryuse** | 地址空间限制，以字节为单位 |
| **pseudoterminals** | PTY 数量 |
| **swapuse** | 可预留或使用的交换空间，以字节为单位 |
| **nthr** | 线程数 |
| **msgqqueued** | 排队的 SysV 消息数 |
| **msgqsize** | SysV 消息队列大小，以字节为单位 |
| **nmsgq** | SysV 消息队列数 |
| **nsem** | SysV 信号量数 |
| **nsemop** | 单次 [semop(2)](../sys/semop.2.md) 调用中修改的 SysV 信号量数 |
| **nshm** | SysV 共享内存段数 |
| **shmsize** | SysV 共享内存大小，以字节为单位 |
| **wallclock** | 挂钟时间，以秒为单位 |
| **pcpu** | %CPU，以单个 CPU 核心百分比为单位 |
| **readbps** | 文件系统读取，以字节/秒为单位 |
| **writebps** | 文件系统写入，以字节/秒为单位 |
| **readiops** | 文件系统读取，以操作数/秒为单位 |
| **writeiops** | 文件系统写入，以操作数/秒为单位 |

## 操作

| **deny** | 拒绝分配；不支持 **cputime** 、 **wallclock** 、 **readbps** 、 **writebps** 、 **readiops** 和 **writeiops** |
| --- | --- |
| **log** | 向控制台记录警告 |
| **devctl** | 使用 **system** = "RCTL"、 **subsystem** = "rule"、 **type** = "matched" 向 devd(8) 发送通知 |
| **sig\*** （例如 **sigterm** ） | 向违规进程发送信号。支持的信号列表参见 [signal(3)](../gen/signal.3.md) |
| **throttle** | 减慢进程执行；仅支持 **readbps** 、 **writebps** 、 **readiops** 和 **writeiops** |

并非所有操作都支持所有资源。尝试添加具有给定资源不支持的操作的规则将导致错误。

## 退出状态

`rctl` 工具成功时退出码为 0，发生错误时 >0。

## 实例

阻止用户 "joe" 分配超过 1GB 的虚拟内存：

```sh
`rctl` `-a` `user:joe:vmemoryuse:deny=1g`
```

移除所有 RCTL 规则：

```sh
`rctl` `-r` `:`
```

显示名为 "www" 的 Jail 的资源使用信息：

```sh
`rctl` `-hu` `jail:www`
```

显示适用于 PID 为 512 的进程的所有规则：

```sh
`rctl` `-l` `process:512`
```

显示所有规则：

```sh
`rctl`
```

显示匹配用户 "joe" 的所有规则：

```sh
`rctl` `user:joe`
```

显示匹配登录类的所有规则：

```sh
`rctl` `loginclass:`
```

## 参见

[cpuset(1)](../man1/cpuset.1.md), [rctl(4)](../man4/rctl.4.md), [rctl.conf(5)](../man5/rctl.conf.5.md)

## 历史

`rctl` 命令出现于 FreeBSD 9.0。

## 作者

`rctl` 由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。

## 缺陷

限制 **memoryuse** 可能因系统过度颠簸而导致机器崩溃。

**readiops** 和 **writeiops** 计数器仅为近似值。与 **readbps** 和 **writebps** 一样，它们在文件系统层计算，在该层难以甚至无法观察实际的磁盘设备操作。

**writebps** 和 **writeiops** 资源通常统计的是对文件系统缓存的写入，而非对实际设备的写入。
