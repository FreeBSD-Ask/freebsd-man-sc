# rc.conf(5)

`rc.conf` — 系统配置信息

## 名称

`rc.conf`

## 描述

`rc.conf` 文件包含有关本地主机名、任何潜在网络接口的配置细节以及系统初始引导时应启动哪些服务的描述性信息。在新安装的系统中，`rc.conf` 文件通常由系统安装实用程序初始化。

`rc.conf` 的目的不是直接运行命令或执行系统启动操作。相反，它被 **/etc** 中的各种通用启动脚本包含，这些脚本根据其中找到的设置来有条件地执行内部操作。

**/etc/rc.conf** 文件从 **/etc/defaults/rc.conf** 文件中包含，后者指定了所有可用选项的默认设置。只有当系统管理员希望覆盖这些默认值时，才需要在 **/etc/rc.conf** 中指定选项。**/etc/defaults/vendor.conf** 文件允许供应商覆盖 FreeBSD 的默认值。出于历史原因，**/etc/rc.conf.local** 文件用于覆盖 **/etc/rc.conf** 中的设置。

sysrc(8) 命令提供了修改系统配置文件的脚本接口。

除了 **/etc/rc.conf.local** 之外，你还可以在 **/etc/rc.conf.d** 目录或 <`dir`>`/rc.conf.d` 目录（其中 <`dir`> 是 `local_startup` 中指定的每个条目，但去掉末尾的 `/rc.d`）中为每个 [rc(8)](../man8/rc.8.md) 脚本放置较小的配置文件，这些文件将被 `load_rc_config` 函数包含。对于 Jail 配置，你可以使用 **/etc/rc.conf.d/jail** 文件来存储特定于 Jail 的配置选项。如果 `local_startup` 包含 **/usr/local/etc/rc.d** 和 **/opt/conf**，则会加载 **/usr/local/etc/rc.conf.d/jail** 和 **/opt/conf/rc.conf.d/jail**。如果 <`dir`>`/rc.conf.d/`<`name`> 是一个目录，则该目录中的所有文件都将被加载。另请参阅下文的 `rc_conf_files` 变量。

选项使用 [sh(1)](../man1/sh.1.md) 语法的 “`name``=``value`” 赋值来设置。以下列表提供了可在 `rc.conf` 文件中设置的每个变量的名称和简短描述：

```sh
${argument}_cmd
```

**`open`** 不受限制的 IP 访问
**`closed`** 除通过 “`lo0`” 外，禁用所有 IP 服务
**`client`** 工作站的基本保护
**`workstation`** 使用状态防火墙的工作站基本保护
**`simple`** LAN 的基本保护。

```sh
ipfilter_enable="YES"
ipnat_enable="YES"
ipmon_enable="YES"
ipfs_enable="YES"
```

```sh
options IPFILTER
options IPFILTER_LOG
options IPFILTER_DEFAULT_BLOCK
```

```sh
/var/log/ipflog  640  10  100  *  Z  /var/run/ipmon.pid
```

```sh
pf_enable="YES"
```

```sh
device pf
```

```sh
pf_fallback_rules="
	block drop log all
	pass in quick on em0"
```

"RFC 1323"。

```sh
ifconfig_em0="inet 192.0.2.1/24 up"
```

```sh
ifconfig_em0_alias0="inet 127.0.0.253/32"
ifconfig_em0_alias1="inet 127.0.0.254/32"
```

```sh
netif_ipexpand_max="4096"
```

```sh
ifconfig_em0_alias2="inet 192.0.2.129/27"
ifconfig_em0_alias3="inet 192.0.2.1-5/28"
```

```sh
ifconfig_em0_alias0="inet 127.0.0.251/32"
ifconfig_em0_alias1="inet 127.0.0.252/32"
ifconfig_em0_alias2="inet 127.0.0.253/32"
ifconfig_em0_alias4="inet 127.0.0.254/32"
```

```sh
ifconfig_em0_aliases="\
	inet 127.0.0.251/32 \
	inet 127.0.0.252/32 \
	inet 127.0.0.253/32 \
	inet 127.0.0.254/32"
```

```sh
vlans_em0="101"
ifconfig_em0_101="inet 192.0.2.1/24"
```

```sh
vlans_em0="myvlan"
create_args_myvlan="vlan 102"
```

```sh
ifconfig_em0="DHCP"
```

```sh
wlans_ath0="wlan0"
ifconfig_wlan0="DHCP WPA mode 11b"
```

```sh
ifconfig_em0_name="net0"
ifconfig_net0="inet 192.0.2.1/24"
```

```sh
ifconfig_em0_ipv6="inet6 2001:db8:1::1 prefixlen 64"
ifconfig_em0_alias0="inet6 2001:db8:2::1 prefixlen 64"
```

"RFC 4862"。

"RFC 4862"，第 5.3 节。

```sh
ifconfig_em0_ipv6="inet6 auto_linklocal"
```

```sh
ifconfig_em0_ipv6="inet6 fe80::1 prefixlen 64"
```

```sh
ipv6_prefix_em0="2001:db8:1:0 2001:db8:2:0"
```

```sh
ifconfig_em0_alias0="inet6 2001:db8:1:: eui64 prefixlen 64"
ifconfig_em0_alias1="inet6 2001:db8:1:: prefixlen 64 anycast"
ifconfig_em0_alias2="inet6 2001:db8:2:: eui64 prefixlen 64"
ifconfig_em0_alias3="inet6 2001:db8:2:: prefixlen 64 anycast"
```

```sh
gif_interfaces="gif0 gif1"
gifconfig_gif0="100.64.0.1 100.64.0.2"
ifconfig_gif0="inet 10.0.0.1/30 10.0.0.2"
gifconfig_gif1="inet6 2a00::1 2a01::1"
ifconfig_gif1="inet 10.1.0.1/30 10.1.0.2"
```

```sh
0 4 * * * root /etc/rc.d/bgfsck forcestart
```

```sh
static_arp_pairs="gw"
static_arp_gw="192.168.1.1 00:01:02:03:04:05"
```

```sh
static_ndp_pairs="gw"
static_ndp_gw="2001:db8:3::1 00:01:02:03:04:05"
```

```sh
static_routes="ext mcast:gif0 gif0local:gif0"
route_ext="-net 10.0.0.0/24 -gateway 192.168.0.1"
route_mcast="-net 224.0.0.0/4 -iface gif0"
route_gif0local="-host 169.254.1.1 -iface lo0"
```

**`microsoft`** Microsoft 鼠标（串口）
**`intellimouse`** Microsoft IntelliMouse（串口）
**`mousesystems`** Mouse Systems Corp. 鼠标（串口）
**`mmseries`** MM Series 鼠标（串口）
**`logitech`** Logitech 鼠标（串口）
**`busmouse`** 总线鼠标
**`mouseman`** Logitech MouseMan 和 TrackMan（串口）
**`glidepoint`** ALPS GlidePoint（串口）
**`thinkingmouse`** Kensington ThinkingMouse（串口）
**`ps/2`** PS/2 鼠标
**`mmhittab`** MM HitTablet（串口）
**`x10mouseremote`** X10 MouseRemote（串口）
**`versapad`** Interlink VersaPad（串口）

**`path`** 从 `jail_`<`jname`>`_rootdir` 设置

**`host.hostname`** 从 `jail_`<`jname`>`_hostname` 设置

**`exec.consolelog`** 从 `jail_`<`jname`>`_consolelog` 设置。默认值为 **/var/log/jail_**<`jname`>`_console.log`。

**`interface`** 从 `jail_`<`jname`>`_interface` 设置。

**`vnet.interface`** 从 `jail_`<`jname`>`_vnet_interface` 设置。这表示将启用 `vnet` 参数，且不能与 `jail_`<`jname`>`_interface`、`jail_`<`jname`>`_ip` 和/或 `jail_`<`jname`>`_ip_multi`<`n`> 同时指定。

**`fstab`** 从 `jail_`<`jname`>`_fstab` 设置

**`mount`** 从 `jail_`<`jname`>`_procfs_enable` 设置。

**`exec.fib`** 从 `jail_`<`jname`>`_fib` 设置

**`exec.start`** 从 `jail_`<`jname`>`_exec_start` 设置。该参数名在较早的版本中为 `command`。

**`exec.prestart`** 从 `jail_`<`jname`>`_exec_prestart` 设置

**`exec.poststart`** 从 `jail_`<`jname`>`_exec_poststart` 设置

**`exec.stop`** 从 `jail_`<`jname`>`_exec_stop` 设置

**`exec.prestop`** 从 `jail_`<`jname`>`_exec_prestop` 设置

**`exec.poststop`** 从 `jail_`<`jname`>`_exec_poststop` 设置

**`ip4.addr`** 当 `jail_`<`jname`>`_ip` 或 `jail_`<`jname`>`_ip_multi`<`n`> 包含 IPv4 地址时设置

**`ip6.addr`** 当 `jail_`<`jname`>`_ip` 或 `jail_`<`jname`>`_ip_multi`<`n`> 包含 IPv6 地址时设置

**`allow.mount`** 从 `jail_`<`jname`>`_mount_enable` 设置

**`mount.devfs`** 从 `jail_`<`jname`>`_devfs_enable` 设置

**`devfs_ruleset`** 从 `jail_`<`jname`>`_devfs_ruleset` 设置。必须为整数，而非字符串。

**`mount.fdescfs`** 从 `jail_`<`jname`>`_fdescfs_enable` 设置

**`allow.set_hostname`** 从 `jail_`<`jname`>`_set_hostname_allow` 设置

**`allow.rawsocket`** 从 `jail_`<`jname`>`_socket_unixiproute_only` 设置

**`allow.sysvipc`** 从 `jail_`<`jname`>`_sysvipc_allow` 设置

```sh
mdconfig_md0_cmd="tar xfzC /var/file.tgz e${_mp}"
```

```sh
autobridge_interfaces="bridge0"
autobridge_bridge0="tap* dc0 vlan[345]"
```

```sh
virtual_oss_configs="foo bar"
```

**`rc_debug`** (`bool`) 如果设为 “`YES`”，启用 rc 脚本的调试消息输出。此变量在编辑或集成新脚本时有助于诊断错误。注意，这会在终端和 syslog(3) 中产生大量输出。

**`rc_info`** (`bool`) 如果设为 “`NO`”，禁用 rc 脚本的信息消息。当发生不够严重、不值得警告或错误的条件时，会显示信息消息。

**`rc_startmsgs`** (`bool`) 如果设为 “`YES`”，在使用 faststart 时（例如引导时）显示 “Starting foo:”。

**`early_late_divider`** (`str`) 用作引导过程 “早期” 和 “晚期” 阶段之间分隔符的脚本名称。早期阶段应包含挂载磁盘（本地或远程）所需的所有服务，以便晚期阶段可以包含 `local_startup` 变量中所列目录中的脚本（见下文）。因此，此值的两个可能候选者是：典型系统使用 `mountcritlocal`，如果系统需要挂载远程文件系统才能访问 `local_startup` 目录（例如 **/usr/local** 通过 NFS 挂载时），则使用 `mountcritremote`。对于 [jail(8)](../man8/jail.8.md) 中的 `rc.conf`，`NETWORKING` 可能是合适的值。更改此值时应格外小心，在更改之前应确保有足够的措施从失败的引导中恢复（例如与机器的物理接触或可靠的远程控制台访问）。

**`always_force_depends`** (`bool`) 各种 `rc.d` 脚本使用 force_depend 函数检查所需服务是否已在运行，并在必要时启动它们。默认情况下，在引导期间，如果所需服务在 **/etc/rc.conf[.local]** 中已启用，则跳过此检查。设置此选项将在引导时跳过该检查，并始终测试服务是否实际在运行。如果启用了使用 force_depend 检查的服务，启用此选项可能会增加引导时间。

**<`name`>`_audit_user`** (`str`) 用作服务的 [audit(4)](../man4/audit.4.md) 用户的用户名或 UID。在此系统组下运行 chroot 服务。默认情况下，当非特权用户使用 sudo 或 doas 等实用程序重启服务时，服务的审计会话将指向该非特权用户，这可能是不希望发生的。在这种情况下，可以使用此变量通过 setaudit(8) 覆盖审计用户。

**<`name`>`_chroot`** (`str`) 在运行服务之前 [chroot(8)](../man8/chroot.8.md) 到此目录。

**<`name`>`_cpuset`** (`str`) 运行服务的 CPU 列表。通过 `-l` 标志传递给 cpuset(1)。

**<`name`>`_fib`** (`int`) 运行服务的 setfib(1) 值。

**<`name`>`_group`** (`str`) 与 <`name`>`_user` 设置不同，如果服务未 chroot，此设置无效。

**<`name`>`_limits`** (`str`) 使用 [limits(1)](../man1/limits.1.md) 应用于服务的资源限制。默认情况下，资源限制基于 <`name`>`_login_class` 中定义的登录类。

**<`name`>`_login_class`** (`str`) 与 <`name`>`_limits` 一起使用的登录类。默认为 “`daemon`”。

**<`name`>`_nice`** (`int`) 运行服务的 [nice(1)](../man1/nice.1.md) 值。

**<`name`>`_oomprotect`** (`str`) 使用 protect(1) 防止服务在交换空间耗尽时被杀死。使用 “`YES`” 仅保护服务本身，使用 “`ALL`” 保护服务及其所有子进程。请注意，重新定义（参见 [rc.subr(8)](../man8/rc.subr.8.md)）的 rc 脚本（如 PostgreSQL）不会继承 OOM killer 保护。此变量对在 [jail(8)](../man8/jail.8.md) 中运行的服务无效。

**<`name`>`_setup`** (`str`) 在启动实际服务命令之前立即运行指定的设置脚本。适用于自动生成配置文件。

**<`name`>`_umask`** (`int`) 使用此 umask(1) 值运行服务。

**<`name`>`_user`** (`str`) 在此用户账户下运行服务。

**<`name`>`_svcj`** (`bool`) 如果设为 “`YES`”，根据 <`name`>`_svcj_options` 自动将服务放入继承文件系统和其他 Jail 属性的 Jail 中。

**<`name`>`_svcj_ipaddrs`** (`str`) 服务 Jail 允许使用的 IP 地址列表。如果未指定，且 Jail 中启用了网络，则服务 Jail 允许使用所有已分配的 IP 地址。

**<`name`>`_svcj_options`** (`str`) 服务的 Jail 属性列表。有效属性列表请参见 SERVICE JAILS 部分。

**`apm_enable`** (`bool`) 如果设为 “`YES`”，使用 apm(8) 命令启用高级电源管理支持。

**`apmd_enable`** (`bool`) 运行 apmd(8) 以从用户空间处理 APM 事件。这也会启用 APM 支持。

**`apmd_flags`** (`str`) 如果 `apmd_enable` 设为 “`YES`”，这些是传递给 apmd(8) 守护进程的标志。

**`devd_enable`** (`bool`) 运行 devd(8) 以处理来自内核的设备添加、删除或未知事件。

**`ddb_enable`** (`bool`) 运行 ddb(8) 在引导时安装 [ddb(4)](../man4/ddb.4.md) 脚本。

**`ddb_config`** (`str`) ddb(8) 的配置文件。默认为 **/etc/ddb.conf**。

**`devmatch_enable`** (`bool`) 如果设为 “`NO`”，禁用 [devmatch(8)](../man8/devmatch.8.md) 自动加载内核模块。

**`devmatch_blocklist`** (`str`) 由 [devmatch(8)](../man8/devmatch.8.md) 忽略的内核模块的空白分隔列表。此外，[kenv(1)](../man1/kenv.1.md) 的 `devmatch_blocklist` 会追加到此变量，以允许从引导加载器禁用 [devmatch(8)](../man8/devmatch.8.md) 加载的模块。

**`devmatch_blacklist`** (`str`) 此变量已弃用。请改用 `devmatch_blocklist`。由 [devmatch(8)](../man8/devmatch.8.md) 忽略的内核模块的空白分隔列表。

**`kld_list`** (`str`) 在本地磁盘挂载后立即加载的内核模块的空白分隔列表，不带 `.ko` 扩展名或路径。

**`kldxref_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 可在引导时使用 [kldxref(8)](../man8/kldxref.8.md) 自动重建 `linker.hints` 文件。

**`kldxref_clobber`** (`bool`) 默认设为 “`NO`”。如果 `kldxref_enable` 为真，设为 “`YES`” 将在引导时覆盖现有的 `linker.hints` 文件。否则，仅生成缺失的 `linker.hints` 文件。

**`kldxref_module_path`** (`str`) 默认为空。以分号（`;`）分隔的包含 [kld(4)](../man4/kld.4.md) 模块的路径列表。如果为空，则使用 `kern.module_path` [sysctl(8)](../man8/sysctl.8.md) 的内容。

**`powerd_enable`** (`bool`) 如果设为 “`YES`”，使用 [powerd(8)](../man8/powerd.8.md) 守护进程启用系统电源控制功能。

**`powerd_flags`** (`str`) 如果 `powerd_enable` 设为 “`YES`”，这些是传递给 [powerd(8)](../man8/powerd.8.md) 守护进程的标志。

**`svcj_all_enable`** 启用所有未明确排除的服务的自动 Jail 化。更多信息请参见 SERVICE JAILS 部分。

**`tmpmfs`** 控制 **/tmp** 内存文件系统的创建。设为 “`YES`” 时始终创建，设为 “`NO`” 时从不创建。设为其他值时，如果 **/tmp** 不可写，则创建内存文件系统。

**`tmpsize`** 控制所创建的 **/tmp** 内存文件系统的大小。

**`tmpmfs_flags`** 创建 **/tmp** 内存文件系统时传递给 mdmfs(8) 实用程序的额外选项。默认为 “`-S`”，这会禁止在 **/tmp** 上使用 softupdates，以便在文件截断或删除后立即释放文件系统空间。关于可在 `tmpmfs_flags` 中使用的其他选项，请参见 mdmfs(8)。

**`varmfs`** 控制 **/var** 内存文件系统的创建。设为 “`YES`” 时始终创建，设为 “`NO`” 时从不创建。设为其他值时，如果 **/var** 不可写，则创建内存文件系统。

**`varsize`** 控制所创建的 **/var** 内存文件系统的大小。

**`varmfs_flags`** 创建 **/var** 内存文件系统时传递给 mdmfs(8) 实用程序的额外选项。默认为 “`-S`”，这会禁止在 **/var** 上使用 softupdates，以便在文件截断或删除后立即释放文件系统空间。关于可在 `varmfs_flags` 中使用的其他选项，请参见 mdmfs(8)。

**`populate_var`** 控制 **/var** 文件系统的自动填充。设为 “`YES`” 时始终执行，设为 “`NO`” 时从不执行。设为其他值时，如果 **/var** 不可写，则创建内存文件系统。请注意，此过程在 **/usr** 挂载之前需要访问 **/usr** 中的某些命令（在正常系统上）。

**`cleanvar_enable`** (`bool`) 清理 **/var** 目录。

**`var_run_enable`** (`bool`) 设为 “YES” 以启用在关机时将 **/var/run** 目录结构保存到 mtree 文件，并在引导时重新加载 **/var/run** 目录结构。

**`var_run_autosave`** (`bool`) 在某些情况下，可能不希望在关机时保存 **/var/run**。设为 "NO" 时，**/var/run** 在重启时加载，但在关机时不保存。通常在这种情况下，会执行 `service var_run save` 一次以保存 **/var/run** 目录结构的副本，以便在后续所有重启时重新加载。

**`var_run_mtree`** (`str`) 保存 **/var/run** mtree 的位置。默认位置为 **/var/db/mtree/BSD.var-run.mtree**。

**`local_startup`** (`str`) 搜索启动脚本文件的目录列表。

**`script_name_sep`** (`str`) 用于将启动脚本文件列表拆分为单个文件名的字段分隔符。默认为空格。除非启动脚本的文件名包含空格，否则无需更改此项。

**`hostapd_enable`** (`bool`) 设为 “`YES`” 以在系统引导时启动 hostapd(8)。

**`hostname`** (`str`) 此主机在网络上的完全限定域名（FQDN）。即使没有网络连接，也应将其设置为有意义的值。如果使用 dhclient(8) 通过 DHCP 设置主机名，此变量应设为空字符串。在 [jail(8)](../man8/jail.8.md) 中，主机名通常已设置，此变量可以省略。如果系统完成引导后此值仍未设置，控制台登录将显示默认主机名 “Amnesiac”。

**`nisdomainname`** (`str`) 此主机的 NIS 域名，如果不使用 NIS 则为 “`NO`”。

**`hostid_enable`** (`bool`) 如果设为 “`NO`”，禁用系统引导和关机时 `hostid` 和 `machine-id` 文件的生成或保存。

**`hostid_file`** (`str`) `hostid` 文件的路径，默认为 **/etc/hostid**。

**`hostid_uuidgen_flags`** (`str`) 生成软件主机 UUID 时传递给 [uuidgen(1)](../man1/uuidgen.1.md) 的标志。仅当系统无法确定硬件 UUID 时使用。默认设为 “`-r`”。

**`machine_id_file`** (`str`) `machine-id` 文件的路径，默认为 **/etc/machine-id**。

**`dhclient_program`** (`str`) DHCP 客户端程序的路径，默认为 **/sbin/dhclient**。

**`dhclient_flags`** (`str`) 传递给 DHCP 客户端程序的额外标志。可用命令行选项的说明请参见 dhclient(8) 手册页。

**`dhclient_flags_`**<`iface`> 仅传递给在 `iface` 上运行的 DHCP 客户端程序的额外标志。指定时，此变量覆盖 `dhclient_flags`。

**`background_dhclient`** (`bool`) 设为 “`YES`” 以在后台启动 DHCP 客户端。这可能会对依赖正常网络的应用程序造成问题，但在许多情况下会提供更快的启动速度。

**`background_dhclient_`**<`iface`> 指定时，此变量仅覆盖接口 `iface` 的 `background_dhclient` 变量。

**`dhclient_arpwait`** (`bool`) 设为 “`NO`” 以阻止 dhclient(8) 等待 ARP 解析，从而加快系统引导。在 DHCP 服务器确定知道地址是否可用的情况下可以这样做。

**`synchronous_dhclient`** (`bool`) 设为 “`YES`” 以在启动时同步启动 dhclient(8)。通过将 `ifconfig_`<`interface`> 变量中的 “`DHCP`” 关键字替换为 “`SYNCDHCP`” 或 “`NOSYNCDHCP`”，可以在每个接口上覆盖此行为。

**`defaultroute_delay`** (`int`) 设为正值时，在启动时配置 DHCP 接口后最多等待此时间（秒），以给接口时间接收租约。

**`firewall_enable`** (`bool`) 设为 “`YES`” 以在启动时加载防火墙规则。如果内核未构建 `options IPFIREWALL`，将加载 `ipfw.ko` 内核模块。另请参见 `ipfilter_enable`。

**`firewall_script`** (`str`) 此变量指定要运行的防火墙脚本的完整路径。默认为 **/etc/rc.firewall**。

**`firewall_type`** (`str`) 从 **/etc/rc.firewall** 中的选择项命名防火墙类型，或指定包含本地防火墙规则集的文件。**/etc/rc.firewall** 中的有效选择项为：如果指定了文件名，必须给出完整路径。大多数预定义规则集定义了额外的配置变量。这些在 **/etc/rc.firewall** 中有文档说明。

**`firewall_quiet`** (`bool`) 设为 “`YES`” 以在引导期间禁用控制台上的防火墙规则显示。

**`firewall_logging`** (`bool`) 设为 “`YES`” 以启用防火墙事件日志记录。这等同于 `IPFIREWALL_VERBOSE` 内核选项。

**`firewall_logif`** (`bool`) 设为 “`YES`” 以创建用于日志记录的伪接口 `ipfw0`。更多详情请参见 [ipfw(8)](../man8/ipfw.8.md) 手册页。

**`firewall_flags`** (`str`) 如果 `firewall_type` 指定了文件名，则传递给 [ipfw(8)](../man8/ipfw.8.md) 的标志。

**`firewall_coscripts`** (`str`) 防火墙启动/停止后运行的可执行文件和/或 rc 脚本列表。默认为空。

**`firewall_nat_enable`** (`bool`) [ipfw(8)](../man8/ipfw.8.md) 中 `natd_enable` 的等价物。如果 `firewall_enable` 也设为 “`YES`”，将此设为 “`YES`” 会自动加载 [ipfw(8)](../man8/ipfw.8.md) NAT 内核模块。

**`firewall_nat_interface`** (`str`) [ipfw(8)](../man8/ipfw.8.md) 中 `natd_interface` 的等价物。这是内核 NAT 应运行的公共接口或 IP 地址的名称。

**`firewall_nat_flags`** (`str`) 内核 NAT 的额外配置参数应放在此处。

**`firewall_nat64_enable`** (`bool`) 如果 `firewall_enable` 也设为 “`YES`”，将此设为 “`YES`” 会自动加载 [ipfw(8)](../man8/ipfw.8.md) NAT64 内核模块。

**`firewall_nptv6_enable`** (`bool`) 如果 `firewall_enable` 也设为 “`YES`”，将此设为 “`YES`” 会自动加载 [ipfw(8)](../man8/ipfw.8.md) NPTv6 内核模块。

**`firewall_pmod_enable`** (`bool`) 如果 `firewall_enable` 也设为 “`YES`”，将此设为 “`YES`” 会自动加载 [ipfw(8)](../man8/ipfw.8.md) pmod 内核模块。

**`dummynet_enable`** (`bool`) 如果 `firewall_enable` 也设为 “`YES`”，将此设为 “`YES`” 会自动加载 [dummynet(4)](../man4/dummynet.4.md) 模块。

**`ipfw_netflow_enable`** (`bool`) 将此设为 “`YES`” 会通过 [ng_netflow(4)](../man4/ng_netflow.4.md) 启用 netflow 日志记录。默认情况下会插入一条 ipfw 规则，所有数据包都通过 ngtee 命令复制，并使用协议版本 5 将 netflow 数据包发送到 127.0.0.1 的 netflow 端口。

**`ipfw_netflow_hook`** (`int`) netflow 钩子名，必须为数字（默认 `9995`）。

**`ipfw_netflow_rule`** (`int`) ipfw 规则号（默认 `1000`）。

**`ipfw_netflow_ip`** (`str`) 接收 netflow 数据的目标服务器 IP（默认 `127.0.0.1`）。

**`ipfw_netflow_port`** (`int`) 接收 netflow 数据的目标服务器端口（默认 `9995`）。

**`ipfw_netflow_version`** (`int`) 不设置则使用 netflow 协议版本 5，设为 9 则使用版本 9。

**`ipfw_netflow_fib`** (`int`) 仅匹配 FIB `ipfw_netflow_fib` 中的数据包（默认未定义，表示所有 FIB）。

**`natd_program`** (`str`) [natd(8)](../man8/natd.8.md) 的路径。

**`natd_enable`** (`bool`) 设为 “`YES`” 以启用 [natd(8)](../man8/natd.8.md)。`firewall_enable` 也必须设为 “`YES`”，且内核中必须启用 [divert(4)](../man4/divert.4.md) 套接字。如果内核未构建 `options IPDIVERT`，将加载 `ipdivert.ko` 内核模块。

**`natd_interface`** (`str`) 这是 [natd(8)](../man8/natd.8.md) 应运行的公共接口的名称。接口可以以接口名或 IP 地址形式给出。

**`natd_flags`** (`str`) 额外的 [natd(8)](../man8/natd.8.md) 标志应放在此处。`-n` 或 `-a` 标志会自动添加，并将上述 `natd_interface` 作为参数。

**`ipfilter_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 启用 ipf(8) 数据包过滤。典型用法需要放入 **/etc/rc.conf** 并适当编辑 **/etc/ipf.rules** 和 **/etc/ipnat.rules**。注意，`ipfilter_enable` 和 `ipnat_enable` 可以独立启用。`ipmon_enable` 和 `ipfs_enable` 都要求至少启用 `ipfilter_enable` 和 `ipnat_enable` 中的一个。在内核配置文件中包含相应选项也是个好主意。

**`ipfilter_program`** (`str`) ipf(8) 的路径（默认 **/sbin/ipf**）。

**`ipfilter_rules`** (`str`) 默认设为 **/etc/ipf.rules**。此变量包含过滤规则定义文件的名称。该文件需要可读以便 ipf(8) 命令执行。

**`ipfilter_flags`** (`str`) 默认为空。此变量包含传递给 ipf(8) 程序的标志。

**`ipnat_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 以启用 ipnat(8) 网络地址转换。详细讨论请参见 `ipfilter_enable`。

**`ipnat_program`** (`str`) ipnat(8) 的路径（默认 **/sbin/ipnat**）。

**`ipnat_rules`** (`str`) 默认设为 **/etc/ipnat.rules**。此变量包含保存网络地址转换定义的文件名。该文件需要可读以便 ipnat(8) 命令执行。

**`ipnat_flags`** (`str`) 默认为空。此变量包含传递给 ipnat(8) 程序的标志。

**`ipmon_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 以启用 ipmon(8) 监控（记录 ipf(8) 和 ipnat(8) 事件）。设置此变量也需要设置 `ipfilter_enable` 或 `ipnat_enable`。详细讨论请参见 `ipfilter_enable`。

**`ipmon_program`** (`str`) ipmon(8) 的路径（默认 **/sbin/ipmon**）。

**`ipmon_flags`** (`str`) 默认设为 “`-Ds`”。此变量包含传递给 ipmon(8) 程序的标志。另一个典型示例是 “`-D` `/var/log/ipflog`”，让 ipmon(8) 直接记录到文件，绕过 syslogd(8)。在这种情况下，请确保像这样调整 **/etc/newsyslog.conf**：

**`ipfs_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 以启用 ipfs(8) 在关机时保存过滤器和 NAT 状态表，并在启动时重新加载。设置此变量也需要将 `ipfilter_enable` 或 `ipnat_enable` 设为 “`YES`”。详细讨论请参见 `ipfilter_enable`。注意，如果 `kern_securelevel` 设为 3，则不能使用 `ipfs_enable`，因为提高的安全级别会阻止 ipfs(8) 在关机时保存状态表。

**`ipfs_program`** (`str`) ipfs(8) 的路径（默认 **/sbin/ipfs**）。

**`ipfs_flags`** (`str`) 默认为空。此变量包含传递给 ipfs(8) 程序的标志。

**`pf_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 启用 [pf(4)](../man4/pf.4.md) 数据包过滤。典型用法需要放入 **/etc/rc.conf** 并适当编辑 **/etc/pf.conf**。在内核中添加 [pf(4)](../man4/pf.4.md) 支持的构建，否则将加载内核模块。

**`pf_rules`** (`str`) [pf(4)](../man4/pf.4.md) 规则集配置文件的路径（默认 **/etc/pf.conf**）。

**`pf_program`** (`str`) pfctl(8) 的路径（默认 **/sbin/pfctl**）。

**`pf_flags`** (`str`) 如果 `pf_enable` 设为 “`YES`”，加载规则集时这些标志会传递给 pfctl(8) 程序。

**`pf_fallback_rules_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 以在加载 `pf_rules` 中的规则集出现问题时，启用加载 `pf_fallback_rules_file` 或 `pf_fallback_rules`。

**`pf_fallback_rules_file`** (`str`) 加载 `pf_rules` 中的规则集失败时要加载的 pf 规则集路径（默认 **/etc/pf-fallback.conf**）。

**`pf_fallback_rules`** (`str`) 加载 `pf_rules` 中的规则集失败且未找到 `pf_fallback_rules_file` 时要加载的 pf 规则集。可以按如下方式设置多条规则：默认后备规则为 “block drop log all”

**`pflog_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 启用 pflogd(8)，它会记录来自 [pf(4)](../man4/pf.4.md) 数据包过滤器的数据包。

**`pflog_logfile`** (`str`) 如果 `pflog_enable` 设为 “`YES`”，这控制 pflogd(8) 存储日志文件的位置（默认 **/var/log/pflog**）。检查 **/etc/newsyslog.conf** 以调整此日志文件的轮转。

**`pflog_program`** (`str`) pflogd(8) 的路径（默认 **/sbin/pflogd**）。

**`pflog_flags`** (`str`) 默认为空。此变量包含传递给 pflogd(8) 程序的额外标志。

**`pflog_instances`** (`str`) 如果需要记录到多个 [pflog(4)](../man4/pflog.4.md) 接口，`pflog_instances` 设为系统引导时应启动的 pflogd(8) 实例列表。如果设置了 `pflog_instances`，对于列表中每个空白分隔的 `element`，假定存在 <`element`>`_dev` 和 <`element`>`_logfile` 元素。<`element`>`_dev` 必须包含由指定 pflogd(8) 实例监视的 [pflog(4)](../man4/pflog.4.md) 接口。<`element`>`_logfile` 必须包含该 pflogd(8) 实例将使用的日志文件名。

**`ftpproxy_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 启用 [ftp-proxy(8)](../man8/ftp-proxy.8.md)，它支持 [pf(4)](../man4/pf.4.md) 数据包过滤器转换 ftp 连接。

**`ftpproxy_flags`** (`str`) 默认为空。此变量包含传递给 [ftp-proxy(8)](../man8/ftp-proxy.8.md) 程序的额外标志。

**`ftpproxy_instances`** (`str`) 默认为空。如果在引导时需要多个 [ftp-proxy(8)](../man8/ftp-proxy.8.md) 实例，`ftpproxy_instances` 应包含空白分隔的实例名列表。对于列表中的每个 `element`，应定义一个名为 <`element`>`_flags` 的变量，包含要传递给 [ftp-proxy(8)](../man8/ftp-proxy.8.md) 实例的命令行标志。

**`pfsync_enable`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 启用通过 [pfsync(4)](../man4/pfsync.4.md) 向网络上其他主机公开 [pf(4)](../man4/pf.4.md) 状态更改。此时还必须设置 `pfsync_syncdev` 变量。

**`pfsync_syncdev`** (`str`) 默认为空。此变量指定 [pfsync(4)](../man4/pfsync.4.md) 应通过其操作的网络接口名。如果 `pfsync_enable` 设为 “`YES`”，则必须相应设置。

**`pfsync_syncpeer`** (`str`) 默认为空。此变量是可选的。默认情况下，状态更改消息使用 IP 多播数据包在同步接口上发送。协议为 IP 协议 240（PFSYNC），使用的多播组为 224.0.0.240。使用 `pfsync_syncpeer` 选项指定对端地址时，该对端地址用作 pfsync 流量的目标，然后可以使用 [ipsec(4)](../man4/ipsec.4.md) 保护该流量。关于在 [pfsync(4)](../man4/pfsync.4.md) 接口上使用 [ipsec(4)](../man4/ipsec.4.md) 的更多详情，请参见 [pfsync(4)](../man4/pfsync.4.md) 手册页。

**`pfsync_ifconfig`** (`str`) 默认为空。此变量可包含传递给用于设置 [pfsync(4)](../man4/pfsync.4.md) 的 [ifconfig(8)](../man8/ifconfig.8.md) 命令的额外选项。

**`tcp_extensions`** (`bool`) 默认设为 “`YES`”。设为 “`NO`” 禁用某些 TCP 选项（如所述）。设为 “`NO`” 可能有助于解决连接随机挂起或其他异常行为的问题。已知某些网络设备在这些选项方面存在缺陷。

**`log_in_vain`** (`int`) 默认设为 0。[sysctl(8)](../man8/sysctl.8.md) 变量 `net.inet.tcp.log_in_vain` 和 `net.inet.udp.log_in_vain`（如 [tcp(4)](../man4/tcp.4.md) 和 [udp(4)](../man4/udp.4.md) 中所述）将设为给定值。

**`tcp_keepalive`** (`bool`) 默认设为 “`YES`”。设为 “`NO`” 将禁用对空闲 TCP 连接的探测，以验证对端是否仍然存活且可达。

**`tcp_drop_synfin`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 将使内核忽略同时设置了 SYN 和 FIN 标志的 TCP 帧。这可以防止操作系统指纹识别，但可能破坏某些合法应用程序。

**`icmp_drop_redirect`** (`bool`) 默认设为 “`AUTO`”。如果启用了动态路由守护进程，此设置等同于 “`YES`”，因为重定向处理可能对大型路由表造成性能问题。如果未启用此类服务，此设置的行为类似于 “`NO`”。设为 “`YES`” 将使内核忽略 ICMP REDIRECT 数据包。设为 “`NO`” 将使内核处理 ICMP REDIRECT 数据包。更多信息请参见 [icmp(4)](../man4/icmp.4.md)。

**`icmp_log_redirect`** (`bool`) 默认设为 “`NO`”。设为 “`YES`” 将使内核记录 ICMP REDIRECT 数据包。注意，日志消息不受速率限制，因此此选项仅应用于网络故障排除。更多信息请参见 [icmp(4)](../man4/icmp.4.md)。

**`icmp_bmcastecho`** (`bool`) 设为 “`YES`” 以响应广播或多播 ICMP ping 数据包。更多信息请参见 [icmp(4)](../man4/icmp.4.md)。

**`ip_portrange_first`** (`int`) 如果未设为 “`NO`”，这是默认端口范围中的第一个端口。更多信息请参见 [ip(4)](../man4/ip.4.md)。

**`ip_portrange_last`** (`int`) 如果未设为 “`NO`”，这是默认端口范围中的最后一个端口。更多信息请参见 [ip(4)](../man4/ip.4.md)。

**`network_interfaces`** (`str`) 设为要在本主机上配置的网络接口列表，或 “`AUTO`”（默认）表示所有当前接口。将 `network_interfaces` 变量设为默认值以外的值已弃用。管理员希望存储配置但不在引导时启动的接口，应在其 `ifconfig_`<`interface`> 变量中使用 “`NOAUTO`” 关键字进行配置，如下所述。假定每个 `interface` 值都存在对应的 `ifconfig_`<`interface`> 变量。当接口名包含 “`.-/+`” 中的任何字符时，在查找之前会转换为 “`_`”。例如，接口 `em0.102` 将使用变量 `ifconfig_em0_102` 进行配置。该变量可以包含 [ifconfig(8)](../man8/ifconfig.8.md) 的参数，以及下文所述的特殊不区分大小写关键字。这些关键字在将值传递给 [ifconfig(8)](../man8/ifconfig.8.md) 之前会被移除，而其他参数的顺序会保留。例如，要将 IPv4 地址 192.0.2.1/24 分配给接口 em0：如果设置了 `ifconfig_`<`interface`>`_ipv6` 变量，则不需要设置 `ifconfig_`<`interface`>，除非还应为接口分配 IPv4 地址。可以使用 [ifconfig(8)](../man8/ifconfig.8.md) 语法添加 IP 别名条目，并使用地址族关键字如 `inet`。假设所讨论的接口为 `em0`，可能如下所示：还可以使用无类别域间路由（CIDR）地址表示法配置多个 IP 地址，每个地址组件可以是一个范围，如 `inet 192.0.2.5-23/24` 或 `inet6 2001:db8:1-f::1/64`。此表示法仅允许地址和前缀长度部分，不允许其他地址修饰符。请注意，从范围规范生成的地址最大数量受 `rc.conf` 中 `netif_ipexpand_max` 指定的整数值限制，因为小的输入错误可能意外生成大量地址。默认值为 `2048`。可以通过在 `rc.conf` 中添加以下行来增加：在 `192.0.2.5-23/24` 的情况下，地址 192.0.2.5 将以前缀长度 /24 配置，地址 192.0.2.6 到 192.0.2.23 以前缀长度 /32 配置，如 [ifconfig(8)](../man8/ifconfig.8.md) 别名部分所述。请注意，此特殊 CIDR 处理仅适用于 `inet`，不适用于 `inet6` 等其他地址族。以 `em0` 为例，可能如下所示：依此类推。请注意，已弃用的 `ipv4_addrs_`<`interface`> 变量曾用于 IPv4 CIDR 地址表示法。`ifconfig_`<`interface`>`_alias`<`n`> 变量取代了它，但 `ipv4_addrs_`<`interface`> 仍为向后兼容而支持。对于每个带地址族关键字的 `ifconfig_`<`interface`>`_alias`<`n`> 条目，其内容会传递给 [ifconfig(8)](../man8/ifconfig.8.md)。执行在第一次不成功的访问时停止，因此如果出现如下内容：注意 alias4 *不会* 被添加，因为搜索会在缺失的 “`alias3`” 条目处停止。由于这种难以管理的行为，存在 `ifconfig_`<`interface`>`_aliases` 变量，它具有与 `ifconfig_`<`interface`>`_alias`<`n`> 相同的功能，可以将所有条目放在一个变量中，如下所示：它还支持网络掩码表示法以保持向后兼容。如果 **/etc/start_if**.<`interface`> 文件存在，它会在按 `ifconfig_`<`interface`> 和 `ifconfig_`<`interface`>`_alias`<`n`> 变量指定配置接口之前，由 [sh(1)](../man1/sh.1.md) 解释器读取并执行。如果设置了 `vlans_`<`interface`> 变量，将为列表中的每个项目创建一个 [vlan(4)](../man4/vlan.4.md) 接口，并将 `vlandev` 参数设为 `interface`。如果 vlan 接口名是数字，则该数字用作 vlan 标记，新 vlan 接口命名为 `interface`.`tag`。否则，vlan 标记必须通过 `create_args_`<`interface`> 变量中的 `vlan` 参数指定。要在 `em0` 上创建名为 `em0.101`、vlan 标记为 101、可选 IPv4 地址为 192.0.2.1/24 的 vlan 设备：要在 `em0` 上创建名为 `myvlan`、vlan 标记为 102 的 vlan 设备：如果设置了 `wlans_`<`interface`> 变量，将为列表中的每个项目创建一个 [wlan(4)](../man4/wlan.4.md) 接口，并将 `wlandev` 参数设为 `interface`。可以通过设置 `create_args_`<`interface`> 变量将更多 wlan 克隆参数传递给 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令。从 FreeBSD 8.0 起，每个无线设备必须创建一个或多个 [wlan(4)](../man4/wlan.4.md) 设备。由 wlandebug(8) 设置的 [wlan(4)](../man4/wlan.4.md) 设备调试标志可通过 `wlandebug_`<`interface`> 变量指定。此变量的内容将直接传递给 wlandebug(8)。如果 `ifconfig_`<`interface`> 包含关键字 “`NOAUTO`”，则当 `network_interfaces` 设为 “`AUTO`” 时，接口不会在引导时或由 **/etc/pccard_ether** 配置。可以通过在 `ifconfig_`<`interface`> 变量中添加 “`DHCP`” 来通过 DHCP 启动接口。例如，要通过 DHCP 初始化 `em0` 设备，可以使用如下内容：如果要使用 wpa_supplicant(8) 配置无线接口以用于 WPA、EAP/LEAP 或 WEP，需要在 `ifconfig_`<`interface`> 变量中添加 “`WPA`”。另一方面，如果要使用 hostapd(8) 配置无线接口，需要在 `ifconfig_`<`interface`> 变量中添加 “`HOSTAP`”。hostapd(8) 将使用 **/etc/hostapd-**<`interface`>`.conf` 中的设置。最后，你可以在 `ifconfig_`<`interface`> 变量中添加 [ifconfig(8)](../man8/ifconfig.8.md) 选项，除 **/etc/start_if**.<`interface`> 文件外。例如，要将 [ath(4)](../man4/ath.4.md) 无线设备配置为工作站模式，使用通过 DHCP 获取的地址、WPA 认证和 802.11b 模式，可以使用如下内容：除 `ifconfig_`<`interface`> 形式外，还可以配置后备变量 `ifconfig_DEFAULT`。它将用于所有没有 `ifconfig_`<`interface`> 变量的接口。还可以通过以下方式重命名接口：

**`ipv6_enable`** (`bool`) 此变量已弃用。如有必要，请使用 `ifconfig_`<`interface`>`_ipv6` 和 `ipv6_activate_all_interfaces`。如果变量为 “`YES`”，则将 “`inet6 accept_rtadv`” 添加到所有 `ifconfig_`<`interface`>`_ipv6`，并将 `ipv6_activate_all_interfaces` 变量定义为 “`YES`”。

**`ipv6_prefer`** (`bool`) 此变量已弃用。请改用 `ip6addrctl_policy`。如果变量为 “`YES`”，由 ip6addrctl(8) 设置的默认地址选择策略表将为 IPv6 优先。如果变量为 “`NO`”，由 ip6addrctl(8) 设置的默认地址选择策略表将为 IPv4 优先。

**`ipv6_activate_all_interfaces`** (`bool`) 这控制没有对应 `ifconfig_`<`interface`>`_ipv6` 变量的 IPv6 功能接口的初始配置。请注意，在 FreeBSD 上使用 IPv6 功能并不总是需要将此变量设为 “YES”。在大多数情况下，只需配置 `ifconfig_`<`interface`>`_ipv6` 变量即可。如果变量为 “`NO`”，所有没有对应 `ifconfig_`<`interface`>`_ipv6` 变量的接口在创建时将标记为 “`IFDISABLED`”。这意味着该接口上的所有 IPv6 功能都被完全禁用，以强制执行安全策略。如果变量设为 “YES”，则所有接口上的该标志将被清除。在大多数情况下，只需为 IPv6 功能接口定义 `ifconfig_`<`interface`>`_ipv6` 即可。但是，如果接口是动态添加的（例如由 PPP 等隧道协议），通常难以预先定义该变量。在这种情况下，可以通过将此变量设为 “YES” 来禁用 “`IFDISABLED`” 标志的配置。关于 “`IFDISABLED`” 标志和 “`inet6 ifdisabled`” 关键字的更多详情，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。默认为 “`NO`”。

**`ipv6_privacy`** (`bool`) 如果变量为 “`YES`”，将按 RFC 4941 所述为每个 IPv6 接口生成隐私地址。

**`ipv6_network_interfaces`** (`str`) 这是 `network_interfaces` 的 IPv6 等价物。通常不需要手动配置此变量。

**`ipv6_cpe_wanif`** (`str`) 如果变量设为接口名，则在评估 `ifconfig_`<`interface`>`_ipv6` 之前，会自动将 [ifconfig(8)](../man8/ifconfig.8.md) 选项 “inet6 -no_radr accept_rtadv” 添加到指定接口，并将两个 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.inet6.ip6.rfc6204w3` 和 `net.inet6.ip6.no_radr` 设为 1。这意味着指定接口将接受该链路上的 ICMPv6 路由器通告消息，并将发现的路由器添加到默认路由器列表。虽然其他接口如果指定了 “inet6 accept_rtadv” 选项仍可接受 RA 消息，但默认情况下通过 “inet6 no_radr” 选项禁用将路由添加到默认路由器列表。更多详情请参见 [ifconfig(8)](../man8/ifconfig.8.md)。请注意，当 `net.inet6.ip6.rfc6204w3` 设为 1 时，即使 `net.inet6.ip6.forwarding` 为 1（启用数据包转发），也会接受 ICMPv6 路由器通告消息。默认为 “`NO`”。

**`ifconfig_`**<`interface`>`_descr` (`str`) 这为接口分配任意描述。[sysctl(8)](../man8/sysctl.8.md) 变量 `net.ifdescr_maxlen` 限制其长度。此静态设置可被 dhclient(8) 钩子等动态接口配置实用程序启动的命令覆盖。可以使用 [ifconfig(8)](../man8/ifconfig.8.md) 命令查看描述，并可通过 bsnmpd(1) 守护进程使用其 MIB-2 模块导出。

**`ifconfig_`**<`interface`>`_ipv6` (`str`) 接口上的 IPv6 功能应由 `ifconfig_`<`interface`>`_ipv6` 配置，而不是在 `ifconfig_`<`interface`> 中设置 ifconfig 参数。如果此变量为空，则指定接口上由 `ipv6_prefix_`<`interface`> 等其他变量指定的所有 IPv6 配置都将被忽略。别名应通过带 “`inet6`” 关键字的 `ifconfig_`<`interface`>`_alias`<`n`> 设置。例如：在 `ifconfig_`<`interface`>`_ipv6` 设置中具有 “`inet6 accept_rtadv`” 关键字的接口将由 SLAAC（无状态地址自动配置）自动配置，详见由于 IPv6 规范要求每条链路上都需要链路本地地址，因此除了配置的全局范围地址外，还会自动配置链路本地地址。该地址通过使用算法定义的算法从 MAC 地址计算得出。如果接口上仅需链路本地地址，可使用以下配置：也可以手动配置链路本地地址。这对于 IPv6 路由器的默认路由器地址很有用，这样当网卡更换时它不会改变。例如：

**`ipv6_prefix_`**<`interface`> (`str`) 如果在 `ipv6_prefix_`<`interface`> 中定义了一个或多个前缀，则基于每个前缀和 EUI-64 接口索引的地址将在该接口上配置。请注意，当 `ifconfig_`<`interface`>`_ipv6` 为空时，此变量将被忽略。例如，以下配置等同于以下内容：这些子网路由器任播地址仅在 `ipv6_gateway_enable` 为 YES 时添加。

**`ipv6_default_interface`** (`str`) 如果未设为 “`NO`”，这是范围地址的默认输出接口。这仅在 ipv6_gateway_enable="NO" 时有效。

**`ip6addrctl_enable`** (`bool`) 此变量用于启用配置默认地址选择策略表（RFC 3484）。该表可在另一个变量 `ip6addrctl_policy` 中指定。对于 `ip6addrctl_policy`，可指定以下关键字：“`ipv4_prefer`”、“`ipv6_prefer`” 或 “`AUTO`”。如果指定 “`ipv4_prefer`” 或 “`ipv6_prefer`”，ip6addrctl(8) 会安装 RFC 3484 第 10.3 节（IPv4 优先）或第 2.1 节（IPv6 优先）中所述的预定义策略表。如果指定 “`AUTO`”，它首先尝试读取 **/etc/ip6addrctl.conf** 文件。如果找到此文件，ip6addrctl(8) 会读取并安装它。如果未找到，则根据 `ipv6_activate_all_interfaces` 变量自动设置策略；如果该变量设为 “`YES`”，则使用 IPv6 优先策略。否则为 IPv4 优先。`ip6addrctl_enable` 和 `ip6addrctl_policy` 的默认值分别为 “`YES`” 和 “`AUTO`”。

**`cloned_interfaces`** (`str`) 设为要在本主机上创建的可克隆网络接口列表。可以通过设置 `create_args_`<`interface`> 变量为每个接口传递额外的克隆参数给 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令。如果接口名以 “:sticky” 关键字指定，即使 `rc.d/netif` 脚本以 “stop” 参数调用，该接口也不会被销毁。这在重新配置接口而不销毁它时很有用。`cloned_interfaces` 中的条目会自动追加到 `network_interfaces` 以进行配置。

**`cloned_interfaces_sticky`** (`bool`) 此变量用于全局启用 `cloned_interfaces` 中 “:sticky” 关键字对所有接口的功能。默认值为 “NO”。即使此变量设为 “YES”，也可使用 “:nosticky” 关键字在每个接口上覆盖它。

**`gif_interfaces`** 设为要在本主机上配置的 [gif(4)](../man4/gif.4.md) 隧道接口列表。假定每个 `interface` 值都存在对应的 `gifconfig_`<`interface`> 变量。此变量的值用于通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `tunnel` 选项配置隧道的链路层。此外，此选项确保在尝试配置之前通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `create` 选项创建每个列出的接口。例如，配置两个 [gif(4)](../man4/gif.4.md) 接口：

**`ppp_enable`** (`bool`) 如果设为 “`YES`”，运行 ppp(8) 守护进程。

**`ppp_profile`** (`str`) 从 **/etc/ppp/ppp.conf** 使用的配置文件名。也用于 `ppp_mode` 和 `ppp_nat` 的每配置文件覆盖，以及 `ppp_`<`profile`>`_unit`。当配置文件名包含 “`.-/+`” 中的任何字符时，对于覆盖变量名，它们会转换为 “`_`”。

**`ppp_mode`** (`str`) 运行 ppp(8) 守护进程的模式。

**`ppp_`**<`profile`>`_mode` (`str`) 覆盖 `profile` 的全局 `ppp_mode`。接受的模式有 “`auto`”、“`ddial`”、“`direct`” 和 “`dedicated`”。完整描述请参见手册。

**`ppp_nat`** (`bool`) 如果设为 “`YES`”，启用网络地址转换。与 `gateway_enable` 配合使用，允许私有网络地址上的主机使用此主机作为网络地址转换路由器访问互联网。默认为 “`YES`”。

**`ppp_`**<`profile`>`_nat` (`str`) 覆盖 `profile` 的全局 `ppp_nat`。

**`ppp_`**<`profile`>`_unit` (`int`) 设置此配置文件使用的单元号。详情请参见 `-unit``N` 的手册描述。

**`ppp_user`** (`str`) 启动 ppp(8) 的用户名。默认情况下，ppp(8) 以 “`root`” 启动。

**`rc_conf_files`** (`str`) 此选项用于指定将覆盖 **/etc/defaults/rc.conf** 中设置的文件列表。文件将按指定的顺序读取，并应包含文件的完整路径。默认情况下，指定的文件为 **/etc/rc.conf** 和 **/etc/rc.conf.local**。

**`zfs_enable`** (`bool`) 如果设为 “`YES`”，**/etc/rc.d/zfs** 将尝试自动挂载 ZFS 文件系统并初始化 ZFS 卷（ZVOL）。

**`zpool_reguid`** (`str`) 空格分隔的 ZFS 池名列表，在首次引导时应为这些池分配新的池 GUID。这在使用从模板（如虚拟机镜像）复制的 ZFS 池时很有用。

**`zpool_upgrade`** (`str`) 空格分隔的 ZFS 池名列表，在首次引导时应升级这些池的版本。这在使用由 makefs(8) 实用程序生成的 ZFS 池时很有用。

**`gptboot_enable`** (`bool`) 如果设为 “`YES`”，**/etc/rc.d/gptboot** 将记录系统是否成功（或未成功）从使用 [gpart(8)](../man8/gpart.8.md) 实用程序设置 `bootonce` 属性的 GPT 分区引导。

**`geli_devices`** (`str`) 引导时自动附加的设备列表。注意，**/etc/fstab** 中的 .eli 设备会自动追加到此列表。

**`geli_groups`** (`str`) 包含引导时使用相同密钥文件和密码短语自动附加的设备组列表。这必须伴随对应的 `geli_`<`group`>`_devices` 变量。

**`geli_tries`** (`int`) 询问用户密码短语的次数。如果为空，则从 `kern.geom.eli.tries` sysctl 变量获取。

**`geli_default_flags`** (`str`) geli(8) 配置磁盘加密时使用的默认标志。可以通过定义 `geli_`<`device`>`_flags` 变量为每个设备单独配置标志，通过定义 `geli_`<`group`>`_flags` 变量为每个组单独配置标志。

**`geli_autodetach`** (`str`) 指定 GELI 设备是否在文件系统挂载后标记为最后关闭时分离。默认为 “`YES`”。可以通过定义 `geli_`<`device`>`_autodetach` 变量为每个设备单独更改。

**`root_rw_mount`** (`bool`) 默认设为 “`YES`”。在引导时检查文件系统后，如果此选项设为 “`YES`”，根文件系统将重新挂载为读写。从只读远程 NFS 共享挂载根文件系统的无盘系统应在其 `rc.conf` 中将此设为 “`NO`”。

**`fsck_y_enable`** (`bool`) 如果设为 “`YES`”，如果文件系统的初始预检失败，fsck(8) 将以 `-y` 标志运行。

**`background_fsck`** (`bool`) 如果设为 “`NO`”，系统将不会尝试在可能的情况下在后台运行 fsck(8)。

**`background_fsck_delay`** (`int`) 启动后台 fsck(8) 前休眠的秒数。默认为 60 秒，以允许大型应用程序（如 X 服务器）在磁盘 I/O 带宽被 fsck(8) 独占之前启动。如果设为负数，后台文件系统检查将无限期延迟，以允许管理员在更方便的时间运行它。例如，可以通过向 **/etc/crontab** 添加如下行从 cron(8) 运行：

**`netfs_types`** (`str`) 基于网络的文件系统类型列表。此列表通常不应由最终用户修改。请改用 `extra_netfs_types`。

**`extra_netfs_types`** (`str`) 如果设为 “`NO`”（默认）以外的值，此变量扩展了 [rc(8)](../man8/rc.8.md) 在启动时应延迟到网络初始化后才自动挂载的文件系统类型列表。它应包含空白分隔的网络文件系统描述符对，每对由传递给 [mount(8)](../man8/mount.8.md) 的文件系统类型和人类可读的单字描述组成，以冒号（`:`）连接。仅在使用第三方文件系统类型时才需要以这种方式扩展默认列表。

**`syslogd_enable`** (`bool`) 如果设为 “`YES`”，运行 syslogd(8) 守护进程。注意，`syslogd_oomprotect` 变量在 **/etc/defaults/rc.conf** 中默认设为 “`YES`”。

**`syslogd_program`** (`str`) syslogd(8) 的路径（默认 **/usr/sbin/syslogd**）。

**`syslogd_flags`** (`str`) 如果 `syslogd_enable` 设为 “`YES`”，这些是传递给 syslogd(8) 的标志。

**`inetd_enable`** (`bool`) 如果设为 “`YES`”，运行 [inetd(8)](../man8/inetd.8.md) 守护进程。

**`inetd_program`** (`str`) [inetd(8)](../man8/inetd.8.md) 的路径（默认 **/usr/sbin/inetd**）。

**`inetd_flags`** (`str`) 如果 `inetd_enable` 设为 “`YES`”，这些是传递给 [inetd(8)](../man8/inetd.8.md) 的标志。

**`hastd_enable`** (`bool`) 如果设为 “`YES`”，运行 hastd(8) 守护进程。

**`hastd_program`** (`str`) hastd(8) 的路径（默认 **/sbin/hastd**）。

**`hastd_flags`** (`str`) 如果 `hastd_enable` 设为 “`YES`”，这些是传递给 hastd(8) 的标志。

**`local_unbound_enable`** (`bool`) 如果设为 “`YES`”，以本地缓存 DNS 解析器运行 unbound(8) 守护进程。注意，`local_unbound_oomprotect` 变量在 **/etc/defaults/rc.conf** 中默认设为 “`YES`”。

**`nscd_enable`** (`bool`) 设为 “`YES`” 以启动 `nsswitch` 子系统的 nscd(8) 缓存守护进程。

**`nscd_flags`** (`str`) 如果 `nscd_enable` 设为 “`YES`”，这些标志传递给 nscd(8)。

**`kdc_enable`** (`bool`) 设为 “`YES`” 以在引导时启动 Kerberos 5 认证服务器。

**`kdc_program`** (`str`) 如果 `kdc_enable` 设为 “`YES`”，这是 Kerberos 5 认证服务器的路径。

**`kdc_flags`** (`str`) 默认为空。此变量包含传递给 Kerberos 5 认证服务器的额外标志。

**`kadmind_enable`** (`bool`) 设为 “`YES`” 以启动 kadmind(8)（Kerberos 5 管理守护进程）；在从服务器上设为 “`NO`”。

**`kadmind_program`** (`str`) 如果 `kadmind_enable` 设为 “`YES`”，这是 Kerberos 5 管理守护进程的路径。

**`kpasswdd_enable`** (`bool`) 设为 “`YES`” 以启动 kpasswdd(8)（Kerberos 5 密码更改守护进程）；在从服务器上设为 “`NO`”。

**`kpasswdd_program`** (`str`) 如果 `kpasswdd_enable` 设为 “`YES`”，这是 Kerberos 5 密码更改守护进程的路径。

**`kfd_enable`** (`bool`) 设为 “`YES`” 以在引导时启动 kfd(8)（Kerberos 5 票据转发守护进程）。

**`kfd_program`** (`str`) kfd(8) 的路径（默认 **/usr/libexec/kfd**）。

**`rwhod_enable`** (`bool`) 如果设为 “`YES`”，在引导时运行 rwhod(8) 守护进程。

**`rwhod_flags`** (`str`) 如果 `rwhod_enable` 设为 “`YES`”，这些是传递给它的标志。

**`update_motd`** (`bool`) 如果设为 “`YES`”，**/var/run/motd** 会在引导时更新以反映正在运行的内核版本。如果设为 “`NO`”，**/var/run/motd** 不会更新。

**`nfs_client_enable`** (`bool`) 如果设为 “`YES`”，在引导时运行 NFS 客户端守护进程。

**`nfs_access_cache`** (`int`) 如果 `nfs_client_enable` 设为 “`YES`”，可设为 “`0`” 以禁用 NFS ACCESS RPC 缓存，或设为 NFS ACCESS 结果应缓存的秒数。2-10 秒的值将大大减少许多 NFS 操作的网络流量。

**`nfs_server_enable`** (`bool`) 如果设为 “`YES`”，在引导时运行 NFS 服务器守护进程。

**`nfs_server_flags`** (`str`) 如果 `nfs_server_enable` 设为 “`YES`”，这些是传递给 nfsd(8) 守护进程的标志。

**`nfsv4_server_enable`** (`bool`) 如果 `nfs_server_enable` 设为 “`YES`” 且 `nfsv4_server_enable` 设为 “`YES`”，启用 NFSv4 以及 NFSv2 和 NFSv3 服务器。

**`nfsv4_server_only`** (`bool`) 如果 `nfs_server_enable` 设为 “`YES`” 且 `nfsv4_server_only` 设为 “`YES`”，仅为 NFSv4 启用 NFS 服务器。

**`nfs_server_maxio`** (`int`) 设置 vfs.nfsd.srvmaxio 的值，即 NFS 服务器的最大 I/O 大小。

**`tlsclntd_enable`** (`bool`) 如果设为 “`YES`”，运行 rpc.tlsclntd(8) 守护进程，NFS-over-TLS NFS 挂载需要此守护进程。

**`tlsservd_enable`** (`bool`) 如果设为 “`YES`”，运行 rpc.tlsservd(8) 守护进程，nfsd(8) 需要 it 以支持 NFS-over-TLS NFS 挂载。

**`nfsuserd_enable`** (`bool`) 如果 `nfsuserd_enable` 设为 “`YES`”，运行 nfsuserd 守护进程，NFSv4 需要它以在用户/组名与 uid/gid 号之间映射。如果 `nfsv4_server_enable` 设为 “`YES`”，将强制启用。

**`nfsuserd_flags`** (`str`) 如果 `nfsuserd_enable` 设为 “`YES`”，这些是传递给 nfsuserd(8) 守护进程的标志。

**`nfscbd_enable`** (`bool`) 如果 `nfscbd_enable` 设为 “`YES`”，运行 nfscbd 守护进程，它为 NFSv4 客户端启用回调/委托。

**`nfscbd_flags`** (`str`) 如果 `nfscbd_enable` 设为 “`YES`”，这些是传递给 nfscbd(8) 守护进程的标志。

**`mountd_enable`** (`bool`) 如果设为 “`YES`” 且未设置 `nfs_server_enable`，启动 mountd(8) 但不启动 nfsd(8) 守护进程。这通常用于在不实际使用 NFS 的情况下运行 CFS。

**`mountd_flags`** (`str`) 如果 `mountd_enable` 设为 “`YES`”，这些是传递给 mountd(8) 守护进程的标志。

**`weak_mountd_authentication`** (`bool`) 如果设为 “`YES`”，允许 PCNFSD 等服务发出非特权挂载请求。

**`nfs_reserved_port_only`** (`bool`) 如果设为 “`YES`”，仅在安全端口上提供 NFS 服务。

**`nfs_bufpackets`** (`int`) 如果设为数字，表示在 NFS 客户端上保留的套接字缓冲区空间的数据包数量。内核默认值通常为 4。在千兆网络上使用更高的值可能有助于提高性能。最小值为 2，最大值为 64。

**`rpc_lockd_enable`** (`bool`) 如果设为 “`YES`” 且同时为 NFS 服务器或客户端，在引导时运行 rpc.lockd(8)。

**`rpc_lockd_flags`** (`str`) 如果 `rpc_lockd_enable` 设为 “`YES`”，这些是传递给 rpc.lockd(8) 守护进程的标志。

**`rpc_statd_enable`** (`bool`) 如果设为 “`YES`” 且同时为 NFS 服务器或客户端，在引导时运行 rpc.statd(8)。

**`rpc_statd_flags`** (`str`) 如果 `rpc_statd_enable` 设为 “`YES`”，这些是传递给 rpc.statd(8) 守护进程的标志。

**`rpcbind_program`** (`str`) rpcbind(8) 的路径（默认 **/usr/sbin/rpcbind**）。

**`rpcbind_enable`** (`bool`) 如果设为 “`YES`”，在引导时运行 rpcbind(8) 服务。

**`rpcbind_flags`** (`str`) 如果 `rpcbind_enable` 设为 “`YES`”，这些是传递给 rpcbind(8) 守护进程的标志。

**`pppoed_enable`** (`bool`) 如果设为 “`YES`”，在引导时运行 pppoed(8) 守护进程以提供以太网上的 PPP 服务。

**`pppoed_`**<`provider`> (`str`) pppoed(8) 监听对此 `provider` 的请求，并最终以同名的 `system` 参数运行 ppp(8)。

**`pppoed_flags`** (`str`) 传递给 pppoed(8) 的额外标志。

**`pppoed_interface`** (`str`) 运行 pppoed(8) 的网络接口。当 `pppoed_enable` 设为 “`YES`” 时，这是必需的。

**`ntpdate_enable`** (`bool`) 如果设为 “`YES`”，在系统启动时运行 ntpdate(8)。此命令旨在从某个标准参考*仅同步一次*系统时钟。注意，使用 `ntpd_sync_on_start` 变量是 ntpdate(8) 实用程序的首选替代方案，因为 ntpdate(8) 即将从 NTP 发行版中退役。

**`ntpdate_config`** (`str`) ntpdate(8) 的配置文件。默认为 **/etc/ntp.conf**。

**`ntpdate_hosts`** (`str`) 启动时要同步的 NTP 服务器空白分隔列表。默认使用 `ntpdate_config` 中列出的服务器（如果该文件存在）。

**`ntpdate_program`** (`str`) ntpdate(8) 的路径（默认 **/usr/sbin/ntpdate**）。

**`ntpdate_flags`** (`str`) 如果 `ntpdate_enable` 设为 “`YES`”，这些是传递给 ntpdate(8) 命令的标志（通常是主机名）。

**`ntpd_enable`** (`bool`) 如果设为 “`YES`”，在引导时运行 ntpd(8) 命令。

**`ntpd_program`** (`str`) ntpd(8) 的路径（默认 **/usr/sbin/ntpd**）。

**`ntpd_config`** (`str`) ntpd(8) 配置文件的路径。默认为 **/etc/ntp.conf**。

**`ntpd_flags`** (`str`) 如果 `ntpd_enable` 设为 “`YES`”，这些是传递给 ntpd(8) 守护进程的标志。

**`ntpd_sync_on_start`** (`bool`) 如果设为 “`YES`”，ntpd(8) 会以 `-g` 标志运行，在启动时同步系统时钟。关于 `-g` 选项的更多信息请参见 ntpd(8)。这是使用 ntpdate(8) 或指定 `ntpdate_enable` 变量的首选替代方案。

**`nis_client_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 ypbind(8) 服务。

**`nis_client_flags`** (`str`) 如果 `nis_client_enable` 设为 “`YES`”，这些是传递给 ypbind(8) 服务的标志。

**`nis_ypldap_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 ypldap(8) 守护进程。

**`nis_ypldap_flags`** (`str`) 如果 `nis.ypldap_enable` 设为 “`YES`”，这些是传递给 ypldap(8) 守护进程的标志。

**`nis_ypset_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 ypset(8) 守护进程。

**`nis_ypset_flags`** (`str`) 如果 `nis_ypset_enable` 设为 “`YES`”，这些是传递给 ypset(8) 守护进程的标志。

**`nis_server_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 ypserv(8) 守护进程。

**`nis_server_flags`** (`str`) 如果 `nis_server_enable` 设为 “`YES`”，这些是传递给 ypserv(8) 守护进程的标志。

**`nis_ypxfrd_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 rpc.ypxfrd(8) 守护进程。

**`nis_ypxfrd_flags`** (`str`) 如果 `nis_ypxfrd_enable` 设为 “`YES`”，这些是传递给 rpc.ypxfrd(8) 守护进程的标志。

**`nis_yppasswdd_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 rpc.yppasswdd(8) 守护进程。

**`nis_yppasswdd_flags`** (`str`) 如果 `nis_yppasswdd_enable` 设为 “`YES`”，这些是传递给 rpc.yppasswdd(8) 守护进程的标志。

**`rpc_ypupdated_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 `rpc.ypupdated` 守护进程。

**`bsnmpd_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 bsnmpd(1) 守护进程。请确保理解在主机上运行 SNMP 守护进程的安全影响。

**`bsnmpd_flags`** (`str`) 如果 `bsnmpd_enable` 设为 “`YES`”，这些是传递给 bsnmpd(1) 守护进程的标志。

**`defaultrouter`** (`str`) 如果未设为 “`NO`”，创建到该主机名或 IP 地址的默认路由（如果到达名称服务器也需要此路由，请使用 IP 地址！）。

**`defaultrouter_fibN`** (`str`) 如果未设为 “`NO`”，在 FIB N 中创建到该主机名或 IP 地址的默认路由。

**`ipv6_defaultrouter`** (`str`) `defaultrouter` 的 IPv6 等价物。

**`ipv6_defaultrouter_fibN`** (`str`) `defaultrouter_fibN` 的 IPv6 等价物。

**`static_arp_pairs`** (`str`) 设为系统引导时要添加的静态 ARP 对列表。对于值中的每个空白分隔 `element`，假定存在一个 `static_arp_`<`element`> 变量，其内容稍后将传递给 “`arp` `-S`” 操作。例如

**`static_ndp_pairs`** (`str`) 设为系统引导时要添加的静态 NDP 对列表。对于值中的每个空白分隔 `element`，假定存在一个 `static_ndp_`<`element`> 变量，其内容稍后将传递给 “`ndp` `-s`” 操作。例如

**`static_routes`** (`str`) 设为系统引导时要添加的静态路由列表。如果未设为 “`NO`”，对于值中的每个空白分隔 `element`，假定存在一个 `route_`<`element`> 变量，其内容稍后将传递给 “`route` `add`” 操作。例如：当 `element` 采用 `name:ifname` 形式时，该路由特定于接口 `ifname`。

**`ipv6_static_routes`** (`str`) `static_routes` 的 IPv6 等价物。如果未设为 “`NO`”，对于值中的每个空白分隔 `element`，假定存在一个 `ipv6_route_`<`element`> 变量，其内容稍后将传递给 “`route` `add` `-inet6`” 操作。

**`gateway_enable`** (`bool`) 如果设为 “`YES`”，将主机配置为 IP 路由器，例如在接口之间转发数据包。

**`ipv6_gateway_enable`** (`bool`) `gateway_enable` 的 IPv6 等价物。

**`routed_enable`** (`bool`) 如果设为 “`YES`”，根据 `routed_program` 和 `routed_flags` 的设置运行某种路由守护进程。

**`route6d_enable`** (`bool`) `routed_enable` 的 IPv6 等价物。如果设为 “`YES`”，根据 `route6d_program` 和 `route6d_flags` 的设置运行某种路由守护进程。

**`routed_program`** (`str`) 如果 `routed_enable` 设为 “`YES`”，这是要使用的路由守护进程的名称。默认为 [routed(8)](../man8/routed.8.md)。

**`route6d_program`** (`str`) `routed_program` 的 IPv6 等价物。默认为 [route6d(8)](../man8/route6d.8.md)。

**`routed_flags`** (`str`) 如果 `routed_enable` 设为 “`YES`”，这些是传递给路由守护进程的标志。

**`route6d_flags`** (`str`) `routed_flags` 的 IPv6 等价物。

**`rtadvd_enable`** (`bool`) 如果设为 “`YES`”，在引导时运行 rtadvd(8) 守护进程。rtadvd(8) 实用程序向 `rtadvd_interfaces` 中指定的接口发送 ICMPv6 路由器通告消息。启用此功能时应格外小心。你可能需要微调 rtadvd.conf(5)。

**`rtadvd_flags`** (`str`) 如果 `rtadvd_enable` 设为 “`YES`”，这些是传递给 rtadvd(8) 的标志。

**`rtadvd_interfaces`** (`str`) 如果 `rtadvd_enable` 设为 “`YES`”，这是要使用的接口列表。

**`arpproxy_all`** (`bool`) 如果设为 “`YES`”，启用全局代理 ARP。

**`forward_sourceroute`** (`bool`) 如果设为 “`YES`” 且 `gateway_enable` 也设为 “`YES`”，源路由数据包将被转发。

**`accept_sourceroute`** (`bool`) 如果设为 “`YES`”，系统将接受发往它的源路由数据包。

**`rarpd_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 [rarpd(8)](../man8/rarpd.8.md) 守护进程。

**`rarpd_flags`** (`str`) 如果 `rarpd_enable` 设为 “`YES`”，这些是传递给 [rarpd(8)](../man8/rarpd.8.md) 守护进程的标志。

**`bootparamd_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 bootparamd(8) 守护进程。

**`bootparamd_flags`** (`str`) 如果 `bootparamd_enable` 设为 “`YES`”，这些是传递给 bootparamd(8) 守护进程的标志。

**`stf_interface_ipv4addr`** (`str`) 如果未设为 “`NO`”，这是 6to4（IPv4 上的 IPv6 隧道接口）的本地 IPv4 地址。指定此项以启用 6to4 接口。

**`stf_interface_ipv4plen`** (`int`) 6to4 IPv4 地址的前缀长度，用于限制对端地址范围。有效值为 0-31。

**`stf_interface_ipv6_ifid`** (`str`) [stf(4)](../man4/stf.4.md) 的 IPv6 接口 ID。可设为 “`AUTO`”。

**`stf_interface_ipv6_slaid`** (`str`) [stf(4)](../man4/stf.4.md) 的 IPv6 站点级聚合器。

**`ipv6_ipv4mapping`** (`bool`) 如果设为 “`YES`”，启用 IPv4 映射的 IPv6 地址通信（如 `::ffff:a.b.c.d`）。

**`rtsold_enable`** (`bool`) 设为 “`YES`” 以启用 rtsold(8) 守护进程发送 ICMPv6 路由器请求消息。

**`rtsold_flags`** (`str`) 如果 `rtsold_enable` 设为 “`YES`”，这些是传递给 rtsold(8) 的标志。

**`rtsol_flags`** (`str`) 对于以 “`inet6 accept_rtadv`” 关键字配置的接口，这些是传递给 rtsol(8) 的标志。注意，`rtsold_enable` 与 `rtsol_flags` 互斥；`rtsold_enable` 优先。

**`keybell`** (`str`) 键盘铃声声音。设为 “`normal`”、“`visual`”、“`off`” 或 “`NO`”（如果需要默认行为）。详情请参见 kbdcontrol(1) 手册页。

**`keyboard`** (`str`) 如果设为非空字符串，虚拟控制台的键盘输入设为此设备。

**`keymap`** (`str`) 如果设为 “`NO`”，不安装任何键位映射，否则该值用于安装 **/usr/share/syscons/keymaps/**<`value`>`.kbd` 中的键位映射文件（如果使用 [syscons(4)](../man4/syscons.4.md)）或 **/usr/share/vt/keymaps/**<`value`>`.kbd`（如果使用 [vt(4)](../man4/vt.4.md)）。

**`keyrate`** (`str`) 键盘重复速度。设为 “`slow`”、“`normal`”、“`fast`” 或 “`NO`”（如果需要默认行为）。

**`keychange`** (`str`) 如果未设为 “`NO`”，尝试用该值编程功能键。该值应为形如 “`funkey_number new_value` [`funkey_number new_value ...`]” 的单个字符串。

**`cursor`** (`str`) 可设为 “`normal`”、“`blink`”、“`destructive`” 或 “`NO`”，以显式设置光标行为或选择默认行为。

**`scrnmap`** (`str`) 如果设为 “`NO`”，不安装任何屏幕映射，否则该值用于安装 **/usr/share/syscons/scrnmaps/**<`value`> 中的屏幕映射文件。使用 [vt(4)](../man4/vt.4.md) 作为控制台驱动程序时忽略此参数。

**`font8x16`** (`str`) 如果设为 “`NO`”，屏幕大小请求使用默认 8x16 字体值，否则使用 **/usr/share/syscons/fonts/**<`value`> 或 **/usr/share/vt/fonts/**<`value`> 中的值（取决于使用的控制台驱动程序）。

**`font8x14`** (`str`) 如果设为 “`NO`”，屏幕大小请求使用默认 8x14 字体值，否则使用 **/usr/share/syscons/fonts/**<`value`> 或 **/usr/share/vt/fonts/**<`value`> 中的值（取决于使用的控制台驱动程序）。

**`font8x8`** (`str`) 如果设为 “`NO`”，屏幕大小请求使用默认 8x8 字体值，否则使用 **/usr/share/syscons/fonts/**<`value`> 或 **/usr/share/vt/fonts/**<`value`> 中的值（取决于使用的控制台驱动程序）。

**`blanktime`** (`int`) 如果设为 “`NO`”，使用默认屏幕空白间隔，否则设为 `value` 秒。

**`saver`** (`str`) 如果未设为 “`NO`”，这是要使用的实际屏幕保护程序（`blank`、`snake`、`daemon` 等）。

**`moused_nondefault_enable`** (`str`) 如果设为 “`NO`”，命令行上指定的鼠标设备不会被 **/etc/rc.d/moused** 脚本自动视为已启用。将此变量设为 “`YES`” 允许 [usb(4)](../man4/usb.4.md) 鼠标等设备在插入时立即启用。

**`moused_enable`** (`str`) 如果设为 “`YES`”，启动 [moused(8)](../man8/moused.8.md) 守护进程以在控制台上执行剪切/粘贴选择。

**`moused_type`** (`str`) 这是连接到此主机的鼠标的协议类型。如果 `moused_enable` 设为 “`YES`”，必须设置此变量，但默认为 “`auto`”，因为 [moused(8)](../man8/moused.8.md) 守护进程在许多情况下能自动检测适当的鼠标类型。如果自动检测失败，请将此变量设为以下列表中的一个。如果鼠标连接到 PS/2 鼠标端口，选择 “`auto`” 或 “`ps/2`”，无论鼠标的品牌和型号。同样，如果鼠标连接到总线鼠标端口，选择 “`auto`” 或 “`busmouse`”。所有其他协议用于串口鼠标，不适用于 PS/2 和总线鼠标。如果是 USB 鼠标，“`auto`” 是唯一可用的协议类型。即使鼠标不在上述列表中，它也可能与列表中的某个兼容。兼容性信息请参见 [moused(8)](../man8/moused.8.md) 手册页。还应注意的是，启用此功能后，鼠标的任何其他客户端（如 X 服务器）应通过虚拟鼠标设备 **/dev/sysmouse** 访问鼠标，并将其配置为 “`sysmouse`” 类型鼠标，因为使用 [moused(8)](../man8/moused.8.md) 时所有鼠标数据都转换为这种单一规范格式。如果客户端程序不支持 “`sysmouse`” 类型，请指定 “`mousesystems`” 类型。这是第二种首选类型。

**`moused_port`** (`str`) 如果 `moused_enable` 设为 “`YES`”，这是鼠标所在的实际端口。例如，COM1 串口鼠标可能为 **/dev/cuau0**，PS/2 鼠标可能为 **/dev/psm0**。

**`moused_flags`** (`str`) 如果设置了 `moused_flags`，其值用作传递给 [moused(8)](../man8/moused.8.md) 守护进程的额外标志集。

**`moused_`**`XXX``_flags` 当 `moused_nondefault_enable` 启用且为非默认端口启动 [moused(8)](../man8/moused.8.md) 守护进程时，`moused_``XXX``_flags` 选项集优先于并替换默认 `moused_flags`（其中 `XXX` 是非默认端口的名称，即 `ums0`）。通过设置 `moused_``XXX``_flags`，可为每个 [moused(8)](../man8/moused.8.md) 实例设置不同的默认标志集。例如，你可以为默认 `moused_flags` 使用 “`-3`” 使笔记本电脑的触摸板更舒适，但当 [usb(4)](../man4/usb.4.md) 鼠标有三个或更多按钮时，为 `moused_ums0_flags` 使用空选项集。

**`mousechar_start`** (`int`) 如果设为 “`NO`”，使用默认鼠标光标字符范围 `0xd0`-`0xd3`，否则范围起始设为 `value` 字符，参见 vidcontrol(1)。如果默认范围在语言代码表中被占用，则使用此项。

**`allscreens_flags`** (`str`) 如果设置，vidcontrol(1) 会为每个虚拟终端（**/dev/ttyv\***）以这些选项运行。例如，如果 `moused_enable` 设为 “`YES`”，“`-m` `on`” 将在所有虚拟终端上启用鼠标指针。

**`allscreens_kbdflags`** (`str`) 如果设置，kbdcontrol(1) 会为每个虚拟终端（**/dev/ttyv\***）以这些选项运行。例如，“`-h` `200`” 会将 [syscons(4)](../man4/syscons.4.md) 或 [vt(4)](../man4/vt.4.md) 的回滚（历史）缓冲区设为 200 行。

**`cron_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 cron(8) 守护进程。

**`cron_program`** (`str`) cron(8) 的路径（默认 **/usr/sbin/cron**）。

**`cron_flags`** (`str`) 如果 `cron_enable` 设为 “`YES`”，这些是传递给 cron(8) 的标志。

**`cron_dst`** (`bool`) 如果设为 “`YES`”，在 cron(8) 中启用夏令时转换的特殊处理（等同于使用标志 `-s`）。

**`lpd_program`** (`str`) lpd(8) 的路径（默认 **/usr/sbin/lpd**）。

**`lpd_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时运行 lpd(8) 守护进程。

**`lpd_flags`** (`str`) 如果 `lpd_enable` 设为 “`YES`”，这些是传递给 lpd(8) 守护进程的标志。

**`chkprintcap_enable`** (`bool`) 如果设为 “`YES`”，在启动 lpd(8) 守护进程之前运行 chkprintcap(8) 命令。

**`chkprintcap_flags`** (`str`) 如果 `lpd_enable` 和 `chkprintcap_enable` 都设为 “`YES`”，这些是传递给 chkprintcap(8) 程序的标志。默认为 “`-d`”，这会创建缺失的目录。

**`dumpdev`** (`str`) 指示在系统崩溃时应将崩溃转储写入的设备（通常是交换分区）。如果此变量的值为 “`AUTO`”，将使用 **/etc/fstab** 中列出的第一个合适的交换设备作为转储设备。否则，此变量的值作为参数传递给 dumpon(8) 和 savecore(8)。要禁用崩溃转储，将此变量设为 “`NO`”。

**`dumpon_flags`** (`str`) 将 `dumpdev` 配置为系统转储设备时传递给 dumpon(8) 的标志。

**`dumpdir`** (`str`) 当系统崩溃后重启且在 `dumpdev` 变量指定的设备上找到崩溃转储时，savecore(8) 会将该崩溃转储和内核副本保存到 `dumpdir` 变量指定的目录。默认值为 **/var/crash**。设为 “`NO`” 以在设置 `dumpdir` 时不引导时运行 savecore(8)。

**`savecore_enable`** (`bool`) 如果设为 “`NO`”，禁用从 `dumpdev` 自动提取崩溃转储。

**`savecore_flags`** (`str`) 如果启用了崩溃转储，这些是传递给 savecore(8) 实用程序的标志。

**`quota_enable`** (`bool`) 设为 “`YES`” 以通过 quotaon(8) 命令在系统启动时为 **/etc/fstab** 中标记为已启用配额的所有文件系统启用用户和组磁盘配额。内核必须构建 `options QUOTA` 才能使磁盘配额正常工作。

**`check_quotas`** (`bool`) 设为 “`YES`” 以通过 quotacheck(8) 命令启用用户和组磁盘配额检查。

**`quotacheck_flags`** (`str`) 如果 `quota_enable` 设为 “`YES`” 且 `check_quotas` 设为 “`YES`”，这些是传递给 quotacheck(8) 实用程序的标志。默认为 “`-a`”，检查 **/etc/fstab** 中所有启用配额的文件系统的配额。

**`quotaon_flags`** (`str`) 如果 `quota_enable` 设为 “`YES`”，这些是传递给 quotaon(8) 实用程序的标志。默认为 “`-a`”，为 **/etc/fstab** 中所有启用配额的文件系统启用配额。

**`quotaoff_flags`** (`str`) 如果 `quota_enable` 设为 “`YES`”，这些是关闭配额系统时传递给 quotaoff(8) 实用程序的标志。默认为 “`-a`”，为 **/etc/fstab** 中所有启用配额的文件系统禁用配额。

**`accounting_enable`** (`bool`) 设为 “`YES`” 以通过 accton(8) 设施启用系统记账。

**`firstboot_sentinel`** (`str`) 此变量指定 “首次引导” 哨兵文件的完整路径。如果存在具有此路径的文件，带有 “firstboot” 关键字的 `rc.d` 脚本将在启动时运行，且引导过程完成后哨兵文件将被删除。哨兵文件必须位于可写文件系统上，且不得晚于 `early_late_divider` 挂载才能正常工作。默认为 **/firstboot**。

**`linux_enable`** (`bool`) 设为 “`YES`” 以在系统初始引导时启用 Linux/ELF 二进制模拟。

**`sysvipc_enable`** (`bool`) 如果设为 “`YES`”，在引导时加载 System V IPC 原语。

**`clear_tmp_enable`** (`bool`) 设为 “`YES`” 以在启动时清理 **/tmp**。

**`clear_tmp_X`** (`bool`) 设为 “`NO`” 以禁用删除 X11 锁文件，以及删除并（安全地）重新创建 X11 相关程序的各种套接字目录。

**`ldconfig_paths`** (`str`) 设为与 ldconfig(8) 一起使用的共享库路径列表。注意：**/lib** 和 **/usr/lib** 总是首先添加，因此它们无需出现在此列表中。

**`ldconfig32_paths`** (`str`) 设为与 ldconfig(8) 一起使用的 32 位兼容共享库路径列表。

**`ldconfig_insecure`** (`bool`) ldconfig(8) 实用程序通常拒绝使用除 root 外任何人可写的目录。将此变量设为 “`YES`” 以在系统启动期间禁用该安全检查。

**`ldconfig_local_dirs`** (`str`) 设为本地 ldconfig(8) 目录列表。所列目录中所有文件的名称将作为参数传递给 ldconfig(8)。

**`ldconfig_local32_dirs`** (`str`) 设为本地 32 位兼容 ldconfig(8) 目录列表。所列目录中所有文件的名称将作为参数传递给 “`ldconfig` `-32`”。

**`kern_securelevel_enable`** (`bool`) 设为 “`YES`” 以在系统启动时设置内核安全级别。

**`kern_securelevel`** (`int`) 启动时设置的内核安全级别。`value` 的允许范围从 -1（编译时默认值）到 3（最安全）。可能的安全级别及其对系统操作的影响列表请参见 [security(7)](../man7/security.7.md)。

**`sshd_program`** (`str`) SSH 服务器程序的路径（默认为 **/usr/sbin/sshd**）。

**`sshd_enable`** (`bool`) 设为 “`YES`” 以在系统引导时启动 sshd(8)。注意，`sshd_oomprotect` 变量在 **/etc/defaults/rc.conf** 中默认设为 “`YES`”。

**`sshd_flags`** (`str`) 如果 `sshd_enable` 设为 “`YES`”，这些是传递给 sshd(8) 守护进程的标志。

**`watchdogd_enable`** (`bool`) 如果设为 “`YES`”，在引导时启动 [watchdogd(8)](../man8/watchdogd.8.md) 守护进程。这要求内核已编译 [watchdog(4)](../man4/watchdog.4.md) 兼容设备。

**`watchdogd_flags`** (`str`) 如果 `watchdogd_enable` 设为 “`YES`”，这些是传递给 [watchdogd(8)](../man8/watchdogd.8.md) 守护进程的标志。

**`watchdogd_timeout`** (`int`) 如果 `watchdogd_enable` 设为 “`YES`”，这是 [watchdogd(8)](../man8/watchdogd.8.md) 守护进程将使用的超时时间。如果设置了此选项，它将覆盖 `watchdogd_flags` 中的 `-t`。

**`watchdogd_shutdown_timeout`** (`int`) 如果 `watchdogd_enable` 设为 “`YES`”，这是 [watchdogd(8)](../man8/watchdogd.8.md) 守护进程在系统关机期间退出时设置的超时时间。当返回单用户模式或使用 [service(8)](../man8/service.8.md) 命令或 rc.d 脚本单独停止 watchdogd 服务时，不会设置此超时。请注意，如果在 [rc(8)](../man8/rc.8.md) 框架之外停止 [watchdogd(8)](../man8/watchdogd.8.md)，将应用此超时。如果设置了此选项，它将覆盖 `watchdogd_flags` 中的 `-x`。

**`devfs_rulesets`** (`str`) 包含 devfs(8) 规则集的文件列表。

**`devfs_system_ruleset`** (`str`) 应用于系统 **/dev** 本身的规则名。

**`devfs_set_rulesets`** (`str`) 已挂载 `dev` 目录和应应用于它们的规则集的对。例如：/mount/dev=ruleset_name

**`devfs_load_rulesets`** (`bool`) 如果设置，始终加载 `devfs_rulesets` 中列出的默认规则集。

**`performance_cx_lowest`** (`str`) 使用交流电源时要使用的 CPU 空闲状态。字符串 “`LOW`” 表示 [acpi(4)](../man4/acpi.4.md) 应使用可用的最低功耗状态，而 “`HIGH`” 表示应使用最低延迟状态（较少节能）。

**`performance_cpu_freq`** (`str`) 使用交流电源时要使用的 CPU 时钟频率。字符串 “`LOW`” 表示 [cpufreq(4)](../man4/cpufreq.4.md) 应使用可用的最低频率，而 “`HIGH`” 表示应使用最高频率（较少节能）。

**`economy_cx_lowest`** (`str`) 不使用交流电源时要使用的 CPU 空闲状态。字符串 “`LOW`” 表示 [acpi(4)](../man4/acpi.4.md) 应使用可用的最低功耗状态，而 “`HIGH`” 表示应使用最低延迟状态（较少节能）。

**`economy_cpu_freq`** (`str`) 不使用交流电源时要使用的 CPU 时钟频率。字符串 “`LOW`” 表示 [cpufreq(4)](../man4/cpufreq.4.md) 应使用可用的最低频率，而 “`HIGH`” 表示应使用最高频率（较少节能）。

**`jail_enable`** (`bool`) 如果设为 “`NO`”，不会启动任何已配置的 Jail。

**`jail_conf`** (`str`) [jail(8)](../man8/jail.8.md) 实用程序使用的配置文件名。默认值为 **/etc/jail.conf**。如果在 `jail_list` 中设置了 <`jname`>，还将使用 **/etc/jail.**<`jname`>`.conf` 和 **/etc/jail.conf.d/**<`jname`>`.conf`。

**`jail_parallel_start`** (`bool`) 如果设为 “`YES`”，所有已配置的 Jail 将在后台（并行）启动。

**`jail_flags`** (`str`) 默认未设置。设置后，用作 `jail_list` 中每个 Jail 的 `jail_`<`jname`>`_flags` 的默认值。

**`jail_list`** (`str`) 空格分隔的 Jail 名称列表。留空时，将启动配置文件中定义的所有 [jail(8)](../man8/jail.8.md) 实例。此列表中指定的名称控制 Jail 启动顺序。`jail_list` 中缺失的 [jail(8)](../man8/jail.8.md) 实例必须手动启动。请注意，配置文件中 Jail 的 `depend` 参数可能会覆盖此列表。

**`jail_reverse_stop`** (`bool`) 设为 “`YES`” 时，`jail_list` 中所有已配置的 Jail 将按相反顺序停止。

**`jail_`**\* 变量 请注意，较早的版本通过 `ldconfig` 变量支持每 Jail 配置。例如，名为 `vjail` 的 Jail 的主机名可以通过 `jail_vjail_hostname` 设置。这些每 Jail 配置变量现在已被 [jail(8)](../man8/jail.8.md) 配置文件取代。为了向后兼容，当定义了每 Jail 配置变量时，会创建 **/var/run/jail.**<`jname`>`.conf` 并使用。[jail(8)](../man8/jail.8.md) 配置文件由 `rc.d/jail` 脚本从其对应的 `ldconfig` 变量中处理以下每 Jail 参数。除这些之外，`jail_`<`jname`>`_parameters` 中的参数将添加到配置文件中。它们必须是以分号（`;`）分隔的 “key=value” 列表。更多详情请参见 [jail(8)](../man8/jail.8.md) 手册页。

**`harvest_mask`** (`int`) 设为表示你希望收集的熵源的位掩码。更多信息请参见 [random(4)](../man4/random.4.md)。

**`entropy_dir`** (`str`) 设为 “`NO`” 以禁用通过 cron(8) 缓存熵。否则设为存储熵文件的目录。要有效，必须有一个定期写入和轮转文件此处文件的系统 cron 作业。引导时会使用找到的所有文件。默认为 **/var/db/entropy**。

**`entropy_file`** (`str`) 设为 “`NO`” 以禁用通过重启缓存熵。否则设为用于存储缓存熵的文件名。此文件应位于 [fstab(5)](fstab.5.md) 中指定的所有卷挂载之前可读的文件系统上。默认使用 **/entropy**，但如果找到 **/var/db/entropy-file** 也会使用。这对 bsdinstall(8) 有用。

**`entropy_boot_file`** (`str`) 设为 “`NO`” 以禁用通过重启的非常早期缓存熵。否则设为用于读取非常早期重启缓存熵的文件名。此文件应位于 [loader(8)](../man8/loader.8.md) 可读取的位置。另请参见 loader.conf(5)。默认位置为 **/boot/entropy**。

**`entropy_save_sz`** (`int`) `save-entropy` 定期保存的熵缓存文件大小。

**`entropy_save_num`** (`int`) `save-entropy` 定期保存的熵缓存文件数量。

**`ipsec_enable`** (`bool`) 设为 “`YES`” 以在引导时对 `ipsec_file` 运行 setkey(8)。

**`ipsec_file`** (`str`) setkey(8) 的配置文件。

**`dmesg_enable`** (`bool`) 设为 “`YES`” 以在引导时将 [dmesg(8)](../man8/dmesg.8.md) 保存到 **/var/run/dmesg.boot**。

**`rcshutdown_timeout`** (`int`) 如果设置，在后台启动一个看门狗定时器，如果 [shutdown(8)](../man8/shutdown.8.md) 在指定时间（秒）内未完成，将终止 `rc.shutdown`。注意，除此外软超时外，[init(8)](../man8/init.8.md) 还对 `rc.shutdown` 的执行应用硬超时。这通过 [sysctl(8)](../man8/sysctl.8.md) 变量 `kern.init_shutdown_timeout` 配置，默认为 120 秒。将 `rcshutdown_timeout` 的值设为超过 120 秒在 [sysctl(8)](../man8/sysctl.8.md) 变量 `kern.init_shutdown_timeout` 也增加之前无效。

**`virecover_enable`** (`bool`) 设为 “`NO`” 以防止系统尝试恢复过早终止的 [vi(1)](../man1/vi.1.md) 会话。

**`ugidfw_enable`** (`bool`) 设为 “`YES`” 以在系统初始化时加载 [mac_bsdextended(4)](../man4/mac_bsdextended.4.md) 模块并加载默认规则集文件。

**`bsdextended_script`** (`str`) 要加载的默认 [mac_bsdextended(4)](../man4/mac_bsdextended.4.md) 规则集文件。此变量的默认值为 **/etc/rc.bsdextended**。

**`newsyslog_enable`** (`bool`) 如果设为 “`YES`”，在启动时运行 newsyslog(8) 命令。

**`newsyslog_flags`** (`str`) 如果 `newsyslog_enable` 设为 “`YES`”，这些是传递给 newsyslog(8) 程序的标志。默认为 “`-CN`”，这会创建带有 `C` 标志的日志文件。

**`mdconfig_md`**<`X`> (`str`) [md(4)](../man4/md.4.md) 设备 `X` 的 mdconfig(8) 参数。至少必须指定 `-t` `type`，以及用于 malloc 或 swap 支持的 [md(4)](../man4/md.4.md) 设备的 `-s` `size` 或用于 vnode 支持的 [md(4)](../man4/md.4.md) 设备的 `-f` `file`。注意，`mdconfig_md`<`X`> 变量会被评估直到某个变量未设置或为空。

**`mdconfig_md`**<`X`>`_newfs` (`str`) 传递给 newfs(8) 以初始化 [md(4)](../man4/md.4.md) 设备 `X` 的可选参数。

**`mdconfig_md`**<`X`>`_owner` (`str`) 在指定 [md(4)](../man4/md.4.md) 设备 `X` 挂载后传递给 [chown(8)](../man8/chown.8.md) 的所有权规范。[md(4)](../man4/md.4.md) 设备和挂载点都会被更改。

**`mdconfig_md`**<`X`>`_perms` (`str`) 在指定 [md(4)](../man4/md.4.md) 设备 `X` 挂载后传递给 [chmod(1)](../man1/chmod.1.md) 的模式字符串。[md(4)](../man4/md.4.md) 设备和挂载点都会被更改。

**`mdconfig_md`**<`X`>`_files` (`str`) 在 [md(4)](../man4/md.4.md) 设备 `X` 挂载后要复制到其挂载点的文件。

**`mdconfig_md`**<`X`>`_cmd` (`str`) 在指定 [md(4)](../man4/md.4.md) 设备 `X` 挂载后要执行的命令。注意，命令传递给 `eval`，且 `_dev` 和 `_mp` 变量可用于分别引用 [md(4)](../man4/md.4.md) 设备和挂载点。假设 [md(4)](../man4/md.4.md) 设备为 `md0`，可以设置如下：

**`autobridge_interfaces`** (`str`) 设为将检查新到达接口以自动添加的桥接接口列表。如果未设为 “`NO`”，对于值中的每个空白分隔 `element`，假定存在一个 `autobridge_`<`element`> 变量，其中包含要匹配的接口名空白分隔列表，这些名称可使用通配符。例如：

**`mixer_enable`** (`bool`) 如果设为 “`YES`”，启用声音混音器支持。

**`hcsecd_enable`** (`bool`) 如果设为 “`YES`”，启用蓝牙安全守护进程。

**`hcsecd_config`** (`str`) hcsecd(8) 的配置文件。默认为 **/etc/bluetooth/hcsecd.conf**。

**`sdpd_enable`** (`bool`) 如果设为 “`YES`”，启用蓝牙服务发现协议守护进程。

**`sdpd_control`** (`str`) sdpd(8) 控制套接字的路径。默认为 **/var/run/sdp**。

**`sdpd_groupname`** (`str`) 设置 sdpd(8) 初始化后以哪个组运行。默认为 “`nobody`”。

**`sdpd_username`** (`str`) 设置 sdpd(8) 初始化后以哪个用户运行。默认为 “`nobody`”。

**`bthidd_enable`** (`bool`) 如果设为 “`YES`”，启用蓝牙人机接口设备守护进程。

**`bthidd_config`** (`str`) bthidd(8) 的配置文件。默认为 **/etc/bluetooth/bthidd.conf**。

**`bthidd_hids`** (`str`) bthidd(8) 存储已知 HID 设备信息的文件路径。默认为 **/var/db/bthidd.hids**。

**`rfcomm_pppd_server_enable`** (`bool`) 如果设为 “`YES`”，启用蓝牙 RFCOMM PPP 包装守护进程。

**`rfcomm_pppd_server_profile`** (`str`) 从 **/etc/ppp/ppp.conf** 使用的配置文件名。此处可指定多个配置文件。也用于指定每配置文件的覆盖。当配置文件名包含 “`.-/+`” 中的任何字符时，对于覆盖变量名，它们会转换为 “`_`”。

**`rfcomm_pppd_server_`**<`profile`>`_bdaddr` (`str`) 覆盖要监听的本地地址。默认情况下 rfcomm_pppd(8) 会监听 “`ANY`” 地址。地址可以指定为 BD_ADDR 或名称。

**`rfcomm_pppd_server_`**<`profile`>`_channel` (`str`) 覆盖要监听的本地 RFCOMM 通道。默认情况下 rfcomm_pppd(8) 会监听 RFCOMM 通道 1。如果同时使用多个配置文件，必须正确设置。

**`rfcomm_pppd_server_`**<`profile`>`_register_sp` (`bool`) 告知 rfcomm_pppd(8) 是否应在指定 RFCOMM 通道上注册串口服务。默认为 “`NO`”。

**`rfcomm_pppd_server_`**<`profile`>`_register_dun` (`bool`) 告知 rfcomm_pppd(8) 是否应在指定 RFCOMM 通道上注册拨号网络服务。默认为 “`NO`”。

**`ubthidhci_enable`** (`bool`) 如果设为 “`YES`”，将 USB 蓝牙控制器从 HID 模式更改为 HCI 模式。你还需要使用 `ubthidhci_busnum` 和 `ubthidhci_addr` 变量指定 USB 蓝牙控制器的位置。

**`ubthidhci_busnum`** USB 蓝牙控制器所在的总线号。检查系统上 usbconfig(8) 的输出以查找此信息。

**`ubthidhci_addr`** USB 蓝牙控制器的总线地址。检查系统上 usbconfig(8) 的输出以查找此信息。

**`utx_enable`** (`bool`) 设为 “`YES`” 以通过 utx(8) 设施启用用户记账。

**`netwait_enable`** (`bool`) 如果设为 “`YES`”，延迟启动依赖网络的服务，直到 `netwait_if` 启动、重复地址发现（DAD）完成，并且到 `netwait_ip` 中定义的目标的 ICMP 数据包流通。首先检查链路状态，然后是 DAD，然后 “`ping`” 一个 IP 地址以验证网络可用性。如果无法到达任何目标或超过超时，网络服务仍会启动，但不保证网络可用。

**`netwait_ip`** (`str`) 默认为空。此变量包含要 [ping(8)](../man8/ping.8.md) 的 IP 地址的空格分隔列表。不应使用 DNS 主机名，因为此时无法保证解析功能。如果指定了多个 IP 地址，将依次尝试直到成功或列表耗尽。

**`netwait_timeout`** (`int`) 表示对 `netwait_ip` 中每个 IP 地址执行 “`ping`” 的总秒数，速率为每秒一次 ping。如果任何 ping 成功，则认为完整的网络连接是可靠的。默认为 60。

**`netwait_if`** (`str`) 默认为空。定义要监视链路的网络接口名。使用 [ifconfig(8)](../man8/ifconfig.8.md) 监视接口，查找 “`status: no carrier`”。一旦消失，则认为链路已启动。如果需要，这可以是 [vlan(4)](../man4/vlan.4.md) 接口。

**`netwait_if_timeout`** (`int`) 定义等待链路变为可用的总秒数，以 1 秒间隔轮询。默认为 30。

**`netwait_dad`** (`str`) 默认设为 “`NO`”。设为 “`YES`” 以启用等待 DAD 完成。

**`netwait_dad_timeout`** (`int`) 默认未设置。表示等待 DAD 完成的最大秒数。如果为零或未设置，超时将为 `net.inet6.ip6.dad_count` sysctl 变量值加一。

**`rctl_enable`** (`bool`) 如果设为 “`YES`”，从定义的规则集加载 rctl(8) 规则。内核必须构建 `options RACCT` 和 `options RCTL`。

**`rctl_rules`** (`str`) 默认设为 **/etc/rctl.conf**。此变量包含要为 rctl(8) 加载的 [rctl.conf(5)](rctl.conf.5.md) 规则集。

**`iovctl_files`** (`str`) iovctl(8) 使用的配置文件的空格分隔列表。默认值为空字符串。

**`autofs_enable`** (`bool`) 如果设为 “`YES`”，在引导时启动 automount(8) 实用程序以及 automountd(8) 和 [autounmountd(8)](../man8/autounmountd.8.md) 守护进程。

**`automount_flags`** (`str`) 如果 `autofs_enable` 设为 “`YES`”，这些是传递给 automount(8) 程序的标志。默认不传递任何标志。

**`automountd_flags`** (`str`) 如果 `autofs_enable` 设为 “`YES`”，这些是传递给 automountd(8) 守护进程的标志。默认不传递任何标志。

**`autounmountd_flags`** (`str`) 如果 `autofs_enable` 设为 “`YES`”，这些是传递给 [autounmountd(8)](../man8/autounmountd.8.md) 守护进程的标志。默认不传递任何标志。

**`ctld_enable`** (`bool`) 如果设为 “`YES`”，在引导时启动 ctld(8) 守护进程。

**`iscsid_enable`** (`bool`) 如果设为 “`YES`”，在引导时启动 iscsid(8) 守护进程。

**`iscsictl_enable`** (`bool`) 如果设为 “`YES`”，在引导时启动 iscsictl(8) 实用程序。

**`iscsictl_flags`** (`str`) 如果 `iscsictl_enable` 设为 “`YES`”，这些是传递给 iscsictl(8) 程序的标志。默认为 “`-Aa`”，基于 **/etc/iscsi.conf** 配置文件配置会话。

**`cfumass_enable`** (`bool`) 如果设为 “`YES`”，在引导时使用 [cfumass(4)](../man4/cfumass.4.md) 创建并导出 USB LUN。

**`cfumass_dir`** (`str`) USB LUN 导出文件所在的目录。默认目录为 **/var/cfumass**。

**`service_delete_empty`** (`bool`) 如果设为 “`YES`”，`Li service delete` 会删除空的 “`rc.conf.d`” 文件。

**`zfs_bootonce_activate`** (`bool`) 如果设为 “`YES`”，且标记为 bootonce 的引导环境成功引导，它将被永久激活。

**`zfskeys_enable`** (`bool`) 如果设为 “`YES`”，启用加密 ZFS 数据集的加密密钥自动加载。对于每个数据集，脚本会先加载适当的加密密钥，然后尝试解锁数据集。脚本仅对使用 ZFS 原生加密且具有以 “`file://`” 开头的 ZFS “`keylocation`” 数据集属性的数据集进行操作。

**`zfskeys_datasets`** (`str`) 要解锁的 ZFS 数据集的空白分隔列表。默认列表为空，表示脚本会尝试解锁所有数据集。

**`zfskeys_timeout`** (`int`) 定义等待 zfskeys 脚本解锁加密数据集的总秒数。默认为 10。

**`sendmail_enable`** (`str`) 如果设为 “`YES`”，在系统引导时运行 sendmail(8) 守护进程。如果设为 “`NO`”，不运行 sendmail(8) 守护进程监听传入的网络邮件。这不会阻止 sendmail(8) 守护进程监听环回接口的 SMTP 端口。“`NONE`” 选项将每个 `sendmail_enable`、`sendmail_submit_enable`、`sendmail_outbound_enable`、`sendmail_msp_queue_enable` 设为 “`NO`”。

**`sendmail_cert_create`** (`str`) 如果 `sendmail_enable` 设为 “`YES`”，创建由 **/etc/mail/certs/cacert.pem** 中的 CA 证书签名的签名证书 **/etc/mail/certs/host.cert**，代表 **/etc/mail/certs/host.key**。这将使连接的主机能协商 STARTTLS，允许传入电子邮件在传输中加密。sendmail(8) 需要配置为使用这些生成的文件。**/etc/mail/freebsd.mc** 中的默认配置已包含所需选项。

**`sendmail_cert_cn`** (`str`) 如果 `sendmail_enable` 设为 “`YES`” 且 `sendmail_cert_create` 设为 “`YES`”，这是将创建的证书的通用名（CN）。如果未设置 `sendmail_cert_cn`，将使用系统的主机名。如果未设置主机名，则使用 “`amnesiac`”。

**`sendmail_flags`** (`str`) 如果 `sendmail_enable` 设为 “`YES`”，这些是传递给 sendmail(8) 守护进程的标志。

**`sendmail_submit_enable`** (`bool`) 如果设为 “`YES`” 且 `sendmail_enable` 设为 “`NO`”，使用 `sendmail_submit_flags` 而非 `sendmail_flags` 运行 sendmail(8)。这旨在允许通过仅监听 localhost 的 SMTP 服务进行本地邮件提交，这是将 sendmail(8) 作为非 set-user-ID 二进制文件运行所必需的。请注意，这在 jail(2) 系统中不起作用，因为 Jail 不允许仅绑定到 localhost 接口。

**`sendmail_submit_flags`** (`str`) 如果 `sendmail_enable` 设为 “`NO`” 且 `sendmail_submit_enable` 设为 “`YES`”，这些是传递给 sendmail(8) 守护进程的标志。

**`sendmail_outbound_enable`** (`bool`) 如果设为 “`YES`” 且 `sendmail_enable` 和 `sendmail_submit_enable` 都设为 “`NO`”，使用 `sendmail_outbound_flags` 而非 `sendmail_flags` 运行 sendmail(8)。这旨在允许不提供监听 SMTP 服务的系统进行本地邮件队列管理。

**`sendmail_outbound_flags`** (`str`) 如果 `sendmail_enable` 和 `sendmail_submit_enable` 都设为 “`NO`” 且 `sendmail_outbound_enable` 设为 “`YES`”，这些是传递给 sendmail(8) 守护进程的标志。

**`sendmail_msp_queue_enable`** (`bool`) 如果设为 “`YES`”，在系统引导时启动客户端（MSP）队列运行器 sendmail(8) 守护进程。从 sendmail 8.12 起，命令行提交使用单独的队列。客户端队列运行器确保提交队列中不留任何内容。

**`sendmail_msp_queue_flags`** (`str`) 如果 `sendmail_msp_queue_enable` 设为 “`YES`”，这些是传递给 sendmail(8) 守护进程的标志。

**`precious_machine`** 如果设为 “`YES`”，某些破坏性操作需要先移除特定于操作的安全带才能允许。例如，创建 **/var/run/noshutdown** 文件以防止对错误机器执行 [shutdown(8)](../man8/shutdown.8.md)。

**`virtual_oss_enable`** (`bool`) 如果设为 “`YES`”，为 `virtual_oss_configs` 中定义的每个配置运行一个 virtual_oss(8) 实例。

**`virtual_oss_configs`** (`str`) virtual_oss(8) 配置的空格分隔列表。例如：配置需要在 `virtual_oss_`<`config_name`> 中定义。默认情况下，有一个 `dsp` 配置，它用 virtual_oss(8) 设备替换由 sound(4) 创建的 **/dev/dsp** 设备。可以通过设置 `virtual_oss_dsp` 变量重新定义它。

**`virtual_oss_`**<`config_name`> (`str`) 配置 <`config_name`> 的 virtual_oss(8) 参数列表。

**`virtual_oss_default_control_device`** (`str`) 对应于默认配置 `virtual_oss_dsp` 的 virtual_oss(8) 控制设备名。默认设为 `vdsp.ctl`。设置 `virtual_oss_dsp` 时，强烈建议也设置此变量，并将其用作 `virtual_oss_dsp` 中 `-t` 选项的参数，因为它被其他程序和脚本（如 **/etc/devd/snd.conf**）使用。

## 服务 Jail

rc 系统的服务 Jail 部分会自动将服务放入 Jail 中。此 Jail 根据 <`name`>`_svcj_options` 变量的内容继承父级的文件系统和各种其他部分（如果在 Jail 中允许子 Jail，则服务 Jail 可在 Jail 中使用）。通常此变量在 rc 脚本中设置，但可在 rc 配置中覆盖。<`name`>`_svcj_options` 的有效选项有：

**mlock** 允许将内存页锁定在物理内存中。

**netv4** 允许 IPv4 网络访问以及绑定到保留端口的能力。如果设置了 <`name`>`_svcj_ipaddrs`，则 Jail 仅能看到其中列出的 IPv4 地址，否则所有已分配的 IPv4 地址都可见。这不能与 `netv6` 组合。

**netv6** 允许 IPv6 网络访问以及绑定到保留端口的能力。如果设置了 <`name`>`_svcj_ipaddrs`，则 Jail 仅能看到其中列出的 IPv6 地址，否则所有已分配的 IPv6 地址都可见。这不能与 `netv4` 组合。

**net_basic** 等同于同时启用 `netv6` 和 `netv4`。

**net_raw** 允许打开原始套接字。此选项可与 `netv4`、`netv6`、`net_basic` 组合。

**net_all** 允许如 `netv4` 和 `netv6` 那样的 IPv6 和 IPv4 网络访问，允许打开原始套接字，并允许打开尚未添加 Jail 功能的协议栈的套接字。

**nfsd** 允许运行 nfsd 及其关联守护进程。

**routing** 允许修改系统路由表。

**settime** 允许设置和调整系统时间。

**sysvipc** 从主机或父 Jail 继承 SysV 信号量、SysV 共享内存和 SysV 消息。

**sysvipcnew** 为此特定服务 Jail 创建新的 SysV 信号量、SysV 共享内存和 SysV 消息命名空间。

**vmm** 允许访问 [vmm(4)](../man4/vmm.4.md)。此选项仅在内核中启用 [vmm(4)](../man4/vmm.4.md) 时可用。

所有非网络选项都可与其他所有选项组合。SysV 选项中只能指定一个。如果 <`name`>`_svcj` 变量设为 “`YES`”，此特定服务将在名为 `svcj-``name` 的服务 Jail 中启动。`svcj_all_enable` 变量允许一次性为系统所有服务启用服务 Jail。<`name`>`_svcj` 设为 “`NO`” 的服务被排除。某些服务可能在脚本中将 <`name`>`_svcj` 设为 “`NO`”，以完全阻止此服务的服务 Jail，或者在 rc 配置中未设置时将其设为 “`NO`”，以从 `svcj_all_enable` 中排除但允许显式启用。例如，sshd 服务作为服务 Jail 运行时不会看到其他 Jail。这可能是也可能不是所需的行为，因此它被排除在 `svcj_all_enable` 之外，但可以通过将 `sshd_svcj` 设为 “`YES`” 启用。

## 文件

**/etc/defaults/rc.conf**

**/etc/defaults/vendor.conf**

**/etc/rc.conf**

**/etc/rc.conf.local**

**/etc/rc.conf.d/**

## 参见

[chmod(1)](../man1/chmod.1.md), cpuset(1), gdb(1) (`ports/devel/gdb`), kbdcontrol(1), [limits(1)](../man1/limits.1.md), protect(1), [sh(1)](../man1/sh.1.md), umask(1), [uuidgen(1)](../man1/uuidgen.1.md), [vi(1)](../man1/vi.1.md), vidcontrol(1), [bridge(4)](../man4/bridge.4.md), [dummynet(4)](../man4/dummynet.4.md), [ip(4)](../man4/ip.4.md), ipf(4), ipfw(4), ipnat(4), [kld(4)](../man4/kld.4.md), [pf(4)](../man4/pf.4.md), [pflog(4)](../man4/pflog.4.md), [pfsync(4)](../man4/pfsync.4.md), [tcp(4)](../man4/tcp.4.md), [udp(4)](../man4/udp.4.md), exports(5), [fstab(5)](fstab.5.md), ipf(5), ipnat(5), jail.conf(5), loader.conf(5), login.conf(5), [motd(5)](motd.5.md), newsyslog.conf(5), [pf.conf(5)](pf.conf.5.md), [firewall(7)](../man7/firewall.7.md), [growfs(7)](../man7/growfs.7.md), [security(7)](../man7/security.7.md), [tuning(7)](../man7/tuning.7.md), accton(8), apm(8), bsdinstall(8), bthidd(8), chkprintcap(8), [chown(8)](../man8/chown.8.md), cron(8), devfs(8), dhclient(8), geli(8), hcsecd(8), [ifconfig(8)](../man8/ifconfig.8.md), [inetd(8)](../man8/inetd.8.md), iovctl(8), ipf(8), [ipfw(8)](../man8/ipfw.8.md), ipnat(8), [jail(8)](../man8/jail.8.md), [kldxref(8)](../man8/kldxref.8.md), [loader(8)](../man8/loader.8.md), lpd(8), makewhatis(8), mdconfig(8), mdmfs(8), mixer(8), mountd(8), [moused(8)](../man8/moused.8.md), newfs(8), newsyslog(8), nfsd(8), ntpd(8), ntpdate(8), pfctl(8), pflogd(8), [ping(8)](../man8/ping.8.md), [powerd(8)](../man8/powerd.8.md), quotacheck(8), quotaon(8), [rc(8)](../man8/rc.8.md), [rc.subr(8)](../man8/rc.subr.8.md), [rcorder(8)](../man8/rcorder.8.md), rfcomm_pppd(8), [route(8)](../man8/route.8.md), [route6d(8)](../man8/route6d.8.md), [routed(8)](../man8/routed.8.md), rpc.lockd(8), rpc.statd(8), rpc.tlsclntd(8), rpc.tlsservd(8), rpcbind(8), rwhod(8), savecore(8), sdpd(8), sendmail(8), [service(8)](../man8/service.8.md), sshd(8), swapon(8), [sysctl(8)](../man8/sysctl.8.md), syslogd(8), [sysrc(8)](../man8/sysrc.8.md), unbound(8), usbconfig(8), utx(8), virtual_oss(8), wlandebug(8), [yp(8)](../man8/yp.8.md), ypbind(8), ypserv(8), ypset(8)

## 历史

`save-entropy` 文件出现于 FreeBSD 2.2.2。

## 作者

Jordan K. Hubbard.
