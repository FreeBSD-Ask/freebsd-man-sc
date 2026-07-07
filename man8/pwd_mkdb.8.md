# pwd_mkdb(8)

`pwd_mkdb` — 生成密码数据库

## 名称

`pwd_mkdb`

## 概要

`pwd_mkdb [-CiNp] [-d directory] [-s cachesize] [-u username] file`

## 描述

`pwd_mkdb` 工具为指定文件创建 db(3) 风格的安全和不安全数据库。然后将这些数据库分别安装到 **/etc/spwd.db** 和 **/etc/pwd.db**。该文件安装到 **/etc/master.passwd**。文件必须采用正确的格式（参见 [passwd(5)](../man5/passwd.5.md)）。重要的是要注意，本系统中使用的格式与历史上的 Version 7 风格格式不同。

选项如下：

**`-C`** 检查密码文件是否采用正确的格式。不更改、添加或删除任何文件。

**`-d`** `directory` 将数据库存储到指定的目标目录而不是 **/etc**。

**`-i`** 忽略 `master.passwd` 文件的锁定失败。此选项旨在用于在 NFS 上的发布过程中构建密码文件，那里不会发生争用。还必须使用 `-d` 选项指定非默认目录才能忽略锁定。强烈不鼓励以其他方式使用此选项。

**`-N`** 告诉 `pwd_mkdb` 如果无法获得文件锁则以错误退出。默认情况下，我们阻塞等待源文件上的锁。在重建数据库期间保持锁定。

**`-p`** 创建 Version 7 风格的密码文件并安装到 **/etc/passwd**。

**`-s`** `cachesize` 以兆字节为单位指定哈希库使用的内存缓存大小。在用户基数大的系统上，缓存大小过小可能导致数据库文件重建时间长得令人望而却步。粗略指导，`pwd_mkdb` 的内存使用量（以兆字节为单位）将略多于此处指定数字的两倍。默认为 2 兆字节。

**`-u`** `username` 仅更新指定用户的记录。对单个用户进行操作的工具可以使用此选项来避免重建整个数据库的开销。

这两个数据库的不同之处在于，安全版本包含用户的加密密码，而不安全版本包含星号（“\*”）。

这些数据库由 C 库密码例程使用（参见 [getpwent(3)](../gen/getpwent.3.md)）。

`pwd_mkdb` 工具成功时退出零，失败时退出非零。

## 环境变量

如果设置了 `PW_SCAN_BIG_IDS` 环境变量，`pwd_mkdb` 将抑制通常为大型用户和组 ID 生成的警告消息。此类 ID 可能对假设 ID 值的软件造成严重问题。

## 文件

**`/etc/pwd.db`** 不安全密码数据库文件。  
**`/etc/pwd.db.tmp`** 临时文件。  
**`/etc/spwd.db`** 安全密码数据库文件。  
**`/etc/spwd.db.tmp`** 临时文件。  
**`/etc/master.passwd`** 当前密码文件。  
**`/etc/passwd`** Version 7 格式密码文件。

## 实例

手动编辑或替换密码文件后重新生成密码数据库：

```sh
/usr/sbin/pwd_mkdb -p /etc/master.passwd
```

## 兼容性

以前版本的系统有一个类似于 `pwd_mkdb` 的程序 mkpasswd，它为密码文件构建 [dbm(3)](../db/dbm.3.md) 风格的数据库，但依赖于调用程序来安装它们。该程序被重命名，以便该程序以前的用户不会因功能更改而感到意外。

## 参见

chpass(1), [passwd(1)](../man1/passwd.1.md), db(3), [getpwent(3)](../gen/getpwent.3.md), [passwd(5)](../man5/passwd.5.md), [vipw(8)](vipw.8.md)

## 缺陷

由于密码文件需要原子更新，`pwd_mkdb` 使用 [rename(2)](../sys/rename.2.md) 来安装它们。然而，这要求命令行上指定的文件与 **/etc** 目录位于同一文件系统上。

多人同时在不同密码文件上运行 `pwd_mkdb` 存在明显的竞争。`pwd_mkdb` 的前端 chpass(1)、[passwd(1)](../man1/passwd.1.md) 和 [vipw(8)](vipw.8.md) 处理避免此问题所需的锁定。
