  OWC(4)  

OWC(4)

FreeBSD Kernel Interfaces Manual

OWC(4)

[名称](#__u540D___u79F0_)
=======================

`owc` —

Dallas Semiconductor 1-Wire 控制器

[概要](#__u6982___u8981_)
=======================

`owc 设备`

[描述](#__u63CF___u8FF0_)
=======================

The `owc` 模块实现了 Dallas Semiconductor 1-Wire 信令。它连接了 ow(4) 驱动器的1-Wire总线协议。 `owc` 设备实现了1-Wire总线协议栈的链接层。

gpiobus(4) 上的位撞针是唯一支持的控制器。 标准和超速传输时序都已实现。支持寄生模式所需的强上拉功能没有实现。

要为FDT系统启用1-Wire，需要为你的电路板修改DTS，增加一些内容:

/ { ... onewire { compatible = "w1-gpio"; gpios = <&gpio 4 1>; }; ... }; 

gpios 属性描述了1-Wire总线所连接的GPIO引脚。 关于 gpios 属性的更多细节，请参考 /usr/src/sys/dts/bindings-gpio.txt 。

在基于 device.hints(5) )的系统中， `owc` 需要这些值:

hint.owc.%d.at

你所连接的 `gpiobus` 。

hint.owc.%d.pins

一个比特掩码，定义了 `gpiobus` 上用于1-Wire总线的引脚。 例如，要配置引脚10，使用0x400的掩码。 请注意，这个掩码应该只设置一个位（任何其他位--即针脚--将被忽略）。

[参见](#__u53C2___u89C1_)
=======================

gpiobus(4), ow(4), ow\_temp(4), owll(9), own(9)

[法律条款](#__u6CD5___u5F8B___u6761___u6B3E_)
=========================================

1-Wire 是Maxim Integrated Products, Inc.的注册商标。

[历史](#__u5386___u53F2_)
=======================

`owc` 驱动程序首次出现在 FreeBSD 11.0 中。

[作者](#__u4F5C___u8005_)
=======================

`owc` 设备驱动程序和本手册页是由 Warner Losh 编写的。

[警告](#__u8B66___u544A_)
=======================

gpio 驱动程序通过繁忙的等待来实现计时，这在较慢的系统上可能会导致高负载。

[缺陷](#__u7F3A___u9677_)
=======================

Overdrive模式还没有被实际测试。

June 26, 2019

FreeBSD 13.1-RELEASE