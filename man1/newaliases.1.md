# newaliases.1

`newaliases` — 重建 sendmail 别名文件的数据

## 名称

`newaliases`

## 概要

`newaliases`

## 描述

`newaliases` 重建邮件别名文件 **/etc/mail/aliases** 的随机访问数据库。每次修改该文件后都必须运行此命令，更改才能生效。

`newaliases` 等同于 `sendmail -bi`。

`newaliases` 实用程序成功时退出值为 0，发生错误时大于 0。

注意：**不要**使用 `makemap` 创建别名数据库，因为 `newaliases` 会在数据库中放入 `sendmail` 所需的特殊标记。

## 文件

**/etc/mail/aliases** 邮件别名文件

## 参见

aliases(5), sendmail(8)

## 历史

`newaliases` 命令出现于 4.0BSD。
