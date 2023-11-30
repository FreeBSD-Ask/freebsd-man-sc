  ZDIFF(1)  

ZDIFF(1)

FreeBSD General Commands Manual

ZDIFF(1)

[名称](#__u540D___u79F0_)
=======================

`zcmp`, `zdiff` —

比较压缩文件

[概要](#__u6982___u8981_)
=======================

`zcmp` \[options\] file \[file2\] `zdiff` \[options\] file \[file2\]

[描述](#__u63CF___u8FF0_)
=======================

`zcmp` 和 `zdiff` 是分别调用 cmp(1) 或 diff(1)-
来比较压缩文件的过滤器。 指定的任何 options 都将传递给 cmp(1) 或 diff(1) 。

如果仅指定了 file1 ，则将其与同名但已删除扩展名的文件进行比较。 当同时指定 file1 或 file2 时，可以压缩任一文件。

gzip(1) 处理的扩展：

*   z, Z,
*   gz,
*   taz,
*   tgz.

bzip2(1) 处理的扩展：

*   bz,
*   bz2,
*   tbz,
*   tbz2.

xz(1) 处理的扩展：

*   lzma,
*   xz,
*   tlz,
*   txz.

[环境](#__u73AF___u5883_)
=======================

[`TMPDIR`](#TMPDIR)

放置临时文件的目录。 如果未设置，则使用 /tmp 。

[文件](#__u6587___u4EF6_)
=======================

/tmp/zcmp.XXXXXXXXXX

`zcmp` 的临时文件。

/tmp/zdiff.XXXXXXXXXX

`zdiff` 的临时文件。

[参见](#__u53C2___u89C1_)
=======================

bzip2(1), cmp(1), diff(1), gzip(1), xz(1)

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

`zcmp` 和 `zdiff` 仅依靠文件扩展名来确定什么是或不是压缩文件。 因此，不支持以下内容作为参数：

*   目录
*   设备特殊文件
*   表示标准输入的文件名 (“-”)

May 23, 2011

FreeBSD 13.1-RELEASE