# debug.sh.8

`debug.sh` — 选择性调试脚本

## 名称

`debug.sh`

## 概要

`$_DEBUG_SH . debug.sh`

`DebugOn [-eo] tag ...`

`DebugOff [-eo] [rc=rc] tag ...`

`Debugging`

`DebugAdd tag`

`DebugEcho [message]`

`DebugLog [message]`

`DebugShell tag ...`

`DebugTrace message`

`Debug tag ...`

## 描述

`debug.sh` 提供以下函数，便于对复杂 shell 脚本进行灵活的运行时跟踪。

```sh
$DEBUG_DO echo "$@"
```

**`DebugOn`** [`-eo`] `tag ...` 如果在 `DEBUG_SH`（以逗号分隔的标签列表）中找到某个 `tag`，则开启跟踪。如果在 `DEBUG_SH` 中找到 `!tag`，则关闭跟踪。它将 `DEBUG_ON` 设置为导致启用跟踪的 `tag`，如果匹配到 `!tag` 则设置为 `DEBUG_OFF`。如果存在 `-e` 选项，当没有 `tag` 匹配时返回 1。如果存在 `-o` 选项，除非有匹配的 `tag`，否则关闭跟踪，适用于跟踪输出过于嘈杂的函数。

**`DebugOff`** [`-eo`] [`rc=` `rc`] `tag ...` 如果某个 `tag` 匹配 `DEBUG_OFF` 则开启跟踪，如果某个 `tag` 匹配 `DEBUG_ON` 则关闭跟踪。这使得嵌套函数不会相互干扰。标志 `-e` 和 `-o` 会被忽略，它们的存在只是为了与 `DebugOn()` 调用保持对称。可选的 `rc` 值将被返回，而非默认值 0。因此，如果 `DebugOff()` 是函数中的最后一个操作，`rc` 将成为该函数的返回码。

**`Debugging`** 如果启用了跟踪则返回 true。它适用于限定复杂调试操作的范围，而非使用大量 `$DEBUG_DO` 行。

**`DebugAdd`** `tag` 将 `tag` 添加到 `DEBUG_SH`，以影响后续输出（可能在子进程中）。

**`DebugEcho`** 只是以下命令的简写：

**`DebugLog`** [`message`] 如果启用了调试，则输出带有时间戳前缀的 `message`。

**`DebugShell`** `tag ...` 如果在 `DEBUG_INTERACTIVE` 中找到任意 `tag`，且有可用的 tty，则运行交互式 shell。所使用的 shell 由 `DEBUG_SHELL` 或 `SHELL` 定义，默认为 **/bin/sh**。

**`DebugTrace`** `message` 调试输出可能非常嘈杂，且难以与脚本对齐。此函数输出一个非常醒目的横幅，指示 `DEBUG_ON` 的值，并将 `message` 传递给 `DebugLog()`，最后重复该横幅。

**`Debug`** `tag ...` 为向后兼容，调用 `DebugOn()`，如果未开启跟踪，则调用 `DebugOff()` 将其关闭。

变量 `DEBUG_SKIP` 和 `DEBUG_DO` 被设置用于启用/禁用调试开启时应跳过/运行的代码。`DEBUGGING` 与 `DEBUG_SKIP` 相同，用于向后兼容，仅由 `Debug()` 设置。

使用 `$_DEBUG_SH` 是为了防止重复包含，不过在这种情况下重复包含也无害。

## 文件

**/libexec/debug.sh** 调试功能的源代码。

## 缺陷

在某些版本的 ksh(1) 中无法工作。如果某个函数开启了跟踪，ksh 会在该函数返回时将其关闭——毫无用处。

PD ksh 工作正常 ;-)

## 作者

`debug.sh` 由 Simon J Gerraty <sjg@crufty.net> 编写。
