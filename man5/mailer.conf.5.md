# mailer.conf(5)

`mailer.conf` — mailwrapper(8) 的配置文件

## 名称

`mailer.conf` mailwrapper(8)

## 描述

文件 **/etc/mail/mailer.conf** 包含若干行，每行格式如下：

`name` `program` [`arguments ...`]

每行的第一个词是调用 mailwrapper(8) 的程序 `name`。（例如，在典型系统上 **/usr/sbin/sendmail** 会是指向 mailwrapper(8) 的符号链接，[newaliases(1)](../man1/newaliases.1.md) 和 mailq(1) 也会如此。因此，`name` 可能是 “`sendmail`” 或 “`newaliases`” 等。）

每行的第二个词是在第一个名称被调用时实际要执行的 `program` 的名称。

后续的 `arguments`（如果有）会传递给 `program`，后面跟着 mailwrapper(8) 被调用时所接收的参数。

该文件还可以包含注释行，以任何一行的第一列的 `#` 标记表示。

## 文件

**/etc/mail/mailer.conf**

## 实例

以下示例展示如何设置 `mailer.conf` 来调用传统的 sendmail(8) 程序：

```sh
# 执行位于
# /usr/libexec/sendmail/sendmail 的“真实”sendmail 程序
sendmail	/usr/libexec/sendmail/sendmail
mailq		/usr/libexec/sendmail/sendmail
newaliases	/usr/libexec/sendmail/sendmail
```

使用 `Postfix`（来自 ports）替换 sendmail(8)：

```sh
# 使用 postfix 模拟 sendmail
sendmail	/usr/local/sbin/sendmail
mailq		/usr/local/sbin/sendmail
newaliases	/usr/local/sbin/sendmail
```

使用 `Exim`（来自 ports）替换 sendmail(8)：

```sh
# 使用 exim 模拟 sendmail
sendmail	/usr/local/sbin/exim
mailq		/usr/local/sbin/exim -bp
newaliases	/usr/bin/true
rmail		/usr/local/sbin/exim -i -oee
```

使用 `mini_sendmail`（来自 ports）替换 sendmail(8)：

```sh
# 使用 mini_sendmail 将外发邮件发送到智能中继
sendmail	/usr/local/bin/mini_sendmail -srelayhost
```

使用 dma(8) 替换 sendmail(8)：

```sh
# 执行 dma 代替 sendmail
sendmail	/usr/libexec/dma
mailq		/usr/libexec/dma
newaliases	/usr/libexec/dma
rmail		/usr/libexec/dma
```

## 参见

mail(1), mailq(1), [newaliases(1)](../man1/newaliases.1.md), dma(8), mailwrapper(8), sendmail(8)

postfix(1)（`ports/mail/postfix`），dma(8)（`ports/mail/dma`），exim(8)（`ports/mail/exim`），mini_sendmail(8)（`ports/mail/mini_sendmail`）

## 历史

`mini_sendmail` 出现于 NetBSD 1.4。

## 作者

Perry E. Metzger <perry@piermont.com>

## 缺陷

这个程序存在的整个理由本身就是一种权宜之计。相反，应当标准化提交邮件的命令，并且 mailq(1) 等工具的“以不同名称调用就表现不同”的行为应当被取消。
