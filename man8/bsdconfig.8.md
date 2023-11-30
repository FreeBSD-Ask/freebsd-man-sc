  BSDCONFIG(8)  

BSDCONFIG(8)

FreeBSD System Manager's Manual

BSDCONFIG(8)

[名称](#__u540D___u79F0_)
=======================

`bsdconfig` —

系统配置实用程序

[概要](#__u6982___u8981_)
=======================

`bsdconfig` \[`-h`\] `bsdconfig` command \[`-h`\] `bsdconfig` \[OPTIONS\] \[command \[OPTIONS\]\]

[描述](#__u63CF___u8FF0_)
=======================

`bsdconfig` 用于设置许多系统配置设置，既适用于新系统，也适用于更改现有系统的配置设置。

`bsdconfig` 可以选择将命令作为参数。 如果不带参数调用，它将弹出一个列出可用模块的交互式菜单。

可以使用以下选项：

[`-d`](#d)

运行时提供大量关于标准输出的调试信息。

[`-D`](#D) file

将调试信息发送到文件。 如果文件以加号开头，则将调试信息发送到标准输出和文件（减去前导加号）。

[`-f`](#f) file

将 file 加载为脚本，然后退出。 如果多次出现，程序只会在最后一次出现后退出。 如果 file 是单个破折号 (‘`-`’), `bsdconfig` 从标准输入读取。

[`-h`](#h)

打印使用说明并退出。

[`-S`](#S)

安全 X11 模式 (意味着 `-X`) 。 以 root 身份，在开始之前始终提示并验证 sudo(8) 用户名/密码。

[`-X`](#X)

使用 Xdialog(1) 代替 dialog(1) 。

[命令](#__u547D___u4EE4_)
=======================

以下命令 (按字母顺序排列) 当前包含在基本 `bsdconfig` 程序中，不久将添加更多命令。 可以添加其他命令，如下面的 `ADDING COMMANDS` 部分所述，添加后，将出现在主菜单和 `-h` 列表中。

[`console`](#console)

用于自定义系统控制台行为的实用程序。

[`defaultrouter`](#defaultrouter)

网络下默认路由器/网关菜单的快捷方式。

[`diskmgmt`](#diskmgmt)

管理磁盘分区和/或标签。 执行 sade(8) 。

[`docsinstall`](#docsinstall)

执行 `bsdinstall docsinstall` 子实用程序以允许安装/重新安装 FreeBSD 文档集。

[`dot`](#dot)

生成一个可视化 `bsdconfig` 菜单、包含和快捷方式结构关系的 dot(1) 语言文件 (打印在标准输出上) ）。 有关详细信息，请参阅 “bsdconfig dot -h” 。

[`groupadd`](#groupadd)

groupmgmt 下添加组菜单的快捷方式。

[`groupdel`](#groupdel)

groupmgmt 下删除组菜单的快捷方式。

[`groupedit`](#groupedit)

groupmgmt 下编辑/查看组菜单的快捷方式。

[`groupmgmt`](#groupmgmt)

添加/更改/查看/删除组帐户的实用程序。

[`hostname`](#hostname)

网络下主机名/域菜单的快捷方式。

[`kern_securelevel`](#kern_securelevel)

安全性下 kern.securelevel 菜单的快捷方式。

[`mouse`](#mouse)

用于配置、探索和启用控制台鼠标支持的实用程序。

[`mouse_disable`](#mouse_disable)

鼠标下禁用菜单的快捷方式。

[`mouse_enable`](#mouse_enable)

鼠标下启用菜单的快捷方式。

[`mouse_flags`](#mouse_flags)

鼠标下标志菜单的快捷方式。

[`mouse_port`](#mouse_port)

鼠标下端口菜单的快捷方式。

[`mouse_type`](#mouse_type)

鼠标下类型菜单的快捷方式。

[`nameservers`](#nameservers)

网络下 DNS 名称服务器菜单的快捷方式。

[`netdev`](#netdev)

网络下网络接口菜单的快捷方式。

[`networking`](#networking)

用于设置/更改主机名/域、网络接口、无线网络、默认路由器/网关和 DNS 名称服务器的实用程序。

[`packages`](#packages)

浏览、安装、卸载或重新安装打包软件。

[`password`](#password)

设置系统管理员 (root) 密码。

[`security`](#security)

配置各种系统安全设置。

[`startup`](#startup)

配置系统启动的各个方面。

[`startup_misc`](#startup_misc)

启动下杂项启动服务菜单的快捷方式。

[`startup_rcadd`](#startup_rcadd)

启动的 View/Edit Startup Configuration 菜单 (startup\_rcconf) 下的 Add New 菜单的快捷方式。

[`startup_rcconf`](#startup_rcconf)

启动下查看/编辑启动配置菜单的快捷方式。

[`startup_rcdelete`](#startup_rcdelete)

启动的查看/编辑启动配置菜单（startup\_rcconf）下删除菜单的快捷方式。

[`startup_rcvar`](#startup_rcvar)

启动下切换启动服务菜单的快捷方式。

[`syscons_font`](#syscons_font)

控制台下字体菜单的快捷方式。

[`syscons_keymap`](#syscons_keymap)

控制台下 Keymap 菜单的快捷方式。

[`syscons_repeat`](#syscons_repeat)

控制台下重复菜单的快捷方式。

[`syscons_saver`](#syscons_saver)

控制台下的 Saver 菜单的快捷方式。

[`syscons_screenmap`](#syscons_screenmap)

控制台下 Screenmap 菜单的快捷方式。

[`syscons_ttys`](#syscons_ttys)

控制台下 Ttys 菜单的快捷方式。

[`timezone`](#timezone)

设置本地机器的区域时区。

[`ttys`](#ttys)

使用您喜欢的编辑器编辑 ttys(5) 数据库。

[`useradd`](#useradd)

usermgmt 下添加用户菜单的快捷方式。

[`userdel`](#userdel)

usermgmt 下删除用户菜单的快捷方式。

[`useredit`](#useredit)

usermgmt 下编辑/查看用户菜单的快捷方式。

[`usermgmt`](#usermgmt)

添加/编辑/查看/删除用户帐户的实用程序。

[`wireless`](#wireless)

网络下无线网络菜单的快捷方式。

[国际化](#__u56FD___u9645___u5316_)
================================

i18n 功能内置于 `bsdconfig` 中，并且特定语言的翻译文件将在可用时添加。 如果没有特定语言的翻译文件，将使用默认 (en\_US.ISO8859-1) 文件。

[添加命令](#__u6DFB___u52A0___u547D___u4EE4_)
=========================================

稍后记录。INDEX 文件的文档 menu\_selection="command|\*" 语法。

[环境变量](#__u73AF___u5883___u53D8___u91CF_)
=========================================

以下环境变量影响 `bsdconfig` 的执行：

[`LANG`](#LANG)

如果设置了 LANG，则将从名为 messages.$LANG 和 INDEX 的文件中读取消息和索引信息。 $LANG 并在 messages.$LANG 和 INDEX.$LANG 不存在时回退到名为 messages 和 INDEX 的文件。 LANG 优先于 LC\_ALL。

[`LC_ALL`](#LC_ALL)

如果设置了 LC\_ALL，则将从名为 messages.$LC\_ALL 和 INDEX 的文件中读取消息和索引信息。 $LC\_ALL 如果 messages.$LC\_ALL 和 INDEX.$LC\_ALL 不存在，则回退到名为 messages 和 INDEX 的文件。

[文件](#__u6587___u4EF6_)
=======================

/usr/share/examples/bsdconfig/bsdconfigrc 可以复制到 $HOME/.bsdconfigrc 并根据需要进行定制。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `bsdconfig` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

bsdinstall(8)

[历史](#__u5386___u53F2_)
=======================

`bsdconfig` 最早出现在 FreeBSD 9.2 中。

[作者](#__u4F5C___u8005_)
=======================

Ron McDowell Devin Teske <[dteske@FreeBSD.org](mailto:dteske@FreeBSD.org)\>

[缺陷](#__u7F3A___u9677_)
=======================

docsinstall 和 diskmgmt 模块调用 bsdinstall。 在这些模块中发现的错误应该被认为是 bsdinstall，而不是 `bsdconfig` 。

April 12, 2020

FreeBSD 13.1-RELEASE