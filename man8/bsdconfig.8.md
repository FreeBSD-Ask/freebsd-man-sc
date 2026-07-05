# bsdconfig.8

`bsdconfig` — 系统配置工具

## 名称

`bsdconfig`

## 概要

`bsdconfig [-h]`

`bsdconfig command [-h]`

`bsdconfig [OPTIONS] [command [OPTIONS]]`

## 描述

`bsdconfig` 用于设置许多系统配置项，既可用于新系统的初始设置，也可用于更改现有系统的配置。

`bsdconfig` 可选地接受一个命令作为参数。若不带参数调用，将弹出一个交互式菜单列出可用模块。

可用选项如下：

**`-d`** 运行时在标准输出提供大量调试信息。

**`-D`** `file` 将调试信息发送到 `file`。如果 `file` 以加号开头，调试信息将同时发送到标准输出和文件（去掉开头的加号）。

**`-f`** `file` 加载 `file` 作为脚本然后退出。若多次出现，程序将在最后一次出现后才退出。如果 `file` 是单个短横线（‘`-`’），`bsdconfig` 从标准输入读取。

**`-h`** 打印用法说明并退出。

**`-S`** 安全 X11 模式（隐含 `-X`）。以 root 身份时，在启动前始终提示并验证 sudo(8)（`ports/security/sudo`）的用户名/密码。

**`-X`** 使用 Xdialog(1)（`ports/x11/xdialog`）替代 [dialog(1)](../man1/dialog.1.md)。

## 命令

以下命令（按字母顺序排列）目前包含在基础 `bsdconfig` 程序中，后续将添加更多。其他命令可按需添加，详见下文 “添加命令” 章节的说明；添加后将出现在主菜单以及 `-h` 列表中。

**`console`** 用于自定义系统控制台行为的工具。

**`defaultrouter`** 进入 networking 下的默认路由器/网关菜单的快捷方式。

**`diskmgmt`** 管理磁盘分区和/或标签。执行 sade(8)。

**`docsinstall`** 执行 `bsdinstall docsinstall` 子工具，用于安装/重新安装 FreeBSD 文档集。

**`dot`** 生成 graphviz dot(1)（`ports/graphics/graphviz`）语言文件（输出到 stdout），可视化展示 `bsdconfig` 菜单、包含和快捷方式的结构关系。详见 “bsdconfig dot -h”。

**`groupadd`** 进入 groupmgmt 下添加组菜单的快捷方式。

**`groupdel`** 进入 groupmgmt 下删除组菜单的快捷方式。

**`groupedit`** 进入 groupmgmt 下编辑/查看组菜单的快捷方式。

**`groupmgmt`** 用于添加/更改/查看/删除组账户的工具。

**`hostname`** 进入 networking 下主机名/域名菜单的快捷方式。

**`kern_securelevel`** 进入 security 下 kern.securelevel 菜单的快捷方式。

**`mouse`** 用于配置、查看和启用控制台鼠标支持的工具。

**`mouse_disable`** 进入 mouse 下禁用菜单的快捷方式。

**`mouse_enable`** 进入 mouse 下启用菜单的快捷方式。

**`mouse_flags`** 进入 mouse 下标志菜单的快捷方式。

**`mouse_port`** 进入 mouse 下端口菜单的快捷方式。

**`mouse_type`** 进入 mouse 下类型菜单的快捷方式。

**`nameservers`** 进入 networking 下 DNS 名称服务器菜单的快捷方式。

**`netdev`** 进入 networking 下网络接口菜单的快捷方式。

**`networking`** 用于设置/更改主机名/域名、网络接口、无线网络、默认路由器/网关和 DNS 名称服务器的工具。

**`packages`** 浏览、安装、卸载或重新安装打包软件。

**`password`** 设置系统管理员（root）密码。

**`security`** 配置各种系统安全设置。

**`startup`** 配置系统启动的各个方面。

**`startup_misc`** 进入 startup 下杂项启动服务菜单的快捷方式。

**`startup_rcadd`** 进入 startup 下查看/编辑启动配置菜单（startup_rcconf）中的添加新条目菜单的快捷方式。

**`startup_rcconf`** 进入 startup 下查看/编辑启动配置菜单的快捷方式。

**`startup_rcdelete`** 进入 startup 下查看/编辑启动配置菜单（startup_rcconf）中的删除菜单的快捷方式。

**`startup_rcvar`** 进入 startup 下切换启动服务菜单的快捷方式。

**`syscons_font`** 进入 [syscons(4)](../man4/syscons.4.md) 控制台下字体菜单的快捷方式。

**`syscons_keymap`** 进入 [syscons(4)](../man4/syscons.4.md) 控制台下键盘映射菜单的快捷方式。

**`syscons_repeat`** 进入 [syscons(4)](../man4/syscons.4.md) 控制台下重复率菜单的快捷方式。

**`syscons_saver`** 进入 [syscons(4)](../man4/syscons.4.md) 控制台下屏幕保护程序菜单的快捷方式。

**`syscons_screenmap`** 进入 [syscons(4)](../man4/syscons.4.md) 控制台下屏幕映射菜单的快捷方式。

**`syscons_ttys`** 进入 [syscons(4)](../man4/syscons.4.md) 控制台下 Ttys 菜单的快捷方式。

**`vt_font`** 进入 [vt(4)](../man4/vt.4.md) 控制台下字体菜单的快捷方式。

**`vt_keymap`** 进入 [vt(4)](../man4/vt.4.md) 控制台下键盘映射菜单的快捷方式。

**`vt_repeat`** 进入 [vt(4)](../man4/vt.4.md) 控制台下重复率菜单的快捷方式。

**`vt_saver`** 进入 [vt(4)](../man4/vt.4.md) 控制台下屏幕保护程序菜单的快捷方式。

**`vt_screenmap`** 进入 [vt(4)](../man4/vt.4.md) 控制台下屏幕映射菜单的快捷方式。

**`vt_ttys`** 进入 [vt(4)](../man4/vt.4.md) 控制台下 Ttys 菜单的快捷方式。

**`timezone`** 设置本机的区域时区。

**`ttys`** 使用你喜欢的编辑器编辑 ttys(5) 数据库。

**`useradd`** 进入 usermgmt 下添加用户菜单的快捷方式。

**`userdel`** 进入 usermgmt 下删除用户菜单的快捷方式。

**`useredit`** 进入 usermgmt 下编辑/查看用户菜单的快捷方式。

**`usermgmt`** 用于添加/编辑/查看/删除用户账户的工具。

**`wireless`** 进入 networking 下无线网络菜单的快捷方式。

## 国际化

i18n 功能内置于 `bsdconfig`，特定语言的翻译文件将在可用时添加。在没有特定语言翻译文件的情况下，将使用默认（en_US.ISO8859-1）文件。

## 添加命令

将在稍后补充文档。文档将说明 INDEX 文件中的 menu_selection="command|*" 语法。

## 环境变量

以下环境变量影响 `bsdconfig` 的执行：

**`LANG`** 若设置了 LANG，则消息和索引信息将从名为 messages.$LANG 和 INDEX.$LANG 的文件读取；如果这些文件不存在，则回退到名为 messages 和 INDEX 的文件。LANG 优先于 LC_ALL。

**`LC_ALL`** 若设置了 LC_ALL，则消息和索引信息将从名为 messages.$LC_ALL 和 INDEX.$LC_ALL 的文件读取；如果这些文件不存在，则回退到名为 messages 和 INDEX 的文件。

## 文件

/usr/share/examples/bsdconfig/bsdconfigrc 可复制到 $HOME/.bsdconfigrc 并按需自定义。

## 退出状态

`bsdconfig` 工具成功时退出状态为 0，发生错误时大于 0。

## 参见

bsdinstall(8)

## 历史

`bsdconfig` 首次出现于 FreeBSD 9.2。

## 作者

Ron McDowell

Devin Teske <dteske@FreeBSD.org>

## 缺陷

docsinstall 和 diskmgmt 模块会调用 bsdinstall。在这些模块中发现的 bug 应视为 bsdinstall 的 bug，而非 `bsdconfig` 的。
