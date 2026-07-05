# ossl.4

`ossl` — 使用 OpenSSL 汇编例程的驱动

## 名称

`ossl`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device crypto
> device cryptodev
> device ossl

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ossl_load="YES"
```

## 描述

OpenSSL 发行版包含一些常用加密算法的架构特定实现。此驱动为这些例程提供了一个包装器，使其能被内核加密消费者（如内核 TLS 和 IPsec）使用。

`ossl` 驱动包含以下架构的特定实现：

- arm64
- amd64
- i386

`ossl` 驱动支持以下算法：

- AES-CBC
- AES-GCM（仅 amd64）
- ChaCha20
- ChaCha20-Poly1305（RFC 8439）
- Poly1305
- SHA1
- SHA1-HMAC
- SHA2-224
- SHA2-224-HMAC
- SHA2-256
- SHA2-256-HMAC
- SHA2-384
- SHA2-384-HMAC
- SHA2-512
- SHA2-512-HMAC

## 参见

[crypto(4)](crypto.4.md), [intro(4)](intro.4.md), [ipsec(4)](ipsec.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`ossl` 驱动最早出现于 FreeBSD 13.0。
