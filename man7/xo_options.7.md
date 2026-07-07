# xo_options(7)

`xo_options` — 基于 libxo 的命令的通用选项

## 名称

`xo_options`

## 描述

`libxo` 允许将数据渲染为多种输出样式，包括 *text、* *XML、* *JSON* 和 *HTML。* `libxo` 使用命令行选项来触发渲染行为。选项有以下三种形式：

- --libxo <options>
- --libxo=<options>
- --libxo:<brief-options>

前两种形式接受以逗号分隔的单词集合（详见下文），第三种形式接受一组字母（同样详见下文）。它们触发的功能完全相同。

| **选项操作** |
| --- |
| color 为显示样式（TEXT、HTML）启用颜色/效果 |
| flush 在每次 emit 调用之后刷新 |
| flush-line 逐行刷新输出 |
| html 输出 HTML |
| indent=xx 设置缩进级别 |
| info 添加 info 属性（HTML） |
| json 输出 JSON |
| keys 为键输出 key 属性（XML） |
| log-gettext 记录（通过 stderr）每次 gettext(3) 字符串查找 |
| log-syslog 记录（通过 stderr）每条 syslog 消息（通过 xo_syslog） |
| no-humanize 忽略 {h:} 修饰符（TEXT、HTML） |
| no-locale 不初始化 locale 设置 |
| no-retain 阻止保留格式化信息 |
| pretty 输出经过美化打印的输出 |
| retain 强制保留格式化信息 |
| text 输出 TEXT |
| underscores 将 XML 友好的“-”替换为 JSON 友好的“_” |
| units 添加 'units'（XML）或 'data-units'（HTML）属性 |
| warn 当 libxo 检测到错误调用时发出警告 |
| warn-xml 以 XML 形式发出警告 |
| xml 输出 XML |
| xpath 添加 XPath 表达式（HTML） |

简写选项是一组单字母别名，用于替代较长的术语，作为一个单独的字符串使用：

| **值 等价标记** |
| --- |
| c color |
| f flush |
| F flush-line |
| H html |
| I info |
| i<num> indent=<num> |
| J json |
| k keys |
| n no-humanize |
| P pretty |
| T text |
| U units |
| u underscores |
| W warn |
| X xml |
| x xpath |

这些选项大多简单直接，但有些需要额外说明：

`flush-line` 执行行缓冲，即使输出未定向到 TTY 设备也是如此。

`info` 为 HTML 生成附加数据，以属性形式编码，属性名以“data-”开头。

`keys` 为 XML 输出添加“key”属性，以指示某个叶节点是列表成员的标识符。

`no-humanize` 避免对数字输出进行“人性化”处理（详见 humanize_number(3)）。

`no-locale` 指示 `libxo` 不要将输出转换为当前 locale。

`no-retain` 禁用 `libxo` 内部保留有关格式化字符串的“已编译”信息的能力。

`underscores` 可与 *JSON* 输出配合使用，将带有连字符的 *XML 友好*名称更改为带有下划线的 *JSON 友好*名称。

`warn` 允许 `libxo` 在应用程序代码进行错误调用时通过 stderr 发出警告。`warn-xml` 使这些警告以 *XML* 形式置于输出中。

## 实例

以下是对 [ps(1)](../man1/ps.1.md) 的三个调用示例：

```sh
      ps --libxo json,pretty,warn -ux
      ps --libxo=xml -lg
      ps --libxo:Hxc 1
```

## 参见

[libxo(3)](../man3/libxo.3.md), xo_format(5)

## 历史

`libxo` 库首次出现于 FreeBSD 11.0。

## 作者

`libxo` 由 Phil Shafer <phil@freebsd.org> 编写。
