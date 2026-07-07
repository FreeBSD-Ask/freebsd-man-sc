# mail.local(8)

`mail.local` — 将邮件存储到邮箱中

## 名称

`mail.local`

## 概要

`mail.local` [`-7`] [`-B`] [`-b`] [`-d`] [`-D` *mbdb*] [`-l`] [`-s`] [`-f` *from*|`-r` *from*] [`-h` *filename*] *user ...*

## 描述

`mail.local` 读取标准输入直到文件结束，并将其追加到每个 *user* 的 `mail` 文件中。*user* 必须是有效的用户名。

选项如下：

**`-7`** 在 LMTP 模式下不宣告支持 8BITMIME。

**`-B`** 关闭通知 `biff` 服务的尝试。

**`-b`** 当邮箱超出配额时返回永久错误而不是临时错误。

**`-d`** 指定这是投递（为了向后兼容）。此选项无任何效果。

**`-D`** *mbdb* 指定用于查找本地收件人名称的邮箱数据库名称。此选项默认为“pw”，即使用 getpwnam()。

**`-f`** *from* 指定发件人名称。

**`-l`** 开启 LMTP 模式。

**`-s`** 关闭 fsync(2) 调用，该调用强制在返回“成功”状态之前将邮箱提交到磁盘。

**`-r`** *from* 指定发件人名称（为了向后兼容）。与 `-f` 相同。

**`-h`** *filename* 将传入的邮件存储在用户主目录中的 *filename* 中，而不是系统邮件 spool 目录中。

以下选项仅在 `mail.local` 编译时使用了 -DHASHSPOOL 的情况下可用：

**`-H`** *hashtypehashdepth* 选择哈希邮件目录。有效的哈希类型为 `u`（用户名）和 `m`（MD5，需要编译时使用 -DHASHSPOOLMD5）。示例：`-H u2` 选择用户名哈希，哈希深度为 2。注意：哈希类型和深度之间不能有空格。

**`-p`** *path* 指定替代的邮件 spool 路径。

**`-n`** 指定在 LMTP 模式下不应去除收件人地址的域部分。

邮箱中的各邮件由一个空行后跟以字符串“From ”开头的行分隔。每封投递的邮件前面会添加一行包含字符串“From ”、发件人名称和时间戳的行。每封邮件后追加一个空行。对于邮件中任何可能被误认为是“From ”分隔符的行（即空行后跟以五个字符“From ”开头的行），会在该行前加上大于号（“>”）。

追加邮件时，邮件文件会使用 flock(2) 进行独占锁定，并且在锁定邮箱时还会创建一个 `user.lock` 文件，以与较旧的 MUA 兼容。

如果 getservbyname(3) 返回了“biff”服务，则会通知 biff 服务器已投递的邮件。

`mail.local` 工具成功时退出值为 0，发生错误时退出值大于 0。

## 环境变量

**`TZ`** 用于在时间戳上设置适当的时区。

## 文件

**`/tmp/local.XXXXXX`** 临时文件

**`/var/mail/user`** 用户默认邮箱目录

**`/var/mail/user.lock`** 用户默认邮箱的锁定文件

## 参见

mail(1), flock(2), getservbyname(3), comsat(8), sendmail(8)

## 警告

`mail.local` 仅转义空行后面的“^From ”行。如果所有以“From ”开头的行都应被转义，请在 sendmail.cf 文件中为本地 mailer 使用“E”标志。

## 历史

`mail.local` 的超集（处理邮箱读取和邮件投递）作为程序 `mail` 出现在 Version 7 AT&T UNIX 中。
