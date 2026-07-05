# ccr.4

`ccr` — Chelsio T6 加密加速器驱动

## 名称

`ccr`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device ccr
> device cxgbe

要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
ccr_load="YES"
```

## 描述

`ccr` 驱动为基于 Chelsio Terminator 6 ASIC（T6）的 PCI Express 以太网适配器上集成的加密加速引擎提供支持。该驱动为 [crypto(9)](../man9/crypto.9.md) 消费者（如 [ktls(4)](ktls.4.md)、geli(4) 和 [ipsec(4)](ipsec.4.md)）加速 AES-CBC、AES-CCM、AES-CTR、AES-GCM、AES-XTS、SHA1、SHA2-224、SHA2-256、SHA2-384、SHA2-512、SHA1-HMAC、SHA2-224-HMAC、SHA2-256-HMAC、SHA2-384-HMAC 和 SHA2-512-HMAC 操作。该驱动还支持将 AES-CBC、AES-CTR 或 AES-XTS 之一与 SHA1-HMAC、SHA2-224-HMAC、SHA2-256-HMAC、SHA2-384-HMAC 或 SHA2-512-HMAC 之一链接，用于先加密后认证操作。有关进一步的硬件信息和与硬件要求相关的问题，请参见 <http://www.chelsio.com/>。

`ccr` 驱动作为现有 Chelsio NIC 设备的子设备附加，因此需要 [cxgbe(4)](cxgbe.4.md) 驱动处于活动状态。

## 硬件

`ccr` 驱动支持基于 T6 ASIC 的适配器上集成的加密加速引擎：

- Chelsio T6225-CR
- Chelsio T6225-SO-CR
- Chelsio T62100-LP-CR
- Chelsio T62100-SO-CR
- Chelsio T62100-CR

## 支持

有关一般信息和支持，请访问 Chelsio 支持网站：<http://www.chelsio.com/>

如果在使用所支持适配器时发现此驱动存在问题，请将与问题相关的所有具体信息通过电子邮件发送至 <support@chelsio.com>。

## 参见

[crypto(4)](crypto.4.md), [cxgbe(4)](cxgbe.4.md), geli(4), [ipsec(4)](ipsec.4.md), [ktls(4)](ktls.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`ccr` 设备驱动首次出现于 FreeBSD 12.0。

## 作者

`ccr` 驱动由 John Baldwin <jhb@FreeBSD.org> 编写。
