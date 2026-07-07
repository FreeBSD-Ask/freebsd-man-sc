# kmsan(9)

`KMSAN` — 内核内存消毒器

## 名称

`KMSAN`

## 概要

GENERIC-KMSAN 内核配置可用于以 GENERIC 为基础配置编译启用 KMSAN 的内核。或者，要将 KMSAN 编译进内核，请将以下行放入你的内核配置文件中：

> options KMSAN

```c
#include <sys/msan.h>

void
kmsan_mark(const void *addr, size_t size, uint8_t code)

void
kmsan_orig(const void *addr, size_t size, int type, uintptr_t pc)

void
kmsan_check(const void *addr, size_t size, const char *descr)

void
kmsan_check_bio(const struct bio *, const char *descr)

void
kmsan_check_ccb(const union ccb *, const char *descr)

void
kmsan_check_mbuf(const struct mbuf *, const char *descr)

void
kmsan_check_uio(const struct uio *, const char *descr)
```

## 描述

`KMSAN` 是一个利用编译器插桩检测内核中未初始化内存使用的子系统。目前仅在 amd64 和 arm64 平台上实现。

当 `KMSAN` 编译进内核时，编译器被配置为在内存访问之前发出函数调用。这些函数由 `KMSAN` 运行时组件实现，使用隐藏的字节粒度影子状态来确定源操作数是否已初始化。当未初始化内存用作某些操作（如控制流表达式或内存访问）的源操作数时，运行时报告错误。否则，影子状态传播到目标操作数。例如，复制未初始化内存的变量赋值或 `memcpy` 调用将导致目标缓冲区或变量被标记为未初始化。

为报告错误，`KMSAN` 运行时将根据 `debug.kmsan.panic_on_violation` sysctl 的值触发内核崩溃或向控制台打印消息。在两种情况下，都包含堆栈跟踪和有关未初始化内存来源的信息。

除编译器检测的未初始化内存使用外，各种内核 I/O “出口点”（如 copyout(9)）执行输入影子状态的验证，如果检测到任何未初始化字节将引发错误。

`KMSAN` 选项带来显著的性能损失。内核代码通常运行速度慢两到三倍，内核映射中的每个字节需要两字节的影子状态。因此，`KMSAN` 应仅用于内核测试和开发。不建议在物理 RAM 少于 8GB 的系统上启用 `KMSAN`。

KMSAN 配置的内核中的消毒器可通过设置 loader 可调参数 `debug.kmsan.disable=1` 禁用。

## 函数

`kmsan_mark` 和 `kmsan_orig` 函数更新 `KMSAN` 影子状态。`kmsan_mark` 根据 `code` 参数的值将地址范围标记为有效或无效。此参数的有效值为 `KMSAN_STATE_INITED` 和 `KMSAN_STATE_UNINIT`，分别将范围标记为已初始化和未初始化。例如，当一块内存被释放到内核分配器时，通常已被标记为已初始化；在内存被重用于新分配之前，分配器应将其标记为未初始化。作为另一个例子，设备执行的对主机内存的写入（例如通过 DMA）不被消毒器拦截；为避免误报，驱动程序应将设备写入的内存标记为已初始化。对于许多驱动程序，这由 busdma(9) 子系统内部处理。

`kmsan_orig` 函数更新 “origin” 影子状态。特别地，它将给定的未初始化缓冲区与内存类型和代码地址关联。这由 `KMSAN` 运行时用于跟踪未初始化内存的来源，仅用于调试目的。更多细节参见实现说明。

`kmsan_check` 函数及其子类型兄弟函数验证作为输入参数传递的内核内存区域的影子状态。如果输入的任何字节被标记为未初始化，运行时将生成报告。这些函数在调试期间很有用，因为它们可以策略性地插入到代码路径中以缩小未初始化内存的来源范围。它们还用于在各种内核 I/O 路径中执行验证，帮助确保例如通过网络传输的数据包不包含未初始化的内核内存。`kmsan_check` 及相关函数还接受一个 `descr` 参数，该参数插入到检查引发的任何报告中。

## 实现说明

### 影子映射

`KMSAN` 运行时使用内核映射的两个影子。内核映射中的每个地址与两个影子中的地址有线性映射。第一个简称为影子映射，跟踪相应内核内存的状态。影子映射中的非零字节指示相应的内核内存字节未初始化。`KMSAN` 插桩在内核内存内容被转换和复制时自动传播影子状态。

第二个影子称为 origin 映射，仅用于帮助调试消毒器的报告。为避免误报，`KMSAN` 不会对未初始化内存的某些操作（如复制或算术）引发报告。因此，对引发报告的未初始化状态的操作可能远离错误源，使调试复杂化。origin 映射包含可帮助定位特定 `KMSAN` 报告根本原因的信息；生成报告时，运行时使用 origin 映射中的状态提供额外细节。

与影子映射不同，origin 映射不是字节粒度的，而是由 4 字节 “单元” 组成。每个单元描述映射的内核内存的相应四个字节，并保存类型和压缩的代码地址。当为某目的分配内核内存时，其 origin 由编译器插桩或分配器中的运行时钩子初始化。类型指示特定的分配器，例如 uma(9)，地址提供分配内存的内核代码位置。

### 汇编代码

当配置 `KMSAN` 时，编译器仅为 C 代码发出插桩。包含汇编代码的文件不被插桩。在某些情况下，这由消毒器运行时处理，它为汇编实现的子例程定义包装器。这些包装器称为拦截器，处理更新影子状态以反映原始子例程执行的操作。在其他情况下，调用汇编代码或被汇编代码调用的 C 代码可能需要使用 `kmsan_mark` 手动更新影子状态。这通常仅在机器相关代码中必要。

内联汇编由编译器插桩以根据代码的输出操作数更新影子状态，因此通常不需要任何特殊处理来避免误报。

### 中断和异常

除影子映射外，消毒器需要一些线程本地存储（TLS）来跟踪函数参数和返回值的初始化和 origin 状态。消毒器插桩将自动获取、更新和验证此状态。特别地，此存储块具有由消毒器 ABI 定义的布局。

大多数内核代码在中断或异常可能将 CPU 重定向到开始执行无关代码的上下文中运行。为确保线程本地的消毒器状态保持一致，运行时为每个线程维护一个 TLS 块栈。当机器相关的中断和异常处理程序开始执行时，它们在调用任何 C 代码之前向栈压入新条目，在恢复执行被中断代码之前弹出栈。这些操作由消毒器运行时中的 `kmsan_intr_enter` 和 `kmsan_intr_leave` 函数执行。

## 实例

以下人为示例演示了 `KMSAN` 自动检测的一些错误类型：

```c
int
f(size_t osz)
{
	struct {
		uint32_t bar;
		uint16_t baz;
		/* 这里有一个 2 字节的洞。 */
	} foo;
	char *buf;
	size_t sz;
	int error;
	/*
	 * 这将引发报告，因为 "sz" 在此处未初始化。
	 * 如果它已初始化，而 "osz" 被调用者留下未初始化，
	 * 也会引发报告。
	 */
	if (sz < osz)
		return (1);
	buf = malloc(32, M_TEMP, M_WAITOK);
	/*
	 * 这将引发报告，因为 "buf" 未初始化，
	 * 包含该内存上次使用后遗留的数据。
	 */
	for (i = 0; i < 32; i++)
		if (buf[i] != ' ')
			foo.bar++;
	foo.baz = 0;
	/*
	 * 这将引发报告，因为 "foo" 中的填充字节未初始化
	 * （例如通过 memset()），此调用将把未初始化的
	 * 内核栈内存复制到用户态。
	 */
	copyout(&foo, uaddr, sizeof(foo));
	/*
	 * 此行本身不会引发报告，但可能根据返回值的使用方式
	 * 在调用者中触发报告。
	 */
	return (error);
}
```

## 参见

[build(7)](../man7/build.7.md), busdma(9), copyout(9), KASAN(9), [uio(9)](uio.9.md), uma(9)

> Evgeniy Stepanov, Konstantin Serebryany, "MemorySanitizer: fast detector of uninitialized memory use in C++", *2015 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*, 2015.

## 历史

`KMSAN` 从 NetBSD 移植，首次出现于 FreeBSD 14.0。

## 缺陷

`KMSAN` 运行时忽略对内核映射之外的内核内存的访问。特别地，通过直接映射的内存访问不被验证。当内存从内核映射之外复制到内核映射时，该内核映射区域被标记为已初始化。当配置 `KMSAN` 时，内核内存分配器被配置为使用内核映射，文件系统被配置为始终将数据缓冲区映射到内核映射，从而尽量减少直接映射的使用。但是，仍存在一些直接映射的使用。这是一种旨在避免误报的保守策略，但它会掩盖某些内核子系统中的错误。

在 amd64 上，全局变量和物理页数组 `vm_page_array` 不被消毒。这是故意的，因为通过避免创建内核映射大区域的影子来减少内存使用。但是，这可能使 `KMSAN` 无法检测到错误。

某些内核内存分配器提供类型稳定的对象，使用它们的代码经常依赖对象数据在多次分配之间保留。此类分配无法由 `KMSAN` 消毒。但是，在某些情况下，可使用 `kmsan_mark` 手动注释已知在分配时包含无效数据的字段。
