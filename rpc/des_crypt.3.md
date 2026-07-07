# des_crypt(3)

`des_crypt` — 快速 DES 加密

## 名称

`des_crypt`

## 库

Lb libc

## 概要

`#include <rpc/des_crypt.h>`

```c
int
ecb_crypt(char *key, char *data, unsigned datalen, unsigned mode);

int
cbc_crypt(char *key, char *data, unsigned datalen, unsigned mode,
    char *ivec);

void
des_setparity(char *key);
```

## 描述

`ecb_crypt` 和 `cbc_crypt` 函数实现了 NBS DES（数据加密标准）。这些例程比 crypt(3) 更快且更通用。如果 DES 硬件可用，它们还能利用硬件加速。`ecb_crypt` 函数以 ECB（电子密码本）模式加密，该模式独立地加密各数据块。`cbc_crypt` 函数以 CBC（密码块链接）模式加密，该模式将连续的数据块链接在一起。CBC 模式可防止数据块的插入、删除和替换。此外，明文中的规律性不会出现在密文中。

以下是这些例程的使用方法。第一个参数 `key` 是带奇偶校验的 8 字节加密密钥。要设置密钥的奇偶校验位（对于 DES 位于每个字节的低位），使用 `des_setparity`。第二个参数 `data` 包含要加密或解密的数据。第三个参数 `datalen` 是 `data` 的字节长度，必须是 8 的倍数。第四个参数 `mode` 由若干值通过 *OR* 运算组合而成。对于加密方向，*OR* 入 `DES_ENCRYPT` 或 `DES_DECRYPT`。对于软件加密还是硬件加密，*OR* 入 `DES_HW` 或 `DES_SW`。如果指定了 `DES_HW` 但没有硬件，则加密在软件中执行，例程返回 `DESERR_NOHWDEVICE`。对于 `cbc_crypt`，`ivec` 参数是用于链接的 8 字节初始化向量。返回时它会被更新为下一个初始化向量。

## 错误

**`[DESERR_NONE]`** 无错误。

**`[DESERR_NOHWDEVICE]`** 加密成功，但在软件中而非所请求的硬件中完成。

**`[DESERR_HWERROR]`** 硬件或驱动程序中发生错误。

**`[DESERR_BADPARAM]`** 传递给例程的参数错误。

给定结果状态 `stat`，宏 `DES_FAILED(stat)` 仅在前两种状态下为假。

## 参见

crypt(3)

## 限制

这些例程在 RPCSRC 4.0 中不可用。提供此信息是为了描述 Secure RPC 所期望的 DES 接口。
