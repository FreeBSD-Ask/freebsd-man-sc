# crypto(9)

`crypto` — 内核中密码学服务的 API

## 名称

`crypto`

## 概要

```c
#include <opencrypto/cryptodev.h>
```

## 描述

`crypto` 是一个内核内密码学框架。它允许内核内消费者加密和解密数据，并使用户态应用程序能够通过 **`/dev/crypto`** 设备使用密码学硬件。

`crypto` 支持使用分组密码和流密码进行加密和解密操作，以及计算和验证消息认证码（MAC）。消费者分配会话来描述一种变换，参见 [crypto_session(9)](crypto_session.9.md)。消费者随后分配请求对象来描述每次变换，例如加密一个网络数据包或解密一个磁盘扇区。请求在 [crypto_request(9)](crypto_request.9.md) 中描述。

设备驱动程序负责处理由消费者提交的请求。[crypto_driver(9)](crypto_driver.9.md) 描述了驱动程序向框架注册所使用的接口、框架为促进请求处理而提供的辅助例程，以及驱动程序需要提供的接口。

### 回调

由于消费者可能不与任何进程关联，驱动程序不能 [sleep(9)](sleep.9.md)。框架同样如此。因此，使用回调机制通知消费者某个请求已完成（回调由消费者按每个请求指定）。无论请求是否成功完成，回调都会由框架调用。错误会报告给回调函数。

会话初始化不使用回调，并同步返回错误。

### 会话迁移

操作可能因特定错误码 `EAGAIN` 而失败，指示会话句柄已更改，请求可立即使用新会话重新提交。消费者应将其保存的会话句柄副本更新为 `crp_session` 的值，以便后续请求使用新会话。

### 支持的算法

某些算法的更多细节可参见 [crypto(7)](../man7/crypto.7.md)。

支持以下认证算法：

**`CRYPTO_AES_CCM_CBC_MAC`**
**`CRYPTO_AES_NIST_GMAC`**
**`CRYPTO_BLAKE2B`**
**`CRYPTO_BLAKE2S`**
**`CRYPTO_NULL_HMAC`**
**`CRYPTO_POLY1305`**
**`CRYPTO_RIPEMD160`**
**`CRYPTO_RIPEMD160_HMAC`**
**`CRYPTO_SHA1`**
**`CRYPTO_SHA1_HMAC`**
**`CRYPTO_SHA2_224`**
**`CRYPTO_SHA2_224_HMAC`**
**`CRYPTO_SHA2_256`**
**`CRYPTO_SHA2_256_HMAC`**
**`CRYPTO_SHA2_384`**
**`CRYPTO_SHA2_384_HMAC`**
**`CRYPTO_SHA2_512`**
**`CRYPTO_SHA2_512_HMAC`**

支持以下加密算法：

**`CRYPTO_AES_CBC`**
**`CRYPTO_AES_ICM`**
**`CRYPTO_AES_XTS`**
**`CRYPTO_CAMELLIA_CBC`**
**`CRYPTO_CHACHA20`**
**`CRYPTO_NULL_CBC`**

支持以下带附加数据的认证加密（AEAD）算法：

**`CRYPTO_AES_CCM_16`**
**`CRYPTO_AES_NIST_GCM_16`**
**`CRYPTO_CHACHA20_POLY1305`**

支持以下压缩算法：

**`CRYPTO_DEFLATE_COMP`**

## 文件

**`sys/opencrypto/crypto.c`** 框架的大部分代码

## 参见

[crypto(4)](../man4/crypto.4.md), [ipsec(4)](../man4/ipsec.4.md), [crypto(7)](../man7/crypto.7.md), [crypto_driver(9)](crypto_driver.9.md), [crypto_request(9)](crypto_request.9.md), [crypto_session(9)](crypto_session.9.md), [sleep(9)](sleep.9.md)

## 历史

该密码学框架首次出现于 OpenBSD 2.7，由 Angelos D. Keromytis <angelos@openbsd.org> 编写。

## 缺陷

该框架需要一种机制来确定哪个驱动程序最适合处理与会话关联的特定算法集合。此处需要某种类型的基准测试。
