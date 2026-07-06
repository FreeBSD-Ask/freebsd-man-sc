# style.lua.9

`style.lua` — FreeBSD Lua 文件风格指南

## 名称

`style.lua` FreeBSD Lua 文件风格指南

## 描述

本文件指定了 FreeBSD 源码树中 Lua 源文件的首选风格。许多风格规则隐含在示例中。在假设 `style.lua` 对某个问题保持沉默之前，请仔细检查示例。

版权头部应是一系列单行注释。多行注释中的每一行都使用单行注释风格。

任何版权头部之后有一个空行。

包含其他文件和模块的首选方法是使用 `require name`，例如：

```sh
-- 许可证块
config = require("config");
menu = require("menu");
password = require("password");
-- 模块 require 块之后一个空行
```

通常避免使用 `include`。

缩进和换行应匹配 [style(9)](style.9.md) 提供的指南。注意，如果可读性会受影响，可以在远早于 80 列时换行。

在可能的情况下，`s:method ...` 优先于 `method s ...`。这适用于具有方法的对象。字符串是具有方法的对象的常用示例。

对 `nil` 的测试应显式进行，而不是作为布尔表达式。应避免单行条件语句和循环。

在模块作用域中，`local` 变量应优先于全局变量。变量标识符倾向使用内部下划线，而函数标识符倾向使用 camelCase。

如果表定义跨多行，则表中最后一个值应包含可选的终止逗号。例如：

```sh
-- 简单表定义不需要终止逗号
local trivial_table = {1, 2, 3, 4}
local complex_table = {
	{
		id = "foo",
		func = foo_function, -- 首选尾随逗号
	},
	{
		id = "bar",
		func = bar_function,
	},	-- 首选尾随逗号
}
```

这减少了修改更复杂表时引入错误的机会。

多个局部变量不应在单行上**同时**声明并初始化。包含多个未初始化变量声明的行可以。包含多个变量声明并初始化为返回具有相同数量值的元组的单个函数调用的行也可以。

初始化**应**在声明时酌情进行。

## 参见

[style(9)](style.9.md)

## 历史

本手册页的灵感来自 FreeBSD 中 [style(9)](style.9.md) 手册页的相同来源。
