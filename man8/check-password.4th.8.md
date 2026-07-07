# check-password.4th(8)

`check-password.4th` — FreeBSD 密码检查引导模块

## 名称

`check-password.4th`

## 描述

名为 `check-password.4th` 的文件是一组命令，旨在执行以下一项或多项功能：

- 防止在无密码情况下引导
- 防止在无密码情况下修改引导选项
- 提供密码以挂载 geli(8) 加密的根磁盘

`check-password.4th` 的命令本身对大多数用途来说是不够的。请参阅下文示例了解最常见的情况，并参阅 [loader(8)](loader.8.md) 了解其他命令。

在使用 `check-password.4th` 提供的任何命令之前，必须通过以下命令将其包含进来：

```sh
include check-password.4th
```

此行已存在于 **/boot/loader.4th** 文件中，因此在正常设置中不需要（且不应重新发出）。

它提供的命令有：

**`check-password`** 多功能函数，可保护交互式引导菜单、防止在无密码情况下引导，或提示输入 geli(8) 密码短语（取决于 loader.conf(5) 设置）。首先检查 `bootlock_password`，如果已设置，用户必须输入正确密码才能继续。接着检查 `geom_eli_passphrase_prompt`，如果设置为 `YES`（不区分大小写），则提示用户输入其 GELI 密码，以便在引导期间稍后挂载根设备。最后检查 `password`，如果已设置，则尝试 `autoboot`，仅在失败或用户中断时才提示输入密码。更多信息请参见 loader.conf(5)。

影响其行为的环境变量有：

**`bootlock_password`** 设置 bootlock 密码（最长 255 个字符），`check-password` 要求在系统允许引导之前输入此密码。

**`geom_eli_passphrase_prompt`** 选择 loader(8) 是否提示输入 GELI 凭据，将其传递给内核以便稍后挂载 geli(8) 加密的根设备。

**`password`** 设置密码（最长 255 个字符），`check-password` 要求用户在访问引导菜单之前输入此密码。

## 文件

**/boot/loader** [loader(8)](loader.8.md)。

**/boot/check-password.4th** `check-password.4th` 本身。

**/boot/loader.rc** [loader(8)](loader.8.md) 引导脚本。

## 实例

标准 i386 **/boot/loader.rc**：

```sh
include /boot/loader.4th
check-password
```

在 loader.conf(5) 中设置密码以防止修改引导选项：

```sh
password="abc123"
```

在 loader.conf(5) 中设置密码以防止在无密码情况下引导：

```sh
bootlock_password="boot"
```

在 loader.conf(5) 中添加以下内容，以在引导时生成提示，收集 GELI 凭据用于挂载 geli(8) 加密的根设备：

```sh
geom_eli_passphrase_prompt="YES"
```

## 参见

loader.conf(5), [loader(8)](loader.8.md), [loader.4th(8)](loader.4th.8.md)

## 历史

`check-password.4th` 命令集首次出现于 FreeBSD 9.0。

## 作者

`check-password.4th` 命令集由 Devin Teske <dteske@FreeBSD.org> 编写。
