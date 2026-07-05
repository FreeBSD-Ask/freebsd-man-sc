# make.conf.5

`make.conf` — 系统构建信息

## 名称

`make.conf`

## 描述

`make.conf` 文件包含的系统级设置将应用于使用 [make(1)](../man1/make.1.md) 和标准 `sys.mk` 文件的每次构建。其实现方式如下：[make(1)](../man1/make.1.md) 默认会在任何其他文件之前处理系统 makefile `sys.mk`，而 `sys.mk` 包含了 `make.conf`。

`make.conf` 文件使用标准的 makefile 语法。但是，`make.conf` 不应向 [make(1)](../man1/make.1.md) 指定任何依赖关系。相反，`make.conf` 用于设置控制其他 makefile 行为的 [make(1)](../man1/make.1.md) 变量。

`make.conf` 的默认位置是 **/etc/make.conf**，但可以在 [make(1)](../man1/make.1.md) 变量 `__MAKE_CONF` 中指定其他位置。如果系统级设置不适合特定构建，可能需要覆盖 `make.conf` 的位置。例如，将 `__MAKE_CONF` 设置为 **/dev/null** 会将所有构建控制有效地重置为默认值。

`make.conf` 的主要目的是控制 FreeBSD 源码、文档和移植应用程序的编译，它们通常位于 **/usr/src**、**/usr/doc** 和 **/usr/ports**。通常，当某些控制变量的值需要从默认值更改时，系统管理员会创建 `make.conf`。

系统构建过程涉及四个主要方面：world、内核、文档和 Ports。在 `make.conf` 中设置的变量可能适用于其中之一、之二或全部四个方面。此外，可以通过 [make(1)](../man1/make.1.md) 的 `-D` 选项或 [environ(7)](../man7/environ.7.md) 为特定构建指定控制变量。对于 world 和内核构建，可以将这些变量放入 [src.conf(5)](src.conf.5.md) 而不是 `make.conf`。这样，文档和 Ports 构建的环境就不会被无关的变量所污染。

以下列表提供了在指定构建期间可使用的每个变量的名称和简要说明。标记为 `bool` 的变量的值会被忽略；只要设置了该变量（即使设置为 “`FALSE`” 或 “`NO`”），就会被视为已设置。

以下列表提供了用于所有构建，或被 `makefiles` 用于构建以外的其他事项的变量的名称和简要说明。

```sh
INSTALL+= -C
```

```sh
MAKE_SHELL?=sh
```

**`ALWAYS_CHECK_MAKE`**（`bool`）指示源码树中的顶层 makefile（通常是 **/usr/src**）始终检查 [make(1)](../man1/make.1.md) 是否为最新。通常仅对 world 和 buildworld 目标执行此操作，以处理从旧版 FreeBSD 的升级。

**`CFLAGS`**（`str`）控制编译 C 代码时的编译器设置。不支持 `-O` 和 `-O2` 以外的优化级别。

**`CPUTYPE`**（`str`）控制生成代码时面向的处理器。这控制某些代码（当前仅 OpenSSL）中特定于处理器的优化，并修改 `CFLAGS` 和 `COPTFLAGS` 的值，使其包含对 [cc(1)](../man1/cc.1.md) 的适当优化指令。要设置 `CPUTYPE` 的值，请使用 “`?=`” 而不是 “`=`”，以便 [make(1)](../man1/make.1.md) 的目标可以覆盖它。可以使用 `NO_CPU_CFLAGS` 变量覆盖 `CFLAGS` 的自动设置。有关可识别的 `CPUTYPE` 选项列表，请参见 **/usr/share/examples/etc/make.conf**。

**`CXXFLAGS`**（`str`）控制编译 C++ 代码时的编译器设置。`CXXFLAGS` 初始设置为 `CFLAGS` 的值。如果要向 `CXXFLAGS` 值中追加内容，请使用 “`+=`” 而不是 “`=`”。

**`DTC`**（`str`）选择用于 DTS（设备树语法）文件的编译器。`DTC` 初始设置为 dtc 的值。

**`INSTALL`**（`str`）默认的安装命令。要仅安装目标不同或不存在的文件，请使用 `-C`。注意，某些 makefile（包括 **/usr/share/mk** 中的）可能会为所提供的安装命令硬编码选项。

**`LOCAL_DIRS`**（`str`）在此变量中列出在 **/usr/src** 中执行 make 时应进入的任何目录。

**`MAKE_SHELL`**（`str`）控制 [make(1)](../man1/make.1.md) 在内部用于处理 makefile 中命令脚本的 shell。当前支持 [sh(1)](../man1/sh.1.md)、ksh(1) 和 [csh(1)](../man1/csh.1.md)。

**`MTREE_FOLLOWS_SYMLINKS`**（`str`）将其设置为 “`-L`” 以使 [mtree(8)](../man8/mtree.8.md) 跟随符号链接。

**`NO_CPU_CFLAGS`**（`str`）设置此变量将防止在编译时自动向 `CFLAGS` 添加特定于 CPU 的编译器标志。

### 构建内核

以下列表提供了仅在内核构建期间使用的变量的名称和简要说明：

```sh
KERNCONF=MINE DEBUG GENERIC OTHERMACHINE
```

**`BOOTWAIT`**（`int`）控制内核在引导默认内核之前等待控制台按键的时间长度。该值约为毫秒。在从磁盘引导之前，BIOS 会接受按键，因此即使将其设置为 0，也可以给出自定义引导参数。

**`COPTFLAGS`**（`str`）控制构建内核时的编译器设置。不保证高于 `-O`（`-O2` 等）的优化级别能正常工作。

**`KERNCONF`**（`str`）控制由 “`${MAKE} buildkernel`” 构建并由 “`${MAKE} installkernel`” 安装的内核配置。例如，将构建由配置文件 `MINE`、`DEBUG`、`GENERIC` 和 `OTHERMACHINE` 指定的内核，并安装由配置文件 `MINE` 指定的内核。默认值为 `GENERIC`。

**`MODULES_OVERRIDE`**（`str`）设置为要构建的模块列表，而不是构建全部模块。

**`NO_KERNELCLEAN`**（`bool`）设置此项以在 “`${MAKE} buildkernel`” 期间跳过运行 “`${MAKE} clean`”。

**`NO_KERNELCONFIG`**（`bool`）设置此项以在 “`${MAKE} buildkernel`” 期间跳过运行 [config(8)](../man8/config.8.md)。

**`NO_KERNELOBJ`**（`bool`）设置此项以在 “`${MAKE} buildkernel`” 期间跳过运行 “`${MAKE} obj`”。

**`NO_MODULES`**（`bool`）设置此项以不随内核构建模块。

**`PORTS_MODULES`** 将此项设置为每次构建内核时希望重新构建的 ports 列表。

**`WITHOUT_MODULES`**（`str`）设置为要从构建中排除的模块列表。与指定 `MODULES_OVERRIDE` 相比，这提供了一种更简单的方式来排除你确信永远不会需要的模块。它在 `MODULES_OVERRIDE` *之后* 应用。

### 构建 world

以下列表提供了在 world 构建期间使用的变量的名称和简要说明：

```sh
SENDMAIL_CFLAGS=-I/usr/local/include -DSASL
SENDMAIL_LDFLAGS=-L/usr/local/lib
SENDMAIL_LDADD=-lsasl
```

**`BOOT_COMCONSOLE_PORT`**（`str`）如果引导块已配置为使用串行控制台而不是键盘/显卡，则用于控制台的端口地址。

**`BOOT_COMCONSOLE_SPEED`**（`int`）如果引导块已配置为使用串行控制台而不是键盘/显卡，则用于控制台的波特率。

**`BOOT_PXELDR_ALWAYS_SERIAL`**（`bool`）将强制使用串行控制台的代码编译到 pxeboot(8) 中。这类似于 [boot(8)](../man8/boot.8.md) 块中的 `-h` 选项。

**`BOOT_PXELDR_PROBE_KEYBOARD`**（`bool`）将探测键盘的代码编译到 pxeboot(8) 中。如果未找到键盘，则以双控制台配置引导。这类似于 [boot(8)](../man8/boot.8.md) 块中的 `-D` 选项。

**`ENABLE_SUID_K5SU`**（`bool`）如果你希望使用 ksu 工具，请设置此项。否则，它将在未设置 set-user-ID 位的情况下安装。

**`ENABLE_SUID_NEWGRP`**（`bool`）设置此项以安装设置了 set-user-ID 位的 newgrp(1)。否则，newgrp(1) 将无法更改用户的组。

**`LOADER_TFTP_SUPPORT`**（`bool`）默认情况下，pxeboot(8) 加载器通过 NFS 检索内核。定义此项并重新编译 **/usr/src/stand** 将使其通过 TFTP 检索内核。这允许 pxeboot(8) 加载自定义的 BOOTS 无盘内核，同时仍挂载服务器的 **/** 而不是加载服务器的内核。

**`LOADER_FIREWIRE_SUPPORT`**（`bool`）定义此项并重新编译 **/usr/src/stand/i386** 会将 [dcons(4)](../man4/dcons.4.md) 控制台驱动程序添加到 [loader(8)](../man8/loader.8.md) 中，并允许通过 FireWire(IEEE1394) 使用 dconschat(8) 进行访问。当前仅支持 i386 和 amd64。

**`MAN_ARCH`**（`str`）以空格分隔的一个或多个 MACHINE 和/或 MACHINE_ARCH 值列表，用于安装第 4 节手册页。特殊值 ‘all’ 安装所有可用架构。它也是默认值。

**`MODULES_WITH_WORLD`**（`bool`）设置为随系统而不是随内核构建模块。

**`NO_CLEAN`**（`bool`）设置此项以在 “`make buildworld`” 期间禁用清理。除非你清楚自己在做什么，否则不应设置此项。

**`NO_CLEANDIR`**（`bool`）设置此项以运行 “`${MAKE} clean`” 而不是 “`${MAKE} cleandir`”。

**`WITH_MANCOMPRESS`**（`defined`）设置此项以压缩方式安装手册页。

**`WITHOUT_MANCOMPRESS`**（`defined`）设置此项以未压缩方式安装手册页。

**`NO_SHARE`**（`bool`）设置此项以不在 `share` 子目录中构建。

**`NO_SHARED`**（`bool`）设置此项以静态链接方式构建 **/bin** 和 **/sbin**，这可能会有问题。如果设置，每个使用 `bsd.prog.mk` 的工具都将被静态链接。

**`PKG_REPO_SIGNING_KEY`**（`str`）传递给 pkg-repo(8) 用于对构建 `packages` 目标（即 pkgbase）时创建的包进行签名的 RSA 私钥的路径。该变量在 poudriere(8) 中同名，因此在使用 poudriere 构建 pkgbase 时会自动被识别。

**`PPP_NO_NAT`**（`bool`）构建不支持网络地址转换（NAT）的 ppp(8)。

**`PPP_NO_NETGRAPH`**（`bool`）设置此项以构建不支持 Netgraph 的 ppp(8)。

**`PPP_NO_RADIUS`**（`bool`）设置此项以构建不支持 RADIUS 的 ppp(8)。

**`PPP_NO_SUID`**（`bool`）设置此项以禁止将 ppp(8) 安装为 set-user-ID root 程序。

**`SENDMAIL_ADDITIONAL_MC`**（`str`）在构建时应构建为 `.cf` 文件的附加 `.mc` 文件。该值应包含 `.mc` 文件的完整路径，例如 **/etc/mail/foo.mc**、**/etc/mail/bar.mc**。

**`SENDMAIL_ALIASES`**（`str`）使用 **/etc/mail/Makefile** 时要重建的 aliases(5) 文件列表。默认值为 **/etc/mail/aliases**。

**`SENDMAIL_CFLAGS`**（`str`）构建 sendmail(8) 时传递给编译命令的标志。`SENDMAIL_*` 标志可用于提供 SASL 支持，设置如下：

**`SENDMAIL_CF_DIR`**（`str`）覆盖用于从 `.mc` 文件构建 `.cf` 文件的 m4(1) 配置文件的默认位置。

**`SENDMAIL_DPADD`**（`str`）构建 sendmail(8) 时要添加的额外依赖项。

**`SENDMAIL_LDADD`**（`str`）构建 sendmail(8) 时添加到 [ld(1)](../man1/ld.1.md) 命令末尾的标志。

**`SENDMAIL_LDFLAGS`**（`str`）构建 sendmail(8) 时传递给 [ld(1)](../man1/ld.1.md) 命令的标志。

**`SENDMAIL_M4_FLAGS`**（`str`）从 `.mc` 文件构建 `.cf` 文件时传递给 m4(1) 的标志。

**`SENDMAIL_MAP_PERMS`**（`str`）使用 **/etc/mail/Makefile** 生成别名和映射数据库文件时使用的模式。默认值为 0640。

**`SENDMAIL_MAP_SRC`**（`str`）使用 **/etc/mail/Makefile** 时要重建的附加映射。`access`、`bitdomain`、`domaintable`、`genericstable`、`mailertable`、`uucpdomain` 和 `virtusertable` 映射如果存在，则总是被重建。

**`SENDMAIL_MAP_TYPE`**（`str`）使用 **/etc/mail/Makefile** 生成映射数据库文件时要使用的数据库映射类型。默认值为 hash。替代值为 btree。

**`SENDMAIL_MC`**（`str`）安装时使用的默认 m4(1) 配置文件。该值应包含 `.mc` 文件的完整路径，例如 **/etc/mail/myconfig.mc**。请谨慎使用，因为 make install 会覆盖任何现有的 **/etc/mail/sendmail.cf**。注意 `SENDMAIL_CF` 已弃用。

**`SENDMAIL_SET_USER_ID`**（`bool`）如果设置，将 sendmail(8) 安装为 set-user-ID root 二进制文件而不是 set-group-ID 二进制文件，并且不安装 **/etc/mail/submit.{cf,mc}**。不建议使用此标志，如果可能，应遵循 **/etc/mail/README** 中的替代建议。

**`SENDMAIL_START_SCRIPT`**（`str`）由 **/etc/mail/Makefile** 用于启动、停止和重启 sendmail(8) 的脚本。默认值为 **/etc/rc.d/sendmail**。

**`SENDMAIL_SUBMIT_MC`**（`str`）安装时使用的默认邮件提交 m4(1) 配置文件。该值应包含 `.mc` 文件的完整路径，例如 **/etc/mail/mysubmit.mc**。请谨慎使用，因为 make install 会覆盖任何现有的 **/etc/mail/submit.cf**。

**`TOP_TABLE_SIZE`**（`int`）[top(1)](../man1/top.1.md) 对用户名使用哈希表。可以调整此哈希表的大小以匹配本地用户数。表大小应为一个约等于 **/etc/passwd** 中行数两倍的素数。默认值为 20011。

**`WANT_FORCE_OPTIMIZATION_DOWNGRADE`**（`int`）使系统编译器以将高优化级别强制降低到较低级别的方式构建。已知 [cc(1)](../man1/cc.1.md) `-O2` 及以上级别会在不同时期触发已知的优化器错误。所赋值是所使用的最高优化值。

### 构建文档

以下列表提供了构建文档时使用的变量的名称和简要说明：

**`DOC_LANG`**（`str`）在 **/usr/doc** 中构建文档时要构建和安装的语言列表。

**`PRINTERDEVICE`**（`str`）**/usr/src/share/doc** 中系统文档的默认格式，取决于你的打印机。对于简单打印机，可设置为 “`ascii`”；对于带有 ghostscript 过滤器的 postscript 或图形打印机，可设置为 “`ps`”，或两者都设置。

### 构建 Ports

可以设置若干影响 Ports 构建的 make 变量。这些变量及其效果记录在 [ports(7)](../man7/ports.7.md)、`${PORTSDIR}/Mk/*` 和 FreeBSD Porter's Handbook 中。

## 文件

**/etc/make.conf**

**/usr/doc/Makefile**

**/usr/ports/Makefile**

**/usr/share/examples/etc/make.conf**

**/usr/share/mk/sys.mk**

**/usr/src/Makefile**

**/usr/src/Makefile.inc1**

## 参见

[cc(1)](../man1/cc.1.md), install(1), [make(1)](../man1/make.1.md), [src.conf(5)](src.conf.5.md), [style.Makefile(5)](style.Makefile.5.md), [environ(7)](../man7/environ.7.md), [ports(7)](../man7/ports.7.md), sendmail(8)

## 历史

`make.conf` 文件在 FreeBSD 4.0 之前的某个时候出现。

## 作者

本手册页由 Mike W. Meyer <mwm@mired.org> 编写。

## 注意事项

注意，`MAKEOBJDIRPREFIX` 和 `MAKEOBJDIR` 是环境变量，不应在 `make.conf` 中或作为 [make(1)](../man1/make.1.md) 的命令行参数设置，而应在 make 的环境中设置。

## 缺陷

本手册页有时可能会与 `make.conf` 中当前可用的选项不同步。请查看 **/usr/share/examples/etc/make.conf** 文件以获取最新的可用选项。
