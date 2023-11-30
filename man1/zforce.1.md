  ZFORCE(1)  

ZFORCE(1)

FreeBSD General Commands Manual

ZFORCE(1)

[名称](#__u540D___u79F0_)
=======================

`zforce` —

强制 gzip 文件具有 .gz 后缀

[概要](#__u6982___u8981_)
=======================

`zforce` file ...

[描述](#__u63CF___u8FF0_)
=======================

`zforce` 实用程序将 gzip(1) 文件重命名为具有 ‘.gz’ 后缀，因此 gzip(1) 不会将它们压缩两次。如果文件名在文件传输期间被截断，这将很有用。具有现有 ‘.gz’, ‘-gz’, ‘\_gz’, ‘.tgz’ 或 ‘.taz’ 后缀的文件，或者没有被 gzip(1) 压缩的文件将被忽略。

[SEE ALSO](#SEE_ALSO)
=====================

gzip(1)

[警告](#__u8B66___u544A_)
=======================

`zforce` 会在没有警告的情况下覆盖现有文件。

January 26, 2007

FreeBSD 13.1-RELEASE