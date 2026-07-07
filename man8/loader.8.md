# loader(8)

`loader` — 内核引导的最终阶段

## 名称

`loader`

## 描述

名为 `loader` 的程序是 FreeBSD 内核引导过程的最终阶段。它负责将内核、内核模块和其他文件载入内存。它创建一组类似 [sh(1)](../man1/sh.1.md) 的环境变量并传递给内核。它执行以多种解释器之一编写的引导脚本。它与脚本一起控制引导过程以及与用户的交互。

它提供了一种脚本语言，可用于自动化任务、进行预配置或协助恢复操作。此脚本语言大致分为两个主要组件。较小的一组是专为普通用户直接使用而设计的命令集合，出于历史原因称为“内建命令”。这些命令的主要驱动力是用户友好性。较大的组件是内置于引导加载器中的脚本语言。FreeBSD 提供三种不同的解释器：Forth、Lua 和 Simple。Forth 加载器基于由 John Sadler 编写的 FICL，这是一个与 ANS Forth 兼容的 Forth 解释器。Lua 加载器是来自 `https://www.lua.org/` 的完整 Lua 解释器。Simple 加载器仅解释一系列内建命令，不包含任何控制结构。

在初始化期间，`loader` 会探测控制台并设置 `console` 变量，或者如果前一引导阶段使用了串口控制台，则将其设置为串口控制台（“`comconsole`”）。如果选择了多个控制台，它们将以空格分隔列出。然后，探测设备，设置 `currdev` 和 `loaddev`，并将 `LINES` 设置为 24。最后，将执行特定于解释器的文件。

## 内建命令

所有解释器通用的命令在 loader_simp(8) 的“内建命令”章节中描述。

以下命令仅在 loader_lua(8) 和 loader_4th(8) 中可用：

**`be-list`** 列出 `loader` 可见的引导环境。列出的名称可直接与 `be-switch` 一起使用。

**`be-switch`** `beName` 切换到 `beName` 引导环境。`loader` 配置将从新的根目录重新加载，并且任何先前加载的内核和模块将立即被卸载。

**`boot-conf`** 加载 `loader` 配置并启动自动引导序列。

**`read-conf`** `file` 加载指定的配置文件。

**`reload-conf`** 还原所有先前应用的设置，并重新加载配置。在命令行中执行的、用于覆盖先前由 loader.conf(5) 配置 `set` 的变量的命令也将被还原，同时还原任何已切换的模块选项。

**`enable-module`** `kmod-name`
**`disable-module`** `kmod-name`
**`toggle-module`** `kmod-name` 启用、禁用或切换名为“`kmod-name`”的内核模块的加载。

**`show-module-options`** 描述 `loader` 已知的所有模块，并显示它们是否已启用。

以下命令仅在 loader_lua(8) 中可用：

**`disable-device`** `device` 设置 newbus 提示以禁用 `device`。

### 内建环境变量

所有解释器通用的环境变量在 loader_simp(8) 的“内建环境变量”章节中描述。

## 参见

libsa(3), loader.conf(5), [tuning(7)](../man7/tuning.7.md), [boot(8)](boot_i386.8.md), btxld(8), [loader.efi(8)](loader.efi.8.md), loader_4th(8), loader_lua(8), loader_simp(8)

## 历史

`loader` 首次出现于 FreeBSD 3.1。`loader` 脚本语言在 FreeBSD 12.0 中默认更改为 Lua。

## 作者

`loader` 由 Michael Smith <msmith@FreeBSD.org> 编写。

FICL 由 John Sadler <john_sadler@alum.mit.edu> 编写。

Warner Losh <imp@FreeBSD.org> 基于 Pedro Souza 为 2014 年 Google 夏季代码节所做的初始工作，将 Lua 集成到源码树中。
