# pkg.8

`pkg` — 用于操作软件包的工具

## 名称

`pkg`

## 概要

`pkg [-d] command ...` `pkg [-d] add [-fy] [-r reponame] pkg.pkg` `pkg -N` `pkg [-46d] bootstrap [-fy] [-r reponame]`

## 描述

`pkg` 是软件包管理工具。它用于管理从 [ports(7)](../man7/ports.7.md) 安装的本地软件包，以及从远程仓库安装/升级软件包。

为避免向后兼容性问题，实际的 [pkg(8)](pkg.8.md) 工具并未安装在基本系统中。首次调用时，`pkg` 将从远程仓库引导安装真正的 [pkg(8)](pkg.8.md)。

**`pkg`** `command ...` 如果尚未安装 [pkg(8)](pkg.8.md)，将获取它、验证其签名、安装，然后将原始命令转发给它。如果已安装，则将所请求的命令转发给真正的 [pkg(8)](pkg.8.md)。

**`pkg`** `add` [`-fy`] [`-r` `reponame`] `pkg.pkg` 从本地软件包安装 [pkg(8)](pkg.8.md)，而非从远程获取。如果启用了签名检查，则必须存在正确的签名文件且签名有效，软件包才会被安装。如果指定了 `-f` 标志，则无论是否已安装 [pkg(8)](pkg.8.md)，都将安装。如果指定了 `-y` 标志，引导安装 [pkg(8)](pkg.8.md) 时将不询问确认。如果指定了 `reponame`，则使用该仓库的签名配置。

**`pkg`** `-N` 不进行引导安装，仅确定是否实际安装了 [pkg(8)](pkg.8.md)。如果已安装，返回 0 和已安装的软件包数量，否则返回 1。

**`pkg`** [`-46`] `bootstrap` [`-fy`] [`-r` `reponame`] 尝试引导安装，并在安装完成后不向 [pkg(8)](pkg.8.md) 转发任何内容。使用 `-4` 和 `-6` 时，`pkg` 将分别强制使用 IPv4 或 IPv6 来获取 [pkg(8)](pkg.8.md) 及其签名（按需）。如果指定了 `-f` 标志，则无论是否已安装 [pkg(8)](pkg.8.md)，都将获取并安装。如果指定了 `-y` 标志，引导安装 [pkg(8)](pkg.8.md) 时将不询问确认。如果指定了 `reponame`，则使用该仓库的配置。

## 选项

`pkg` 支持以下选项：

**`-d,`** `--debug` 显示调试信息。可以多次指定以提高详细程度。指定两次时，将启用 fetch(3) 调试输出。

## 配置

配置因位于仓库配置文件还是全局配置文件而异。FreeBSD 的默认仓库配置存储在 **/etc/pkg/FreeBSD.conf** 中，其他仓库配置文件将在 `REPOS_DIR` 中搜索，如果未设置则为 **/usr/local/etc/pkg/repos**。

对于引导安装，`pkg` 将处理它找到的所有仓库，并默认使用最后启用的仓库。

仓库配置以以下格式存储：

```sh
FreeBSD: {
  url: "pkg+http://pkg.FreeBSD.org/${ABI}/latest",
  mirror_type: "srv",
  signature_type: "none",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

**url** 参见环境变量中的 `PACKAGESITE`
**mirror_type** 参见环境变量中的 `MIRROR_TYPE`
**signature_type** 参见环境变量中的 `SIGNATURE_TYPE`
**fingerprints** 参见环境变量中的 `FINGERPRINTS`
**enabled** 定义是否应使用此仓库。有效值为 `yes`、`true`、`1`、`no`、`false`、`0`。

全局配置可以以下格式存储在 **/usr/local/etc/pkg.conf** 中：

```sh
PACKAGESITE: "pkg+http://pkg.FreeBSD.org/${ABI}/latest",
MIRROR_TYPE: "srv",
SIGNATURE_TYPE: "none",
FINGERPRINTS: "/usr/share/keys/pkg",
ASSUME_ALWAYS_YES: "yes"
REPOS_DIR: ["/etc/pkg", "/usr/local/etc/pkg/repos"]
```

每个变量参见环境变量。

## 环境变量

可以设置以下环境变量来覆盖所使用的 `pkg.conf` 文件中的设置。

**`MIRROR_TYPE`** 定义应使用哪种镜像类型。有效值为 `SRV`、`HTTP`、`NONE`。

**`ABI`** 定义要安装的软件包的 ABI。默认 ABI 由 **/bin/sh** 确定。

**`ASSUME_ALWAYS_YES`** 如果设置，引导安装 [pkg(8)](pkg.8.md) 时将不询问确认。

**`SIGNATURE_TYPE`** 如果设置为 `FINGERPRINTS`，则在引导安装 [pkg(8)](pkg.8.md) 时将要求签名并根据已知证书指纹进行验证。

**`FINGERPRINTS`** 如果 **SIGNATURE_TYPE** 设置为 `FINGERPRINTS`，此值应设置为已知指纹所在的目录路径。

**`PACKAGESITE`** 获取 [pkg(8)](pkg.8.md) 和其他软件包的 URL。

**`REPOS_DIR`** 以逗号分隔的目录列表，将在其中搜索仓库配置文件。

## 文件

配置按所列顺序从以下文件中读取。此路径可以通过设置 `REPOS_DIR` 更改。最后启用的仓库用于引导安装 [pkg(8)](pkg.8.md)。

**/usr/local/etc/pkg.conf**

**/etc/pkg/FreeBSD.conf**

**/usr/local/etc/pkg/repos/\*.conf**

## 实例

此处列出了一些示例。可用命令的完整列表在引导安装后可通过 [pkg(8)](pkg.8.md) 获得。

搜索软件包：

```sh
$ pkg search perl
```

安装软件包：

```sh
% pkg install perl
```

列出已安装的软件包：

```sh
$ pkg info
```

从远程仓库升级：

```sh
% pkg upgrade
```

列出非自动安装的软件包：

```sh
$ pkg query -e '%a = 0' %o
```

列出自动安装的软件包：

```sh
$ pkg query -e '%a = 1' %o
```

删除已安装的软件包：

```sh
% pkg delete perl
```

移除不需要的依赖项：

```sh
% pkg autoremove
```

将软件包从自动改为非自动，这将防止 pkg-autoremove(8) 将其移除：

```sh
% pkg set -A 0 perl
```

将软件包从非自动改为自动，这将使 pkg-autoremove(8) 在没有其他软件包依赖它时允许将其移除：

```sh
% pkg set -A 1 perl
```

从已安装的软件包创建软件包文件：

```sh
% pkg create -o /usr/ports/packages/All perl
```

确定哪个软件包安装了某个文件：

```sh
$ pkg which /usr/local/bin/perl
```

审计已安装软件包的安全公告：

```sh
$ pkg audit
```

检查已安装软件包的校验和不匹配：

```sh
# pkg check -s -a
```

检查缺失的依赖项：

```sh
# pkg check -d -a
```

为不同的 FreeBSD 版本获取软件包及其所有依赖项：

```sh
# pkg -o ABI=FreeBSD:15:amd64 -o IGNORE_OSVERSION=yes fetch -o destdir -d perl
```

## 参见

[ports(7)](../man7/ports.7.md), [pkg(8)](pkg.8.md)

## 历史

`pkg` 命令首次出现在 FreeBSD 9.1 中。它在 FreeBSD 10.0 中成为默认的软件包工具，替代了 pkg_install 工具套件 pkg_add(1)、pkg_info(1) 和 pkg_create(1)。
