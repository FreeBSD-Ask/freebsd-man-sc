# hesiod.conf(5)

`hesiod.conf` — Hesiod 库的配置文件

## 名称

`hesiod.conf`

## 描述

`hesiod.conf` 文件决定 Hesiod 库的行为。空行和以 `#` 字符开头的行将被忽略。所有其他行应采用 `variable` = `value` 的形式，其中 `value` 应为单个单词。可用的 `variables` 和 `values` 如下：

**`lhs`** 指定用于 Hesiod 查询的域前缀。在几乎所有情况下，你应指定 "`lhs=.ns`"。如果未指定 lhs 值，默认值为无域前缀，这与大多数 Hesiod 域不兼容。

**`rhs`** 指定默认的 Hesiod 域；此值可被 `HES_DOMAIN` 环境变量覆盖。必须指定一行 rhs 才能使 Hesiod 库正常工作。

**`classes`** 指定 Hesiod 应在哪些 DNS 类中进行查找。可能的值为 `IN`（首选类）和 `HS`（已弃用的类，仍被某些站点使用）。你可以指定两个类并以逗号分隔，先在一个类中查找，如果该类中没有条目再在另一个类中查找。classes 变量的默认值为 "`IN,HS`"。

## 参见

hesiod(3)

## 缺陷

`lhs` 的默认值可能应该更合理一些。
