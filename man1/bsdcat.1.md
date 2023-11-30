  BSDCAT(1)  

BSDCAT(1)

FreeBSD General Commands Manual

BSDCAT(1)

[名称](#__u540D___u79F0_)
=======================

`bsdcat` —

扩展文件到标准输出

[概要](#__u6982___u8981_)
=======================

`bsdcat` \[options\] \[files\]

[描述](#__u63CF___u8FF0_)
=======================

`bsdcat` 将文件扩展为标准输出。

[选项](#__u9009___u9879_)
=======================

`bsdcat` 通常将文件名作为参数或在管道中使用时读取标准输入。在这两种情况下，它都将解压缩的数据写入标准输出。

[实例](#__u5B9E___u4F8B_)
=======================

解压文件：

`bsdcat example.txt.gz > example.txt`

在管道中解压缩标准输入：

`cat example.txt.gz | bsdcat > example.txt`

这两个示例都实现了相同的结果——通过重定向输出来解压缩文件。

[参见](#__u53C2___u89C1_)
=======================

bzcat(1) 、 uncompress(1) 、 xzcat(1) 、 zcat(1) 、 libarchive-formats(5)

March 1, 2014

FreeBSD 13.1-RELEASE