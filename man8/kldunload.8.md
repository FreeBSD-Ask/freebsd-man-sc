  KLDUNLOAD(8)  

KLDUNLOAD(8)

FreeBSD System Manager's Manual

KLDUNLOAD(8)

[名称](#__u540D___u79F0_)
=======================

`kldunload` —

从内核卸载文件

[概要](#__u6982___u8981_)
=======================

`kldunload` \[`-fv`\] `-i` id ... `kldunload` \[`-fv`\] \[`-n`\] name ...

[描述](#__u63CF___u8FF0_)
=======================

`kldunload` 实用程序卸载以前用 kldload(8) 加载的文件。

可以使用以下选项：

[`-f`](#f)

强制卸载。 这会忽略从模块返回到 `MOD_QUIESCE` 的错误，并暗示即使模块当前正在使用，也应该卸载该模块。 让用户尽其所能应对。

[`-v`](#v)

更冗长。

[`-i`](#i) id

卸载具有此 ID 的文件。

[`-n`](#n) name

卸载具有此名称的文件。

name

卸载具有此名称的文件。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `kldunload` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

kldunload(2), kldload(8), kldstat(8)

[历史](#__u5386___u53F2_)
=======================

`kldunload` 实用程序首次出现在 FreeBSD 3.0 中，取代了 `lkm` 界面。

[作者](#__u4F5C___u8005_)
=======================

Doug Rabson <[dfr@FreeBSD.org](mailto:dfr@FreeBSD.org)\>

February 27, 2006

FreeBSD 13.1-RELEASE