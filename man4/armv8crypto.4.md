# armv8crypto(4)

`armv8crypto` — ARM CPU 上 AES 加速器驱动

## 名称

`armv8crypto`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device crypto
> device armv8crypto

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
armv8crypto_load="YES"
```

## 描述

从 ARMv8 架构开始，ARM Limited 加入了可选的密码学指令，以加速 AES、SHA-1、SHA-2 和有限域算术运算。

处理器能力在引导时以 Instruction Set Attributes 0 行中的 AES 形式报告。`armv8crypto` 驱动不会在缺乏所需 CPU 能力的系统上挂载。

`armv8crypto` 驱动注册自身以为 [crypto(4)](crypto.4.md) 加速 AES 操作。

## 参见

crypt(3), [crypto(4)](crypto.4.md), [intro(4)](intro.4.md), [ipsec(4)](ipsec.4.md), [random(4)](random.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`armv8crypto` 驱动首次出现于 FreeBSD 11.0。

## 作者

`armv8crypto` 驱动由 Andrew Turner <andrew@FreeBSD.org> 编写。
