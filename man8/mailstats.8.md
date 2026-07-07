# mailstats(8)

`mailstats` — 显示邮件统计信息

## 名称

`mailstats`

## 概要

`mailstats` [`-c`] [`-o`] [`-p`] [`-P`] [`-C` *cffile*] [`-f` *stfile*]

## 描述

`mailstats` 工具显示当前的邮件统计信息。

首先，显示开始保留统计信息的时间，格式由 ctime(3) 指定。然后，每个 mailer 的统计信息显示在一行上，每个统计信息由以下空白分隔的字段组成：

**`M`** mailer 编号。

**`msgsfr`** 来自该 mailer 的消息数。

**`bytes_from`** 来自该 mailer 的千字节数。

**`msgsto`** 发送到该 mailer 的消息数。

**`bytes_to`** 发送到该 mailer 的千字节数。

**`msgsrej`** 被拒绝的消息数。

**`msgsdis`** 被丢弃的消息数。

**`msgsqur`** 被隔离的消息数。

**`Mailer`** mailer 的名称。

在此显示之后，显示一行所有 mailer 值的总计（以“T”开头），通过一行仅包含等号（“=”）字符的行与前面的信息分隔开。另一行以“C”开头列出 TCP 连接数。

选项如下：

**`-C`** 读取指定文件而不是默认的 `sendmail` 配置文件。

**`-c`** 尝试使用 submit.cf 而不是默认的 `sendmail` 配置文件。

**`-f`** 读取指定的统计文件而不是 `sendmail` 配置文件中指定的统计文件。

**`-P`** 以程序可读模式输出信息，不清除统计信息。

**`-p`** 以程序可读模式输出信息，并清除统计信息。

**`-o`** 不在输出中显示 mailer 的名称。

`mailstats` 工具成功时退出值为 0，发生错误时退出值大于 0。

## 文件

**`/etc/mail/sendmail.cf`** 默认的 `sendmail` 配置文件。

**`/etc/mail/statistics`** 默认的 `sendmail` 统计文件。

## 参见

mailq(1), sendmail(8)
