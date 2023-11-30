  OW(4)  

OW(4)

FreeBSD Kernel Interfaces Manual

OW(4)

[名称](#__u540D___u79F0_)
=======================

`ow` —

Dallas Semiconductor 1-Wire bus

[概要](#__u6982___u8981_)
=======================

`device ow`

[描述](#__u63CF___u8FF0_)
=======================

`ow` 模块实现了 Dallas Semiconductor 1-Wire 总线。它与 owc(4) 驱动器相连，后者实现了 1-Wire 总线的低级别信号。

[参见](#__u53C2___u89C1_)
=======================

ow\_temp(4), owc(4), owll(9), own(9)

[法律条款](#__u6CD5___u5F8B___u6761___u6B3E_)
=========================================

1-Wire 是 Maxim Integrated Products, Inc. 的注册商标。

[历史](#__u5386___u53F2_)
=======================

`ow` 驱动程序首次出现在 FreeBSD 11.0 中。

[作者](#__u4F5C___u8005_)
=======================

`ow` 设备驱动程序和本手册页是由 Warner Losh 编写的。

July 20, 2015

FreeBSD 13.1-RELEASE