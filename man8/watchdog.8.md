  WATCHDOG(8)  

WATCHDOG(8)

FreeBSD System Manager's Manual

WATCHDOG(8)

[名称](#__u540D___u79F0_)
=======================

`watchdog` —

看门狗控制程序

[概要](#__u6982___u8981_)
=======================

`watchdog` \[`-d`\] \[`-t` timeout\]

[描述](#__u63CF___u8FF0_)
=======================

`watchdog` 实用程序可用于控制内核的看门狗设施。

`-d` 选项启用调试。

`-t` timeout 选项以秒为单位指定所需的超时时间，零值将禁用看门狗。 默认超时为 128 秒。

[参见](#__u53C2___u89C1_)
=======================

watchdog(4), watchdogd(8), watchdog(9)

[历史](#__u5386___u53F2_)
=======================

`watchdog` 实用程序出现在 FreeBSD 5.1 中。

[作者](#__u4F5C___u8005_)
=======================

`watchdog` 实用程序和手册页由 Sean Kelly <[smkelly@FreeBSD.org](mailto:smkelly@FreeBSD.org)\> 和 Poul-Henning Kamp <[phk@FreeBSD.org](mailto:phk@FreeBSD.org)\> 编写。

Jeff Roberson <[jeff@FreeBSD.org](mailto:jeff@FreeBSD.org)\> 做出的一些贡献。

October 18, 2014

FreeBSD 13.1-RELEASE