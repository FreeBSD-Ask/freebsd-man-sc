# manpath(1)

`manpath` — 显示手册页搜索路径

## 名称

`manpath`

## 概要

`manpath [-Ldq]`

## 描述

`manpath` 实用程序从用户的 `PATH` 和本地配置文件确定用户的手册搜索路径。结果输出到标准输出。

**`-L`** 输出手册区域列表而非手册路径。

**`-d`** 打印额外的调试信息。

**`-q`** 抑制警告消息。

## 实现说明

`manpath` 实用程序从两个来源构造手册路径：

1. 从用户 `PATH` 的每个组成部分中查找以下第一个匹配项：
   - **pathname/man**
   - **pathname/MAN**
   - 如果 pathname 以 /bin 结尾：**pathname/../share/man** 和 **pathname/../man**
2. “文件” 章节中列出的配置文件里的 `MANPATH` 条目。

然后将这些位置的信息连接在一起。

如果设置了 `-L` 标志，`manpath` 实用程序将搜索 “文件” 章节中列出的配置文件中的 `MANLOCALE` 条目。

## 环境变量

以下环境变量影响 `manpath` 的执行：

**`MANLOCALES`** 如果与 `-L` 标志一起设置，使实用程序显示警告和该值，覆盖系统上找到的任何其他配置。

**`MANPATH`** 如果设置，使实用程序显示警告和该值，覆盖系统上找到的任何其他配置。

**`PATH`** 按 “实现说明” 中所述影响手册路径。

## 文件

**/etc/man.conf** 系统配置文件。

**/usr/local/etc/man.d/\*.conf** 本地配置文件。

## 参见

[apropos(1)](apropos.1.md), [man(1)](man.1.md), [whatis(1)](whatis.1.md), man.conf(5)
