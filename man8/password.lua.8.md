# password.lua(8)

`password.lua` — 引导加载器密码模块

## 名称

`password.lua`

## 描述

`password.lua` 包含提示输入和检查密码的功能。

在使用 `password.lua` 提供的功能之前，必须使用如下语句将其包含：

```lua
local password = require("password")
```

以下函数从 `password.lua` 导出：

**`password.read(prompt_length)`** 在提示后读取密码。需要 `prompt_length` 以便在用户输入时正确绘制旋转符。

**`password.check()`** 驱动加载器完成的主要密码检查。`password.check()` 函数将检查 `bootlock_password`、`geom_eli_passphrase_prompt` 和 `password`，并按需提示用户输入密码。如果设置了 `password`，则在提示用户输入密码时将开始自动引导序列。

## 参见

screen.lua(8)

## 作者

`password.lua` 文件最初由 Pedro Souza <pedrosouza@FreeBSD.org> 编写。后续工作及本手册页由 Kyle Evans <kevans@FreeBSD.org> 完成。
