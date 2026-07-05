# forward.5

`forward` — 邮件转发指令

## 名称

`forward`

## 描述

`.forward` 文件包含一系列邮件地址或程序，用户的邮件将被重定向到这些地址或程序。如果该文件不存在，则不进行邮件转发。通过在行首加上正常的 shell 管道符号（`|`），邮件也可以作为程序的标准输入转发。如果要向命令传递参数，则整行应用引号括起。出于安全原因，`.forward` 文件必须由邮件接收用户或 root 拥有，并且该用户的 shell 必须列在 **/etc/shells** 中。

例如，如果 `.forward` 文件包含以下行：

```sh
nobody@FreeBSD.org
"|/usr/bin/vacation nobody"
```

邮件将被转发到 <nobody@FreeBSD.org>，并以 `nobody` 作为单个参数传递给程序 **/usr/bin/vacation**。

如果本地用户地址以反斜杠字符为前缀，邮件将直接投递到该用户的邮件 spool 文件，跳过进一步的重定向。

例如，如果用户 chris 的 `.forward` 文件包含以下行：

```sh
chris@otherhost
echris
```

一份邮件副本将转发到 `chris@otherhost`，另一份副本将作为本地用户 chris 的邮件保留。

## 文件

**`$HOME/.forward`** 用户的转发指令。

## 参见

aliases(5), sendmail(8)
