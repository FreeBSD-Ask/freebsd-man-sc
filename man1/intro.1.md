# intro(1)

`intro` — 通用命令（工具与实用程序）简介

## 名称

`intro`

## 描述

手册第一节包含构成 FreeBSD 用户环境的大部分命令。系统中第一节收录的命令包括文本编辑器、命令 shell 解释器、搜索与排序工具、文件操作命令、系统状态命令、远程文件复制命令、邮件命令、编译器与编译工具、格式化输出工具以及行式打印机命令。

数以万计的附加命令可通过 [pkg(8)](../man8/pkg.8.md) 安装，或通过 ports(7) 集合编译获得。其中包括网页浏览器、办公套件、日历、会议工具、集成开发环境、媒体播放器、音频与视频处理套件等。

所有命令在退出时都会设置一个状态值，可用于检测命令是否正常完成。按照惯例，值 0 表示命令成功完成，而大于 0 的值表示出错。部分命令尝试使用 sysexits(3) 中定义的退出代码来描述失败的性质，其他命令则简单地将状态设置为大于 0 的任意值（通常为 1）。

## 文件

**`/bin/`** 单用户和多用户模式下都必不可少的基本命令。

**`/usr/bin/`** 基础系统附带的通用命令。

**`/usr/local/bin/`** 通过 [pkg(8)](../man8/pkg.8.md) 或 ports(7) 本地安装的命令。

## 参见

[apropos(1)](apropos.1.md), [man(1)](man.1.md), [which(1)](which.1.md), [intro(2)](../sys/intro.2.md), [intro(3)](../man3/intro.3.md), [sysexits(3)](../man3/sysexits.3.md), [intro(4)](../man4/intro.4.md), [intro(5)](../man5/intro.5.md), [intro(6)](../man6/intro.6.md), [intro(7)](../man7/intro.7.md), [ports(7)](../man7/ports.7.md), [security(7)](../man7/security.7.md), [intro(8)](../man8/intro.8.md), [pkg(8)](../man8/pkg.8.md), [intro(9)](../man9/intro.9.md)

《UNIX 用户手册补充文档》中的教程。

## 历史

`intro`(1) 手册页首次出现于 Version 6 AT&T UNIX。
