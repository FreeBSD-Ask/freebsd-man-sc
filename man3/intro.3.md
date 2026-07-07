# intro(3)

`intro` — C 库简介

## 名称

`intro`

## 概要

`cc [flags] file [-llibrary]`

## 描述

本节概述 C 库函数、其错误返回以及其他常见定义和概念。这些函数大多可从 C 库 *libc* 中获取。其他库（如数学库 *libm*）必须在编译时通过编译器的 `-l` 选项指定。

各种库（括号内为加载器标志）如下：

**标准** I/O 例程参见 stdio(3)

**数据库** 例程参见 db(3)

**位** 字符串操作参见 [bitstring(3)](bitstring.3.md)

**位** 与字节工具参见 [stdbit(3)](stdbit.3.md)

**字符串** 操作参见 string(3) 和 bstring(3)

**字符** 测试与字符操作参见 ctype(3)

**存储** 分配参见 mpool(3)

**正则表达式** 参见 regex(3)

**远程** 过程调用（RPC）参见 rpc(3)

**时间** 函数参见 time(3)

**信号** 处理参见 signal(3)

`#include <threads.h>`

***libbluetooth*** (`-l``bluetooth`) 蓝牙库。参见 bluetooth(3)。

***libc*** (`-l``c`) 标准 C 库函数。使用 C 编译器 [cc(1)](../man1/clang.1.md) 时，无需为这些函数提供加载器标志 `-l``c`。*libc* 中包含若干“库”或函数组：

***libcalendar*** (`-l``calendar`) 日历算术库。参见 calendar(3)。

***libcam*** (`-l``cam`) 通用访问方法（CAM）用户库。参见 cam(3)。

***libcrypt*** (`-l``crypt`) 加密库。参见 crypt(3)。

***libcurses*** (`-l``curses` `-l``termcap`) 用于二维非位图显示终端的终端无关屏幕管理例程。参见 ncurses(3)。

***libcuse*** (`-l``cuse`) 用户态字符设备库。参见 cuse(3)。

***libcompat*** (`-l``compat`) 已过时但为与 4.3BSD 兼容而保留的函数。特别地，BSD 早期版本提供的若干系统调用接口为源码兼容性而被保留。大多数情况下应避免使用这些例程。每个兼容性例程的手册页条目都会指明应当使用的正确接口。

***libdevinfo*** (`-l``devinfo`) 设备与资源信息工具库。参见 devinfo(3)。

***libdevstat*** (`-l``devstat`) 设备统计库。参见 devstat(3)。

***libdwarf*** (`-l``dwarf`) DWARF 访问库。参见 dwarf(3)。

***libelf*** (`-l``elf`) ELF 访问库。参见 elf(3)。

***libfetch*** (`-l``fetch`) 文件传输库。参见 fetch(3)。

***libfigpar*** (`-l``figpar`) 配置文件解析库。参见 figpar(3)。

***libgpio*** (`-l``gpio`) 通用输入输出（GPIO）库。参见 gpio(3)。

***libgssapi*** (`-l``gssapi`) 通用安全服务应用程序编程接口库。参见 gssapi(3)。

***libjail*** (`-l``jail`) Jail 库。参见 jail(3)。

***libkvm*** (`-l``kvm`) 用于访问内核内存的函数库。这些函数既可用于运行中的系统，也可用于崩溃转储。参见 kvm(3)。

***libl*** (`-l``l`) lex(1) 使用的库。

***libm*** (`-l``m`) 数学库。参见 math(3)。

***libmd*** (`-l``md`) 消息摘要库。参见 md4(3)、md5(3)、sha(3)、sha256(3)、sha512(3)、ripemd(3)、skein(3)。

***libmp*** (`-l``mp`)

***libpam*** (`-l``pam`) 可插拔认证模块库。参见 pam(3)。

***libpcap*** (`-l``pcap`) 数据包捕获库。参见 pcap(3)。

***libpmc*** (`-l``pmc`) 性能计数器库。参见 pmc(3)。

***libpthread*** (`-l``pthread`) POSIX 线程库。参见 [pthread(3)](pthread.3.md)。

***libstdthreads*** (`-l``stdthreads`) ISO C11 标准线程库。参见 thrd_create(3)。

***libsysdecode*** (`-l``sysdecode`) 系统参数解码库。参见 sysdecode(3)。

***libtermcap*** (`-l``termcap`) 终端无关操作库包。参见 termcap(3)。

***libusb*** (`-l``usb`) USB 访问库。参见 usb(3)。

***libvgl*** (`-l``vgl`) 视频图形库。参见 vgl(3)。

***liby*** (`-l``y`) yacc(1) 使用的库。

***libz*** (`-l``z`) 通用数据压缩库。参见 zlib(3)。

## 文件

**`/usr/lib/libc.a`** C 库

**`/usr/lib/libm.a`** 数学库

## 库类型

系统库位于 **`/lib`** 和 **`/usr/lib`**。库遵循以下命名约定：

```sh
libc.so.7
```

后缀为 `.a` 的库是静态库。当程序与静态库链接时，所有必要的库代码都会被包含进二进制文件中。这意味着即使库不可用，二进制文件也能运行。然而，这在磁盘空间和执行时的内存使用上可能效率较低。可通过指定 `-static` 标志让 C 编译器 [cc(1)](../man1/clang.1.md) 进行静态链接。

后缀为 `.so.X` 的库是动态库。当代码以动态方式链接时，应用程序所需的库代码不会包含在二进制文件中。取而代之的是，会添加包含要链接的动态库信息的数据结构。当二进制文件执行时，运行时链接器 ld.so(1) 读取这些数据结构并将其加载到进程的虚拟地址空间中。rtld(1) 在程序执行时加载共享库。

`X` 表示库的版本号。在上面的示例中，与 `libc.so.8` 链接的二进制文件在只有 `libc.so.7` 可用的系统上将无法使用。

动态库的优势在于同一库的多个实例可以共享地址空间，并且二进制文件的物理大小更小。每个共享库可通过隐藏可见性获得独立的命名空间，使库中的多个编译单元能够共享内容而不暴露给其他库。可通过 dlopen(3) 动态加载库。其劣势在于动态加载库所带来的额外复杂性，以及加载库所需的额外时间。当然，如果库不可用，二进制文件将无法执行。跨共享库的调用也稍慢，且无法内联，即便使用链接时优化也不行。可通过指定 `-shared` 标志让 C 编译器 [cc(1)](../man1/clang.1.md) 进行动态链接。

共享库，以及在默认情况下生成位置无关可执行文件（PIE）的架构上的静态库，都包含位置无关代码（PIC）。通常，编译器生成可重定位代码。可重定位代码在运行时需要根据其在内存中的运行位置进行修改。可通过指定 `-fPIC` 标志让 C 编译器 [cc(1)](../man1/clang.1.md) 生成 PIC 代码。

静态库通过 [ar(1)](../man1/ar.1.md) 工具生成。库中包含一个内容索引，存储在库自身内部。该索引列出库中作为可重定位目标文件的成员所定义的每个符号。这加快了与库的链接速度，并允许库中的例程相互调用，而不管它们在库中的位置如何。

## 参见

[ar(1)](../man1/ar.1.md), [cc(1)](../man1/clang.1.md), [ld(1)](../man1/ld.lld.1.md), nm(1), intro(2), math(3), stdio(3), [make.conf(5)](../man5/make.conf.5.md), [src.conf(5)](../man5/src.conf.5.md)

## 历史

`cc` 手册首次出现于 Version 7 AT&T UNIX。
