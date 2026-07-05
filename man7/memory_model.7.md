# memory_model.7

`memory` — 内存模型概述

## 名称

`memory`

## 描述

描述 FreeBSD 实现的内存模型。

### 简介

本文档涵盖 FreeBSD 支持的体系结构、编译器和语言运行时所实现的内存模型的各个方面。某些方面目前在其他地方有文档记录，特别是在 [atomic(9)](../man9/atomic.9.md) 中。

### 指针来源

表面上看，指针是（通常为虚拟）地址空间内的整数地址。在系统编程语言中，指针还具有来源（provenance），指示指针在何处以及何时可以访问内存。编译器使用来源信息执行别名分析以支持优化。

在 CHERI 目标上，能力的边界、权限和有效性标签使来源的某些方面具体化。CHERI 能力只能从其他能力派生，并受单调性保证的约束。具体而言，对 CHERI 能力的任何操作都不能产生比原始能力权限更多的能力。

开发者必须注意确保不会无意中丢失指针来源。具体而言：

- 在复制或操作指针时，使用指针类型（如 `char *`）、`intptr_t` 或 `uintptr_t` 来保留来源。其他整数类型不保留来源。
- 确保使用 `intptr_t` 或 `uintptr_t` 的表达式具有单一、清晰的来源。例如，当添加两个 `intptr_t` 类型的变量时，将作为偏移量的那个转换为 `size_t`。
- 确保指针以其自然对齐方式存储。这是 CHERI 所要求的，通过未正确对齐的指针访问对象在 C 中是未定义行为。
- 当需要指针的地址而不需要来源时，将指针转换为无来源的类型，如 `ptraddr_t`。
- 避免操作指针地址使其落在底层分配之外，但 ISO C 允许的越过末尾一个位置除外。将指针进一步移出边界（即使暂时地）在 C 标准中是未定义行为。在实践中，CHERI 能力可以超出边界一定距离，但如果超出边界太远，有效性标签将被剥离。

开发者还必须注意不要让有效指针跨越地址空间边界泄露。具体而言：

- 使用保留来源的 API 复制包含指针的对象，例如：copyinptr(9)、copyoutptr(9)、memcpy(3) 和 memmove(3)。
- 使用不保留来源的 API 复制不应包含指针的对象，例如：copyin(9)、copyout(9)、memcpy_data(9) 和 memmove_data(9)。

关于适配 CHERI C/C++ 来源概念的实际建议，请参见 <https://ctsrd-cheri.github.io/cheri-c-programming/> CHERI C/C++ 编程指南。C 的来源感知内存对象模型记录在 ISO/IEC TS 6010:2025：《编程语言——C 的来源感知内存对象模型》中，可以以草案形式作为 WG14 文件 <https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3057.pdf> N3057 阅读。关于系统编程语言中来源的更多背景信息可在 Rust RFC <https://rust-lang.github.io/rfcs/3559-rust-has-provenance.html> 3559-rust-has-provenance 中找到。

## 参见

[arch(7)](arch.7.md), [atomic(9)](../man9/atomic.9.md)

## 作者

该软件和本手册页由 Capabilities Limited 开发，资金来自 Innovate UK 和科学、创新与技术部，用于在项目 10168042（"CheriBSD feature extraction, maturity, and testing"）下采用和推广 CHERI 技术。
