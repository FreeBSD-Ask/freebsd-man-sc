# libxo(3)

`libxo` — 用于生成文本、XML、JSON 或 HTML 输出的库

## 名称

`libxo`

## 库

Lb libxo

## 概要

`#include <libxo/xo.h>`

## 描述

`libxo` 中定义的函数用于生成 *TEXT*、*XML*、*JSON* 或 *HTML* 输出。这些函数使用一组通用的调用，通过传递给库的命令行开关来控制输出的细节。

大多数命令输出面向人类的文本。这种输出旨在让用户解析和理解。人类善于提取细节和模式匹配。程序员经常需要从这种面向人类的输出中提取信息。程序员使用 [grep(1)](../man1/grep.1.md)、[awk(1)](../man1/awk.1.md) 和正则表达式等工具来挖掘所需的信息片段。这种解决方案脆弱，当输出内容变化或演进时需要更新，且需要测试和验证。

现代工具开发者偏爱 XML 和 JSON 等编码方案，它们允许轻松解析和提取数据。这些格式简单、易于理解、层次化、易于解析，且通常更容易与常用工具和环境集成。

此外，现代的现实意味着更多的输出最终会出现在 Web 浏览器中而非终端中，使 HTML 输出具有价值。

`libxo` 允许源代码中的一组函数调用生成传统文本输出，以及 XML 和 JSON 格式的数据。也可以生成 HTML；`<div>` 元素围绕传统文本输出，带有详细说明如何渲染数据的属性。

`libxo` 支持四种编码样式：

- TEXT 输出可在终端会话中显示，允许与传统命令行用法兼容。
- XML 输出适用于 XPath 等工具和 NETCONF 等协议。
- JSON 输出可用于 RESTful API 以及与 Javascript 和 Python 等语言的集成。
- HTML 可与一个小型 CSS 文件匹配，以允许在任何 HTML5 浏览器中渲染。

通常，XML 和 JSON 适用于编码数据，而 TEXT 适用于终端输出，HTML 适用于在 Web 浏览器中显示（参见 xohtml(1)）。

`libxo` 使用命令行选项触发渲染行为。识别以下选项：

** --libxo <options>

** --libxo=<options>

** --libxo:<brief-options>

options 是一个以逗号分隔的标记列表，对应于输出样式、标志或功能：

**标记** **操作**

**`dtrt`** 启用“Do The Right Thing”模式

**`html`** 输出 HTML

**`indent=xx`** 设置缩进级别

**`info`** 添加 info 属性（HTML）

**`json`** 输出 JSON

**`keys`** 为键输出 key 属性（XML）

**`log-gettext`** 记录（通过 stderr）每次 gettext(3) 字符串查找

**`log-syslog`** 记录（通过 stderr）每条 syslog 消息（通过 xo_syslog(3)）

**`no-humanize`** 忽略 {h:} 修饰符（TEXT、HTML）

**`no-locale`** 不初始化区域设置

**`no-retain`** 防止保留格式信息

**`no-top`** 不输出顶层花括号（JSON）

**`not-first`** 假装第一个输出项不是第一个（JSON）

**`pretty`** 输出美化打印的输出

**`retain`** 强制保留格式信息

**`text`** 输出 TEXT

**`underscores`** 将 XML 友好的“-”替换为 JSON 友好的“_”

**`units`** 添加 'units'（XML）或 'data-units'（HTML）属性

**`warn`** 当 libxo 检测到错误调用时发出警告

**`warn-xml`** 以 XML 形式发出警告

**`xml`** 输出 XML

**`xpath`** 添加 XPath 表达式（HTML）

“brief-options”是单字母命令，为那些缺乏耐心使用真正标记的人设计。不使用逗号分隔符。

| **标记** | **操作** |
| --- |
| H | 启用 HTML 输出 (XO_STYLE_HTML) |
| I | 启用 info 输出 (XOF_INFO) |
| i<num> | 缩进 <number> |
| J | 启用 JSON 输出 (XO_STYLE_JSON) |
| P | 启用美化打印输出 (XOF_PRETTY) |
| T | 启用文本输出 (XO_STYLE_TEXT) |
| W | 启用警告 (XOF_WARN) |
| X | 启用 XML 输出 (XO_STYLE_XML) |
| x | 启用 XPath 数据 (XOF_XPATH) |

有关更多选项信息，请参阅 [xo_options(7)](../man7/xo_options.7.md)。

`libxo` 库允许应用程序使用一组通用的函数调用生成文本、XML、JSON 和 HTML 输出。应用程序在运行时决定应生成哪种输出样式。应用程序调用 xo_emit(3) 函数来生成由格式字符串描述的输出。“字段描述符”告诉 `libxo` 该字段是什么以及它的含义。每个字段描述符放在花括号中，带有类似 printf 的格式字符串：

```sh
    xo_emit(" {:lines/%7ju} {:words/%7ju} "
            "{:characters/%7ju}{d:filename/%s}n",
            linect, wordct, charct, file);
```

每个字段可以有一个角色，默认为 'value' 角色，该角色告诉 `libxo` 如何以及何时渲染该字段，还有一个类似 [printf(3)](printf.3.md) 的格式字符串。

然后可以使用“--libxo”选项以各种样式生成输出。

## 默认句柄

句柄为 `libxo` 提供了一种抽象，封装了输出流的状态。句柄的数据类型为“xo_handle_t”，对调用者不透明。

该库有一个自动初始化的默认句柄。默认情况下，此句柄将文本样式输出发送到标准输出。可以使用 xo_set_style(3) 和 xo_set_flags(3) 函数更改此行为。

许多 `libxo` 函数将句柄作为第一个参数；大多数不使用句柄的函数使用默认句柄。任何接受句柄的函数都可以传入 `NULL` 来访问默认句柄。

对于在标准输出上生成输出的典型命令，无需创建显式句柄，但在需要时可用，例如对于生成多个输出流的守护进程。

## 函数概览

`libxo` 库包含以下函数：

**函数** **描述**

`xo_attr`

`xo_attr_h`

`xo_attr_hv` 允许调用者将 XML 属性与下一个打开的元素一起输出。

`xo_create`

`xo_create_to_file` 允许调用者创建新句柄。注意 `libxo` 有一个默认句柄，允许调用者避免使用显式创建的句柄。只有写入 `stdout` 以外的文件的调用者才需要调用 `xo_create`。

`xo_destroy` 释放与句柄关联的所有资源，包括句柄本身。

`xo_emit`

`xo_emit_h`

`xo_emit_hv` 输出格式化的内容。`fmt` 字符串控制将其余参数转换为格式化输出。详见 xo_format(5)。

`xo_emit_warn`

`xo_emit_warnx`

`xo_emit_warn_c`

`xo_emit_warn_hc`

`xo_emit_err`

`xo_emit_errc`

`xo_emit_errx` 这些函数与其标准 libc 同名函数基本兼容，但使用 xo_format(5) 中定义的格式字符串。虽然转换字符串的成本增加，但所提供的输出可以更丰富且更有用。另见 xo_err(3)

`xo_warn`

`xo_warnx`

`xo_warn_c`

`xo_warn_hc`

`xo_err`

`xo_errc`

`xo_errx`

`xo_message`

`xo_message_c`

`xo_message_hc`

`xo_message_hcv` 这些函数旨在与其标准 libc 同名函数兼容。

`xo_finish`

`xo_finish_h` 刷新输出、关闭打开的构造并完成任何挂起的操作。

`xo_flush`

`xo_flush_h` 允许调用者刷新句柄的任何挂起输出。

`xo_no_setlocale` 指示 `libxo` 避免初始化区域设置。此函数应在调用任何其他 `libxo` 函数之前调用。

`xo_open_container`

`xo_open_container_h`

`xo_open_container_hd`

`xo_open_container_d`

`xo_close_container`

`xo_close_container_h`

`xo_close_container_hd`

`xo_close_container_d` 容器是层次结构的单例级别，通常用于组织相关内容。

`xo_open_list_h`

`xo_open_list`

`xo_open_list_hd`

`xo_open_list_d`

`xo_open_instance_h`

`xo_open_instance`

`xo_open_instance_hd`

`xo_open_instance_d`

`xo_close_instance_h`

`xo_close_instance`

`xo_close_instance_hd`

`xo_close_instance_d`

`xo_close_list_h`

`xo_close_list`

`xo_close_list_hd`

`xo_close_list_d` 列表是层次结构的级别，可在同一父级中出现多次。需要两次调用来封装它们，一次用于列表，一次用于列表的每个实例。通常 `xo_open_list` 和 `xo_close_list` 在 for 循环外部调用，而 `xo_open_instance` 在循环顶部调用，`xo_close_instance` 在循环底部调用。

`xo_parse_args` 检查命令行参数以获取对 `libxo` 的指示。此函数应在应用程序检查 `argv` 之前调用。

`xo_set_allocator` 指示 `libxo` 使用替代的内存分配器和释放器。

`xo_set_flags`

`xo_clear_flags` 更改句柄的标志设置。

`xo_set_info` 提供有关元素的附加信息，用于 HTML 渲染。

`xo_set_options` 更改句柄使用的格式化选项。

`xo_set_style`

`xo_set_style_name` 更改句柄使用的输出样式。

`xo_set_writer` 指示 `libxo` 使用一组替代的低级输出函数。

## 参见

libxo-csv(7), xo(1), xolint(1), xo_attr(3), xo_create(3), xo_emit(3), xo_emit_err(3), xo_err(3), xo_finish(3), xo_flush(3), xo_no_setlocale(3), xo_open_container(3), xo_open_list(3), xo_options(7), xo_parse_args(3), xo_set_allocator(3), xo_set_flags(3), xo_set_info(3), xo_set_options(3), xo_set_style(3), xo_set_writer(3), xo_format(5)

## 历史

`libxo` 库首次出现在 FreeBSD 11.0 中。

## 作者

`libxo` 由 Phil Shafer <phil@freebsd.org> 编写。
