# boot0cfg(8)

`boot0cfg` — 引导管理器安装/配置工具

## 名称

`boot0cfg`

## 概要

`boot0cfg [-Bv] [-b boot0] [-d drive] [-e bell character] [-f file] [-i volume-id] [-m mask] [-o options] [-s slice] [-t ticks] disk`

## 描述

FreeBSD 的 ‘boot0’ 引导管理器允许操作者选择从哪个磁盘和 slice 启动 i386 机器（PC）。

注意，这里所说的 “slices” 在非 BSD 的 PC 相关文档中通常被称为 “partitions”（分区）。通常，只有不可移动磁盘才会被切片（slice）。

`boot0cfg` 工具可选择在指定的 `disk` 上安装 ‘boot0’ 引导管理器，并允许配置各种操作参数。

在 PC 上，引导管理器通常占据磁盘的 0 扇区，即主引导记录（Master Boot Record，MBR）。MBR 同时包含代码（PC BIOS 将控制权传递给它）和数据（一个内嵌的已定义 slice 表）。

可用选项如下：

**`-B`** 安装 ‘boot0’ 引导管理器。此选项会替换 MBR 代码，但不影响内嵌的 slice 表。

**`-b`** `boot0` 指定使用哪个 ‘boot0’ 镜像。默认为 **/boot/boot0**，使用显卡作为输出设备；也可以使用 **/boot/boot0sio** 输出到 COM1 端口。（注意，除非调制解调器信号 DSR 和 CTS 处于活动状态，否则不会有任何内容输出到 COM1 端口。）

**`-d`** `drive` 指定 PC BIOS 在引用包含指定 `disk` 的驱动器时所使用的驱动器号。通常，第一个硬盘为 0x80，第二个硬盘为 0x81，以此类推；但此处接受 0 到 0xff 之间的任何整数。

**`-e`** `bell character` 设置在输入错误时打印的字符。

**`-f`** `file` 指定将现有 MBR 的备份副本写入 `file`。如果该文件不存在则创建，已存在则替换。

**`-i`** `volume-id` 指定一个卷 ID（格式为 XXXX-XXXX），保存到 MBR 的 0x1b8 位置。此信息有时被 NT、XP 和 Vista 用于识别磁盘驱动器。此选项仅与 512 字节引导块的 2.00 版本兼容。

**`-m`** `mask` 指定要启用/禁用的 slice，其中 `mask` 是 0（不启用任何 slice）到 0xf（启用全部四个 slice）之间的整数。每个掩码位设置为 1 时启用对应的 slice。掩码的最低有效位对应 slice 1，最高有效位对应 slice 4。

**`-o`** `options` 可以指定一个由以下选项组成的逗号分隔字符串（必要时可在前面加 “no”）：

- `packet`：进行磁盘 I/O 时使用磁盘包（BIOS INT 0x13 扩展）接口，而非传统（CHS）接口。这允许在 1023 柱面之上启动，但需要特定的 BIOS 支持。默认为 ‘packet’。
- `setdrv`：强制使用通过 `-d` 选项定义的驱动器号引用包含该磁盘的驱动器。默认为 ‘nosetdrv’。
- `update`：允许引导管理器更新 MBR。（MBR 可被更新以将 slice 标记为 ‘active’，以及保存 slice 选择信息。）此为默认行为；‘noupdate’ 选项会使 MBR 被视为只读。

**`-s`** `slice` 将默认启动选择设置为 `slice`。值 1 到 4 对应各 slice；值为 5 表示从第二个磁盘启动的选项。可以使用特殊字符串 “PXE” 或值 6 通过 PXE 启动。

**`-t`** `ticks` 将超时值设置为 `ticks`。（每秒大约 18.2 个 tick。）

**`-v`** 详细模式：显示已定义的 slice 等信息。

## 文件

**/boot/boot0** 默认的 ‘boot0’ 镜像

**/boot/boot0sio** 用于串行控制台的镜像（COM1,9600,8,N,1,MODEM）

## 退出状态

`boot0cfg` 工具成功时退出状态为 0，发生错误时大于 0。

## 实例

在下次启动时启动 slice 2：

```sh
boot0cfg -s 2 ada0
```

在菜单中仅启用 slice 1 和 3：

```sh
boot0cfg -m 0x5 ada0
```

要恢复为非交互式启动，可使用 [gpart(8)](gpart.8.md) 安装默认的 MBR：

```sh
gpart bootcode -b /boot/mbr ada0
```

## 参见

[geom(4)](../man4/geom.4.md), [boot(8)](boot_i386.8.md), [gpart(8)](gpart.8.md)

## 作者

Robert Nordier <rnordier@FreeBSD.org>

## 缺陷

使用 ‘packet’ 选项可能导致 ‘boot0’ 失败，具体取决于 BIOS 支持的性质。

使用 ‘setdrv’ 选项时若 `-d` 操作数不正确，可能导致 boot0 代码将 MBR 写入错误的磁盘，从而破坏其原有内容。请小心使用。
