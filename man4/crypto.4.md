# crypto.4

`crypto` — 用户态访问硬件加速密码学

## 名称

`crypto`, `cryptodev`

## 概要

`device crypto device cryptodev`

`#include <sys/ioctl.h>`

`#include <sys/time.h>`

`#include <crypto/cryptodev.h>`

## 描述

`cryptodev` 驱动使用户态应用程序能够访问由 [crypto(9)](../man9/crypto.9.md) 内核接口实现的硬件加速密码学变换。

**/dev/crypto** 特殊设备提供基于 ioctl(2) 的接口。用户态应用程序打开该特殊设备，然后对该描述符发出 ioctl(2) 调用。对 **/dev/crypto** 的用户态访问由 `kern.cryptodevallowsoft` [sysctl(8)](../man8/sysctl.8.md) 变量控制。如果此变量为零，则用户态会话仅允许使用密码学协处理器。

## 工作原理

使用该设备需要执行以下基本步骤：

- 打开 **/dev/crypto** 设备。
- 使用 `CIOCGSESSION` 或 `CIOCGSESSION2` 创建会话。应用程序至少需要一个对称会话。由于加密和 MAC 密钥与会话绑定，许多应用程序需要更多会话。
- 使用 `CIOCCRYPT` 或 `CIOCCRYPTAEAD` 同步提交请求。
- 可选地使用 `CIOCFSESSION` 销毁会话。
- 关闭 **/dev/crypto** 设备。这将自动关闭与该文件描述符关联的所有剩余会话。

## 对称密钥操作

`cryptodev` 为传统对称密钥加密（或保密）算法、带密钥和不带密钥的单向哈希（HMAC 和 MAC）算法、先加密后认证（ETA）融合操作以及带附加数据的认证加密（AEAD）操作提供基于上下文的 API。对于 ETA 操作，驱动程序对数据单次遍历同时执行保密算法和完整性校验算法：可以是融合的加密/HMAC 生成操作，也可以是融合的 HMAC 验证/解密操作。类似地，对于 AEAD 操作，驱动程序执行加密/MAC 生成操作或 MAC 验证/解密操作。

所使用的算法和密钥在创建会话时指定。单个请求可以指定每次请求的初始化向量或 nonce。

### 算法

有关支持的算法列表，请参见 [crypto(7)](../man7/crypto.7.md)。

### ioctl 请求描述

```sh
struct crypt_find_op {
    int     crid;       /* 驱动 ID + 标志 */
    char    name[32];   /* 设备/驱动名称 */
};
```

```sh
struct session_op {
    uint32_t cipher;	/* 例如 CRYPTO_AES_CBC */
    uint32_t mac;	/* 例如 CRYPTO_SHA2_256_HMAC */
    uint32_t keylen;	/* 加密密钥 */
    const void *key;
    int mackeylen;	/* MAC 密钥 */
    const void *mackey;
    uint32_t ses;	/* 返回：会话编号 */
};
```

```sh
struct session2_op {
    uint32_t cipher;	/* 例如 CRYPTO_AES_CBC */
    uint32_t mac;	/* 例如 CRYPTO_SHA2_256_HMAC */
    uint32_t keylen;	/* 加密密钥 */
    const void *key;
    int mackeylen;	/* MAC 密钥 */
    const void *mackey;
    uint32_t ses;	/* 返回：会话编号 */
    int	crid;		/* 驱动 ID + 标志（读写） */
    int ivlen;		/* nonce/IV 长度 */
    int maclen;		/* MAC/标签长度 */
    int	pad[2];		/* 供未来扩展使用 */
};
```

```sh
struct crypt_op {
    uint32_t ses;
    uint16_t op;	/* 例如 COP_ENCRYPT */
    uint16_t flags;
    u_int len;
    const void *src;
    void *dst;
    void *mac;		/* 必须足够大以容纳结果 */
    const void *iv;
};
```

```sh
struct crypt_aead {
    uint32_t ses;
    uint16_t op;	/* 例如 COP_ENCRYPT */
    uint16_t flags;
    u_int len;
    u_int aadlen;
    u_int ivlen;
    const void *src;
    void *dst;
    const void *aad;	/* 附加认证数据 */
    void *tag;		/* 必须能容纳所选的 TAG 长度 */
    const void *iv;
};
```

**`CIOCFINDDEV`** `struct crypt_find_op *fop` 如果 `crid` 为 -1，则查找名为 `name` 的驱动并在 `crid` 中返回其 ID。如果 `crid` 不为 -1，则在 `name` 中返回具有该 `crid` 的驱动名称。无论哪种情况，如果未找到驱动，则返回 `ENOENT`。

**`CIOCGSESSION`** `struct session_op *sessp` 在设备的文件描述符上创建新的密码学会话；即一个特定于 `sessp` 中指定的保密算法、完整性算法和密钥的持久对象。保密或完整性任一方的特殊值 0 保留用于表示该会话不需要相应的操作（保密或完整性）。ETA 会话同时指定保密和完整性算法。AEAD 会话仅指定保密算法。多个会话可绑定到单个文件描述符。在 `sessp-ses` 中返回的会话 ID 在后续加密或哈希请求中作为 `crypt_op` 操作结构的必填字段提供。对于非零保密算法，必须在 `sessp-cipher` 中指定保密算法，在 `sessp-keylen` 中指定密钥长度，在 `sessp-key` 所寻址的字节中指定密钥值。对于带密钥的单向哈希算法，必须在 `sessp-mac` 中指定单向哈希，在 `sessp-mackey` 中指定密钥长度，在 `sessp-mackeylen` 所寻址的字节中指定密钥值。是否支持特定的融合保密和完整性校验算法组合，取决于底层硬件是否支持该组合。并非所有硬件都支持所有组合，即使硬件支持每种操作作为独立的非融合操作。

**`CIOCGSESSION2`** `struct session2_op *sessp` 此请求类似于 CIOGSESSION，但增加了额外字段。`sessp-crid` 请求特定的加密设备或一类设备（软件还是硬件）。`sessp-ivlen` 指定每次请求提供的 IV 或 nonce 的长度。如果此字段设为零，则使用默认的 IV 或 nonce 长度。`sessp-maclen` 指定每次请求提供或计算的 MAC 或认证标签的长度。如果此字段设为零，则使用完整的 MAC。`sessp-pad` 字段必须初始化为零。

**`CIOCCRYPT`** `struct crypt_op *cr_op` 请求加密/解密（或哈希）操作。要加密，将 `cr_op-op` 设为 `COP_ENCRYPT`。要解密，将 `cr_op-op` 设为 `COP_DECRYPT`。`cr_op-len` 字段提供输入缓冲区的长度；`cr_op-src`、`cr_op-dst`、`cr_op-mac`、`cr_op-iv` 字段分别提供输入缓冲区、输出缓冲区、单向哈希和初始化向量的地址。如果会话使用了融合的先加密后认证或 AEAD 算法，则解密操作需要将关联哈希作为输入。如果哈希不正确，操作将以 `EBADMSG` 失败，输出缓冲区保持不变。

**`CIOCCRYPTAEAD`** `struct crypt_aead *cr_aead` `CIOCCRYPTAEAD` 类似于 `CIOCCRYPT`，但在 `cr_aead-aad` 中提供了附加数据以包含在认证模式中。

**`CIOCFSESSION`** `u_int32_t ses_id` 销毁由 `ses_id` 标识的会话。

## 参见

[aesni(4)](aesni.4.md), [armv8crypto(4)](armv8crypto.4.aarch64.md), [ccr(4)](ccr.4.md), [glxsb(4)](glxsb.4.i386.md), [ipsec(4)](ipsec.4.md), [padlock(4)](padlock.4.md), [qat(4)](qat.4.md), [qat_c2xxx(4)](qat_c2xxx.4.md), [safe(4)](safe.4.md), [safexcel(4)](safexcel.4.md), [crypto(7)](../man7/crypto.7.md), geli(8), [crypto(9)](../man9/crypto.9.md)

## 历史

`cryptodev` 驱动首次出现于 OpenBSD 3.0。`cryptodev` 驱动被引入 FreeBSD 5.0。

## 缺陷

错误检查和报告较为薄弱。

为 `CIOCGSESSION` 指定的对称密钥大小值必须与 opencrypto(9) 期望的值完全匹配。提供给 `CIOCCRYPT` 的输出缓冲区和 MAC 缓冲区必须与会话是否指定了保密或完整性算法相匹配：如果请求了非 `NULL` 算法，则必须提供大小合适的缓冲区。
