  DEVICE.HINTS(5)  

DEVICE.HINTS(5)

FreeBSD File Formats Manual

DEVICE.HINTS(5)

[名称](#__u540D___u79F0_)
=======================

`device.hints` —

设备资源提示

[描述](#__u63CF___u8FF0_)
=======================

`device.hints` 文件在系统即将启动时被 loader(8) 读取，其内容被传递给内核。它包含各种变量来控制内核的启动行为。这些变量通常是 “device hints”, 但也可以包括任何内核可调整的值。

该文件每行包含一个变量。 以 ‘`#`’ 字符开头的行是注释，被 Boot Loader 忽略。

在 Boot Loader 读取文件之后，你可以使用 `show` 命令检查变量，也可以使用 Boot Loader 的 `set` 和 `unset` 命令增加一个新的变量，修改一个已经存在的变量，或者删除一个变量（见 loader(8) ) 。

在系统启动后，你可以使用 kenv(1) 命令来转储这些变量。

[设备提示](#__u8BBE___u5907___u63D0___u793A_)
=========================================

设备提示变量被设备驱动用来设置设备。 它们最常被ISA设备驱动用来指定驱动将在哪里探测相关设备，以及它将尝试使用哪些资源。

一个设备提示行看起来像。:

`hint.`driver.unit.keyword`=`“value”

其中， driver 是设备驱动程序的名称， unit 是单元号， keyword 是提示的关键词。 关键字可以是：

[`at`](#at)

指定设备所连接的总线。

[`port`](#port)

指定设备要使用的I/O端口的起始地址。

[`portsize`](#portsize)

指定设备使用的端口的数量。

[`irq`](#irq)

要使用的中断线号。

[`drq`](#drq)

是DMA通道的编号。

[`maddr`](#maddr)

指定设备使用的物理内存地址。

[`msize`](#msize)

指定设备使用的物理内存大小。

[`flags`](#flags)

设置设备的各种标志位。

[`disabled`](#disabled)

可以被设置为 “1” 来禁用设备。

一个设备驱动可能需要一个或多个带有这些关键字的提示行，并且可以通过 resource\_int\_value(9) 接受其他没有在这里列出的关键字。 关于可用的关键字和它们可能的值，请查阅各个设备驱动的手册页面。

[文件](#__u6587___u4EF6_)
=======================

/boot/device.hints

设备资源提示文件。

/sys/ARCH/conf/GENERIC.hints

GENERIC 内核的资源提示样本。

/sys/ARCH/conf/NOTES

关于内核配置文件和设备资源提示的说明。

[实例](#__u5B9E___u4F8B_)
=======================

下面的例子为 ISA 总线上的 uart(4) 驱动程序设置了资源：

hint.uart.0.at="isa" hint.uart.0.port="0x3F8" hint.uart.0.flags="0x10" hint.uart.0.irq="4" 

下面的例子禁用了ACPI驱动:

hint.acpi.0.disabled="1" 

-
设置一个可调整的变量:

vm.pmap.pg\_ps\_enabled=1 

[参见](#__u53C2___u89C1_)
=======================

kenv(1), loader.conf(5), loader(8), resource\_int\_value(9)

[历史](#__u5386___u53F2_)
=======================

`device.hints` 文件首次出现在 FreeBSD 5.0 中。

November 19, 2019

FreeBSD 13.1-RELEASE