# nsmb.conf(5)

`nsmb.conf` — 服务器消息块（SMB1/CIFS）请求的配置文件

## 名称

`nsmb.conf`

## 描述

`nsmb.conf` 文件包含有关 SMB 网络协议的计算机、用户、共享或挂载点的信息。

配置文件按以下顺序加载：

- `~/.nsmbrc`
- **/etc/nsmb.conf**

因此，**/etc/nsmb.conf** 中的设置会覆盖 `~/.nsmbrc` 中的设置。

配置层次结构由若干节组成，每节包含若干行参数及其赋值。每个节必须以方括号括起的节名开始，类似于：

> [`section_name`]

每节的结束由新节的开始或文件的突然结束（通常称为 EOF）标记。每节可以包含零个或多个参数，例如：

> [`section_name`]

> `key`=`value`

其中 `key` 表示参数名，`value` 是该参数的赋值。

SMB 库使用以下信息作为节名：

**`A)`** [`default`]

**`B)`** [`SERVER`]

**`C)`** [`SERVER`:`USER`]

**`D)`** [`SERVER`:`USER`:`SHARE`]

可能的关键字包括：

| Keyword | Section | Comment |
| --- | --- | --- |
| `addr` | A B C D | 服务器的 IP 地址或主机名 |
| `charsets` | A B C D | 字符集设置，例如 koi8-r:cp866 |
| `nbns` | A B C D | NetBIOS 名称服务器地址 |
| `nbscope` | A B C D | NetBIOS 作用域 |
| `nbtimeout` | A B C D | NetBIOS 超时（秒） |
| `password` | B C D | 用于认证的密码 |
| `retry_count` | A B C D | 重试次数 |
| `timeout` | A B C D | 超时（秒） |
| `workgroup` | A B C D | 工作组或域的名称 |

## 文件

**/etc/nsmb.conf** 默认的远程挂载点配置文件。

**~/.nsmbrc** 用户特定的远程挂载点配置文件。

## 实例

以下是一个示例配置文件，可能与你的环境相符，也可能不相符：

```sh
# example.com 的配置文件
[default]
workgroup=SALES
# “FSERVER”是一台 NT 服务器。
[FSERVER]
charsets=koi8-r:cp866
addr=fserv.example.com
# FSERVER 的用户特定数据
[FSERVER:MYUSER]
password=$$16144562c293a0314e6e1
```

所有以 `#` 字符开头的行均为注释，不会被解析。“`default`” 节描述默认的工作组或域，本例中为 “`SALES`”。此处展示的下一个节 “`FSERVER`” 定义了一个服务器节，并为其分配字符集，该设置仅在不使用西里尔字符时需要。主机名值 “`fserv.example.com`” 也在该节中分配。“`FSERVER:USER`” 定义用户设置，可用于保存特定连接所使用的密码。密码可以是明文，也可以通过简单的加密进行混淆。简单加密的密码以 `$$1` 符号开头。警告：该加密函数非常脆弱，仅用于隐藏明文密码。如果希望使用简单加密，可以对密码使用以下命令：

```sh
smbutil crypt
```

## 参见

smbutil(1), mount_smbfs(8)

## 作者

本手册页由 Sergey Osokin <osa@FreeBSD.org> 和 Tom Rhodes <trhodes@FreeBSD.org> 编写。
