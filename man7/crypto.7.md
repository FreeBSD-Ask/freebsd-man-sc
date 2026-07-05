# crypto.7

`crypto` — OpenCrypto 算法

## 名称

`crypto`

## 描述

内核内 OpenCrypto 框架支持多种不同的加密和认证算法。本文档描述这些算法的参数和要求。除非另有说明，下文列出的所有尺寸均以字节为单位。

### 认证器

认证器对字节输入计算值（也称为摘要、哈希或标签）。内核内请求可以计算给定输入的值，或验证给定标签是否与给定输入的计算标签匹配。支持以下认证算法：

AES-CCM 的仅认证模式

Galois 消息认证码

Blake2b

Blake2s

IPsec NULL HMAC

Poly1305 认证器

RIPE 消息摘要-160

RIPE 消息摘要-160 HMAC

SHA-1

SHA-1 HMAC

SHA-2 224

SHA-2 224 HMAC

SHA-2 256

SHA-2 256 HMAC

SHA-2 384

SHA-2 384 HMAC

SHA-2 512

SHA-2 512 HMAC

| **名称** | **Nonce** | **密钥尺寸** | **摘要** | **描述** |
| --- | --- | --- | --- | --- |
| `CRYPTO_AES_CCM_CBC_MAC` | 12 | 16, 24, 32 | 16 | |
| `CRYPTO_AES_NIST_GMAC` | 12 | 16, 24, 32 | 16 | |
| `CRYPTO_BLAKE2B` | | 0, 64 | 64 | |
| `CRYPTO_BLAKE2S` | | 0, 32 | 32 | |
| `CRYPTO_NULL_HMAC` | | | 12 | |
| `CRYPTO_POLY1305` | | 32 | 16 | |
| `CRYPTO_RIPEMD160` | | | 20 | |
| `CRYPTO_RIPEMD160_HMAC` | | 64 | 20 | |
| `CRYPTO_SHA1` | | | 20 | |
| `CRYPTO_SHA1_HMAC` | | 64 | 20 | |
| `CRYPTO_SHA2_224` | | | 28 | |
| `CRYPTO_SHA2_224_HMAC` | | 64 | 28 | |
| `CRYPTO_SHA2_256` | | | 32 | |
| `CRYPTO_SHA2_256_HMAC` | | 64 | 32 | |
| `CRYPTO_SHA2_384` | | | 48 | |
| `CRYPTO_SHA2_384_HMAC` | | 128 | 48 | |
| `CRYPTO_SHA2_512` | | | 64 | |
| `CRYPTO_SHA2_512_HMAC` | | 128 | 64 | |

### 分组密码

OCF 中的分组密码只能对长度为密码块尺寸的精确倍数的消息操作。OCF 支持以下分组密码：

AES-CBC

AES-XTS

Camellia CBC

IPsec NULL 密码

| **名称** | **IV 尺寸** | **块尺寸** | **密钥尺寸** | **描述** |
| --- | --- | --- | --- | --- |
| `CRYPTO_AES_CBC` | 16 | 16 | 16, 24, 32 | |
| `CRYPTO_AES_XTS` | 8 | 16 | 32, 64 | |
| `CRYPTO_CAMELLIA_CBC` | 16 | 16 | 16, 24, 32 | |
| `CRYPTO_NULL_CBC` | 0 | 4 | 0-256 | |

`CRYPTO_AES_XTS` 实现了 NIST SP 800-38E 中定义的带密文窃取的 XEX 可调分组密码。OCF 使用者提供 IV 的前 8 字节。其余 8 字节定义为从 0 开始的块计数器。

注意：并非所有后端都实现了密文窃取部分，因此此密码要求输入是块尺寸的倍数。

### 流密码

流密码可以对任意长度的消息操作。OCF 支持以下流密码：

AES 计数器模式

ChaCha20

| **名称** | **IV 尺寸** | **密钥尺寸** | **描述** |
| --- | --- | --- | --- |
| `CRYPTO_AES_ICM` | 16 | 16, 24, 32 | |
| `CRYPTO_CHACHA20` | 16 | 16, 32 | |

每个请求的 IV 必须通过 `CRYPTO_F_IV_SEPARATE` 标志在 `crp_iv` 中提供。

`CRYPTO_AES_ICM` 将整个 IV 用作 128 位大端块计数器。IV 设置消息的初始计数器值。如果使用者希望使用值分为独立 nonce 和计数器字段的 IV（例如 IPsec），使用者负责拆分请求以处理计数器回绕。

`CRYPTO_CHACHA20` 接受 16 字节 IV。前 8 字节用作 nonce。后 8 字节用作 64 位小端块计数器。

### 带关联数据的认证加密算法

OCF 中的 AEAD 算法将流密码与认证算法结合，同时提供保密性和认证。AEAD 算法除了密文或明文外还接受附加认证数据（AAD）。AAD 以特定 AEAD 算法定义的方法作为输入传递给认证算法。

OCF 中的 AEAD 算法接受一个 nonce，与算法定义的计数器组合以构造底层流密码的 IV。此 nonce 必须通过 `CRYPTO_F_IV_SEPARATE` 标志在 `crp_iv` 中提供。某些 AEAD 算法支持多种 nonce 尺寸。列出的第一个尺寸是默认 nonce 尺寸。

支持以下 AEAD 算法：

AES Galois/Counter 模式

AES 带 CBC-MAC 的计数器模式

ChaCha20-Poly1305

XChaCha20-Poly1305

| **名称** | **Nonce** | **密钥尺寸** | **标签** | **描述** |
| --- | --- | --- | --- | --- |
| `CRYPTO_AES_NIST_GCM_16` | 12 | 16, 24, 32 | 16 | |
| `CRYPTO_AES_CCM_16` | 12, 7-13 | 16, 24, 32 | 16 | |
| `CRYPTO_CHACHA20_POLY1305` | 12, 8 | 32 | 16 | |
| `CRYPTO_XCHACHA20_POLY1305` | 24 | 32 | 16 | |

## 参见

[crypto(4)](../man4/crypto.4.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`crypto` 手册页首次出现于 FreeBSD 10.1。
