  BUILTIN(1)  

BUILTIN(1)

FreeBSD General Commands Manual

BUILTIN(1)

[名称](#__u540D___u79F0_)
=======================

`内置`, `!`, `%`, `.`, `:`, `@`, `[`, `{`, `}`, `alias`, `alloc`, `bg`, `bind`, `bindkey`, `break`, `breaksw`, `builtins`, `case`, `cd`, `chdir`, `command`, `complete`, `continue`, `default`, `dirs`, `do`, `done`, `echo`, `echotc`, `elif`, `else`, `end`, `endif`, `endsw`, `esac`, `eval`, `exec`, `exit`, `export`, `false`, `fc`, `fg`, `filetest`, `fi`, `for`, `foreach`, `getopts`, `glob`, `goto`, `hash`, `hashstat`, `history`, `hup`, `if`, `jobid`, `jobs`, `kill`, `limit`, `local`, `log`, `login`, `logout`, `ls-F`, `nice`, `nohup`, `notify`, `onintr`, `popd`, `printenv`, `printf`, `pushd`, `pwd`, `read`, `readonly`, `rehash`, `repeat`, `return`, `sched`, `set`, `setenv`, `settc`, `setty`, `setvar`, `shift`, `source`, `stop`, `suspend`, `switch`, `telltc`, `test`, `then`, `time`, `times`, `trap`, `true`, `type`, `ulimit`, `umask`, `unalias`, `uncomplete`, `unhash`, `unlimit`, `unset`, `unsetenv`, `until`, `wait`, `where`, `which`, `while` —

shell 内置命令

[概要](#__u6982___u8981_)
=======================

请参阅相应 shell 手册页中的内置命令描述。

[描述](#__u63CF___u8FF0_)
=======================

Shell 内置命令是可以在运行的 shell 进程中执行的命令。请注意，在 csh(1) 内置命令的情况下，如果该命令作为管道中除最后一个以外的任何组件出现，则该命令将在子 shell 中执行。

如果指定给 shell 的命令包含斜杠 ‘`/`’, 则 shell 将不会执行内置命令，即使指定命令的最后一个组件与内置命令的名称匹配。因此，虽然指定 “`echo`” 会导致在支持 `echo` 内置命令的 shell 下执行内置命令，但指定 “`/bin/echo`” 或 “`./echo`” 不会。

-
虽然某些内置命令可能存在于多个 shell 中，但在支持它们的每个 shell 下它们的操作可能不同。下表列出了 shell 内置命令、支持它们的标准 shell 以及它们是否作为独立实用程序存在。

此处仅列出 csh(1) 和 sh(1) shell 的内置命令。有关其内置命令的操作的详细信息，请参阅 shell 的手册页。请注意，至少 sh(1) 手册页将其中一些命令称为 “内置命令” ，其中一些称为 “保留字 。” 其他 shell 的用户可能需要查阅 info(1) 页面或其他文档来源。

在 _External_ 下标记为 “`No**`” 的命令确实存在于外部，但使用同名的内置命令作为脚本实现。

_Command_

_External_

csh(1)

sh(1)

[`!`](#!)

No

No

Yes

[`%`](#_)

No

Yes

No

[`.`](#.)

No

No

Yes

[`:`](#:)

No

Yes

Yes

[`@`](#@)

No

Yes

No

[`[`](#__2)

Yes

No

Yes

[`{`](#__3)

No

No

Yes

[`}`](#__4)

No

No

Yes

[`alias`](#alias)

No\*\*

Yes

Yes

[`alloc`](#alloc)

No

Yes

No

[`bg`](#bg)

No\*\*

Yes

Yes

[`bind`](#bind)

No

No

Yes

[`bindkey`](#bindkey)

No

Yes

No

[`break`](#break)

No

Yes

Yes

[`breaksw`](#breaksw)

No

Yes

No

[`builtin`](#builtin)

No

No

Yes

[`builtins`](#builtins)

No

Yes

No

[`case`](#case)

No

Yes

Yes

[`cd`](#cd)

No\*\*

Yes

Yes

[`chdir`](#chdir)

No

Yes

Yes

[`command`](#command)

No\*\*

No

Yes

[`complete`](#complete)

No

Yes

No

[`continue`](#continue)

No

Yes

Yes

[`default`](#default)

No

Yes

No

[`dirs`](#dirs)

No

Yes

No

[`do`](#do)

No

No

Yes

[`done`](#done)

No

No

Yes

[`echo`](#echo)

Yes

Yes

Yes

[`echotc`](#echotc)

No

Yes

No

[`elif`](#elif)

No

No

Yes

[`else`](#else)

No

Yes

Yes

[`end`](#end)

No

Yes

No

[`endif`](#endif)

No

Yes

No

[`endsw`](#endsw)

No

Yes

No

[`esac`](#esac)

No

No

Yes

[`eval`](#eval)

No

Yes

Yes

[`exec`](#exec)

No

Yes

Yes

[`exit`](#exit)

No

Yes

Yes

[`export`](#export)

No

No

Yes

[`false`](#false)

Yes

No

Yes

[`fc`](#fc)

No\*\*

No

Yes

[`fg`](#fg)

No\*\*

Yes

Yes

[`filetest`](#filetest)

No

Yes

No

[`fi`](#fi)

No

No

Yes

[`for`](#for)

No

No

Yes

[`foreach`](#foreach)

No

Yes

No

[`getopts`](#getopts)

No\*\*

No

Yes

[`glob`](#glob)

No

Yes

No

[`goto`](#goto)

No

Yes

No

[`hash`](#hash)

No\*\*

No

Yes

[`hashstat`](#hashstat)

No

Yes

No

[`history`](#history)

No

Yes

No

[`hup`](#hup)

No

Yes

No

[`if`](#if)

No

Yes

Yes

[`jobid`](#jobid)

No

No

Yes

[`jobs`](#jobs)

No\*\*

Yes

Yes

[`kill`](#kill)

Yes

Yes

Yes

[`limit`](#limit)

No

Yes

No

[`local`](#local)

No

No

Yes

[`log`](#log)

No

Yes

No

[`login`](#login)

Yes

Yes

No

[`logout`](#logout)

No

Yes

No

[`ls-F`](#ls-F)

No

Yes

No

[`nice`](#nice)

Yes

Yes

No

[`nohup`](#nohup)

Yes

Yes

No

[`notify`](#notify)

No

Yes

No

[`onintr`](#onintr)

No

Yes

No

[`popd`](#popd)

No

Yes

No

[`printenv`](#printenv)

Yes

Yes

No

[`printf`](#printf)

Yes

No

Yes

[`pushd`](#pushd)

No

Yes

No

[`pwd`](#pwd)

Yes

No

Yes

[`read`](#read)

No\*\*

No

Yes

[`readonly`](#readonly)

No

No

Yes

[`rehash`](#rehash)

No

Yes

No

[`repeat`](#repeat)

No

Yes

No

[`return`](#return)

No

No

Yes

[`sched`](#sched)

No

Yes

No

[`set`](#set)

No

Yes

Yes

[`setenv`](#setenv)

No

Yes

No

[`settc`](#settc)

No

Yes

No

[`setty`](#setty)

No

Yes

No

[`setvar`](#setvar)

No

No

Yes

[`shift`](#shift)

No

Yes

Yes

[`source`](#source)

No

Yes

No

[`stop`](#stop)

No

Yes

No

[`suspend`](#suspend)

No

Yes

No

[`switch`](#switch)

No

Yes

No

[`telltc`](#telltc)

No

Yes

No

[`test`](#test)

Yes

No

Yes

[`then`](#then)

No

No

Yes

[`time`](#time)

Yes

Yes

No

[`times`](#times)

No

No

Yes

[`trap`](#trap)

No

No

Yes

[`true`](#true)

Yes

No

Yes

[`type`](#type)

No\*\*

No

Yes

[`ulimit`](#ulimit)

No\*\*

No

Yes

[`umask`](#umask)

No\*\*

Yes

Yes

[`unalias`](#unalias)

No\*\*

Yes

Yes

[`uncomplete`](#uncomplete)

No

Yes

No

[`unhash`](#unhash)

No

Yes

No

[`unlimit`](#unlimit)

No

Yes

No

[`unset`](#unset)

No

Yes

Yes

[`unsetenv`](#unsetenv)

No

Yes

No

[`until`](#until)

No

No

Yes

[`wait`](#wait)

No\*\*

Yes

Yes

[`where`](#where)

No

Yes

No

[`which`](#which)

Yes

Yes

No

[`while`](#while)

No

Yes

Yes

[参见](#__u53C2___u89C1_)
=======================

csh(1), echo(1), false(1), info(1), kill(1), login(1), nice(1), nohup(1), printenv(1), printf(1), pwd(1), sh(1), test(1), time(1), true(1), which(1)

[历史](#__u5386___u53F2_)
=======================

`内置` 手册页首次出现在 FreeBSD 3.4 中。

[作者](#__u4F5C___u8005_)
=======================

本手册页由 Sheldon Hearn 编写 <[sheldonh@FreeBSD.org](mailto:sheldonh@FreeBSD.org) [。](mailto:。)\>

December 21, 2010

FreeBSD 13.1-RELEASE