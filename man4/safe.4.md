# safe(4)

`safe` — SafeNet SafeXcel 1141/1741 加密加速器

## 名称

`safe`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device crypto
> device cryptodev
> device safe

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
safe_load="YES"
```

`在 sysctl.conf(5) 中：`

> hw.safe.debug
> hw.safe.dump
> hw.safe.rnginterval
> hw.safe.rngbufsize
> hw.safe.rngmaxalarm

## 弃用通知

`safe` 驱动已弃用，计划在 FreeBSD 16.0 中移除。

## 描述

`safe` 驱动支持包含 SafeNet 加密加速器芯片的卡。

`safe` 驱动注册自身以为 [ipsec(4)](ipsec.4.md) 和 [crypto(4)](crypto.4.md) 加速 AES、SHA1-HMAC 和 NULL 操作。

在所有型号上，驱动注册自身以向 [random(4)](random.4.md) 子系统提供随机数据。驱动会定期轮询硬件 RNG 并检索数据供系统使用。如果驱动检测到硬件 RNG 与任何本地信号共振，将重置生成随机数据的振荡器。三个 [sysctl(8)](../man8/sysctl.8.md) 设置控制此过程：`hw.safe.rnginterval` 指定轮询操作之间的时间（以秒为单位），`hw.safe.rngbufsize` 指定每次轮询检索的 32 位字数，`hw.safe.rngmaxalarm` 指定重置振荡器的阈值。

当驱动在编译时定义了 `SAFE_DEBUG`，会提供两个 [sysctl(8)](../man8/sysctl.8.md) 变量用于调试：`hw.safe.debug` 可设置为非零值以对每个加密操作启用向控制台发送调试消息，`hw.safe.dump` 是只写变量，可用于强制将驱动状态发送到控制台。将此变量设置为“`ring`”转储描述符环的当前状态，设置为“`dma`”转储硬件 DMA 寄存器，或设置为“`int`”转储硬件中断寄存器。

## 硬件

`safe` 驱动支持以下 SafeXcel 芯片：

支持 DES、Triple-DES、AES、MD5 和 SHA-1 对称加密操作、RNG、公钥操作和完整 IPsec 数据包处理。

| SafeNet 1141 | 原始芯片组。 |
| ------------ | ------------ |
| SafeNet 1741 | 1141 的更快版本。 |

## 参见

crypt(3), [crypto(4)](crypto.4.md), [intro(4)](intro.4.md), [ipsec(4)](ipsec.4.md), [random(4)](random.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`safe` 驱动最早出现于 FreeBSD 5.2。在 FreeBSD 15.0 中弃用，在 FreeBSD 16.0 中移除。

## 缺陷

未实现公钥支持。
