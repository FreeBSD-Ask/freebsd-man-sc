# service.8

`service` — 控制（启动/停止等）或列出系统服务

## 名称

`service`

## 概要

`service [-j jail] -e`
`service [-j jail] [-q] -R`
`service [-j jail] [-v] -l`
`service [-j jail] [-v] -r`
`service [-j jail] [-dqv] [-E var=value] script [command]`

## 描述

`service` 命令是 rc.d 系统的简易接口。其主要用途是启动和停止由 rc.d 脚本提供的服务。用于此目的时，它会设置与启动时使用的相同的受限环境（参见下文的 [环境变量](#环境变量)）。它还可用于根据各种条件列出脚本。

`command` 的可用值集合取决于所调用的特定 rc.d 脚本。有关大多数 rc.d 脚本支持的标准命令列表，请参见 [rc(8)](rc.8.md)。

可用选项如下：

**`-d`** 启用调试。

**`-E`** `var=value` 在启动脚本之前将环境变量 `var` 设置为指定的 `value`。此选项可多次使用。

**`-e`** 列出已启用的服务。待检查的脚本列表使用 [rcorder(8)](rcorder.8.md) 编译，方式与 [rc(8)](rc.8.md) 中相同，然后检查该脚本列表中是否存在 "rcvar" 赋值。如果存在，则检查脚本是否已启用。

**`-j`** `jail` 在指定的 jail 中执行给定操作。`jail` 参数可以是 jail ID 或 jail 名称。

**`-l`** 列出 **/etc/rc.d** 和本地启动目录中的所有文件。如 [rc.conf(5)](../man5/rc.conf.5.md) 所述，这通常是 **/usr/local/etc/rc.d**。无论是否为实际的 rc.d 脚本，所有文件都会被列出。

**`-q`** 静默模式，将输出重定向到 **/dev/null**。

**`-R`** 重启所有已启用的本地服务。

**`-r`** 像上文的 `-e` 一样生成 [rcorder(8)](rcorder.8.md) 顺序，但列出所有文件，而不仅是已启用的文件。

**`-v`** 稍微更详细地输出。

## 环境变量

用于运行 rc.d 脚本时，`service` 命令将 `HOME` 设置为 **/**，将 `PATH` 设置为 **/sbin:/bin:/usr/sbin:/usr/bin**，与启动时在 **/etc/rc** 中的设置一致。如果使用了 `-E` 选项，则相应地设置对应的变量。

## 退出状态

`service` 工具成功时退出状态为 0，发生错误时大于 0。

## 实例

以下是一些最常见的 service 命令示例。有关大多数 rc.d 脚本中可用的完整命令列表，请参见 [rc(8)](rc.8.md)。

启用一个服务，然后启动它：

```sh
service sshd enable
service sshd start
```

停止一个服务，然后禁用它：

```sh
service sshd stop
service sshd disable
```

启动一个未启用的服务：

```sh
service sshd onestart
```

报告服务的状态：

```sh
service named status
```

重启在 jail 中运行的服务：

```sh
service -j dns named restart
```

以特定的环境变量启动服务：

```sh
service -E LC_ALL=C.UTF-8 named start
```

报告所有可用服务的详细列表：

```sh
service -rv
```

以下可编程补全条目可用于 [csh(1)](../man1/csh.1.md) 中，用于 rc.d 脚本的名称和常用命令：

```sh
complete service 'c/-/(e l r v)/' 'p/1/`service -l`/' \
		 'n/*/(start stop reload restart \
		 status rcvar onestart onestop)/'
```

以下可编程补全条目可用于 bash(1)（`ports/shells/bash`）中，用于 rc.d 脚本的名称：

```sh
_service () {
	local cur
	cur=${COMP_WORDS[COMP_CWORD]}
	COMPREPLY=( $( compgen -W '$( service -l )' -- $cur ) )
	return 0
}
complete -F _service service
```

## 参见

bash(1)（`ports/shells/bash`）, [rc.conf(5)](../man5/rc.conf.5.md), [rc(8)](rc.8.md), [rcorder(8)](rcorder.8.md), [sysrc(8)](sysrc.8.md)

## 历史

`service` 工具首次出现在 FreeBSD 7.3 中。

## 作者

本手册页由 Douglas Barton <dougb@FreeBSD.org> 编写。
