# crypto_session.9

`crypto_session` — 用于对称密码学服务的状态

## 名称

`crypto_session`

## 概要

```c
#include <opencrypto/cryptodev.h>

struct auth_hash *
crypto_auth_hash(const struct crypto_session_params *csp)

struct enc_xform *
crypto_cipher(const struct crypto_session_params *csp)

const struct crypto_session_params *
crypto_get_params(crypto_session_t cses)

int
crypto_newsession(crypto_session_t *cses,
    const struct crypto_session_params *csp, int crid)

int
crypto_freesession(crypto_session_t cses)
```

## 描述

内核中的对称密码学操作与密码学会话关联。会话持有跨多个请求共享的状态。活动会话与单个密码学驱动程序关联。

`crypto_session_t` 类型表示对活动会话的不透明引用。会话对象由密码学框架分配和管理。

新会话由 `crypto_newsession` 创建。`csp` 描述与新会话关联的各种参数，例如要使用的算法和任何会话范围的密钥。`crid` 可用于请求特定的密码学驱动程序或驱动程序类别。对于后一种情况，`crid` 应设置为以下值的掩码：

**`CRYPTOCAP_F_HARDWARE`** 请求硬件驱动程序。硬件驱动程序不使用主机 CPU 执行操作。通常，独立的协处理器异步执行操作。

**`CRYPTOCAP_F_SOFTWARE`** 请求软件驱动程序。软件驱动程序使用主机 CPU 执行操作。内核在 cryptosoft(4) 驱动程序中包含每种受支持算法的简单且可移植的实现。在提供旨在加速密码学操作的指令的架构上，可能还有其他软件驱动程序可用。

如果同时请求硬件和软件驱动程序，则硬件驱动程序优先于软件驱动程序。加速软件驱动程序优先于基线软件驱动程序。如果有多个硬件驱动程序可用，框架将以轮询方式在这些驱动程序之间分发会话。

成功时，`crypto_newsession` 在 `cses` 中保存对新创建会话的引用。

`crypto_freesession` 用于释放与会话 `cses` 关联的资源。

`crypto_auth_hash` 返回描述由 `csp` 请求的认证算法的基线软件实现的结构。如果 `csp` 未指定认证算法或请求了无效算法，则返回 `NULL`。

`crypto_cipher` 返回描述由 `csp` 请求的加密算法的基线软件实现的结构。如果 `csp` 未指定加密算法或请求了无效算法，则返回 `NULL`。

`crypto_get_params` 返回 `cses` 使用的会话参数的指针。

### 会话参数

会话参数用于描述密码学请求执行的密码学操作。参数存储在 `struct crypto_session_params` 的实例中。初始化要传递给 `crypto_newsession` 的参数时，应首先将整个结构清零。然后设置所需字段，将未使用的字段保持为零。此结构包含以下字段：

**`CSP_MODE_COMPRESS`** 压缩或解压缩请求有效载荷。压缩算法在 `csp_cipher_alg` 中指定。

**`CSP_MODE_CIPHER`** 加密或解密请求有效载荷。加密算法在 `csp_cipher_alg` 中指定。

**`CSP_MODE_DIGEST`** 计算或验证请求有效载荷的摘要或哈希。认证算法在 `csp_auth_alg` 中指定。

**`CSP_MODE_AEAD`** 带附加数据的认证加密。解密操作需要摘要或标签，如果不匹配则失败。AEAD 算法在 `csp_cipher_alg` 中指定。

**`CSP_MODE_ETA`** 先加密后认证。在此模式下，加密操作先加密有效载荷，然后对请求的附加认证数据和加密后的有效载荷计算认证摘要。如果提供的摘要不匹配，解密操作将失败而不解密数据。加密算法在 `csp_cipher_alg` 中指定，认证算法在 `csp_auth_alg` 中指定。

**`CSP_F_SEPARATE_OUTPUT`** 支持使用独立输入和输出缓冲区的请求。设置此标志的会话允许使用单个原地修改缓冲区的请求，或使用独立输入和输出缓冲区的请求。未设置此标志的会话仅允许使用单个原地修改缓冲区的请求。

**`CSP_F_SEPARATE_AAD`** 支持对 AAD 使用独立缓冲区的请求，而不是将 AAD 作为输入缓冲区中的一个区域提供。设置此标志的会话允许 AAD 在输入缓冲区的区域中传递，或在单个虚拟连续缓冲区中传递。未设置此标志的会话仅允许 AAD 作为输入缓冲区中的区域传递。

**`CSP_F_ESN`** 支持对 IPsec ESN（扩展序列号）使用独立缓冲区的请求。设置此标志的会话允许 IPsec ESN 在特殊缓冲区中传递。这是"加密并认证"模式支持 IPsec ESN 所需的，其中序列号的高 32 位被附加到 Next Header 之后（RFC 4303）。

**`csp_mode`** 要执行的操作类型。此字段必须设置为以下之一：

**`csp_flags`** 可选驱动程序功能的掩码。仅当驱动程序支持所有请求的功能时，驱动程序才会附加到会话。

**`csp_ivlen`** 如果加密或认证算法需要显式初始化向量（IV）或 nonce，此参数指定以字节为单位的长度。一个会话的所有请求使用相同的 IV 长度。

**`csp_cipher_alg`** 加密或压缩算法。

**`csp_cipher_klen`** 加密或解密密钥的字节长度。一个会话的所有请求使用相同的密钥长度。

**`csp_cipher_key`** 指向加密或解密密钥的指针。如果一个会话的所有请求使用请求特定的密钥，此字段应保持为 `NULL`。此指针和关联的密钥必须在密码学会话的整个持续时间内保持有效。

**`csp_auth_alg`** 认证算法。

**`csp_auth_klen`** 认证密钥的字节长度。如果认证算法不使用密钥，此字段应保持为零。

**`csp_auth_key`** 指向认证密钥的指针。如果一个会话的所有请求使用请求特定的密钥，此字段应保持为 `NULL`。此指针和关联的密钥必须在密码学会话的整个持续时间内保持有效。

**`csp_auth_mlen`** 摘要的字节长度。如果为零，则使用摘要的完整长度。如果非零，则使用摘要的前 `csp_auth_mlen` 字节。

## 返回值

`crypto_newsession` 在发生错误时返回非零值，成功时返回零。

`crypto_auth_hash` 和 `crypto_cipher` 在请求有效时返回 `NULL`，成功时返回指向结构的指针。

## 参见

[crypto(7)](../man7/crypto.7.md), [crypto(9)](crypto.9.md), [crypto_request(9)](crypto_request.9.md)

## 缺陷

`crypto_freesession` 的当前实现不为调用者提供一种方式来了解是否还有其他对会话关联参数中存储密钥的引用。此函数可能应休眠，直到与会话关联的所有正在进行的密码学操作完成。
