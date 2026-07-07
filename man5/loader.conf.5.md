# loader.conf(5)

`loader.conf` — 系统引导配置信息

## 名称

`loader.conf`

## 描述

文件 `loader.conf` 包含有关系统引导的描述性信息。通过它你可以指定要引导的内核、传递给内核的参数以及要加载的附加模块；并通常可以设置 [loader(8)](../man8/loader.8.md) 中描述的所有变量。

## 语法

虽然 `loader.conf` 的格式被明确定义为类似 [rc.conf(5)](rc.conf.5.md)，并且可由 [sh(1)](../man1/sh.1.md) 加载，但某些设置会以特殊方式处理。此外，某些设置的行为由设置的后缀定义；前缀标识该设置控制哪个模块。

一般解析规则如下：

- 空格和空行被忽略。
- `#` 符号会将该行的其余部分标记为注释。
- 每行只能有一个设置。

所有设置采用以下格式：

```sh
variable="value"
```

除非属于接收特殊处理的设置类别之一，否则设置将设置 [loader(8)](../man8/loader.8.md) 环境变量的值。接收特殊处理的设置列在下面。下面以“*”开头的设置定义要加载的模块，可以有任意前缀；前缀标识一个模块。所有共享公共前缀的此类设置都引用同一模块。

```sh
smbios.system.planar.maker="PLANAR_MAKER"
smbios.system.planar.product="PLANAR_PRODUCT"
smbios.system.product="PRODUCT"
uboot.m_product="M_PRODUCT"
product_vars="smbios.system.planar.maker smbios.system.planar.product smbios.system.product uboot.m_product"
```

- **/boot/loader.conf.d/PLANAR_MAKER**
- **/boot/loader.conf.d/PLANAR_PRODUCT**
- **/boot/loader.conf.d/PRODUCT**
- **/boot/loader.conf.d/M_PRODUCT**

```sh
vfs.root.mountfrom="ufs:/dev/da0s1a"
```

**`autoboot_delay`** 自动引导前的延迟（以秒为单位）。具有控制台访问权限的用户将能够在延迟期间通过在控制台上按键中断 `autoboot` 过程并转义到交互模式。如果设置为“`NO`”，则在处理 **/boot/loader.rc** 后不会自动尝试 `autoboot`，但显式的 `autoboot` 仍会正常处理，使用 10 秒延迟。如果设置为“`0`”，将不插入延迟，引导将立即进行，除非已按下按键，这可能实际上不可能。如果设置为“`-1`”，将不插入延迟，且 `loader.conf` 仅在 `autoboot` 失败时启动交互模式。与 `beastie_disable` 选项结合使用时，此选项可防止具有控制台访问权限的用户中断 `autoboot` 过程并转义到 loader 提示符。要以这种方式使用 `autoboot_delay` 选项，`beastie_disable` 必须设置为“`YES`”。

**`print_delay`** 在打印每行后添加以微秒为单位的延迟。默认为“`0`”。

**`boot_*`** 参见 [loader.efi(8)](../man8/loader.efi.8.md) 中的列表，因为这些标志适用于所有引导加载器。

**`boot_verbose`** 设置为“yes”可获得与 `boot -v` 相同的效果，或从 loader 菜单引导详细模式。参见 `kern.msgbufsize` 可调参数以确保有足够空间容纳增加的消息数量。

**`exec`** 立即执行 [loader(8)](../man8/loader.8.md) 命令。此类设置无法由 [loader(8)](../man8/loader.8.md) 以外的程序处理，因此应避免使用。它的多个实例将独立处理。

**`loader_conf_dirs`** 用于处理配置文件的目录列表（以空格分隔）。基于 lua 的 loader 将处理放置在这些目录中具有“.conf”后缀的文件。此处找到的文件在 `loader_conf_files` 中列出的文件之后但在 `local_loader_conf_files` 中找到的文件之前处理。

**`loader_conf_files`** 定义在当前文件之后立即处理的附加配置文件。`loader_conf_files` 应被视为只写。不能依赖任何保留在 loader 环境或转移到内核环境中的值。

**`local_loader_conf_files`** 以空格分隔的附加配置文件列表，最后处理，即在 `loader_conf_files` 和 `loader_conf_dirs` 处理之后。

**`product_vars`** 设置时，必须是环境变量名称的空格分隔列表，用于遍历以猜测产品信息。顺序很重要，因为读取配置文件会覆盖先前定义的值。未定义的变量将被静默忽略。当可以猜测产品信息时，对于找到的每个产品信息，将 **/boot/loader.conf.d/PRODUCT** 追加到 `loader_conf_dirs`。它通常可按以下方式使用：按以下顺序读取以下目录中找到的文件：

**`kernel`** 要加载的内核名称。如果未设置内核名称，则不会加载附加模块。该名称必须是 **/boot** 中包含内核的子目录。

**`kernel_options`** 要传递给内核的标志。

**`vfs.root.mountfrom`** 指定要挂载的根分区。例如：[loader(8)](../man8/loader.8.md) 从加载内核的分区自动从 **/etc/fstab** 计算此可调参数的值。当 **/etc/fstab** 在 [loader(8)](../man8/loader.8.md) 启动期间不可用（如从 NFS 无盘引导时），或用户希望使用不同设备时，计算值可能会错误地计算。可在 **/loader.conf** 中设置首选值。该值也可以从 [loader(8)](../man8/loader.8.md) 命令行覆盖。这在 **/etc/fstab** 损坏、丢失或从错误分区读取时的系统恢复中很有用。

**`password`** 在不中断 `autoboot` 过程的情况下用密码保护引导菜单。密码应为明文格式。如果设置了密码，则在 `autoboot_delay` 变量指定的倒计时期间按下任意键或 `autoboot` 过程失败之前，引导菜单不会出现。在两种情况下，用户都应提供指定密码才能访问引导菜单。

**`bootlock_password`** 提供一个密码，check-password 在允许继续执行之前需要此密码。密码应为明文格式。如果设置了密码，用户必须提供指定密码才能引导。

**`verbose_loading`** 如果设置为“YES”，模块名称将在加载时显示。

**`module_blacklist`** 模块黑名单。黑名单中指定的模块不能通过 `*_load` 指令自动加载，但可以在 [loader(8)](../man8/loader.8.md) 提示符下直接加载。黑名单模块仍可能作为其他模块的依赖项间接加载。

**`*_load`** 如果设置为“YES”，将加载该模块。如果未定义名称（见下文），则模块名称取与前缀相同。

**`*_name`** 定义模块的名称。

**`*_type`** 定义模块的类型。如果未给出，则默认为 kld 模块。

**`*_flags`** 要传递给模块的标志和参数。

**`*_before`** 在加载模块之前执行的命令。应避免使用此设置。

**`*_after`** 在加载模块之后执行的命令。应避免使用此设置。

**`*_error`** 如果模块加载失败执行的命令。除了特殊值“abort”（中止引导过程）外，应避免使用此设置。

*警告：* 开发者绝不应将这些后缀用于任何内核环境变量（可调参数），否则会导致冲突。

## 默认设置

`loader.conf` 的大多数默认设置可以忽略。其中几个重要或有用的是：

| **值** | **分辨率** |
| --- | --- |
| 480p | 640x480 |
| 720p | 1280x720 |
| 1080p | 1920x1080 |
| 1440p | 2560x1440 |
| 2160p | 3840x2160 |
| 4k | 3840x2160 |
| 5k | 5120x2880 |
| `Width`x`Height` | `Width`x`Height` |

**`local_loader_conf_files`**（“**/boot/loader.conf.local**”）确保 `loader.conf.local` 始终可用于覆盖 `loader_conf_files` 和 `loader_conf_dirs` 中文件中的设置。

**`bitmap_load`**（“NO”）如果设置为“YES”，将加载位图以在引导时显示在屏幕上。

**`bitmap_name`**（“**/boot/splash.bmp**”）要加载的位图名称。可使用任何其他名称。

**`comconsole_speed`**（“115200”或编译 [loader(8)](../man8/loader.8.md) 时 `BOOT_COMCONSOLE_SPEED` 变量的值）。设置串行控制台的速度。如果前一引导加载器阶段指定正在使用串行控制台，则默认速度根据当前串行端口速度设置确定。

**`console`**（“vidconsole”）以逗号或空格分隔的控制台列表。“comconsole”选择串行控制台，“vidconsole”选择视频控制台，“efi”选择 EFI 控制台，“nullconsole”选择静音控制台（适用于既无视频控制台又无串行端口的系统），“spinconsole”选择阻止任何输入并隐藏所有输出、用“旋转”字符替换的视频控制台（适用于嵌入式产品等）。此设置仅适用于 [loader(8)](../man8/loader.8.md)，不设置内核输出。

**`screen.font`** 为帧缓冲模式设置字体大小。默认字体大小根据屏幕分辨率选择。注意终端大小可能变化。

**`screen.textmode`** 值“0”将触发 BIOS loader 切换为使用 VESA BIOS 扩展（VBE）帧缓冲模式作为控制台。通过设置 `vbe_max_resolution` 可实现相同效果。值“1”将强制 BIOS loader 使用 VGA 文本模式。如果未设置 `vbe_max_resolution`，loader 将尝试根据 EDID 信息设置屏幕分辨率。如果 EDID 不可用，默认分辨率为 800x600（如果可用）。

**`screen.height`**

**`screen.width`**

**`screen.depth`** `screen.height`、`screen.width`、`screen.depth` 在 loader 使用帧缓冲模式绘制屏幕时由 loader 设置。

**`efi_max_resolution`**

**`vbe_max_resolution`** 指定 EFI 或 VBE 帧缓冲控制台的最大所需分辨率。接受以下值：

**`kernel`**（“kernel”）

**`kernels`**（“kernel kernel.old”）以空格或逗号分隔的内核列表，用于在引导菜单中呈现。

**`loader_conf_files`**（“**/boot/loader.conf /boot/loader.conf.local**”）

**`loader_conf_dirs`**（“**/boot/loader.conf.d**”）

**`splash_bmp_load`**（“NO”）如果设置为“YES”，将加载启动画面模块，使其可在引导时在屏幕上显示 bmp 图像。

**`splash_pcx_load`**（“NO”）如果设置为“YES”，将加载启动画面模块，使其可在引导时在屏幕上显示 pcx 图像。

**`vesa_load`**（“NO”）如果设置为“YES”，将加载 vesa 模块，使 VGA 分辨率以上的位图能够显示。

**`beastie_disable`** 如果设置为“YES”，将跳过 beastie 引导菜单。

**`loader_autoboot_show`**（“`YES`”）如果设置为“NO”，将不显示 autoboot 菜单

**`loader_gfx`** 如果设置为“NO”，即使图形版本可用，也将使用品牌和徽标的 ASCII 艺术版本。此外，菜单框架也将用 ASCII 艺术绘制。

**`loader_logo`**（“`orbbw`”）在 beastie 引导菜单中选择所需徽标。可能的值为：“`orbbw`”、“`orb`”、“`fbsdbw`”、“`beastiebw`”、“`beastie`”和“`none`”。

**`loader_menu`** 如果设置为“NONE”，将不显示菜单

**`loader_color`** 如果设置为“NO”，beastie 引导菜单将不带 ANSI 着色显示。

**`entropy_cache_load`**（“YES”）如果设置为“NO”，将不加载非常早期的引导时熵文件。参见 [rc.conf(5)](rc.conf.5.md) 中的 entropy 条目。

**`entropy_cache_name`**（“**/boot/entropy**”）非常早期的引导时熵缓存文件的名称。

**`cpu_microcode_load`**（“NO”）如果设置为“YES”，将加载由 `cpu_microcode_name` 指定的微码更新文件，并在引导早期应用。这提供了类似 cpucontrol(8) 的功能，但确保由微码更新启用的 CPU 功能可被内核使用。从 ACPI 睡眠状态恢复时，更新将自动重新应用。如果更新文件包含多个处理器型号的更新，内核将搜索并提取匹配的更新。目前此设置仅在 Intel `i386` 和 `amd64` 处理器上受支持。对其他处理器类型无影响。

**`cpu_microcode_name`** 微码更新文件的路径。

## 其他设置

可在 `loader.conf` 中使用但没有默认值的其他设置：

**`fdt_overlays`** 指定要应用的 FDT 覆盖的逗号分隔列表。默认创建 **/boot/dtb/overlays** 以放置覆盖。

**`kernels_autodetect`** 如果设置为“YES”，尝试自动检测安装在 **/boot** 中的内核。这是基于 Lua 的 loader 特有的选项。在默认的基于 Forth 的 loader 中不可用。

## 文件

**`/boot/defaults/loader.conf`** 默认设置——不要更改此文件。

**`/boot/loader.conf`** 用户定义设置。

**`/boot/loader.conf.lua`** 以 lua 编写的用户定义设置。

**`/boot/loader.conf.d/*.conf`** 拆分为单独文件的用户定义设置。

**`/boot/loader.conf.d/*.lua`** 以 lua 编写并拆分为单独文件的用户定义设置。

**`/boot/loader.conf.local`** 用于具有公共 loader.conf 的站点的特定于机器的设置。允许覆盖其他文件中定义的设置。

## 参见

[kenv(1)](../man1/kenv.1.md), loader.conf.lua(5), [rc.conf(5)](rc.conf.5.md), [boot(8)](../man8/boot_i386.8.md), cpucontrol(8), [loader(8)](../man8/loader.8.md), [loader.4th(8)](../man8/loader.4th.8.md)

## 历史

文件 `loader.conf` 首次出现在 FreeBSD 3.2 中。

## 作者

本手册页由 Daniel C. Sobral <dcs@FreeBSD.org> 编写。

## 缺陷

[loader(8)](../man8/loader.8.md) 在遇到语法错误时停止读取 `loader.conf`，因此对引导特定系统至关重要的任何选项（即“`hw.ata.ata_dma`=0”）应位于 `loader.conf` 中任何实验性添加之前。
