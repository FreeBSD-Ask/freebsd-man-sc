# simd.7

`simd` — SIMD 增强

## 名称

`simd`

## 描述

在某些架构上，FreeBSD *libc* 提供了常用函数的增强实现，替代了 otherwise 使用的与架构无关的实现。根据架构和函数的不同，函数的增强实现可能始终使用，或者 *libc* 在运行时检测支持哪些 SIMD 指令集扩展并自动选择最合适的实现。在 `amd64` 上，可以使用环境变量 `ARCHLEVEL` 覆盖此机制。

以下架构存在增强函数：

| *FUNCTION* | *AARCH64* | *ARM* | *AMD64* | *I386* | *PPC64* | *RISC-V* |
| --- | --- | --- | --- | --- | --- | --- |
| bcmp | A |  | S1 | S |  |  |
| bcopy | A | S | S | S | SV | S |
| bzero | A | S | S | S |  | S |
| div |  |  | S | S |  |  |
| index | A |  | S1 |  | S |  |
| ldiv |  |  | S | S |  |  |
| lldiv |  |  | S |  |  |  |
| memchr | A |  | S1 |  |  | S |
| memcmp | A | S | S1 | S |  |  |
| memccpy | A |  | S1 |  |  |  |
| memcpy | AM | S | S | S | SV | S |
| memmove | AM | S | S | S | SV |  |
| memrchr | A |  | S1 |  |  |  |
| memset | AM | S | S | S |  | S |
| rindex | A |  | S1 | S |  | S |
| stpcpy | A |  | S1 |  |  |  |
| stpncpy |  |  | S1 |  |  |  |
| strcat | A |  | S1 | S |  |  |
| strchr | A |  | S1 | S |  | S |
| strchrnul | A |  | S1 |  |  | S |
| strcmp | A | S | S1 | S |  |  |
| strcpy | A |  | S1 | S | S2 |  |
| strcspn | S |  | S2 |  |  |  |
| strlcat | A |  | S1 |  |  |  |
| strlcpy | A |  | S1 |  |  |  |
| strlen | A | S | S1 |  |  | S |
| strncat | A |  | S1 |  |  |  |
| strncmp | A | S | S1 | S |  |  |
| strncpy |  |  | S1 |  | S2 |  |
| strnlen | A |  | S1 |  |  | S |
| strrchr | A |  | S1 | S |  | S |
| strpbrk | S |  | S2 |  |  |  |
| strsep | S |  | S2 |  |  |  |
| strspn | S |  | S2 |  |  |  |
| swab |  |  |  | S |  |  |
| timingsafe_bcmp | A |  | S1 |  |  |  |
| timingsafe_memcmp | S |  | S |  |  |  |
| wcschr |  |  |  | S |  |  |
| wcscmp |  |  |  | S |  |  |
| wcslen |  |  |  | S |  |  |
| wmemchr |  |  |  | S |  |  |

**S**：标量（非 SIMD），**1**：amd64 基线，**2**：x86-64-v2 或 PowerPC 2.05，**3**：x86-64-v3，**4**：x86-64-v4，**V**：PowerPC VSX，**A**：Arm ASIMD（NEON），**M**：Arm MOPS。

## 环境变量

**`scalar`** 仅标量增强（无 SIMD）

**`baseline`** cmov, cx8, x87 FPU, fxsr, MMX, osfxsr, SSE, SSE2

**`x86-64-v2`** cx16, lahf/sahf, popcnt, SSE3, SSSE3, SSE4.1, SSE4.2

**`x86-64-v3`** AVX, AVX2, BMI1, BMI2, F16C, FMA, lzcnt, movbe, osxsave

**`x86-64-v4`** AVX-512F/BW/CD/DQ/VL

**`ARCHLEVEL`** 在 *amd64* 上，控制所使用的 SIMD 增强级别。如果此变量设置为下面列表中的某个架构级别，并且处理器支持该架构级别，则使用最高到 `ARCHLEVEL` 的 SIMD 增强。如果 `ARCHLEVEL` 未设置、未被识别或处理器不支持，则使用处理器支持的最高级别 SIMD 增强。`ARCHLEVEL` 中以‘’：或‘+’开头的后缀被忽略，可用于未来扩展。架构级别可以加‘’！前缀以强制使用请求的架构级别，即使处理器未声明支持它。这通常会导致应用程序崩溃，应仅用于测试目的，或在架构级别检测产生不正确结果时使用。架构级别遵循 AMD64 SysV ABI 补充规范：

## 诊断

- Illegal Instruction 如果命令通过传递 `SIGILL` 信号终止，则由 [sh(1)](../man1/sh.1.md) 打印，参见 signal(3)。通过将 `ARCHLEVEL` 设置为以‘’！字符开头的字符串，强制使用不支持的架构级别，导致进程因使用不支持的指令而崩溃。取消设置 `ARCHLEVEL`、删除‘’！前缀或选择支持的架构级别。该消息也可能因无关原因而出现。

## 参见

string(3), [arch(7)](arch.7.md)

> H. J. Lu, Michael Matz, Milind Girkar, Jan Hubi[u010D]ka " (vc, Andreas Jaeger, Mark Mitchell, "AMD64 Architecture Processor Supplement", *System V Application Binary Interface*, 2023 年 5 月 23 日，版本 1.0。

## 历史

特定架构的增强 *libc* 函数从 FreeBSD 2.0 开始为 `i386` 添加，FreeBSD 6.0 为 `arm` 添加，FreeBSD 6.1 为 `amd64` 添加，FreeBSD 11.0 为 `aarch64` 添加，FreeBSD 12.0 为 `powerpc64` 添加，FreeBSD 16.0 为 `riscv64` 添加。SIMD 增强函数首次在 FreeBSD 13.0 中为 `powerpc64` 添加，并在 FreeBSD 14.1 中为 `amd64` 添加。

`simd` 手册页出现于 FreeBSD 14.1。

## 作者

Robert Clausecker <fuz@FreeBSD.org>

## 注意事项

FreeBSD 的其他部分（如内核或 OpenSSL 中的加密例程）也可能使用 SIMD 增强。这些增强不受 `ARCHLEVEL` 变量控制，可能有自己的配置机制。

## 缺陷

在 powerpc64 上无法配置 SIMD 增强的使用。
