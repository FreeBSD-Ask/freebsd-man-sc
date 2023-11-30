  SERVICE(8)  

SERVICE(8)

FreeBSD System Manager's Manual

SERVICE(8)

[名称](#__u540D___u79F0_)
=======================

`service` —

控制（启动/停止/等）或列出系统服务

[概要](#__u6982___u8981_)
=======================

`service` \[`-j` jail\] `-e` `service` \[`-j` jail\] `-R` `service` \[`-j` jail\] \[`-v`\] `-l` `service` \[`-j` jail\] \[`-v`\] `-r` `service` \[`-j` jail\] \[`-v`\] script command

[描述](#__u63CF___u8FF0_)
=======================

`service` 命令是 rc.d 系统的简单接口。 它的主要目的是启动和停止 rc.d 脚本提供的服务。 当用于此目的时，它将设置启动时使用的相同受限环境 (请参阅 [环境](#__u73AF___u5883_)) 。 它还可用于使用各种标准列出脚本。

选项如下：

[`-e`](#e)

列出已启用的服务。 要检查的脚本列表使用 rcorder(8) 编译，方法与在 rc(8) 中完成的方式相同，然后检查该脚本列表是否存在 “rcvar” 分配。 如果存在，则检查脚本以查看它是否已启用。

[`-j`](#j) jail

在命名的监狱下执行给定的操作。 jail 参数可以是监狱 ID 或监狱名称。

[`-l`](#l)

列出 /etc/rc.d 和本地启动目录中的所有文件。 如 rc.conf(5) 中所述，这通常是 /usr/local/etc/rc.d 。 所有文件都将被列出，无论它们是否是实际的 rc.d 脚本。

[`-R`](#R)

重新启动所有启用的本地服务。

[`-r`](#r)

像上面的 `-e` 一样生成 rcorder(8) ，但列出所有文件，而不仅仅是启用的文件。

[`-v`](#v)

稍微详细一点。

[环境](#__u73AF___u5883_)
=======================

当用于运行 rc.d 脚本时， `service` 命令将 `HOME` 设置为 / 并将 `PATH` 设置为 /sbin:/bin:/usr/sbin:/usr/bin ，这就是它们在引导时在 /etc/rc 中的设置方式。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `service` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

以下是 `service` 命令的典型用法示例：

service named status service -j dns named status service -rv 

以下可编程完成条目可在 csh(1) 中用于 rc.d 脚本的名称和常用命令：

complete service 'c/-/(e l r v)/' 'p/1/\`service -l\`/' \\ 'n/\*/(start stop reload restart \\ status rcvar onestart onestop)/' 

以下可编程完成条目可在 bash(1) 中用于 rc.d 脚本的名称：

\_service () { local cur cur=${COMP\_WORDS\[COMP\_CWORD\]} COMPREPLY=( $( compgen -W '$( service -l )' -- $cur ) ) return 0 } complete -F \_service service 

[参见](#__u53C2___u89C1_)
=======================

bash(1) (ports/shells/bash), rc.conf(5), rc(8), rcorder(8)

[历史](#__u5386___u53F2_)
=======================

`service` 实用程序首次出现在 FreeBSD 7.3 中。

[作者](#__u4F5C___u8005_)
=======================

本手册页由 Douglas Barton <[dougb@FreeBSD.org](mailto:dougb@FreeBSD.org)\> 编写。

January 16, 2021

FreeBSD 13.1-RELEASE