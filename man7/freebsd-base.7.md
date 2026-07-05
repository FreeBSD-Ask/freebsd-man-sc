# freebsd-base.7

`freebsd-base` — 基本系统软件包

## 名称

`freebsd-base`

## 描述

FreeBSD 基本系统可作为一组 [pkg(8)](../man8/pkg.8.md) 软件包安装，这取代了使用 [tar(1)](../man1/tar.1.md) 归档进行安装的传统方法。

所有基本软件包的名称都以字符串“FreeBSD-”开头，并且其 origin 以“base/”开头。在默认系统配置中，包含这些软件包的仓库称为“FreeBSD-base”，但可以使用任何名称。该仓库名称可与 [pkg(8)](../man8/pkg.8.md) 一起使用，以将软件包操作限制在基本系统软件包范围内。

所有受支持的 FreeBSD 发行版以及活动的“STABLE”和“CURRENT”分支的软件包都托管在 Internet 上的 <https://pkg.freebsd.org>。当新的勘误或安全更新发布时（针对受支持的发行版本），或对开发分支每天更新两次时，这些软件包都会更新。

或者，可以按照 [build(7)](build.7.md) 中的说明，从系统源代码树构建软件包，从而允许使用软件包从源代码更新系统。

## 软件包组织

为了允许对已安装系统进行自定义，每个软件包都被拆分为多个子软件包，其中包含该软件包的不同组件。对于软件包 **FreeBSD-foo,** 可能提供以下子软件包：

**软件包名** **描述**
**FreeBSD-foo** 软件包的基础文件（通常是可执行文件）
**FreeBSD-foo-lib** 原生运行时库
**FreeBSD-foo-lib32** 32 位兼容运行时库
**FreeBSD-foo-dev** 开发文件（头文件和静态库）
**FreeBSD-foo-dev-lib32** 32 位开发文件
**FreeBSD-foo-dbg** 调试符号
**FreeBSD-foo-man** 手册页。仅当构建系统时启用了 **WITH_MANSPLITPKG** [src.conf(5)](../man5/src.conf.5.md) 选项时，手册页才会单独打包，这不是默认设置。

可用的子软件包的确切集合因每个软件包而异。例如，某些软件包可能不提供任何开发文件，在这种情况下不存在 **-dev** 子软件包。

## 软件包集

软件包集是元软件包，它们本身不包含任何文件，但依赖于其他软件包的选择，使得每个软件包集允许安装支持特定工作负载的完整软件包集合。

软件包集以名为 **FreeBSD-set-<name>** 的软件包形式提供。基本系统中提供以下软件包集：

**minimal** 启动多用户 FreeBSD 系统所需的最小软件包集合。这包括核心系统，以及硬件支持所需的软件包（如 [devmatch(8)](../man8/devmatch.8.md) 和可下载的固件），还有基本网络功能，包括 DHCP 和 IEEE Std 802.11™ 无线网络。

**minimal-jail** 等同于在 [jail(8)](../man8/jail.8.md) 环境中运行的系统的 **minimal**。此集合排除了 jail 通常不需要的硬件支持。

**devel** 开发工具，包括 C/C++ 编译器、链接加载器，以及其他工具如 [ar(1)](../man1/ar.1.md) 和 nm(1)。此集合还包括所有软件包的原生开发文件（头文件和静态库）。

**optional** 不属于 **devel** 或 **minimal** 集的可选软件。

**optional-jail** 等同于在 [jail(8)](../man8/jail.8.md) 环境中运行的系统的 **optional**。此集合排除了在 jail 中通常无法工作或无用的系统功能。

**lib32** 32 位兼容库，用于在 64 位主机系统上运行 32 位应用程序。此集合既包括运行时库，也包括开发文件。

**base** 完整的基本系统，不包括测试、系统源代码和调试符号。安装 **base** 集等同于安装 **minimal,** **devel** 和 **optional**。

**base-jail** 等同于在 [jail(8)](../man8/jail.8.md) 环境中运行的系统的 **base**。此集合排除了在 jail 中通常无法工作或无用的系统功能。安装 **base-jail** 集等同于安装 **minimal-jail,** **devel** 和 **optional-jail**。

**src** 用户空间和内核的系统源代码树，安装在 **/usr/src**。

**tests** 系统测试套件，安装在 **/usr/tests**。

**kernels** 所有可用的系统内核。

## 实例

### 安装单个用户空间组件

在运行中的系统上安装 [vi(1)](../man1/vi.1.md) 文本编辑器：

```sh
pkg install FreeBSD-vi
```

### 向 jail 安装用户空间

使用 **minimal-jail** 软件包集安装一个新的 [jail(8)](../man8/jail.8.md) 系统：

```sh
pkg -r /jails/myjail install FreeBSD-set-minimal-jail
```

### 安装原生编译器

在运行中的系统上安装 C/C++ 编译器：

```sh
pkg install FreeBSD-set-devel
```

### 更新当前运行的系统

将可用更新应用到运行中的系统：

```sh
pkg upgrade -r FreeBSD-base
```

### 安装交叉编译器

在备用根目录中安装 FreeBSD/powerpc64le 的开发工具链（例如，用于支持为与主机系统不同的目标进行交叉编译软件）：

```sh
pkg -r /ppcdev -oABI=FreeBSD:16:powerpc64le e
    install FreeBSD-set-devel
```

### 添加本地构建的快照仓库

禁用预定义的仓库，并为本地构建的基本系统软件包添加一个本地仓库：

```sh
cat << EOF > /usr/local/etc/pkg/repos/FreeBSD.conf
FreeBSD-base: { enabled: no }
FreeBSD-local: {
	url: "file:///usr/obj/usr/src/repo/${ABI}/latest",
	enabled: yes
}
EOF
```

这些软件包由 [build(7)](build.7.md) 系统在 `${REPODIR}/${PKG_ABI}/<VERSION>` 中创建，默认为示例目录。

**注意：** 该仓库必须具有与预定义仓库不同的名称。

### 注销当前运行的系统

通过 [pkg(8)](../man8/pkg.8.md) 管理的系统可以从软件包管理器中注销——例如，通过“make installworld”进行就地升级。参见 [build(7)](build.7.md)。

要从软件包管理器中注销基本系统：

```sh
pkg unregister -fg 'FreeBSD-e*'
```

然后，禁用基本系统软件包仓库。如果曾在 **/usr/local/etc/pkg/repos/** 中创建配置文件以启用基本系统软件包，请将其移除：

```sh
rm /usr/local/etc/pkg/repos/FreeBSD-base.conf
```

或者，如果希望保留它，请编辑该文件并将“`enabled:`”更改为“`no`”以禁用该条目。

**警告：** 这是一个破坏性操作，将阻止通过 [pkg(8)](../man8/pkg.8.md) 更新基本系统。

## 参见

[build(7)](build.7.md), [pkg(8)](../man8/pkg.8.md), [src.conf(5)](../man5/src.conf.5.md)

## 历史

将基本系统作为软件包安装的支持是在 FreeBSD 15.0 中引入的。早期版本支持此功能的一部分。对注销现有安装的支持出现在 pkg 2.5 中。

## 注意事项

从 RELEASE 升级到 STABLE 或 CURRENT 分支需要“`pkg upgrade -f`”。
