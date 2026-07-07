# config(8)

`config` — 构建系统配置文件

## 名称

`config`

## 概要

`config [-CVgpv] [-I path] [-d destdir] [-s srcdir] SYSTEM_NAME`

`config [-x kernel]`

## 描述

`config` 工具根据描述待配置系统的 `SYSTEM_NAME` 文件来构建一组系统配置文件。另一个文件告诉 `config` 生成系统需要哪些文件，并且可以通过特定于配置的文件集合进行扩充，这些文件为特定机器提供替代文件（参见下文的文件章节）。

可用选项和操作数如下：

**`-V`** 打印 `config` 版本号。

**`-C`** 如果配置文件中存在 INCLUDE_CONFIG_FILE，内核镜像将包含完整配置文件的逐字内容（保留注释）。保留此标志是为了向后兼容。

**`-I`** `path` 在 `path` 中搜索由 `include` 指令包含的任何文件。此选项可多次指定。

**`-d`** `destdir` 使用 `destdir` 作为输出目录，而非默认目录。注意，`config` 不会将 `SYSTEM_NAME` 追加到给定目录中。

**`-s`** `srcdir` 使用 `srcdir` 作为源代码目录，而非默认目录。

**`-m`** 打印此内核的 MACHINE 和 MACHINE_ARCH 值并退出。

**`-g`** 为调试配置系统。

**`-x`** `kernel` 打印嵌入内核文件中的内核配置文件。仅当配置文件中存在 `options INCLUDE_CONFIG_FILE` 条目时，此选项才有意义。

**`-v`** 开启详细输出。

**`SYSTEM_NAME`** 指定系统配置文件的名称，该文件包含一个系统配置的设备规格、配置选项和其他系统参数。

`config` 工具应在系统源代码的 `conf` 子目录（通常为 **/sys/ARCH/conf**）中运行，其中 `ARCH` 表示 FreeBSD 支持的架构之一。`config` 工具会根据需要创建 **../compile/SYSTEM_NAME** 目录或由 `-d` 选项指定的目录，并将所有输出文件放在那里。`config` 的输出由若干文件组成；对于 i386，它们是：`Makefile`，由 [make(1)](../man1/make.1.md) 用于构建系统；头文件，定义将编译到系统中的各种设备数量。

`config` 工具在 **../..** 目录或由 `-s` 选项指定的目录中查找内核源代码。

运行 `config` 后，必须在新创建 makefile 的目录中运行 “`make depend`”。`config` 工具在完成时会打印相关提示。

如果 `config` 产生任何其他错误消息，应更正配置文件中的问题并再次运行 `config`。尝试编译存在配置错误的系统很可能会失败。

## 调试内核

传统的 BSD 内核编译时不带符号，因为编译 “调试” 内核会给系统带来沉重负担。调试内核包含所有源文件的完整符号，使有经验的内核程序员能够分析问题的原因。4.4BSD Lite 之前可用的调试器能够从普通内核中找到一些信息；gdb(1)（`ports/devel/gdb`）对普通内核的支持很少，要进行任何有意义的分析需要调试内核。

由于历史、时间和空间的原因，FreeBSD 默认不构建调试内核：调试内核的构建时间最多长 30%，在构建目录中需要约 30 MB 的磁盘空间，而非调试内核仅约 6 MB。调试内核大小约 11 MB，而非调试内核约 2 MB。此空间在根文件系统和运行时内存中都会占用。使用 `-g` 选项构建调试内核。使用此选项时，`config` 会在内核构建目录中构建两个内核文件：

- `kernel.debug` 是完整的调试内核。
- `kernel` 是去除调试符号后的内核副本。等同于普通的非调试内核。

目前，安装调试内核并从中引导意义不大，因为使用符号的唯一可用工具不能在线运行。因此，安装调试内核有两个选项：

- “`make install`” 在根文件系统中安装 `kernel`。
- “`make install.debug`” 在根文件系统中安装 `kernel.debug`。

## 文件

**/sys/conf/files** 构建系统的通用文件列表

**/sys/conf/Makefile.ARCH** ARCH 的通用 makefile

**/sys/conf/files.ARCH** ARCH 特定文件列表

**/sys/ARCH/compile/SYSTEM_NAME** ARCH 上系统 SYSTEM_NAME 的默认内核构建目录。

## 参见

config(5)

第 4 节中每个设备的概要部分。

> S. J. Leffler, M. J. Karels, "Building 4.3 BSD UNIX System with Config", *4.4BSD System Manager's Manual (SMM)*.

## 历史

`config` 工具出现于 4.1BSD。

在引入 `-x` 支持之前，`options INCLUDE_CONFIG_FILE` 包含了整个配置文件，该文件过去嵌入在新内核中。这意味着可以使用 strings(1) 从内核中提取它：要提取配置信息，必须使用以下命令：

```sh
strings -n 3 kernel | sed -n 's/^___//p'
```

## 缺陷

错误消息中报告的行号通常相差一行。
