# exterror.9

`exterror` — 向用户态提供扩展错误信息

## 名称

`exterror`

## 概要

```c
#define	EXTERR_CATEGORY EXTERR_CAT_MYCATEGORY

#include <sys/exterrvar.h>

struct kexterr;

void
exterr_clear(struct kexterr *ke)

int
exterr_set_from(const struct kexterr *ke)

int
EXTERROR(int error, const char *msg, ...)

void
EXTERROR_KE(struct kexterr *ke, int error, const char *msg, ...)
```

## 描述

`exterror` 框架允许内核在标准的 errno(3) 错误码之外，返回关于错误的附加信息。errno 错误码简洁但往往缺少上下文。

这种简洁性在 `EINVAL` 或 `EIO` 等常用且含义重载的错误码上尤为明显，它们在某个系统调用的许多位置都会出现，甚至在当前内核调用的上下文之外也会出现。仅使用 `errno` 值来识别返回错误的具体原因，需要搜索内核中返回该错误的所有实例，并尝试猜测最有可能返回该错误的代码路径。`exterror` 将附加数据附加到错误本身，并记录错误类别和内核源代码文件行号。`exterror` 的目的是使用户更容易识别错误的原因。

## 用法

在给定的源 `.c` 文件中使用 `exterror` 之前，应在以下文件中分配扩展错误类别：

```c
#include <sys/exterr_cat.h>
```

该类别是一个唯一的整数，与源代码行号一起唯一标识扩展错误的发生位置。然后，应将 `EXTERR_CATEGORY` 符号定义为所分配类别的别名，如概要中所示。

报告错误的典型代码片段仅为：

```c
return (EINVAL);
```

扩展错误可以为错误码附加额外信息：

```c
return (EXTERROR(EINVAL, "Invalid length"));
```

错误数据和元数据保存在当前线程的存储中。元数据包括类别和源文件行号。

`EXTERROR` 宏的参数：

- `EXTERROR` 的第一个参数是 errno 错误码。
- 第二个参数是具有无界生存期的常量字符串，应简洁地提供关于该错误的足够人类可读细节。
- `EXTERROR` 宏可接受两个可选的 64 位整数参数，其含义特定于子系统。格式字符串可包含最多两个类似 printf 的格式说明符，用于在用户输出中插入可选参数值，此操作在用户态完成。格式说明符必须用于整数类型，并包含“j”格式修饰符以仅接受 `intmax_t` 或 `uintmax_t` 类型。

作为第二个参数传递的字符串仅在内核配置中启用 `option EXTERR_STRINGS` 时保留在内核文本中。否则，它们在编译时被剥离，运行时不可用于用户态。

`EXTERROR` 宏可用于当前线程已定义的任何上下文中。具体而言，`EXTERROR` 不能用于中断上下文和上下文切换代码。此外，在内核线程中使用 `EXTERROR` 没有意义，因为不存在可检索扩展错误数据的用户态。

`EXTERROR_KE` 宏类似于 `EXTERROR`，但它接受一个指向 `struct kexterr` 的显式指针 `kep`，用以填充扩展错误信息。该宏表达式的值为 `void`。异步 I/O 错误设施的描述见下文。

`exterr_clear` 函数清除参数 `ke` 所指向的 `struct kexterr` 的内容。

`exterr_set_from` 函数从参数 `ke` 所指向的 `struct kexterr` 设置当前线程的扩展错误数据。

## 用户态对扩展错误数据的访问

在非错误情况下使用 `exterror` 没有系统调用开销。当发生已提供扩展信息的错误时，内核将该信息复制到向内核注册的用户态每线程区域中，通常在映像激活时或稍后在线程启动时注册。该区域由 exterrctl(2) 内部系统调用控制，通常由用户态 C 运行时完成。

用户态程序无需直接访问扩展信息区域。不存在针对特定错误条件稳定的字段。相反，基础 C 库函数 err(3) 和 warn(3) 已被修改，在通常的 `errno` 解码之外，如果扩展信息可用则一并打印。

## 异步输入/输出

由于 FreeBSD I/O 子系统的特性，大多数输入/输出请求（以缓冲区形式如 `struct buf` 和 geom bio 如 `struct bio` 呈现）在文件系统和 geom 私有线程中异步处理。这使得将扩展错误信息从错误通常发生的 geom 提供者和驱动程序传递回发起请求并消费结果的线程变得具有挑战性。

为缓解这种不匹配，`struct buf` 和 `struct bio` 都有 `struct kexterr` 类型的成员。对于缓冲区，`struct buf` 的成员为 `b_exterr`，`struct bio` 的成员为 `bio_exterr`。异步 I/O 代码可使用 `EXTERROR_KE` 宏，传递指向当前请求内嵌 `struct kexterr` 的指针来记录扩展错误。在这两种情况下，都应设置 `BIO_EXTERR` 标志以指示整个扩展错误有效，而不仅仅是 `b_error` 或 `bio_error` 值。

VFS 和 geom 通用层，以及若干从原始请求生成下级 bio 的 geom 提供者，都了解扩展错误。它们将 `kexterr` 从失败的请求传回创建该请求的线程。

## 参见

errno(3), err(3), uexterr_gettext(3)

## 历史

`exterror` 机制引入于 FreeBSD 15.0。
