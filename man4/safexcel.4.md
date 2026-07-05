# safexcel.4

`safexcel` — Inside Secure SafeXcel-IP-97 加密卸载引擎

## 名称

`safexcel`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device crypto
> device cryptodev
> device safexcel

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
safexcel_load="YES"
```

## 描述

`safexcel` 驱动为某些 Marvell 片上系统中的 EIP-97 设备的加密加速功能实现 [crypto(4)](crypto.4.md) 支持。该驱动可加速以下 AES 模式：

- AES-CBC
- AES-CTR
- AES-XTS
- AES-GCM
- AES-CCM

`safexcel` 还实现了 SHA1 和 SHA2 变换，并可将 AES-CBC 和 AES-CTR 与 SHA1-HMAC 和 SHA2-HMAC 组合用于先加密后验证操作。

## 硬件

`safexcel` 驱动支持某些 Marvell 片上系统中的 Inside Secure EIP-97 设备的加密加速功能。

## 参见

[crypto(4)](crypto.4.md), [ipsec(4)](ipsec.4.md), [random(4)](random.4.md), [crypto(7)](../man7/crypto.7.md), geli(8), [crypto(9)](../man9/crypto.9.md)

## 历史

`safexcel` 驱动最早出现于 FreeBSD 13.0。
