# loader.4th.8

`loader.4th` — loader.conf 处理工具

## 名称

`loader.4th`

## 描述

名为 `loader.4th` 的文件是一组用于处理 loader.conf(5) 文件的命令集合。默认的 **/boot/loader.rc** 包含 `loader.4th` 并使用其中一条命令来自动读取和处理标准的 loader.conf(5) 文件。其他命令可帮助用户指定替代配置。

单凭 `loader.4th` 提供的命令在大多数情况下并不够用。请参考下文示例中的常见场景，并参阅 [loader(8)](loader.8.md) 了解其他可用命令。

在使用 `loader.4th` 提供的任何命令之前，必须先通过以下命令将其引入：

```sh
include loader.4th
```

该行已包含在默认的 **/boot/loader.rc** 文件中，因此在正常配置下无需（也不应）再次执行。

其提供的命令如下：

**`boot`**
**`boot`** `kernelname` [`...`]
**`boot`** `directory` [`...`]
**`boot`** `-flag` `...` 按所读取的 loader.conf(5) 文件中的指定进行引导。

根据传递的参数，它可以覆盖引导标志以及内核名称或内核和模块的搜索路径。

**`boot-conf`**
**`boot-conf`** `kernelname` [`...`]
**`boot-conf`** `directory` [`...`]
**`boot-conf`** `-flag` `...` 工作方式类似于上文描述的 `boot`，但不是立即引导，而是使用 `autoboot`，因此可以被中断。

**`start`** 读取 **/boot/defaults/loader.conf** 及其中指定的所有其他 loader.conf(5) 文件，然后加载所需的内核和模块（如果尚未加载）。之后你可以使用 `boot` 或 `autoboot` 命令，或直接退出（前提是 `autoboot_delay` 未设置为 NO）来引导系统。`start` 是默认 **/boot/loader.rc** 文件中使用的命令（参见 [loader(8)](loader.8.md)）。

**`initialize`** 初始化支持库，使命令无需先执行 `start` 即可使用。与 `start` 一样，它会读取 **/boot/defaults/loader.conf** 及其中指定的所有其他 loader.conf(5) 文件（但不会加载内核或模块）。在栈上返回一个标志以指示是否成功加载了任何配置文件。

**`read-conf`** `filename` 读取并处理一个 loader.conf(5) 文件。不会继续引导。

**`enable-module`** `module` 启用 `module` 的加载。

**`disable-module`** `module` 禁用 `module` 的加载。

**`toggle-module`** `module` 切换 `module` 的加载状态（开启或关闭）。

**`show-module`** `module` 显示在 loader.conf(5) 文件中收集的关于模块 `module` 的信息。

**`retry`** 在 loader.conf(5) 文件内部使用，用于指定模块加载失败后的动作。

**`ignore`** 在 loader.conf(5) 文件内部使用，用于指定模块加载失败后的动作。

**`try-include`** `file` [`file`] 如果脚本文件存在则处理它们。每个文件依次被完整读入内存，然后将其每一行传递给命令行解释器。如果解释器返回任何错误，try-include 命令会立即中止，不再读取任何其他文件，并静默返回而不报错。

## 文件

**/boot/loader** [loader(8)](loader.8.md)。
**/boot/loader.4th** `loader.4th` 本身。
**/boot/loader.rc** [loader(8)](loader.8.md) 的引导脚本。
**/boot/defaults/loader.conf** 由 `start` 命令加载的文件。

## 实例

标准的 **/boot/loader.rc**：

```sh
include /boot/loader.4th
start
```

使用标准配置加载不同的内核：

```sh
set kernel="kernel.old"
unload
boot-conf
```

读取额外的配置文件然后继续引导：

```sh
unload
read-conf /boot/special.conf
boot-conf
```

禁用启动画面模块和位图的加载，然后继续引导：

```sh
unload
disable-module splash_bmp
disable-module bitmap
boot-conf
```

## 参见

loader.conf(5), [loader(8)](loader.8.md)

## 历史

`loader.4th` 命令集首次出现于 FreeBSD 3.2。

## 作者

`loader.4th` 命令集由 Daniel C. Sobral <dcs@FreeBSD.org> 编写。

## 缺陷

一部英国间谍剧。
