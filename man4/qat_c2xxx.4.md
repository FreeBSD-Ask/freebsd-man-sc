# qat_c2xxx.4

`qat_c2xxx` — 适用于 Atom C2000 的 Intel QuickAssist Technology 加密驱动程序

## 名称

`qat_c2xxx`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device crypto
> device cryptodev
> device qat

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
qat_c2xxx_load="YES"
qat_c2xxxfw_load="YES"
```

## 描述

`qat_c2xxx` 驱动程序为 Atom C2000 设备上 Intel QuickAssist (QAT) 设备的部分加密加速功能实现 [crypto(4)](crypto.4.md) 支持。QAT 设备通过 PCIe 枚举，因此可在 pciconf(8) 输出中看到。

`qat_c2xxx` 驱动程序可加速 CBC、CTR 和 GCM 模式下的 AES，并可执行将 CBC 和 CTR 模式与 SHA1-HMAC 和 SHA2-HMAC 结合的认证加密。`qat_c2xxx` 驱动程序还可计算 SHA1 和 SHA2 摘要。AES-GCM 的实现存在固件施加的约束：任何附加认证数据（AAD）的长度不得超过 240 字节。因此，驱动程序会拒绝不满足此约束的 [crypto(9)](../man9/crypto.9.md) 请求。

## 参见

[crypto(4)](crypto.4.md), [ipsec(4)](ipsec.4.md), [pci(4)](pci.4.md), [qat(4)](qat.4.md), [random(4)](random.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`qat_c2xxx` 驱动程序首次出现于 FreeBSD 13.0。

## 作者

`qat_c2xxx` 驱动程序由 Hikaru Abe <hikaru@iij.ad.jp> 为 NetBSD 编写。Mark Johnston <markj@FreeBSD.org> 将其移植到 FreeBSD。

## 缺陷

某些 Atom C2000 QAT 设备具有两个加速引擎而非一个。`qat_c2xxx` 驱动程序目前在两者都启用时行为异常，因此若存在第二个加速引擎，驱动程序不会启用它。
