  PASSWORD.LUA(8)  

PASSWORD.LUA(8)

FreeBSD System Manager's Manual

PASSWORD.LUA(8)

[名称2](#__u540D___u79F0_2)
=========================

`password.lua` —

FreeBSD 密码模块

[描述](#__u63CF___u8FF0_)
=======================

`password.lua` 包含提示和检查密码的功能。

在使用 `password.lua` 提供的功能之前，必须将其包含在如下语句中：

`local password = require("password")`

从 `password.lua` 导出以下函数：

`password.read`(prompt\_length)

根据提示阅读密码。 prompt\_length 是必需的，以便在用户键入时可以正确绘制旋转。

`password.check`()

驱动加载程序完成的主密码检查。 `password.check`() 函数将检查 `bootlock_password`, `geom_eli_passphrase_prompt` 和 `password` ，并根据需要提示用户输入密码。 如果设置了 `password` ，自动引导序列将在提示用户输入密码时开始。

[参见](#__u53C2___u89C1_)
=======================

screen.lua(8)

[作者](#__u4F5C___u8005_)
=======================

`password.lua` 文件最初是由 Pedro Souza <[pedrosouza@FreeBSD.org](mailto:pedrosouza@FreeBSD.org)\> 编写的。 后来的工作和这个手册页是由 Kyle Evans <[kevans@FreeBSD.org](mailto:kevans@FreeBSD.org)\> 编写。

August 19, 2018

FreeBSD 13.1-RELEASE