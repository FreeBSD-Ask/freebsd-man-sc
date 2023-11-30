  LOADER.4TH(8)  

LOADER.4TH(8)

FreeBSD System Manager's Manual

LOADER.4TH(8)

[名称](#__u540D___u79F0_)
=======================

`loader.4th` —

loader.conf 处理工具

[描述](#__u63CF___u8FF0_)
=======================

名为 `loader.4th` 的文件是一组旨在操作 loader.conf(5) 文件的命令。 默认的 /boot/loader.rc 包括 `loader.4th` 并使用它的命令之一来自动读取和处理标准 loader.conf(5) 文件。 存在其他命令来帮助用户指定替代配置。

`loader.4th` 本身的命令对于大多数用途来说是不够的。 请参阅下面的示例了解最常见的情况，并参阅 loader(8) 了解其他命令。

在使用 `loader.4th` 中提供的任何命令之前，必须通过命令包含它：

`include loader.4th`

此行存在于默认的 /boot/loader.rc 文件中，因此在正常设置中不需要（也不应该重新发布）。

它提供的命令是：

[`boot`](#boot)

[`boot`](#boot_2) kernelname \[`...`\]

[`boot`](#boot_3) directory \[`...`\]

[`boot`](#boot_4) `-flag` `...`

由读取的 loader.conf(5) 文件指定引导。

根据传递的参数，它可以覆盖引导标志以及内核名称或内核和模块的搜索路径。

[`boot-conf`](#boot-conf)

[`boot-conf`](#boot-conf_2) kernelname \[`...`\]

[`boot-conf`](#boot-conf_3) directory \[`...`\]

[`boot-conf`](#boot-conf_4) `-flag` `...`

与上述 `boot` 类似，但不是立即启动，而是使用 `autoboot` ，因此可以停止。

[`start`](#start)

读取 /boot/defaults/loader.conf, ，其中指定的所有其他 loader.conf(5) 文件，然后加载所需的内核和模块 (如果尚未加载) 。 之后，您可以使用 `boot` 或 `autoboot` 命令或直接退出（前提是 autoboot\_delay 未设置为 NO）来引导系统。 `start` 是默认 /boot/loader.rc 文件中使用的命令（参见 (see loader(8)) ）。

[`initialize`](#initialize)

初始化支持库，以便可以在不先执行 `start` 的情况下使用命令。 与 `start` 一样，它读取 /boot/defaults/loader.conf 和其中指定的所有其他 loader.conf(5) 文件 (但不加载内核或模块) 。 返回堆栈上的标志以指示是否成功加载了任何配置文件。

[`read-conf`](#read-conf) filename

读取并处理 loader.conf(5) 文件。 不继续引导。

[`enable-module`](#enable-module) module

启用 module 的加载。

[`disable-module`](#disable-module) module

禁用 module 的加载。

[`toggle-module`](#toggle-module) module

打开和关闭 module 的加载。

[`show-module`](#show-module) module

显示在 loader.conf(5) 文件中收集的有关模块 module 的信息。

[`retry`](#retry)

在 loader.conf(5) 文件中使用以指定模块加载失败后的操作。

[`ignore`](#ignore)

在 loader.conf(5) 文件中使用以指定模块加载失败后的操作。

[`try-include`](#try-include) file \[file ...\]

处理脚本文件（如果存在）。 反过来，每个文件都被完全读入内存，然后它的每一行都被传递给命令行解释器。 如果解释器返回任何错误，try-include 命令会立即中止，不读取任何其他文件，并静默返回而不会出现错误。

[文件](#__u6587___u4EF6_)
=======================

/boot/loader

loader(8) 。

/boot/loader.4th

`loader.4th` 本身。

/boot/loader.rc

loader(8) 引导脚本。

/boot/defaults/loader.conf

由 `start` 命令加载的文件。

[实例](#__u5B9E___u4F8B_)
=======================

标准 /boot/loader.rc:

include /boot/loader.4th start 

使用标准配置加载不同的内核：

set kernel="kernel.old" unload boot-conf 

读取额外的配置文件，然后继续引导：

unload read-conf /boot/special.conf boot-conf 

禁用启动屏幕模块和位图的加载，然后继续启动：

unload disable-module splash\_bmp disable-module bitmap boot-conf 

[参见](#__u53C2___u89C1_)
=======================

loader.conf(5), loader(8)

[历史](#__u5386___u53F2_)
=======================

`loader.4th` 指令集最早出现在 FreeBSD 3.2 中。

[作者](#__u4F5C___u8005_)
=======================

`loader.4th` 命令集由 Daniel C. Sobral ⟨dcs@FreeBSD.org⟩ 编写。

[缺陷](#__u7F3A___u9677_)
=======================

英国间谍系列。

November 13, 2013

FreeBSD 13.1-RELEASE