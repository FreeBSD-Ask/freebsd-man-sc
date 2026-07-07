# padlock(4)

`padlock` — VIA 和 Zhaoxin CPU 加密驱动

## 名称

`padlock`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device crypto
> device padlock

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
padlock_load="YES"
```

## 描述

VIA 的 C3 和 Eden 处理器系列包含 AES 的硬件加速。C7 系列包含 AES、SHA1、SHA256 和 RSA 的硬件加速。上述所有处理器系列都包含一个硬件随机数发生器。

`padlock` 驱动注册自身以加速 [crypto(4)](crypto.4.md) 的 AES 操作，以及在可用时加速 HMAC/SHA1 和 HMAC/SHA256。它还注册自身以加速其他 HMAC 算法，尽管这些算法没有硬件加速。这只是为了使 `padlock` 能与 [ipsec(4)](ipsec.4.md) 协同工作。

硬件随机数发生器为内核 [random(4)](random.4.md) 子系统提供数据。

## 硬件

`padlock` 驱动支持以下设备中的 AES、RNG、RSA、SHA-1 和 SHA-2 引擎：

- Via Technologies Nano X2、Nano、C7、C3 和 Eden CPU
- 部分 Zhaoxin CPU

## 参见

crypt(3), [crypto(4)](crypto.4.md), [intro(4)](intro.4.md), [ipsec(4)](ipsec.4.md), [random(4)](random.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`padlock` 驱动最早出现于 OpenBSD。第一个包含它的 FreeBSD 版本是 FreeBSD 6.0。

## 作者

带 AES 加密支持的 `padlock` 驱动由 Jason Wright <jason@OpenBSD.org> 编写。它被移植到 FreeBSD，并由 Pawel Jakub Dawidek <pjd@FreeBSD.org> 扩展以支持 SHA1 和 SHA256。本手册页由 Christian Brueffer <brueffer@FreeBSD.org> 编写。
