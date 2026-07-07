# release(7)

`release` — 发行版构建基础设施

## 名称

`release`

## 描述

FreeBSD 提供了一个完整的构建环境，适合用户制作 FreeBSD 操作系统的完整发行版。构建发行版所需的所有工具都可以从 FreeBSD 源代码仓库的 `src/release` 中获取。仅用一条命令即可构建完整的发行版，包括创建适合刻录到 CD-ROM 的 ISO 镜像、U 盘镜像以及网络安装目录。这条命令被恰当地命名为“`make release`”。

对于某些用户，可能希望提供一个完全干净的构建环境，不包含对源代码树或 [make.conf(5)](../man5/make.conf.5.md) 的任何本地修改，并使用 doc、src 和 ports 树的特定版本进行干净检出。为此，提供了一个脚本（`src/release/release.sh`）来自动化这些检出，然后在干净的 [chroot(8)](../man8/chroot.8.md) 中执行“`make release`”。

在尝试构建发行版之前，预期用户已熟悉 [build(7)](build.7.md) 的内容，并应具有从源代码升级系统的经验。

发行版构建过程要求 **/usr/obj** 中已填充“`make buildworld`”和“`make buildkernel`”的输出。这是为了提供发行版所需的目标文件，或者在使用 `release.sh` 时，以便完整系统的目标文件可以安装到干净的 [chroot(8)](../man8/chroot.8.md) 环境中。

如果目标发行版构建针对不同的架构或机器类型，必须使用 `TARGET` 和 `TARGET_ARCH` 变量。有关更多信息，请参见支持的 `release.conf` 变量。

某些架构上的发行版构建过程还可能要求内核中存在 [md(4)](../man4/md.4.md)（内存磁盘）设备驱动程序（通过编译进内核或作为模块提供）。

本文档不涵盖源代码管理、质量保证或发行工程过程的其他方面。

## 干净发行版生成

FreeBSD 的官方发行版在干净的环境中制作，以确保 src、ports 和 doc 树的版本之间的一致性，并避免来自主机系统的污染（如本地补丁、对 [make.conf(5)](../man5/make.conf.5.md) 的更改等）。这是通过包装脚本 `src/release/release.sh` 实现的。

`release.sh` [`-c` `release.conf`]

`release.sh` 将 `src/`、`ports/` 和 `doc/` 树检出到 `CHROOTDIR`，然后调用“`make buildworld`”和“`make installworld`”以生成 [chroot(8)](../man8/chroot.8.md) 环境。接下来，在 [chroot(8)](../man8/chroot.8.md) 环境中运行“`make release`”，并将结果放在 `$CHROOTDIR/R` 中。

可选的 `release.conf` 配置文件支持以下变量：

**`CHROOTDIR`** 构建发行版的目录。默认为 **/scratch**。

**`CHROOT_MAKEENV`** 要传递的附加 [make(1)](../man1/make.1.md) 参数，直接影响构建 chroot 的调优。

**`NOGIT`** 不显式要求安装 git(1) port。

**`GITROOT`** 用于检出各种树的 git(1) 主机。默认为 `https://git.FreeBSD.org`。

**`SRCBRANCH`** 要使用的 `src/` 分支。默认为 `-b` `main`。

**`PORTBRANCH`** 要使用的 `ports/` 分支。默认为 `head/@rHEAD`。

**`TARGET`** 用于交叉构建发行版的目标机器类型。

**`TARGET_ARCH`** 用于交叉构建发行版的目标机器架构。有关支持的 `TARGET` 和 `TARGET_ARCH` 组合列表，请参阅 [build(7)](build.7.md) 中记录的“make targets”输出。

**`KERNEL`** 要使用的目标内核配置。默认为 `GENERIC`。可以指定多个 `KERNEL` 条目。

**`MAKE_CONF`** 用于发行版构建的 [make.conf(5)](../man5/make.conf.5.md)。默认为 `/dev/null`，以防止本地系统更改污染发行版。

**`SRC_CONF`** 用于发行版构建的 [src.conf(5)](../man5/src.conf.5.md)。默认为 `/dev/null`，以防止本地系统更改污染发行版。

**`MAKE_FLAGS`** 传递给 [make(1)](../man1/make.1.md) 的附加标志。

**`WORLD_FLAGS`** 在“buildworld”阶段传递给 [make(1)](../man1/make.1.md) 的附加标志。默认为在支持 SMP 的系统上将 [make(1)](../man1/make.1.md) 作业数（`-j`）设置为可用 CPU 数量。

**`KERNEL_FLAGS`** 在“buildkernel”阶段传递给 [make(1)](../man1/make.1.md) 的附加标志。默认为在支持 SMP 的系统上将 [make(1)](../man1/make.1.md) 作业数（`-j`）设置为可用 CPU 数量的一半。

**`NOPORTS`** 设置为非空值以跳过 `ports/` 树检出。设置后，`NOPORTS` 将阻止创建 `ports.txz` 分发包。

**`WITH_DVD`** 设置为非空值以包含 `dvdrom` 目标。

**`WITH_COMPRESSED_IMAGES`** 设置为非空值以使用 [xz(1)](../man1/xz.1.md) 压缩发行版镜像。原始（未压缩）镜像不会被删除。

**`XZ_THREADS`**（`int`）设置为 [xz(1)](../man1/xz.1.md) 在压缩镜像时应使用的线程数。默认情况下，`XZ_THREADS` 设置为 `0`，使用系统上所有可用的核心。

**`VCSCMD`** 用于获取源代码树的命令。默认为“” `git clone` `-q`。

**`CHROOTBUILD_SKIP`** 如果定义，则跳过 [chroot(8)](../man8/chroot.8.md) 构建环境设置的 `buildworld`、`installworld` 和 `distribution` 阶段。这仅适用于 [chroot(8)](../man8/chroot.8.md) 用户空间由其他方式提供的情况。

**`SRC_UPDATE_SKIP`** 设置为非空值以防止在 [chroot(8)](../man8/chroot.8.md) 中检出或更新 **/usr/src**。这仅适用于 **/usr/src** 预期以其他方式存在的情况。

**`PORTS_UPDATE_SKIP`** 设置为非空值以防止在 [chroot(8)](../man8/chroot.8.md) 中检出或更新 **/usr/ports**。这仅适用于 **/usr/ports** 预期以其他方式存在的情况。

**`NOPKGBASE`** 包含用于安装介质的传统 tarball 分发集，而不是基本系统软件包。

**`PKG_CMD`** 在以非 root 用户身份在发行版镜像中安装软件包时要使用的 [pkg(8)](../man8/pkg.8.md) 可执行文件路径。

**`PKG_REPOS_DIR`** 包含 [pkg(8)](../man8/pkg.8.md) 仓库配置文件的目录的可选路径。在以非 root 用户身份在发行版镜像中安装软件包时将使用这些配置文件。

**`PKG_REPO_NAME`** 在以非 root 用户身份在发行版镜像中安装软件包时要使用的仓库配置名称。

## 嵌入式构建

以下 `release.conf` 变量仅与嵌入式系统的发行版构建相关：

**`EMBEDDEDBUILD`** 设置为非空值以启用嵌入式设备发行版构建功能。设置后，`WITH_DVD` 将被取消设置。此外，还必须定义 `EMBEDDED_TARGET` 和 `EMBEDDED_TARGET_ARCH`。创建构建环境时，`release.sh` 会运行位于 `src/release/${EMBEDDED_TARGET}/` 中特定架构目录下的单独构建脚本。

**`EMBEDDEDPORTS`** 设置为目标设备所需的任何 port 列表，格式为 `category/port`。

**`EMBEDDED_TARGET`** 设置后，其值传递给 [make(1)](../man1/make.1.md) 以设置 `TARGET`（`uname` `-m` 的值），用于交叉构建目标用户空间。

**`EMBEDDED_TARGET_ARCH`** 设置后，其值传递给 [make(1)](../man1/make.1.md) 以设置 `TARGET_ARCH`（`uname` `-p` 的值），用于交叉构建目标用户空间。

## 虚拟机磁盘镜像

以下 `release.conf` 变量仅与虚拟机磁盘镜像构建相关：

**`WITH_VMIMAGES`** 设置为非空值以作为发行版构建的一部分构建虚拟机磁盘镜像。`WITH_VMIMAGES` 也可以指定为传递给 [make(1)](../man1/make.1.md) 的环境变量。

**`WITH_COMPRESSED_VMIMAGES`** 设置为非空值以作为 `install` [make(1)](../man1/make.1.md) 目标的一部分，使用 [xz(1)](../man1/xz.1.md) 压缩虚拟机磁盘镜像。请注意，在某些系统上压缩虚拟机磁盘镜像可能需要很长时间。

**`VMBASE`** 设置以更改生成的虚拟机磁盘镜像文件名。默认值为 `vm`。

**`VMSIZE`** 设置以更改虚拟机磁盘容量大小。默认值为 `20g`。有关有效值，请参见 makefs(8)。默认情况下，虚拟机磁盘镜像以稀疏镜像形式创建。当使用 `WITH_COMPRESSED_VMIMAGES` 时，使用 [xz(1)](../man1/xz.1.md) 压缩后得到的文件大小大致相同，无论指定的磁盘镜像大小如何。

**`VMFS`**（已弃用。）设置以指定 `VMFSLIST` 中列出的哪个文件系统链接到历史的非文件系统标记文件名。有效值为 `ufs` 和 `zfs`。默认值为 `ufs`。

**`VMFSLIST`** 设置以指定要为其构建镜像的文件系统类型列表。有效值为 `ufs` 和 `zfs` 中的一个或两者。默认值为 `ufs zfs`。

**`VMFORMATS`** 设置要创建的目标虚拟磁盘镜像格式。默认情况下，创建 `vhdf`、`vmdk`、`qcow2` 和 `raw` 格式。有关有效格式值，请参见 mkimg(1)。

有关支持的 `VMFORMATS` 值列表（包括云托管提供商格式）及简要说明，请运行：

```sh
cd /usr/src
make -C release list-vmtargets
```

## 云托管机器镜像

FreeBSD 发行版构建工具支持为各种云托管提供商构建虚拟机镜像，每个提供商都有各自的特定配置，以默认包含对每个托管提供商的支持。

以下 [make(1)](../man1/make.1.md) 环境变量受支持：

**`CLOUDWARE`** 设置为一个或多个云托管提供商列表，用引号括起。需要同时设置 `WITH_CLOUDWARE`。

**`WITH_CLOUDWARE`** 设置为非空值以启用为各种云托管提供商构建虚拟机镜像。需要同时设置 `CLOUDWARE`。

此外，`CLOUDWARE` 和 `WITH_CLOUDWARE` 变量可以添加到 `release.conf` 中，与 `release.sh` 配合使用。

有关支持的 `CLOUDWARE` 值列表，请运行：

```sh
cd /usr/src
make -C release list-cloudware
```

## OCI 镜像

FreeBSD 发行版构建工具对构建 Open Container Initiative（OCI）格式容器基础镜像有实验性支持。这通过 `release.conf` 变量启用：

**`WITH_OCIIMAGES`** 设置为非空值以构建 OCI 基础镜像。

## Makefile 目标

发行版 makefile（`src/release/Makefile`）相当晦涩。大多数开发者只关心 `release` 和 `install` 目标。

**`release`** 用于构建适用于此平台的所有发行版介质和分发的元目标。

**`install`** 将所有生成的发行版介质复制到 `${DESTDIR}`。

**`cdrom`** 构建安装 CD-ROM 镜像。这可能要求内核中存在 [md(4)](../man4/md.4.md)（内存磁盘）设备驱动程序（通过编译进内核或作为模块提供）。此目标产生名为 `disc1.iso` 和 `bootonly.iso` 的文件作为输出。

**`dvdrom`** 构建安装 DVD-ROM 镜像。这可能要求内核中存在 [md(4)](../man4/md.4.md)（内存磁盘）设备驱动程序（通过编译进内核或作为模块提供）。此目标产生 `dvd1.iso` 文件作为输出。

**`memstick`** 构建名为 `memstick.img` 的安装 U 盘镜像。并非在所有平台上都适用。要求内核中存在 [md(4)](../man4/md.4.md)（内存磁盘）设备驱动程序（通过编译进内核或作为模块提供）。

**`mini-memstick`** 类似于 `memstick`，但不包含安装分发集。

**`ftp`** 创建名为 `ftp` 的目录，其中包含用于网络安装的分发文件，适合上传到 FTP 镜像。

**`vm-image`** 以各种格式创建虚拟机磁盘镜像。`vm-image` 目标要求将 `WITH_VMIMAGES` [make(1)](../man1/make.1.md) 环境变量设置为非空值。

**`vm-cloudware`** 为各种云托管提供商构建 FreeBSD 虚拟机镜像。实现细节请参见“云托管机器镜像”章节。

**`list-cloudware`** 显示有效的 `CLOUDWARE` 值列表。

**`list-vmtargets`** 显示有效的 `VMFORMATS` 和 `CLOUDWARE` 值列表。

上述目标调用的主要子目标：

**`packagesystem`** 生成适用于此平台的所有分发归档（base、kernel、ports、doc）。

**`disc1`** 构建一个可引导的安装系统，包含由 `packagesystem` 目标打包的所有分发文件，适用于 `cdrom`、`dvdrom` 和 `memstick` 目标进行镜像制作。

**`reldoc`** 构建发行版文档。这包括发行说明、硬件指南和安装说明。其他文档（如 Handbook）在 `packagesystem` 调用的 `base.txz` 目标期间构建。

## 环境变量

可选变量：

**`OSRELEASE`** 调用 `install` 目标时生成的介质镜像的可选基础名称（例如 FreeBSD-12.1-RELEASE-amd64）。默认为 chroot 中 ``uname -s`-`uname -r`-`uname -p`` 的输出。

**`WORLDDIR`** 包含 src 树的目录位置。默认为包含 makefile（`src`）的目录上一级目录。

**`PORTSDIR`** 包含 ports 树的目录位置。默认为 **/usr/ports**。如果未设置或找不到，发行版中将不包含 ports。

**`NOPORTS`** 如果定义，Ports Collection 将从发行版中省略。

**`NOSRC`** 如果设置，发行版中不包含系统源代码。

**`TARGET`** 目标硬件平台。这类似于“`uname` `-m`”输出。这对于交叉构建某些目标架构是必需的。例如，交叉构建 ARM64 机器需要 `TARGET_ARCH`=`aarch64` 和 `TARGET`=`arm64`。如果未设置，`TARGET` 默认为当前硬件平台。

**`TARGET_ARCH`** 目标机器处理器架构。这类似于“`uname` `-p`”输出。设置此项以交叉构建不同的架构。如果未设置，`TARGET_ARCH` 默认为当前机器架构，除非同时设置了 `TARGET`，在这种情况下它默认为该平台的适当值。通常，只需设置 `TARGET`。

## 文件

**`/scratch`**
**`/usr/doc/Makefile`**
**`/usr/doc/share/mk/doc.project.mk`**
**`/usr/ports/Mk/bsd.port.mk`**
**`/usr/ports/Mk/bsd.sites.mk`**
**`/usr/share/examples/etc/make.conf`**
**`/usr/src/Makefile`**
**`/usr/src/Makefile.inc1`**
**`/usr/src/release/Makefile`**
**`/usr/src/release/Makefile.vm`**
**`/usr/src/release/release.sh`**
**`/usr/src/release/release.conf.sample`**
**`/usr/src/release/tools/*.conf`**
**`/usr/src/release/tools/vmimage.subr`**

## 实例

以下命令序列可用于构建“-CURRENT 快照”：

```sh
cd /usr
git clone -b main https://git.freebsd.org/src.git src
cd src
make buildworld buildkernel
cd release
make obj
make release
make install DESTDIR=/var/freebsd-snapshot
```

运行这些命令后，所有生成的分发文件（用于 FTP 的 tarball、CD-ROM 镜像等）都可以在 **/var/freebsd-snapshot** 目录中找到。

以下命令序列可用于在干净环境中构建“-CURRENT 快照”，包括 ports 和文档：

```sh
cd /usr/src/release
sh release.sh
```

可以选择使用配置文件来自定义发行版构建：

```sh
cd /usr/src/release
sh release.sh -c $HOME/release.conf
```

特定于各种受支持嵌入式系统（如 Raspberry Pi）的配置文件存在于与 `TARGET` [make(1)](../man1/make.1.md) 变量对应的目录中。例如，要为 64 位 Raspberry Pi 构建镜像：

```sh
cd /usr/src/release
sh release.sh -c arm64/RPI.conf
```

运行这些命令后，所有准备好的发行版文件都可以在 **/scratch** 目录中找到。可以通过在 `release.conf` 中指定 `CHROOTDIR` 变量来更改目标目录。

## 兼容性

reldoc 目标在提交 f61e92ca5a23 中已移除，因此 `DOCDIR`、`DOCBRANCH`、`DOC_UPDATE_SKIP` 和 `NODOC` 不再受支持。

## 参见

[cc(1)](../man1/clang.1.md), git(1)（`ports/devel/git`）, install(1), [make(1)](../man1/make.1.md), mkimg(1), [uname(1)](../man1/uname.1.md), [md(4)](../man4/md.4.md), [make.conf(5)](../man5/make.conf.5.md), [build(7)](build.7.md), [ports(7)](ports.7.md), [chroot(8)](../man8/chroot.8.md), [mtree(8)](../man8/mtree.8.md), [sysctl(8)](../man8/sysctl.8.md)

> "FreeBSD Release Engineering"。

> "FreeBSD Developers' Handbook"。

## 历史

FreeBSD 1.x 使用由 Rod Grimes 编制的手动清单来制作发行版。该清单除了不完整外，对可用文件系统提出了许多特定要求，执行起来相当痛苦。

作为 FreeBSD 2.0 发行工程工作的一部分，人们花费了大量精力使 `src/release/Makefile` 至少能够自动化在无菌环境中构建发行版的大部分繁琐工作。

对于 FreeBSD 9.0 发行版，`src/release/Makefile` 经过全面修订，并引入了包装脚本 `src/release/generate-release.sh` 以支持新安装程序的引入。

对于 FreeBSD 9.2 发行版，引入了 `src/release/release.sh` 以支持每次构建的配置文件。`src/release/release.sh` 在很大程度上基于 `src/release/generate-release.sh` 脚本。

在分布于多个分支的近 1000 次修订中，`src/release/Makefile` 的 git(1) 日志包含了发行工程师所经历的一些艰难困苦的生动历史记录。

## 作者

`src/release/Makefile` 最初由 Rod Grimes、Jordan Hubbard 和 Poul-Henning Kamp 编写。

本手册页最初由 Murray Stokely <murray@FreeBSD.org> 编写。

Nathan Whitehorn <nwhitehorn@FreeBSD.org> 更新了本手册页，加入了用于 FreeBSD 9.0 发行周期的 `generate-release.sh` 脚本。

Glen Barber <gjb@FreeBSD.org> 后来更新了本手册页，加入了用于 FreeBSD 9.2 发行周期的 `release.sh` 脚本。
