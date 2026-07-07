# syslog(3)

`syslog` — 控制系统消息日志

## 名称

`syslog`, `vsyslog`, `openlog`, `closelog`, `setlogmask`

## 库

Lb libc

## 概要

`#include <syslog.h>`

```c
void
syslog(int priority, const char *message, ...);

void
openlog(const char *ident, int logopt, int facility);

void
closelog(void);

int
setlogmask(int maskpri);
```

`#include <syslog.h>`

`#include <stdarg.h>`

```c
void
vsyslog(int priority, const char *message, va_list args);
```

## 描述

`syslog` 函数将 `message` 写入系统消息记录器。消息随后会被写入系统控制台、日志文件、已登录的用户，或转发到其他机器。（参见 syslogd(8)）

消息与 [printf(3)](../stdio/printf.3.md) 格式字符串相同，只是 `%m` 会被替换为当前错误消息。（由全局变量 `errno` 表示；参见 [strerror(3)](../string/strerror.3.md)）如果末尾没有换行符，则会自动添加。

`vsyslog` 函数是另一种形式，其中参数通过 [stdarg(3)](../man3/stdarg.3.md) 的可变长度参数功能捕获。

消息以 `priority` 标记。优先级编码为 `facility`（设施）和 *level*（级别）。设施描述了生成消息的系统部分。级别从以下*有序*（从高到低）列表中选择：

**`LOG_EMERG`** 紧急状况。通常会广播给所有用户。

**`LOG_ALERT`** 应当立即纠正的状况，例如损坏的系统数据库。

**`LOG_CRIT`** 严重状况，例如硬设备错误。

**`LOG_ERR`** 错误。

**`LOG_WARNING`** 警告消息。

**`LOG_NOTICE`** 非错误状况，但可能需要特别处理。

**`LOG_INFO`** 信息性消息。

**`LOG_DEBUG`** 包含通常仅在调试程序时才有用信息的消息。

`openlog` 函数为 `syslog` 和 `vsyslog` 发送的消息提供更专门的处理。`ident` 参数是一个将添加到每条消息前缀的字符串。它可以格式化为 `ident[N]`，此时十进制数 `N` 会替换消息中的进程 ID。`logopt` 参数是指定日志选项的位字段，由以下一个或多个值通过按位或组成：

**`LOG_CONS`** 如果 `syslog` 无法将消息传递给 syslogd(8)，它会尝试将消息写入控制台（**/dev/console**）。

**`LOG_NDELAY`** 立即打开与 syslogd(8) 的连接。通常打开操作会延迟到记录第一条消息时。对于需要管理文件描述符分配顺序的程序很有用。

**`LOG_PERROR`** 将消息同时写入标准错误输出和系统日志。

**`LOG_PID`** 在每条消息中记录进程 ID：用于标识守护进程的实例。在 FreeBSD 上，此选项默认启用且无法禁用。

`facility` 参数为所有未显式编码设施的消息编码一个默认设施：

**`LOG_AUTH`** 授权系统：[login(1)](../man1/login.1.md)、[su(1)](../man1/su.1.md)、getty(8) 等。

**`LOG_AUTHPRIV`** 与 `LOG_AUTH` 相同，但记录到仅特定人员可读的文件中。

**`LOG_CONSOLE`** 由内核控制台输出驱动程序写入 **/dev/console** 的消息。

**`LOG_CRON`** cron 守护进程：cron(8)。

**`LOG_DAEMON`** 系统守护进程，例如 [routed(8)](../man8/routed.8.md)，未由其他设施显式提供的。

**`LOG_FTP`** 文件传输协议守护进程：[ftpd(8)](../man8/ftpd.8.md)、[tftpd(8)](../man8/tftpd.8.md)。

**`LOG_KERN`** 由内核生成的消息。这些消息不能由任何用户进程生成。

**`LOG_LPR`** 行式打印机假脱机系统：lpr(1)、lpc(8)、lpd(8) 等。

**`LOG_MAIL`** 邮件系统。

**`LOG_NEWS`** 网络新闻系统。

**`LOG_NTP`** 网络时间协议系统。

**`LOG_SECURITY`** 安全子系统，例如 ipfw(4)。

**`LOG_SYSLOG`** 由 syslogd(8) 内部生成的消息。

**`LOG_USER`** 由随机用户进程生成的消息。如果未指定，这是默认的设施标识符。

**`LOG_UUCP`** UUCP 系统。

**`LOG_LOCAL0`** 保留供本地使用。`LOG_LOCAL1` 到 `LOG_LOCAL7` 同理。

`closelog` 函数可用于关闭日志文件。

`setlogmask` 函数将日志优先级掩码设置为 `maskpri`，并返回之前的掩码。对 `syslog` 的调用如果优先级未在 `maskpri` 中设置，则会被拒绝。单个优先级 `pri` 的掩码由宏 `LOG_MASK(pri)` 计算；直到并包括 `toppri` 的所有优先级的掩码由宏 `LOG_UPTO(toppri)` 给出。默认情况下允许记录所有优先级。

## 返回值

`closelog`、`openlog`、`syslog` 和 `vsyslog` 例程不返回值。

`setlogmask` 例程始终返回之前的日志掩码级别。

## 实例

```c
syslog(LOG_ALERT, "who: internal error 23");
openlog("ftpd", LOG_PID | LOG_NDELAY, LOG_FTP);
setlogmask(LOG_UPTO(LOG_ERR));
syslog(LOG_INFO, "Connection from host %d", CallingHost);
syslog(LOG_ERR|LOG_LOCAL2, "foobar error: %m");
```

## 参见

[logger(1)](../man1/logger.1.md), syslogd(8)

## 历史

这些函数出现于 4.2BSD。

## 缺陷

切勿在未使用 `%s` 的情况下将包含用户提供数据的字符串作为格式字符串传递。攻击者可以在字符串中放入格式说明符来破坏栈，可能导致安全漏洞。即使字符串是使用 `snprintf` 等函数构建的也是如此，因为生成的字符串可能仍包含用户提供的转换说明符，供 `syslog` 后续插值。

始终使用正确的安全写法：

```c
syslog(priority, "%s", string);
```
