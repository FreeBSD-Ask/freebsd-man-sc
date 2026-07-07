# ports(7)

`ports` — 第三方应用程序

## 名称

`ports`

## 描述

FreeBSD Ports Collection 提供了一种简单的方式来编译和安装第三方应用程序。它也用于构建通过 [pkg(8)](../man8/pkg.8.md) 安装的软件包。

ports 树通常位于 **/usr/ports**，由若干子目录组成，每个子目录对应一个类别；这些类别目录下又包含各个独立的 port。每个 port 都是一个目录，其中包含使原始应用程序源代码能够在 FreeBSD 上编译和运行所需的元数据和补丁。编译一个应用程序只需在 port 目录中输入“`make build`”。`Makefile` 会自动从本地磁盘或网络获取应用程序源代码，解包、应用补丁并进行编译。它还会递归处理依赖关系——即该 port 在构建和运行时所依赖的其他软件。之后，“`make install`”会安装该应用程序。

FreeBSD Ports Collection 在多个分支中维护，这些分支主要区别在于所提供软件的版本：*main* 分支包含所有最新更改，对应于 *latest* 软件包集合；而 *quarterly* 分支仅提供关键修复。可以从以下 Git 仓库克隆并更新 *main* 分支：

<https://git.FreeBSD.org/ports.git>

例如：

`git clone https://git.FreeBSD.org/ports.git`

*quarterly* 分支在 Git 中以 `yyyyQn` 形式命名，其中 *yyyy* 表示年份，*n* 表示季度（1 到 4）

`git clone -b 2021Q2 https://git.FreeBSD.org/ports.git`

通常建议使用与所使用的 [pkg(8)](../man8/pkg.8.md) 仓库相匹配的 `ports` 分支。默认情况下，对于 FreeBSD CURRENT，[pkg(8)](../man8/pkg.8.md) 配置为安装从 *main* 分支构建的软件包；而对于 FreeBSD STABLE 或 RELEASE 版本，则配置为安装从最新的 *quarterly* 分支构建的软件包。可以通过查看 `pkg -vv` 输出中的 *url* 字段来验证当前配置的 [pkg(8)](../man8/pkg.8.md) 仓库。

关于使用 ports 的更多信息，请参阅 The FreeBSD Handbook 中的“Packages and Ports”章节：

<https://docs.FreeBSD.org/en/books/handbook/ports/>

关于创建新 port 的信息，请参阅 The Porter's Handbook：

<https://docs.FreeBSD.org/en/books/porters-handbook/>

## 目标

某些 [make(1)](../man1/make.1.md) 目标会递归地在子目录中执行。这使得你可以，例如，用一条命令安装所有“`biology`”类的 ports。这类目标包括 `build , checksum , clean , configure`、`depends , extract , fetch , install` 和 `package`。

以下目标会按顺序由后继目标自动运行。也就是说，`build` 会由 `install` 在需要时运行，依此类推，一直到 `fetch`。通常，你只需使用 `install` 目标。

**`config`** 使用 portconfig(1)（`ports/ports-mgmt/portconfig`）配置该 port 的 `OPTIONS`。

**`fetch`** 从 `MASTER_SITES` 和 `PATCH_SITES` 中列出的站点获取构建该 port 所需的所有文件。参见 `FETCH_CMD , MASTER_SITE_OVERRIDE` 和 `MASTER_SITE_BACKUP`。

**`checksum`** 验证所获取的 distfile 的校验和与该 port 测试时的校验和是否匹配。如果 distfile 的校验和不匹配，它还会获取缺失或校验和计算失败的 distfile。定义 `NO_CHECKSUM` 将跳过此步骤。

**`depends`** 安装（或在只需要编译时编译）当前 port 的任何依赖项。当由 `extract` 或 `fetch` 目标调用时，这会以 `fetch-depends , build-depends` 等方式分步运行。定义 `NO_DEPENDS` 将跳过此步骤。

**`extract`** 将 distfile 解压到工作目录中。

**`patch`** 应用该 port 所需的任何补丁。

**`configure`** 配置该 port。某些 port 在此阶段会向你提问。参见 `INTERACTIVE` 和 `BATCH`。

**`build`** 构建该 port。这与调用 `all` 目标相同。

**`install`** 安装该 port 并将其注册到软件包系统中。这就是你真正需要做的全部操作。

**`install-missing-packages`** 从软件包安装缺失的依赖项，而不是构建它们。

以下目标不会在正常安装过程中运行。

```sh
cd /usr/ports && make search name=query
```

```sh
cd /usr/ports && make search name=pear- \
    xbdeps=apache
```

```sh
cd /usr/ports && make search name=pear- \
    xname='ht(tp|ml)'
```

```sh
make search key=apache display=name,path,info keylim=1
```

```sh
make search name=p5-R icase=0
```

**`showconfig`** 显示该 port 的 `OPTIONS` 配置。

**`showconfig-recursive`** 显示该 port 及其所有依赖项的 `OPTIONS` 配置。

**`rmconfig`** 删除该 port 的 `OPTIONS` 配置。

**`rmconfig-recursive`** 删除该 port 及其所有依赖项的 `OPTIONS` 配置。

**`config-conditional`** 跳过已经配置过 `OPTIONS` 的 port。

**`config-recursive`** 使用 portconfig(1)（`ports/ports-mgmt/portconfig`）配置该 port 及其所有依赖项的 `OPTIONS`。

**`fetch-list`** 显示为构建该 port（但不包括其依赖项）所需获取的文件列表。

**`fetch-recursive`** 获取该 port 及其所有依赖项的 distfile。

**`fetch-recursive-list`** 显示 `fetch-recursive` 将获取的文件列表。

**`build-depends-list , run-depends-list`** 打印该 port 的所有直接编译或运行依赖项列表。

**`all-depends-list`** 打印该 port 的所有递归依赖项列表。

**`pretty-print-build-depends-list , pretty-print-run-depends-list`** 按 port 名称和版本打印该 port 的所有递归编译或运行依赖项列表。

**`missing`** 打印该 port 待安装的缺失依赖项列表。

**`clean`** 删除已解压的源代码。除非定义了 `NOCLEANDEPENDS`，否则会递归处理依赖项。

**`distclean`** 删除该 port 的 distfile 并执行 `clean` 目标。除非定义了 `NOCLEANDEPENDS`，否则 `clean` 部分会递归处理依赖项，但 `distclean` 部分从不递归（这可能是一个 bug）。

**`reinstall`** 在你本应使用 `deinstall` 却使用了 pkg-delete(8) 之后，使用此目标恢复 port。

**`deinstall`** 从系统中删除已安装的 port，类似于 pkg-delete(8)。

**`deinstall-all`** 从系统中删除所有具有相同 `PKGORIGIN` 的已安装 port。

**`package`** 为该 port 制作二进制软件包。如果该 port 尚未安装，则会先安装。该软件包是一个 `.pkg` 文件，你可以使用 pkg-add(8) 在其他机器上安装该 port。如果 `PACKAGES` 指定的目录不存在，软件包将放在 **/usr/ports/category/port/work/pkg** 中。更多信息请参见 `PKGREPOSITORY` 和 `PKGFILE`。

**`package-recursive`** 类似于 `package`，但也会为每个依赖的 port 制作软件包。

**`package-name`** 打印该 port 的带版本号名称。

**`readmes`** 创建 port 的 `README.html`。这可以从 **/usr/ports** 调用，以创建系统中所有 port 的可浏览 Web 页面！

**`search`** 在 `INDEX` 文件中搜索由 `key`（搜索 port 名称、注释和依赖项）、`name`（仅搜索 port 名称）、`path`（搜索 port 路径）、`info`（搜索 port 信息）、`maint`（搜索 port 维护者）、`cat`（搜索 port 类别）、`bdeps`（搜索 port 编译时依赖）、`rdeps`（搜索 port 运行时依赖）、`www`（搜索 port 网站）等 [make(1)](../man1/make.1.md) 变量指定的模式，以及它们的排除对应项：`xname , xkey` 等。例如，输入：查找所有名称匹配“`query`”的 port。结果包括匹配 port 的路径、注释、维护者、编译依赖和运行依赖。查找所有名称中包含“`pear-`”且编译时依赖中不包含 apache 的 port。查找所有名称中包含“`pear-`”，但不包含“`html`”或“`http`”的 port。查找在名称、路径、信息字段中任一项包含“`apache`”的 port，忽略记录的其余部分。默认情况下，搜索不区分大小写。要使其区分大小写，可以使用 `icase` 变量：

**`quicksearch`** 简化的 `search` 输出。仅显示名称、路径和信息。

**`describe`** 为每个 port 生成一行描述，用于 `INDEX` 文件。

**`maintainer`** 显示该 port 维护者的电子邮件地址。

**`index`** 创建 **/usr/ports/INDEX**，供 `pretty-print-*` 和 `search` 目标使用。运行 `index` 目标将确保你的 `INDEX` 文件与 ports 树保持同步。

**`fetchindex`** 从 FreeBSD 集群获取 `INDEX` 文件。

## 环境变量

你可以更改所有这些变量。

**`PKGREPOSITORY`** 用于存放软件包的目录。

**`PKGFILE`** 软件包的完整路径。

```sh
.dk .sunet.se .se dk.php.net .no .de heanet.dl.sourceforge.net
```

**`PORTSDIR`** ports 树的位置。默认为 **/usr/ports**。

**`WRKDIRPREFIX`** 创建任何临时文件的位置。当 `PORTSDIR` 为只读时（例如从 CD-ROM 挂载）很有用。

**`DISTDIR`** 查找/存放 distfile 的位置，通常为 `PORTSDIR` 下的 `distfiles/`。

**`SU_CMD`** 用于提升权限以配置和安装 port 的命令。非特权用户必须对 `WRKDIRPREFIX` 和 `DISTDIR` 具有写权限。默认为 `/usr/bin/su root -c`。许多用户为方便起见将其设置为 `/usr/local/bin/sudo -E sh -c`。

**`PACKAGES`** 仅用于 `package` 目标；软件包树的基础目录，通常为 `PORTSDIR` 下的 `packages/`。如果该目录存在，软件包树将被（部分）构建。该目录不必存在；如果不存在，软件包将放在当前目录中，或者你可以定义以下之一：

**`LOCALBASE`** 已安装内容的位置，以及在解析依赖关系时搜索文件的位置（通常为 `/usr/local`）。

**`PREFIX`** 安装该 port 的位置（通常设置为与 `LOCALBASE` 相同）。

**`MASTER_SITES`** 如果本地找不到分发文件，使用的主要站点。

**`PATCH_SITES`** 如果本地找不到分发补丁文件，使用的主要位置。

**`MASTER_SITE_FREEBSD`** 如果设置，所有文件都前往 FreeBSD 主站点获取。

**`MASTER_SITE_OVERRIDE`** 所有文件和补丁首先尝试前往这些站点。

**`MASTER_SITE_BACKUP`** 所有文件和补丁最后尝试前往这些站点。

**`RANDOMIZE_MASTER_SITES`** 以随机顺序尝试下载位置。

**`MASTER_SORT`** 根据用户提供的模式对下载位置进行排序。示例：

**`MASTER_SITE_INDEX`** 从 FreeBSD 集群获取 `INDEX` 源的位置（用于 `fetchindex` 目标）。默认为 <https://download.FreeBSD.org/ports/index/>。

**`FETCHINDEX`** 获取 `INDEX` 的命令（用于 `fetchindex` 目标）。默认为“`fetch -am`”。

**`NOCLEANDEPENDS`** 如果定义，不让 `clean` 递归到依赖项。

**`FETCH_CMD`** 用于获取文件的命令。通常为 fetch(1)。

**`FORCE_PKG_REGISTER`** 如果设置，覆盖系统上任何现有的软件包注册。

**`INTERACTIVE`** 如果定义，仅当 port 需要交互时才对其进行操作。

**`BATCH`** 如果定义，仅当 port 可以 100% 自动安装时才对其进行操作。

**`DISABLE_VULNERABILITIES`** 如果定义，在安装新 port 时使用 pkg-audit(8) 禁用安全漏洞检查。

**`NO_IGNORE`** 如果定义，允许安装标记为 <`FORBIDDEN`> 的 port。Ports 框架的默认行为是在尝试安装被禁止的 port 时中止。当然，这些 port 可能无法按预期工作，但如果你确实知道自己在做什么并且确定要安装被禁止的 port，那么 `NO_IGNORE` 让你能够这样做。

**`NO_CHECKSUM`** 如果定义，跳过验证该 port 的校验和。

**`TRYBROKEN`** 如果定义，即使 port 被标记为 <`BROKEN`>，也尝试构建。

**`PORT_DBDIR`** 存储 `OPTIONS` 配置结果的目录。默认为 **/var/db/ports**。每个配置过 `OPTIONS` 的 port 都会有一个唯一命名的子目录，其中包含一个 `options` 文件。

## Make 变量

以下列表提供了构建 port 时所使用的许多变量的名称和简短说明。关于这些以及其他相关变量的更多信息，可在 `${PORTSDIR}/Mk/*` 和 FreeBSD Porter's Handbook 中找到。

**`WITH_DEBUG`**（`bool`）如果设置，为 port 二进制文件安装调试符号。

**`WITH_DEBUG_PORTS`** 用于设置 `WITH_DEBUG` 的起源列表。

**`DEBUG_FLAGS`**（默认：`-g`）当设置了 `WITH_DEBUG` 时要设置的附加 `CFLAGS`。

**`DEFAULT_VERSIONS`** 覆盖树中具有多个并发版本的 port（如数据库或编译器版本）所使用的默认变体。

**`WITH_CCACHE_BUILD`**（`bool`）如果设置，启用 ccache(1) 来构建 port。

**`CCACHE_DIR`** 用于 ccache(1) 数据的目录。

## 文件

**`ports/CHANGES`** 创建 port 前必读的重要新闻！
**`ports/CONTRIBUTING.md`** 为 ports 树做贡献的说明。
**`ports/Mk/bsd.port.mk`** ports 框架的内部工作原理。
**`ports/Tools/scripts/`** 维护 port 的工具集合。
**`ports/UPDATING`** 升级 port 前必读的重要新闻！
**`ports/distfiles/`** 存放所获取文件的目录。
**`${PORT}/Makefile`** 构建 port 的规范说明。
**`${PORT}/distinfo`** 使用 `make makesum` 生成的校验和。
**`${PORT}/files/`** 用于补丁或任何附加文件的目录。
**`${PORT}/pkg-descr`** port 的详细描述。
**`${PORT}/pkg-plist`** 该 port 安装的所有文件列表。
**`${PORT}/work/`** 该 port 的构建和暂存目录。
**`/etc/make.conf`** port 构建框架的设置。
**`/usr/ports/`** 标准 ports 树位置。
**`/var/db/ports/`** 用于存储已配置 `OPTIONS` 的目录。

## 实例

```sh
# cd /usr/ports/editors/emacs
# make install
```

```sh
# make install-missing-packages
# make install
```

```sh
# cd /usr/ports/devel/py-pip
# env FLAVOR=py37 make build
```

```sh
# 除非通过选项对话框另行配置，否则为所有 port 启用 NLS
OPTIONS_SET=		NLS
# 覆盖通过选项对话框设置的选项，为所有 port 禁用 DOCS
OPTIONS_UNSET_FORCE=	DOCS
# 为 shells/zsh port 禁用 DOCS 和 EXAMPLES
shells_zsh_UNSET=	DOCS EXAMPLES
```

```sh
# 为 lang/rust port 设置 DISABLE_MAKE_JOBS：
.if ${.CURDIR:M*/lang/rust}
DISABLE_MAKE_JOBS=	yes
TRYBROKEN=		yes
.endif
```

```sh
# 为所有 port 启用调试
WITH_DEBUG=		yes
# 为选定 port 启用调试
WITH_DEBUG_PORTS=	mail/dovecot security/krb5
```

```sh
# make WITH_DEBUG DEBUG_FLAGS="-g -O0" build
```

- 将 `DEBUG_FLAGS`（默认为 `-g`）添加到 `CFLAGS`。
- 尽量防止二进制文件被剥离（包括检查 install 目标以将 `install-strip` 替换为 `install`）。可以使用 file(1) 检查二进制文件是否已被剥离。
- 尝试启用其他调试功能，如调试构建类型或详细日志记录。但是，这是 port 特定的，ports 框架可能不了解给定软件所支持的每种调试功能。

**实例 1：** 构建和安装 Port 以下命令构建并安装 Emacs。

**实例 2：** 使用 [pkg(8)](../man8/pkg.8.md) 安装依赖项 以下示例展示如何构建和安装 port 而无需构建其依赖项。相反，依赖项通过 [pkg(8)](../man8/pkg.8.md) 下载。当依赖项在时间和资源上构建成本很高时（如 `lang/rust`），这特别有用。缺点是 [pkg(8)](../man8/pkg.8.md) 仅提供使用默认 `OPTIONS` 集合构建的软件包。

**实例 3：** 构建非默认 Flavor 的 Port 以下命令构建 port 的非默认 flavor。（此例中 `devel/py-pip` 将以 Python 3.7 支持构建。）

**实例 4：** 通过 [make.conf(5)](../man5/make.conf.5.md) 设置 Port 选项 以下各行展示了通过 [make.conf(5)](../man5/make.conf.5.md) 配置 port 选项的各种方法（作为运行“`make config`”的替代方案）：这些以及其他与选项相关的变量记录在 **/usr/ports/Mk/bsd.options.mk** 中。

**实例 5：** 设置 [make(1)](../man1/make.1.md) [make.conf(5)](../man5/make.conf.5.md) 以下示例展示如何仅为特定 port 设置任意 [make(1)](../man1/make.1.md) 变量：

**实例 6：** 调试 Port 默认情况下，port 在构建和打包时不带调试支持（例如，调试符号从二进制文件中剥离，编译时使用优化标志，详细日志记录被禁用）。port 是否以调试符号构建可以通过 [make.conf(5)](../man5/make.conf.5.md) 中的设置控制，例如：也可以在命令行上使用调试变量：有关调试变量的更多信息，请参见 MAKE VARIABLES 章节。要了解设置调试变量时所发生情况的详细信息，最好查阅位于 `${PORTSDIR}/Mk/*`（特别是 `bsd.port.mk`）的文件。如果为特定 port 启用了调试，ports 框架将：

## 参见

[make(1)](../man1/make.1.md), [make.conf(5)](../man5/make.conf.5.md), [development(7)](development.7.md), pkg(7)

附加的开发者文档：

- portlint(1)
- **/usr/ports/Mk/bsd.port.mk**

附加的用户文档：

- [pkg(8)](../man8/pkg.8.md)
- <https://ports.FreeBSD.org> 所有 port 的可搜索索引

## 历史

Ports Collection 出现于 FreeBSD 1.0。此后它传播到了 NetBSD、OpenBSD 和 macOS。

## 作者

本手册页最初由 David O'Brien 编写。

## 缺陷

Ports 文档分散在四处——**/usr/ports/Mk/bsd.port.mk**、The Porter's Handbook、The FreeBSD Handbook 的“Packages and Ports”章节以及本手册页。
