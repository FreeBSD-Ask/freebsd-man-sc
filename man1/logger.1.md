# logger.1

`logger` — 在系统日志中记录条目

## 名称

`logger`

## 概要

`logger [-46Ais] [-f file] [-H hostname] [-h host] [-P port] [-p pri] [-S addr:port] [-t tag] [message ...]`

## 描述

`logger` 实用程序提供了 syslog(3) 系统日志模块的 shell 命令接口。

可用选项如下：

**`-4`** 强制 `logger` 仅使用 IPv4 地址。

**`-6`** 强制 `logger` 仅使用 IPv6 地址。

**`-A`** 默认情况下，即使主机有多条 A 或 AAAA 记录，`logger` 也仅尝试将消息发送到一个地址。如果指定了此选项，`logger` 会尝试将消息发送到所有地址。

**`-i`** 在每行中记录 logger 进程的进程 ID。此标志会被忽略，进程 ID 始终会被记录。另见 `-t`。

**`-s`** 将消息记录到标准错误以及系统日志。

**`-f`** `file` 将指定文件的内容读入 syslog。当同时指定了 `message` 时，此选项被忽略。

**`-H`** `hostname` 将消息头中的主机名设置为指定值。如果未指定，将使用 gethostname(3) 的主机部分。

**`-h`** `host` 将消息发送到远程系统 `host`，而非在本地记录。注意，`logger` 目前支持 `AF_INET`（IPv4）、`AF_INET6`（IPv6）和 `AF_LOCAL`（Unix 域套接字）地址族。`host` 中有效的地址格式如下：

`AF_INET` **192.168.2.1**

`AF_INET6` **2001:db8::1**

`AF_LOCAL` **/var/run/log**

**`-P`** `port` 将消息发送到远程系统上指定的 `port` 端口号，可指定为服务名或十进制数字。默认为 "`syslog`"。如果使用了未知的服务名，`logger` 会打印警告并回退到端口 514。

**`-p`** `pri` 以指定优先级记录消息。优先级可以以数字方式或 `facility.level` 对的形式指定。例如，"`-p` `local3.info`" 将消息以 `info`（informational）级别记录到 `local3` facility。默认为 "`user.notice`"。

**`-S`** `addr`:`port` 指定使用 `-h` 选项时的源地址和/或源端口。启用 `-A` 标志时，所有远程地址将使用相同的地址。注意，`addr` 中的数字 IPv6 地址必须用 "`[`" 和 "`]`" 括起来。

**`-t`** `tag` 用指定的 `tag` 标记日志中的每一行，而非默认的当前登录名。使用 `-t` `tag[N]` 可插入特定的十进制进程 ID，而非 `logger` 的 ID。

**`message`** 写入日志的消息；如果未指定且未提供 `-f` 标志，则记录标准输入。

## 退出状态

`logger` 实用程序成功时退出码为 0，发生错误时大于 0。

## 实例

```sh
logger System rebooted

logger -p local0.notice -t HOSTIDM -f /dev/idmc
```

## 参见

syslog(3), syslogd(8)

## 标准

`logger` 命令预期与 IEEE Std 1003.2（"POSIX.2"）兼容。
