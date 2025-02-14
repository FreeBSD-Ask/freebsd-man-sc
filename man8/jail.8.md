  JAIL(8)  

JAIL(8)

FreeBSD System Manager's Manual

JAIL(8)

[名称](#__u540D___u79F0_)
=======================

`jail` —

管理系统 jails

[概要](#__u6982___u8981_)
=======================

`jail` \[`-dhilqv`\] \[`-J` jid\_file\] \[`-u` username\] \[`-U` username\] \[`-cmr`\] param\=value ... \[`command`\=command ...\] `jail` \[`-dqv`\] \[`-f` conf\_file\] \[`-p` limit\] \[`-cmr`\] \[jail\] `jail` \[`-qv`\] \[`-f` conf\_file\] \[`-rR`\] \[`*` | jail ...\] `jail` \[`-dhilqv`\] \[`-J` jid\_file\] \[`-u` username\] \[`-U` username\] \[`-n` jailname\] \[`-s` securelevel\] \[path hostname \[ip\[,...\]\] command ...\] `jail` \[`-f` conf\_file\] `-e` separator

[描述](#__u63CF___u8FF0_)
=======================

`jail` 实用程序创建新的 jail ，或者修改或删除现有的 jail 。 它还可以打印配置的 jail 列表及其参数。 jail (或 “prison”) 是通过命令行上的参数或在 jail.conf(5) 文件中指定的。

必须至少指定选项 `-c`, `-e`, `-m` 或 `-r` 之一。 这些选项单独或组合使用来描述要执行的操作：

[`-c`](#c)

创建一个新的 jail 。 jail jid 和 name 参数（如果在命令行中指定）不得引用现有的 jail。

[`-e`](#e) separator

展示所有已配置的非通配符 jail 及其参数的列表。 如果使用此选项，则不会创建、修改或删除 jail 。 separator 字符串用于分隔参数。 使用 jls(8) 实用程序列出正在运行的 jails。

[`-m`](#m)

修改现有的 jail。 jid 或 name 参数之一必须存在并引用现有的 jail。 某些参数可能不会在正在运行的 jail 中更改。

[`-r`](#r)

删除由 jid 或 name 指定的 jail 。 所有被 jail 的进程都被杀死，并且作为这个 jail 的孩子的所有 jail 也被删除。

[`-rc`](#rc)

重新启动现有的 jail 。  jail 首先被删除然后重新创建，就像 “`jail` `-r`” 和 “`jail` `-c`” 连续运行一样。

[`-cm`](#cm)

如果 jail 不存在则创建 jail ，如果 jail 存在则修改 jail 。

[`-mr`](#mr)

修改现有的 jail 。 如果需要修改无法更改的参数，可以重新启动 jail 。

[`-cmr`](#cmr)

如果 jail 不存在，则创建 jail ，如果 jail 存在，则修改（并可能重新启动） jail 。

其他可用选项包括：

[`-d`](#d)

允许对垂死的 jail 进行更改，相当于 allow.dying 参数。

[`-f`](#f) conf\_file

使用配置文件 conf\_file 而不是默认的 /etc/jail.conf 。

[`-h`](#h)

解析 host.hostname 参数（或 hostname) 并将解析器返回的所有 IP 地址添加到此 jail 的地址列表中。 这等效于 ip\_hostname 参数。

[`-i`](#i)

（仅）输出新创建的 jail 的 jail 标识符。 这意味着 `-q` 选项。

[`-J`](#J) jid\_file

编写一个 jid\_file 文件，其中包含用于启动 jail 的参数。

[`-l`](#l)

在干净的环境中运行命令。 这已弃用，等效于 exec.clean 参数。

[`-n`](#n) jailname

设置 jail 的名称。 这已被弃用，等效于 name 参数。

[`-p`](#p) limit

限制 exec.\* 中可以同时运行的命令数量。

[`-q`](#q)

每当创建、修改或删除 jail 时，禁止打印消息。 只会打印错误消息。

[`-R`](#R)

[`-r`](#r_2) 选项的一种变体，它在不使用配置文件的情况下删除现有的 jail 。 不会使用这个 jail 的与删除相关的参数 — 这个 jail 将被简单地删除。

[`-s`](#s) securelevel

将 kern.securelevel MIB 条目设置为新创建的 jail 中的指定值。 这已弃用，等效于 securelevel 参数。

[`-u`](#u) username

主机环境中的用户名，应该运行被 jail 的命令。 这已弃用，等效于 exec.jail\_user 和 exec.system\_jail\_user 参数。

[`-U`](#U) username

来自被 jail 的环境的用户名，被 jail 的命令应该作为该用户运行。 这已弃用，等效于 exec.jail\_user 参数。

[`-v`](#v)

在每个操作上打印一条消息，例如运行命令和挂载文件系统。

如果选项后没有给出任何参数，则操作（除了删除）将在 jail.conf(5) 文件中指定的所有 jail 执行。  jail 名称的单个参数将仅在指定的 jail 上运行。 `-r` 和 `-R` 选项还可以删除不在 jail.conf(5) 文件中的运行中的 jail ，由名称或 jid 指定。

“\*” 参数是一个通配符，将在所有 jail 中运行，无论它们是否出现在 jail.conf(5) 中；这是 `-r` 删除所有 jail 的最可靠方法。 如果存在分层 jail ，则可以指定部分匹配的通配符定义。 例如， “foo.\*” 的参数将适用于名称为 “foo.bar” 和 “foo.bar.baz” 的 jail 。

可以直接在命令行上使用参数指定 jail。 在这种情况下，将不会使用 jail.conf(5) 文件。 为了向后兼容，命令行也可能有四个固定参数，没有名称： path, hostname, ip 和 command 。 此模式将始终创建一个新 jail ，并且 `-c` 和 `-m` 选项不适用（并且不得存在）。

[Jail 参数](#Jail___u53C2___u6570_)
---------------------------------

jail.conf(5) 文件或命令行中的参数通常采用 “name=value” 的形式。 一些参数是布尔值，没有值，而是由名称单独设置，带或不带 “no” 前缀，例如 persist 或 nopersist 。 它们也可以被赋予值 “true” 和 “false” 。 其他参数可能有多个值，指定为逗号分隔的列表或配置文件中的 “+=” （有关详细信息，请参阅 jail.conf(5) )。

`jail`-
实用程序可识别两类参数。在创建 jail 时，有真正的 jail 参数传递给内核，可以使用 jls(8) 看到，并且（通常）可以使用 “`jail` `-m`” 行更改。 然后是只有 `jail` 本身使用的伪参数。

有一组核心参数，内核模块可以添加自己的 jail 参数。 当前可用参数集可以通过 “`sysctl` `-d` security.jail.param” 检索。 任何未设置的参数都将被赋予默认值，通常基于当前环境。核心参数是：

jid

 jail 标识符。 这将自动分配给一个新的 jail （或可以显式设置），并且可以用于识别 jail 以供以后修改，或用于 jls(8) 或 jexec(8) 等命令。

name

 jail 名称。 这是一个标识 jail 的任意字符串（除了它可能不包含 ‘.’ ）。 与 jid 一样，它可以传递给以后的 `jail` 命令，或者 jls(8) 或 jexec(8). 。 如果未提供 name ，则假定默认值与 jid 相同。 name 参数由 jail.conf(5) 文件格式隐含，使用配置文件时无需显式设置。

path

将成为 jail 根目录的目录。 在 jail 中运行的任何命令，无论是通过 `jail` 还是来自 jexec(8) ，都从该目录运行。

ip4.addr

分配给 jail 的 IPv4 地址列表。 如果设置了此项， jail 将被限制为仅使用这些地址。 任何使用其他地址的尝试都会失败，并且尝试使用通配符地址会默默地使用被 jail 的地址。 对于 IPv4，当未绑定套接字上的源地址选择找不到更好的匹配时，给定的第一个地址将用作源地址。 如果没有一个jails 分配给自己的IP 地址不超过这个单一的重叠IP 地址，则只能使用相同的IP 地址启动多个jails。

ip4.saddrsel

一个布尔选项，用于更改前面提到的行为并禁用 jail 的 IPv4 源地址选择，以支持 jail 的主要 IPv4 地址。 默认情况下，所有 jails 都启用源地址选择，并且父 jails 的 ip4.nosaddrsel 设置不会被任何子jails 继承。

ip4

控制 IPv4 地址的可用性。可能的值是 “inherit” 以允许不受限制地访问所有系统地址， “new” 以通过 ip4.addr 限制地址， “disable” 以阻止 jail 完全使用 IPv4。 设置 ip4.addr 参数意味着值为 “new” 。

ip6.addr, ip6.saddrsel, ip6

 jail 的一组 IPv6 选项，对应于上面的 ip4.addr, ip4.saddrsel 和 ip4 。

vnet

使用自己的虚拟网络堆栈、自己的网络接口、地址、路由表等创建 jail 。 必须使用 **VIMAGE option** 编译内核才能使用它。 可能的值是 “inherit” 以使用系统网络堆栈，可能具有受限的 IP 地址，以及 “new” 以创建新的网络堆栈。

host.hostname

 jail 的主机名。 其他类似的参数是 host.domainname, host.hostuuid 和 host.hostid 。

host

设置主机名的来源及相关信息。 可能的值是使用系统信息的 “inherit” 和 jail 使用上述字段中的信息的 “new” 。 设置上述任何字段都意味着 “new” 的值。

securelevel

 jail 的 kern.securelevel sysctl 的值。  jail 的安全级别永远不会低于其父系统，但通过设置此参数，它可能会有更高的安全级别。 如果系统安全级别更改，任何 jail 安全级别都将至少一样安全。

devfs\_ruleset

在此 jail 中安装 devfs 时强制执行的 devfs 规则集的数量。 零值（默认）表示不强制执行任何规则集。 后代 jail 继承父 jail 的 devfs 规则集执行。 仅当 allow.mount 和 allow.mount.devfs 权限有效且 enforce\_statfs 设置为小于 2 的值时，才能在 jail 中挂载 devfs。无法从 jail 中查看或修改 Devfs 规则和规则集。

注意：只有 devfs 中适当的设备节点才会暴露在 jail 中，这一点很重要；访问 jail 中的磁盘设备可能会允许 jail 中的进程通过修改 jail 外的文件来绕过 jail 沙盒。 有关如何使用 devfs 规则来限制对 per-jail devfs 中条目的访问的信息，请参阅 devfs(8) 。 在 /etc/defaults/devfs.rules 中有一个简单的 devfs 规则集作为规则集 #4 提供。

children.max

该 jail （或该 jail 下的其他 jail ）允许创建的子 jail 的数量。 此限制默认为零，表示 jail 不允许创建子 jail 。 有关更多信息，请参阅 [Hierarchical Jails](#Hierarchical_Jails) 部分。

children.cur

该 jail 的后代数量，包括其自己的子 jail 和在其下创建的任何 jail 。

enforce\_statfs

这决定了 jail 中的哪些信息进程能够获取有关挂载点的信息。 它会影响以下系统调用的行为： statfs(2), fstatfs(2), getfsstat(2) 和 fhstatfs(2) （以及类似的兼容性系统调用）。 设置为 0 时，所有挂载点都可用，没有任何限制。 当设置为 1 时，只有在 jail 的 chroot 目录下的挂载点是可见的。 除此之外，jail 的 chroot 目录的路径从其路径名的前面删除。 当设置为 2（默认值）时，上述系统调用只能在 jail 的 chroot 目录所在的挂载点上运行。

persist

坚持 设置此布尔参数允许 jail 在没有任何进程的情况下存在。 通常，命令作为 jail 创建的一部分运行，然后 jail 在其最后一个进程退出时被销毁。 新的 jail 必须具有 persist 参数或 exec.start or command 或命令伪参数集。

cpuset.id

与此 jail 关联的 cpuset 的 ID（只读）。

dying

如果 jail 正在关闭（只读），这是正确的。

parent

这个 jail 的父级的 jid 如果这是一个顶级 jail ，则为零（只读）。

osrelease

 jail 的 kern.osrelease 和 uname -r 的字符串。

osreldate

 jail 的 kern.osreldate 和 uname -K 的编号。

allow.\*

 jail 环境的一些限制可以在每个 jail 的基础上设置。 除了 allow.set\_hostname 和 allow.reserved\_ports, ，这些布尔参数默认是关闭的。

allow.set\_hostname

可以通过 hostname(1) 或 sethostname(3) 更改 jail 的主机名。

allow.sysvipc

 jail 中的进程可以访问 System V IPC 原语。 这已弃用，取而代之的是每个模块的参数（见下文）。 设置此参数时，相当于将 sysvmsg, sysvsem 和 sysvshm 全部设置为 “inherit” 。

allow.raw\_sockets

 jail 根被允许创建原始套接字。 设置此参数允许 ping(8) 和 traceroute(8) 等实用程序在 jail 内运行。 如果设置了此项，则强制源 IP 地址符合绑定到 jail 的 IP 地址，无论是否在套接字上设置了 `IP_HDRINCL` 标志。 由于原始套接字可用于配置各种网络子系统并与之交互，因此在向不受信任的方授予对 jail 的特权访问时应格外小心。

allow.chflags

通常， jail 中的特权用户被 chflags(2) 视为非特权用户。 设置此参数后，此类用户将被视为特权用户，并且可以根据 kern.securelevel 上的通常约束来操作系统文件标志。

allow.mount

 jail 内的特权用户将能够挂载和卸载标记为 jail 友好的文件系统类型。 lsvfs(1) 命令可用于从 jail 中查找可用于挂载的文件系统类型。 仅当 enforce\_statfs 设置为小于 2 的值时，此权限才有效。

allow.mount.devfs

 jail 内的特权用户将能够挂载和卸载 devfs 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。 应该使用 devfs\_ruleset 选项限制 devfs 规则集的默认设置。

allow.quotas

 jail 根可以管理 jail 文件系统的配额。 这包括 jail 可能与其他 jail 或系统的非 jail 部分共享的文件系统。

allow.read\_msgbuf

被 jail 的用户可能会读取内核消息缓冲区。 如果 security.bsd.unprivileged\_read\_msgbuf MIB 条目为零，这将被限制为 root 用户。

allow.socket\_af

jail 中的套接字通常仅限于 IPv4、IPv6、本地 (UNIX) 和路由。 这允许访问没有添加 jail 功能的其他协议栈。

allow.mlock

在 jail 中通常无法锁定或解锁内存中的物理页面。 设置此参数后，用户可能会受到 security.bsd.unprivileged\_mlock 和资源限制的 mlock(2) 或 munlock(2) 内存。

allow.reserved\_ports

 jail 根可能绑定到低于 1024 的端口。

allow.unprivileged\_proc\_debug

 jail 中的非特权进程可能会使用调试工具。

allow.suser

 jail 的 security.bsd.suser\_enabled sysctl 的值。如果其父系统禁用了超级用户，它将自动被禁用。 默认情况下启用超级用户。

内核模块可以添加自己的参数，这些参数仅在模块加载时存在。 这些通常位于以模块命名的参数下，值为 “inherit” 以使 jail 充分利用模块， “new” 以某种特定于模块的方式封装 jail ， “disable” 以使模块不能进 jail 。 也可能有其他参数来定义模块内的 jail 行为。 特定于模块的参数包括：

allow.mount.fdescfs

 jail 内的特权用户将能够挂载和卸载 fdescfs 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。

allow.mount.fusefs

 jail 内的特权用户将能够挂载和卸载基于 fuse 的文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。

allow.mount.nullfs

 jail 内的特权用户将能够挂载和卸载 nullfs 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。

allow.mount.procfs

 jail 内的特权用户将能够挂载和卸载 procfs 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。

allow.mount.linprocfs

 jail 内的特权用户将能够挂载和卸载 linprocfs 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。

allow.mount.linsysfs

 jail 内的特权用户将能够挂载和卸载 linsysfs 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。

allow.mount.tmpfs

 jail 内的特权用户将能够挂载和卸载 tmpfs 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。

allow.mount.zfs

 jail 内的特权用户将能够挂载和卸载 ZFS 文件系统。 此权限仅与 allow.mount 一起有效，并且仅在 enforce\_statfs 设置为低于 2 的值时有效。 有关如何配置 ZFS 文件系统以在 jail 中运行的信息，请参阅 zfs(8) 。

allow.vmm

 jail 可以访问 vmm(4) 。 此标志仅在加载 vmm(4) 内核模块时可用。

linux

确定jail 的Linux 仿真环境如何出现。 “inherit” 的值将保持相同的环境， “new” 将为 jail 提供自己的环境（在创建 jail 时仍然是最初继承的）。

linux.osname, linux.osrelease, linux.oss\_version

与此 jail 关联的 Linux 操作系统名称、操作系统版本和 OSS 版本。

sysvmsg

允许访问 SYSV IPC 消息原语。 如果设置为 “inherit” ，则系统上的所有 IPC 对象都对这个 jail 可见，无论它们是由 jail 本身、基本系统还是其他 jail 创建的。 如果设置为 “new” ，jail 将拥有自己的 key 命名空间，并且只能看到它创建的对象；系统（或父 jail ）可以访问 jail 的对象，但不能访问其密钥。 如果设置为 “disable” ，jail 将无法执行任何与 sysvmsg 相关的系统调用。

sysvsem, sysvshm

允许以与 sysvmsg 相同的方式访问 SYSV IPC 信号量和共享内存原语。

有一些伪参数没有传递给内核，但被 `jail` 用来设置 jail 环境，通常在创建或删除 jail 时运行指定的命令。 exec.\* 命令参数是在系统或 jail 环境中运行的 sh(1) 命令行。 它们可以被赋予多个值，这些值将按顺序运行指定的命令。 所有命令必须成功（返回零退出状态），否则将不会创建或删除 jail ，视情况而定。

伪参数是：

exec.prepare

在系统环境中运行以准备创建 jail 的命令。 这些命令在分配 IP 地址和挂载文件系统之前执行，因此如果新的 jail 文件系统不存在，它们可以用来创建它。

exec.prestart

在创建 jail 之前在系统环境中运行的命令。

exec.created

在 jail 创建之后，命令（或服务）在 jail 中执行之前在系统环境中运行的命令。

exec.start

创建 jail 时在 jail 环境中运行的命令。一个典型的运行命令是 “sh /etc/rc” 。

command

直接在命令行上指定 jail 时使用的 exec.start 的同义词。 与其他值为单个字符串的参数不同， command 使用 `jail` 命令行的其余部分作为其自己的参数。

exec.poststart

创建 jail 后以及任何 exec.start 命令完成后在系统环境中运行的命令。

exec.prestop

在移除 jail 之前在系统环境中运行的命令。

exec.stop

删除 jail 之前和任何 exec.prestop 命令完成后在 jail 环境中运行的命令。 一个典型的运行命令是 “sh /etc/rc.shutdown jail” 。

exec.poststop

删除 jail 后在系统环境中运行的命令。

exec.release

完成所有其他操作后在系统环境中运行的命令。 这些命令在卸载文件系统和删除 IP 地址后执行，因此如果不再需要，它们可以用于删除 jail 文件系统。

exec.clean

在干净的环境中运行命令。 除 `HOME`, `SHELL`, `TERM` 和 `USER` 之外的环境被丢弃。 `HOME` 和 `SHELL` 设置为目标登录的默认值。 `USER` 设置为目标登录。 `TERM` 是从当前环境中导入的。 还设置了目标登录的登录类能力数据库中的环境变量。

exec.jail\_user

运行命令的用户，在 jail 环境中运行时。 默认以当前用户身份运行命令。

exec.system\_jail\_user

这个布尔选项在系统 passwd(5) 文件中查找 exec.jail\_user ，而不是在 jail 文件中。

exec.system\_user

用户运行命令时，在系统环境中运行时。默认以当前用户身份运行命令。

exec.timeout

等待命令完成的最长时间，以秒为单位。 如果超过此超时时间后命令仍在运行，则不会创建或删除 jail ，视情况而定。

exec.consolelog

将命令输出（stdout 和 stderr）定向到的文件。

exec.fib

在 jail 内运行命令时要设置的 FIB（路由表）。

stop.timeout

发送 `SIGTERM` 信号后等待 jail 进程退出的最长时间（这发生在 exec.stop 命令完成之后）。 经过这么多秒后， jail 将被移除，这将杀死所有剩余的进程。 如果设置为零，则不发送 `SIGTERM` 并立即删除 jail 。 默认值为 10 秒。

interface

用于添加 jail  IP 地址 (ip4.addr 和 ip6.addr) 的网络接口。 在创建jail之前，每个地址的别名都会被添加到接口中，并在jail被移除后从接口中移除。

ip4.addr

除了传递给内核的 IP 地址之外，还可以指定接口、网络掩码和其他参数（由 ifconfig(8) 支持），格式为 “interface|ip-address/netmask param ...” 。 如果在 IP 地址之前给出了接口，则该地址的别名将添加到该接口，与 interface 参数一样。 如果在 IP 地址之后给出了以点分四线形式或 CIDR 形式的网络掩码，则在添加 IP 别名时将使用它。 如果指定了其他参数，那么在添加 IP 别名时也会使用它们。

ip6.addr

除了传递给内核的 IP 地址之外，还可以指定接口、前缀和附加参数（由 ifconfig(8) 支持），格式为 “interface|ip-address/prefix param ...” 。

vnet.interface

创建后提供给启用 vnet 的 jail 的网络接口。 移除jail后，界面会自动释放。

ip\_hostname

解析 host.hostname 参数并将解析器返回的所有 IP 地址添加到此 jail 的地址列表（ (ip4.addr 或 ip6.addr) ）。 这可能会影响从 jail 传出 IPv4 连接的默认地址选择。 解析器首先为每个地址族返回的地址将用作主地址。

mount

在创建 jail 之前挂载的文件系统（并在删除它之后卸载），以单个 fstab(5) 行的形式给出。

mount.fstab

fstab(5) 格式的文件，其中包含在创建 jail 之前要挂载的文件系统。

mount.devfs

在 /dev 目录上挂载 devfs(5) 文件系统，并在 devfs\_ruleset 参数中应用规则集（或规则集 4 的默认值：devfsrules\_jail）以限制在 jail 中可见的设备。

mount.fdescfs

在 chrooted /dev/fd 目录上挂载 fdescfs(5) 文件系统。

mount.procfs

在 chrooted /proc 目录上挂载 procfs(5) 文件系统。

allow.dying

允许对 dying 的 jail 进行更改。

depend

指定该 jail 所依赖的 jail （或多个 jail ）。当要创建这个 jail 时，它所依赖的任何 jail 都必须已经存在。 如果没有，它们将被自动创建，直到最后一个 exec.poststart 命令完成，然后才会采取任何行动来创建这个 jail 。 当 jail 被删除时，情况正好相反：这个 jail 将被删除，直到最后一个 exec.poststop 命令，在它所依赖的任何 jail 被停止之前。

[实例](#__u5B9E___u4F8B_)
=======================

 jail 通常使用以下两种理念之一设置：要么限制特定的应用程序（可能以特权运行），要么创建运行各种守护程序和服务的 “virtual system image” 在这两种情况下，都需要一个相当完整的 FreeBSD 文件系统安装，以便提供必要的命令行工具、守护进程、库、应用程序配置文件等。 但是，对于虚拟服务器配置，需要大量的额外工作来替代 “boot” 过程。 本手册页记录了支持其中任何一个步骤所需的配置步骤，尽管配置步骤可能需要根据当地要求进行细化。

[设置 jail 目录树](#__u8BBE___u7F6E___u76D1___u72F1___u76EE___u5F55___u6811_)
--------------------------------------------------------------------

要设置包含整个 FreeBSD 发行版的 jail 目录树，可以使用以下 sh(1) 命令脚本：

D=/here/is/the/jail cd /usr/src mkdir -p $D make world DESTDIR=$D make distribution DESTDIR=$D 

在许多情况下，这个例子会比需要的更多。 在另一种极端情况下， jail 可能只包含一个文件：要在 jail 中运行的可执行文件。

我们建议进行实验，并警告从 “fat”  jail 开始并删除东西直到它停止工作比从 “thin”  jail 开始并添加东西直到它工作要容易得多。

[设立 jail ](#__u8BBE___u7ACB___u76D1___u72F1_)
-----------------------------------------

执行 [设置 Jail 目录树](#__u8BBE___u7F6E__Jail___u76EE___u5F55___u6811_) 中所述的操作来构建 jail 目录树。 为了这个例子，我们假设你在 /data/jail/testjail 中构建了一个名为 “testjail” 的 jail 。 根据需要用您自己的目录、IP 地址和主机名替换下面的内容。

[设置主机环境](#__u8BBE___u7F6E___u4E3B___u673A___u73AF___u5883_)
-----------------------------------------------------------

首先，将真实系统的环境设置为 “jail-friendly” 。 为了保持一致性，我们将父框称为 “host environment” ，将被 jail 的虚拟机称为 “jail environment” 。 由于 jail 是使用 IP 别名实现的，因此要做的第一件事就是禁用主机系统上的 IP 服务，该服务侦听服务的所有本地 IP 地址。 如果主机环境中存在绑定所有可用 IP 地址而不是特定 IP 地址的网络服务，则如果 jail 未绑定端口，它可能会为发送到 jail  IP 地址的请求提供服务。 这意味着将 inetd(8) 更改为仅侦听适当的 IP 地址，依此类推。 将以下内容添加到主机环境中的 /etc/rc.conf 中：

sendmail\_enable="NO" inetd\_flags="-wW -a 192.0.2.23" rpcbind\_enable="NO" 

在本例中， `192.0.2.23` 是主机系统的本地 IP 地址。 用完 inetd(8) 的守护进程可以很容易地配置为仅使用指定的主机 IP 地址。 其他守护进程需要手动配置——有些可以通过 rc.conf(5) 标志条目来实现；对于其他人来说，有必要修改每个应用程序的配置文件，或重新编译应用程序。 以下经常部署的服务必须修改其各自的配置文件，以限制应用程序侦听特定的 IP 地址：

要配置 sshd(8) ，需要修改 /etc/ssh/sshd\_config 。

要配置 sendmail(8) ，需要修改 /etc/mail/sendmail.cf 。

对于 named(8) ，需要修改 /etc/namedb/named.conf 。

此外，许多服务必须重新编译才能在主机环境中运行。 这包括大多数使用 rpc(3) 提供服务的应用程序，例如 rpcbind(8), nfsd(8) 和 mountd(8) 。 通常，无法指定绑定哪个 IP 地址的应用程序不应在主机环境中运行，除非它们还应为发送到 jail  IP 地址的请求提供服务。 尝试从主机环境提供 NFS 也可能会导致混淆，并且不能轻松地重新配置为仅使用特定的 IP，因为某些 NFS 服务是直接从内核托管的。 还应检查和配置在主机环境中运行的任何第三方网络软件，使其不会绑定所有 IP 地址，这将导致这些服务似乎也由 jail 环境提供。

一旦这些守护进程在主机环境中被禁用或修复后，最好重新启动以使所有守护进程处于已知状态，以减少以后混淆的可能性（例如，当您将邮件发送到 jail 时发现 sendmail 已关闭，邮件已投递到主机等）。

[配置 jail ](#__u914D___u7F6E___u76D1___u72F1_)
-----------------------------------------

首次启动任何 jail 时无需配置网络接口，以便您可以稍微清理一下并设置帐户。 与任何机器（虚拟机或非虚拟机）一样，您需要设置 root 密码、时区等。 仅当您打算在 jail 中运行完整的虚拟服务器时，其中一些步骤才适用；其他的既适用于限制特定应用程序，也适用于运行虚拟服务器。

在 jail 中启动一个 shell：

jail -c path=/data/jail/testjail mount.devfs \\ host.hostname=testhostname ip4.addr=192.0.2.100 \\ command=/bin/sh 

假设没有错误，您最终会在 jail 中看到一个 shell 提示符。 您现在可以运行 bsdconfig(8) 并进行安装后配置以设置各种配置选项，或者通过编辑 /etc/rc.conf 等手动执行这些操作。

*   配置 /etc/resolv.conf 以便在 jail 中的名称解析能够正常工作。
*   运行 newaliases(1) 以消除 sendmail(8) 警告。
*   设置一个root密码，可能与真实主机系统不同。
*   设置时区。
*   为 jail 环境中的用户添加帐户。
*   安装环境所需的任何软件包。

您可能还想执行任何特定于包的配置（Web 服务器、SSH 服务器等），修补 /etc/syslog.conf 以便它按照您的意愿进行记录等。 如果你没有使用虚拟服务器，你可能希望在宿主环境中修改 syslogd(8) 来监听 jail 环境中的 syslog 套接字；在此示例中，系统日志套接字将存储在 /data/jail/testjail/var/run/log 中。

退出shell， jail 将被关闭。

[启动 jail ](#__u542F___u52A8___u76D1___u72F1_)
-----------------------------------------

您现在已准备好重新启动 jail 并启动包含所有守护程序和其他程序的环境。 在 /etc/jail.conf-
中为 jail 创建一个条目：

testjail { path = /tmp/jail/testjail; mount.devfs; host.hostname = testhostname; ip4.addr = 192.0.2.100; interface = em0; exec.start = "/bin/sh /etc/rc"; exec.stop = "/bin/sh /etc/rc.shutdown jail"; } 

要启动虚拟服务器环境，运行 /etc/rc 以启动各种守护程序和服务，并运行 /etc/rc.shutdown-
以在移除 jail 时关闭它们。 如果您在 jail 中运行单个应用程序，请将用于启动应用程序的命令替换为 “/bin/sh /etc/rc” ；可能有一些脚本可用于彻底关闭应用程序，或者无需停止命令就足够了，让 `jail` 向应用程序发送 `SIGTERM` 。

运行以下命令启动 jail ：

jail -c testjail 

可能会产生一些警告；但是，它应该都能正常工作。 您应该能够使用 ps(1) 看到 inetd(8), syslogd(8) 和其他在 jail 中运行的进程，并且 ‘`J`’ 标志出现在被 jail 的进程旁边。 要查看 jails 的活动列表，请使用 jls(8) 。 如果在 jail 环境中启用了 sshd(8) ，您应该能够 ssh(1) 到 jail 环境的主机名或 IP 地址，并使用您之前创建的帐户登录。

可以在引导时启动 jail 。 有关详细信息，请参阅 rc.conf(5) 中的 “jail\_\*” 变量。

[管理 jail ](#__u7BA1___u7406___u76D1___u72F1_)
-----------------------------------------

正常的机器关闭命令，例如 halt(8), reboot(8) 和 shutdown(8) ，不能在jail 中成功使用。 要从 jail 中杀死所有进程，您可以使用以下命令之一，具体取决于您要完成的任务：

kill -TERM -1 kill -KILL -1 

这将向 jail 中的所有进程发送 `SIGTERM` 或 `SIGKILL` 信号——注意不要在主机环境中运行它！一旦 jail 的所有进程都死了，除非 jail 是使用 persist 参数创建的，否则 jail 将被删除。 根据 jail 的预期用途，您可能还想在 jail 中运行 /etc/rc.shutdown 。

要从外部关闭 jail ，只需使用 `jail` \-r 删除它，它将运行 exec.stop 指定的任何命令，然后发送 `SIGTERM` 并最终发送 `SIGKILL` 到任何剩余的 jail 进程。

/proc/pid/status 文件的最后一个字段包含进程运行所在的 jail 的名称，或 “`-`” 表示进程未在 jail 中运行。 ps(1) 命令还为 jail 中的进程显示一个 ‘`J`’ 标志。

您还可以根据其 jail  ID 列出/杀死进程。 要显示进程及其 jail  ID，请使用以下命令：

`ps ax -o pid,jid,args`

要显示并杀死 3 号 jail 中的进程，请使用以下命令：

pgrep -lfj 3 pkill -j 3 

或:

`killall -j 3`

[ jail 和文件系统](#__u76D1___u72F1___u548C___u6587___u4EF6___u7CFB___u7EDF_)
--------------------------------------------------------------------

除非文件系统被标记为 jail-friendly，jail 的 allow.mount 参数已设置，并且 jail 的 enforce\_statfs 参数低于 2，否则不可能在 jail 中 mount(8) 或 umount(8) 任何文件系统。

共享同一文件系统的多个 jail 可以相互影响。 例如，一个 jail 中的用户可以填满文件系统，而另一个 jail 中的进程没有空间。 尝试使用 quota(1) 来防止这种情况也不起作用，因为文件系统配额不知道 jail ，而只查看用户和组 ID。 这意味着两个 jail 中的相同用户 ID 共享一个文件系统配额。 每个 jail 都需要使用一个文件系统才能完成这项工作。

[Sysctl MIB 条目](#Sysctl_MIB___u6761___u76EE_)
---------------------------------------------

只读条目 security.jail.jailed 可用于确定进程是否在 jail 中运行（值为 1）或不（值为 0）。

变量 security.jail.max\_af\_ips 确定 jail 可能拥有的每个地址族的地址。默认值为 255。

一些 MIB 变量具有每个 jail 的设置。  jail 进程对这些变量的更改不会影响主机环境，只会影响 jail 环境。 这些变量是 kern.securelevel, security.bsd.suser\_enabled, kern.hostname, kern.domainname, kern.hostid 和 kern.hostuuid 。

[分级 jail ](#__u5206___u7EA7___u76D1___u72F1_)
-----------------------------------------

通过设置 jail 的 children.max 参数，jail 中的进程可以创建自己的jail。 这些子 jail 保存在一个层次结构中， jail 只能查看和/或修改他们创建的 jail （或这些 jail 的孩子）。 每个 jail 都有一个只读的 parent 参数，包含创建它的 jail 的 jid ; jid 为 0 表示 jail 是当前 jail 的子 jail （如果当前进程没有被 jail ，则它是顶级 jail ）。

被 jail 的进程不允许授予比它们自己更大的权限，例如，如果使用 allow.nomount 创建 jail ，则无法创建设置了 allow.mount 的 jail 。 同样，在儿童 jail 中也可能无法绕过 ip4.addr 和 securelevel 等限制。

如果设置了自己的 children.max 参数，则子 jail 可以反过来创建自己的子 jail （请记住，默认情况下它为零）。 这些 jail 对其父级和所有祖先都是可见的，并且可以由其修改。

 jail 名称反映了这种层次结构，全名是由点分隔的 MIB 类型字符串。 例如，如果一个基本系统进程创建了一个 jail  “foo” ，并且该 jail 下的一个进程创建了另一个 jail  “bar” ，那么第二个 jail 将被视为基本系统中的 “foo.bar” 尽管它只是被视为 jail  “bar” 中的任何进程的 “foo) 。” 另一方面，jid 存在于单个空间中，每个 jail 必须有一个唯一的 jid。

就像名字一样，儿童 jail 的 path 相对于其创建者自己的 path 出现。 这是由于在第一个 jail 的 chroot 环境中创建了子 jail 。

[参见](#__u53C2___u89C1_)
=======================

killall(1), lsvfs(1), newaliases(1), pgrep(1), pkill(1), ps(1), quota(1), jail\_set(2), vmm(4), devfs(5), fdescfs(5), jail.conf(5), linprocfs(5), linsysfs(5), procfs(5), rc.conf(5), sysctl.conf(5), bsdconfig(8), chroot(8), devfs(8), halt(8), ifconfig(8), inetd(8), jexec(8), jls(8), mount(8), named(8), reboot(8), rpcbind(8), sendmail(8), shutdown(8), sysctl(8), syslogd(8), umount(8)

[历史](#__u5386___u53F2_)
=======================

`jail` 实用程序出现在 FreeBSD 4.0 中。 FreeBSD 8.0 中引入了分层/可扩展 jail 。 FreeBSD 9.1 中引入了配置文件。

[作者](#__u4F5C___u8005_)
=======================

 jail 功能由 Poul-Henning Kamp 为 R&D Associates 编写，后者将其贡献给 FreeBSD 。

Robert Watson 编写了扩展文档，发现了一些错误，添加了一些新功能，并清理了用户级 jail 环境。

Bjoern A. Zeeb 基于最初由 Pawel Jakub Dawidek 为 IPv4 完成的补丁添加了对 IPv4 和 IPv6 的多 IP  jail 支持。

James Gritton 添加了可扩展的 jail 参数、分层 jail 和配置文件。

[缺陷](#__u7F3A___u9677_)
=======================

添加地址别名标志可能是一个好主意，这样监听所有 IP (`INADDR_ANY`) 的守护进程将不会绑定到该地址，这将有助于构建安全的主机环境，以便主机守护进程不会强加从 jail 内提供的服务. 目前，最简单的答案是最小化主机上提供的服务，可能将其限制为易于配置的 inetd(8) 提供的服务。

[笔记](#__u7B14___u8BB0_)
=======================

管理 jail 中可见的目录时应格外小心。 例如，如果被 jail 的进程将其当前工作目录设置为移出 jail 的 chroot 的目录，则该进程可能会访问 jail 外的文件空间。 建议始终将目录从 jail 中复制而不是移动。

此外， jail 外的非特权用户可以通过多种方式与 jail 内的特权用户合作，从而在主机环境中获得提升的特权。 通过确保主机环境中的非特权用户无法访问jail root，可以减轻大多数攻击。 无论如何，作为一般规则，不应授予对 jail 具有特权访问权限的不受信任的用户访问主机环境。

November 18, 2020

FreeBSD 13.1-RELEASE
