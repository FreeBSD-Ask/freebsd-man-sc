# rijndael.9

`rijndael_makeKey` — AES 加密

## 名称

`rijndael_makeKey`, `rijndael_cipherInit`, `rijndael_blockEncrypt`, `rijndael_padEncrypt`, `rijndael_blockDecrypt`, `rijndael_padDecrypt`

## 概要

```c
#include <sys/types.h>
```

```c
#include <crypto/rijndael.h>
```

```c
int
rijndael_makeKey(keyInstance *key, uint8_t direction, int keyLen, char *keyMaterial)

int
rijndael_cipherInit(cipherInstance *cipher, uint8_t mode, char *IV)

int
rijndael_blockEncrypt(cipherInstance *cipher, keyInstance *key, uint8_t *input, int inputLen, uint8_t *outBuffer)

int
rijndael_padEncrypt(cipherInstance *cipher, keyInstance *key, uint8_t *input, int inputOctets, uint8_t *outBuffer)

int
rijndael_blockDecrypt(cipherInstance *cipher, keyInstance *key, uint8_t *input, int inputLen, uint8_t *outBuffer)

int
rijndael_padDecrypt(cipherInstance *cipher, keyInstance *key, uint8_t *input, int inputOctets, uint8_t *outBuffer)
```

## 描述

`rijndael_makeKey` 函数用于在 `key` 中设置密钥调度。`direction`（可以是 `DIR_ENCRYPT` 或 `DIR_DECRYPT`）指定密钥的预期用途。密钥的长度（以位为单位）由 `keyLen` 给出，必须为 128、192 或 256。实际密钥在 `keyMaterial` 所指向的缓冲区中提供。此材料可以是原始二进制数据，或包含原始二进制数据十六进制表示的 ASCII 字符串，取决于 `rijndael_padDecrypt` 源代码中的编译时选项 `BINARY_KEY_MATERIAL`。

## 返回值

`rijndael_makeKey` 函数在传入 `NULL` `key` 时返回 `BAD_KEY_INSTANCE`，如果 `direction` 不是 `DIR_ENCRYPT` 或 `DIR_DECRYPT` 则返回 `BAD_KEY_DIR`，如果密钥材料不是十六进制字符串（且未设置二进制密钥）则返回 `BAD_KEY_MAT`，否则返回 `TRUE`。

## 作者

Mark V Murray
