  LDD(1)  

LDD(1)

FreeBSD General Commands Manual

LDD(1)

[名称](#__u540D___u79F0_)
=======================

`ldd` —

列出动态对象依赖项

[概要](#__u6982___u8981_)
=======================

`ldd` \[`-a`\] \[`-v`\] \[`-f` format\] program ...

[描述](#__u63CF___u8FF0_)
=======================

`ldd` 实用程序显示运行给定程序或加载给定共享对象所需的所有共享对象。 与 nm(1) 不同，该列表包括 “indirect” 依赖关系，这些依赖关系是所需共享对象的结果，这些共享对象本身又依赖于其他共享对象。

可以给出零个、一个或两个 `-f` 选项。 该参数是传递给 rtld(1) 的格式字符串，并允许自定义 `ldd`的输出。 如果给定一个，它会设置 `LD_TRACE_LOADED_OBJECTS_FMT1` 。如果给出两个，它们分别设置 `LD_TRACE_LOADED_OBJECTS_FMT1` 和 `LD_TRACE_LOADED_OBJECTS_FMT2。` 有关详细信息，包括已识别的转换字符列表，请参见 rtld(1) 。

`-a` 选项显示每个加载的对象所需的所有对象的列表。 此选项不适用于 a.out(5) 二进制文件。

`-v` 选项显示在可执行文件中编码的动态链接头的详细列表。 请参阅源代码和包含文件以了解所有字段的明确含义。

[实现说明](#__u5B9E___u73B0___u8BF4___u660E_)
=========================================

`ldd` 通过设置 rtld(1) 环境变量并在子进程中运行可执行文件来列出可执行文件的依赖项。 如果可执行文件损坏或无效，则 `ldd` 可能会因此失败，而不会提供任何诊断错误消息。

[实例](#__u5B9E___u4F8B_)
=======================

以下是使用 `-f` 选项的 shell 管道示例。 它将打印当前目录中所有 ELF 二进制文件的报告，这些文件链接到 libc.so.6:

`find . -type f | xargs -n1 file -F ' ' | grep 'ELF.*dynamically' | cut -f1 -d' ' | xargs ldd -f '%A %o\n' | grep libc.so.6`

[参见](#__u53C2___u89C1_)
=======================

ld(1) 、 nm(1) 、 readelf(1) 、 rtld(1)

[历史](#__u5386___u53F2_)
=======================

`ldd` 实用程序首先出现在 SunOS 4.0 中，它以当前形式出现在 FreeBSD 1.1 中。

`-v` 支持基于 John Polstra <[jdp@polstra.com](mailto:jdp@polstra.com)\> 编写的代码

October 23, 2018

FreeBSD 13.1-RELEASE