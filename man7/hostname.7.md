# hostname(7)

`hostname` — 主机名解析描述

## 名称

`hostname`

## 描述

主机名就是域名，其中域名是一个分层的、以点分隔的子域列表；例如，在 Internet 的 EDU 子域下的 Berkeley 子域中的机器 monet 将表示为

```sh
monet.Berkeley.EDU
```

（不带尾随点）。

主机名常用于网络客户端和服务器程序，这些程序通常必须将名称转换为地址以供使用。（此功能通常由库例程 gethostbyname(3) 执行。）主机名由 Internet 名称解析器按以下方式进行解析。

如果名称由单个组件组成，即不包含点，并且如果环境变量“`HOSTALIASES`”设置为某个文件名，则会在该文件中搜索与输入主机名匹配的任何字符串。该文件应由成对的以空白分隔的字符串行组成，其中第一个字符串是主机名别名，第二个字符串是要替换该别名的完整主机名。如果在要解析的主机名与文件中某行的第一个字段之间找到不区分大小写的匹配，则查找替换后的名称，不再进行进一步处理。

如果输入名称以尾随点结尾，则去除尾随点，并查找剩余名称，不再进行进一步处理。

如果输入名称不以尾随点结尾，则通过搜索一系列域名直到找到匹配项来查找它。默认搜索列表首先包括本地域，然后是其至少包含 2 个名称组件的父域（最长的优先）。例如，在域 CS.Berkeley.EDU 中，名称 lithium.CChem 将首先作为 lithium.CChem.CS.Berkeley.EDU 检查，然后作为 lithium.CChem.Berkeley.EDU 检查。Lithium.CChem.EDU 不会被尝试，因为从本地域起只剩下一个组件。搜索路径可以通过系统范围配置文件从默认值更改（参见 [resolver(5)](../man5/resolver.5.md)）。

## 参见

gethostbyname(3), [resolver(5)](../man5/resolver.5.md)

## 历史

`Hostname` 出现于 4.2BSD。
