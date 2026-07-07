# beastie.4th(8)

`beastie.4th` — FreeBSD ASCII 字符画引导模块

## 名称

`beastie.4th`

## 描述

名为 `beastie.4th` 的文件是一组命令集合，用于在引导加载器菜单右侧绘制 ASCII 字符画形式的 FreeBSD 吉祥物——简称为 *beastie*。单凭 `beastie.4th` 提供的命令在大多数情况下并不够用。请参考下文示例中的常见场景，并参阅 [loader(8)](loader.8.md) 了解其他可用命令。

在使用 `beastie.4th` 提供的任何命令之前，必须先通过以下命令将其引入：

```sh
include beastie.4th
```

该行已包含在默认的 **/boot/loader.rc** 文件中，因此在正常配置下无需再次执行。

其提供的命令如下：

**`draw-beastie`** 绘制 FreeBSD 徽标。绘制的徽标通过在 loader.conf(5) 中设置 `loader_logo` 变量来配置，可选值为 `beastie`、`beastiebw`、`fbsdbw`、`orb` 和 `orbbw`（默认值）。徽标的位置可通过在 loader.conf(5) 中设置 `loader_logo_x` 和 `loader_logo_y` 变量来配置。默认值为 46（x）和 4（y）。

**`clear-beastie`** 清除屏幕上的 beastie 图案。

**`beastie-start`** 初始化交互式引导加载器菜单。可在 loader.conf(5) 中配置 `loader_delay` 变量，以指定延迟加载引导菜单的秒数。在延迟期间，用户可以按 Ctrl-C 退回到 `autoboot`，或按 ENTER 继续。默认行为是不延迟。

影响其行为的变量如下：

**`loader_logo`** 选择 beastie 引导菜单中所需的徽标。可取值为：`fbsdbw`、`beastie`、`beastiebw`、`orb`、`orbbw`（默认）和 `none`。

**`loader_logo_x`** 设置徽标的列位置。默认为 46。

**`loader_logo_y`** 设置徽标的行位置。默认为 4。

**`beastie_disable`** 若设置为 “YES”，将跳过 beastie 引导菜单。在非 x86 硬件上运行时，始终跳过 beastie 引导菜单。

**`loader_delay`** 若设置为大于零的数值，将在启动 beastie 引导菜单前引入一段延迟。在延迟期间，用户可以按 Ctrl-C 跳过菜单，或按 ENTER 进入菜单。默认在加载菜单时不延迟。

## 文件

**/boot/loader** [loader(8)](loader.8.md)。
**/boot/beastie.4th** `beastie.4th` 本身。
**/boot/loader.rc** [loader(8)](loader.8.md) 的引导脚本。

## 实例

标准 i386 **/boot/loader.rc**：

```sh
include /boot/beastie.4th
beastie-start
```

在 loader.conf(5) 中设置不同的徽标：

```sh
loader_logo="beastie"
```

## 参见

loader.conf(5), [loader(8)](loader.8.md), [loader.4th(8)](loader.4th.8.md)

## 历史

`beastie.4th` 命令集首次出现在 FreeBSD 5.1 中。

## 作者

`beastie.4th` 命令集由 Scott Long <scottl@FreeBSD.org>、Aleksander Fafula <alex@fafula.com> 和 Devin Teske <dteske@FreeBSD.org> 编写。
