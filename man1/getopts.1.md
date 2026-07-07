# getopts.1

`getopts` — FreeBSD shell 内建命令索引

## 名称

`getopts`, `builtin`, `keybinds`

## 概要

`参见你所使用的 shell 手册以了解操作详情。`

## 描述

`getopts` 是一个 shell 内建命令。本页面提供 [csh(1)](csh.1.md) 和 [sh(1)](sh.1.md)（构成 BSD 用户环境的命令行解释器）所提供的 `builtin` 命令、关键字和键盘绑定的索引。

### 命令

下表列出了 `builtin` 命令和关键字、它们是否作为独立实用程序存在，以及提供它们的标准 shell。

| *Command* | *Standalone* | [csh(1)](csh.1.md) | [sh(1)](sh.1.md) |
| --- | --- | --- | --- |
| `!` | No | No | Yes |
| `%` | No | Yes | No |
| `.` | No | No | Yes |
| `:` | No | Yes | Yes |
| `@` | No | Yes | No |
| `[` | Yes | No | Yes |
| `{` | No | No | Yes |
| `}` | No | No | Yes |
| `alias` | No | Yes | Yes |
| `alloc` | No | Yes | No |
| `bg` | No | Yes | Yes |
| `bind` | No | No | Yes |
| `bindkey` | No | Yes | No |
| `break` | No | Yes | Yes |
| `breaksw` | No | Yes | No |
| `builtin` | No | No | Yes |
| `builtins` | No | Yes | No |
| `case` | No | Yes | Yes |
| `cd` | No | Yes | Yes |
| `chdir` | No | Yes | Yes |
| `command` | No | No | Yes |
| `complete` | No | Yes | No |
| `continue` | No | Yes | Yes |
| `default` | No | Yes | No |
| `dirs` | No | Yes | No |
| `do` | No | No | Yes |
| `done` | No | No | Yes |
| `echo` | Yes | Yes | Yes |
| `echotc` | No | Yes | No |
| `elif` | No | No | Yes |
| `else` | No | Yes | Yes |
| `end` | No | Yes | No |
| `endif` | No | Yes | No |
| `endsw` | No | Yes | No |
| `esac` | No | No | Yes |
| `eval` | No | Yes | Yes |
| `exec` | No | Yes | Yes |
| `exit` | No | Yes | Yes |
| `export` | No | No | Yes |
| `false` | Yes | No | Yes |
| `fc` | No | No | Yes |
| `fg` | No | Yes | Yes |
| `fi` | No | No | Yes |
| `filetest` | No | Yes | No |
| `for` | No | No | Yes |
| `foreach` | No | Yes | No |
| `getopts` | No | No | Yes |
| `glob` | No | Yes | No |
| `goto` | No | Yes | No |
| `hash` | No | No | Yes |
| `hashstat` | No | Yes | No |
| `history` | No | Yes | No |
| `hup` | No | Yes | No |
| `if` | No | Yes | Yes |
| `jobid` | No | No | Yes |
| `jobs` | No | Yes | Yes |
| `kill` | Yes | Yes | Yes |
| `limit` | No | Yes | No |
| `local` | No | No | Yes |
| `log` | No | Yes | No |
| `login` | Yes | Yes | No |
| `logout` | No | Yes | No |
| `ls-F` | No | Yes | No |
| `nice` | Yes | Yes | No |
| `nohup` | Yes | Yes | No |
| `notify` | No | Yes | No |
| `onintr` | No | Yes | No |
| `popd` | No | Yes | No |
| `printenv` | Yes | Yes | No |
| `printf` | Yes | No | Yes |
| `pushd` | No | Yes | No |
| `pwd` | Yes | No | Yes |
| `read` | No | No | Yes |
| `readonly` | No | No | Yes |
| `rehash` | No | Yes | No |
| `repeat` | No | Yes | No |
| `return` | No | No | Yes |
| `sched` | No | Yes | No |
| `set` | No | Yes | Yes |
| `setenv` | No | Yes | No |
| `settc` | No | Yes | No |
| `setty` | No | Yes | No |
| `setvar` | No | No | Yes |
| `shift` | No | Yes | Yes |
| `source` | No | Yes | No |
| `stop` | No | Yes | No |
| `suspend` | No | Yes | No |
| `switch` | No | Yes | No |
| `telltc` | No | Yes | No |
| `test` | Yes | No | Yes |
| `then` | No | No | Yes |
| `time` | Yes | Yes | No |
| `times` | No | No | Yes |
| `trap` | No | No | Yes |
| `true` | Yes | No | Yes |
| `type` | No | No | Yes |
| `ulimit` | No | No | Yes |
| `umask` | No | Yes | Yes |
| `unalias` | No | Yes | Yes |
| `uncomplete` | No | Yes | No |
| `unhash` | No | Yes | No |
| `unlimit` | No | Yes | No |
| `unset` | No | Yes | Yes |
| `unsetenv` | No | Yes | No |
| `until` | No | No | Yes |
| `wait` | No | Yes | Yes |
| `where` | No | Yes | No |
| `which` | Yes | Yes | No |
| `while` | No | Yes | Yes |

### 键盘绑定

命令行环境还提供以下默认键盘绑定：

| *Signal* | [csh(1)](csh.1.md) | [sh(1)](sh.1.md) |
| --- | --- | --- |
| `Backspace` | ^H | ^H |
| `Carriage Return` | ^M \| ^J | ^M \| ^J |
| `Tab` | ^I | ^I |
| `Beginning of Line` | ^A | ^A |
| `End of Line` | ^E | ^E |
| `Cursor Forward` | ^F | ^F |
| `Cursor Backward` | ^B | ^B |
| `Clear Screen` | ^L | ^L |
| `Cut Line` | ^U | ^U |
| `Cut Word Backwards` | ^W | ^W |
| `Cut Rest of Line` | ^K | ^K |
| `Paste Last Cut` | ^Y | ^Y |
| `Typo` | ^T | ^T |
| End of File (`EOF` ) | ^D | ^D |
| Interupt (`SIGINT` ) | ^C | ^C |
| Process info (`SIGINFO` ) | ^T | ^T |
| `Search History` | No | ^R |
| `Exit Search History` | No | ^G |
| `Previous Command` | ^P | ^P |
| `Next Command` | ^N | ^N |
| `Print Next Character` | ^V | ^V |
| `Pause Job` | ^S | ^S |
| `Resume Job` | ^Q | ^Q |
| Suspend Job `(SIGTSTP)` | ^Z | ^Z |
| `Scrollback Mode` | ScrLk* | ScrLk* |

\*: 标记 `*` 的绑定由控制台驱动 [vt(4)](../man4/vt.4.md) 提供。

## 参见

[csh(1)](csh.1.md), echo(1), false(1), [kill(1)](kill.1.md), [login(1)](login.1.md), [nice(1)](nice.1.md), nohup(1), [printenv(1)](printenv.1.md), printf(1), [pwd(1)](pwd.1.md), [sh(1)](sh.1.md), [test(1)](test.1.md), [time(1)](time.1.md), true(1), [which(1)](which.1.md)

## 历史

`builtin` 手册页首次出现于 FreeBSD 3.4。

## 作者

本手册页由 Alexander Ziaee <ziaee@FreeBSD.org> 基于 Sheldon Hearn <sheldonh@FreeBSD.org> 的早期版本编写。

## 注意事项

虽然 `builtin` 命令可能存在于多个 shell 或独立实用程序中，但各自的实现可能不同。

独立实用程序及其手册必须从具有同名 `builtin` 命令的 shell 中通过路径调用。
