  MANPATH(1)  

MANPATH(1)

FreeBSD General Commands Manual

MANPATH(1)

[名称](#__u540D___u79F0_)
=======================

`manpath` —

显示手册页的搜索路径

[概要](#__u6982___u8981_)
=======================

`manpath` \[`-Ldq`\]

[描述](#__u63CF___u8FF0_)
=======================

`manpath` 实用程序根据用户的 `PATH` 和本地配置文件确定用户的手动搜索路径。 此结果回显到标准输出。

[`-L`](#L)

输出手动语言环境列表而不是手动路径。

[`-d`](#d)

打印额外的调试信息。

[`-q`](#q)

禁止警告消息。

[实现说明](#__u5B9E___u73B0___u8BF4___u660E_)
=========================================

`manpath`-
实用程序从两个来源构建手动路径：

1.  从用户的 `PATH` 的每个组件中获取第一个：
    *   pathname/man
    *   pathname/MAN
    *   如果路径名以 /bin 结尾: pathname/../share/man 和 pathname/../man
2.  MANPATH 条目的 [FILES](#FILES) 部分中列出的配置文件。

然后将来自这些位置的信息连接在一起。

如果设置了 `-L` 标志， `manpath` 实用程序将在 [FILES](#FILES) 部分列出的配置文件中搜索 MANLOCALE 条目。

[环境](#__u73AF___u5883_)
=======================

以下环境变量会影响 `manpath` 的执行：

[`MANLOCALES`](#MANLOCALES)

如果使用 `-L` 标志设置，则使实用程序显示警告和值，覆盖系统上找到的任何其他配置。

[`MANPATH`](#MANPATH)

如果设置，将导致实用程序显示警告和值，覆盖系统上找到的任何其他配置。

[`PATH`](#PATH)

影响手动路径，如 [实现说明](#__u5B9E___u73B0___u8BF4___u660E_) 中所述。

[文件](#__u6587___u4EF6_)
=======================

/etc/man.conf

系统配置文件。

/usr/local/etc/man.d/\*.conf

本地配置文件。

[参见](#__u53C2___u89C1_)
=======================

apropos(1), man(1), whatis(1), man.conf(5)

March 11, 2017

FreeBSD 13.1-RELEASE