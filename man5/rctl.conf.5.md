# rctl.conf.5

`rctl.conf` — 资源限制数据库默认值

## 名称

`rctl.conf`

## 描述

**/etc/rctl.conf** 文件在系统进入多用户模式时被读取，用于设置 RCTL 数据库的默认内容。**/etc/rctl.conf** 采用 rctl(8) 命令的格式，即

```sh
subject:subject-id:resource:action=amount/per
```

以 “#” 开头的行表示注释。注释也可以出现在行尾，如下文实例部分所示。

## 文件

**/etc/rctl.conf** — rctl(8) 的初始设置。

## 实例

要限制登录类 “testing” 中用户的进程数量，可以使用如下规则：

```sh
# "testing" 类的资源限制
loginclass:testing:maxproc:deny=100/user # 每个用户最多 100 个进程
```

## 参见

rctl(8)

## 历史

`rctl.conf` 文件出现于 FreeBSD 9.0。
