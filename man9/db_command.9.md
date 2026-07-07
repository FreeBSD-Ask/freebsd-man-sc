# DB_COMMAND(9)

`DB_COMMAND` — 扩展 ddb 命令集

## 名称

`DB_COMMAND`, `DB_COMMAND_FLAGS`, `DB_SHOW_COMMAND`, `DB_SHOW_COMMAND_FLAGS`, `DB_SHOW_ALL_COMMAND`, `DB_TABLE_COMMAND`, `DB_TABLE_COMMAND_FLAGS`, `DB_ALIAS`, `DB_ALIAS_FLAGS`, `DB_SHOW_ALIAS`, `DB_SHOW_ALIAS_FLAGS`, `DB_SHOW_ALL_ALIAS`, `DB_TABLE_ALIAS`, `DB_TABLE_ALIAS_FLAGS`, `DB_DECLARE_TABLE`, `DB_DEFINE_TABLE`

## 概要

```c
#include <ddb/ddb.h>
```

```c
DB_COMMAND(command_name, command_function);
DB_COMMAND_FLAGS(command_name, command_function, flags);
DB_SHOW_COMMAND(command_name, command_function);
DB_SHOW_COMMAND_FLAGS(command_name, command_function, flags);
DB_SHOW_ALL_COMMAND(command_name, command_function);
DB_TABLE_COMMAND(table, command_name, command_function);
DB_TABLE_COMMAND_FLAGS(table, command_name, command_function, flags);
DB_ALIAS(alias_name, command_function);
DB_ALIAS_FLAGS(alias_name, command_function, flags);
DB_SHOW_ALIAS(alias_name, command_function);
DB_SHOW_ALIAS_FLAGS(alias_name, command_function, flags);
DB_SHOW_ALL_ALIAS(alias_name, command_function);
DB_TABLE_ALIAS(table, alias_name, command_function);
DB_TABLE_ALIAS_FLAGS(table, alias_name, command_function, flags);
DB_DEFINE_TABLE(parent, name, table);
DB_DECLARE_TABLE(table);
```

## 描述

`DB_COMMAND` 宏将 `command_name` 添加到顶级命令列表中。从 ddb 调用 `command_name` 将执行 `command_function`。

`DB_SHOW_COMMAND` 和 `DB_SHOW_ALL_COMMAND` 宏大致等同于 `DB_COMMAND`，但在这些情况下，`command_name` 分别是 ddb **show** 命令和 **show all** 命令的子命令。

`DB_TABLE_COMMAND` 宏也类似于 `DB_COMMAND`，但将新命令作为 ddb 命令 `table` 的子命令添加。

`DB_ALIAS`、`DB_SHOW_ALIAS`、`DB_SHOW_ALL_ALIAS` 和 `DB_TABLE_ALIAS` 宏以替代命令名 `alias_name` 注册现有的 `command_function`。

这些命令的 _FLAGS 变体允许程序员为命令结构的 `flag` 字段指定值。可能的标志值与 `struct db_command` 一起定义于

`#include <ddb/ddb.h>`

通用命令语法：`command`[`/``modifier`] `address`[,`count`]，转换为 `command_function` 的以下参数：

**`addr`** 作为参数传递给命令的地址。

**`have_addr`** 布尔值，如果 addr 字段有效则为真。

**`count`** 从偏移量 `addr` 开始命令必须处理的四字数量。

**`modif`** 指向修饰符字符串的指针。即一系列用于向命令传递某些选项的符号。例如，**examine** 命令在传入修饰符 "d" 时将以十进制形式显示字。

`DB_DEFINE_TABLE` 宏将新命令 `name` 作为现有命令表 `parent` 的子命令添加。新命令定义了一个名为 `table` 的表，其中包含子命令。通过将 `table` 作为第一个参数传递给 DB_TABLE_ 系列宏之一，可以向此表添加新命令和别名。

## 实例

在你的模块中，命令声明如下：

```c
DB_COMMAND(mycmd, my_cmd_func)
{
	if (have_addr)
		db_printf("Calling my command with address %pn", addr);
}
```

此命令的别名声明如下：

```c
DB_ALIAS(mycmd2, my_cmd_func);
```

然后，在 ddb 中：

```sh
db> mycmd 0x1000
Calling my command with address 0x1000
db> mycmd2 0x2500
Calling my command with address 0x2500
db>
```

## 参见

[ddb(4)](../man4/ddb.4.md)

## 作者

本手册页由 Guillaume Ballet <gballet@gmail.com> 编写。
