# os-release(5)

`os-release` — 描述当前操作系统及其部分属性的文件

## 名称

`os-release`

## 描述

`os-release` 文件是一个以换行符分隔的键值对列表。该文件的语法是简化版的 [sh(1)](../man1/sh.1.md) 变量赋值，具有以下限制：

- 字符串不能连接在一起
- 不进行变量展开
- 所有 shell 特殊字符必须按照 [sh(1)](../man1/sh.1.md) 中的说明进行引用
- 如果变量赋值包含 A-Z、a-z 和 0-9 以外的字符，则必须包含在双引号内
- 所有字符串应采用 UTF-8 格式
- 字符串中不应使用不可打印字符

以字符 `#` 开头的行作为注释被忽略。

## 变量

以下变量由标准定义。

**`NAME`** 描述首选操作系统名称的字符串。

**`VERSION`** 操作系统的版本字符串，采用其通常的格式。

**`ID`** 名称的小写版本，仅包含 a-z、0-9、`.`、`-` 和 `_`。

**`VERSION_ID`** 版本的小写版本，仅包含 a-z、0-9、`.`、`-` 和 `_`。

**`PRETTY_NAME`** 向用户展示的名称的精美版本。可能包含发行信息。

**`ANSI_COLOR`** 操作系统的建议颜色呈现。此字符串应适合包含在 ESC [ m ANSI/ECMA-48 转义序列中，以首选颜色呈现操作系统。此变量是可选的。

**`CPE_NAME`** 操作系统的 CPE 名称。此字段应遵循 NIST 通用平台枚举规范。

**`HOME_URL`**

**`SUPPORT_URL`**

**`BUG_REPORT_URL`**

**`PRIVACY_POLICY_URL`** 互联网上的链接，采用 RFC 3986 格式，指向此操作系统不同方面的内容。这些变量是可选的。

**`BUILD_ID`** 标识构建的字符串。此变量是可选的。

**`VARIANT`** 描述此操作系统变体的字符串。此变量是可选的。

**`VARIANT_ID`** 变体的小写版本，仅包含 a-z、0-9、`.`、`-` 和 `_`。此变量是可选的。

所有其他变量没有标准定义的含义。

## 文件

**/etc/os-release** 指向实际 `os-release` 文件的符号链接。

**/var/run/os-release** 生成的 os-release 文件，描述当前运行的系统。

## 参见

**CPE** 规范 https://csrc.nist.gov/projects/security-content-automation-protocol/scap-specifications/cpe

**RFC** 3986 https://tools.ietf.org/html/rfc3986

**os-release** 规范 https://www.linux.org/docs/man5/os-release.html

## 历史

此文件首次出现在 FreeBSD 13.0 中。
