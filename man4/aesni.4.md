# aesni(4)

`aesni` — x86 CPU AES 和 SHA 加密加速驱动

## 名称

`aesni`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device crypto
> device cryptodev
> device aesni

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
aesni_load="YES"
```

## 描述

从 Intel Westmere 和 AMD Bulldozer 开始，一些 x86 处理器实现了一组称为 AESNI 的新指令。这六条指令加速了高级加密标准（AES）对称密码的 128、192 和 256 位密钥长度密钥调度计算，并提供了常规和最后一轮加密/解密的硬件实现。

处理器能力在引导时的 Features2 行中报告为 AESNI。

从 Intel Goldmont 和 AMD Ryzen 微架构开始，一些 x86 处理器实现了一组新的 SHA 指令。这七条指令加速了 SHA1 和 SHA256 哈希的计算。

处理器能力在引导时的 Structured Extended Features 行中报告为 SHA。

`aesni` 驱动不会在缺少这两种 CPU 能力的系统上附加。在仅支持 AESNI 或 SHA 扩展之一的系统上，驱动将附加并支持该功能。

`aesni` 驱动注册自身以加速 [crypto(4)](crypto.4.md) 的 AES 和 SHA 操作。除了速度之外，使用 `aesni` 驱动的优势在于 AESNI 操作与数据无关，从而消除了基于测量缓存使用和时间的某些攻击向量，这些攻击通常存在于基于表驱动的实现中。

## 参见

crypt(3), [crypto(4)](crypto.4.md), [intro(4)](intro.4.md), [ipsec(4)](ipsec.4.md), [padlock(4)](padlock.4.md), [random(4)](random.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`aesni` 驱动最早出现在 FreeBSD 9.0 中。SHA 支持在 FreeBSD 12.0 中添加。

## 作者

`aesni` 驱动由 Konstantin Belousov <kib@FreeBSD.org> 和 Conrad Meyer <cem@FreeBSD.org> 编写。密钥调度计算代码采用自 Intel 提供的示例，并用于 OpenBSD 的类似驱动。哈希步骤内联函数实现由 Intel 提供。
