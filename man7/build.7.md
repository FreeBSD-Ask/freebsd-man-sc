# build(7)

`build` — 构建 FreeBSD 系统的通用说明

## 名称

`build` FreeBSD 系统

## 描述

FreeBSD 系统及其应用程序的源代码包含在三个目录中，通常为：

**`/usr/src`** “基本系统”，大致定义为将系统构建到可用状态所需的一切

**`/usr/doc`** 系统文档，不包括手册页

**`/usr/ports`** 第三方软件，提供一致的构建和安装接口；参见 [ports(7)](ports.7.md)

在使用 Git（来自 FreeBSD Ports Collection 的 `devel/git`）更新之前，这些目录可能初始为空或不存在

在每个目录中使用 [make(1)](../man1/make.1.md) 命令构建和安装该目录中的内容。在任何目录中发出 [make(1)](../man1/make.1.md) 命令都会在所有子目录中递归发出 [make(1)](../man1/make.1.md) 命令。未指定目标时，仅构建目录中的项目，不执行其他操作。

源代码树允许只读。如 [make(1)](../man1/make.1.md) 所述，对象通常在由环境变量 `MAKEOBJDIRPREFIX` 指定的单独对象目录层次结构中构建，若未设置变量 `MAKEOBJDIRPREFIX`，则在 `/usr/obj` 下构建。规范对象目录在下文 `buildworld` 目标的文档中说明。

`build` 可通过定义下文 Sx ENVIRONMENT 章节中描述的 [make(1)](../man1/make.1.md) 变量，以及 [make.conf(5)](../man5/make.conf.5.md) 中记录的变量来控制。

构建中包含的默认组件在源代码树的 `/etc/src.conf` 文件中指定。要覆盖默认文件，在 make 步骤中包含 SRCCONF 选项，指向自定义的 src.conf 文件。更多信息参见 [src.conf(5)](../man5/src.conf.5.md)。

以下列表提供构建系统支持的目标名称和操作：

**`analyze`** 对所有对象运行 Clang 静态分析器，并在 stdout 上呈现输出。

**`check`** 为给定子目录运行测试。使用的默认目录是 `${.OBJDIR}`，但可通过 `${CHECKDIR}` 更改检查目录。

**`checkworld`** 在已安装的 world 上运行 FreeBSD 测试套件。

**`clean`** 移除构建过程中创建的所有文件。

**`cleandepend`** 移除先前“`make`”和“`make depend`”步骤生成的 `${.OBJDIR}/${DEPENDFILE}*` 文件。

**`cleandir`** 如果存在规范对象目录则移除之，否则执行等效于“`make clean cleandepend`”的操作。此目标还会移除 `${.CURDIR}` 中的 `obj` 链接（如果存在）。建议运行“`make cleandir`”两次：第一次调用移除规范对象目录，第二次清理 `${.CURDIR}`。

**`depend`** 在文件 `${.OBJDIR}/${DEPENDFILE}` 中生成构建依赖列表。每个对象的依赖在构建时生成并存储在 `${.OBJDIR}/${DEPENDFILE}.${OBJ}` 中。

**`install`** 将构建结果安装到变量 `DESTDIR` 指定的安装目录层次结构中的相应位置。

**`obj`** 创建与当前目录关联的规范对象目录。

**`objlink`** 在 `${.CURDIR}` 中创建指向规范对象目录的符号链接。

**`tags`** 使用 [make(1)](../man1/make.1.md) 变量 `CTAGS` 指定的程序生成 tags 文件。构建系统支持 ctags(1) 和 `GNU Global`。

目录 `/usr/src` 下支持的其他目标：

- 如果正在更新旧仓库，则自上一版本以来内容未更改的包将被复制到新仓库中，以避免不必要的版本号更新。
- 如果定义了 `PKG_REPO_SIGNING_KEY`，仓库将根据 pkg-repo(8) 进行签名。

**`buildenv`** 启动一个交互式 shell，其环境变量已设置为构建系统或单个组件。对于交叉构建，需要用 [make(1)](../man1/make.1.md) 变量 `TARGET_ARCH` 和 `TARGET` 指定目标架构。此目标仅在完整工具链（包括编译器、链接器、汇编器、头文件和库）构建完成后才有用；参见下文的 `toolchain` 目标。执行 `BUILDENV_SHELL`，默认为 `/bin/sh`。可将其设置为在此构建环境中执行操作的命令，如交叉构建应用程序。但如果该应用程序有依赖关系，`devel/poudriere` 包或 port 提供更通用的解决方案。

**`buildenvvars`** 打印为 `buildenv` 环境设置的 shell 变量并退出。

**`buildworld`** 构建除内核、`etc` 中的配置文件和 `release` 之外的所有内容。可通过设置 `MAKEOBJDIRPREFIX` [make(1)](../man1/make.1.md) 变量将对象目录从默认的 `/usr/obj` 更改。使用的实际构建位置前缀取决于 [src.conf(5)](../man5/src.conf.5.md) 中的 `WITH_UNIFIED_OBJDIR` 选项。启用时，所有构建使用 `${MAKEOBJDIRPREFIX}${.CURDIR}/${TARGET}.${TARGET_ARCH}`。禁用时，原生构建使用 `${MAKEOBJDIRPREFIX}${.CURDIR}`，交叉构建和设置了变量 `CROSS_BUILD_TESTING` 的原生构建使用 `${MAKEOBJDIRPREFIX}/${TARGET}.${TARGET_ARCH}${.CURDIR}`。

**`cleankernel`** 尝试清理由先前 `buildkernel` 或类似步骤构建的目标，这些步骤从同一源目录和 `KERNCONF` 构建。

**`cleanworld`** 尝试清理由先前 `buildworld` 或类似步骤构建的目标，这些步骤从此源目录构建。

**`cleanuniverse`** 启用 `WITH_UNIFIED_OBJDIR` 时，尝试清理由先前 `buildworld`、`universe` 或类似步骤构建的目标，针对从此源目录构建的任何架构。

**`distributeworld`** 分发先前 `buildworld` 步骤编译的所有内容。文件放置在 [make(1)](../man1/make.1.md) 变量 `DISTDIR` 指定的目录层次结构中。此目标在构建 release 时使用；参见 [release(7)](release.7.md)。

**`native-xtools`** 此目标为给定 **TARGET** 和 **TARGET_ARCH,** 构建交叉工具链，以及主机系统的精选静态用户态工具列表。旨在 jail 中使用 QEMU 时使用，通过避免模拟不需要模拟的二进制文件来提高性能。应定义 **TARGET** 和 **TARGET_ARCH**。

**`native-xtools-install`** 将结果安装到 `${DESTDIR}/${NXTP}`，其中 `NXTP` 默认为 `nxb-bin`。必须定义 **TARGET** 和 **TARGET_ARCH**。

**`packages`** 创建包含可用于安装或升级基本系统的包的 [freebsd-base(7)](freebsd-base.7.md) 包仓库。仓库在对象目录下的 `${REPODIR}/${PKG_ABI}` 中创建，其中 `REPODIR` 是创建仓库的基目录，`PKG_ABI` 是构建目标的 pkg(7) ABI，例如 `/usr/obj/${SRCDIR}/repo/FreeBSD:15:amd64`。

**`packageworld`** 归档 `distributeworld` 的结果，将结果放入 `DISTDIR`。此目标在构建 [release(7)](release.7.md) 时使用，与构建 [freebsd-base(7)](freebsd-base.7.md) 包无关。

**`installworld`** 将先前 `buildworld` 步骤构建的所有内容安装到 [make(1)](../man1/make.1.md) 变量 `DESTDIR` 指向的目录层次结构中。如果安装到 NFS 文件系统并使用 `-j` 选项运行 [make(1)](../man1/make.1.md)，确保 rpc.lockd(8) 在客户端和服务器上都运行。参见 [rc.conf(5)](../man5/rc.conf.5.md) 了解如何使其在启动时运行。

**`toolchain`** 创建构建系统其余部分所需的构建工具链。对于跨架构构建，此步骤创建交叉工具链。

**`universe`** 对每个架构执行 `buildworld`，然后对该架构的所有内核（包括 `LINT`）执行 `buildkernel`。此命令耗时较长。

**`kernels`** 类似于定义了 `WITHOUT_WORLDS` 的 `universe`，因此只构建每个架构的内核。

**`worlds`** 类似于定义了 `WITHOUT_KERNELS` 的 `universe`，因此只构建每个架构的 world。

**`targets`** 打印 world 和 kernel 目标支持的 `TARGET`/`TARGET_ARCH` 对列表。

**`tinderbox`** 执行与 `universe` 相同的目标。此外在结束时打印所有失败目标的摘要，如果有任何失败则以错误退出。

**`toolchains`** 为构建系统支持的每个架构创建构建工具链。

**`xdev`** 为给定 **TARGET** 和 **TARGET_ARCH.** 构建并安装交叉工具链和 sysroot。sysroot 包含目标库和头文件。该目标是 `xdev-build` 和 `xdev-install` 的别名。安装文件的位置可通过 `DESTDIR` 控制。`DESTDIR` 中的目标位置为 `${DESTDIR}/${XDTP}`，其中 `XDTP` 默认为 `/usr/${XDDIR}`，`XDDIR` 默认为 `${TARGET_ARCH}-freebsd`。

**`update-packages`** 为基本系统创建或更新 [freebsd-base(7)](freebsd-base.7.md) 包仓库。

**`xdev-build`** 为 `xdev` 目标构建。

**`xdev-install`** 为 `xdev` 目标安装文件。

**`xdev-links`** 在 `${DESTDIR}/usr/bin` 中安装 autoconf 风格的符号链接，指向 `${DESTDIR}/${XDTP}` 中的 xdev 工具链。

`/usr/src` 中特定于内核的构建目标：

**`buildkernel`** 重新构建内核和内核模块。可通过设置 `MAKEOBJDIRPREFIX` [make(1)](../man1/make.1.md) 变量将对象目录从默认的 `/usr/obj` 更改。

**`installkernel`** 将内核和内核模块安装到目录 `${DESTDIR}/boot/kernel`，如果先前存在同名目录且包含当前运行的内核，则将其重命名为 `kernel.old`。可使用 `INSTKERNNAME` 或 `KODIR` [make(1)](../man1/make.1.md) 变量修改 `${DESTDIR}` 下的目标目录。

**`distributekernel`** 将内核安装到目录 `${DISTDIR}/kernel/boot/kernel`。此目标在构建 release 时使用；参见 [release(7)](release.7.md)。

**`packagekernel`** 归档 `distributekernel` 的结果，将结果放入 `DISTDIR`。此目标在构建 [release(7)](release.7.md) 时使用，与构建 [freebsd-base(7)](freebsd-base.7.md) 包无关。

**`kernel`** 等效于 `buildkernel` 后跟 `installkernel`

**`kernel-toolchain`** 重新构建内核编译所需的工具。如果未先执行 `buildworld`，请使用此目标。

**`reinstallkernel`** 重新安装内核和内核模块，覆盖目标目录的内容。与 `installkernel` 目标一样，可使用 [make(1)](../man1/make.1.md) 变量 `INSTKERNNAME` 指定目标目录。

清理由变量 `DESTDIR` 表示的安装目标目录的便捷目标包括：

**`check-old`** 打印系统中旧文件和目录的列表。

**`check-old-libs`** 打印过时的基本系统库列表。

**`delete-old`** 以交互方式删除过时的基本系统文件和目录。在命令行指定 `-DBATCH_DELETE_OLD_FILES` 时，删除操作将以非交互方式进行。变量 `DESTDIR`、`TARGET_ARCH` 和 `TARGET` 的设置应与“`make installworld`”相同。

**`delete-old-libs`** 以交互方式删除过时的基本系统库。此目标仅在没有第三方软件使用这些库时使用。在命令行指定 `-DBATCH_DELETE_OLD_FILES` 时，删除操作将以非交互方式进行。变量 `DESTDIR`、`TARGET_ARCH` 和 `TARGET` 的设置应与“`make installworld`”相同。

## 环境变量

影响所有构建的变量包括：

**`DEBUG_FLAGS`** 定义一组调试标志，用于构建 `/usr/src` 下的所有用户态二进制文件。定义 `DEBUG_FLAGS` 时，`install` 和 `installworld` 目标从当前 `MAKEOBJDIRPREFIX` 安装二进制文件而不剥离，以便在安装的二进制文件中保留调试信息。

**`DESTDIR`** 安装构建对象的目录层次结构前缀。未设置时，`DESTDIR` 默认为空字符串。设置时，`DESTDIR` 必须指定绝对路径。

**`MAKEOBJDIRPREFIX`** 定义构建对象树中目录名的前缀。未定义时默认为 `/usr/obj`。此变量只能在环境或 `/etc/src-env.conf` 中设置，不能通过 `/etc/make.conf` 或 `/etc/src.conf` 或命令行设置。`MAKEOBJDIRPREFIX` 必须指定绝对路径。

**`WITHOUT_WERROR`** 如果定义，编译器警告不会导致构建停止，即使 makefile 另有说明。

**`WITH_CTF`** 如果定义，构建过程将对构建对象运行 DTrace CTF 转换工具。

此外，`/usr/src` 中的构建受以下 [make(1)](../man1/make.1.md) 变量影响：

```sh
PORTS_MODULES=graphics/gpu-firmware-intel-kmod@kabylake
PORTS_MODULES+=graphics/drm-66-kmod
```

```sh
make some-target SUBDIR_OVERRIDE=foo/bar
```

**`CROSS_TOOLCHAIN`** 请求使用外部工具链构建 world 或内核。此变量的值可以是文件的完整路径，或 `${LOCALBASE}/share/toolchains` 中文件的基本名称。该文件应为 make 文件，设置变量以请求外部工具链，如 `XCC`。Ports 中提供 LLVM 和 GCC/binutils 的外部工具链。对于 Ports 中可用的外部工具链，`CROSS_TOOLCHAIN` 应设置为包名。LLVM 工具链包使用名称 llvm<主版本号>。GCC 工具链为每个架构提供单独的包，使用名称 ${MACHINE_ARCH}-gcc<主版本号>。

**`INSTKERNNAME`** 如果设置，指定各种内核 make 目标的替代构建和安装名称。默认为“`kernel`”。

**`KERNCONF`** 指定一个或多个空格分隔的内核，用于各种内核 make 目标的构建和安装。如果指定多个内核，第一个列出的内核安装到 `/boot/${INSTKERNNAME}`，后续内核安装到 `/boot/${INSTKERNNAME}.NAME`。未设置时，默认为 GENERIC，但 POWER 架构例外，powerpc64 默认为 GENERIC64，powerpc64le 默认为 GENERIC64LE。

**`KERNBUILDDIR`** 覆盖默认目录以获取构建内核模块的所有 opt_\*.h 文件。适用于依赖 [config(8)](../man8/config.8.md) 选项的独立模块。对于随内核构建的模块自动设置。

**`KERNCONFDIR`** 覆盖应在其中查找 `KERNCONF` 和 `KERNCONF` 包含的任何文件的目录。默认为 `sys/${ARCH}/conf`。

**`KERNFAST`** 如果设置，构建目标 `buildkernel` 默认设置 `NO_KERNELCLEAN`、`NO_KERNELCONFIG` 和 `NO_KERNELOBJ`。设置为 `1` 以外的值时，`KERNCONF` 设置为 `KERNFAST` 的值。

**`KODIR`** 如果设置，此变量指定安装内核的替代目录。

**`LOCAL_DIRS`** 如果设置，此变量提供相对于源代码树根的附加目录列表，作为 `everything` 目标的一部分构建。这些目录相互并行构建，并与基本系统目录并行构建。在 `LOCAL_DIRS` 列表开头插入 `.WAIT` 指令可确保先构建所有基本系统目录。`.WAIT` 也可根据需要在列表中的其他位置使用。

**`LOCAL_ITOOLS`** 如果设置，此变量提供 `installworld` 和 `distributeworld` 目标使用的附加工具列表。

**`LOCAL_LIB_DIRS`** 如果设置，此变量提供相对于源代码树根的附加目录列表，作为 `libraries` 目标的一部分构建。这些目录相互并行构建，并与基本系统库并行构建。在 `LOCAL_DIRS` 列表开头插入 `.WAIT` 指令可确保先构建所有基本系统库。`.WAIT` 也可根据需要在列表中的其他位置使用。

**`LOCAL_MTREE`** 如果设置，此变量提供相对于源代码树根的附加 mtree 列表，作为 `hierarchy` 目标的一部分使用。

**`LOCAL_LEGACY_DIRS`** 如果设置，此变量提供相对于源代码树根的附加目录列表，作为 `legacy` 目标的一部分构建。

**`LOCAL_BSTOOL_DIRS`** 如果设置，此变量提供相对于源代码树根的附加目录列表，作为 `bootstrap-tools` 目标的一部分构建。

**`LOCAL_TOOL_DIRS`** 如果设置，此变量提供相对于源代码树根的附加目录列表，作为 `build-tools` 目标的一部分构建。

**`LOCAL_XTOOL_DIRS`** 如果设置，此变量提供相对于源代码树根的附加目录列表，作为 `cross-tools` 目标的一部分构建。

**`OBJROOT`** 对象目录根定义为 `${OBJDIR}/${SRCDIR}/`。参见 `share/mk/src.sys.obj.mk`。

**`PKG_FORMAT`** 构建 [freebsd-base(7)](freebsd-base.7.md) 包时指定包压缩格式。默认：`tzst`。考虑使用 `tar` 禁用压缩。可接受的选项记录在 pkg-create(8) 的 `-f` 描述中。

**`PORTS_MODULES`** 具有内核模块的 ports 列表，应作为 `buildkernel` 和 `installkernel` 流程的一部分构建和安装。目前与构建 [freebsd-base(7)](freebsd-base.7.md) 包不兼容。每个 port 必须指定为 `category``/``port`[`@``flavor`]，例如

**`LOCAL_MODULES`** 外部内核模块列表，应作为 `buildkernel` 和 `installkernel` 流程的一部分构建和安装。默认为 `LOCAL_MODULES_DIR` 的子目录列表。

**`LOCAL_MODULES_DIR`** 搜索 `LOCAL_MODULES` 指定的内核模块的目录。每个内核模块应由包含 makefile 的目录组成。默认为 `${LOCALBASE}/sys/modules`。

**`SRCCONF`** 指定覆盖默认 `/etc/src.conf` 的文件。src.conf 文件控制要构建的组件。参见 [src.conf(5)](../man5/src.conf.5.md)

**`REPODIR`** 用于创建构建 packages(7) 包仓库的根目录。默认为 `${OBJROOT}/repo/`。也可在 src-env.conf(5) 中设置。

**`STRIPBIN`** 安装时剥离二进制文件时使用的命令。确保在运行 `distributeworld` 或 `installworld` 目标之前，将运行 `STRIPBIN` 所需的任何附加工具添加到 `LOCAL_ITOOLS` [make(1)](../man1/make.1.md) 变量中。更多细节参见 install(1)。

**`SUBDIR_OVERRIDE`** 覆盖默认子目录列表，仅构建此变量中命名的子目录。如果与 `buildworld` 组合，则所有库和 includes 以及某些构建工具仍会构建。指定 `-DNO_LIBS` 和 `-DWORLDFAST` 将仅构建指定目录，如同历史做法。与 `buildworld` 组合时，必须用包含库的任何自定义目录覆盖 `LOCAL_LIB_DIRS`。这允许以与 `buildworld` 使用其 sysroot 处理相同的方式构建系统的子集。此变量在调试失败的构建时也很有用。

**`SYSDIR`** 指定内核源代码位置以覆盖默认的 `/usr/src/sys`。内核源代码位于从 `src.git` 仓库检出的源代码树的 `sys` 子目录中。

**`TARGET`** 目标硬件平台。类似于“`uname` `-m`”输出。交叉构建某些目标架构时需要。例如，交叉构建 ARM64 机器需要 `TARGET_ARCH`=`aarch64` 和 `TARGET`=`arm64`。未设置时，`TARGET` 默认为当前硬件平台，除非也设置了 `TARGET_ARCH`，此时默认为该架构的适当值。

**`TARGET_ARCH`** 目标机器处理器架构。类似于“`uname` `-p`”输出。设置此项以交叉构建不同架构。未设置时，`TARGET_ARCH` 默认为当前机器架构，除非也设置了 `TARGET`，此时默认为该平台的适当值。通常只需设置 `TARGET`。

`/usr/src` 目录下的构建还受通过 [make(1)](../man1/make.1.md) 的 `-D` 选项定义以下一个或多个符号的影响：

**`LOADER_DEFAULT_INTERP`** 定义默认加载器程序的解释器。有效值包括“4th”、“lua”和“simp”。这会创建 `/boot/loader` 到具有该解释器的加载器的默认链接。它还决定编译到 `userboot` 中的解释器。

**`NO_CLEANDIR`** 如果设置，清理对象树部分的构建目标使用等效的“make clean”而非“make cleandir”。

**`NO_CLEAN`** 如果设置，完全不清理任何对象树文件。这是 `WITH_META_MODE` 与 [filemon(4)](../man4/filemon.4.md) 一起使用时的默认行为。更多细节参见 [src.conf(5)](../man5/src.conf.5.md)。设置 `NO_CLEAN` 意味着 `NO_KERNELCLEAN`，因此设置 `NO_CLEAN` 时也不清理内核对象。

**`NO_CTF`** 如果设置，构建过程不对构建对象运行 DTrace CTF 转换工具。

**`NO_SHARE`** 如果设置，构建不进入 `/usr/src/share` 子目录（即手册页、区域设置数据文件、时区数据文件和其他 `/usr/src/share` 文件不会从其源代码重新构建）。

**`NO_KERNELCLEAN`** 如果设置，构建过程不作为 `buildkernel` 目标的一部分运行“make clean”。

**`NO_KERNELCONFIG`** 如果设置，构建过程不作为 `buildkernel` 目标的一部分运行 [config(8)](../man8/config.8.md)。

**`NO_KERNELOBJ`** 如果设置，构建过程不作为 `buildkernel` 目标的一部分运行“make obj”。

**`NO_LIBS`** 如果设置，将跳过库阶段。

**`NO_OBJWALK`** 如果设置，不创建对象目录。仅在先前构建中已创建对象目录且未连接新目录时使用。

**`UNIVERSE_TOOLCHAIN`** 请求使用作为 `universe` 目标一部分构建的工具链作为外部工具链。

**`WORLDFAST`** 如果设置，构建目标 `buildworld` 默认设置 `NO_CLEAN`、`NO_OBJWALK`，并跳过大多数引导阶段。它仅引导库并构建所有用户态。仅在已知无需更改任何引导且未连接新目录到构建时使用此选项。

`/usr/doc` 目录下的构建受以下 [make(1)](../man1/make.1.md) 变量影响：

**`DOC_LANG`** 如果设置，将文档构建限制为作为其内容指定的语言子目录。默认操作是构建所有语言的文档。

使用 `universe` 及相关目标的构建受以下 [make(1)](../man1/make.1.md) 变量影响：

**`JFLAG`** 将此变量的值传递给用于构建 world 和内核的每次 [make(1)](../man1/make.1.md) 调用。可用于在单个架构构建中启用多个作业，同时仍按顺序构建每个架构。

**`MAKE_JUST_KERNELS`** 仅构建每个支持架构的内核。

**`MAKE_JUST_WORLDS`** 仅构建每个支持架构的 world。

**`WITHOUT_WORLDS`** 仅构建每个支持架构的内核。

**`WITHOUT_KERNELS`** 仅构建每个支持架构的 world。

**`UNIVERSE_LOGDIR`** 将每个支持架构的所有构建日志写入此目录。调用 `tinderbox` 时，还将所有失败目标的摘要写入此目录。

**`UNIVERSE_TARGET`** 为每个支持架构执行指定的 [make(1)](../man1/make.1.md) 目标，而非构建一个 world 和一个或多个内核的默认操作。此变量意味着 `WITHOUT_KERNELS`。

**`USE_GCC_TOOLCHAINS`** 使用外部 GCC 工具链构建请求的目标。如果未安装支持架构所需工具链包，则跳过该架构的构建。可通过将此变量的值设置为所需版本（例如“gcc14”）来使用特定版本的 GCC；否则使用默认版本的 GCC。

**`TARGETS`** 仅构建列出的目标，而非每个支持的架构。

**`EXTRA_TARGETS`** 除支持的架构外，还构建半支持架构。半支持架构在 FreeBSD 树中有构建支持，但测试要少得多，通常用于没有广泛吸引力的边缘用途。

## 文件

**`/usr/doc/Makefile`**
**`/usr/doc/share/mk/doc.project.mk`**
**`/usr/ports/Mk/bsd.port.mk`**
**`/usr/ports/Mk/bsd.sites.mk`**
**`/usr/src/Makefile`**
**`/usr/src/Makefile.inc1`** 每个树的 [make(1)](../man1/make.1.md) 基础设施
**`/usr/ports/UPDATING`**
**`/usr/src/UPDATING`** 每个树的显著变更
**`/usr/share/examples/etc/make.conf`** [make.conf(5)](../man5/make.conf.5.md) 示例
**`/etc/src.conf`** src 构建配置，参见 [src.conf(5)](../man5/src.conf.5.md)

## 实例

本节描述常见情况的最佳实践。需要手动干预时，将在 `UPDATING` 中提及。确保在继续之前有完整备份！

### 实例 1：就地构建和升级系统

如果使用已安装的驱动程序（如图形或虚拟机客户机驱动程序），检出 [ports(7)](ports.7.md) 树，并在 [src.conf(5)](../man5/src.conf.5.md) 中指定驱动程序，使其在内核之后自动构建和安装：

```sh
git clone https://git.FreeBSD.org/ports.git /usr/ports
cat << EOF >> /etc/src.conf
PORTS_MODULES+=graphics/drm-kmod emulators/virtualbox-ose-kmod
EOF
```

检出 CURRENT 分支，构建并安装，覆盖当前系统：

```sh
git clone https://git.FreeBSD.org/src.git /usr/src
cd /usr/src
make buildworld buildkernel
make installkernel
shutdown -r now
```

对于主版本升级，引导进入单用户模式。重启后，安装用户空间并合并配置。验证不需要后，删除旧文件：

```sh
cd /usr/src
etcupdate -p
make installworld
etcupdate
make delete-old
shutdown -r now
```

测试新系统并验证应用程序不依赖它们后，删除旧库：

```sh
make delete-old-libs
```

### 实例 2：构建和升级自定义内核

通过包含现有配置并使用 `device`/`nodevice` 和 `options`/`nooption` 选择和配置组件，创建自定义内核配置 `MYKERNEL`：

```sh
cd /usr/src
cat << EOF > sys/amd64/conf/MYKERNEL
include GENERIC
ident MYKERNEL
nodevice sound
EOF
```

创建新内核配置后，构建新工具链，构建内核并直接安装，将旧内核移动到 `/boot/kernel.old/`：

```sh
make kernel-toolchain
make -DALWAYS_CHECK_MAKE buildkernel KERNCONF=MYKERNEL
make -DALWAYS_CHECK_MAKE installkernel KERNCONF=MYKERNEL
shutdown -r now
```

要将内核打包为 [freebsd-base(7)](freebsd-base.7.md) 包而非直接安装，使用 `update-packages` 而非 `installkernel`：

```sh
make buildworld buildkernel KERNCONF=MYKERNEL
make update-packages KERNCONF=MYKERNEL
```

要将内核直接安装到备用位置，使用 `INSTKERNNAME` 变量并通过 nextboot(8) 引导一次以测试：

```sh
make installkernel KERNCONF=MYKERNEL INSTKERNNAME=testkernel
nextboot -k testkernel
shutdown -r now
```

### 实例 3：构建和升级单个用户空间组件

重新构建并重新安装单个用户空间组件，本例中为 [ls(1)](../man1/ls.1.md)：

```sh
cd /usr/src/bin/ls
make clean all
make install
```

### 实例 4：构建和升级可加载内核模块

重新构建并重新安装单个可加载内核模块，本例中为 sound(4)：

```sh
cd /usr/src/sys/modules/sound
make all install clean cleandepend KMODDIR=/boot/kernel
```

重要细节是内核二进制接口受其配置影响。在常规内核构建流程之外构建的模块仍必须针对目标内核配置构建，该配置由 [config(8)](../man8/config.8.md) 生成的 `opt_*.h` 头文件集合定义。使用 `KERNBUILDDIR` 变量将模块构建指向已配置的内核。无需在该目录中实际构建已配置的内核，模块构建仅消耗其中的头文件。

此外，`SYSDIR` 环境变量可用于指向用于构建目标内核的特定内核源代码树，因为内核头文件定义模块的二进制接口。

假设 FreeBSD 源代码位于 `/home/user/src` 目录，使用的内核配置名为 Vd MY_KERNEL，模块源代码在 `my-module` 目录中，以下命令序列将用 `opt_*.h` 头文件填充 `/home/user/my-kernel-builddir` 目录，然后构建与 Vd MY_KERNEL 兼容的模块。

```sh
config -d /home/user/my-kernel-builddir -s /home/user/src/sys/amd64/conf MY-KERNEL
cd my-module
make all KERNBUILDDIR=/home/user/my-kernel-builddir SYSDIR
```

### 实例 5：就地快速重建内核

快速重建并重新安装内核，仅重新编译自上次构建以来更改的文件；注意这仅在之前已完成完整内核构建时有效，不适用于全新源代码树：

```sh
cd /usr/src
make kernel KERNFAST=1
```

### 实例 6：为不同架构交叉编译

要为另一 CPU 架构重建 FreeBSD 的部分内容，首先通过构建交叉工具链准备源代码树：

```sh
cd src
make toolchain TARGET_ARCH=aarch64
```

以下命令序列可在不同主机架构（如 amd64）上交叉构建 arm64（aarch64）架构的系统：

```sh
cd /usr/src
make TARGET_ARCH=aarch64 buildworld buildkernel
make TARGET_ARCH=aarch64 DESTDIR=/client installworld installkernel
```

之后，要构建和安装单个用户空间组件，使用：

```sh
cd src/bin/ls
make buildenv TARGET_ARCH=aarch64
make clean all install DESTDIR=/client
```

同样，要快速重建并重新安装内核，使用：

```sh
cd src
make buildenv TARGET_ARCH=aarch64
make kernel KERNFAST=1 DESTDIR=/client
```

## 诊断

- Bad system call (core dumped)
- rescue/sh check failed, installation aborted 内核由于构建过程不正确而未更新。研究上述示例。

## 参见

[cc(1)](../man1/clang.1.md), install(1), [make(1)](../man1/make.1.md), [make.conf(5)](../man5/make.conf.5.md), [src.conf(5)](../man5/src.conf.5.md), [arch(7)](arch.7.md), [development(7)](development.7.md), [freebsd-base(7)](freebsd-base.7.md), pkg(7), [ports(7)](ports.7.md), [release(7)](release.7.md), [tests(7)](tests.7.md), [config(8)](../man8/config.8.md), etcupdate(8), nextboot(8), pkg-repo(8), [shutdown(8)](../man8/shutdown.8.md)

## 历史

`uname` 手册页首次出现于 FreeBSD 4.3。

## 作者

Mike W. Meyer <mwm@mired.org>

## 注意事项

旧对象可能导致模糊的构建问题；尝试 `make cleandir cleandir`。

环境污染可能导致模糊的构建问题；尝试在 [make(1)](../man1/make.1.md) 命令前加 `env -i`

进行主版本升级时，需要引导进入单用户模式执行 `installworld`。

更新引导 [loader(8)](../man8/loader.8.md) 因架构而异。有关你的架构的更多细节，请查阅 [boot(8)](../man8/boot_i386.8.md)。
