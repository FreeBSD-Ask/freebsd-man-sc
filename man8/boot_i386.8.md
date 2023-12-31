  BOOT(8) (i386)  

BOOT(8)

FreeBSD System Manager's Manual (i386)

BOOT(8)

[名称](#__u540D___u79F0_)
=======================

`boot` —

系统引导程序

[描述](#__u63CF___u8FF0_)
=======================

**电源故障和崩溃恢复。** 通常，系统会在上电或崩溃后自行重启。 将执行文件系统的自动一致性检查，除非检查失败，否则系统将恢复多用户操作。

**冷启动。** 大多数 i386 PC 尝试首先从软盘驱动器 0（有时称为驱动器 A:）启动，如果失败，则从硬盘驱动器 0（有时称为驱动器 C:，或作为 BIOS 的驱动器 0x80）启动。 某些 BIOS 允许您更改此默认顺序，并且可能还包括一个 CD-ROM 驱动器作为引导设备。

一些较新的 PC 使用 UEFI 固件而不是 BIOS 启动。 该过程在 uefi(8) 中进行了描述。

采用三阶段自举。 控制从引导块（引导阶段一和二）传递到第三阶段引导程序 loader(8) 。 这第三阶段对引导过程提供了比在引导块中可能实现的更复杂的控制，引导块受到在给定磁盘或片上占用有限固定空间的限制。

本小节的其余部分仅涉及引导块。 loader(8) 程序单独记录。

加载引导块后，您应该会看到类似于以下内容的提示：

\>> FreeBSD/x86 BOOT Default: 0:ad(0,a)/boot/loader boot: 

自动引导将尝试从软盘或硬盘的分区 ‘`a`’ 加载 /boot/loader 通过在键盘上的 ‘`boot:`’ 提示符下键入任何字符，可以中止此引导。 此时，将接受以下输入：

[`?`](#?)

给出默认引导设备根目录中文件的简短列表，作为有关可用引导文件的提示。 （A `?` 也可以指定为路径的最后一段，在这种情况下，列表将是相关子目录的。）

bios\_drive:interface(unit,\[slice,\]part)filename \[`-aCcDdghmnPprsv`\] \[`-S`speed\]

指定引导文件和标志。

bios\_drive

BIOS 识别的驱动器号。 第一个驱动器为 0，第二个驱动器为 1，依此类推。

interface

要从中引导的控制器的类型。 请注意，控制器需要具有 BIOS 支持，因为 BIOS 服务用于加载引导文件映像。

支持的接口有：

ad

WD100\[2367\] 或类似控制器上的 ST506、IDE、ESDI、RLL 磁盘

fd

5 1/4" 或 3 1/2" 高密度软盘

da

任何支持的 SCSI 控制器上的 SCSI 磁盘

unit

正在使用的接口上的驱动器的单元号。 第一个驱动器为 0，第二个驱动器为 1，依此类推。

\[slice,\]part

磁盘的 BSD 部分内的分区号。 请参见 bsdlabel(8) 。 按照惯例，只有分区 ‘`a`’ 包含可引导映像。 如果使用分片磁盘 (“fdisk partitions”) ，则可以从任何 slice （第一个分片为 1，第二个分片为 2 等）启动，默认（如果未指定）为活动分片，否则，第一个 FreeBSD FreeBSD 切片。 如果将 slice 指定为 0，则从第一个 FreeBSD 分片（也称为 “compatibility” 分片）启动。

filename

要引导的文件的路径名（相对于指定分区上的根目录）。 默认为 /boot/kernel/kernel 。 不支持符号链接（支持硬链接）。

\[`-aCcDdghmnPpqrsv`\] \[`-S`speed\]

引导标志：

[`-a`](#a)

在内核初始化期间，要求设备作为根文件系统挂载。

[`-C`](#C)

尝试从 CD-ROM 挂载根文件系统。

[`-c`](#c)

此标志当前是无操作的。

[`-D`](#D)

使用双控制台配置启动。 在单一配置中，控制台将是内部显示器或串行端口，具体取决于以下 `-h` 选项的状态。 在双控制台配置中，无论 `-h` 选项的状态如何，内部显示器和串口都将同时成为控制台。

[`-d`](#d)

在内核初始化中尽早进入 DDB 内核调试器（参见 ddb(4) ）。

[`-g`](#g)

使用 GDB 远程调试协议。

[`-h`](#h)

强制串行控制台。 例如，如果您从内部控制台启动，您可以使用 `-h` 选项强制内核使用串行端口作为其控制台设备。

[`-m`](#m)

使控制台静音以在引导期间抑制所有内核控制台输入和输出。

[`-n`](#n)

在调用 loader(8) 之前忽略按键以中断引导。

[`-P`](#P)

探测键盘。 如果未找到键盘，则会自动设置 `-D` 和 `-h` 选项。

[`-p`](#p)

在设备探测阶段每个连接的设备后暂停。

[`-q`](#q)

保持安静，除非自动启动失败或被禁用，否则不要向控制台写入任何内容。 此选项仅影响第二阶段引导程序，以防止下一个阶段与 `-m` 选项结合使用写入控制台。

[`-r`](#r)

对包含根文件系统的设备使用静态配置的默认值（请参阅 config(8) ）。通常，根文件系统位于从中加载内核的设备上。

[`-s`](#s)

启动进入单用户模式；如果控制台被标记为 “insecure” (参见 ttys(5)), 则必须输入 root 密码。

[`-S`](#S)speed

将串行控制台的速度设置为 speed 。 默认值为 9600，除非已通过在 make.conf(5) 中设置 BOOT\_COMCONSOLE\_SPEED 并重新编译和重新安装引导块来覆盖它。

[`-v`](#v)

在设备探测（及以后）期间要冗长。

使用 /boot.config 文件设置引导块代码的默认配置选项。 有关 boot.config(5) 文件的更多信息，请参见 /boot.config 。

[文件](#__u6587___u4EF6_)
=======================

/boot.config

引导块的参数（可选）

/boot/boot1

第一阶段引导文件

/boot/boot2

第二阶段引导文件

/boot/loader

第三阶段引导

/boot/kernel/kernel

默认内核

/boot/kernel.old/kernel

典型的非默认内核（可选）

[诊断](#__u8BCA___u65AD_)
=======================

当发生与磁盘相关的错误时，第二阶段引导程序会使用 BIOS 返回的相同错误代码报告这些错误，例如 “Disk error 0x1 (lba=0x12345678)” 。 以下是这些错误代码的部分列表：

0x1

无效的论点

0x2

找不到地址标记

0x4

未找到扇区

0x8

DMA 溢出

0x9

跨 64K 边界的 DMA 尝试

0xc

无效的媒体

0x10

不可纠正的 CRC/ECC 错误

0x20

控制器故障

0x40

搜索失败

0x80

暂停

**注意**: 在较旧的机器上，或者在 EDD 支持（磁盘数据包接口支持）不可用的其他地方，所有需要在引导阶段访问的与引导相关的文件和结构（包括内核）必须驻留在磁盘上或以下位置柱面 1023（因为 BIOS 了解几何结构）。 当第二阶段引导程序报告 “Disk error 0x1” 时，通常表示未遵守此要求。

[参见](#__u53C2___u89C1_)
=======================

ddb(4), boot.config(5), make.conf(5), mount.conf(5), ttys(5), boot0cfg(8), btxld(8), config(8), efibootmgr(8), efivar(8), gpart(8), gptboot(8), gptzfsboot(8), halt(8), loader(8), nextboot(8), reboot(8), shutdown(8), uefi(8), zfsbootcfg(8)

[缺陷](#__u7F3A___u9677_)
=======================

这个版本的 BSD 使用的 bsdlabel 格式与其他体系结构完全不同。

由于空间限制，由 `-P` 选项启动的键盘探测只是测试 BIOS 是否检测到 “extended” 键盘。 如果连接了 “XT/AT” 键盘（没有 F11 和 F12 键等），则探头将失败。

July 11, 2020

FreeBSD 13.1-RELEASE