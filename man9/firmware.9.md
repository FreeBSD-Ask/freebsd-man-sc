# firmware.9

`firmware_register` — 固件镜像加载与管理

## 名称

`firmware_register`, `firmware_unregister`, `firmware_get`, `firmware_get_flags`, `firmware_put`

## 概要

```c
#include <sys/param.h>

#include <sys/systm.h>

#include <sys/linker.h>

#include <sys/firmware.h>

struct firmware {
	const char	*name;		/* 系统范围的名称 */
	const void	*data;		/* 镜像位置 */
	size_t		datasize;	/* 镜像大小（字节） */
	unsigned int	version;	/* 镜像版本 */
};

const struct firmware *
firmware_register(const char *imagename, const void *data,
    size_t datasize, unsigned int version, const struct firmware *parent)

int
firmware_unregister(const char *imagename)

const struct firmware *
firmware_get(const char *imagename)

const struct firmware *
firmware_get_flags(const char *imagename, uint32_t flags)

void
firmware_put(const struct firmware *fp, int flags)
```

## 描述

`firmware` 抽象层为将 `firmware` 加载到内核以及从内核组件访问此类镜像提供了便捷的接口。

一个 `firmware`（简称 `image`）是驻留在内核内存中的不透明数据块。它与一个作为搜索键的唯一 `imagename` 以及一个整数 `version` 版本号关联，版本号对于固件子系统而言也是不透明信息。

镜像通过调用 `firmware_register` 函数向 `firmware` 子系统注册，并通过调用 `firmware_unregister` 注销。这些函数通常（但不仅限于）由包含固件镜像的专门构造的内核模块调用。这些模块可静态编译进内核，或由 **/boot/loader** 加载，或在运行时手动加载，或由固件子系统按需加载。

固件二进制文件也可直接加载，而无需嵌入到内核模块中。

固件子系统的 `Clients` 可以通过以所需的 `imagename` 为参数调用 `firmware_get`，或以 `imagename` 和 `flags` 为参数调用 `firmware_get_flags` 来请求访问给定镜像。如果尚未注册匹配的镜像，固件子系统将尝试使用下文指定的机制加载它（通常是名称与镜像相同的内核模块，带 `flags`）。

## API 描述

内核固件 API 由以下函数组成：

`firmware_register` 向内核注册一个大小为 `datasize`、位于地址 `data` 的镜像，名称为 `imagename`。

该函数出错时返回 `NULL`（例如由于已存在同名镜像，或镜像表已满），或返回指向所请求镜像的 `const struct firmware *` 指针。

`firmware_unregister` 尝试从系统中注销固件镜像 `imagename`。如果没有对该镜像的待处理引用，则函数成功并返回 0；否则不注销镜像并返回 `EBUSY`。

`firmware_get` 和 `firmware_get_flags` 返回所请求的固件镜像。`flags` 参数可设置为 `FIRMWARE_GET_NOWARN`，指示固件加载或注册错误仅在 `booverbose` 时才记录日志。如果镜像尚未在系统中注册，这些函数会尝试加载它。这涉及链接器子系统和磁盘访问，因此 `firmware_get` 或 `firmware_get_flags` 不得在持有任何锁时调用（`Giant` 除外）。还需注意，如果固件镜像从文件系统加载，该文件系统必须已挂载。特别地，这意味着可能需要延迟来自驱动程序附加方法的请求，除非已知根文件系统已挂载。

成功时，`firmware_get` 和 `firmware_get_flags` 返回指向镜像描述的指针，并增加该镜像的引用计数。失败时，这些函数返回 `NULL`。

`firmware_put` 释放对固件镜像的引用。`flags` 参数可设置为 `FIRMWARE_UNLOAD`，指示如果这是最后一个引用，`firmware_put` 可自由回收与固件镜像关联的资源。默认情况下，固件镜像会被推迟到 [taskqueue(9)](taskqueue.9.md) 线程处理，因此可在持有锁时调用。在某些情况下，例如驱动程序分离时，这是不允许的。

## 通过模块加载固件

如前所述，系统的任何组件都可以通过简单调用 `firmware_register` 在任何时候注册固件镜像。

这通常在包含固件镜像的模块获得控制权时完成，无论是编译进内核、由 **/boot/loader** 预加载，还是通过 [kldload(8)](../man8/kldload.8.md) 手动加载。然而，系统可以实现额外的机制，在调用 `firmware_register` 之前将这些镜像带入内存。

当 `firmware_get` 或 `firmware_get_flags` 找不到所请求的镜像时，它会尝试使用可用的加载机制之一加载它。目前只有一种，即 `Loadable`。

名为 `foo` 的固件镜像通过尝试加载名为 `foo.ko` 的模块来查找，使用 [kld(4)](../man4/kld.4.md) 中描述的设施。特别地，镜像在 sysctl 变量 `kern.module_path` 指定的目录中查找，在大多数系统上默认为 **/boot/kernel;/boot/modules**。

注意，如果一个模块包含多个镜像，调用者应先对该模块中包含的第一个镜像请求 `firmware_get` 或 `firmware_get_flags`，然后再请求其他镜像。

## 构建可加载固件模块

固件模块通过将 `firmware` 嵌入到合适的可加载内核模块中构建，该模块在加载时调用 `firmware_register`，在卸载时调用 `firmware_unregister`。

各种系统脚本和 makefile 允许你通过简单地编写包含以下条目的 Makefile 来构建模块：

```sh
        KMOD=   imagename
        FIRMWS= image_file:imagename[:version]
        .include <bsd.kmod.mk>
```

其中 KMOD 是模块的基本名；FIRMWS 是以冒号分隔的元组列表，指示要嵌入模块的 image_file、每个固件镜像的 imagename 和 version。

如果需要将固件镜像嵌入到系统中，应在 <files.arch> 或 <files> 文件中编写适当的条目，例如以下示例来自 **sys/conf/files**：

```sh
iwn1000fw.c			optional iwn1000fw | iwnfw		\
	compile-with	"${AWK} -f $S/tools/fw_stub.awk iwn1000.fw:iwn1000fw -miwn1000fw -c${.TARGET}" \
	no-ctfconvert no-implicit-rule before-depend local		\
	clean		"iwn1000fw.c"
#
# 注意：ld 将为固件镜像生成的二进制符号中的路径编码，
#     因此将文件链接到目标目录以获取在 _fw.c 文件中引用的已知值。
#
iwn1000fw.fwo			optional iwn1000fw | iwnfw		\
	dependency	"iwn1000.fw"					\
	compile-with	"${NORMAL_FWO}"					\
	no-implicit-rule						\
	clean		"iwn1000fw.fwo"
```

固件以前以 uuencoded 文件形式提交到源代码树中，但现在不再需要；二进制固件文件应按供应商提供的形式提交到树中。

注意，以这种方式生成固件模块需要以下工具可用：[awk(1)](../man1/awk.1.md)、[make(1)](../man1/make.1.md)、编译器和链接器。

## 加载二进制固件文件

### 二进制固件格式

二进制固件文件也可以加载，从 **/boot/loader** 加载，或当 `firmware_get` 无法从内核模块找到已注册的固件时加载。二进制固件文件是固件创建者制作的原始二进制文件。它们提供了一种更简单的固件加载方式，但缺少内核模块的完全灵活性和通用性，具有以下限制：

- 二进制固件文件仅保存一组固件。
- 它们不提供内核模块依赖项，无法确保由引导加载程序自动加载。
- 它们不能编译进内核。
- `imagename` 与用于加载模块的完整路径名相同。
- 版本号假定为零。

### 从 /boot/loader 加载

二进制固件文件可以从命令行使用 “load -t firmware /boot/firmware/filename” 加载，或使用 loader.conf(5) 机制加载类型为 “firmware” 的模块。例如：

```sh
wififw_load="YES"
wififw_name="/boot/firmware/wifi2034_fw.bin"
wififw_type="firmware"
```

### 从 firmware_get 按需加载

如果没有加载名为 `imagename` 的内嵌固件镜像内核模块，则 `imagename` 将附加到模块路径（默认为 **/boot/firmware/**），如果该文件存在，将使用 `firmware_register` 加载并注册，以文件的完整路径作为 `imagename`。

### 搜索 imagename

`firmware_get` 使用以下算法查找固件镜像：

- 如果已为 `imagename` 注册了现有固件镜像，则返回该镜像。
- 如果 `imagename` 与某个具有完整路径的已注册镜像的尾部子路径匹配，则返回该镜像。
- 内核链接器搜索名为 `imagename` 的内核模块。如果找到内核模块，则加载它，并再次搜索已注册的固件镜像列表。如果找到匹配项，则返回匹配的镜像。
- 内核在固件镜像路径（默认为 **/boot/firmware/**）中搜索名为 `imagename` 的文件。如果该文件存在且可读，其内容将以完整路径作为 `imagename` 注册为固件镜像，并返回该固件。目前，固件镜像的大小限制为 8MB。这可通过 sysctl 变量 `debug.max_firmware_size` 更改。

## 参见

[kld(4)](../man4/kld.4.md), [module(9)](module.9.md)

**/boot/firmware**

**/usr/share/examples/kld/firmware**

## 历史

`firmware` 系统引入于 FreeBSD 6.1。二进制固件加载引入于 FreeBSD 15.0。

## 作者

本手册页由 Max Laier <mlaier@FreeBSD.org> 编写。
