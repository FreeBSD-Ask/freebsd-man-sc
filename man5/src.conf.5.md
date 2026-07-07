# src.conf(5)

`src.conf` — 源码构建选项

## 名称

`src.conf`

## 描述

`src.conf` 文件包含控制 FreeBSD 源码树构建过程中将生成哪些组件的变量；参见 [build(7)](../man7/build.7.md)。

`src.conf` 文件使用标准的 makefile 语法。但是，`src.conf` 不应向 [make(1)](../man1/make.1.md) 指定任何依赖关系。相反，`src.conf` 用于设置控制系统构建方式的 [make(1)](../man1/make.1.md) 变量。

`src.conf` 的默认位置是源码树的顶层，如果源码树本身中没有找到 `src.conf`，则为 **/etc/src.conf**，但可以在 [make(1)](../man1/make.1.md) 变量 `SRCCONF` 中指定其他位置。如果系统级设置不适合特定构建，可能需要覆盖 `src.conf` 的位置。例如，将 `SRCCONF` 设置为 **/dev/null** 会将所有构建控制有效地重置为默认值。

`src.conf` 的唯一目的是控制 FreeBSD 源码的编译，源码通常位于 **/usr/src**。通常，当某些控制变量的值需要从默认值更改时，系统管理员会创建 `src.conf`。

此外，可以通过 [make(1)](../man1/make.1.md) 的 `-D` 选项或在其环境中为特定构建指定控制变量；参见 [environ(7)](../man7/environ.7.md)。

构建时 [make(1)](../man1/make.1.md) 的环境可以通过 `SRC_ENV_CONF` 变量控制，该变量默认为 **/etc/src-env.conf**。一些只能在此文件中设置的示例有 `WITH_DIRDEPS_BUILD`、`WITH_META_MODE` 和 `MAKEOBJDIRPREFIX`，因为它们是仅环境变量。

`WITH_` 和 `WITHOUT_` 变量的值无论设置如何都会被忽略；即使设置为 “`FALSE`” 或 “`NO`”。只要存在某个选项，[make(1)](../man1/make.1.md) 就会使其生效。

以下列表提供了可用于源码构建的变量的名称和简要说明。

- `WITH_LLVM_BINUTILS`

**`WITH_LOADER_EFI_SECUREBOOT`**（除非显式设置了 `WITHOUT_LOADER_EFI_SECUREBOOT`）
**`WITH_LOADER_VERIEXEC`**（除非显式设置了 `WITHOUT_LOADER_VERIEXEC`）
**`WITH_LOADER_VERIEXEC_VECTX`**（除非显式设置了 `WITHOUT_LOADER_VERIEXEC_VECTX`）
**`WITH_VERIEXEC`**（除非显式设置了 `WITHOUT_VERIEXEC`）

- `WITHOUT_BLOCKLIST`

**`WITHOUT_BLACKLIST_SUPPORT`**（除非显式设置了 `WITH_BLACKLIST_SUPPORT`）
**`WITHOUT_BLOCKLIST_SUPPORT`**（除非显式设置了 `WITH_BLOCKLIST_SUPPORT`）

- `WITHOUT_BLOCKLIST_SUPPORT`

- `WITHOUT_BLACKLIST`

**`WITHOUT_BLACKLIST_SUPPORT`**（除非显式设置了 `WITH_BLACKLIST_SUPPORT`）
**`WITHOUT_BLOCKLIST_SUPPORT`**（除非显式设置了 `WITH_BLOCKLIST_SUPPORT`）

- `WITHOUT_BLACKLIST_SUPPORT`

```sh
CCACHE_BASEDIR='${SRCTOP:H}' MAKEOBJDIRPREFIX='${SRCTOP:H}/obj'
```

- `WITHOUT_CTF`
- `WITHOUT_DTRACE`
- `WITHOUT_LOADER_ZFS`
- `WITHOUT_ZFS`
- `WITHOUT_ZFS_TESTS`

- `WITHOUT_CLANG_EXTRAS`
- `WITHOUT_CLANG_FORMAT`
- `WITHOUT_CLANG_FULL`
- `WITHOUT_LLVM_COV`

**`WITHOUT_LLVM_TARGET_AARCH64`**（除非显式设置了 `WITH_LLVM_TARGET_AARCH64`）
**`WITHOUT_LLVM_TARGET_ALL`**（除非显式设置了 `WITH_LLVM_TARGET_ALL`）
**`WITHOUT_LLVM_TARGET_ARM`**（除非显式设置了 `WITH_LLVM_TARGET_ARM`）
**`WITHOUT_LLVM_TARGET_POWERPC`**（除非显式设置了 `WITH_LLVM_TARGET_POWERPC`）
**`WITHOUT_LLVM_TARGET_RISCV`**（除非显式设置了 `WITH_LLVM_TARGET_RISCV`）

**`WITHOUT_DEPEND_CLEANUP`**（除非显式设置了 `WITH_DEPEND_CLEANUP`）

- `WITHOUT_CLANG_BOOTSTRAP`
- `WITHOUT_ELFTOOLCHAIN_BOOTSTRAP`
- `WITHOUT_LLD_BOOTSTRAP`
- `WITHOUT_LLVM_BINUTILS_BOOTSTRAP`

- `WITHOUT_DMAGENT`
- `WITHOUT_KERBEROS`
- `WITHOUT_LDNS`
- `WITHOUT_LDNS_UTILS`
- `WITHOUT_LOADER_ZFS`
- `WITHOUT_MITKRB5`
- `WITHOUT_OPENSSH`
- `WITHOUT_OPENSSL`
- `WITHOUT_OPENSSL_KTLS`
- `WITHOUT_PKGBOOTSTRAP`
- `WITHOUT_UNBOUND`
- `WITHOUT_ZFS`
- `WITHOUT_ZFS_TESTS`

**`WITHOUT_KERBEROS_SUPPORT`**（除非显式设置了 `WITH_KERBEROS_SUPPORT`）

```sh
make show-valid-targets
```

- `WITH_INSTALL_AS_USER`

**`WITH_META_ERROR_TARGET`**（除非显式设置了 `WITHOUT_META_ERROR_TARGET`）
**`WITH_META_MODE`**（除非显式设置了 `WITHOUT_META_MODE`）
**`WITH_STAGING`**（除非显式设置了 `WITHOUT_STAGING`）
**`WITH_STAGING_MAN`**（除非显式设置了 `WITHOUT_STAGING_MAN`）
**`WITH_STAGING_PROG`**（除非显式设置了 `WITHOUT_STAGING_PROG`）
**`WITH_SYSROOT`**（除非显式设置了 `WITHOUT_SYSROOT`）

- `WITHOUT_CTF`

- `WITHOUT_INET_SUPPORT`

- `WITHOUT_INET6_SUPPORT`

**`WITHOUT_KERBEROS_SUPPORT`**（除非显式设置了 `WITH_KERBEROS_SUPPORT`）

**`WITHOUT_KVM_SUPPORT`**（除非显式设置了 `WITH_KVM_SUPPORT`）

- `WITHOUT_LDNS_UTILS`
- `WITHOUT_UNBOUND`

**`WITHOUT_LLVM_TARGET_AARCH64`**（除非显式设置了 `WITH_LLVM_TARGET_AARCH64`）
**`WITHOUT_LLVM_TARGET_ARM`**（除非显式设置了 `WITH_LLVM_TARGET_ARM`）
**`WITHOUT_LLVM_TARGET_POWERPC`**（除非显式设置了 `WITH_LLVM_TARGET_POWERPC`）
**`WITHOUT_LLVM_TARGET_RISCV`**（除非显式设置了 `WITH_LLVM_TARGET_RISCV`）

**`WITH_LOADER_EFI_SECUREBOOT`**（除非显式设置了 `WITHOUT_LOADER_EFI_SECUREBOOT`）
**`WITH_LOADER_VERIEXEC_VECTX`**（除非显式设置了 `WITHOUT_LOADER_VERIEXEC_VECTX`）

- `WITHOUT_DMAGENT`
- `WITHOUT_MAILWRAPPER`
- `WITHOUT_SENDMAIL`

**`WITHOUT_MAN_UTILS`**（除非显式设置了 `WITH_MAN_UTILS`）

- 执行的命令发生变化。
- 当前工作目录发生变化。
- 目标的 meta 文件缺失。
- 当 filemon 已加载而上次运行未加载时，目标的 meta 文件缺少 filemon 数据。
- [需要 [filemon(4)](../man4/filemon.4.md)] 读取、执行或链接到的文件比目标新。
- [需要 [filemon(4)](../man4/filemon.4.md)] 读取、写入、执行或链接的文件缺失。

- `WITHOUT_BLUETOOTH`

**`WITHOUT_NETGRAPH_SUPPORT`**（除非显式设置了 `WITH_NETGRAPH_SUPPORT`）

- `WITHOUT_NLS_CATALOGS`

- `WITHOUT_OFED_EXTRA`

- `WITHOUT_DMAGENT`
- `WITHOUT_KERBEROS`
- `WITHOUT_LDNS`
- `WITHOUT_LDNS_UTILS`
- `WITHOUT_LOADER_ZFS`
- `WITHOUT_MITKRB5`
- `WITHOUT_OPENSSH`
- `WITHOUT_OPENSSL_KTLS`
- `WITHOUT_PKGBOOTSTRAP`
- `WITHOUT_UNBOUND`
- `WITHOUT_ZFS`
- `WITHOUT_ZFS_TESTS`

**`WITHOUT_KERBEROS_SUPPORT`**（除非显式设置了 `WITH_KERBEROS_SUPPORT`）

**`WITHOUT_PAM_SUPPORT`**（除非显式设置了 `WITH_PAM_SUPPORT`）

- `WITHOUT_AUTHPF`

- `WITHOUT_SOURCELESS_HOST`
- `WITHOUT_SOURCELESS_UCODE`

- `WITHOUT_KERNEL_SYMBOLS`

**`WITH_STAGING_MAN`**（除非显式设置了 `WITHOUT_STAGING_MAN`）
**`WITH_STAGING_PROG`**（除非显式设置了 `WITHOUT_STAGING_PROG`）

- `WITHOUT_DTRACE_TESTS`
- `WITHOUT_ZFS_TESTS`

**`WITHOUT_GOOGLETEST`**（除非显式设置了 `WITH_GOOGLETEST`）
**`WITHOUT_TESTS_SUPPORT`**（除非显式设置了 `WITH_TESTS_SUPPORT`）

- `WITHOUT_GOOGLETEST`

- `WITHOUT_CLANG`
- `WITHOUT_CLANG_EXTRAS`
- `WITHOUT_CLANG_FORMAT`
- `WITHOUT_CLANG_FULL`
- `WITHOUT_LLD`
- `WITHOUT_LLDB`
- `WITHOUT_LLVM_COV`

**`WITHOUT_LLVM_BINUTILS`**（除非显式设置了 `WITH_LLVM_BINUTILS`）

- `WITHOUT_USB_GADGET_EXAMPLES`

**`WITHOUT_WIRELESS_SUPPORT`**（除非显式设置了 `WITH_WIRELESS_SUPPORT`）

- `WITHOUT_ZFS_TESTS`

- `WITHOUT_ZONEINFO_LEAPSECONDS_SUPPORT`

**`WITHOUT_ACCT`** 不构建进程记账工具，如 accton(8) 和 sa(8)。

**`WITHOUT_ACPI`** 不构建 acpiconf(8)、acpidump(8) 及相关程序。

**`WITHOUT_APM`** 不构建 apm(8)、apmd(8) 及相关程序。

**`WITH_ASAN`** 使用地址消毒器（ASan）构建基本系统，以检测内存损坏错误，如缓冲区溢出或释放后使用。需要将 Clang 用作基本系统编译器，并且运行时支持库可用。设置后，它会强制以下选项：

**`WITHOUT_ASSERT_DEBUG`** 编译程序和库时不带 [assert(3)](../man3/assert.3.md) 检查。

**`WITHOUT_AT`** 不构建 [at(1)](../man1/at.1.md) 及相关工具。

**`WITHOUT_AUDIT`** 不在系统程序中构建审计支持。

**`WITHOUT_AUTHPF`** 不构建 [authpf(8)](../man8/authpf.8.md)。

**`WITHOUT_AUTOFS`** 不构建与 [autofs(4)](../man4/autofs.4.md) 相关的程序、库和内核模块。

**`WITHOUT_AUTO_OBJ`** 禁用自动创建 objdirs。如果所需的 OBJDIR 可被当前用户写入，则默认启用。必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITH_BEARSSL`** 构建 BearSSL 库。BearSSL 是一个适合嵌入式环境的小型 SSL 库。详情见 https://www.BearSSL.org/ 此库目前仅用于为 Verified Exec 和 [loader(8)](../man8/loader.8.md) 执行签名验证和相关操作。由于 x86 上 BIOS 环境的大小限制，可能需要将 `LOADERSIZE` 设置为大于默认值 500000，尽管 loader 通常即使使用此选项也在 500k 限制以内。将 `LOADERSIZE` 设置为大于 500000 可能导致 pxeboot(8) 过大而无法工作。在目标环境中使用较大限制构建的 loader 进行仔细测试以确定安全限制至关重要，因为不同的 BIOS 环境保留了不同数量的低 640k 空间，使得为所有人确定一个精确限制是不可能的。有关其他注意事项，另请参见 `WITH_LOADER_PXEBOOT`。设置后，以下选项也生效：

**`WITHOUT_BHYVE`** 不构建或安装 [bhyve(8)](../man8/bhyve.8.md)、相关工具和示例。此选项仅影响 amd64/amd64 和 arm64/aarch64。

**`WITH_BHYVE_SNAPSHOT`** 在 [bhyve(8)](../man8/bhyve.8.md) 和 [bhyvectl(8)](../man8/bhyvectl.8.md) 中包含保存和恢复（快照）支持。此选项仅影响 amd64/amd64。

**`WITH_BIND_NOW`** 构建所有二进制文件时设置 `DF_BIND_NOW` 标志，指示运行时加载器在进程启动时执行所有重定位处理，而不是按需处理。`BIND_NOW` 和 `RELRO` 选项的组合提供“完整”的重定位只读（RELRO）支持。使用完整 RELRO 时，整个 GOT 在启动时执行重定位后被设为只读，避免 GOT 覆盖攻击。

**`WITHOUT_BLACKLIST`** 此选项已重命名为 `WITHOUT_BLOCKLIST`。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITHOUT_BLACKLIST_SUPPORT`** 此选项已重命名为 `WITHOUT_BLOCKLIST_SUPPORT`。设置后，它会强制以下选项：

**`WITHOUT_BLOCKLIST`** 如果不想构建 blocklistd(8) 和 blocklistctl(8)，请设置此选项。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITHOUT_BLOCKLIST_SUPPORT`** 构建某些程序时不带 libblocklist(3) 支持，如 fingerd(8) 和 sshd(8)。设置后，它会强制以下选项：

**`WITHOUT_BLUETOOTH`** 不构建蓝牙相关的内核模块、程序和库。

**`WITHOUT_BOOT`** 不构建引导块和 loader。

**`WITHOUT_BOOTPARAMD`** 不构建或安装 bootparamd(8)。

**`WITHOUT_BOOTPD`** 不构建或安装 bootpd(8)。

**`WITH_BRANCH_PROTECTION`** 构建时启用分支保护。在 arm64 上启用指针认证和分支目标标识指令的使用。这些可用于帮助缓解某些利用技术。

**`WITHOUT_BSDINSTALL`** 不构建 bsdinstall(8)、sade(8) 及相关程序。

**`WITHOUT_BSNMP`** 不构建或安装 bsnmpd(1) 及相关库和数据文件。

**`WITHOUT_CALENDAR`** 不构建 calendar(1)。

**`WITHOUT_CAROOT`** 不将 Mozilla NSS 包中的受信任证书添加到 base 中。

**`WITHOUT_CASPER`** 此选项无效。

**`WITH_CCACHE_BUILD`** 在构建时使用 ccache(1)。无需配置，只需安装 **devel/ccache**、**devel/ccache4** 或 **devel/sccache** port 或软件包；在后一种情况下，设置 **CCACHE_NAME=sccache**。与 distcc(1) 一起使用时，设置 **CCACHE_PREFIX=${LOCALBASE}/bin/distcc**。默认缓存目录为 `$HOME/.ccache`，可通过设置 **CCACHE_DIR** 更改。使用树内引导编译器时，**CCACHE_COMPILERCHECK** 选项默认为 **content**，使用外部编译器时为 **mtime**。**CCACHE_CPP2** 选项用于 Clang 但不用于 GCC。在多个工作目录之间共享缓存需要使用类似 **/some/prefix/src** **/some/prefix/obj** 的布局和如下环境：有关更多配置选项，参见 ccache(1)。

**`WITHOUT_CCD`** 不构建 geom_ccd(4) 及相关工具。

**`WITHOUT_CDDL`** 不构建在 Sun CDDL 许可下授权的代码。设置后，它会强制以下选项：

**`WITHOUT_CLANG`** 不在构建的常规阶段构建 Clang C/C++ 编译器。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITHOUT_CLANG_BOOTSTRAP`** 不在构建的引导阶段构建 Clang C/C++ 编译器。要能够构建系统，必须启用 gcc 或 clang 引导，除非通过 XCC 提供备用编译器。

**`WITH_CLANG_EXTRAS`** 构建额外的 clang 和 llvm 工具，如 bugpoint 和 clang-format。

**`WITH_CLANG_FORMAT`** 构建 clang-format。

**`WITHOUT_CLANG_FULL`** 避免构建 Clang C/C++ 编译器的 ARCMigrate、Rewriter 和 StaticAnalyzer 组件。

**`WITH_CLEAN`** 在构建 world 和/或内核之前进行清理。注意，在源码树根目录的 `.clean_build_epoch` 中记录新纪元也会强制进行 clean world 构建。设置后，以下选项也生效：

**`WITHOUT_CPP`** 不构建 [cpp(1)](../man1/clang.1.md)。

**`WITHOUT_CROSS_COMPILER`** 不在 buildworld 的交叉工具阶段构建任何交叉编译器。当编译与系统上安装的 FreeBSD 版本不同的 FreeBSD 时，通过 XCC 提供备用编译器以确保成功。当使用与主机相同版本的 FreeBSD 进行编译时，可以安全使用此选项。当主机 FreeBSD 版本与正在构建的源码接近时，此选项也可能是安全的，但如果版本之间工具链有任何变化，则无法保证。设置后，它会强制以下选项：

**`WITHOUT_CRYPT`** 不构建任何加密代码。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITH_CTF`** 使用 CTF（紧凑 C 类型格式）数据编译。CTF 数据封装了类似于 DWARF 和古老的 stabs 的调试信息的精简形式，是 DTrace 所需的。

**`WITHOUT_CUSE`** 不构建 CUSE 相关的程序和库。

**`WITHOUT_CXGBETOOL`** 不构建 cxgbetool(8) 这是 arm/armv7 和 riscv/riscv64 上的默认设置。

**`WITH_CXGBETOOL`** 构建 cxgbetool(8) 这是 amd64/amd64、arm64/aarch64、i386/i386、powerpc/powerpc64 和 powerpc/powerpc64le 上的默认设置。

**`WITHOUT_DEBUG_FILES`** 避免为每个可执行二进制文件和共享库构建或安装独立的调试文件。

**`WITHOUT_DEPEND_CLEANUP`** 不尝试在构建之前检测对象树是否需要部分或全部清理。这加快了增量构建，特别是在试验构建选项时，但可能导致构建莫名其妙地失败或产生无法正常工作的二进制文件。

**`WITH_DETECT_TZ_CHANGES`** 使时间处理代码检测时区文件的更改。

**`WITH_DIALOG`** 构建 [dialog(1)](../man1/dialog.1.md)、dialog(3)、dpv(1) 和 dpv(3)。

**`WITHOUT_DICT`** 不构建 Webster 词典文件。

**`WITH_DIRDEPS_BUILD`** 这是一个替代构建系统。详情见 https://www.crufty.net/sjg/docs/freebsd-meta-mode.htm。可以从顶层查看构建命令：构建由 dirdeps.mk 使用每个目录中 Makefile.depend 文件中存储的 `DIRDEPS` 驱动。构建可以从任何地方启动，并且行为相同。[make(1)](../man1/make.1.md) 的初始实例从 `Makefile.depend` 递归读取 `DIRDEPS`，从当前起点计算树依赖图。设置 `NO_DIRDEPS` 会跳过检查 dirdep 依赖，仅在当前和子目录中构建。`NO_DIRDEPS_BELOW` 跳过构建任何 dirdeps，仅构建当前目录。这还利用 `WITH_META_MODE` 逻辑进行增量构建。除非定义了 `NO_SILENT`，否则构建会隐藏执行的命令。注意，目前没有用于此功能的大规模安装功能。此构建专为生成软件包而设计，然后可以在目标系统上安装。FreeBSD 中的实现不完整。完成需要为每个内核和软件包构建叶目录，以便跟踪其依赖项。设置后，它会强制以下选项：设置后，以下选项也生效：必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITH_DIRDEPS_CACHE`** 缓存 dirdeps.mk 的结果，可以为后续构建节省大量时间。依赖于 `WITH_DIRDEPS_BUILD`。必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITH_DISK_IMAGE_TOOLS_BOOTSTRAP`** 将 etdump(1)、makefs(8) 和 mkimg(1) 作为引导工具构建。

**`WITHOUT_DMAGENT`** 不构建 dma 邮件传输代理。

**`WITHOUT_DOCCOMPRESS`** 不安装压缩的系统文档。仅安装未压缩的版本。

**`WITHOUT_DTRACE`** 不构建 DTrace 框架内核模块、库和用户命令。设置后，它会强制以下选项：

**`WITH_DTRACE_ASAN`** 使用地址和未定义行为消毒器编译用户空间 DTrace 代码（libdtrace、dtrace(1)、lockstat(1)、plockstat(1)）。需要将 Clang 用作基本系统编译器，并且运行时支持库可用。

**`WITH_DTRACE_TESTS`** 在 **/usr/tests/cddl/usr.sbin/dtrace** 中构建并安装 DTrace 测试套件。此测试套件在 amd64/amd64 以外的架构上被视为实验性的，运行它可能导致系统不稳定。

**`WITHOUT_DYNAMICROOT`** 如果不想动态链接 **/bin** 和 **/sbin**，请设置此选项。

**`WITHOUT_EE`** 不构建和安装 [edit(1)](../man1/ee.1.md)、[ee(1)](../man1/ee.1.md) 及相关程序。

**`WITHOUT_EFI`** 不构建 efivar(3) 和 efivar(8)。这是 i386/i386、powerpc/powerpc64 和 powerpc/powerpc64le 上的默认设置。

**`WITH_EFI`** 构建 efivar(3) 和 efivar(8)。这是 amd64/amd64、arm/armv7、arm64/aarch64 和 riscv/riscv64 上的默认设置。

**`WITHOUT_ELFTOOLCHAIN_BOOTSTRAP`** 不将 ELF 工具链工具（addr2line、nm、size、strings 和 strip）作为引导过程的一部分构建。必须提供备用引导工具链。

**`WITHOUT_EXAMPLES`** 避免将示例安装到 **/usr/share/examples/**。

**`WITHOUT_FDT`** 不将扁平设备树支持作为基本系统的一部分构建。这包括设备树编译器（dtc）和 libfdt 支持库。这是 amd64/amd64 和 i386/i386 上的默认设置。

**`WITH_FDT`** 将扁平设备树支持作为基本系统的一部分构建。这包括设备树编译器（dtc）和 libfdt 支持库。这是 arm/armv7、arm64/aarch64、powerpc/powerpc64、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITHOUT_FILE`** 不构建 file(1) 及相关程序。

**`WITHOUT_FINGER`** 不构建或安装 finger(1) 和 fingerd(8)。

**`WITHOUT_FLOPPY`** 不构建或安装用于操作软盘驱动器的程序。

**`WITHOUT_FORMAT_EXTENSIONS`** 编译内核时不启用 `-fformat-extensions`。同时禁用所有格式检查。

**`WITHOUT_FORTH`** 构建引导加载器时不带 Forth 支持。

**`WITHOUT_FREEBSD_UPDATE`** 不构建 [freebsd-update(8)](../man8/freebsd-update.8.md)。

**`WITHOUT_FTP`** 不构建或安装 [ftp(1)](../man1/ftp.1.md)。

**`WITHOUT_GAMES`** 不构建游戏。

**`WITHOUT_GOOGLETEST`** 既不构建也不安装 libgmock、libgtest 及相关测试。

**`WITHOUT_GPIO`** 不将 [gpioctl(8)](../man8/gpioctl.8.md) 作为基本系统的一部分构建。

**`WITHOUT_HAST`** 不构建 hastd(8) 及相关工具。

**`WITH_HESIOD`** 构建 Hesiod 支持。

**`WITHOUT_HTML`** 不构建 HTML 文档。

**`WITHOUT_HYPERV`** 不构建或安装 HyperV 工具。这是 arm/armv7、powerpc/powerpc64、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITH_HYPERV`** 构建或安装 HyperV 工具。这是 amd64/amd64、arm64/aarch64 和 i386/i386 上的默认设置。

**`WITHOUT_ICONV`** 不将 iconv 作为 libc 的一部分构建。

**`WITHOUT_INCLUDES`** 不安装头文件。此选项过去拼写为 `NO_INCS`。该选项对构建目标无效。

**`WITHOUT_INET`** 不构建与 IPv4 网络相关的程序和库。设置后，它会强制以下选项：

**`WITHOUT_INET6`** 不构建与 IPv6 网络相关的程序和库。设置后，它会强制以下选项：

**`WITHOUT_INET6_SUPPORT`** 构建不带 IPv6 支持的库、程序和内核模块。

**`WITHOUT_INETD`** 不构建 [inetd(8)](../man8/inetd.8.md)。

**`WITHOUT_INET_SUPPORT`** 构建不带 IPv4 支持的库、程序和内核模块。

**`WITHOUT_INSTALLLIB`** 设置此选项以不安装可选库。例如，在创建 [nanobsd(8)](../man8/nanobsd.8.md) 镜像时。该选项对构建目标无效。

**`WITH_INSTALL_AS_USER`** 通过将文件的所有者和组属性设置为运行 [make(1)](../man1/make.1.md) 命令的用户，使安装目标对非 root 用户成功。用户仍必须将 `DESTDIR` 变量设置为指向用户有写入权限的目录。

**`WITHOUT_IPFILTER`** 不构建 IP Filter 软件包。

**`WITH_IPFILTER_IPFS`** 启用构建 ipfs(8) 工具以保存和恢复 IPFilter 状态表。

**`WITHOUT_IPFW`** 不构建 IPFW 工具。

**`WITHOUT_IPSEC_SUPPORT`** 不构建带 [ipsec(4)](../man4/ipsec.4.md) 支持的内核。此选项是 [ipsec(4)](../man4/ipsec.4.md) 和 tcpmd5(4) 所需的。

**`WITHOUT_ISCSI`** 不构建 iscsid(8) 及相关工具。

**`WITHOUT_JAIL`** 不构建用于支持 jail 的工具；例如 [jail(8)](../man8/jail.8.md)。

**`WITHOUT_JEMALLOC_LG_VADDR_WIDE`** 不允许程序在 amd64 上使用超过 48 位地址位。与 LA57 模式不兼容。启用此选项可能会略微减少 jemalloc 元数据的内存消耗，但也需要禁用 LA57（如果硬件支持）。

**`WITHOUT_KDUMP`** 不构建 [kdump(1)](../man1/kdump.1.md) 和 [truss(1)](../man1/truss.1.md)。

**`WITHOUT_KERBEROS`** 设置此选项以不构建 Kerberos。设置后，以下选项也生效：

**`WITHOUT_KERBEROS_SUPPORT`** 构建某些程序时不带 Kerberos 支持，如 [ssh(1)](../man1/ssh.1.md)、[telnet(1)](../man1/telnet.1.md) 和 sshd(8)。

**`WITH_KERNEL_BIN`** 作为内核正常构建和安装过程的一部分，从 kernel 生成并安装 kernel.bin。仅在 arm 和 arm64 上可用。通常这将通过以下方式添加到内核配置文件中：makeoptions	WITH_KERNEL_BIN=1 但也可以在命令行上使用。

**`WITH_KERNEL_RETPOLINE`** 在内核构建中启用针对 CVE-2017-5715 的 “retpoline” 缓解措施。

**`WITHOUT_KERNEL_SYMBOLS`** 不安装独立的内核调试符号文件。此选项在构建时无效。

**`WITHOUT_KVM`** 不将 `libkvm` 库作为基本系统的一部分构建。该选项目前无效。设置后，以下选项也生效：

**`WITHOUT_KVM_SUPPORT`** 构建某些程序时不带可选的 `libkvm` 支持。

**`WITHOUT_LDNS`** 设置此变量将阻止构建 LDNS 库。设置后，它会强制以下选项：

**`WITHOUT_LDNS_UTILS`** 设置此变量将阻止构建 LDNS 工具 drill(1) 和 [host(1)](../man1/host.1.md)。

**`WITHOUT_LEGACY_CONSOLE`** 不构建支持旧式 PC 控制台的程序；例如 kbdcontrol(1) 和 vidcontrol(1)。

**`WITHOUT_LIB32`** 在 64 位平台上，不构建 32 位库集和 `ld-elf32.so.1` 运行时链接器。这是 arm/armv7、i386/i386、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITH_LIB32`** 在 64 位平台上，构建 32 位库集和 `ld-elf32.so.1` 运行时链接器。这是 amd64/amd64、arm64/aarch64 和 powerpc/powerpc64 上的默认设置。

**`WITHOUT_LLD`** 不构建 LLVM 的 lld 链接器。

**`WITHOUT_LLDB`** 不构建 LLDB 调试器。这是 riscv/riscv64 上的默认设置。

**`WITH_LLDB`** 构建 LLDB 调试器。这是 amd64/amd64、arm/armv7、arm64/aarch64、i386/i386、powerpc/powerpc64 和 powerpc/powerpc64le 上的默认设置。

**`WITHOUT_LLD_BOOTSTRAP`** 不在构建的引导阶段构建 LLD 链接器。要能够构建系统，必须通过 XLD 提供备用链接器。

**`WITHOUT_LLVM_ASSERTIONS`** 禁用 LLVM 中的调试断言。

**`WITHOUT_LLVM_BINUTILS`** 安装 ELF 工具链的二进制工具而不是 LLVM 的。这包括 [addr2line(1)](../man1/llvm-addr2line.1.md)、[ar(1)](../man1/ar.1.md)、nm(1)、objcopy(1)、[ranlib(1)](../man1/ar.1.md)、[readelf(1)](../man1/readelf.1.md)、size(1) 和 strip(1)。无论此设置如何，c++filt(1) 和 objdump(1) 都使用 LLVM 工具。strings(1) 始终由 ELF 工具链提供。

**`WITHOUT_LLVM_BINUTILS_BOOTSTRAP`** 不在构建的引导阶段构建 LLVM 二进制工具。要能够构建系统，必须通过 `XAR`、`XNM`、`XOBJCOPY`、`XSIZE`、`XSTRINGS` 和 `XSTRIPBIN` 提供备用二进制工具。

**`WITHOUT_LLVM_COV`** 不构建 llvm-cov(1) 工具。

**`WITH_LLVM_FULL_DEBUGINFO`** 为 LLVM 库和工具生成完整的调试信息，这会使用更多的磁盘空间和构建资源，但允许更容易的调试。

**`WITH_LLVM_LINK_STATIC_LIBRARIES`** 将 LLVM 库（libllvm、libclang、liblldb）静态链接到使用它们的每个二进制文件中。这意味着链接到这些库的二进制文件（如 clang、ld.lld 和 lldb）将更大且位置相关，但启动更快。

**`WITHOUT_LLVM_TARGET_AARCH64`** 不构建 AArch64 的 LLVM 目标支持。在大多数情况下，应使用 `LLVM_TARGET_ALL` 选项而不是此选项。

**`WITHOUT_LLVM_TARGET_ALL`** 仅构建所需的 LLVM 目标支持。此选项优先于特定目标支持选项。设置后，以下选项也生效：

**`WITHOUT_LLVM_TARGET_ARM`** 不构建 ARM 的 LLVM 目标支持。在大多数情况下，应使用 `LLVM_TARGET_ALL` 选项而不是此选项。

**`WITH_LLVM_TARGET_BPF`** 构建 BPF 的 LLVM 目标支持。在大多数情况下，应使用 `LLVM_TARGET_ALL` 选项而不是此选项。

**`WITH_LLVM_TARGET_MIPS`** 构建 MIPS 的 LLVM 目标支持。在大多数情况下，应使用 `LLVM_TARGET_ALL` 选项而不是此选项。

**`WITHOUT_LLVM_TARGET_POWERPC`** 不构建 PowerPC 的 LLVM 目标支持。在大多数情况下，应使用 `LLVM_TARGET_ALL` 选项而不是此选项。

**`WITHOUT_LLVM_TARGET_RISCV`** 不构建 RISC-V 的 LLVM 目标支持。在大多数情况下，应使用 `LLVM_TARGET_ALL` 选项而不是此选项。

**`WITHOUT_LLVM_TARGET_X86`** 不构建 X86 的 LLVM 目标支持。在大多数情况下，应使用 `LLVM_TARGET_ALL` 选项而不是此选项。

**`WITHOUT_LOADER_BIOS_TEXTONLY`** 在 i386 和 amd64 BIOS 引导加载器中包含图形、字体和视频模式支持。

**`WITH_LOADER_EFI_SECUREBOOT`** 启用构建带验证支持的 [loader(8)](../man8/loader.8.md)，该验证基于从 UEFI 获取的证书。

**`WITHOUT_LOADER_GELI`** 禁用在引导链二进制文件中包含 GELI 加密支持。这是 powerpc/powerpc64 和 powerpc/powerpc64le 上的默认设置。

**`WITH_LOADER_GELI`** 构建 GELI 引导加载器支持。这是 amd64/amd64、arm/armv7、arm64/aarch64、i386/i386 和 riscv/riscv64 上的默认设置。

**`WITHOUT_LOADER_IA32`** 不构建 32 位 UEFI loader。这是 arm/armv7、arm64/aarch64、i386/i386、powerpc/powerpc64、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITH_LOADER_IA32`** 构建 32 位 UEFI loader。这是 amd64/amd64 上的默认设置。

**`WITHOUT_LOADER_KBOOT`** 不构建 kboot（一个 linuxboot 环境加载器）。这是 arm/armv7、i386/i386、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITH_LOADER_KBOOT`** 构建 kboot（一个 linuxboot 环境加载器）。这是 amd64/amd64、arm64/aarch64 和 powerpc/powerpc64 上的默认设置。

**`WITHOUT_LOADER_LUA`** 不为引导加载器构建 LUA 绑定。这是 powerpc/powerpc64 和 powerpc/powerpc64le 上的默认设置。

**`WITH_LOADER_LUA`** 为引导加载器构建 LUA 绑定。这是 amd64/amd64、arm/armv7、arm64/aarch64、i386/i386 和 riscv/riscv64 上的默认设置。

**`WITHOUT_LOADER_OFW`** 禁用构建 openfirmware 引导加载器组件。这是 amd64/amd64、arm/armv7、arm64/aarch64、i386/i386 和 riscv/riscv64 上的默认设置。

**`WITH_LOADER_OFW`** 构建 openfirmware 引导加载器组件。这是 powerpc/powerpc64 和 powerpc/powerpc64le 上的默认设置。

**`WITHOUT_LOADER_PXEBOOT`** 不在 i386/amd64 上构建 pxeboot。当 pxeboot 过大或不需要时，可以使用此选项禁用它。关于如何在你需要更大的 **/boot/loader** 和 **/boot/pxeboot** 时调整默认值，参见 `WITH_LOADER_PXEBOOT`。此选项仅对 x86 有效。

**`WITHOUT_LOADER_UBOOT`** 禁用构建 ubldr。这是 amd64/amd64、arm64/aarch64、i386/i386、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITH_LOADER_UBOOT`** 构建 ubldr。这是 arm/armv7 和 powerpc/powerpc64 上的默认设置。

**`WITH_LOADER_USB`** 构建 usb/kshim 库。

**`WITH_LOADER_VERBOSE`** 构建时在 loader 中加入额外的详细调试。可能使已经接近过大限制的 loader 超出限制。谨慎使用。

**`WITH_LOADER_VERIEXEC`** 启用构建带验证支持的 [loader(8)](../man8/loader.8.md)，类似于 Verified Exec。依赖于 `WITH_BEARSSL`。可能需要更大的 `LOADERSIZE`。设置后，以下选项也生效：

**`WITH_LOADER_VERIEXEC_PASS_MANIFEST`** 启用构建 [loader(8)](../man8/loader.8.md)，支持将已验证的清单传递给内核。内核必须使用一个模块来解析清单。依赖于 `WITH_LOADER_VERIEXEC`。

**`WITH_LOADER_VERIEXEC_VECTX`** 启用构建 [loader(8)](../man8/loader.8.md)，作为加载的副作用支持对内核和模块进行哈希和验证。依赖于 `WITH_LOADER_VERIEXEC`。

**`WITHOUT_LOADER_ZFS`** 不构建 ZFS 文件系统引导加载器支持。

**`WITHOUT_LOCALES`** 不构建本地化文件；参见 locale(1)。

**`WITHOUT_LOCATE`** 不构建 [locate(1)](../man1/locate.1.md) 及相关程序。

**`WITHOUT_LPR`** 不构建 lpr(1) 及相关程序。

**`WITHOUT_LS_COLORS`** 构建 [ls(1)](../man1/ls.1.md) 时不带用于区分文件类型的颜色支持。

**`WITHOUT_MACHDEP_OPTIMIZATIONS`** 在 libc 和 libm 中优先使用机器无关的非汇编代码。

**`WITHOUT_MAIL`** 不构建任何邮件支持（MUA 或 MTA）。设置后，它会强制以下选项：

**`WITHOUT_MAILWRAPPER`** 不构建 mailwrapper(8) MTA 选择器。

**`WITHOUT_MAKE`** 不安装 [make(1)](../man1/make.1.md) 及相关支持文件。

**`WITHOUT_MAKE_CHECK_USE_SANDBOX`** 不在有限的沙盒模式中执行 “`make check`”。如果以非特权用户身份执行，此选项应与 `WITH_INSTALL_AS_USER` 配对使用。更多细节参见 [tests(7)](../man7/tests.7.md)。

**`WITH_MALLOC_PRODUCTION`** 禁用 malloc(3) 中的断言和统计收集。运行时选项 `opt.abort`、`opt.abort_conf` 和 `opt.junk` 也默认为 false。

**`WITHOUT_MAN`** 不构建手册页。设置后，以下选项也生效：

**`WITHOUT_MANCOMPRESS`** 不安装压缩的手册页。仅安装未压缩的版本。

**`WITH_MANSPLITPKG`** 在 make package 期间将手册页拆分为单独的软件包。

**`WITHOUT_MAN_UTILS`** 不构建手册页工具，[apropos(1)](../man1/apropos.1.md)、makewhatis(1)、[man(1)](../man1/man.1.md)、[whatis(1)](../man1/apropos.1.md)、manctl(8) 及相关支持文件。

**`WITH_META_ERROR_TARGET`** 启用 META_MODE .ERROR 目标。此目标将失败目标的 meta 文件复制到 `ERROR_LOGDIR`（默认为 `${SRCTOP:H}/error`）以帮助进行故障分析。依赖于 `WITH_META_MODE`。设置 `WITH_DIRDEPS_BUILD` 时这是默认值。必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITH_META_MODE`** 在构建时创建 [make(1)](../man1/make.1.md) meta 文件，这可以在使用 [filemon(4)](../man4/filemon.4.md) 时提供可靠的增量构建。meta 文件在 OBJDIR 中创建为 `target.meta`。这些 meta 文件跟踪执行的命令、其输出和当前目录。除非定义了 `NO_FILEMON`，否则需要 [filemon(4)](../man4/filemon.4.md) 模块。当模块加载时，执行的命令使用的任何文件都作为依赖项跟踪到其 meta 文件中的目标。与上次构建相比，如果以下任何条件为真，则目标被视为过时并重新构建：meta 文件也可用于调试。除非定义了 `NO_SILENT`，否则构建会隐藏执行的命令。错误会导致 [make(1)](../man1/make.1.md) 显示其部分环境以进行进一步调试。在其他方面，构建按正常方式运行。此选项最初调用不同的构建系统，但该系统已被重命名为 `WITH_DIRDEPS_BUILD`。必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITHOUT_MITKRB5`** 设置此选项以构建 KTH Heimdal 而不是 MIT Kerberos 5。

**`WITHOUT_MLX5TOOL`** 不构建 mlx5tool(8) 这是 arm/armv7 和 riscv/riscv64 上的默认设置。

**`WITH_MLX5TOOL`** 构建 mlx5tool(8) 这是 amd64/amd64、arm64/aarch64、i386/i386、powerpc/powerpc64 和 powerpc/powerpc64le 上的默认设置。

**`WITHOUT_NETCAT`** 不构建 [nc(1)](../man1/nc.1.md) 工具。

**`WITHOUT_NETGRAPH`** 不构建支持 [netgraph(4)](../man4/netgraph.4.md) 的应用程序。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITHOUT_NETGRAPH_SUPPORT`** 构建不带 netgraph 支持的库、程序和内核模块。

**`WITHOUT_NETLINK`** 不构建 genl(1) 工具。

**`WITHOUT_NETLINK_SUPPORT`** 使库和程序使用 rtsock 和 sysctl(3) 接口而不是 [snl(3)](../man3/snl.3.md)。

**`WITHOUT_NIS`** 不构建 NIS(8) 支持和相关程序。如果设置，你可能需要调整你的 [nsswitch.conf(5)](nsswitch.conf.5.md) 并移除 “nis” 条目。

**`WITHOUT_NLS`** 不构建 NLS 目录。设置后，它会强制以下选项：

**`WITHOUT_NLS_CATALOGS`** 不为 [csh(1)](../man1/csh.1.md) 构建 NLS 目录支持。

**`WITHOUT_NS_CACHING`** 禁用 `nsswitch` 子系统中的名称缓存。如果设置了此选项，也不会构建通用缓存守护进程 nscd(8)。

**`WITHOUT_NTP`** 不构建 ntpd(8) 及相关程序。

**`WITHOUT_NUAGEINIT`** 不安装有限的云初始化支持脚本。

**`WITHOUT_OFED`** 不构建 “OpenFabrics Enterprise Distribution” InfiniBand 软件栈，包括内核模块和用户空间库。这是 arm/armv7 上的默认设置。设置后，它会强制以下选项：

**`WITH_OFED`** 构建 “OpenFabrics Enterprise Distribution” InfiniBand 软件栈，包括内核模块和用户空间库。这是 amd64/amd64、arm64/aarch64、i386/i386、powerpc/powerpc64、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITH_OFED_EXTRA`** 构建 “OpenFabrics Enterprise Distribution” InfiniBand 软件栈的非必要组件，主要是示例。

**`WITH_OPENLDAP`** 使用 ports 中的 openldap 客户端启用 kerberos 的 LDAP 支持。

**`WITHOUT_OPENMP`** 不构建 LLVM 的 OpenMP 运行时。这是 arm/armv7 上的默认设置。

**`WITH_OPENMP`** 构建 LLVM 的 OpenMP 运行时。这是 amd64/amd64、arm64/aarch64、i386/i386、powerpc/powerpc64、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITHOUT_OPENSSH`** 不构建 OpenSSH。

**`WITHOUT_OPENSSL`** 不构建 OpenSSL。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITHOUT_OPENSSL_KTLS`** 不在 OpenSSL 中包含内核 TLS 支持。这是 arm/armv7 和 i386/i386 上的默认设置。

**`WITH_OPENSSL_KTLS`** 在 OpenSSL 中包含内核 TLS 支持。这是 amd64/amd64、arm64/aarch64、powerpc/powerpc64、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITHOUT_PAM`** 不构建 PAM 库和模块。此选项已弃用且无效。设置后，以下选项也生效：

**`WITHOUT_PAM_SUPPORT`** 构建 ppp(8) 时不带 PAM 支持。

**`WITHOUT_PF`** 不构建 PF 防火墙软件包。设置后，它会强制以下选项：

**`WITHOUT_PIE`** 不将动态链接的二进制文件构建为位置无关可执行文件（PIE）。这是 arm/armv7 和 i386/i386 上的默认设置。

**`WITH_PIE`** 将动态链接的二进制文件构建为位置无关可执行文件（PIE）。这是 amd64/amd64、arm64/aarch64、powerpc/powerpc64、powerpc/powerpc64le 和 riscv/riscv64 上的默认设置。

**`WITHOUT_PKGBOOTSTRAP`** 不构建 pkg(7) 引导工具。

**`WITHOUT_PKGCONF`** 不构建 pkgconf 二进制文件和 libpkgconf 库。

**`WITHOUT_PKGSERVE`** 不构建或安装 pkg-serve(8)。

**`WITHOUT_PMC`** 不构建 [pmccontrol(8)](../man8/pmccontrol.8.md) 及相关程序。

**`WITHOUT_PPP`** 不构建 ppp(8) 及相关程序。

**`WITHOUT_PTHREADS_ASSERTIONS`** 禁用 pthreads 库中的调试断言。

**`WITHOUT_QUOTAS`** 不构建 quota(1) 及相关程序。

**`WITHOUT_RADIUS_SUPPORT`** 不在各个应用程序中构建 radius 支持，如 pam_radius(8) 和 ppp(8)。

**`WITH_RATELIMIT`** 构建带速率限制支持的系统。这使得 `SO_MAX_PACING_RATE` 在 getsockopt(2) 中生效，以及通过代理使 [ifconfig(8)](../man8/ifconfig.8.md) 中的 `txrlimit` 支持生效。

**`WITHOUT_RBOOTD`** 不构建或安装 rbootd(8)。

**`WITHOUT_RELRO`** 不应用重定位只读（RELRO）漏洞缓解措施。另请参见 `BIND_NOW` 选项。

**`WITH_REPRODUCIBLE_BUILD`** 从内核、引导加载器和 [uname(1)](../man1/uname.1.md) 输出中排除构建元数据（如构建时间、用户或主机），使构建产生位级相同的输出。

**`WITH_REPRODUCIBLE_PATHS`** 将二进制制品中编码的路径修改为标准路径。通常，实际路径被编码在二进制文件中。但是，这使构建因构建路径而异。启用此选项后，记录的路径为 /usr/src，无论实际路径如何。禁用此选项后，记录的是实际路径。

**`WITHOUT_RESCUE`** 不构建 [rescue(8)](../man8/rescue.8.md)。

**`WITH_RETPOLINE`** 使用针对 CVE-2017-5715 的 retpoline 推测执行漏洞缓解措施构建基本系统。

**`WITHOUT_ROUTED`** 不构建 [routed(8)](../man8/routed.8.md) 工具。

**`WITH_RPCBIND_WARMSTART_SUPPORT`** 构建带 warmstart 支持的 rpcbind(8)。

**`WITH_RUN_TESTS`** 作为构建的一部分运行测试。

**`WITHOUT_SCTP_SUPPORT`** 禁用内核对 [sctp(4)](../man4/sctp.4.md) 流控制传输协议可加载内核模块的支持。

**`WITHOUT_SENDMAIL`** 不构建 sendmail(8) 及相关程序。

**`WITHOUT_SERVICESDB`** 不安装 **/var/db/services.db**。

**`WITHOUT_SETUID_LOGIN`** 设置此选项以禁用将 [login(1)](../man1/login.1.md) 安装为 set-user-ID root 程序。

**`WITHOUT_SHAREDOCS`** 不构建 4.4BSD 遗留文档。

**`WITH_SORT_THREADS`** 在 [sort(1)](../man1/sort.1.md) 中启用线程。

**`WITHOUT_SOUND`** 不构建用户空间声音工具，如 beep(1) 和 mixer(8)。

**`WITHOUT_SOURCELESS`** 不构建包含无源代码（主机 CPU 的微代码或本机代码）的内核模块。设置后，它会强制以下选项：

**`WITHOUT_SOURCELESS_HOST`** 不构建包含主机 CPU 无源本机代码的内核模块。

**`WITHOUT_SOURCELESS_UCODE`** 不构建包含无源微代码的内核模块。

**`WITHOUT_SPLIT_KERNEL_DEBUG`** 不构建独立的内核调试文件。调试数据（如果由内核配置文件启用）将包含在内核和模块中。设置后，它会强制以下选项：

**`WITHOUT_SSP`** 不使用栈溢出保护构建 world。更多信息参见 [mitigations(7)](../man7/mitigations.7.md)。

**`WITH_STAGING`** 启用将文件暂存到暂存树。这可以最好地理解为自动安装到 `DESTDIR`，带有一些额外的元数据以确保可以跟踪依赖项。依赖于 `WITH_DIRDEPS_BUILD`。设置后，以下选项也生效：必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITH_STAGING_MAN`** 启用将手册页暂存到暂存树。

**`WITH_STAGING_PROG`** 启用将 PROG 暂存到暂存树。

**`WITH_STALE_STAGED`** 检查暂存文件是否过时。

**`WITHOUT_STATS`** 既不构建也不安装 libstats 及相关二进制文件。

**`WITHOUT_SYSCONS`** 不构建 [syscons(4)](../man4/syscons.4.md) 支持文件，如键盘映射、字体和屏幕输出映射。

**`WITH_SYSROOT`** 在构建期间启用 sysroot 的使用。依赖于 `WITH_DIRDEPS_BUILD`。必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITHOUT_SYSTEM_COMPILER`** 不在构建的引导阶段投机性地跳过构建交叉编译器。通常，如果当前安装的编译器与计划的引导编译器类型和修订版匹配，则不会构建它。这不会阻止为安装而构建编译器，仅阻止为构建本身构建编译器。`WITHOUT_CLANG` 选项控制前者。

**`WITHOUT_SYSTEM_LINKER`** 不在构建的引导阶段投机性地跳过构建交叉链接器。通常，如果当前安装的链接器与计划的引导链接器类型和修订版匹配，则不会构建它。这不会阻止为安装而构建链接器，仅阻止为构建本身构建链接器。`WITHOUT_LLD` 选项控制前者。此选项仅在设置 `WITH_LLD_BOOTSTRAP` 时相关。

**`WITHOUT_TALK`** 不构建或安装 talk(1) 和 talkd(8)。

**`WITHOUT_TCP_WRAPPERS`** 不构建或安装 tcpd(8) 及相关工具。

**`WITHOUT_TCSH`** 不构建和安装 **/bin/csh**（即 [tcsh(1)](../man1/csh.1.md)）。

**`WITHOUT_TELNET`** 不构建 [telnet(1)](../man1/telnet.1.md) 及相关程序。

**`WITHOUT_TESTS`** 不在 **/usr/tests/** 中构建或安装 FreeBSD 测试套件。更多细节参见 [tests(7)](../man7/tests.7.md)。这还禁用所有测试相关依赖项的构建，包括 ATF。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITHOUT_TESTS_SUPPORT`** 禁用所有测试相关依赖项的构建，包括 ATF。设置后，它会强制以下选项：

**`WITHOUT_TEXTPROC`** 不构建用于文本处理的程序。

**`WITHOUT_TFTP`** 不构建或安装 tftp(1) 和 [tftpd(8)](../man8/tftpd.8.md)。

**`WITHOUT_TOOLCHAIN`** 不安装用于程序开发的程序，如编译器、调试器等。设置后，它会强制以下选项：设置后，以下选项也生效：

**`WITH_UBSAN`** 使用未定义行为消毒器（UBSan）构建基本系统，以在运行时检测各种未定义行为。需要将 Clang 用作基本系统编译器，并且运行时支持库可用。

**`WITHOUT_UNBOUND`** 不构建 unbound(8) 及相关程序。

**`WITH_UNDEFINED_VERSION`** 使用 --undefined-version 链接库，这允许版本映射包含库中不存在的符号。如果这对于构建特定配置是必要的，则存在错误，应报告该配置。

**`WITHOUT_UNIFIED_OBJDIR`** 对 [build(7)](../man7/build.7.md) 目标使用历史对象目录格式。对于本机构建和直接在子目录中完成的构建，使用 `${MAKEOBJDIRPREFIX}/${.CURDIR}` 格式，而对于交叉构建，使用 `${MAKEOBJDIRPREFIX}/${TARGET}.${TARGET_ARCH}/${.CURDIR}` 格式。此选项是过渡性的，将在未来版本的 FreeBSD 中移除，届时 `WITH_UNIFIED_OBJDIR` 将永久启用。必须在环境、make 命令行或 **/etc/src-env.conf** 中设置，而不是 **/etc/src.conf**。

**`WITHOUT_USB`** 不构建 USB 相关的程序和库。设置后，它会强制以下选项：

**`WITHOUT_USB_GADGET_EXAMPLES`** 不构建 USB gadget 内核模块。

**`WITHOUT_UTMPX`** 不构建用户记账工具，如 [last(1)](../man1/last.1.md)、[users(1)](../man1/users.1.md)、[who(1)](../man1/who.1.md)、ac(8)、[lastlogin(8)](../man8/lastlogin.8.md) 和 utx(8)。

**`WITH_VERIEXEC`** 启用构建 veriexec(8)，它将已验证清单的内容加载到内核中供 mac_veriexec(4) 使用。依赖于 `WITH_BEARSSL`。

**`WITHOUT_VI`** 不构建和安装 vi、view、ex 及相关程序。

**`WITHOUT_VT`** 不构建 [vt(4)](../man4/vt.4.md) 支持文件（字体和键映射）。

**`WITHOUT_WARNS`** 设置此选项以不向编译器调用添加警告标志。当代码进入源码树并在与原始开发者不同的环境中触发警告时，这作为临时变通方法很有用。

**`WITHOUT_WERROR`** 设置此选项以不将编译器警告视为错误。在修复编译器警告时作为临时变通方法很有用。设置后，警告仍会打印在构建日志中，但不会使构建失败。

**`WITHOUT_WIRELESS`** 不构建用于 802.11 无线网络的程序；特别是 wpa_supplicant(8) 和 hostapd(8)。设置后，以下选项也生效：

**`WITHOUT_WIRELESS_SUPPORT`** 构建不带 802.11 无线支持的库、程序和内核模块。

**`WITHOUT_WPA_SUPPLICANT_EAPOL`** 构建 wpa_supplicant(8) 时不带 IEEE 802.1X 协议支持，且不带 EAP-PEAP、EAP-TLS、EAP-LEAP 和 EAP-TTLS 协议支持（仅可通过 802.1X 使用）。

**`WITH_ZEROREGS`** 构建基本系统时加入在函数返回时将调用者使用的寄存器内容清零的代码。这防止了临时值的侧信道攻击泄露。此外，这减少了攻击者可用的 ROP gadget 数量。

**`WITHOUT_ZFS`** 不构建 ZFS 文件系统内核模块、libbe(3) 等库以及 zpool(8) 或 [zfs(8)](../man8/zfs.8.md) 等用户命令。同时在实现 ZFS 特定功能的工具和库中禁用 ZFS 支持。设置后，它会强制以下选项：

**`WITHOUT_ZFS_TESTS`** 不构建和安装旧版 ZFS 测试套件。

**`WITHOUT_ZONEINFO`** 不构建时区数据库。设置后，它会强制以下选项：

**`WITH_ZONEINFO_LEAPSECONDS_SUPPORT`** 在时区数据库中构建闰秒信息。此选项违反 IEEE Std 1003.1（“POSIX.1”）和所有其他适用标准，并且已知会在许多应用程序和编程语言中导致日期/时间处理的意外问题。

以下选项从有效值列表中接受单个值。

**`none`** 不初始化栈变量（标准 C/C++ 行为）。

**`pattern`** 构建基本系统或内核时，在函数入口将栈变量初始化为（编译器定义的）调试模式。

**`zero`** 构建基本系统或内核时，在函数入口将栈变量初始化为零。对于 amd64 内核构建，由于与 ifunc memset 不兼容，此值会转换为 `none`。

**`jemalloc`**

**`INIT_ALL`** 控制 C 和 C++ 代码中栈变量的默认初始化。除 `none` 外的选项需要 Clang 编译器或 GCC 12.0 或更高版本。默认值为 `none`。有效值为：

**`LIBC_MALLOC`** 指定 libc 使用的 malloc(3) 实现。默认值为 `jemalloc`。有效值为：未来在 FreeBSD 和下游消费者中都预期会有其他实现。

## 文件

**`/etc/src.conf`**
**`/etc/src-env.conf`**
**`/usr/share/mk/bsd.own.mk`**

## 参见

[make(1)](../man1/make.1.md), [make.conf(5)](make.conf.5.md), [build(7)](../man7/build.7.md), [ports(7)](../man7/ports.7.md)

## 历史

`ld-elf32.so.1` 文件出现于 FreeBSD 7.0。

## 作者

本手册页由 tools/build/options/makeman 自动生成。
