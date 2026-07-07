# jail(8)

`jail` — 管理系统 jail

## 名称

`jail`

## 概要

### 通过配置文件

`jail [-cm] [-Cdqv] [-f conf_file] [-p limit] [jail]`

`jail [-r] [-Cqv] [-f conf_file] [-p limit] [* | jail ...]`

### 不使用配置文件

`jail [-cm] [-dhilqv] [-J jid_file] [-u username] [-U username] param=value ... [command=command ...]`

`jail [-rR] [-qv] [* | jail ...]`

### 显示参数

`jail [-f conf_file] -e separator`

### 向后兼容

`jail [-dhilqv] [-J jid_file] [-u username] [-U username] [-n jailname] [-s securelevel] path hostname ip[,...] command ...`

## 描述

`jail` 工具用于创建新 jail、修改或删除现有 jail。它还能列出已配置的 jail 及其参数。jail（或称 "prison"）通过命令行参数或在 jail.conf(5) 文件中指定。

必须指定 `-c`、`-e`、`-m` 或 `-r` 中的至少一个选项。这些选项可以单独使用，也可以组合使用，以描述要执行的操作：

**`-c`** 创建新 jail。jail 的 `jid` 和 `name` 参数（如果在命令行上指定）不能引用已存在的 jail。

**`-e`** `separator` 列出所有已配置的非通配符 jail 及其参数。使用此选项时不执行 jail 的创建、修改或删除操作。`separator` 字符串用于分隔参数。使用 [jls(8)](jls.8.md) 工具可以列出正在运行的 jail。

**`-m`** 修改现有 jail。必须存在 `jid` 或 `name` 参数之一，并引用已存在的 jail。某些参数在正在运行的 jail 上无法更改。

**`-r`** 删除由 jid 或 name 指定的 jail。所有 jail 内的进程都会被杀死，且该 jail 的所有子 jail 也会被删除。

**`-rc`** 重启现有 jail。jail 会先被删除然后重新创建，就像依次运行 "`jail` `-r`" 和 "`jail` `-c`" 一样。

**`-cm`** 如果 jail 不存在则创建，如果存在则修改。

**`-mr`** 修改现有 jail。如果需要修改否则无法更改的参数，jail 可能会被重启。

**`-cmr`** 如果 jail 不存在则创建，如果存在则修改（并可能重启）。

其他可用选项：

**`-C`** 在已删除的 jail 之后进行清理，运行通常在 jail 删除之后执行的命令和操作。

**`-f`** `conf_file` 使用配置文件 `conf_file` 代替默认的 **/etc/jail.conf**。

**`-h`** 解析 `host.hostname` 参数（或 `hostname`），并将解析器返回的所有 IP 地址添加到该 jail 的地址列表中。这等效于 `ip_hostname` 参数。

**`-i`** 输出（仅输出）新创建 jail 的 jail 标识符。这隐含了 `-q` 选项。

**`-J`** `jid_file` 写入一个 `jid_file` 文件，其中包含用于启动 jail 的参数。

**`-l`** 在干净的环境中运行命令。此选项已弃用，等效于 exec.clean 参数。

**`-n`** `jailname` 设置 jail 的名称。此选项已弃用，等效于 `name` 参数。

**`-p`** `limit` 限制 `exec.*` 中可以同时运行的命令数量。

**`-q`** 抑制每次创建、修改或删除 jail 时打印的消息。仅打印错误消息。

**`-R`** `-r` 选项的变体，在不使用配置文件的情况下删除现有 jail。不会使用该 jail 的任何与删除相关的参数——jail 将被直接删除。

**`-s`** `securelevel` 将新创建 jail 内的 `kern.securelevel` MIB 条目设置为指定值。此选项已弃用，等效于 `securelevel` 参数。

**`-u`** `username` 主机环境中运行 jail 内命令时所使用的用户名。此选项已弃用，等效于 `exec.jail_user` 和 `exec.system_jail_user` 参数。

**`-U`** `username` jail 环境中运行 jail 内命令时所使用的用户名。此选项已弃用，等效于 `exec.jail_user` 参数。

**`-v`** 在每次操作时打印消息，例如运行命令和挂载文件系统。

**`-d`** 此选项已弃用，等效于 `allow.dying` 参数（该参数也已弃用）。它曾经允许对 `dying` 状态的 jail 进行更改。现在，当使用相同的 `jid` 或 `name` 创建新 jail 时，此类 jail 总是会被替换。

如果在选项之后没有给出参数，操作（删除除外）将对 jail.conf(5) 文件中指定的所有 jail 执行。单个 jail 名称参数将仅对指定的 jail 进行操作。`-r` 和 `-R` 选项也可以删除不在 jail.conf(5) 文件中但通过名称或 jid 指定的正在运行的 jail。

参数 "*" 是一个通配符，将对所有 jail 进行操作，无论它们是否出现在 jail.conf(5) 中；这是 `-r` 删除所有 jail 最可靠的方法。如果存在分层 jail，可以指定部分匹配的通配符定义。例如，参数 "foo.*" 将应用于名为 "foo.bar" 和 "foo.bar.baz" 的 jail。

也可以直接在命令行上以 "name=value" 形式通过参数指定 jail，忽略 jail.conf(5) 的内容。为了向后兼容，命令行也可以有四个不带名称的固定参数：`path`、`hostname`、`ip` 和 `command`。

### Jail 参数

jail.conf(5) 文件中或命令行上的参数通常采用 "name=value" 形式。某些参数是布尔值，没有值，仅通过名称设置，带或不带 "no" 前缀，例如 `persist` 或 `nopersist`。它们也可以接受值 "true" 和 "false"。其他参数可能有多个值，以逗号分隔列表的形式指定，或在配置文件中使用 "+=" 指定（详见 jail.conf(5)）。基于列表的参数也可以在命令行上多次指定，例如，"name=value1,value2" 和 "name=value1 name=value2" 对于此类参数是等效的。

`jail` 工具识别两类参数。一类是真正的 jail 参数，在创建 jail 时传递给内核，可以通过 [jls(8)](jls.8.md) 查看，并且（通常）可以用 "`jail` `-m`" 更改。另一类是仅由 `jail` 本身使用的伪参数。

jail 有一组核心参数，内核模块可以添加自己的 jail 参数。可以通过 "`sysctl` `-d` `security.jail.param`" 检索当前可用参数集合。任何未设置的参数都将获得默认值，通常基于当前环境。核心参数包括：

**`allow.set_hostname`** jail 的主机名可以通过 [hostname(1)](../man1/hostname.1.md) 或 sethostname(3) 更改。

**`allow.sysvipc`** jail 内的进程可以访问 System V IPC 原语。此参数已弃用，建议使用按模块的参数（见下文）。设置此参数时，等效于将 `sysvmsg`、`sysvsem` 和 `sysvshm` 都设置为 "inherit"。

**`allow.raw_sockets`** 允许 jail 的 root 用户创建原始套接字。设置此参数允许 [ping(8)](ping.8.md) 和 traceroute(8) 等工具在 jail 内运行。如果设置了此参数，源 IP 地址将被强制符合绑定到 jail 的 IP 地址，无论套接字上是否设置了 `IP_HDRINCL` 标志。由于原始套接字可用于配置和与各种网络子系统交互，在向不可信方提供 jail 特权访问时应格外谨慎。

**`allow.chflags`** 通常，jail 内的特权用户被 chflags(2) 视为非特权用户。设置此参数后，此类用户将被视为特权用户，并可以在 `kern.securelevel` 的常规约束下操纵系统文件标志。

**`allow.mount`** jail 内的特权用户将能够挂载和卸载标记为 jail 友好的文件系统类型。可以使用 [lsvfs(1)](../man1/lsvfs.1.md) 命令查找可从 jail 内挂载的文件系统类型。此权限仅在 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.devfs`** jail 内的特权用户将能够挂载和卸载 devfs 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。应通过 `devfs_ruleset` 选项从默认规则集进行限制。

**`allow.quotas`** jail 的 root 用户可以管理 jail 文件系统上的配额。这包括 jail 可能与其他 jail 或系统非 jail 部分共享的文件系统。

**`allow.read_msgbuf`** jail 内的用户可以读取内核消息缓冲区。如果 `security.bsd.unprivileged_read_msgbuf` MIB 条目为零，则此功能将仅限于 root 用户。

**`allow.socket_af`** jail 内的套接字通常仅限于 IPv4、IPv6、本地（UNIX）和 route。此参数允许访问尚未添加 jail 功能的其他协议栈。

**`allow.mlock`** 在 jail 内通常无法锁定或解锁内存中的物理页面。设置此参数后，用户可以在 `security.bsd.unprivileged_mlock` 和资源限制的约束下执行 mlock(2) 或 munlock(2)。

**`allow.nfsd`** mountd(8)、nfsd(8)、nfsuserd(8)、gssd(8) 和 rpc.tlsservd(8) 守护进程允许在正确配置的启用 vnet 的 jail 内运行。jail 的根目录必须是文件系统挂载点，且 `enforce_statfs` 不能设置为 0，以便 mountd(8) 能导出 jail 内可见的文件系统。如果需要由 [mount(8)](mount.8.md) 导出挂载在 jail 文件系统下的文件系统，`enforce_statfs` 必须设置为 1。如果仅导出 jail 的文件系统，设置为 2 即可。如果内核配置未包含 **NFSD** 选项，则必须在 jail 之外加载 `nfsd.ko`。这通常通过在 jail 之外的 [rc.conf(5)](../man5/rc.conf.5.md) 文件中将 "nfsd" 添加到 `kld_list` 来完成。类似地，如果要在 jail 中运行 gssd(8)，则需要在内核中指定 **KGSSAPI** 选项，或者在 jail 之外的 [rc.conf(5)](../man5/rc.conf.5.md) 文件中将 "kgssapi" 和 "kgssapi_krb5" 添加到 `kld_list`。

**`allow.reserved_ports`** jail 的 root 用户可以绑定低于 1024 的端口。

**`allow.unprivileged_parent_tampering`** jail 父级中的非特权进程可以篡改 jail 中相同 UID 的进程。这包括发信号、调试和 cpuset(1) 属于该 jail 的进程的能力。

**`allow.unprivileged_proc_debug`** jail 内的非特权进程可以使用调试功能。

**`allow.suser`** jail 的 `security.bsd.suser_enabled` sysctl 的值。如果其父系统已禁用超级用户，则超级用户将自动被禁用。超级用户默认启用。

**`allow.extattr`** 允许 jail 内的特权进程操纵系统命名空间中的文件系统扩展属性。

**`allow.adjtime`** 允许 jail 内的特权进程缓慢调整全局操作系统时间。例如通过 ntpd(8) 等工具。

**`allow.settime`** 允许 jail 内的特权进程设置全局操作系统日期和时间。例如通过 [date(1)](../man1/date.1.md) 等工具。此权限还包括 `allow.adjtime`。

**`allow.routing`** 允许非 VNET jail 内的特权进程修改系统路由表。

**`allow.setaudit`** 允许 jail 内的特权进程使用 setaudit(2) 和相关系统调用设置 [audit(4)](../man4/audit.4.md) 会话状态。例如，这对于允许 jail 内的 sshd(8) 为已认证会话设置审计用户 ID 很有用。但是，它赋予了 jail 内进程修改或禁用审计会话状态的能力，因此应谨慎配置。

**`jid`** jail 标识符。这将自动分配给新 jail（也可以显式设置），并可用于在后续修改或对于 [jls(8)](jls.8.md) 或 [jexec(8)](jexec.8.md) 等命令中标识 jail。

**`name`** jail 名称。这是标识 jail 的任意字符串（但不能包含 '.'）。与 `jid` 类似，它可以传递给后续的 `jail` 命令，或传递给 [jls(8)](jls.8.md) 或 [jexec(8)](jexec.8.md)。如果未提供 `name`，则假定默认值与 `jid` 相同。`name` 参数由 jail.conf(5) 文件格式隐含，使用配置文件时无需显式设置。

**`path`** 作为 jail 根目录的目录。在 jail 内运行的任何命令（无论是通过 `jail` 还是从 [jexec(8)](jexec.8.md)）都从此目录运行。

**`ip4.addr`** 分配给 jail 的 IPv4 地址列表。如果设置此参数，jail 将被限制为仅使用这些地址。任何使用其他地址的尝试都会失败，使用通配符地址的尝试会静默使用 jail 地址代替。对于 IPv4，当未绑定套接字的源地址选择无法找到更好的匹配时，将使用给定的第一个地址作为源地址。仅当所有 jail 都没有分配除这个单一重叠 IP 地址之外的其他地址时，才能启动具有相同 IP 地址的多个 jail。

**`ip4.saddrsel`** 一个布尔选项，用于更改前述行为并禁用 jail 的 IPv4 源地址选择，转而使用 jail 的主 IPv4 地址。所有 jail 默认启用源地址选择，父 jail 的 `ip4.nosaddrsel` 设置不会被任何子 jail 继承。

**`ip4`** 控制 IPv4 地址的可用性。可能的值为 "inherit"（允许不受限制地访问所有系统地址）、"new"（通过 `ip4.addr` 限制地址）和 "disable"（完全阻止 jail 使用 IPv4）。设置 `ip4.addr` 参数隐含值为 "new"。

**`ip6.addr`** , `ip6.saddrsel`, `ip6` 一组 jail 的 IPv6 选项，是上述 `ip4.addr`、`ip4.saddrsel` 和 `ip4` 的对应项。

**`vnet`** 创建具有自己虚拟网络栈的 jail，包括自己的网络接口、地址、路由表等。内核必须使用 **VIMAGE 选项** 编译才能使用此功能。可能的值为 "inherit"（使用系统网络栈，可能带有受限的 IP 地址）和 "new"（创建新的网络栈）。

**`host.hostname`** jail 的主机名。其他类似参数包括 `host.domainname`、`host.hostuuid` 和 `host.hostid`。

**`host`** 设置主机名和相关信息的来源。可能的值为 "inherit"（使用系统信息）和 "new"（jail 使用上述字段中的信息）。设置上述任何字段都隐含值为 "new"。

**`securelevel`** jail 的 `kern.securelevel` sysctl 的值。jail 的安全级别永远不会低于其父系统，但通过设置此参数可以使其更高。如果系统安全级别发生更改，任何 jail 安全级别都将至少同样安全。

**`devfs_ruleset`** 为在此 jail 中挂载 devfs 而强制执行的 devfs 规则集编号。值为零（默认）表示不强制执行规则集。后代 jail 继承父 jail 的 devfs 规则集强制执行。仅当 `allow.mount` 和 `allow.mount.devfs` 权限有效且 `enforce_statfs` 设置为低于 2 的值时，才能在 jail 内挂载 devfs。devfs 规则和规则集无法从 jail 内部查看或修改。注意：仅将 devfs 中适当的设备节点暴露给 jail 非常重要；在 jail 中访问磁盘设备可能允许 jail 内的进程通过修改 jail 外部的文件来绕过 jail 沙箱。有关如何使用 devfs 规则限制对每个 jail 的 devfs 中条目的访问的信息，请参见 devfs(8)。**/etc/defaults/devfs.rules** 中的规则集 #4 提供了一个简单的 jail devfs 规则集。

**`children.max`** 此 jail（或此 jail 下的其他 jail）允许创建的子 jail 数量。此限制默认为零，表示不允许 jail 创建子 jail。有关更多信息，请参见"分层 Jail"部分。

**`children.cur`** 此 jail 的后代数量，包括其自身的子 jail 和在它们之下创建的任何 jail。

**`enforce_statfs`** 此参数决定 jail 内的进程能够获取关于挂载点的信息。它影响以下系统调用的行为：statfs(2)、fstatfs(2)、getfsstat(2) 和 fhstatfs(2)（以及类似的兼容性系统调用）。设置为 0 时，所有挂载点都可无限制地访问。设置为 1 时，仅可见 jail 的 chroot 目录下的挂载点。此外，jail 的 chroot 目录路径会从其路径名前面移除。设置为 2（默认）时，上述系统调用只能在 jail 的 chroot 目录所在的挂载点上操作。

**`persist`** 设置此布尔参数允许 jail 在没有任何进程的情况下存在。通常，命令作为 jail 创建的一部分运行，然后 jail 在其最后一个进程退出时被销毁。新 jail 必须设置 `persist` 参数或 `exec.start` 或 `command` 伪参数之一。

**`cpuset.id`** 与此 jail 关联的 cpuset ID（只读）。

**`dying`** 如果 jail 正在关闭过程中，则为 true（只读）。

**`mac.label`** 与此 jail 关联的 mac(3) 标签。注意，可能需要在 mac.conf(5) 中配置 "jail" 条目才能检索 MAC 标签。

**`parent`** 此 jail 父级的 `jid`，如果这是顶级 jail 则为零（只读）。

**`osrelease`** jail 的 `kern.osrelease` sysctl 和 uname -r 的字符串。

**`osreldate`** jail 的 `kern.osreldate` 和 uname -K 的数字。

**`meta`** , `env` 与 jail 关联的任意字符串。其最大缓冲区大小由全局 `security.jail.meta_maxbufsize` sysctl 控制，该 sysctl 只能由非 jail 的 root 用户调整。`meta` 对 jail 隐藏，而 `env` 可通过 `security.jail.env` sysctl 读取。每个缓冲区可以视为一组 key=value 字符串。要添加或替换特定键，必须使用 `meta.keyname=value` 或 `env.keyname=value` 参数表示法。`meta.keyname=` 或 `env.keyname=` 将值重置为空字符串，而不带等号的 `meta.keyname` 或 `env.keyname` 表示法会移除给定的键。同样，使用 [jls(8)](jls.8.md) 等命令读取 jail 参数时，使用相同的 `meta.keyname` 或 `env.keyname` 表示法查询特定键。可以通过单个命令查询或修改多个键。

**`allow.*`** jail 环境的某些限制可以按 jail 设置。除 `allow.set_hostname` 和 `allow.reserved_ports` 外，这些布尔参数默认关闭。

内核模块可以添加自己的参数，这些参数仅在模块加载时存在。它们通常位于以模块命名的参数下，值为 "inherit"（赋予 jail 完全使用该模块的能力）、"new"（以某种模块特定的方式封装 jail）和 "disable"（使该模块对 jail 不可用）。还可能有其他参数定义模块内的 jail 行为。模块特定的参数包括：

**`allow.mount.fdescfs`** jail 内的特权用户将能够挂载和卸载 fdescfs 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.fusefs`** jail 内的特权用户将能够挂载和卸载基于 fuse 的文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.nullfs`** jail 内的特权用户将能够挂载和卸载 nullfs 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.procfs`** jail 内的特权用户将能够挂载和卸载 procfs 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.linprocfs`** jail 内的特权用户将能够挂载和卸载 linprocfs 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.linsysfs`** jail 内的特权用户将能够挂载和卸载 linsysfs 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.tmpfs`** jail 内的特权用户将能够挂载和卸载 tmpfs 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。

**`allow.mount.zfs`** jail 内的特权用户将能够挂载和卸载 ZFS 文件系统。此权限仅在同时启用 `allow.mount` 且 `enforce_statfs` 设置为低于 2 的值时有效。有关如何配置 ZFS 文件系统以从 jail 内操作的信息，请参见 zfs-jail(8)。

**`allow.vmm`** jail 可以访问 [vmm(4)](../man4/vmm.4.md)。此标志仅在加载 [vmm(4)](../man4/vmm.4.md) 内核模块时可用。

**`allow.vmm_ppt`** jail 可以为 [vmm(4)](../man4/vmm.4.md) 虚拟机客户机配置 PCI 直通设备。这允许 jail 内的特权用户操纵由 `ppt` 驱动程序声明的物理设备，因此不得在不可信的 jail 中配置。此标志仅在加载 [vmm(4)](../man4/vmm.4.md) 内核模块时可用。

**`linux`** 决定 jail 的 Linux 模拟环境如何呈现。值为 "inherit" 将保持相同的环境，"new" 将给 jail 自己的环境（在创建 jail 时仍然最初继承）。

**`linux.osname`** , `linux.osrelease`, `linux.oss_version` 与此 jail 关联的 Linux 操作系统名称、版本和 OSS 版本。

**`sysvmsg`** 允许访问 SYSV IPC 消息原语。如果设置为 "inherit"，系统上的所有 IPC 对象对此 jail 可见，无论它们是由 jail 本身、基本系统还是其他 jail 创建的。如果设置为 "new"，jail 将拥有自己的键命名空间，并且只能看到它创建的对象；系统（或父 jail）可以访问 jail 的对象，但不能访问其键。如果设置为 "disable"，jail 无法执行任何与 sysvmsg 相关的系统调用。

**`sysvsem`** , **`sysvshm`** 以与 `sysvmsg` 相同的方式允许访问 SYSV IPC 信号量和共享内存原语。

**`zfs.mount_snapshot`** 设置为 1 时，jail 内的用户可以访问文件系统 `.zfs` 目录下 ZFS 快照的内容。如果设置了 `allow.mount.zfs`，还可以挂载快照。

还有不传递给内核的伪参数，由 `jail` 用于设置 jail 环境，通常通过在创建或删除 jail 时运行指定的命令。`exec.*` 命令参数是在系统或 jail 环境中运行的 [sh(1)](../man1/sh.1.md) 命令行。它们可以接受多个值，从而按顺序运行指定的命令。所有命令都必须成功（返回零退出状态），否则 jail 将不会被创建或删除（视情况而定）。

以下变量被添加到环境中：

**`JID`** `jid`，即 jail 标识符。

**`JNAME`** jail 的 `name`。

**`JPATH`** jail 的 `path`。

伪参数包括：

**`exec.prepare`** 在系统环境中运行以准备创建 jail 的命令。这些命令在分配 IP 地址和挂载文件系统之前执行，因此可用于在 jail 文件系统不存在时创建新的 jail 文件系统。

**`exec.prestart`** 在创建 jail 之前在系统环境中运行的命令。

**`exec.created`** 在 jail 创建之后、在 jail 内执行命令（或服务）之前，在系统环境中运行的命令。

**`exec.start`** 创建 jail 时在 jail 环境中运行的命令。通常运行的命令是 "sh /etc/rc"。

**`command`** 在命令行上直接指定 jail 时使用的 `exec.start` 的同义词。与其他值为单个字符串的参数不同，`command` 使用 `jail` 命令行的其余部分作为其自己的参数。

**`exec.poststart`** 在 jail 创建之后以及任何 `exec.start` 命令完成后，在系统环境中运行的命令。

**`exec.prestop`** 在删除 jail 之前在系统环境中运行的命令。

**`exec.stop`** 在删除 jail 之前以及任何 `exec.prestop` 命令完成后，在 jail 环境中运行的命令。通常运行的命令是 "sh /etc/rc.shutdown jail"。

**`exec.poststop`** 在 jail 删除之后在系统环境中运行的命令。

**`exec.release`** 在所有其他操作完成后在系统环境中运行的命令。这些命令在卸载文件系统和删除 IP 地址之后执行，因此可用于在不再需要 jail 文件系统时将其删除。

**`exec.clean`** 在干净的环境中运行命令。环境被丢弃，仅保留 `HOME`、`SHELL`、`TERM` 和 `USER`。`HOME` 和 `SHELL` 设置为目标登录的默认值。`USER` 设置为目标登录。`TERM` 从当前环境导入。`PATH` 设置为 "/bin:/usr/bin"。目标登录的登录类能力数据库中的环境变量也会被设置。`JID`、`JNAME` 和 `JPATH` 不会被设置。如果指定了用户（如 `exec.jail_user`），命令将从该（可能是 jail 内的）用户的目录运行。

**`exec.jail_user`** 在 jail 环境中运行命令时使用的用户。默认以当前用户身份运行命令。

**`exec.system_jail_user`** 此布尔选项在系统 [passwd(5)](../man5/passwd.5.md) 文件中查找 `exec.jail_user`，而不是在 jail 的文件中查找。

**`exec.system_user`** 在系统环境中运行命令时使用的用户。默认以当前用户身份运行命令。

**`exec.timeout`** 等待命令完成的最长时间（以秒为单位）。如果命令在此超时后仍在运行，jail 将不会被创建或删除（视情况而定）。

**`exec.consolelog`** 用于将命令输出（stdout 和 stderr）重定向到的文件。

**`exec.fib`** 在 jail 内运行命令时设置的 FIB（路由表）。

**`stop.timeout`** 在向 jail 的进程发送 `SIGTERM` 信号后等待它们退出的最长时间（在 `exec.stop` 命令完成后发生）。在此秒数过后，jail 将被删除，这将杀死所有剩余的进程。如果设置为零，则不发送 `SIGTERM`，jail 会立即删除。默认为 10 秒。

**`interface`** 用于将 jail 的 IP 地址（`ip4.addr` 和 `ip6.addr`）添加到的网络接口。在创建 jail 之前，每个地址的别名将添加到该接口，在删除 jail 之后从接口移除。

**`ip4.addr`** 除了传递给内核的 IP 地址外，还可以指定接口、网络掩码和附加参数（由 [ifconfig(8)](ifconfig.8.md) 支持），格式为 "`interface`|`ip-address`/`netmask param ...`"。如果在 IP 地址之前给出接口，则该地址的别名将添加到该接口，与 `interface` 参数相同。如果在 IP 地址之后给出点分四元组或 CIDR 形式的网络掩码，则在添加 IP 别名时将使用它。如果指定了附加参数，则在添加 IP 别名时也将使用它们。

**`ip6.addr`** 除了传递给内核的 IP 地址外，还可以指定接口、前缀和附加参数（由 [ifconfig(8)](ifconfig.8.md) 支持），格式为 "`interface`|`ip-address`/`prefix param ...`"。

**`vnet.interface`** 在创建启用 vnet 的 jail 之后提供给它的网络接口的逗号分隔列表。当 jail 被删除时，这些接口将自动释放。

**`zfs.dataset`** 附加到 jail 的 ZFS 数据集列表。这需要设置 `allow.mount.zfs`。有关如何配置 ZFS 数据集以从 jail 内操作的信息，请参见 zfs-jail(8)。

**`ip_hostname`** 解析 `host.hostname` 参数，并将解析器返回的所有 IP 地址添加到此 jail 的地址列表（`ip4.addr` 或 `ip6.addr`）中。这可能会影响 jail 发出 IPv4 连接的默认地址选择。解析器为每个地址族返回的第一个地址将用作主地址。

**`mount`** 在创建 jail 之前挂载（在删除之后卸载）的文件系统，以单行 [fstab(5)](../man5/fstab.5.md) 格式给出。

**`mount.fstab`** 包含在创建 jail 之前要挂载的文件系统的 [fstab(5)](../man5/fstab.5.md) 格式文件。

**`mount.devfs`** 在 chroot 的 **/dev** 目录上挂载 [devfs(4)](../man4/devfs.4.md) 文件系统，并应用 `devfs_ruleset` 参数中的规则集（或默认的规则集 4：devfsrules_jail）以限制 jail 内可见的设备。

**`mount.fdescfs`** 在 chroot 的 **/dev/fd** 目录上挂载 [fdescfs(4)](../man4/fdescfs.4.md) 文件系统。

**`mount.procfs`** 在 chroot 的 **/proc** 目录上挂载 [procfs(4)](../man4/procfs.4.md) 文件系统。

**`allow.dying`** 此参数已弃用且无效。它曾经允许对 `dying` 状态的 jail 进行更改。现在，当使用相同的 `jid` 或 `name` 创建新 jail 时，此类 jail 总是会被替换。

**`depend`** 指定此 jail 依赖的一个或多个 jail。当要创建此 jail 时，它依赖的任何 jail 必须已经存在。如果不存在，它们将自动创建，直到最后一个 `exec.poststart` 命令完成，然后才会采取任何操作来创建此 jail。当删除 jail 时情况相反：此 jail 将被删除，直到最后一个 `exec.poststop` 命令，然后才会停止它依赖的任何 jail。

## 实例

jail 通常采用两种理念之一进行设置：要么用于约束特定应用程序（可能以特权运行），要么用于创建运行各种守护进程和服务的"虚拟系统映像"。在两种情况下，都需要相当完整的 FreeBSD 文件系统安装，以提供必要的命令行工具、守护进程、库、应用程序配置文件等。但是，对于虚拟服务器配置，需要相当多的额外工作来替换"引导"过程。本手册页记录了支持上述任一步骤所需的配置步骤，但可能需要根据本地需求细化配置步骤。

### 从源代码设置 Jail 目录树

要设置包含完整 FreeBSD 发行版的 jail 目录树，可以使用以下 [sh(1)](../man1/sh.1.md) 命令脚本：

```sh
D=/here/is/the/jail
cd /usr/src
mkdir -p $D
make world DESTDIR=$D
make distribution DESTDIR=$D
```

### 从发行版文件设置 Jail 目录树

要设置包含完整 FreeBSD 发行版的 jail 目录树，可以使用以下 [sh(1)](../man1/sh.1.md) 命令脚本：

```sh
D=/here/is/the/jail
mkdir -p $D
tar -xf /usr/freebsd-dist/base.txz -C $D --unlink
```

### 从系统包设置 Jail 目录树

要设置包含可选 FreeBSD 发行版的 jail 目录树（使用包技术预览），可以使用以下命令：

```sh
bsdinstall jail /here/is/the/jail
```

在许多情况下，这些示例会在 jail 中放置远超所需的内容。在另一个极端情况下，jail 可能只包含一个文件：要在 jail 中运行的可执行文件。

我们建议进行实验，并提醒注意：从"胖"jail 开始并移除内容直到它停止工作，比从"瘦"jail 开始并添加内容直到它工作要容易得多。

### 设置 Jail

按照"设置 Jail 目录树"中所述构建 jail 目录树。在本示例中，我们假设你将其构建在 **/data/jail/testjail** 中，用于名为 "testjail" 的 jail。请根据需要用你自己的目录、IP 地址和主机名替换下面的内容。

### 设置主机环境

首先，将真实系统的环境设置为"jail 友好"。为保持一致，我们将父机称为"主机环境"，将被 jail 的虚拟机称为"jail 环境"。由于 jail 使用 IP 别名实现，首先要做的事情之一是禁用主机系统上侦听所有本地 IP 地址的服务。如果主机环境中存在绑定所有可用 IP 地址而非特定 IP 地址的网络服务，当 jail 未绑定端口时，它可能会服务于发送到 jail IP 地址的请求。这意味着要将 [inetd(8)](inetd.8.md) 更改为仅侦听适当的 IP 地址等等。在主机环境中将以下内容添加到 **/etc/rc.conf**：

```sh
sendmail_enable="NO"
inetd_flags="-wW -a 192.0.2.23"
rpcbind_enable="NO"
```

在本示例中，`192.0.2.23` 是主机系统的本机 IP 地址。从 [inetd(8)](inetd.8.md) 运行的守护进程可以轻松配置为仅使用指定的主机 IP 地址。其他守护进程需要手动配置——对于某些守护进程，可以通过 [rc.conf(5)](../man5/rc.conf.5.md) 标志条目实现；对于其他守护进程，需要修改每个应用程序的配置文件或重新编译应用程序。以下经常部署的服务必须修改其各自的配置文件以限制应用程序仅侦听特定 IP 地址：

要配置 sshd(8)，需要修改 **/etc/ssh/sshd_config**。

要配置 sendmail(8)，需要修改 **/etc/mail/sendmail.cf**。

此外，许多服务必须重新编译才能在主机环境中运行。这包括大多数使用 rpc(3) 提供服务的应用程序，例如 rpcbind(8)、nfsd(8) 和 mountd(8)。通常，无法指定绑定哪个 IP 地址的应用程序不应在主机环境中运行，除非它们也应服务于发送到 jail IP 地址的请求。尝试从主机环境提供 NFS 服务也可能造成混乱，并且无法轻松重新配置为仅使用特定 IP，因为某些 NFS 服务直接由内核承载。主机环境中运行的任何第三方网络软件也应进行检查和配置，使其不绑定所有 IP 地址，否则这些服务看起来也会像是由 jail 环境提供的。

在主机环境中禁用或修复这些守护进程后，最好重新启动，以便所有守护进程都处于已知状态，以减少以后出现混乱的可能性（例如，当向 jail 发送邮件时发现其 sendmail 已关闭，邮件被投递到主机等）。

### 配置 Jail

首次启动任何 jail 时不配置网络接口，以便你可以稍作清理并设置账户。与任何机器（虚拟或非虚拟）一样，你需要设置 root 密码、时区等。其中一些步骤仅在打算在 jail 内运行完整虚拟服务器时才适用；其他步骤既适用于约束特定应用程序，也适用于运行虚拟服务器。

在 jail 中启动 shell：

```sh
jail -c path=/data/jail/testjail mount.devfs \
	host.hostname=testhostname ip4.addr=192.0.2.100 \
	command=/bin/sh
```

假设没有错误，你将在 jail 内获得一个 shell 提示符。现在你可以运行 [bsdconfig(8)](bsdconfig.8.md) 进行安装后配置以设置各种配置选项，或通过编辑 **/etc/rc.conf** 等手动执行这些操作。

- 配置 **/etc/resolv.conf**，以便 jail 内的名称解析正常工作。
- 运行 [newaliases(1)](../man1/newaliases.1.md) 以抑制 sendmail(8) 警告。
- 设置 root 密码，可能与真实主机系统不同。
- 设置时区。
- 为 jail 环境中的用户添加账户。
- 安装环境所需的任何包。

你可能还想执行任何特定于包的配置（Web 服务器、SSH 服务器等），修改 **/etc/syslog.conf** 使其按你的意愿记录日志等。如果你不使用虚拟服务器，你可能希望修改主机环境中的 syslogd(8) 以侦听 jail 环境中的 syslog 套接字；在本示例中，syslog 套接字将存储在 **/data/jail/testjail/var/run/log** 中。

退出 shell，jail 将被关闭。

### 启动 Jail

现在你已准备好重启 jail 并启动包含所有守护进程和其他程序的环境。在 **/etc/jail.conf** 中为 jail 创建一个条目：

```sh
testjail {
	path = /tmp/jail/testjail;
	mount.devfs;
	host.hostname = testhostname;
	ip4.addr = 192.0.2.100;
	interface = em0;
	exec.start = "/bin/sh /etc/rc";
	exec.stop = "/bin/sh /etc/rc.shutdown jail";
}
```

要启动虚拟服务器环境，运行 **/etc/rc** 以启动各种守护进程和服务，运行 **/etc/rc.shutdown** 在 jail 删除时关闭它们。如果你在 jail 中运行单个应用程序，请用用于启动应用程序的命令替换 "/bin/sh /etc/rc"；可能有某些脚本可用于干净地关闭应用程序，或者不带停止命令也可能足够，让 `jail` 向应用程序发送 `SIGTERM`。

通过运行以下命令启动 jail：

```sh
jail -c testjail
```

可能会产生一些警告；但是，它应该都能正常工作。你应该能够使用 [ps(1)](../man1/ps.1.md) 看到 [inetd(8)](inetd.8.md)、syslogd(8) 和其他进程在 jail 内运行，并且 jail 内进程旁边会出现 `J` 标志。要查看活动 jail 列表，请使用 [jls(8)](jls.8.md)。如果在 jail 环境中启用了 sshd(8)，你应该能够通过 [ssh(1)](../man1/ssh.1.md) 连接到 jail 环境的主机名或 IP 地址，并使用先前创建的账户登录。

可以在引导时启动 jail。有关更多信息，请参阅 [rc.conf(5)](../man5/rc.conf.5.md) 中的 "jail_*" 变量。

### 管理 Jail

普通的机器关机命令，如 [halt(8)](reboot.8.md)、[reboot(8)](reboot.8.md) 和 [shutdown(8)](shutdown.8.md)，无法在 jail 内成功使用。要从 jail 内杀死所有进程，你可以使用以下命令之一，具体取决于你要完成的目标：

```sh
kill -TERM -1
kill -KILL -1
```

这会向 jail 中的所有进程发送 `SIGTERM` 或 `SIGKILL` 信号——小心不要从主机环境运行此命令！一旦 jail 的所有进程都已死亡，除非 jail 是使用 `persist` 参数创建的，否则 jail 将被删除。根据 jail 的预期用途，你可能还想从 jail 内运行 **/etc/rc.shutdown**。

要从外部关闭 jail，只需使用以下命令删除它：

```sh
jail -r
```

这将运行由 `exec.stop` 指定的任何命令，然后向任何剩余的 jail 进程发送 `SIGTERM`，最终发送 `SIGKILL`。

**/proc/`pid`/status** 文件包含作为其最后一个字段的进程运行的 jail 名称，或 "`-`" 表示该进程未在 jail 内运行。[ps(1)](../man1/ps.1.md) 命令还为 jail 中的进程显示 `J` 标志。

你还可以根据 jail ID 列出/杀死进程。要显示进程及其 jail ID，请使用以下命令：

```sh
ps ax -o pid,jid,args
```

要显示然后杀死 jail 编号为 3 的进程，请使用以下命令：

```sh
pgrep -lfj 3
pkill -j 3
```

或：

```sh
killall -j 3
```

### Jail 和文件系统

除非文件系统被标记为 jail 友好、jail 的 `allow.mount` 参数已设置且 jail 的 `enforce_statfs` 参数低于 2，否则无法在 jail 内 [mount(8)](mount.8.md) 或 [umount(8)](umount.8.md) 任何文件系统。

共享相同文件系统的多个 jail 可能会相互影响。例如，一个 jail 中的用户可能会填满文件系统，使另一个 jail 中的进程没有空间。尝试使用 quota(1) 来防止这种情况也无效，因为文件系统配额不感知 jail，仅查看用户和组 ID。这意味着两个 jail 中相同的用户 ID 共享单个文件系统配额。要使此功能生效，需要为每个 jail 使用一个文件系统。

### Sysctl MIB 条目

只读条目 `security.jail.jailed` 可用于确定进程是否在 jail 内运行（值为一）或不在（值为零）。

变量 `security.jail.jail_max_af_ips` 决定每个地址族一个 jail 可以拥有多少地址。默认为 255。

某些 MIB 变量具有按 jail 的设置。jail 内进程对这些变量的更改不会影响主机环境，仅影响 jail 环境。这些变量包括 `kern.securelevel`、`security.bsd.suser_enabled`、`kern.hostname`、`kern.domainname`、`kern.hostid` 和 `kern.hostuuid`。

### 分层 Jail

通过设置 jail 的 `children.max` 参数，jail 内的进程可能能够创建自己的 jail。这些子 jail 保持在层次结构中，jail 只能查看和/或修改它们创建的 jail（或这些 jail 的子 jail）。每个 jail 都有一个只读的 `parent` 参数，包含创建它的 jail 的 `jid`；`jid` 为 0 表示该 jail 是当前 jail 的子级（如果当前进程未被 jail，则是顶级 jail）。

jail 内的进程不允许授予比它们自己拥有的更大的权限，例如，如果使用 `allow.nomount` 创建 jail，则它无法创建设置了 `allow.mount` 的 jail。类似地，`ip4.addr` 和 `securelevel` 等限制不能在子 jail 中绕过。

如果子 jail 自身的 `children.max` 参数已设置（记住默认为零），则子 jail 可以依次创建自己的子 jail。这些 jail 对其父级和所有祖先可见并可由其修改。

jail 名称反映此层次结构，完整名称是以点分隔的 MIB 类型字符串。例如，如果基本系统进程创建 jail "foo"，而该 jail 下的进程创建另一个 jail "bar"，则第二个 jail 在基本系统中将显示为 "foo.bar"（尽管对于 jail "foo" 内的任何进程仅显示为 "bar"）。另一方面，jid 存在于单个空间中，每个 jail 必须具有唯一的 jid。

与名称一样，子 jail 的 `path` 显示为相对于其创建者自身 `path` 的路径。这是因为子 jail 是在第一个 jail 的 chroot 环境中创建的。

## 参见

[date(1)](../man1/date.1.md), [killall(1)](../man1/killall.1.md), [lsvfs(1)](../man1/lsvfs.1.md), [newaliases(1)](../man1/newaliases.1.md), pgrep(1), pkill(1), [ps(1)](../man1/ps.1.md), quota(1), adjtime(2), clock_settime(2), jail_set(2), ntp_adjtime(2), mac(3), [devfs(4)](../man4/devfs.4.md), [fdescfs(4)](../man4/fdescfs.4.md), [linprocfs(4)](../man4/linprocfs.4.md), [linsysfs(4)](../man4/linsysfs.4.md), [procfs(4)](../man4/procfs.4.md), [vmm(4)](../man4/vmm.4.md), jail.conf(5), mac.conf(5), [rc.conf(5)](../man5/rc.conf.5.md), [sysctl.conf(5)](../man5/sysctl.conf.5.md), [bsdconfig(8)](bsdconfig.8.md), [chroot(8)](chroot.8.md), devfs(8), [halt(8)](reboot.8.md), [ifconfig(8)](ifconfig.8.md), [inetd(8)](inetd.8.md), [jexec(8)](jexec.8.md), [jls(8)](jls.8.md), [mount(8)](mount.8.md), mountd(8), nfsd(8), ntpd(8), [reboot(8)](reboot.8.md), rpcbind(8), sendmail(8), [shutdown(8)](shutdown.8.md), [sysctl(8)](sysctl.8.md), syslogd(8), [umount(8)](umount.8.md), zfs-jail(8), [extattr(9)](../man9/extattr.9.md)

## 历史

`jail` 工具出现在 FreeBSD 4.0 中。分层/可扩展 jail 在 FreeBSD 8.0 中引入。配置文件在 FreeBSD 9.1 中引入。

## 作者

jail 功能由 Poul-Henning Kamp 为 R&D Associates 编写，并贡献给 FreeBSD。

Robert Watson 编写了扩展文档，发现了一些错误，添加了一些新功能，并清理了用户空间 jail 环境。

Bjoern A. Zeeb 基于 Pawel Jakub Dawidek 最初为 IPv4 编写的补丁，添加了对 IPv4 和 IPv6 的多 IP jail 支持。

James Gritton 添加了可扩展 jail 参数、分层 jail 和配置文件。

## 缺陷

添加地址别名标志可能是个好主意，这样侦听所有 IP（`INADDR_ANY`）的守护进程就不会绑定到该地址，这将有助于构建安全的主机环境，使主机守护进程不会侵入 jail 内提供的服务。目前，最简单的答案是最小化主机上提供的服务，可能仅限于从 [inetd(8)](inetd.8.md) 提供的服务，这易于配置。

## 注释

管理 jail 内可见的目录时应格外小心。例如，如果 jail 内的进程将其当前工作目录设置为移出 jail chroot 的目录，则该进程可能会获得对 jail 外部文件空间的访问权限。建议始终从 jail 中复制目录，而不是移动目录。

此外，jail 外部的非特权用户可以通过多种方式与 jail 内的特权用户合作，从而在主机环境中获得提升的权限。大多数此类攻击可以通过确保 jail 根目录对主机环境中的非特权用户不可访问来缓解。无论如何，作为一般规则，不应给予具有 jail 特权访问权限的不可信用户对主机环境的访问权限。
